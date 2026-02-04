#!/usr/bin/env python3
import os
import re
import sys
import tty
import termios
import time
from datetime import datetime
from rich.console import Console, Group
from rich.table import Table
from rich.panel import Panel
from rich.live import Live
from rich.text import Text
from rich import box

# Earthy Colors
ACCENT = "#556b2f"
TEXT = "#2d2a26"

console = Console()

class TableManager:
    def __init__(self, initial_file):
        self.file_stack = []
        self.cursor_stack = []
        self.current_file = os.path.abspath(initial_file)
        self.cursor_idx = 0
        self.all_items = []
        self.filtered_items = []
        self.lines = []
        self.title = ""
        self.search_query = ""
        self.search_mode = False
        self.message = ""

    def load_current(self):
        if not os.path.exists(self.current_file):
            return False
        
        with open(self.current_file, 'r') as f:
            self.lines = f.readlines()
        
        self.all_items = []
        self.title = os.path.basename(os.path.dirname(self.current_file)).replace("-", " ").title()
        if not self.title or self.title == "Content":
            self.title = "Main Index"

        for i, line in enumerate(self.lines):
            # Regex captures: | ID | ... | [Link](Path) | ... | [status] |
            match = re.search(r'^\s*\|\s*([0-9]+)\s*\|(.*)\|\s*\[([ xX\-])\]\s*\|\s*$', line.strip())
            if match:
                row_id = match.group(1).strip()
                middle = match.group(2)
                status_char = match.group(3).lower()
                
                link_match = re.search(r'\[([^\]]+)\]\(([^)]+)\)', middle)
                link_name = link_match.group(1) if link_match else "Item"
                link_path = link_match.group(2) if link_match else None
                
                self.all_items.append({
                    "line_index": i,
                    "id": row_id,
                    "name": link_name,
                    "link": link_path,
                    "status": status_char
                })
        
        self.apply_filter()
        return len(self.all_items) > 0

    def apply_filter(self):
        if not self.search_query:
            self.filtered_items = self.all_items
        else:
            query = self.search_query.lower()
            self.filtered_items = [
                item for item in self.all_items 
                if query in item['name'].lower() or query in item['id']
            ]
        if self.cursor_idx >= len(self.filtered_items):
            self.cursor_idx = max(0, len(self.filtered_items) - 1)

    def calculate_folder_status(self):
        if not self.all_items: return " "
        done_count = sum(1 for item in self.all_items if item['status'] == 'x')
        if done_count == len(self.all_items): return "x"
        elif done_count > 0 or any(item['status'] == '-' for item in self.all_items): return "-"
        else: return " "

    def propagate_up(self):
        if not self.file_stack: return
        current_status = self.calculate_folder_status()
        parent_file = self.file_stack[-1]
        parent_line_idx = self.cursor_stack[-1][1]

        with open(parent_file, 'r') as f:
            p_lines = f.readlines()

        line = p_lines[parent_line_idx]
        p_lines[parent_line_idx] = re.sub(r'\[([ xX\-])\](\s*\|\s*)$', fr'[{current_status}]\2', line.rstrip()) + "\n"

        with open(parent_file, 'w') as f:
            f.writelines(p_lines)

    def drill_down(self):
        if not self.filtered_items: return False
        item = self.filtered_items[self.cursor_idx]
        if not item['link']: return False

        base_dir = os.path.dirname(self.current_file)
        target_path = item['link'].strip("/")
        new_path = os.path.abspath(os.path.join(base_dir, target_path))
        
        if os.path.isdir(new_path): potential_file = os.path.join(new_path, "_index.md")
        else: potential_file = new_path + ".md"

        if os.path.exists(potential_file):
            # Save parent state
            self.file_stack.append(self.current_file)
            self.cursor_stack.append((self.cursor_idx, item['line_index'], self.search_query))
            
            # Switch to new file
            old_file = self.current_file
            self.current_file = potential_file
            self.cursor_idx = 0
            self.search_query = ""
            self.search_mode = False
            
            if not self.load_current():
                # NO TABLE FOUND - Show message and go back
                self.message = f"Info: '{item['name']}' is a content file (no sub-tasks)."
                self.go_back()
                return False
            return True
        return False

    def go_back(self):
        if self.file_stack:
            self.propagate_up()
            self.current_file = self.file_stack.pop()
            saved_cursor, _, saved_query = self.cursor_stack.pop()
            self.cursor_idx = saved_cursor
            self.search_query = saved_query
            self.load_current()
            return True
        return False

    def toggle(self):
        if not self.filtered_items: return
        item = self.filtered_items[self.cursor_idx]
        line = self.lines[item['line_index']]
        
        new_char = " " if item['status'] == 'x' else "x"
        self.lines[item['line_index']] = re.sub(r'\[([ xX\-])\](\s*\|\s*)$', fr'[{new_char}]\2', line.rstrip()) + "\n"
        
        self.save()
        self.load_current()
        self.propagate_up()

    def save(self):
        with open(self.current_file, 'w') as f:
            f.writelines(self.lines)

