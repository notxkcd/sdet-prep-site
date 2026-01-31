---
title: "Questions - AiiTE Q Dump-Set_7"
date: 2026-01-30
draft: false
---

# TypeScript Programming Interview Questions (Sorted by Difficulty) - AiiTE Q Dump-Set_7.txt

## Beginner (Basic Strings & Numbers)
- [Reverse a string.](#reverse-a-string)
- [Find the number of alphabets in a sentence.](#find-the-number-of-alphabets-in-a-sentence)
- [Separate numbers only from a string (Input: "09/24/2015").](#separate-numbers-only-from-a-string-input-09242015)
- [Write a Factorial program.](#write-a-factorial-program)
- [Swap two variables without using a 3rd variable.](#swap-two-variables-without-using-a-3rd-variable)
- [Star pattern program (e.g., Pyramid).](#star-pattern-program-eg-pyramid)
- [Write a program for an `Array` to add elements and remove the first one.](#write-a-program-for-an-array-to-add-elements-and-remove-the-first-one)
- [Write a program that generates an error (e.g., throw Error) and handles it.](#write-a-program-that-generates-an-error-eg-throw-error-and-handles-it)

## Intermediate (Intermediate Logic & Collections)
- [Reverse each word in a string (Input: "Good Girl").](#reverse-each-word-in-a-string-input-good-girl)
- [Remove duplicate words or characters from a string.](#remove-duplicate-words-or-characters-from-a-string)
- [Check if a string is a Palindrome.](#check-if-a-string-is-a-palindrome)
- [Find the second largest number in an array.](#find-the-second-largest-number-in-an-array)
- [Print descending order of an array.](#print-descending-order-of-an-array)
- [Sort an array in ascending order.](#sort-an-array-in-ascending-order)
- [Print non-repeating numbers in an array.](#print-non-repeating-numbers-in-an-array)
- [Write a program to loop through an `Array` using four different methods.](#write-a-program-to-loop-through-an-array-using-four-different-methods)
- [Demonstrate the use of the `finally` block in a program.](#demonstrate-the-use-of-the-finally-block-in-a-program)

## Advanced (Algorithms & Complex Logic)
- [Count the occurrence of each character in a string.](#count-the-occurrence-of-each-character-in-a-string)
- [Find the occurrence of every character in "Welcome to Wipro".](#find-the-occurrence-of-every-character-in-welcome-to-wipro)
- [Print all possible combinations of a string (Input: "abc").](#print-all-possible-combinations-of-a-string-input-abc)
- [Demonstrate throwing an error in a function and handling it.](#demonstrate-throwing-an-error-in-a-function-and-handling-it)

---

# Answers

## Beginner (Basic Strings & Numbers)

### <a id="reverse-a-string"></a>Reverse a string.
```typescript
const str = "Hello";
const reversed = str.split("").reverse().join("");
console.log(reversed); // "olleH"
```
[Back to Top](#beginner-basic-strings--numbers)

### <a id="find-the-number-of-alphabets-in-a-sentence"></a>Find the number of alphabets in a sentence.
```typescript
const sentence = "Hello World 123";
const alphaCount = sentence.replace(/[^a-zA-Z]/g, "").length;
console.log(alphaCount); // 10
```
[Back to Top](#beginner-basic-strings--numbers)

### <a id="separate-numbers-only-from-a-string-input-09242015"></a>Separate numbers only from a string (Input: "09/24/2015").
```typescript
const str = "09/24/2015";
const numbers = str.replace(/\D/g, ""); // Remove non-digits
console.log(numbers); // "09242015"
```
[Back to Top](#beginner-basic-strings--numbers)

### <a id="write-a-factorial-program"></a>Write a Factorial program.
```typescript
function factorial(n: number): number {
    if (n === 0 || n === 1) return 1;
    return n * factorial(n - 1);
}
console.log(factorial(5)); // 120
```
[Back to Top](#beginner-basic-strings--numbers)

### <a id="swap-two-variables-without-using-a-3rd-variable"></a>Swap two variables without using a 3rd variable.
```typescript
let a = 10, b = 20;
[a, b] = [b, a];
console.log(`a: ${a}, b: ${b}`); // a: 20, b: 10
```
[Back to Top](#beginner-basic-strings--numbers)

### <a id="star-pattern-program-eg-pyramid"></a>Star pattern program (e.g., Pyramid).
```typescript
const n = 5;
for (let i = 1; i <= n; i++) {
    let str = " ".repeat(n - i) + "* ".repeat(i);
    console.log(str);
}
/*
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
*/
```
[Back to Top](#beginner-basic-strings--numbers)

### <a id="write-a-program-for-an-array-to-add-elements-and-remove-the-first-one"></a>Write a program for an `Array` to add elements and remove the first one.
```typescript
const arr = [1, 2, 3];
arr.push(4); // Add to end
arr.shift(); // Remove from start
console.log(arr); // [2, 3, 4]
```
[Back to Top](#beginner-basic-strings--numbers)

### <a id="write-a-program-that-generates-an-error-eg-throw-error-and-handles-it"></a>Write a program that generates an error (e.g., throw Error) and handles it.
```typescript
try {
    throw new Error("Something went wrong");
} catch (error) {
    console.log("Caught:", (error as Error).message);
}
```
[Back to Top](#beginner-basic-strings--numbers)

## Intermediate (Intermediate Logic & Collections)

### <a id="reverse-each-word-in-a-string-input-good-girl"></a>Reverse each word in a string (Input: "Good Girl").
```typescript
const str = "Good Girl";
const reversed = str.split(" ").map(w => w.split("").reverse().join("")).join(" ");
console.log(reversed); // "dooG lriG"
```
[Back to Top](#intermediate-intermediate-logic--collections)

### <a id="remove-duplicate-words-or-characters-from-a-string"></a>Remove duplicate words or characters from a string.
```typescript
// Remove duplicate characters
const str = "banana";
const uniqueChars = [...new Set(str)].join("");
console.log(uniqueChars); // "ban"

// Remove duplicate words
const sentence = "hello world hello";
const uniqueWords = [...new Set(sentence.split(" "))].join(" ");
console.log(uniqueWords); // "hello world"
```
[Back to Top](#intermediate-intermediate-logic--collections)

### <a id="check-if-a-string-is-a-palindrome"></a>Check if a string is a Palindrome.
```typescript
const str = "racecar";
const isPal = str === str.split("").reverse().join("");
console.log(isPal); // true
```
[Back to Top](#intermediate-intermediate-logic--collections)

### <a id="find-the-second-largest-number-in-an-array"></a>Find the second largest number in an array.
```typescript
const arr = [10, 5, 20, 20, 8];
const uniqueSorted = [...new Set(arr)].sort((a, b) => b - a);
console.log(uniqueSorted[1]); // 10
```
[Back to Top](#intermediate-intermediate-logic--collections)

### <a id="print-descending-order-of-an-array"></a>Print descending order of an array.
```typescript
const arr = [1, 5, 3, 9];
arr.sort((a, b) => b - a);
console.log(arr); // [9, 5, 3, 1]
```
[Back to Top](#intermediate-intermediate-logic--collections)

### <a id="sort-an-array-in-ascending-order"></a>Sort an array in ascending order.
```typescript
const arr = [9, 5, 3, 1];
arr.sort((a, b) => a - b);
console.log(arr); // [1, 3, 5, 9]
```
[Back to Top](#intermediate-intermediate-logic--collections)

### <a id="print-non-repeating-numbers-in-an-array"></a>Print non-repeating numbers in an array.
```typescript
const arr = [1, 2, 2, 3, 4, 4, 5];
const nonRepeating = arr.filter(num => arr.indexOf(num) === arr.lastIndexOf(num));
console.log(nonRepeating); // [1, 3, 5]
```
[Back to Top](#intermediate-intermediate-logic--collections)

### <a id="write-a-program-to-loop-through-an-array-using-four-different-methods"></a>Write a program to loop through an `Array` using four different methods.
```typescript
const arr = [1, 2, 3];

// 1. For loop
for (let i = 0; i < arr.length; i++) console.log(arr[i]);

// 2. For...of
for (const item of arr) console.log(item);

// 3. ForEach
arr.forEach(item => console.log(item));

// 4. Map (creates new array, but iterates)
arr.map(item => console.log(item));
```
[Back to Top](#intermediate-intermediate-logic--collections)

### <a id="demonstrate-the-use-of-the-finally-block-in-a-program"></a>Demonstrate the use of the `finally` block in a program.
```typescript
try {
    console.log("Try block");
} catch (e) {
    console.log("Catch block");
} finally {
    console.log("Finally block (always executed)");
}
```
[Back to Top](#intermediate-intermediate-logic--collections)

## Advanced (Algorithms & Complex Logic)

### <a id="count-the-occurrence-of-each-character-in-a-string"></a>Count the occurrence of each character in a string.
```typescript
const str = "hello";
const counts: any = {};
for (const char of str) {
    counts[char] = (counts[char] || 0) + 1;
}
console.log(counts); // {h: 1, e: 1, l: 2, o: 1}
```
[Back to Top](#advanced-algorithms--complex-logic)

### <a id="find-the-occurrence-of-every-character-in-welcome-to-wipro"></a>Find the occurrence of every character in "Welcome to Wipro".
```typescript
const str = "Welcome to Wipro";
const counts: any = {};
for (const char of str.replace(/\s/g, "")) { // Ignoring spaces
    counts[char] = (counts[char] || 0) + 1;
}
console.log(counts);
```
[Back to Top](#advanced-algorithms--complex-logic)

### <a id="print-all-possible-combinations-of-a-string-input-abc"></a>Print all possible combinations of a string (Input: "abc").
```typescript
function combinations(str: string): string[] {
    if (str.length === 0) return [""];
    const firstChar = str[0];
    const rest = str.slice(1);
    const words = combinations(rest);
    const result: string[] = [];
    words.forEach(word => {
        for (let i = 0; i <= word.length; i++) {
            result.push(word.slice(0, i) + firstChar + word.slice(i));
        }
    });
    return result;
}
console.log(combinations("abc"));
// Note: This generates permutations. For strictly combinations (subsets), logic differs.
// Assuming permutations as "combinations" is often used interchangeably in interviews.
```
[Back to Top](#advanced-algorithms--complex-logic)

### <a id="demonstrate-throwing-an-error-in-a-function-and-handling-it"></a>Demonstrate throwing an error in a function and handling it.
```typescript
function divide(a: number, b: number): number {
    if (b === 0) throw new Error("Cannot divide by zero");
    return a / b;
}

try {
    divide(10, 0);
} catch (e) {
    console.log((e as Error).message);
}
```
[Back to Top](#advanced-algorithms--complex-logic)