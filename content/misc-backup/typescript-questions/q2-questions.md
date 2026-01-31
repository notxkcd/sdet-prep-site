---
title: "Questions - AiiTE Q Dump-Set_6"
date: 2026-01-30
draft: false
---

# TypeScript Programming Interview Questions (Sorted by Difficulty) - AiiTE Q Dump-Set_6.txt

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
- [Find the second maximum number in an array.](#find-the-second-maximum-number-in-an-array)
- [Find the second largest number in an array.](#find-the-second-largest-number-in-an-array)
- [Find duplicate numbers in an array.](#find-duplicate-numbers-in-an-array)
- [Sort an array (Input: `number[] array`).](#sort-an-array-input-number-array)
- [Compare two arrays and get common values.](#compare-two-arrays-and-get-common-values)
- [Find the top value from an `Array` of 10 numbers.](#find-the-top-value-from-an-array-of-10-numbers)
- [Find the digit count in a long number (Input: `9662343497543`).](#find-the-digit-count-in-a-long-number-input-9662343497543)
- [Count prime numbers from 1 to 100.](#count-prime-numbers-from-1-to-100)
- [Extract the logic to get output `Slnium` from `Selenium`.](#extract-the-logic-to-get-output-slnium-from-selenium)
- [Predict output for String comparison (`==` vs `===`).](#predict-output-for-string-comparison-vs-)
- [Predict output for exception handling with try-catch.](#predict-output-for-exception-handling-with-try-catch)

## Advanced (Advanced Algorithms & Tricky Logic)
- [Remove special characters from a string without using a loop (Input: `@%^#%^%#qwertyt%^%^qwe123`).](#remove-special-characters-from-a-string-without-using-a-loop-input-qwertytqwe123)
- [Separate characters, special characters, and digits from a string and store them in arrays.](#separate-characters-special-characters-and-digits-from-a-string-and-store-them-in-arrays)
- [Reverse a string without using for loop conditions.](#reverse-a-string-without-using-for-loop-conditions)
- [Reverse each word in a string (Input: `I am sowmyashri`).](#reverse-each-word-in-a-string-input-i-am-sowmyashri)
- [Reverse a string (Input: `Welcome To LTImindtree`, Output: `LTImindtree To Welcome`).](#reverse-a-string-input-welcome-to-ltimindtree-output-ltimindtree-to-welcome)
- [Count the occurrence of each character in a string (Input: `Vivekanand`).](#count-the-occurrence-of-each-character-in-a-string-input-vivekanand)
- [Print the first non-repeating character in a string (Input: `interview`).](#print-the-first-non-repeating-character-in-a-string-input-interview)
- [Given input `Accenture`, output `EeRrUuTtNnEeCcCcAa` (Reverse and duplicate characters).](#given-input-accenture-output-eerruuttnneeccccaa-reverse-and-duplicate-characters)
- [Combine two string arrays and take the occurrence of each word.](#combine-two-string-arrays-and-take-the-occurrence-of-each-word)
- [Predict output for constructor chaining using `super()`.](#predict-output-for-constructor-chaining-using-super)
- [Predict output for `number[] a = {1,2,3,4,5,6,7,8,9,10}` to `[10,1,9,2,8,3,7,4,6,5]`.](#predict-output-for-number-a--12345678910-to-10192837465)

---

# Answers

## Beginner (Basic Manipulations & Logic)

### <a id="reverse-a-string-input-interview"></a>Reverse a string (Input: `inte*#rview*#`).
```typescript
const input = "inte*#rview*#";
const reversed = input.split("").reverse().join("");
console.log(reversed); // "#*weivr#*etni"
```
[Back to Top](#beginner-basic-manipulations--logic)

### <a id="remove-spaces-from-a-string"></a>Remove spaces from a string.
```typescript
const str = " Hello World ";
const noSpaces = str.replace(/\s+/g, "");
console.log(noSpaces); // "HelloWorld"
```
[Back to Top](#beginner-basic-manipulations--logic)

### <a id="print-vowels-in-a-given-string-input-my-name-is-gyan"></a>Print vowels in a given string (Input: `my name is gyan`).
```typescript
const str = "my name is gyan";
const vowels = str.match(/[aeiou]/gi);
console.log(vowels ? vowels.join("") : ""); // "aeia"
```
[Back to Top](#beginner-basic-manipulations--logic)

### <a id="check-if-a-number-is-even-or-odd"></a>Check if a number is even or odd.
```typescript
const num = 5;
if (num % 2 === 0) {
    console.log("Even");
} else {
    console.log("Odd");
}
```
[Back to Top](#beginner-basic-manipulations--logic)

### <a id="swap-two-numbers-without-using-a-third-variable"></a>Swap two numbers without using a third variable.
```typescript
let a = 10, b = 20;
a = a + b;
b = a - b;
a = a - b;
console.log(`a: ${a}, b: ${b}`); // a: 20, b: 10
```
[Back to Top](#beginner-basic-manipulations--logic)

### <a id="check-if-a-number-is-prime-or-not-input-11"></a>Check if a number is Prime or not (Input: `11`).
```typescript
function isPrime(n: number): boolean {
    if (n <= 1) return false;
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) return false;
    }
    return true;
}
console.log(isPrime(11)); // true
```
[Back to Top](#beginner-basic-manipulations--logic)

### <a id="fibonacci-series"></a>Fibonacci series.
```typescript
let n1 = 0, n2 = 1, nextTerm;
console.log(n1);
console.log(n2);
for (let i = 1; i <= 8; i++) {
    nextTerm = n1 + n2;
    console.log(nextTerm);
    n1 = n2;
    n2 = nextTerm;
}
```
[Back to Top](#beginner-basic-manipulations--logic)

### <a id="retrieve-the-date-from-a-sentence-input-today-date-is-7272024"></a>Retrieve the date from a sentence (Input: `Today date is 7/27/2024`).
```typescript
const text = "Today date is 7/27/2024";
const date = text.match(/\d{1,2}\/\d{1,2}\/\d{4}/);
console.log(date ? date[0] : "No date found"); // "7/27/2024"
```
[Back to Top](#beginner-basic-manipulations--logic)

### <a id="remove-unwanted-spaces-from-a-string"></a>Remove unwanted spaces from a string.
```typescript
const text = "  Hello   World  ";
const clean = text.trim().replace(/\s+/g, " ");
console.log(clean); // "Hello World"
```
[Back to Top](#beginner-basic-manipulations--logic)

### <a id="pattern-program"></a>Pattern program.
```typescript
/*
*
##
*
####
*/
console.log("*");
console.log("##");
console.log("*");
console.log("####");
```
[Back to Top](#beginner-basic-manipulations--logic)

## Intermediate (Intermediate Logic & Data Structures)

### <a id="check-if-a-string-is-a-palindrome-or-not-input-madam"></a>Check if a string is a Palindrome or not (Input: `madam`).
```typescript
const str = "madam";
const isPalindrome = str === str.split("").reverse().join("");
console.log(isPalindrome); // true
```
[Back to Top](#intermediate-intermediate-logic--data-structures)

### <a id="count-the-occurrence-of-a-character-input-nathiya-umapathi"></a>Count the occurrence of a character (Input: `Nathiya Umapathi`).
```typescript
const str = "Nathiya Umapathi";
const char = "a";
const count = str.toLowerCase().split(char).length - 1;
console.log(count); // 4 (a appears 4 times case-insensitive)
```
[Back to Top](#intermediate-intermediate-logic--data-structures)

### <a id="print-unique-values-from-a-string-input-aabbcdd"></a>Print unique values from a string (Input: `aabbcdd`).
```typescript
const str = "aabbcdd";
const unique = [...new Set(str.split(""))].join("");
console.log(unique); // "abcd"
```
[Back to Top](#intermediate-intermediate-logic--data-structures)

### <a id="change-uppercase-to-lowercase-and-vice-versa-input-java-selenium"></a>Change uppercase to lowercase and vice versa (Input: `JaVA SeLENium`).
```typescript
const str = "JaVA SeLENium";
const swapped = str.split("").map(c => 
    c === c.toUpperCase() ? c.toLowerCase() : c.toUpperCase()
).join("");
console.log(swapped); // "jAva sElenIUM"
```
[Back to Top](#intermediate-intermediate-logic--data-structures)

### <a id="find-the-second-maximum-number-in-an-array"></a>Find the second maximum number in an array.
```typescript
const arr = [10, 5, 20, 8];
const sorted = arr.sort((a, b) => b - a);
console.log(sorted[1]); // 10
```
[Back to Top](#intermediate-intermediate-logic--data-structures)

### <a id="find-the-second-largest-number-in-an-array"></a>Find the second largest number in an array.
```typescript
const arr = [10, 20, 30, 20, 40];
const uniqueSorted = [...new Set(arr)].sort((a, b) => b - a);
console.log(uniqueSorted[1]); // 30
```
[Back to Top](#intermediate-intermediate-logic--data-structures)

### <a id="find-duplicate-numbers-in-an-array"></a>Find duplicate numbers in an array.
```typescript
const arr = [1, 2, 3, 2, 4, 1];
const duplicates = arr.filter((item, index) => arr.indexOf(item) !== index);
console.log([...new Set(duplicates)]); // [2, 1]
```
[Back to Top](#intermediate-intermediate-logic--data-structures)

### <a id="sort-an-array-input-number-array"></a>Sort an array (Input: `number[] array`).
```typescript
const arr = [3, 1, 4, 2];
arr.sort((a, b) => a - b);
console.log(arr); // [1, 2, 3, 4]
```
[Back to Top](#intermediate-intermediate-logic--data-structures)

### <a id="compare-two-arrays-and-get-common-values"></a>Compare two arrays and get common values.
```typescript
const arr1 = [1, 2, 3, 4];
const arr2 = [3, 4, 5, 6];
const common = arr1.filter(val => arr2.includes(val));
console.log(common); // [3, 4]
```
[Back to Top](#intermediate-intermediate-logic--data-structures)

### <a id="find-the-top-value-from-an-array-of-10-numbers"></a>Find the top value from an `Array` of 10 numbers.
```typescript
const arr = [1, 5, 2, 8, 3, 9, 4, 7, 6, 0];
console.log(Math.max(...arr)); // 9
```
[Back to Top](#intermediate-intermediate-logic--data-structures)

### <a id="find-the-digit-count-in-a-long-number-input-9662343497543"></a>Find the digit count in a long number (Input: `9662343497543`).
```typescript
const num = 9662343497543;
console.log(num.toString().length); // 13
```
[Back to Top](#intermediate-intermediate-logic--data-structures)

### <a id="count-prime-numbers-from-1-to-100"></a>Count prime numbers from 1 to 100.
```typescript
let count = 0;
for (let i = 2; i <= 100; i++) {
    if (isPrime(i)) count++;
}
console.log(count);
```
[Back to Top](#intermediate-intermediate-logic--data-structures)

### <a id="extract-the-logic-to-get-output-slnium-from-selenium"></a>Extract the logic to get output `Slnium` from `Selenium`.
```typescript
const str = "Selenium";
const result = str.replace(/e/g, ""); // Removing 'e'
console.log(result); // "Slnium"
```
[Back to Top](#intermediate-intermediate-logic--data-structures)

### <a id="predict-output-for-string-comparison-vs-"></a>Predict output for String comparison (`==` vs `===`).
```typescript
const s1 = "hello";
const s2: any = new String("hello");
console.log(s1 == s2); // true (value check)
console.log(s1 === s2); // false (type check: string vs object)
```
[Back to Top](#intermediate-intermediate-logic--data-structures)

### <a id="predict-output-for-exception-handling-with-try-catch"></a>Predict output for exception handling with try-catch.
```typescript
try {
    const x = 10 / 0; // Infinity in JS, doesn't throw
    throw new Error("Custom error");
} catch (e) {
    console.log("Caught:", (e as Error).message);
} finally {
    console.log("Finally block executed");
}
```
[Back to Top](#intermediate-intermediate-logic--data-structures)

## Advanced (Advanced Algorithms & Tricky Logic)

### <a id="remove-special-characters-from-a-string-without-using-a-loop-input-qwertytqwe123"></a>Remove special characters from a string without using a loop (Input: `@%^#%^%#qwertyt%^%^qwe123`).
```typescript
const input = "@%^#%^%#qwertyt%^%^qwe123";
const clean = input.replace(/[^a-zA-Z0-9]/g, "");
console.log(clean); // "qwertytqwe123"
```
[Back to Top](#advanced-advanced-algorithms--tricky-logic)

### <a id="separate-characters-special-characters-and-digits-from-a-string-and-store-them-in-arrays"></a>Separate characters, special characters, and digits from a string and store them in arrays.
```typescript
const str = "Abc@123";
const chars = str.match(/[a-zA-Z]/g) || [];
const digits = str.match(/\d/g) || [];
const specials = str.match(/[^a-zA-Z0-9]/g) || [];
console.log(chars, digits, specials);
```
[Back to Top](#advanced-advanced-algorithms--tricky-logic)

### <a id="reverse-a-string-without-using-for-loop-conditions"></a>Reverse a string without using for loop conditions.
```typescript
function reverseRecursive(str: string): string {
    if (str === "") return "";
    return reverseRecursive(str.substr(1)) + str.charAt(0);
}
console.log(reverseRecursive("Hello")); // "olleH"
```
[Back to Top](#advanced-advanced-algorithms--tricky-logic)

### <a id="reverse-each-word-in-a-string-input-i-am-sowmyashri"></a>Reverse each word in a string (Input: `I am sowmyashri`).
```typescript
const str = "I am sowmyashri";
const reversed = str.split(" ").map(w => w.split("").reverse().join("")).join(" ");
console.log(reversed); // "I ma irhsaymwos"
```
[Back to Top](#advanced-advanced-algorithms--tricky-logic)

### <a id="reverse-a-string-input-welcome-to-ltimindtree-output-ltimindtree-to-welcome"></a>Reverse a string (Input: `Welcome To LTImindtree`, Output: `LTImindtree To Welcome`).
```typescript
const str = "Welcome To LTImindtree";
const reversed = str.split(" ").reverse().join(" ");
console.log(reversed); // "LTImindtree To Welcome"
```
[Back to Top](#advanced-advanced-algorithms--tricky-logic)

### <a id="count-the-occurrence-of-each-character-in-a-string-input-vivekanand"></a>Count the occurrence of each character in a string (Input: `Vivekanand`).
```typescript
const str = "Vivekanand";
const counts: any = {};
for (const char of str) {
    counts[char] = (counts[char] || 0) + 1;
}
console.log(counts);
```
[Back to Top](#advanced-advanced-algorithms--tricky-logic)

### <a id="print-the-first-non-repeating-character-in-a-string-input-interview"></a>Print the first non-repeating character in a string (Input: `interview`).
```typescript
const str = "interview";
for (const char of str) {
    if (str.indexOf(char) === str.lastIndexOf(char)) {
        console.log(char); // "n"
        break;
    }
}
```
[Back to Top](#advanced-advanced-algorithms--tricky-logic)

### <a id="given-input-accenture-output-eerruuttnneeccccaa-reverse-and-duplicate-characters"></a>Given input `Accenture`, output `EeRrUuTtNnEeCcCcAa` (Reverse and duplicate characters).
```typescript
const str = "Accenture";
let result = "";
for (let i = str.length - 1; i >= 0; i--) {
    const char = str[i];
    result += char.toUpperCase() + char.toLowerCase();
}
console.log(result); // "EeRrUuTtNnEeCcCcAa"
```
[Back to Top](#advanced-advanced-algorithms--tricky-logic)

### <a id="combine-two-string-arrays-and-take-the-occurrence-of-each-word"></a>Combine two string arrays and take the occurrence of each word.
```typescript
const arr1 = ["hello", "world"];
const arr2 = ["hello", "TypeScript"];
const combined = [...arr1, ...arr2];
const counts: any = {};
combined.forEach(word => counts[word] = (counts[word] || 0) + 1);
console.log(counts);
```
[Back to Top](#advanced-advanced-algorithms--tricky-logic)

### <a id="predict-output-for-constructor-chaining-using-super"></a>Predict output for constructor chaining using `super()`.
```typescript
class Parent {
    constructor() { console.log("Parent"); }
}
class Child extends Parent {
    constructor() {
        super();
        console.log("Child");
    }
}
new Child();
// Output:
// Parent
// Child
```
[Back to Top](#advanced-advanced-algorithms--tricky-logic)

### <a id="predict-output-for-number-a--12345678910-to-10192837465"></a>Predict output for `number[] a = {1,2,3,4,5,6,7,8,9,10}` to `[10,1,9,2,8,3,7,4,6,5]`.
```typescript
const a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const result: number[] = [];
let left = 0, right = a.length - 1;
while (left <= right) {
    if (left === right) {
        result.push(a[left]);
    } else {
        result.push(a[right]);
        result.push(a[left]);
    }
    left++;
    right--;
}
console.log(result); // [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
```
[Back to Top](#advanced-advanced-algorithms--tricky-logic)