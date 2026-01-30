import re
import os

def convert_list_to_table(file_path):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    with open(file_path, 'r') as f:
        lines = f.readlines()

    header = []
    list_items = []
    
    # Simple parser to find list items
    for line in lines:
        if line.strip().startswith('-'):
            list_items.append(line)
        elif not list_items:
            header.append(line)

    new_content = "".join(header)
    new_content += "| ID | Companies | Status |\n| :--- | :--- | :---: |\n"

    for i, line in enumerate(list_items, 1):
        # Extract link: [Text](Link)
        match = re.search(r'\[([^\]]+)\]\(([^)]+)\)', line)
        if match:
            name = match.group(1)
            link = match.group(2)
            # Use [x] if it was already checked, else [ ]
            status = "[x]" if "[x]" in line else "[ ]"
            new_content += f"| {i:02d} | [{name}]({link}) | {status} |\n"

    with open(file_path, 'w') as f:
        f.write(new_content)
    print(f"Table created in {file_path}")

if __name__ == "__main__":
    convert_list_to_table('content/12_company_based_questions/_index.md')
