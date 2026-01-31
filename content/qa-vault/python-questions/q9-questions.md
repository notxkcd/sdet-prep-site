---
title: "Questions - Aiite Q Dump -Set_5"
date: 2026-01-30
draft: false
---

# Python Programming Interview Questions (Sorted by Difficulty) - Aiite Q Dump -Set_5.txt

## Beginner (Basics)
- [Write a program to reverse a string.](#write-a-program-to-reverse-a-string)
- [Write a program to find even and odd numbers in a given list.](#write-a-program-to-find-even-and-odd-numbers-in-a-given-list)
- [Swap two numbers with and without using a third variable.](#swap-two-numbers-with-and-without-using-a-third-variable)

## Intermediate (Intermediate Logic)
- [Write a program to count the occurrences of a specific character (e.g., 'a') in a given string.](#write-a-program-to-count-the-occurrences-of-a-specific-character-eg-a-in-a-given-string)
- [Write a program to count the number of words in a given sentence.](#write-a-program-to-count-the-number-of-words-in-a-given-sentence)
- [Swap two strings without using a temporary variable.](#swap-two-strings-without-using-a-temporary-variable)
- [Write a program to remove duplicate elements from a list.](#write-a-program-to-remove-duplicate-elements-from-a-list)

---

# Answers

## Beginner (Basics)

### <a id="write-a-program-to-reverse-a-string"></a>Write a program to reverse a string.
```python
s = "hello"
print(s[::-1]) # "olleh"
```
[Back to Top](#beginner-basics)

### <a id="write-a-program-to-find-even-and-odd-numbers-in-a-given-list"></a>Write a program to find even and odd numbers in a given list.
```python
lst = [1, 2, 3, 4, 5]
evens = [x for x in lst if x % 2 == 0]
odds = [x for x in lst if x % 2 != 0]
print("Evens:", evens) # [2, 4]
print("Odds:", odds) # [1, 3, 5]
```
[Back to Top](#beginner-basics)

### <a id="swap-two-numbers-with-and-without-using-a-third-variable"></a>Swap two numbers with and without using a third variable.
```python
a, b = 1, 2
# With temp
temp = a; a = b; b = temp
print(a, b) # 2 1
# Without temp
a, b = b, a
print(a, b) # 1 2
```
[Back to Top](#beginner-basics)

## Intermediate (Intermediate Logic)

### <a id="write-a-program-to-count-the-occurrences-of-a-specific-character-eg-a-in-a-given-string"></a>Write a program to count the occurrences of a specific character (e.g., 'a') in a given string.
```python
s = "banana"
print(s.count('a')) # 3
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="write-a-program-to-count-the-number-of-words-in-a-given-sentence"></a>Write a program to count the number of words in a given sentence.
```python
s = "Hello world from Python"
print(len(s.split())) # 4
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="swap-two-strings-without-using-a-temporary-variable"></a>Swap two strings without using a temporary variable.
```python
s1, s2 = "Hello", "World"
s1, s2 = s2, s1
print(s1, s2) # "World" "Hello"
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="write-a-program-to-remove-duplicate-elements-from-a-list"></a>Write a program to remove duplicate elements from a list.
```python
lst = [1, 2, 2, 3]
print(list(set(lst))) # [1, 2, 3]
```
[Back to Top](#intermediate-intermediate-logic)