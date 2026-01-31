---
title: "Questions - Aiite Q Dump - Set_2"
date: 2026-01-30
draft: false
---

# TypeScript Programming Interview Questions (Sorted by Difficulty) - Aiite Q Dump - Set_2.txt

## Beginner (Basics)
- [Reverse a string.](#reverse-a-string)
- [Reverse an integer number.](#reverse-an-integer-number)
- [Count vowels in a string (e.g., "welcome").](#count-vowels-in-a-string-eg-welcome)
- [Print vowels from a string.](#print-vowels-from-a-string)
- [Find the maximum and minimum numbers in an array.](#find-the-maximum-and-minimum-numbers-in-an-array)
- [Swap two numbers without using a third variable.](#swap-two-numbers-without-using-a-third-variable)
- [Find the count of letters in a string (Input: " Hello ").](#find-the-count-of-letters-in-a-string-input-hello-)
- [Replace '-' with '/' in a date string (Input: "03-06-1995").](#replace---with--in-a-date-string-input-03-06-1995)
- [How to get system date and time?](#how-to-get-system-date-and-time)
- [Convert a string to an integer (Input: "123456").](#convert-a-string-to-an-integer-input-123456)
- [Get all elements from an array using a loop.](#get-all-elements-from-an-array-using-a-loop)

## Intermediate (Intermediate Logic)
- [Reverse a string word by word.](#reverse-a-string-word-by-word)
- [Count duplicate characters in a string.](#count-duplicate-characters-in-a-string)
- [Find the frequency of characters in a string.](#find-the-frequency-of-characters-in-a-string)
- [Find duplicate words in a string (e.g., "Hexaware").](#find-duplicate-words-in-a-string-eg-hexaware)
- [Reverse two numbers without using a temporary variable (Input: `x = 10`, `y = 20`).](#reverse-two-numbers-without-using-a-temporary-variable-input-x--10-y--20)
- [Reverse two strings without using a temporary variable (Input: `a = "India"`, `b = "uk"`).](#reverse-two-strings-without-using-a-temporary-variable-input-a--india-b--uk)
- [Find the second highest number in an array.](#find-the-second-highest-number-in-an-array)
- [Find duplicate elements in an array.](#find-duplicate-elements-in-an-array)
- [Sort an array.](#sort-an-array)
- [Convert an array to a list (or Set/Map).](#convert-an-array-to-a-list-or-setmap)
- [Retrieve key-value pairs from a `Map` or Object (Input: `X = "A", Y = "B"`).](#retrieve-key-value-pairs-from-a-map-or-object-input-x--a-y--b)
- [Write a class or interface for Username and Password.](#write-a-class-or-interface-for-username-and-password)

## Advanced (Advanced Algorithms & Logic)
- [Reverse a string word by word but keep word position.](#reverse-a-string-word-by-word-but-keep-word-position)
- [Find repeated characters in the word "ASSASINATION".](#find-repeated-characters-in-the-word-assasination)
- [Remove duplicates from a string without using collection concepts.](#remove-duplicates-from-a-string-without-using-collection-concepts)
- [Anagram check: Determine if two string patterns are the same (e.g., "CAT" and "ACT").](#anagram-check-determine-if-two-string-patterns-are-the-same-eg-cat-and-act)
- [Count characters, numbers, and special characters in a mixed string.](#count-characters-numbers-and-special-characters-in-a-mixed-string)
- [Find the 3rd maximum element in an array.](#find-the-3rd-maximum-element-in-an-array)
- [Sum of two integer arrays.](#sum-of-two-integer-arrays)
- [Find common duplicates between two arrays.](#find-common-duplicates-between-two-arrays)
- [Logic to connect to a database (e.g., MongoDB, PostgreSQL).](#logic-to-connect-to-a-database-eg-mongodb-postgresql)

---

# Answers

## Beginner (Basics)

### <a id="reverse-a-string"></a>Reverse a string.
```typescript
const str = "hello";
console.log(str.split("").reverse().join("")); // "olleh"
```
[Back to Top](#beginner-basics)

### <a id="reverse-an-integer-number"></a>Reverse an integer number.
```typescript
const num = 123;
console.log(parseInt(num.toString().split("").reverse().join(""))); // 321
```
[Back to Top](#beginner-basics)

### <a id="count-vowels-in-a-string-eg-welcome"></a>Count vowels in a string (e.g., "welcome").
```typescript
const str = "welcome";
console.log(str.match(/[aeiou]/gi)?.length || 0); // 3
```
[Back to Top](#beginner-basics)

### <a id="print-vowels-from-a-string"></a>Print vowels from a string.
```typescript
const str = "welcome";
console.log(str.match(/[aeiou]/gi)?.join("")); // "eoe"
```
[Back to Top](#beginner-basics)

### <a id="find-the-maximum-and-minimum-numbers-in-an-array"></a>Find the maximum and minimum numbers in an array.
```typescript
const arr = [1, 5, 2, 8, 3];
console.log(Math.max(...arr), Math.min(...arr)); // 8 1
```
[Back to Top](#beginner-basics)

### <a id="swap-two-numbers-without-using-a-third-variable"></a>Swap two numbers without using a third variable.
```typescript
let a = 5, b = 10;
[a, b] = [b, a];
console.log(a, b); // 10 5
```
[Back to Top](#beginner-basics)

### <a id="find-the-count-of-letters-in-a-string-input-hello-"></a>Find the count of letters in a string (Input: " Hello ").
```typescript
const str = " Hello ";
console.log(str.trim().length); // 5
```
[Back to Top](#beginner-basics)

### <a id="replace---with--in-a-date-string-input-03-06-1995"></a>Replace '-' with '/' in a date string (Input: "03-06-1995").
```typescript
const date = "03-06-1995";
console.log(date.replace(/-/g, "/")); // "03/06/1995"
```
[Back to Top](#beginner-basics)

### <a id="how-to-get-system-date-and-time"></a>How to get system date and time?
```typescript
console.log(new Date().toString());
```
[Back to Top](#beginner-basics)

### <a id="convert-a-string-to-an-integer-input-123456"></a>Convert a string to an integer (Input: "123456").
```typescript
const str = "123456";
console.log(parseInt(str)); // 123456
```
[Back to Top](#beginner-basics)

### <a id="get-all-elements-from-an-array-using-a-loop"></a>Get all elements from an array using a loop.
```typescript
const arr = [1, 2, 3];
for (const item of arr) console.log(item);
```
[Back to Top](#beginner-basics)

## Intermediate (Intermediate Logic)

### <a id="reverse-a-string-word-by-word"></a>Reverse a string word by word.
```typescript
const str = "Hello World";
console.log(str.split(" ").reverse().join(" ")); // "World Hello"
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="count-duplicate-characters-in-a-string"></a>Count duplicate characters in a string.
```typescript
const str = "hello";
const counts: any = {};
for (const char of str) counts[char] = (counts[char] || 0) + 1;
const duplicates = Object.keys(counts).filter(k => counts[k] > 1);
console.log(duplicates.length); // 1 (l)
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="find-the-frequency-of-characters-in-a-string"></a>Find the frequency of characters in a string.
```typescript
const str = "hello";
const counts: any = {};
for (const char of str) counts[char] = (counts[char] || 0) + 1;
console.log(counts);
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="find-duplicate-words-in-a-string-eg-hexaware"></a>Find duplicate words in a string (e.g., "Hexaware").
```typescript
// Assuming "duplicate words" implies repeating characters or substrings?
// Or if it means input "Hexaware Hexaware"
const str = "Hexaware Hexaware";
const words = str.split(" ");
const duplicates = words.filter((w, i) => words.indexOf(w) !== i);
console.log(duplicates); // ["Hexaware"]
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="reverse-two-numbers-without-using-a-temporary-variable-input-x--10-y--20"></a>Reverse two numbers without using a temporary variable (Input: `x = 10`, `y = 20`).
```typescript
let x = 10, y = 20;
[x, y] = [y, x];
console.log(x, y); // 20 10
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="reverse-two-strings-without-using-a-temporary-variable-input-a--india-b--uk"></a>Reverse two strings without using a temporary variable (Input: `a = "India"`, `b = "uk"`).
```typescript
let a = "India", b = "uk";
[a, b] = [b, a];
console.log(a, b); // "uk" "India"
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="find-the-second-highest-number-in-an-array"></a>Find the second highest number in an array.
```typescript
const arr = [10, 20, 30, 20];
const sorted = [...new Set(arr)].sort((a, b) => b - a);
console.log(sorted[1]); // 20
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="find-duplicate-elements-in-an-array"></a>Find duplicate elements in an array.
```typescript
const arr = [1, 2, 3, 2, 1];
const duplicates = arr.filter((item, index) => arr.indexOf(item) !== index);
console.log([...new Set(duplicates)]); // [2, 1]
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="sort-an-array"></a>Sort an array.
```typescript
const arr = [3, 1, 2];
console.log(arr.sort()); // [1, 2, 3]
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="convert-an-array-to-a-list-or-setmap"></a>Convert an array to a list (or Set/Map).
```typescript
const arr = [1, 2, 3];
const set = new Set(arr);
console.log(set);
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="retrieve-key-value-pairs-from-a-map-or-object-input-x--a-y--b"></a>Retrieve key-value pairs from a `Map` or Object (Input: `X = "A", Y = "B"`).
```typescript
const obj = { X: "A", Y: "B" };
for (const [key, value] of Object.entries(obj)) {
    console.log(`${key}: ${value}`);
}
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="write-a-class-or-interface-for-username-and-password"></a>Write a class or interface for Username and Password.
```typescript
class UserCredentials {
    constructor(public username: string, private password: string) {}
}
const user = new UserCredentials("admin", "1234");
```
[Back to Top](#intermediate-intermediate-logic)

## Advanced (Advanced Algorithms & Logic)

### <a id="reverse-a-string-word-by-word-but-keep-word-position"></a>Reverse a string word by word but keep word position.
```typescript
const str = "Hello World";
console.log(str.split(" ").map(w => w.split("").reverse().join("")).join(" ")); // "olleH dlroW"
```
[Back to Top](#advanced-advanced-algorithms--logic)

### <a id="find-repeated-characters-in-the-word-assasination"></a>Find repeated characters in the word "ASSASINATION".
```typescript
const str = "ASSASINATION";
const counts: any = {};
for (const char of str) counts[char] = (counts[char] || 0) + 1;
const repeated = Object.keys(counts).filter(k => counts[k] > 1);
console.log(repeated); // ["S", "A", "I", "N"]
```
[Back to Top](#advanced-advanced-algorithms--logic)

### <a id="remove-duplicates-from-a-string-without-using-collection-concepts"></a>Remove duplicates from a string without using collection concepts.
```typescript
const str = "hello";
let unique = "";
for (let i = 0; i < str.length; i++) {
    if (unique.indexOf(str[i]) === -1) unique += str[i];
}
console.log(unique); // "helo"
```
[Back to Top](#advanced-advanced-algorithms--logic)

### <a id="anagram-check-determine-if-two-string-patterns-are-the-same-eg-cat-and-act"></a>Anagram check: Determine if two string patterns are the same (e.g., "CAT" and "ACT").
```typescript
const s1 = "CAT", s2 = "ACT";
console.log(s1.split("").sort().join("") === s2.split("").sort().join("")); // true
```
[Back to Top](#advanced-advanced-algorithms--logic)

### <a id="count-characters-numbers-and-special-characters-in-a-mixed-string"></a>Count characters, numbers, and special characters in a mixed string.
```typescript
const str = "Abc@123";
const chars = str.replace(/[^a-zA-Z]/g, "").length;
const nums = str.replace(/[^0-9]/g, "").length;
const specials = str.length - chars - nums;
console.log(chars, nums, specials); // 3 3 1
```
[Back to Top](#advanced-advanced-algorithms--logic)

### <a id="find-the-3rd-maximum-element-in-an-array"></a>Find the 3rd maximum element in an array.
```typescript
const arr = [10, 20, 30, 40, 50];
const sorted = [...new Set(arr)].sort((a, b) => b - a);
console.log(sorted[2]); // 30
```
[Back to Top](#advanced-advanced-algorithms--logic)

### <a id="sum-of-two-integer-arrays"></a>Sum of two integer arrays.
```typescript
const arr1 = [1, 2], arr2 = [3, 4];
const sum = [...arr1, ...arr2].reduce((a, b) => a + b, 0);
console.log(sum); // 10
```
[Back to Top](#advanced-advanced-algorithms--logic)

### <a id="find-common-duplicates-between-two-arrays"></a>Find common duplicates between two arrays.
```typescript
const arr1 = [1, 2, 3], arr2 = [3, 4, 5];
const common = arr1.filter(val => arr2.includes(val));
console.log(common); // [3]
```
[Back to Top](#advanced-advanced-algorithms--logic)

### <a id="logic-to-connect-to-a-database-eg-mongodb-postgresql"></a>Logic to connect to a database (e.g., MongoDB, PostgreSQL).
```typescript
// Conceptual MongoDB connection
import { MongoClient } from 'mongodb';

async function connect() {
    const url = 'mongodb://localhost:27017';
    const client = new MongoClient(url);
    try {
        await client.connect();
        console.log("Connected to database");
    } finally {
        await client.close();
    }
}
```
[Back to Top](#advanced-advanced-algorithms--logic)