---
title: "Questions - Aiite Q Dump - Set_3"
date: 2026-01-30
draft: false
---

# Python Programming Interview Questions (Sorted by Difficulty) - Aiite Q Dump - Set_3.txt

## Beginner (Basics)
- [Write a program to reverse a string.](#write-a-program-to-reverse-a-string)
- [Write a program to find odd numbers in a list.](#write-a-program-to-find-odd-numbers-in-a-list)
- [Write a program demonstrating a Constructor (`__init__`) and its uses.](#write-a-program-demonstrating-a-constructor-__init__-and-its-uses)

## Intermediate (Logical Reasoning)
- [Reverse a string word by word.](#reverse-a-string-word-by-word)
- [Identify repeated characters in a string.](#identify-repeated-characters-in-a-string)
- [Find duplicate elements/characters in a string.](#find-duplicate-elementscharacters-in-a-string)
- [Write a program demonstrating Method Overloading (or how to simulate it).](#write-a-program-demonstrating-method-overloading-or-how-to-simulate-it)
- [Write a pattern program (Generic).](#write-a-pattern-program-generic)

## Advanced (Advanced Algorithms & Logic)
- [Change the first letter of every word in a sentence to uppercase.](#change-the-first-letter-of-every-word-in-a-sentence-to-uppercase)
- [Combine two integer lists into a third list, then extract only the odd numbers into a fourth list.](#combine-two-integer-lists-into-a-third-list-then-extract-only-the-odd-numbers-into-a-fourth-list)

---

# Answers

## Beginner (Basics)

### <a id="write-a-program-to-reverse-a-string"></a>Write a program to reverse a string.
```python
s = "hello"
print(s[::-1]) # "olleh"
```
[Back to Top](#beginner-basics)

### <a id="write-a-program-to-find-odd-numbers-in-a-list"></a>Write a program to find odd numbers in a list.
```python
lst = [1, 2, 3, 4, 5]
print([x for x in lst if x % 2 != 0]) # [1, 3, 5]
```
[Back to Top](#beginner-basics)

### <a id="write-a-program-demonstrating-a-constructor-__init__-and-its-uses"></a>Write a program demonstrating a Constructor (`__init__`) and its uses.
```python
class Car:
    def __init__(self, model):
        self.model = model
        print(f"Car {model} initialized")

c = Car("Tesla")
```
[Back to Top](#beginner-basics)

## Intermediate (Logical Reasoning)

### <a id="reverse-a-string-word-by-word"></a>Reverse a string word by word.
```python
s = "Hello World"
print(" ".join(s.split()[::-1])) # "World Hello"
```
[Back to Top](#intermediate-logical-reasoning)

### <a id="identify-repeated-characters-in-a-string"></a>Identify repeated characters in a string.
```python
s = "hello"
print([c for c in set(s) if s.count(c) > 1]) # ['l']
```
[Back to Top](#intermediate-logical-reasoning)

### <a id="find-duplicate-elementscharacters-in-a-string"></a>Find duplicate elements/characters in a string.
```python
s = "hello"
print(list(set([c for c in s if s.count(c) > 1]))) # ['l']
```
[Back to Top](#intermediate-logical-reasoning)

### <a id="write-a-program-demonstrating-method-overloading-or-how-to-simulate-it"></a>Write a program demonstrating Method Overloading (or how to simulate it).
```python
# Python doesn't support traditional overloading, but we can use default args or *args
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

c = Calculator()
print(c.add(1, 2)) # 3
print(c.add(1, 2, 3)) # 6
```
[Back to Top](#intermediate-logical-reasoning)

### <a id="write-a-pattern-program-generic"></a>Write a pattern program (Generic).
```python
for i in range(1, 4):
    print("*" * i)
```
[Back to Top](#intermediate-logical-reasoning)

## Advanced (Advanced Algorithms & Logic)

### <a id="change-the-first-letter-of-every-word-in-a-sentence-to-uppercase"></a>Change the first letter of every word in a sentence to uppercase.
```python
s = "hello world"
print(s.title()) # "Hello World"
```
[Back to Top](#advanced-advanced-algorithms--logic)

### <a id="combine-two-integer-lists-into-a-third-list-then-extract-only-the-odd-numbers-into-a-fourth-list"></a>Combine two integer lists into a third list, then extract only the odd numbers into a fourth list.
```python
l1, l2 = [1, 2], [3, 4]
l3 = l1 + l2
l4 = [x for x in l3 if x % 2 != 0]
print(l4) # [1, 3]
```
[Back to Top](#advanced-advanced-algorithms--logic)