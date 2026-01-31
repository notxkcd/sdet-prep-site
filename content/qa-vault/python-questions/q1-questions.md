---
title: "Questions - 2025 Interview questions"
date: 2026-01-30
draft: false
---

# Python Programming Interview Questions (Sorted by Difficulty) - 2025 Interview questions.txt

## Beginner (Basic Logic & Loops)
- [Swap two numbers using a temporary variable.](#swap-two-numbers-using-a-temporary-variable)
- [Write a code for String reverse.](#write-a-code-for-string-reverse)
- [Reverse a number.](#reverse-a-number)
- [Print "Infosys" but skip the letter "o".](#print-infosys-but-skip-the-letter-o)
- [How to replace a letter from a string?](#how-to-replace-a-letter-from-a-string)
- [Replace vowels with `*` (Input: "chennai").](#replace-vowels-with--input-chennai)
- [Find the maximum and minimum values in a list.](#find-the-maximum-and-minimum-values-in-a-list)
- [Find the smallest value in a list.](#find-the-smallest-value-in-a-list)
- [Print all dividends of 8 between 1 and 100.](#print-all-dividends-of-8-between-1-and-100)
- [Sum the integers found in a mixed string.](#sum-the-integers-found-in-a-mixed-string)
- [Write a code for Palindrome.](#write-a-code-for-palindrome)

## Intermediate (Intermediate Strings, Arrays & Logical Reasoning)
- [Swap two variables without using a 3rd variable.](#swap-two-variables-without-using-a-3rd-variable)
- [Fibonacci series code.](#fibonacci-series-code)
- [Write a sorting program.](#write-a-sorting-program)
- [Find the second maximum value in a list.](#find-the-second-maximum-value-in-a-list)
- [Find the second largest number in a list.](#find-the-second-largest-number-in-a-list)
- [Find duplicate numbers in a list.](#find-duplicate-numbers-in-a-list)
- [Find the maximum salary of an individual in a list.](#find-the-maximum-salary-of-an-individual-in-a-list)
- [Count the occurrence of a character in a string.](#count-the-occurrence-of-a-character-in-a-string)
- [Find the occurrence of a substring in a string.](#find-the-occurrence-of-a-substring-in-a-string)
- [How to replace multiple letters from a string using the same `replace` method?](#how-to-replace-multiple-letters-from-a-string-using-the-same-replace-method)
- [Separate String and Integer from a mixed list.](#separate-string-and-integer-from-a-mixed-list)
- [Reverse the words in a string (Input: "test program").](#reverse-the-words-in-a-string-input-test-program)
- [Format a string (Input: "xperience", Output: "xp*ri*nc**").](#format-a-string-input-xperience-output-xprinc)
- [Extract ABC and 123 from "AB12C3" and print "ABC123".](#extract-abc-and-123-from-ab12c3-and-print-abc123)
- [Input: `Same`, Output: `Saammmeeee`.](#input-same-output-saammmeeee)

## Advanced (Advanced Algorithms, Complex Manipulations & Optimization)
- [Check if two strings are Anagram or not (e.g., "Bored" and "Robed").](#check-if-two-strings-are-anagram-or-not-eg-bored-and-robed)
- [Reverse each word in a given string without changing the caps and small letters.](#reverse-each-word-in-a-given-string-without-changing-the-caps-and-small-letters)
- [Find character count and duplicate characters in a string list.](#find-character-count-and-duplicate-characters-in-a-string-list)
- [Remove duplicates from a string and print unique values (Input: "giggling").](#remove-duplicates-from-a-string-and-print-unique-values-input-giggling)
- [Remove duplicates in a long list of integers/strings.](#remove-duplicates-in-a-long-list-of-integersstrings)
- [Count words greater than 5 and reverse only those.](#count-words-greater-than-5-and-reverse-only-those)
- [Split letters and numbers from a string and print them separately (Input: "1am a C0dingF4n 0r Pr0gr4mm3r or S0ftw4r3 D3v3l0p3r").](#split-letters-and-numbers-from-a-string-and-print-them-separately-input-1am-a-c0dingf4n-0r-pr0gr4mm3r-or-s0ftw4r3-d3v3l0p3r)
- [Print the frequency of integers and letters in a mixed string.](#print-the-frequency-of-integers-and-letters-in-a-mixed-string)
- [List rotational coding.](#list-rotational-coding)
- [Sum the numbers in a mixed list (e.g., from `1,2,3,a,b,c` sum `1,2,3`).](#sum-the-numbers-in-a-mixed-list-eg-from-123abc-sum-123)
- [Find the occurrence of a specific number in a long sequence.](#find-the-occurrence-of-a-specific-number-in-a-long-sequence)
- [Transpose a 2D list.](#transpose-a-2d-list)
- [Declare a 2D list and perform operations.](#declare-a-2d-list-and-perform-operations)
- [Input: `list = [1,0,0,2,0,0,0,3]`, Output: `[1,2,3,0,0,0]`.](#input-list--10020003-output-123000)
- [Input: `a (1,2,3,a,b,c)`, Task: Remove (a b c) and sum (1 2 3).](#input-a-123abc-task-remove-a-b-c-and-sum-1-2-3)

---

# Answers

## Beginner (Basic Logic & Loops)

### <a id="swap-two-numbers-using-a-temporary-variable"></a>Swap two numbers using a temporary variable.
```python
a = 10
b = 20
temp = a
a = b
b = temp
print(f"a: {a}, b: {b}") # a: 20, b: 10
```
[Back to Top](#beginner-basic-logic--loops)

### <a id="write-a-code-for-string-reverse"></a>Write a code for String reverse.
```python
s = "hello"
reversed_s = s[::-1]
print(reversed_s) # "olleh"
```
[Back to Top](#beginner-basic-logic--loops)

### <a id="reverse-a-number"></a>Reverse a number.
```python
num = 12345
reversed_num = int(str(num)[::-1])
print(reversed_num) # 54321
```
[Back to Top](#beginner-basic-logic--loops)

### <a id="print-infosys-but-skip-the-letter-o"></a>Print "Infosys" but skip the letter "o".
```python
company = "Infosys"
result = "".join([char for char in company if char != "o"])
print(result) # "Infsys"
```
[Back to Top](#beginner-basic-logic--loops)

### <a id="how-to-replace-a-letter-from-a-string"></a>How to replace a letter from a string?
```python
text = "Hello World"
new_text = text.replace("World", "Python")
print(new_text) # "Hello Python"
```
[Back to Top](#beginner-basic-logic--loops)

### <a id="replace-vowels-with--input-chennai"></a>Replace vowels with `*` (Input: "chennai").
```python
import re
city = "chennai"
replaced = re.sub(r'[aeiouAEIOU]', '*', city)
print(replaced) # "ch*nn**"
```
[Back to Top](#beginner-basic-logic--loops)

### <a id="find-the-maximum-and-minimum-values-in-a-list"></a>Find the maximum and minimum values in a list.
```python
nums = [10, 5, 20, 8, 15]
print(f"Max: {max(nums)}, Min: {min(nums)}") # Max: 20, Min: 5
```
[Back to Top](#beginner-basic-logic--loops)

### <a id="find-the-smallest-value-in-a-list"></a>Find the smallest value in a list.
```python
nums = [10, 5, 20, 8, 15]
smallest = nums[0]
for num in nums:
    if num < smallest:
        smallest = num
print(smallest) # 5
```
[Back to Top](#beginner-basic-logic--loops)

### <a id="print-all-dividends-of-8-between-1-and-100"></a>Print all dividends of 8 between 1 and 100.
```python
for i in range(1, 101):
    if i % 8 == 0:
        print(i)
```
[Back to Top](#beginner-basic-logic--loops)

### <a id="sum-the-integers-found-in-a-mixed-string"></a>Sum the integers found in a mixed string.
```python
mixed_str = "abc123xyz45"
total = sum([int(char) for char in mixed_str if char.isdigit()])
print(total) # 1 + 2 + 3 + 4 + 5 = 15
```
[Back to Top](#beginner-basic-logic--loops)

### <a id="write-a-code-for-palindrome"></a>Write a code for Palindrome.
```python
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam")) # True
```
[Back to Top](#beginner-basic-logic--loops)

## Intermediate (Intermediate Strings, Arrays & Logical Reasoning)

### <a id="swap-two-variables-without-using-a-3rd-variable"></a>Swap two variables without using a 3rd variable.
```python
x = 10
y = 20
x, y = y, x
print(f"x: {x}, y: {y}") # x: 20, y: 10
```
[Back to Top](#intermediate-intermediate-strings-arrays--logical-reasoning)

### <a id="fibonacci-series-code"></a>Fibonacci series code.
```python
def fibonacci(n):
    series = [0, 1]
    for i in range(2, n):
        series.append(series[-1] + series[-2])
    return series

print(fibonacci(10)) # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```
[Back to Top](#intermediate-intermediate-strings-arrays--logical-reasoning)

### <a id="write-a-sorting-program"></a>Write a sorting program.
```python
arr = [5, 2, 9, 1, 5, 6]
arr.sort()
print(arr) # [1, 2, 5, 5, 6, 9]
```
[Back to Top](#intermediate-intermediate-strings-arrays--logical-reasoning)

### <a id="find-the-second-maximum-value-in-a-list"></a>Find the second maximum value in a list.
```python
arr = [10, 20, 5, 30, 25]
unique_sorted = sorted(list(set(arr)), reverse=True)
print(unique_sorted[1]) # 25
```
[Back to Top](#intermediate-intermediate-strings-arrays--logical-reasoning)

### <a id="find-the-second-largest-number-in-a-list"></a>Find the second largest number in a list.
```python
# Same logic
arr = [100, 20, 5, 30, 25]
max_val = float('-inf')
second_max = float('-inf')
for num in arr:
    if num > max_val:
        second_max = max_val
        max_val = num
    elif num > second_max and num != max_val:
        second_max = num
print(second_max) # 30
```
[Back to Top](#intermediate-intermediate-strings-arrays--logical-reasoning)

### <a id="find-duplicate-numbers-in-a-list"></a>Find duplicate numbers in a list.
```python
arr = [1, 2, 3, 2, 4, 5, 1]
duplicates = list(set([x for x in arr if arr.count(x) > 1]))
print(duplicates) # [1, 2]
```
[Back to Top](#intermediate-intermediate-strings-arrays--logical-reasoning)

### <a id="find-the-maximum-salary-of-an-individual-in-a-list"></a>Find the maximum salary of an individual in a list.
```python
salaries = [5000, 7000, 4500, 8000, 6000]
print(max(salaries)) # 8000
```
[Back to Top](#intermediate-intermediate-strings-arrays--logical-reasoning)

### <a id="count-the-occurrence-of-a-character-in-a-string"></a>Count the occurrence of a character in a string.
```python
s = "hello world"
char_to_count = "l"
print(s.count(char_to_count)) # 3
```
[Back to Top](#intermediate-intermediate-strings-arrays--logical-reasoning)

### <a id="find-the-occurrence-of-a-substring-in-a-string"></a>Find the occurrence of a substring in a string.
```python
s = "hello world hello"
sub_s = "hello"
print(s.count(sub_s)) # 2
```
[Back to Top](#intermediate-intermediate-strings-arrays--logical-reasoning)

### <a id="how-to-replace-multiple-letters-from-a-string-using-the-same-replace-method"></a>How to replace multiple letters from a string using the same `replace` method?
```python
s = "hello world"
table = str.maketrans({'l': '1', 'o': '0'})
print(s.translate(table)) # "he110 w0r1d"
```
[Back to Top](#intermediate-intermediate-strings-arrays--logical-reasoning)

### <a id="separate-string-and-integer-from-a-mixed-list"></a>Separate String and Integer from a mixed list.
```python
mixed = [1, "a", 2, "b", 3, "c"]
numbers = [x for x in mixed if isinstance(x, int)]
strings = [x for x in mixed if isinstance(x, str)]
print(numbers) # [1, 2, 3]
print(strings) # ['a', 'b', 'c']
```
[Back to Top](#intermediate-intermediate-strings-arrays--logical-reasoning)

### <a id="reverse-the-words-in-a-string-input-test-program"></a>Reverse the words in a string (Input: "test program").
```python
text = "test program"
reversed_text = " ".join(text.split()[::-1])
print(reversed_text) # "program test"
```
[Back to Top](#intermediate-intermediate-strings-arrays--logical-reasoning)

### <a id="format-a-string-input-xperience-output-xprinc"></a>Format a string (Input: "xperience", Output: "xp*ri*nc**").
```python
text = "xperience"
# Assuming logic is replace 'e' with '*'
output = text.replace('e', '*')
print(output) # "xp*ri*nc*"
```
[Back to Top](#intermediate-intermediate-strings-arrays--logical-reasoning)

### <a id="extract-abc-and-123-from-ab12c3-and-print-abc123"></a>Extract ABC and 123 from "AB12C3" and print "ABC123".
```python
import re
text = "AB12C3"
letters = "".join(re.findall(r'[A-Za-z]', text))
numbers = "".join(re.findall(r'\d', text))
print(letters + numbers) # "ABC123"
```
[Back to Top](#intermediate-intermediate-strings-arrays--logical-reasoning)

### <a id="input-same-output-saammmeeee"></a>Input: `Same`, Output: `Saammmeeee`.
```python
text = "Same"
output = ""
for i, char in enumerate(text):
    output += char * (i + 1)
print(output) # "Saammmeeee"
```
[Back to Top](#intermediate-intermediate-strings-arrays--logical-reasoning)

## Advanced (Advanced Algorithms, Complex Manipulations & Optimization)

### <a id="check-if-two-strings-are-anagram-or-not-eg-bored-and-robed"></a>Check if two strings are Anagram or not (e.g., "Bored" and "Robed").
```python
def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

print(is_anagram("Bored", "Robed")) # True
```
[Back to Top](#advanced-advanced-algorithms-complex-manipulations--optimization)

### <a id="reverse-each-word-in-a-given-string-without-changing-the-caps-and-small-letters"></a>Reverse each word in a given string without changing the caps and small letters.
```python
text = "Hello World"
reversed_words = " ".join([word[::-1] for word in text.split()])
print(reversed_words) # "olleH dlroW"
```
[Back to Top](#advanced-advanced-algorithms-complex-manipulations--optimization)

### <a id="find-character-count-and-duplicate-characters-in-a-string-list"></a>Find character count and duplicate characters in a string list.
```python
arr = ["abc", "bcd", "cde"]
combined = "".join(arr)
counts = {}
for char in combined:
    counts[char] = counts.get(char, 0) + 1

print(counts)
duplicates = [char for char, count in counts.items() if count > 1]
print("Duplicates:", duplicates)
```
[Back to Top](#advanced-advanced-algorithms-complex-manipulations--optimization)

### <a id="remove-duplicates-from-a-string-and-print-unique-values-input-giggling"></a>Remove duplicates from a string and print unique values (Input: "giggling").
```python
text = "giggling"
unique = "".join(sorted(set(text), key=text.index))
print(unique) # "giln"
```
[Back to Top](#advanced-advanced-algorithms-complex-manipulations--optimization)

### <a id="remove-duplicates-in-a-long-list-of-integersstrings"></a>Remove duplicates in a long list of integers/strings.
```python
lst = [1, 2, 2, 3, 4, 4, 5, "a", "a", "b"]
unique_list = list(set(lst)) # Order not guaranteed with set
# To preserve order:
unique_list_ordered = list(dict.fromkeys(lst))
print(unique_list_ordered) # [1, 2, 3, 4, 5, 'a', 'b']
```
[Back to Top](#advanced-advanced-algorithms-complex-manipulations--optimization)

### <a id="count-words-greater-than-5-and-reverse-only-those"></a>Count words greater than 5 and reverse only those.
```python
sentence = "I am learning Python programming"
processed = " ".join([word[::-1] if len(word) > 5 else word for word in sentence.split()])
print(processed) # "I am gninrael nohtyP gnimmargorp"
```
[Back to Top](#advanced-advanced-algorithms-complex-manipulations--optimization)

### <a id="split-letters-and-numbers-from-a-string-and-print-them-separately-input-1am-a-c0dingf4n-0r-pr0gr4mm3r-or-s0ftw4r3-d3v3l0p3r"></a>Split letters and numbers from a string and print them separately (Input: "1am a C0dingF4n 0r Pr0gr4mm3r or S0ftw4r3 D3v3l0p3r").
```python
import re
text = "1am a C0dingF4n 0r Pr0gr4mm3r or S0ftw4r3 D3v3l0p3r"
letters = "".join(re.findall(r'[A-Za-z]', text))
numbers = "".join(re.findall(r'\d', text))
print("Letters:", letters)
print("Numbers:", numbers)
```
[Back to Top](#advanced-advanced-algorithms-complex-manipulations--optimization)

### <a id="print-the-frequency-of-integers-and-letters-in-a-mixed-string"></a>Print the frequency of integers and letters in a mixed string.
```python
text = "a1b2c3a1"
counts = {}
for char in text:
    counts[char] = counts.get(char, 0) + 1
print(counts) # {'a': 2, '1': 2, 'b': 1, '2': 1, 'c': 1, '3': 1}
```
[Back to Top](#advanced-advanced-algorithms-complex-manipulations--optimization)

### <a id="list-rotational-coding"></a>List rotational coding.
```python
def rotate_list(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

print(rotate_list([1, 2, 3, 4, 5], 2)) # [4, 5, 1, 2, 3]
```
[Back to Top](#advanced-advanced-algorithms-complex-manipulations--optimization)

### <a id="sum-the-numbers-in-a-mixed-list-eg-from-123abc-sum-123"></a>Sum the numbers in a mixed list (e.g., from `1,2,3,a,b,c` sum `1,2,3`).
```python
mixed = [1, 2, 3, 'a', 'b', 'c']
total = sum([x for x in mixed if isinstance(x, int)])
print(total) # 6
```
[Back to Top](#advanced-advanced-algorithms-complex-manipulations--optimization)

### <a id="find-the-occurrence-of-a-specific-number-in-a-long-sequence"></a>Find the occurrence of a specific number in a long sequence.
```python
sequence = [1, 2, 3, 4, 2, 2, 5]
target = 2
print(sequence.count(target)) # 3
```
[Back to Top](#advanced-advanced-algorithms-complex-manipulations--optimization)

### <a id="transpose-a-2d-list"></a>Transpose a 2D list.
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
transposed = list(map(list, zip(*matrix)))
print(transposed) # [[1, 4], [2, 5], [3, 6]]
```
[Back to Top](#advanced-advanced-algorithms-complex-manipulations--optimization)

### <a id="declare-a-2d-list-and-perform-operations"></a>Declare a 2D list and perform operations.
```python
grid = [
    [1, 2],
    [3, 4]
]
# Operation: Double each element
doubled = [[val * 2 for val in row] for row in grid]
print(doubled) # [[2, 4], [6, 8]]
```
[Back to Top](#advanced-advanced-algorithms-complex-manipulations--optimization)

### <a id="input-list--10020003-output-123000"></a>Input: `list = [1,0,0,2,0,0,0,3]`, Output: `[1,2,3,0,0,0]`.
```python
lst = [1, 0, 0, 2, 0, 0, 0, 3]
non_zeros = [x for x in lst if x != 0]
zeros = [x for x in lst if x == 0]
result = non_zeros + zeros
print(result) # [1, 2, 3, 0, 0, 0, 0, 0]
```
[Back to Top](#advanced-advanced-algorithms-complex-manipulations--optimization)

### <a id="input-a-123abc-task-remove-a-b-c-and-sum-1-2-3"></a>Input: `a (1,2,3,a,b,c)`, Task: Remove (a b c) and sum (1 2 3).
```python
a = [1, 2, 3, 'a', 'b', 'c']
total = sum([x for x in a if isinstance(x, int)])
print(total) # 6
```
[Back to Top](#advanced-advanced-algorithms-complex-manipulations--optimization)