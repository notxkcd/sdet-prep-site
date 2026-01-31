---
title: "Questions - Aiite Q Dump - Set_3"
date: 2026-01-30
draft: false
---

# TypeScript Programming Interview Questions (Sorted by Difficulty) - Aiite Q Dump - Set_3.txt

## Beginner (Basics)
- [Write a program to reverse a string.](#write-a-program-to-reverse-a-string)
- [Write a program to find odd numbers in an array.](#write-a-program-to-find-odd-numbers-in-an-array)
- [Write a program demonstrating a Class Constructor and its uses.](#write-a-program-demonstrating-a-class-constructor-and-its-uses)

## Intermediate (Logical Reasoning)
- [Reverse a string word by word.](#reverse-a-string-word-by-word)
- [Identify repeated characters in a string.](#identify-repeated-characters-in-a-string)
- [Find duplicate elements/characters in a string.](#find-duplicate-elementscharacters-in-a-string)
- [Write a program demonstrating Function Overloading.](#write-a-program-demonstrating-function-overloading)
- [Write a pattern program (Generic).](#write-a-pattern-program-generic)

## Advanced (Advanced Algorithms & Logic)
- [Change the first letter of every word in a sentence to uppercase.](#change-the-first-letter-of-every-word-in-a-sentence-to-uppercase)
- [Combine two integer arrays into a third array, then extract only the odd numbers into a fourth array.](#combine-two-integer-arrays-into-a-third-array-then-extract-only-the-odd-numbers-into-a-fourth-array)

---

# Answers

## Beginner (Basics)

### <a id="write-a-program-to-reverse-a-string"></a>Write a program to reverse a string.
```typescript
const str = "hello";
console.log(str.split("").reverse().join("")); // "olleh"
```
[Back to Top](#beginner-basics)

### <a id="write-a-program-to-find-odd-numbers-in-an-array"></a>Write a program to find odd numbers in an array.
```typescript
const arr = [1, 2, 3, 4, 5];
const odds = arr.filter(n => n % 2 !== 0);
console.log(odds); // [1, 3, 5]
```
[Back to Top](#beginner-basics)

### <a id="write-a-program-demonstrating-a-class-constructor-and-its-uses"></a>Write a program demonstrating a Class Constructor and its uses.
```typescript
class Car {
    constructor(public model: string) {
        console.log(`Car model ${model} created`);
    }
}
const car = new Car("Tesla");
```
[Back to Top](#beginner-basics)

## Intermediate (Logical Reasoning)

### <a id="reverse-a-string-word-by-word"></a>Reverse a string word by word.
```typescript
const str = "Hello World";
console.log(str.split(" ").reverse().join(" ")); // "World Hello"
```
[Back to Top](#intermediate-logical-reasoning)

### <a id="identify-repeated-characters-in-a-string"></a>Identify repeated characters in a string.
```typescript
const str = "hello";
const counts: any = {};
for (const char of str) counts[char] = (counts[char] || 0) + 1;
console.log(Object.keys(counts).filter(k => counts[k] > 1)); // ["l"]
```
[Back to Top](#intermediate-logical-reasoning)

### <a id="find-duplicate-elementscharacters-in-a-string"></a>Find duplicate elements/characters in a string.
```typescript
const str = "hello";
// Same logic as above
const counts: any = {};
for (const char of str) counts[char] = (counts[char] || 0) + 1;
console.log(Object.keys(counts).filter(k => counts[k] > 1));
```
[Back to Top](#intermediate-logical-reasoning)

### <a id="write-a-program-demonstrating-function-overloading"></a>Write a program demonstrating Function Overloading.
```typescript
function add(a: number, b: number): number;
function add(a: string, b: string): string;
function add(a: any, b: any): any {
    return a + b;
}
console.log(add(1, 2)); // 3
console.log(add("Hello", "World")); // "HelloWorld"
```
[Back to Top](#intermediate-logical-reasoning)

### <a id="write-a-pattern-program-generic"></a>Write a pattern program (Generic).
```typescript
/*
*
**
***
*/
for (let i = 1; i <= 3; i++) {
    console.log("*".repeat(i));
}
```
[Back to Top](#intermediate-logical-reasoning)

## Advanced (Advanced Algorithms & Logic)

### <a id="change-the-first-letter-of-every-word-in-a-sentence-to-uppercase"></a>Change the first letter of every word in a sentence to uppercase.
```typescript
const sentence = "hello world";
const capitalized = sentence.split(" ").map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(" ");
console.log(capitalized); // "Hello World"
```
[Back to Top](#advanced-advanced-algorithms--logic)

### <a id="combine-two-integer-arrays-into-a-third-array-then-extract-only-the-odd-numbers-into-a-fourth-array"></a>Combine two integer arrays into a third array, then extract only the odd numbers into a fourth array.
```typescript
const arr1 = [1, 2], arr2 = [3, 4];
const arr3 = [...arr1, ...arr2];
const arr4 = arr3.filter(n => n % 2 !== 0);
console.log(arr4); // [1, 3]
```
[Back to Top](#advanced-advanced-algorithms--logic)