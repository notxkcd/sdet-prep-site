import os
import re
import shutil

BASE_DIR = "content/12_company_based_questions"

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split('([0-9]+)', s)]

def generate_table():
    if not os.path.exists(BASE_DIR):
        print(f"Directory {BASE_DIR} not found.")
        return

    for subdir in os.listdir(BASE_DIR):
        path = os.path.join(BASE_DIR, subdir)
        if not os.path.isdir(path):
            continue

        index_file = os.path.join(path, "_index.md")
        if not os.path.exists(index_file):
            continue

        # Find all .md files excluding _index.md
        md_files = [f for f in os.listdir(path) if f.endswith(".md") and f != "_index.md"]
        if not md_files:
            continue

        # Sort files: main.md first, then others naturally
        md_files.sort(key=lambda x: (0 if x == "main.md" else 1, natural_sort_key(x)))

        # Backup existing _index.md
        backup_file = index_file + ".bak"
        if not os.path.exists(backup_file):
            shutil.copy2(index_file, backup_file)
            print(f"Backed up {index_file} to {backup_file}")

        # Read frontmatter
        with open(index_file, 'r') as f:
            content = f.read()
        
        fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        frontmatter = fm_match.group(0) if fm_match else "---"

        # Generate new content
        new_content = frontmatter + "\n\n## Interview Rounds\n\n"
        new_content += "| ID | Round | Status |\n"
        new_content += "| :--- | :--- | :---: |\n"

        for i, f in enumerate(md_files):
            # Label: remove .md, capitalize
            name = f.replace(".md", "").replace("-", " ").title()
            # Link: ./filename/ (Hugo standard)
            link = f"./{f.replace('.md', '')}/"
            
            # Check if this link was already marked as done in the old file?
            # For simplicity, we start fresh [ ] or try to preserve if possible.
            # Let's check the old content for [x] related to this link
            status = "[ ]"
            if f"[{name}]({link})" in content or f"({link})" in content:
                # This is a bit complex to preserve exactly without parsing the old list.
                # Since the user wants to convert, we'll start with [ ] and they can re-check.
                pass

            new_content += f"| {i+1:02d} | [{name}]({link}) | {status} |\n"

        with open(index_file, 'w') as f:
            f.write(new_content)
        print(f"Updated {index_file} with table.")

if __name__ == "__main__":
    generate_table()
