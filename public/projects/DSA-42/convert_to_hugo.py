import os
import re
import json

def html_to_md(html):
    if not html:
        return ""
    # Simple conversion for the tags seen in the files
    md = re.sub(r'<h1>.*?</h1>', '', html) # Remove h1 content entirely as it's in front matter
    md = re.sub(r'</?p>', '\n\n', md)
    md = re.sub(r'<code>(.*?)</code>', r'`\1`', md)
    md = re.sub(r'<h3>(.*?)</h3>', r'### \1', md)
    md = re.sub(r'<h2>(.*?)</h2>', r'## \1', md)
    md = re.sub(r'<strong>(.*?)</strong>', r'**\1**', md)
    md = re.sub(r'<b>(.*?)</b>', r'**\1**', md)
    md = re.sub(r'<em>(.*?)</em>', r'*\1*', md)
    md = re.sub(r'<i>(.*?)</i>', r'*\1*', md)
    md = re.sub(r'<ul>', '\n', md)
    md = re.sub(r'</ul>', '\n', md)
    md = re.sub(r'<li>(.*?)</li>', r'- \1\n', md)
    md = re.sub(r'<ol>', '\n', md)
    md = re.sub(r'</ol>', '\n', md)
    md = re.sub(r'<li>', r'- ', md) # Fallback for nested or complex lists
    md = re.sub(r'<div class="markdown-content">', '', md)
    md = re.sub(r'<div class="explanation-fence">', '\n---\n', md)
    md = re.sub(r'</div>', '', md)
    md = re.sub(r'<br\s*/*>', '\n', md)
    md = re.sub(r'&lt;', '<', md)
    md = re.sub(r'&gt;', '>', md)
    md = re.sub(r'&amp;', '&', md)
    
    # Remove excessive leading whitespace from bullet points
    md = re.sub(r'^\s*-\s+', '- ', md, flags=re.MULTILINE)
    
    md = re.sub(r'\n\s*\n\s*\n', '\n\n', md) # Clean up multiple newlines
    return md.strip()

def extract_content(html, element_id):
    pattern = rf'<div id="{element_id}">(.*?)</div>'
    match = re.search(pattern, html, re.DOTALL)
    if match:
        content = match.group(1)
        return content.strip()
    return ""

def process_file(html_path, md_path, title):
    with open(html_path, 'r') as f:
        html = f.read()

    explanation = extract_content(html, 'explanation-content')
    expanded = extract_content(html, 'expanded-explanation-content')
    code_expl = extract_content(html, 'code-explanation-content')
    apps = extract_content(html, 'application-content')
    
    # Extract code blocks
    code_blocks = []
    code_matches = re.finditer(r'<pre data-lang="(.*?)"><code.*?>\n?(.*?)\n?</code></pre>', html, re.DOTALL)
    for match in code_matches:
        lang = match.group(1)
        code = match.group(2)
        code = code.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&').replace('&quot;', '"').replace('&#39;', "'")
        code_blocks.append((lang, code))

    md_content = f"---\ntitle: \"{title}\"\n---\n\n"
    md_content += html_to_md(explanation) + "\n\n"
    
    if expanded:
        md_content += "## How it Works\n\n"
        md_content += html_to_md(expanded) + "\n\n"
    
    if code_expl:
        md_content += "[Jump to Code Walkthrough](#code-walkthrough)\n\n"

    if code_blocks:
        md_content += "## Implementation {#implementation}\n\n"
        for lang, code in code_blocks:
            md_content += f"### {lang.capitalize()}\n\n"
            md_content += f"```{lang}\n{code}\n```\n\n"
            
    if code_expl:
        md_content += "## Code Walkthrough {#code-walkthrough}\n\n"
        md_content += "[Back to Implementation](#implementation)\n\n"
        md_content += html_to_md(code_expl) + "\n\n"
        md_content += "[Back to Implementation](#implementation)\n\n"
        
    if apps:
        md_content += "## Applications\n\n"
        md_content += html_to_md(apps) + "\n\n"

    os.makedirs(os.path.dirname(md_path), exist_ok=True)
    with open(md_path, 'w') as f:
        f.write(md_content)

def main():
    with open('script.js', 'r') as f:
        js_content = f.read()
    
    title_map = {}
    matches = re.finditer(r"title:\s*'(.*?)',\s*filePath:\s*'(.*?)'", js_content)
    for match in matches:
        title_map[match.group(2)] = match.group(1)

    structure = {} # { dir_path: { 'dirs': [subdirs], 'files': [(title, filename)] } }

    # Walk through content/ directory
    for root, dirs, files in os.walk('content'):
        rel_root = os.path.relpath(root, 'content')
        if rel_root == '.':
            rel_root = ''
        
        structure[rel_root] = {'dirs': dirs, 'files': []}
        
        for file in files:
            if file.endswith('.html'):
                html_path = os.path.join(root, file)
                norm_path = html_path.replace('\\', '/')
                title = title_map.get(norm_path, file.replace('.html', '').replace('_', ' ').title())
                
                md_filename = file.replace('.html', '.md')
                md_path = os.path.join('dsa-42', rel_root, md_filename)

                process_file(html_path, md_path, title)
                structure[rel_root]['files'].append((title, md_filename))
                print(f"Processed: {html_path} -> {md_path}")

    # Create _index.md for each directory
    for rel_dir, content in structure.items():
        dir_title = os.path.basename(rel_dir).replace('_', ' ').title() if rel_dir else "Content"
        
        index_md = f"---\ntitle: \"{dir_title}\"\n---\n\n"
        
        if content['dirs']:
            index_md += "### Categories\n\n"
            for d in sorted(content['dirs']):
                d_title = d.replace('_', ' ').title()
                index_md += f"- [{d_title}]({d}/)\n"
            index_md += "\n"
            
        if content['files']:
            index_md += "### Articles\n\n"
            # Sort files by title
            for title, filename in sorted(content['files']):
                # Hugo links usually don't need .md extension
                link_name = filename.replace('.md', '')
                index_md += f"- [{title}]({link_name})\n"
        
        section_path = os.path.join('dsa-42', rel_dir, '_index.md')
        os.makedirs(os.path.dirname(section_path), exist_ok=True)
        with open(section_path, 'w') as f:
            f.write(index_md)
        print(f"Generated _index.md for: {rel_dir}")

    # Handle root index.html specially
    if os.path.exists('index.html'):
        with open('index.html', 'r') as f:
            index_html = f.read()
        
        index_md = "---\ntitle: \"42 Algorithms & 42 Data Structures\"\ntype: \"home\"\ncategory: \"DSA\"\n---\n\n"
        header_match = re.search(r'<header>(.*?)</header>', index_html, re.DOTALL)
        if header_match:
            index_md += html_to_md(header_match.group(1)) + "\n\n"
        
        index_md += "## Explore\n\n"
        if '' in structure:
            for d in sorted(structure['']['dirs']):
                d_title = d.replace('_', ' ').title()
                index_md += f"- [{d_title}]({d}/)\n"

        with open('dsa-42/_index.md', 'w') as f:
            f.write(index_md)
        print("Processed: index.html -> dsa-42/_index.md")

if __name__ == "__main__":
    main()