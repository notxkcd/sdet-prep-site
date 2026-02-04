#!/usr/bin/env python3
import os
import re
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

# Earthy Colors
ACCENT = "#556b2f"
TEXT = "#2d2a26"

console = Console()
BASE_DIR = "content"

def find_started_items():
    started_items = []
    
    # Recursively walk through content directory
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file == "_index.md":
                filepath = os.path.join(root, file)
                category = os.path.basename(root).replace("-", " ").title()
                
                with open(filepath, 'r') as f:
                    lines = f.readlines()
                
                for line in lines:
                    # Match started rows: | ID | [Name](Link) | [-] |
                    match = re.search(r'^\s*\|\s*([0-9]+)\s*\|(.*)\|\s*\[-\]\s*\|\s*$', line.strip())
                    if match:
                        row_id = match.group(1).strip()
                        middle = match.group(2)
                        
                        link_match = re.search(r'\[([^\]]+)\]\(([^)]+)\)', middle)
                        item_name = link_match.group(1) if link_match else "Item"
                        
                        started_items.append({
                            "category": category,
                            "name": item_name,
                            "id": row_id
                        })
    return started_items

def main():
    console.clear()
    console.print(Panel(f"[bold {ACCENT}]Current Focus[/bold {ACCENT}] - Active Tasks", box=box.ROUNDED))
    
    started = find_started_items()
    
    if not started:
        console.print("\n[dim]No tasks currently in progress. Start one by drilling down in 'make check'![/dim]")
        return

    table = Table(box=box.SIMPLE, header_style=f"bold {ACCENT}", border_style=ACCENT, expand=True)
    table.add_column("Category", style="italic", width=20)
    table.add_column("ID", justify="right", width=4)
    table.add_column("Started Task", ratio=1, style="bold")

    for item in started:
        table.add_row(item['category'], item['id'], item['name'])
    
    console.print(table)
    console.print(f"\n[bold yellow]! Total Active Fronts:[/bold yellow] {len(started)}")

if __name__ == "__main__":
    main()
