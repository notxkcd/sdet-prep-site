---
title: "Questions - AiiTE Q Dump-Set_7"
date: 2026-01-30
draft: false
---

# Python Programming Interview Questions (Sorted by Difficulty) - AiiTE Q Dump-Set_7.txt

## Beginner (Basic Strings & Numbers)
- [Reverse a string.](#reverse-a-string)
- [Find the number of alphabets in a sentence.](#find-the-number-of-alphabets-in-a-sentence)
- [Separate numbers only from a string (Input: "09/24/2015").](#separate-numbers-only-from-a-string-input-09242015)
- [Write a Factorial program.](#write-a-factorial-program)
- [Swap two variables without using a 3rd variable.](#swap-two-variables-without-using-a-3rd-variable)
- [Star pattern program (e.g., Pyramid).](#star-pattern-program-eg-pyramid)
- [Write a program for a `list` to add elements and remove the first one.](#write-a-program-for-a-list-to-add-elements-and-remove-the-first-one)
- [Write a program that generates a `ZeroDivisionError` and handles it.](#write-a-program-that-generates-a-zerodivisionerror-and-handles-it)

## Intermediate (Intermediate Logic & Collections)
- [Reverse each word in a string (Input: "Good Girl").](#reverse-each-word-in-a-string-input-good-girl)
- [Remove duplicate words or characters from a string.](#remove-duplicate-words-or-characters-from-a-string)
- [Check if a string is a Palindrome.](#check-if-a-string-is-a-palindrome)
- [Find the second largest number in a list.](#find-the-second-largest-number-in-a-list)
- [Print descending order of a list.](#print-descending-order-of-a-list)
- [Sort a list in ascending order.](#sort-a-list-in-ascending-order)
- [Print non-repeating numbers in a list.](#print-non-repeating-numbers-in-a-list)
- [Write a program to loop through a `list` using four different methods.](#write-a-program-to-loop-through-a-list-using-four-different-methods)
- [Demonstrate the use of the `finally` keyword in a program.](#demonstrate-the-use-of-the-finally-keyword-in-a-program)

## Advanced (Algorithms & Complex Logic)
- [Count the occurrence of each character in a string.](#count-the-occurrence-of-each-character-in-a-string)
- [Find the occurrence of every character in "Welcome to Wipro".](#find-the-occurrence-of-every-character-in-welcome-to-wipro)
- [Print all possible combinations of a string (Input: "abc").](#print-all-possible-combinations-of-a-string-input-abc)
- [Demonstrate raising an exception in a function.](#demonstrate-raising-an-exception-in-a-function)

---

# Answers

## Beginner (Basic Strings & Numbers)

### <a id="reverse-a-string"></a>Reverse a string.
```python
s = "Hello"
print(s[::-1]) # "olleH"
```
[Back to Top](#beginner-basic-strings--numbers)

### <a id="find-the-number-of-alphabets-in-a-sentence"></a>Find the number of alphabets in a sentence.
```python
sentence = "Hello World 123"
count = sum(1 for c in sentence if c.isalpha())
print(count) # 10
```
[Back to Top](#beginner-basic-strings--numbers)

### <a id="separate-numbers-only-from-a-string-input-09242015"></a>Separate numbers only from a string (Input: "09/24/2015").
```python
import re
s = "09/24/2015"
numbers = re.sub(r'\D', '', s)
print(numbers) # "09242015"
```
[Back to Top](#beginner-basic-strings--numbers)

### <a id="write-a-factorial-program"></a>Write a Factorial program.
```python
import math
print(math.factorial(5)) # 120
# Or recursive:
def factorial(n):
    return 1 if n <= 1 else n * factorial(n-1)
print(factorial(5))
```
[Back to Top](#beginner-basic-strings--numbers)

### <a id="swap-two-variables-without-using-a-3rd-variable"></a>Swap two variables without using a 3rd variable.
```python
a, b = 10, 20
a, b = b, a
print(f"a: {a}, b: {b}") # a: 20, b: 10
```
[Back to Top](#beginner-basic-strings--numbers)

### <a id="star-pattern-program-eg-pyramid"></a>Star pattern program (e.g., Pyramid).
```python
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
```
[Back to Top](#beginner-basic-strings--numbers)

### <a id="write-a-program-for-a-list-to-add-elements-and-remove-the-first-one"></a>Write a program for a `list` to add elements and remove the first one.
```python
lst = [1, 2, 3]
lst.append(4)
lst.pop(0)
print(lst) # [2, 3, 4]
```
[Back to Top](#beginner-basic-strings--numbers)

### <a id="write-a-program-that-generates-a-zerodivisionerror-and-handles-it"></a>Write a program that generates a `ZeroDivisionError` and handles it.
```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Caught division by zero")
```
[Back to Top](#beginner-basic-strings--numbers)

## Intermediate (Intermediate Logic & Collections)

### <a id="reverse-each-word-in-a-string-input-good-girl"></a>Reverse each word in a string (Input: "Good Girl").
```python
s = "Good Girl"
print(" ".join([w[::-1] for w in s.split()])) # "dooG lriG"
```
[Back to Top](#intermediate-intermediate-logic--collections)

### <a id="remove-duplicate-words-or-characters-from-a-string"></a>Remove duplicate words or characters from a string.
```python
# Unique chars
s = "banana"
print("".join(sorted(set(s), key=s.index))) # "ban"

# Unique words
s = "hello world hello"
print(" ".join(sorted(set(s.split()), key=s.split().index))) # "hello world"
```
[Back to Top](#intermediate-intermediate-logic--collections)

### <a id="check-if-a-string-is-a-palindrome"></a>Check if a string is a Palindrome.
```python
s = "racecar"
print(s == s[::-1]) # True
```
[Back to Top](#intermediate-intermediate-logic--collections)

### <a id="find-the-second-largest-number-in-a-list"></a>Find the second largest number in a list.
```python
lst = [10, 5, 20, 20, 8]
print(sorted(list(set(lst)))[-2]) # 10
```
[Back to Top](#intermediate-intermediate-logic--collections)

### <a id="print-descending-order-of-a-list"></a>Print descending order of a list.
```python
lst = [1, 5, 3, 9]
print(sorted(lst, reverse=True)) # [9, 5, 3, 1]
```
[Back to Top](#intermediate-intermediate-logic--collections)

### <a id="sort-a-list-in-ascending-order"></a>Sort a list in ascending order.
```python
lst = [9, 5, 3, 1]
lst.sort()
print(lst) # [1, 3, 5, 9]
```
[Back to Top](#intermediate-intermediate-logic--collections)

### <a id="print-non-repeating-numbers-in-a-list"></a>Print non-repeating numbers in a list.
```python
lst = [1, 2, 2, 3, 4, 4, 5]
print([x for x in lst if lst.count(x) == 1]) # [1, 3, 5]
```
[Back to Top](#intermediate-intermediate-logic--collections)

### <a id="write-a-program-to-loop-through-a-list-using-four-different-methods"></a>Write a program to loop through a `list` using four different methods.
```python
lst = [1, 2, 3]

# 1. For loop
for x in lst: print(x)

# 2. While loop
i = 0
while i < len(lst):
    print(lst[i])
    i += 1

# 3. Enumerate
for i, x in enumerate(lst): print(x)

# 4. List comprehension (side effect)
[print(x) for x in lst]
```
[Back to Top](#intermediate-intermediate-logic--collections)

### <a id="demonstrate-the-use-of-the-finally-keyword-in-a-program"></a>Demonstrate the use of the `finally` keyword in a program.
```python
try:
    print("Try")
finally:
    print("Finally")
```
[Back to Top](#intermediate-intermediate-logic--collections)

## Advanced (Algorithms & Complex Logic)

### <a id="count-the-occurrence-of-each-character-in-a-string"></a>Count the occurrence of each character in a string.
```python
s = "hello"
counts = {c: s.count(c) for c in set(s)}
print(counts)
```
[Back to Top](#advanced-algorithms--complex-logic)

### <a id="find-the-occurrence-of-every-character-in-welcome-to-wipro"></a>Find the occurrence of every character in "Welcome to Wipro".
```python
s = "Welcome to Wipro"
counts = {c: s.count(c) for c in set(s) if c.strip()}
print(counts)
```
[Back to Top](#advanced-algorithms--complex-logic)

### <a id="print-all-possible-combinations-of-a-string-input-abc"></a>Print all possible combinations of a string (Input: "abc").
```python
from itertools import permutations
s = "abc"
perms = [''.join(p) for p in permutations(s)]
print(perms) # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
```
[Back to Top](#advanced-algorithms--complex-logic)

### <a id="demonstrate-raising-an-exception-in-a-function"></a>Demonstrate raising an exception in a function.
```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

try:
    divide(10, 0)
except ValueError as e:
    print(e)
```
[Back to Top](#advanced-algorithms--complex-logic)