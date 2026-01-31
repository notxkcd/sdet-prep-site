---
title: "Questions - Aiite Q Dump - Set_4"
date: 2026-01-30
draft: false
---

# Python Programming Interview Questions (Sorted by Difficulty) - Aiite Q Dump - Set_4.txt

## Beginner (Basics)
- [Write a program to reverse a string (Generic).](#write-a-program-to-reverse-a-string-generic)
- [Reverse a string using a loop and using an inbuilt function (slicing).](#reverse-a-string-using-a-loop-and-using-an-inbuilt-function-slicing)
- [Print the first 3 characters of a string.](#print-the-first-3-characters-of-a-string)
- [Find the minimum and maximum value in a list.](#find-the-minimum-and-maximum-value-in-a-list)

## Intermediate (Intermediate Logic)
- [Manipulate a string: write your name, print its length, add characters, and then print the name/length multiple times.](#manipulate-a-string-write-your-name-print-its-length-add-characters-and-then-print-the-namelength-multiple-times)
- [Input: `abc`, Output: `aabbcc`.](#input-abc-output-aabbcc)

## Advanced (Advanced Algorithms & Logic)
- [Find duplicate characters and unique characters in a string (Input: `weqjhjkAJKDbdnmbcnm`).](#find-duplicate-characters-and-unique-characters-in-a-string-input-weqjhjkajkdbdnmbcnm)

---

# Answers

## Beginner (Basics)

### <a id="write-a-program-to-reverse-a-string-generic"></a>Write a program to reverse a string (Generic).
```python
s = "hello"
print(s[::-1])
```
[Back to Top](#beginner-basics)

### <a id="reverse-a-string-using-a-loop-and-using-an-inbuilt-function-slicing"></a>Reverse a string using a loop and using an inbuilt function (slicing).
```python
s = "hello"
# Loop
rev = ""
for char in s:
    rev = char + rev
print(rev)
# Inbuilt (slicing)
print(s[::-1])
```
[Back to Top](#beginner-basics)

### <a id="print-the-first-3-characters-of-a-string"></a>Print the first 3 characters of a string.
```python
s = "hello"
print(s[:3]) # "hel"
```
[Back to Top](#beginner-basics)

### <a id="find-the-minimum-and-maximum-value-in-a-list"></a>Find the minimum and maximum value in a list.
```python
lst = [1, 5, 2, 8, 3]
print(min(lst), max(lst)) # 1 8
```
[Back to Top](#beginner-basics)

## Intermediate (Intermediate Logic)

### <a id="manipulate-a-string-write-your-name-print-its-length-add-characters-and-then-print-the-namelength-multiple-times"></a>Manipulate a string: write your name, print its length, add characters, and then print the name/length multiple times.
```python
name = "John"
print(len(name))
name += " Doe"
for _ in range(3):
    print(f"{name} - {len(name)}")
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="input-abc-output-aabbcc"></a>Input: `abc`, Output: `aabbcc`.
```python
s = "abc"
print("".join([c*2 for c in s])) # "aabbcc"
```
[Back to Top](#intermediate-intermediate-logic)

## Advanced (Advanced Algorithms & Logic)

### <a id="find-duplicate-characters-and-unique-characters-in-a-string-input-weqjhjkajkdbdnmbcnm"></a>Find duplicate characters and unique characters in a string (Input: `weqjhjkAJKDbdnmbcnm`).
```python
s = "weqjhjkAJKDbdnmbcnm"
counts = {c: s.count(c) for c in set(s)}
duplicates = [c for c, count in counts.items() if count > 1]
unique = [c for c, count in counts.items() if count == 1]
print("Duplicates:", duplicates)
print("Unique:", unique)
```
[Back to Top](#advanced-advanced-algorithms--logic)