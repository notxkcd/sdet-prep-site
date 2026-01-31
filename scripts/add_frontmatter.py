import os
import re

dir_path = 'content/api-from-first-principle'
for filename in os.listdir(dir_path):
    if filename.endswith('.md') and filename != '_index.md':
        filepath = os.path.join(dir_path, filename)
        with open(filepath, 'r') as f:
            content = f.read()
        
        if content.startswith('---\n'):
            continue

        # Extract title from the first H1
        title_match = re.search(r'^#\s+(.*)', content, re.MULTILINE)
        if title_match:
            title = title_match.group(1).strip()
            # Remove the H1 from content
            content = content.replace(title_match.group(0), '', 1).lstrip()
        else:
            title = filename.replace('.md', '').replace('-', ' ').title()
        
        frontmatter = f"---\ntitle: \"{title}\"\ndate: 2026-01-31\n---\n\n"
        with open(filepath, 'w') as f:
            f.write(frontmatter + content)
        print(f"Updated {filename}")