def get_char():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
        if ch == '\x1b': ch += sys.stdin.read(2)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def generate_view(manager):
    term_height = console.height
    visible_rows = term_height - 14
    if visible_rows < 5: visible_rows = 5
    
    items = manager.filtered_items
    total_items = len(items)
    
    if total_items > 0:
        start_idx = max(0, manager.cursor_idx - visible_rows // 2)
        end_idx = min(total_items, start_idx + visible_rows)
        if end_idx == total_items: start_idx = max(0, end_idx - visible_rows)
    else: start_idx, end_idx = 0, 0

    table = Table(box=box.SIMPLE, header_style=f"bold {ACCENT}", border_style=ACCENT, expand=True)
    table.add_column(" ", width=2)
    table.add_column("Status", justify="center", width=12)
    display_title = f"Manager: {manager.title}"
    if total_items > 0: display_title += f" ({manager.cursor_idx + 1}/{total_items})"
    table.add_column(display_title, ratio=1)

    for i in range(start_idx, end_idx):
        item = items[i]
        pointer = f"[bold {ACCENT}]>[/bold {ACCENT}]" if i == manager.cursor_idx else " "
        
        if item['status'] == 'x': status = "[bold green]SOLVED[/bold green]"; name_style = "[strike dim]"
        elif item['status'] == '-': status = "[bold yellow]STARTED[/bold yellow]"; name_style = "[bold]"
        else: status = "[dim]PENDING[/dim]"; name_style = ""
            
        row_style = f"bold {TEXT} on #e8eade" if i == manager.cursor_idx else ""
        table.add_row(pointer, status, f"{name_style}{item['name']}", style=row_style)
    
    content = []
    if manager.message:
        content.append(Panel(f"[bold yellow]{manager.message}[/bold yellow]", border_style="yellow", box=box.ROUNDED))
        manager.message = "" # Clear after display

    if manager.search_mode:
        search_text = Text(" Search: ", style="bold")
        search_text.append(manager.search_query, style=f"bold {ACCENT}")
        search_text.append("_", style="blink")
        content.append(Panel(search_text, border_style=ACCENT, box=box.ROUNDED))
    
    content.append(table)
    footer = "[dim]j/k: Move | l/Ent: In | h/Bksp: Out | Space: Toggle | /: Search | q: Quit[/dim]"
    return Panel(Group(*content), subtitle=footer, border_style=ACCENT, title="[bold]SDET Prep Tracker[/bold]")

def main():
    if len(sys.argv) < 2: return
    manager = TableManager(sys.argv[1])
    if not manager.load_current(): return

    with Live(generate_view(manager), console=console, screen=True, auto_refresh=False) as live:
        while True:
            live.update(generate_view(manager), refresh=True)
            key = get_char()
            
            if manager.search_mode:
                if key in ('\r', '\x1b'): manager.search_mode = False
                elif key in ('\x7f', '\x08'): 
                    manager.search_query = manager.search_query[:-1]
                    manager.apply_filter()
                elif len(key) == 1 and key.isprintable():
                    manager.search_query += key
                    manager.apply_filter()
                continue

            if key in ('k', '\x1b[A'):
                if manager.filtered_items: manager.cursor_idx = (manager.cursor_idx - 1) % len(manager.filtered_items)
            elif key in ('j', '\x1b[B'):
                if manager.filtered_items: manager.cursor_idx = (manager.cursor_idx + 1) % len(manager.filtered_items)
            elif key == ' ': manager.toggle()
            elif key == '/': manager.search_mode = True
            elif key in ('l', '\r'): manager.drill_down()
            elif key in ('h', '\x7f', '\x08'):
                if not manager.go_back(): break
            elif key.lower() == 'q' or key == '\x03':
                manager.propagate_up()
                break

if __name__ == "__main__":
    try:
        main()
        console.print(f"\n[bold {ACCENT}]✔ System Synced.[/bold {ACCENT}] All parent statuses updated.")
    except KeyboardInterrupt: pass