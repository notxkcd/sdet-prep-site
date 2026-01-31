---
title: "Questions - Aiite Q Dump -Set_5"
date: 2026-01-30
draft: false
---

# TypeScript Programming Interview Questions (Sorted by Difficulty) - Aiite Q Dump -Set_5.txt

## Beginner (Basics)
- [Write a program to reverse a string.](#write-a-program-to-reverse-a-string)
- [Write a program to find even and odd numbers in a given array.](#write-a-program-to-find-even-and-odd-numbers-in-a-given-array)
- [Swap two numbers with and without using a third variable.](#swap-two-numbers-with-and-without-using-a-third-variable)

## Intermediate (Intermediate Logic)
- [Write a program to count the occurrences of a specific character (e.g., 'a') in a given string.](#write-a-program-to-count-the-occurrences-of-a-specific-character-eg-a-in-a-given-string)
- [Write a program to count the number of words in a given sentence.](#write-a-program-to-count-the-number-of-words-in-a-given-sentence)
- [Swap two strings without using a temporary variable.](#swap-two-strings-without-using-a-temporary-variable)
- [Write a program to remove duplicate elements from an array.](#write-a-program-to-remove-duplicate-elements-from-an-array)

---

# Answers

## Beginner (Basics)

### <a id="write-a-program-to-reverse-a-string"></a>Write a program to reverse a string.
```typescript
const str = "hello";
console.log(str.split("").reverse().join("")); // "olleh"
```
[Back to Top](#beginner-basics)

### <a id="write-a-program-to-find-even-and-odd-numbers-in-a-given-array"></a>Write a program to find even and odd numbers in a given array.
```typescript
const arr = [1, 2, 3, 4, 5];
const evens = arr.filter(n => n % 2 === 0);
const odds = arr.filter(n => n % 2 !== 0);
console.log("Evens:", evens); // [2, 4]
console.log("Odds:", odds); // [1, 3, 5]
```
[Back to Top](#beginner-basics)

### <a id="swap-two-numbers-with-and-without-using-a-third-variable"></a>Swap two numbers with and without using a third variable.
```typescript
let a = 1, b = 2;
// With temp
let temp = a; a = b; b = temp;
console.log(a, b); // 2 1
// Without temp
[a, b] = [b, a];
console.log(a, b); // 1 2
```
[Back to Top](#beginner-basics)

## Intermediate (Intermediate Logic)

### <a id="write-a-program-to-count-the-occurrences-of-a-specific-character-eg-a-in-a-given-string"></a>Write a program to count the occurrences of a specific character (e.g., 'a') in a given string.
```typescript
const str = "banana";
console.log(str.split("a").length - 1); // 3
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="write-a-program-to-count-the-number-of-words-in-a-given-sentence"></a>Write a program to count the number of words in a given sentence.
```typescript
const sentence = "Hello world from TypeScript";
console.log(sentence.split(" ").length); // 4
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="swap-two-strings-without-using-a-temporary-variable"></a>Swap two strings without using a temporary variable.
```typescript
let s1 = "Hello", s2 = "World";
[s1, s2] = [s2, s1];
console.log(s1, s2); // "World" "Hello"
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="write-a-program-to-remove-duplicate-elements-from-an-array"></a>Write a program to remove duplicate elements from an array.
```typescript
const arr = [1, 2, 2, 3];
console.log([...new Set(arr)]); // [1, 2, 3]
```
[Back to Top](#intermediate-intermediate-logic)