---
title: "Questions - AiiTE Q Dump-Set_6"
date: 2026-01-30
draft: false
---

# Python Programming Interview Questions (Sorted by Difficulty) - AiiTE Q Dump-Set_6.txt

## Beginner (Basic Manipulations & Logic)
- [Reverse a string (Input: `inte*#rview*#`).](#reverse-a-string-input-interview)
- [Remove spaces from a string.](#remove-spaces-from-a-string)
- [Print vowels in a given string (Input: `my name is gyan`).](#print-vowels-in-a-given-string-input-my-name-is-gyan)
- [Check if a number is even or odd.](#check-if-a-number-is-even-or-odd)
- [Swap two numbers without using a third variable.](#swap-two-numbers-without-using-a-third-variable)
- [Check if a number is Prime or not (Input: `11`).](#check-if-a-number-is-prime-or-not-input-11)
- [Fibonacci series.](#fibonacci-series)
- [Retrieve the date from a sentence (Input: `Today date is 7/27/2024`).](#retrieve-the-date-from-a-sentence-input-today-date-is-7272024)
- [Remove unwanted spaces from a string.](#remove-unwanted-spaces-from-a-string)
- [Pattern program.](#pattern-program)

## Intermediate (Intermediate Logic & Data Structures)
- [Check if a string is a Palindrome or not (Input: `madam`).](#check-if-a-string-is-a-palindrome-or-not-input-madam)
- [Count the occurrence of a character (Input: `Nathiya Umapathi`).](#count-the-occurrence-of-a-character-input-nathiya-umapathi)
- [Print unique values from a string (Input: `aabbcdd`).](#print-unique-values-from-a-string-input-aabbcdd)
- [Change uppercase to lowercase and vice versa (Input: `JaVA SeLENium`).](#change-uppercase-to-lowercase-and-vice-versa-input-java-selenium)
- [Find the second maximum number in a list.](#find-the-second-maximum-number-in-a-list)
- [Find the second largest number in a list.](#find-the-second-largest-number-in-a-list)
- [Find duplicate numbers in a list.](#find-duplicate-numbers-in-a-list)
- [Sort a list (Input: `list array`).](#sort-a-list-input-list-array)
- [Compare two lists and get common values.](#compare-two-lists-and-get-common-values)
- [Find the top value from a `list` of 10 numbers.](#find-the-top-value-from-a-list-of-10-numbers)
- [Find the digit count in a long number (Input: `9662343497543`).](#find-the-digit-count-in-a-long-number-input-9662343497543)
- [Count prime numbers from 1 to 100.](#count-prime-numbers-from-1-to-100)
- [Extract the logic to get output `Slnium` from `Selenium`.](#extract-the-logic-to-get-output-slnium-from-selenium)
- [Predict output for String comparison (`is` vs `==`).](#predict-output-for-string-comparison-is-vs-)
- [Predict output for division by zero with multiple except blocks.](#predict-output-for-division-by-zero-with-multiple-except-blocks)

## Advanced (Advanced Algorithms & Tricky Logic)
- [Remove special characters from a string without using a loop (Input: `@%^#%^%#qwertyt%^%^qwe123`).](#remove-special-characters-from-a-string-without-using-a-loop-input-qwertytqwe123)
- [Separate characters, special characters, and digits from a string and store them in lists.](#separate-characters-special-characters-and-digits-from-a-string-and-store-them-in-lists)
- [Reverse a string without using for loop conditions.](#reverse-a-string-without-using-for-loop-conditions)
- [Reverse each word in a string (Input: `I am sowmyashri`).](#reverse-each-word-in-a-string-input-i-am-sowmyashri)
- [Reverse a string (Input: `Welcome To LTImindtree`, Output: `LTImindtree To Welcome`).](#reverse-a-string-input-welcome-to-ltimindtree-output-ltimindtree-to-welcome)
- [Count the occurrence of each character in a string (Input: `Vivekanand`).](#count-the-occurrence-of-each-character-in-a-string-input-vivekanand)
- [Print the first non-repeating character in a string (Input: `interview`).](#print-the-first-non-repeating-character-in-a-string-input-interview)
- [Given input `Accenture`, output `EeRrUuTtNnEeCcCcAa` (Reverse and duplicate characters).](#given-input-accenture-output-eerruuttnneeccccaa-reverse-and-duplicate-characters)
- [Combine two string lists and take the occurrence of each word.](#combine-two-string-lists-and-take-the-occurrence-of-each-word)
- [Predict output for constructor chaining using `super().__init__()`.](#predict-output-for-constructor-chaining-using-super__init__)
- [Predict output for `list a = [1,2,3,4,5,6,7,8,9,10]` to `[10,1,9,2,8,3,7,4,6,5]`.](#predict-output-for-list-a--12345678910-to-10192837465)

---

# Answers

## Beginner (Basic Manipulations & Logic)

### <a id="reverse-a-string-input-interview"></a>Reverse a string (Input: `inte*#rview*#`).
```python
s = "inte*#rview*#"
print(s[::-1]) # "#*weivr#*etni"
```
[Back to Top](#beginner-basic-manipulations--logic)

### <a id="remove-spaces-from-a-string"></a>Remove spaces from a string.
```python
s = " Hello World "
print(s.replace(" ", "")) # "HelloWorld"
```
[Back to Top](#beginner-basic-manipulations--logic)

### <a id="print-vowels-in-a-given-string-input-my-name-is-gyan"></a>Print vowels in a given string (Input: `my name is gyan`).
```python
s = "my name is gyan"
vowels = [char for char in s if char.lower() in "aeiou"]
print("".join(vowels)) # "aeia"
```
[Back to Top](#beginner-basic-manipulations--logic)

### <a id="check-if-a-number-is-even-or-odd"></a>Check if a number is even or odd.
```python
num = 5
print("Even" if num % 2 == 0 else "Odd")
```
[Back to Top](#beginner-basic-manipulations--logic)

### <a id="swap-two-numbers-without-using-a-third-variable"></a>Swap two numbers without using a third variable.
```python
a, b = 10, 20
a, b = b, a
print(f"a: {a}, b: {b}")
```
[Back to Top](#beginner-basic-manipulations--logic)

### <a id="check-if-a-number-is-prime-or-not-input-11"></a>Check if a number is Prime or not (Input: `11`).
```python
def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(11)) # True
```
[Back to Top](#beginner-basic-manipulations--logic)

### <a id="fibonacci-series"></a>Fibonacci series.
```python
n1, n2 = 0, 1
print(n1)
print(n2)
for _ in range(8):
    nth = n1 + n2
    print(nth)
    n1, n2 = n2, nth
```
[Back to Top](#beginner-basic-manipulations--logic)

### <a id="retrieve-the-date-from-a-sentence-input-today-date-is-7272024"></a>Retrieve the date from a sentence (Input: `Today date is 7/27/2024`).
```python
import re
text = "Today date is 7/27/2024"
match = re.search(r'\d{1,2}/\d{1,2}/\d{4}', text)
print(match.group() if match else "None") # "7/27/2024"
```
[Back to Top](#beginner-basic-manipulations--logic)

### <a id="remove-unwanted-spaces-from-a-string"></a>Remove unwanted spaces from a string.
```python
s = "  Hello   World  "
print(" ".join(s.split())) # "Hello World"
```
[Back to Top](#beginner-basic-manipulations--logic)

### <a id="pattern-program"></a>Pattern program.
```python
print("*")
print("##")
print("*")
print("####")
```
[Back to Top](#beginner-basic-manipulations--logic)

## Intermediate (Intermediate Logic & Data Structures)

### <a id="check-if-a-string-is-a-palindrome-or-not-input-madam"></a>Check if a string is a Palindrome or not (Input: `madam`).
```python
s = "madam"
print(s == s[::-1]) # True
```
[Back to Top](#intermediate-intermediate-logic--data-structures)

### <a id="count-the-occurrence-of-a-character-input-nathiya-umapathi"></a>Count the occurrence of a character (Input: `Nathiya Umapathi`).
```python
s = "Nathiya Umapathi"
print(s.lower().count('a')) # 4
```
[Back to Top](#intermediate-intermediate-logic--data-structures)

### <a id="print-unique-values-from-a-string-input-aabbcdd"></a>Print unique values from a string (Input: `aabbcdd`).
```python
s = "aabbcdd"
print("".join(sorted(set(s), key=s.index))) # "abcd"
```
[Back to Top](#intermediate-intermediate-logic--data-structures)

### <a id="change-uppercase-to-lowercase-and-vice-versa-input-java-selenium"></a>Change uppercase to lowercase and vice versa (Input: `JaVA SeLENium`).
```python
s = "JaVA SeLENium"
print(s.swapcase()) # "jAva sElenIUM"
```
[Back to Top](#intermediate-intermediate-logic--data-structures)

### <a id="find-the-second-maximum-number-in-a-list"></a>Find the second maximum number in a list.
```python
lst = [10, 5, 20, 8]
print(sorted(lst)[-2]) # 10
```
[Back to Top](#intermediate-intermediate-logic--data-structures)

### <a id="find-the-second-largest-number-in-a-list"></a>Find the second largest number in a list.
```python
lst = [10, 20, 30, 20, 40]
print(sorted(list(set(lst)))[-2]) # 30
```
[Back to Top](#intermediate-intermediate-logic--data-structures)

### <a id="find-duplicate-numbers-in-a-list"></a>Find duplicate numbers in a list.
```python
lst = [1, 2, 3, 2, 4, 1]
print(list(set([x for x in lst if lst.count(x) > 1]))) # [1, 2]
```
[Back to Top](#intermediate-intermediate-logic--data-structures)

### <a id="sort-a-list-input-list-array"></a>Sort a list (Input: `list array`).
```python
lst = [3, 1, 4, 2]
lst.sort()
print(lst) # [1, 2, 3, 4]
```
[Back to Top](#intermediate-intermediate-logic--data-structures)

### <a id="compare-two-lists-and-get-common-values"></a>Compare two lists and get common values.
```python
l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]
print(list(set(l1) & set(l2))) # [3, 4]
```
[Back to Top](#intermediate-intermediate-logic--data-structures)

### <a id="find-the-top-value-from-a-list-of-10-numbers"></a>Find the top value from a `list` of 10 numbers.
```python
lst = [1, 5, 2, 8, 3, 9, 4, 7, 6, 0]
print(max(lst)) # 9
```
[Back to Top](#intermediate-intermediate-logic--data-structures)

### <a id="find-the-digit-count-in-a-long-number-input-9662343497543"></a>Find the digit count in a long number (Input: `9662343497543`).
```python
num = 9662343497543
print(len(str(num))) # 13
```
[Back to Top](#intermediate-intermediate-logic--data-structures)

### <a id="count-prime-numbers-from-1-to-100"></a>Count prime numbers from 1 to 100.
```python
count = sum(1 for i in range(2, 101) if is_prime(i))
print(count)
```
[Back to Top](#intermediate-intermediate-logic--data-structures)

### <a id="extract-the-logic-to-get-output-slnium-from-selenium"></a>Extract the logic to get output `Slnium` from `Selenium`.
```python
s = "Selenium"
print(s.replace("e", "")) # "Slnium"
```
[Back to Top](#intermediate-intermediate-logic--data-structures)

### <a id="predict-output-for-string-comparison-is-vs-"></a>Predict output for String comparison (`is` vs `==`).
```python
s1 = "hello"
s2 = "hello"
print(s1 == s2) # True (value)
print(s1 is s2) # True (interning, usually)

l1 = [1]
l2 = [1]
print(l1 == l2) # True
print(l1 is l2) # False
```
[Back to Top](#intermediate-intermediate-logic--data-structures)

### <a id="predict-output-for-division-by-zero-with-multiple-except-blocks"></a>Predict output for division by zero with multiple except blocks.
```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Caught ZeroDivisionError")
except Exception as e:
    print(f"Caught {e}")
finally:
    print("Finally block")
```
[Back to Top](#intermediate-intermediate-logic--data-structures)

## Advanced (Advanced Algorithms & Tricky Logic)

### <a id="remove-special-characters-from-a-string-without-using-a-loop-input-qwertytqwe123"></a>Remove special characters from a string without using a loop (Input: `@%^#%^%#qwertyt%^%^qwe123`).
```python
import re
s = "@%^#%^%#qwertyt%^%^qwe123"
print(re.sub(r'[^a-zA-Z0-9]', '', s)) # "qwertytqwe123"
```
[Back to Top](#advanced-advanced-algorithms--tricky-logic)

### <a id="separate-characters-special-characters-and-digits-from-a-string-and-store-them-in-lists"></a>Separate characters, special characters, and digits from a string and store them in lists.
```python
import re
s = "Abc@123"
chars = re.findall(r'[a-zA-Z]', s)
digits = re.findall(r'\d', s)
specials = re.findall(r'[^a-zA-Z0-9]', s)
print(chars, digits, specials)
```
[Back to Top](#advanced-advanced-algorithms--tricky-logic)

### <a id="reverse-a-string-without-using-for-loop-conditions"></a>Reverse a string without using for loop conditions.
```python
# Recursive or slicing
def reverse_recursive(s):
    if not s: return ""
    return reverse_recursive(s[1:]) + s[0]
print(reverse_recursive("Hello")) # "olleH"
```
[Back to Top](#advanced-advanced-algorithms--tricky-logic)

### <a id="reverse-each-word-in-a-string-input-i-am-sowmyashri"></a>Reverse each word in a string (Input: `I am sowmyashri`).
```python
s = "I am sowmyashri"
print(" ".join([w[::-1] for w in s.split()])) # "I ma irhsaymwos"
```
[Back to Top](#advanced-advanced-algorithms--tricky-logic)

### <a id="reverse-a-string-input-welcome-to-ltimindtree-output-ltimindtree-to-welcome"></a>Reverse a string (Input: `Welcome To LTImindtree`, Output: `LTImindtree To Welcome`).
```python
s = "Welcome To LTImindtree"
print(" ".join(s.split()[::-1])) # "LTImindtree To Welcome"
```
[Back to Top](#advanced-advanced-algorithms--tricky-logic)

### <a id="count-the-occurrence-of-each-character-in-a-string-input-vivekanand"></a>Count the occurrence of each character in a string (Input: `Vivekanand`).
```python
s = "Vivekanand"
counts = {}
for char in s:
    counts[char] = counts.get(char, 0) + 1
print(counts)
```
[Back to Top](#advanced-advanced-algorithms--tricky-logic)

### <a id="print-the-first-non-repeating-character-in-a-string-input-interview"></a>Print the first non-repeating character in a string (Input: `interview`).
```python
s = "interview"
for char in s:
    if s.count(char) == 1:
        print(char) # "n"
        break
```
[Back to Top](#advanced-advanced-algorithms--tricky-logic)

### <a id="given-input-accenture-output-eerruuttnneeccccaa-reverse-and-duplicate-characters"></a>Given input `Accenture`, output `EeRrUuTtNnEeCcCcAa` (Reverse and duplicate characters).
```python
s = "Accenture"
res = ""
for char in reversed(s):
    res += char.upper() + char.lower()
print(res) # "EeRrUuTtNnEeCcCcAa"
```
[Back to Top](#advanced-advanced-algorithms--tricky-logic)

### <a id="combine-two-string-lists-and-take-the-occurrence-of-each-word"></a>Combine two string lists and take the occurrence of each word.
```python
l1 = ["hello", "world"]
l2 = ["hello", "python"]
combined = l1 + l2
counts = {}
for word in combined:
    counts[word] = counts.get(word, 0) + 1
print(counts)
```
[Back to Top](#advanced-advanced-algorithms--tricky-logic)

### <a id="predict-output-for-constructor-chaining-using-super__init__"></a>Predict output for constructor chaining using `super().__init__()`.
```python
class Parent:
    def __init__(self):
        print("Parent")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child")

c = Child()
# Output:
# Parent
# Child
```
[Back to Top](#advanced-advanced-algorithms--tricky-logic)

### <a id="predict-output-for-list-a--12345678910-to-10192837465"></a>Predict output for `list a = [1,2,3,4,5,6,7,8,9,10]` to `[10,1,9,2,8,3,7,4,6,5]`.
```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = []
left, right = 0, len(a) - 1
while left <= right:
    if left == right:
        res.append(a[left])
    else:
        res.append(a[right])
        res.append(a[left])
    left += 1
    right -= 1
print(res) # [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
```
[Back to Top](#advanced-advanced-algorithms--tricky-logic)