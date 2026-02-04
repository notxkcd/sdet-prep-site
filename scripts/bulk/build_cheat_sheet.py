import re

def get_questions():
    with open('ultimate-questions-cheatsheet/400-Java.md', 'r') as f:
        content = f.read()
    return re.findall(r'^(\d+)\)\s*(.*?)(?=\n|$)', content, re.MULTILINE)

questions = get_questions()

with open('ultimate-questions-cheatsheet/Java-Ultimate-Cheat-Sheet.md', 'w') as f:
    f.write("---\ntitle: Ultimate Java 21 Interview Questions (400+)\n---\n\n")
    f.write("# Table of Contents\n\n")
    for num, q_text in questions:
        slug = f"q{num}"
        f.write(f"{num}. <a name=\"{slug}-toc\"></a>[{q_text.strip()}](#{slug})\n")
    f.write("\n---\n\n# Answers\n\n")

