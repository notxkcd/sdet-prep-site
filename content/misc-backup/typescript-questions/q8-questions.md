---
title: "Questions - Aiite Q Dump - Set_4"
date: 2026-01-30
draft: false
---

# TypeScript Programming Interview Questions (Sorted by Difficulty) - Aiite Q Dump - Set_4.txt

## Beginner (Basics)
- [Write a program to reverse a string (Generic).](#write-a-program-to-reverse-a-string-generic)
- [Reverse a string using a loop and using an inbuilt function.](#reverse-a-string-using-a-loop-and-using-an-inbuilt-function)
- [Print the first 3 characters of a string.](#print-the-first-3-characters-of-a-string)
- [Find the minimum and maximum value in an array.](#find-the-minimum-and-maximum-value-in-an-array)

## Intermediate (Intermediate Logic)
- [Manipulate a string: write your name, print its length, add characters, and then print the name/length multiple times.](#manipulate-a-string-write-your-name-print-its-length-add-characters-and-then-print-the-namelength-multiple-times)
- [Input: `abc`, Output: `aabbcc`.](#input-abc-output-aabbcc)

## Advanced (Advanced Algorithms & Logic)
- [Find duplicate characters and unique characters in a string (Input: `weqjhjkAJKDbdnmbcnm`).](#find-duplicate-characters-and-unique-characters-in-a-string-input-weqjhjkajkdbdnmbcnm)

---

# Answers

## Beginner (Basics)

### <a id="write-a-program-to-reverse-a-string-generic"></a>Write a program to reverse a string (Generic).
```typescript
const str = "hello";
console.log(str.split("").reverse().join("")); // "olleh"
```
[Back to Top](#beginner-basics)

### <a id="reverse-a-string-using-a-loop-and-using-an-inbuilt-function"></a>Reverse a string using a loop and using an inbuilt function.
```typescript
const str = "hello";
// Loop
let reversed = "";
for (let i = str.length - 1; i >= 0; i--) reversed += str[i];
console.log(reversed);
// Inbuilt
console.log(str.split("").reverse().join(""));
```
[Back to Top](#beginner-basics)

### <a id="print-the-first-3-characters-of-a-string"></a>Print the first 3 characters of a string.
```typescript
const str = "hello";
console.log(str.substring(0, 3)); // "hel"
```
[Back to Top](#beginner-basics)

### <a id="find-the-minimum-and-maximum-value-in-an-array"></a>Find the minimum and maximum value in an array.
```typescript
const arr = [1, 5, 2, 8, 3];
console.log(Math.min(...arr), Math.max(...arr)); // 1 8
```
[Back to Top](#beginner-basics)

## Intermediate (Intermediate Logic)

### <a id="manipulate-a-string-write-your-name-print-its-length-add-characters-and-then-print-the-namelength-multiple-times"></a>Manipulate a string: write your name, print its length, add characters, and then print the name/length multiple times.
```typescript
let name = "John";
console.log(name.length);
name += " Doe";
for (let i = 0; i < 3; i++) {
    console.log(`${name} - ${name.length}`);
}
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="input-abc-output-aabbcc"></a>Input: `abc`, Output: `aabbcc`.
```typescript
const str = "abc";
const res = str.split("").map(c => c + c).join("");
console.log(res); // "aabbcc"
```
[Back to Top](#intermediate-intermediate-logic)

## Advanced (Advanced Algorithms & Logic)

### <a id="find-duplicate-characters-and-unique-characters-in-a-string-input-weqjhjkajkdbdnmbcnm"></a>Find duplicate characters and unique characters in a string (Input: `weqjhjkAJKDbdnmbcnm`).
```typescript
const str = "weqjhjkAJKDbdnmbcnm";
const counts: any = {};
for (const char of str) counts[char] = (counts[char] || 0) + 1;

const duplicates = Object.keys(counts).filter(k => counts[k] > 1);
const unique = Object.keys(counts).filter(k => counts[k] === 1);

console.log("Duplicates:", duplicates);
console.log("Unique:", unique);
```
[Back to Top](#advanced-advanced-algorithms--logic)