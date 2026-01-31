---
title: "Questions - AiiTE Q Dump-Set_8_Update"
date: 2026-01-30
draft: false
---

# Python Programming Interview Questions (Sorted by Difficulty) - AiiTE Q Dump-Set_8_Update.txt

## Beginner
- [Write a Palindrome program.](#write-a-palindrome-program)

## Intermediate
- [Input: `list = [1,0,0,2,0,0,0,3]`, Output: `[1,2,3,0,0,0]`. (Moving non-zero elements to the front).](#input-list--10020003-output-123000-moving-non-zero-elements-to-the-front)

---

# Answers

## Beginner

### <a id="write-a-palindrome-program"></a>Write a Palindrome program.
```python
s = "madam"
print(s == s[::-1]) # True
```
[Back to Top](#beginner)

## Intermediate

### <a id="input-list--10020003-output-123000-moving-non-zero-elements-to-the-front"></a>Input: `list = [1,0,0,2,0,0,0,3]`, Output: `[1,2,3,0,0,0]`. (Moving non-zero elements to the front).
```python
lst = [1, 0, 0, 2, 0, 0, 0, 3]
non_zeros = [x for x in lst if x != 0]
zeros = [x for x in lst if x == 0]
result = non_zeros + zeros
print(result) # [1, 2, 3, 0, 0, 0, 0, 0]
```
[Back to Top](#intermediate)