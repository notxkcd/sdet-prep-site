---
title: "Questions - Aiite Q Dump - Set_2"
date: 2026-01-30
draft: false
---

# Python Programming Interview Questions (Sorted by Difficulty) - Aiite Q Dump - Set_2.txt

## Beginner (Basics)
- [Reverse a string.](#reverse-a-string)
- [Reverse an integer number.](#reverse-an-integer-number)
- [Count vowels in a string (e.g., "welcome").](#count-vowels-in-a-string-eg-welcome)
- [Print vowels from a string.](#print-vowels-from-a-string)
- [Find the maximum and minimum numbers in a list.](#find-the-maximum-and-minimum-numbers-in-a-list)
- [Swap two numbers without using a third variable.](#swap-two-numbers-without-using-a-third-variable)
- [Find the count of letters in a string (Input: " Hello ").](#find-the-count-of-letters-in-a-string-input-hello-)
- [Replace '-' with '/' in a date string (Input: "03-06-1995").](#replace---with--in-a-date-string-input-03-06-1995)
- [How to get system date and time?](#how-to-get-system-date-and-time)
- [Convert a string to an integer (Input: "123456").](#convert-a-string-to-an-integer-input-123456)
- [Get all elements from a list using a loop.](#get-all-elements-from-a-list-using-a-loop)

## Intermediate (Intermediate Logic)
- [Reverse a string word by word.](#reverse-a-string-word-by-word)
- [Count duplicate characters in a string.](#count-duplicate-characters-in-a-string)
- [Find the frequency of characters in a string.](#find-the-frequency-of-characters-in-a-string)
- [Find duplicate words in a string (e.g., "Hexaware").](#find-duplicate-words-in-a-string-eg-hexaware)
- [Reverse two numbers without using a temporary variable (Input: `x = 10`, `y = 20`).](#reverse-two-numbers-without-using-a-temporary-variable-input-x--10-y--20)
- [Reverse two strings without using a temporary variable (Input: `a = "India"`, `b = "uk"`).](#reverse-two-strings-without-using-a-temporary-variable-input-a--india-b--uk)
- [Find the second highest number in a list.](#find-the-second-highest-number-in-a-list)
- [Find duplicate elements in a list.](#find-duplicate-elements-in-a-list)
- [Sort a list.](#sort-a-list)
- [Convert a list to a set or tuple.](#convert-a-list-to-a-set-or-tuple)
- [Retrieve key-value pairs from a `Dictionary` (Input: `X = "A", Y = "B"`).](#retrieve-key-value-pairs-from-a-dictionary-input-x--a-y--b)
- [Write a class for Username and Password.](#write-a-class-for-username-and-password)

## Advanced (Advanced Algorithms & Logic)
- [Reverse a string word by word but keep word position.](#reverse-a-string-word-by-word-but-keep-word-position)
- [Find repeated characters in the word "ASSASINATION".](#find-repeated-characters-in-the-word-assasination)
- [Remove duplicates from a string without using collection concepts.](#remove-duplicates-from-a-string-without-using-collection-concepts)
- [Anagram check: Determine if two string patterns are the same (e.g., "CAT" and "ACT").](#anagram-check-determine-if-two-string-patterns-are-the-same-eg-cat-and-act)
- [Count characters, numbers, and special characters in a mixed string.](#count-characters-numbers-and-special-characters-in-a-mixed-string)
- [Find the 3rd maximum element in a list.](#find-the-3rd-maximum-element-in-a-list)
- [Sum of two integer lists.](#sum-of-two-integer-lists)
- [Find common duplicates between two lists.](#find-common-duplicates-between-two-lists)
- [Logic to connect to a database.](#logic-to-connect-to-a-database)

---

# Answers

## Beginner (Basics)

### <a id="reverse-a-string"></a>Reverse a string.
```python
s = "hello"
print(s[::-1]) # "olleh"
```
[Back to Top](#beginner-basics)

### <a id="reverse-an-integer-number"></a>Reverse an integer number.
```python
num = 123
print(int(str(num)[::-1])) # 321
```
[Back to Top](#beginner-basics)

### <a id="count-vowels-in-a-string-eg-welcome"></a>Count vowels in a string (e.g., "welcome").
```python
s = "welcome"
print(sum(1 for c in s if c.lower() in 'aeiou')) # 3
```
[Back to Top](#beginner-basics)

### <a id="print-vowels-from-a-string"></a>Print vowels from a string.
```python
s = "welcome"
print("".join([c for c in s if c.lower() in 'aeiou'])) # "eoe"
```
[Back to Top](#beginner-basics)

### <a id="find-the-maximum-and-minimum-numbers-in-a-list"></a>Find the maximum and minimum numbers in a list.
```python
lst = [1, 5, 2, 8, 3]
print(max(lst), min(lst)) # 8 1
```
[Back to Top](#beginner-basics)

### <a id="swap-two-numbers-without-using-a-third-variable"></a>Swap two numbers without using a third variable.
```python
a, b = 5, 10
a, b = b, a
print(a, b) # 10 5
```
[Back to Top](#beginner-basics)

### <a id="find-the-count-of-letters-in-a-string-input-hello-"></a>Find the count of letters in a string (Input: " Hello ").
```python
s = " Hello "
print(len(s.strip())) # 5
```
[Back to Top](#beginner-basics)

### <a id="replace---with--in-a-date-string-input-03-06-1995"></a>Replace '-' with '/' in a date string (Input: "03-06-1995").
```python
date = "03-06-1995"
print(date.replace('-', '/')) # "03/06/1995"
```
[Back to Top](#beginner-basics)

### <a id="how-to-get-system-date-and-time"></a>How to get system date and time?
```python
import datetime
print(datetime.datetime.now())
```
[Back to Top](#beginner-basics)

### <a id="convert-a-string-to-an-integer-input-123456"></a>Convert a string to an integer (Input: "123456").
```python
s = "123456"
print(int(s)) # 123456
```
[Back to Top](#beginner-basics)

### <a id="get-all-elements-from-a-list-using-a-loop"></a>Get all elements from a list using a loop.
```python
lst = [1, 2, 3]
for item in lst:
    print(item)
```
[Back to Top](#beginner-basics)

## Intermediate (Intermediate Logic)

### <a id="reverse-a-string-word-by-word"></a>Reverse a string word by word.
```python
s = "Hello World"
print(" ".join(s.split()[::-1])) # "World Hello"
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="count-duplicate-characters-in-a-string"></a>Count duplicate characters in a string.
```python
s = "hello"
counts = {c: s.count(c) for c in set(s) if s.count(c) > 1}
print(len(counts)) # 1
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="find-the-frequency-of-characters-in-a-string"></a>Find the frequency of characters in a string.
```python
s = "hello"
print({c: s.count(c) for c in set(s)})
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="find-duplicate-words-in-a-string-eg-hexaware"></a>Find duplicate words in a string (e.g., "Hexaware").
```python
s = "Hexaware Hexaware"
words = s.split()
duplicates = set([w for w in words if words.count(w) > 1])
print(duplicates) # {'Hexaware'}
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="reverse-two-numbers-without-using-a-temporary-variable-input-x--10-y--20"></a>Reverse two numbers without using a temporary variable (Input: `x = 10`, `y = 20`).
```python
x, y = 10, 20
x, y = y, x
print(x, y) # 20 10
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="reverse-two-strings-without-using-a-temporary-variable-input-a--india-b--uk"></a>Reverse two strings without using a temporary variable (Input: `a = "India"`, `b = "uk"`).
```python
a, b = "India", "uk"
a, b = b, a
print(a, b) # "uk" "India"
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="find-the-second-highest-number-in-a-list"></a>Find the second highest number in a list.
```python
lst = [10, 20, 30, 20]
print(sorted(list(set(lst)))[-2]) # 20
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="find-duplicate-elements-in-a-list"></a>Find duplicate elements in a list.
```python
lst = [1, 2, 3, 2, 1]
print(list(set([x for x in lst if lst.count(x) > 1]))) # [1, 2]
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="sort-a-list"></a>Sort a list.
```python
lst = [3, 1, 2]
lst.sort()
print(lst) # [1, 2, 3]
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="convert-a-list-to-a-set-or-tuple"></a>Convert a list to a set or tuple.
```python
lst = [1, 2, 3]
print(set(lst))
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="retrieve-key-value-pairs-from-a-dictionary-input-x--a-y--b"></a>Retrieve key-value pairs from a `Dictionary` (Input: `X = "A", Y = "B"`).
```python
d = {'X': "A", 'Y': "B"}
for k, v in d.items():
    print(f"{k}: {v}")
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="write-a-class-for-username-and-password"></a>Write a class for Username and Password.
```python
class UserCredentials:
    def __init__(self, username, password):
        self.username = username
        self.password = password
```
[Back to Top](#intermediate-intermediate-logic)

## Advanced (Advanced Algorithms & Logic)

### <a id="reverse-a-string-word-by-word-but-keep-word-position"></a>Reverse a string word by word but keep word position.
```python
s = "Hello World"
print(" ".join([w[::-1] for w in s.split()])) # "olleH dlroW"
```
[Back to Top](#advanced-advanced-algorithms--logic)

### <a id="find-repeated-characters-in-the-word-assasination"></a>Find repeated characters in the word "ASSASINATION".
```python
s = "ASSASINATION"
print([c for c in set(s) if s.count(c) > 1]) # ['S', 'A', 'N', 'I']
```
[Back to Top](#advanced-advanced-algorithms--logic)

### <a id="remove-duplicates-from-a-string-without-using-collection-concepts"></a>Remove duplicates from a string without using collection concepts.
```python
s = "hello"
unique = ""
for char in s:
    if char not in unique:
        unique += char
print(unique) # "helo"
```
[Back to Top](#advanced-advanced-algorithms--logic)

### <a id="anagram-check-determine-if-two-string-patterns-are-the-same-eg-cat-and-act"></a>Anagram check: Determine if two string patterns are the same (e.g., "CAT" and "ACT").
```python
s1, s2 = "CAT", "ACT"
print(sorted(s1) == sorted(s2)) # True
```
[Back to Top](#advanced-advanced-algorithms--logic)

### <a id="count-characters-numbers-and-special-characters-in-a-mixed-string"></a>Count characters, numbers, and special characters in a mixed string.
```python
s = "Abc@123"
chars = sum(1 for c in s if c.isalpha())
nums = sum(1 for c in s if c.isdigit())
specials = len(s) - chars - nums
print(chars, nums, specials) # 3 3 1
```
[Back to Top](#advanced-advanced-algorithms--logic)

### <a id="find-the-3rd-maximum-element-in-a-list"></a>Find the 3rd maximum element in a list.
```python
lst = [10, 20, 30, 40, 50]
print(sorted(list(set(lst)))[-3]) # 30
```
[Back to Top](#advanced-advanced-algorithms--logic)

### <a id="sum-of-two-integer-lists"></a>Sum of two integer lists.
```python
l1, l2 = [1, 2], [3, 4]
print(sum(l1 + l2)) # 10
```
[Back to Top](#advanced-advanced-algorithms--logic)

### <a id="find-common-duplicates-between-two-lists"></a>Find common duplicates between two lists.
```python
l1, l2 = [1, 2, 3], [3, 4, 5]
print(list(set(l1) & set(l2))) # [3]
```
[Back to Top](#advanced-advanced-algorithms--logic)

### <a id="logic-to-connect-to-a-database"></a>Logic to connect to a database.
```python
import sqlite3
# Example using SQLite
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS stocks (date text, trans text, symbol text, qty real, price real)''')
conn.commit()
conn.close()
```
[Back to Top](#advanced-advanced-algorithms--logic)