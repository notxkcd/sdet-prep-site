---
title: "Questions - Java Q_Set_1_and_2"
date: 2026-01-30
draft: false
---

# Python Programming Interview Questions (Sorted by Difficulty) - Java Q_Set_1_and_2.txt

## Intermediate
- [Write a program to convert a `Dictionary` to a `List` (of keys, values, or items).](#write-a-program-to-convert-a-dictionary-to-a-list-of-keys-values-or-items)

## Advanced
- [Write a program using a `Dictionary` to find the number of occurrences of each character in a string.](#write-a-program-using-a-dictionary-to-find-the-number-of-occurrences-of-each-character-in-a-string)

---

# Answers

## Intermediate

### <a id="write-a-program-to-convert-a-dictionary-to-a-list-of-keys-values-or-items"></a>Write a program to convert a `Dictionary` to a `List` (of keys, values, or items).
```python
d = {'a': 1, 'b': 2}
print(list(d.keys()))   # ['a', 'b']
print(list(d.values())) # [1, 2]
print(list(d.items()))  # [('a', 1), ('b', 2)]
```
[Back to Top](#intermediate)

## Advanced

### <a id="write-a-program-using-a-dictionary-to-find-the-number-of-occurrences-of-each-character-in-a-string"></a>Write a program using a `Dictionary` to find the number of occurrences of each character in a string.
```python
s = "hello world"
counts = {}
for char in s:
    counts[char] = counts.get(char, 0) + 1
print(counts)
```
[Back to Top](#advanced)