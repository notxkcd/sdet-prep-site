---
title: "Questions - Aiite Q Dump - Set_1"
date: 2026-01-30
draft: false
---

# Python Programming Interview Questions (Sorted by Difficulty) - Aiite Q Dump - Set_1.txt

## Beginner (Basics)
- [Reverse a string.](#reverse-a-string)
- [Reverse an integer number.](#reverse-an-integer-number)
- [Count the number of letters in a given string (e.g., "Hello" -> 5).](#count-the-number-of-letters-in-a-given-string-eg-hello-5)
- [Factorial program.](#factorial-program)
- [Swap two variables without using a 3rd variable.](#swap-two-variables-without-using-a-3rd-variable)
- [Find the minimum and maximum value in a collection of numbers.](#find-the-minimum-and-maximum-value-in-a-collection-of-numbers)
- [Check if a number is a Palindrome.](#check-if-a-number-is-a-palindrome)
- [Check if a string is a Palindrome.](#check-if-a-string-is-a-palindrome)
- [Check if a number is a Prime number.](#check-if-a-number-is-a-prime-number)
- [Write code to read data from a configuration file (e.g., .ini or .json).](#write-code-to-read-data-from-a-configuration-file-eg-ini-or-json)

## Intermediate (Intermediate Logic)
- [Count vowels and non-vowels in a string.](#count-vowels-and-non-vowels-in-a-string)
- [Count the frequency of a letter in a string.](#count-the-frequency-of-a-letter-in-a-string)
- [Fibonacci series.](#fibonacci-series)
- [Check if a number is an Armstrong number.](#check-if-a-number-is-an-armstrong-number)
- [Sort a `list` in ascending order.](#sort-a-list-in-ascending-order)
- [Separate numbers and alphabets from a mixed string.](#separate-numbers-and-alphabets-from-a-mixed-string)
- [Count digits of 'a' in a sentence (Input: "My name is vaishnavi and I am working in Wipro").](#count-digits-of-a-in-a-sentence-input-my-name-is-vaishnavi-and-i-am-working-in-wipro)
- [How to replace '.' with a space in an email only between names (not after @).](#how-to-replace--with-a-space-in-an-email-only-between-names-not-after-)
- [Reverse a string in different ways: "Deepak Kumar" -> "Kumar Deepak" (Swap words).](#reverse-a-string-in-different-ways-deepak-kumar-kumar-deepak-swap-words)
- [Write a class for: `b1 = Book("Stephen Hawking")`, `b2 = Book(6)`.](#write-a-class-for-b1--bookstephen-hawking-b2--book6)

## Advanced (Algorithms & Complex Challenges)
- [Reverse each word in a string but keep the word position (Input: "Java is a programming language").](#reverse-each-word-in-a-string-but-keep-the-word-position-input-java-is-a-programming-language)
- [Reverse a string (Input: "Deepak Kumar", Output: "kapeed ramuk").](#reverse-a-string-input-deepak-kumar-output-kapeed-ramuk)
- [Count the occurrence of each character in a string.](#count-the-occurrence-of-each-character-in-a-string)
- [Remove all special characters from a string and print only alphanumeric characters.](#remove-all-special-characters-from-a-string-and-print-only-alphanumeric-characters)
- [Remove duplicates from a string without using Set or built-in methods.](#remove-duplicates-from-a-string-without-using-set-or-built-in-methods)
- [Input: `name = a2b3c2`, Output: `aabbbcc`.](#input-name--a2b3c2-output-aabbbcc)
- [Sort a 2D list: `list=[[2,4,5],[3,4,7],[1,2,9]]`.](#sort-a-2d-list-list245347129)
- [Can you execute a method without writing a `main` block (top-level code)?](#can-you-execute-a-method-without-writing-a-main-block-top-level-code)
- [Logic to count duplicates in "babcadaefhef".](#logic-to-count-duplicates-in-babcadaefhef)

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
num = 12345
print(int(str(num)[::-1])) # 54321
```
[Back to Top](#beginner-basics)

### <a id="count-the-number-of-letters-in-a-given-string-eg-hello-5"></a>Count the number of letters in a given string (e.g., "Hello" -> 5).
```python
s = "Hello"
print(len(s)) # 5
```
[Back to Top](#beginner-basics)

### <a id="factorial-program"></a>Factorial program.
```python
import math
print(math.factorial(5)) # 120
```
[Back to Top](#beginner-basics)

### <a id="swap-two-variables-without-using-a-3rd-variable"></a>Swap two variables without using a 3rd variable.
```python
a, b = 1, 2
a, b = b, a
print(a, b) # 2 1
```
[Back to Top](#beginner-basics)

### <a id="find-the-minimum-and-maximum-value-in-a-collection-of-numbers"></a>Find the minimum and maximum value in a collection of numbers.
```python
nums = [1, 5, 2, 8, 3]
print(min(nums), max(nums)) # 1 8
```
[Back to Top](#beginner-basics)

### <a id="check-if-a-number-is-a-palindrome"></a>Check if a number is a Palindrome.
```python
num = 121
print(str(num) == str(num)[::-1]) # True
```
[Back to Top](#beginner-basics)

### <a id="check-if-a-string-is-a-palindrome"></a>Check if a string is a Palindrome.
```python
s = "madam"
print(s == s[::-1]) # True
```
[Back to Top](#beginner-basics)

### <a id="check-if-a-number-is-a-prime-number"></a>Check if a number is a Prime number.
```python
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True
print(is_prime(7)) # True
```
[Back to Top](#beginner-basics)

### <a id="write-code-to-read-data-from-a-configuration-file-eg-ini-or-json"></a>Write code to read data from a configuration file (e.g., .ini or .json).
```python
import json
try:
    with open('config.json', 'r') as f:
        config = json.load(f)
        print(config)
except FileNotFoundError:
    print("File not found")
```
[Back to Top](#beginner-basics)

## Intermediate (Intermediate Logic)

### <a id="count-vowels-and-non-vowels-in-a-string"></a>Count vowels and non-vowels in a string.
```python
s = "hello world"
vowels = sum(1 for c in s if c.lower() in 'aeiou')
non_vowels = sum(1 for c in s if c.isalpha() and c.lower() not in 'aeiou')
print(vowels, non_vowels) # 3 7
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="count-the-frequency-of-a-letter-in-a-string"></a>Count the frequency of a letter in a string.
```python
s = "hello"
print(s.count('l')) # 2
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="fibonacci-series"></a>Fibonacci series.
```python
fib = [0, 1]
for i in range(2, 10):
    fib.append(fib[-1] + fib[-2])
print(fib)
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="check-if-a-number-is-an-armstrong-number"></a>Check if a number is an Armstrong number.
```python
num = 153
sum_cubes = sum(int(digit)**3 for digit in str(num))
print(sum_cubes == num) # True
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="sort-a-list-in-ascending-order"></a>Sort a `list` in ascending order.
```python
lst = [3, 1, 4, 1, 5]
lst.sort()
print(lst) # [1, 1, 3, 4, 5]
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="separate-numbers-and-alphabets-from-a-mixed-string"></a>Separate numbers and alphabets from a mixed string.
```python
s = "a1b2c3"
nums = "".join([c for c in s if c.isdigit()])
alphas = "".join([c for c in s if c.isalpha()])
print(nums, alphas) # "123" "abc"
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="count-digits-of-a-in-a-sentence-input-my-name-is-vaishnavi-and-i-am-working-in-wipro"></a>Count digits of 'a' in a sentence (Input: "My name is vaishnavi and I am working in Wipro").
```python
s = "My name is vaishnavi and I am working in Wipro"
print(s.lower().count('a')) # 4
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="how-to-replace--with-a-space-in-an-email-only-between-names-not-after-"></a>How to replace '.' with a space in an email only between names (not after @).
```python
email = "john.doe@example.com"
name, domain = email.split('@')
print(f"{name.replace('.', ' ')}@{domain}") # "john doe@example.com"
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="reverse-a-string-in-different-ways-deepak-kumar-kumar-deepak-swap-words"></a>Reverse a string in different ways: "Deepak Kumar" -> "Kumar Deepak" (Swap words).
```python
name = "Deepak Kumar"
print(" ".join(name.split()[::-1])) # "Kumar Deepak"
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="write-a-class-for-b1--bookstephen-hawking-b2--book6"></a>Write a class for: `b1 = Book("Stephen Hawking")`, `b2 = Book(6)`.
```python
class Book:
    def __init__(self, arg):
        print(f"Book created with: {arg}")

b1 = Book("Stephen Hawking")
b2 = Book(6)
```
[Back to Top](#intermediate-intermediate-logic)

## Advanced (Algorithms & Complex Challenges)

### <a id="reverse-each-word-in-a-string-but-keep-the-word-position-input-java-is-a-programming-language"></a>Reverse each word in a string but keep the word position (Input: "Java is a programming language").
```python
s = "Java is a programming language"
print(" ".join([w[::-1] for w in s.split()])) # "avaJ si a gnimmargorp egaugnal"
```
[Back to Top](#advanced-algorithms--complex-challenges)

### <a id="reverse-a-string-input-deepak-kumar-output-kapeed-ramuk"></a>Reverse a string (Input: "Deepak Kumar", Output: "kapeed ramuk").
```python
s = "Deepak Kumar"
print(" ".join([w[::-1] for w in s.split()]))
```
[Back to Top](#advanced-algorithms--complex-challenges)

### <a id="count-the-occurrence-of-each-character-in-a-string"></a>Count the occurrence of each character in a string.
```python
s = "hello"
print({c: s.count(c) for c in set(s)})
```
[Back to Top](#advanced-algorithms--complex-challenges)

### <a id="remove-all-special-characters-from-a-string-and-print-only-alphanumeric-characters"></a>Remove all special characters from a string and print only alphanumeric characters.
```python
import re
s = "Hello@#$World123"
print(re.sub(r'[^a-zA-Z0-9]', '', s)) # "HelloWorld123"
```
[Back to Top](#advanced-algorithms--complex-challenges)

### <a id="remove-duplicates-from-a-string-without-using-set-or-built-in-methods"></a>Remove duplicates from a string without using Set or built-in methods.
```python
s = "hello"
unique = ""
for char in s:
    if char not in unique:
        unique += char
print(unique) # "helo"
```
[Back to Top](#advanced-algorithms--complex-challenges)

### <a id="input-name--a2b3c2-output-aabbbcc"></a>Input: `name = a2b3c2`, Output: `aabbbcc`.
```python
s = "a2b3c2"
res = ""
for i in range(0, len(s), 2):
    res += s[i] * int(s[i+1])
print(res) # "aabbbcc"
```
[Back to Top](#advanced-algorithms--complex-challenges)

### <a id="sort-a-2d-list-list245347129"></a>Sort a 2D list: `list=[[2,4,5],[3,4,7],[1,2,9]]`.
```python
lst = [[2, 4, 5], [3, 4, 7], [1, 2, 9]]
lst.sort() # Sorts based on first element by default
print(lst) # [[1, 2, 9], [2, 4, 5], [3, 4, 7]]
```
[Back to Top](#advanced-algorithms--complex-challenges)

### <a id="can-you-execute-a-method-without-writing-a-main-block-top-level-code"></a>Can you execute a method without writing a `main` block (top-level code)?
```python
# Yes, Python executes code line by line.
print("This code runs without a main function or block")
```
[Back to Top](#advanced-algorithms--complex-challenges)

### <a id="logic-to-count-duplicates-in-babcadaefhef"></a>Logic to count duplicates in "babcadaefhef".
```python
s = "babcadaefhef"
counts = {c: s.count(c) for c in set(s) if s.count(c) > 1}
print(list(counts.keys())) # ['b', 'a', 'e', 'f'] (approx)
```
[Back to Top](#advanced-algorithms--complex-challenges)