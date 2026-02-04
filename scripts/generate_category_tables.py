import os
import re
import shutil

BASE_DIR = "content/java-questions-bank/categorized-questions"

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

        # Sort files naturally
        md_files.sort(key=natural_sort_key)

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
        new_content = frontmatter + "\n\n## Questions\n\n"
        new_content += "| ID | Topic | Status |\n"
        new_content += "| :--- | :--- | :---: |\n"

        for i, f in enumerate(md_files):
            name = f.replace(".md", "").replace("-", " ").title()
            link = f"./{f.replace('.md', '')}/"
            status = "[ ]"
            new_content += f"| {i+1:02d} | [{name}]({link}) | {status} |\n"

        with open(index_file, 'w') as f:
            f.write(new_content)
        print(f"Updated {index_file} with table.")

if __name__ == "__main__":
    generate_table()
