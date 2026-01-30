import os
import re

def format_questions(text):
    # Split if there's a '?' followed by a space and a capital letter
    text = re.sub(r'(\?)\s+([A-Z])', r'\1\n\2', text)
    
    lines = text.split('\n')
    new_lines = []
    
    for line in lines:
        trimmed = line.strip()
        if not trimmed:
            new_lines.append("")
            continue
        
        # Header detection logic
        is_header = (
            trimmed.endswith(':') or 
            trimmed.endswith('---') or 
            (len(trimmed) < 15 and not trimmed.endswith('?')) or
            (trimmed.startswith('*') and trimmed.endswith('*'))
        )
        
        # Check if already a list or number
        is_list = re.match(r'^[\-\*1-9]', trimmed)
        
        if is_header or is_list:
            new_lines.append(trimmed)
        else:
            # Bullet point the question
            new_lines.append(f"- {trimmed}")
            
    return "\n".join(new_lines)

def reformat_section(match):
    header = match.group(1)
    body = match.group(2)
    return header + format_questions(body)

def process_files(root_dir):
    pattern = r'(## Original Questions\n+)(.*?)(?=\n+---|\Z)'
    count = 0
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.md') and file != '_index.md':
                file_path = os.path.join(subdir, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = re.sub(pattern, reformat_section, content, flags=re.DOTALL)
                
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Formatted: {file_path}")
                    count += 1
    print(f"Total files reformatted: {count}")

if __name__ == "__main__":
    process_files('content/12_company_based_questions')
