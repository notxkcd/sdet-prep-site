import re

with open('ultimate-questions-cheatsheet/400-Java.md', 'r') as f:
    content = f.read()

questions = re.findall(r'^(\d+)\)\s*(.*?)(?=\n|$)', content, re.MULTILINE)

print(f"---")
print(f"title: Ultimate Java Interview Questions (400+)")
print(f"---")
print(f"\n# Table of Contents\n")

for num, q_text in questions:
    slug = f"q{num}"
    print(f"{num}. <a name=\"{slug}-toc\"></a>[{q_text.strip()}](#{slug})")

print(f"\n# Answers\n")

for num, q_text in questions:
    slug = f"q{num}"
    print(f"<a name=\"{slug}\"></a>")
    print(f"### {num}) {q_text.strip()}")
    print(f"[Back to TOC](#{slug}-toc)")
    print(f"\n**Answer:**\n")
    print(f"*(Answer to be filled)*\n")
    print(f"---\n")

