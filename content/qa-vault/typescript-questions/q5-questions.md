---
title: "Questions - Aiite Q Dump - Set_1"
date: 2026-01-30
draft: false
---

# TypeScript Programming Interview Questions (Sorted by Difficulty) - Aiite Q Dump - Set_1.txt

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
- [Write code to read data from a JSON or configuration file.](#write-code-to-read-data-from-a-json-or-configuration-file)

## Intermediate (Intermediate Logic)
- [Count vowels and non-vowels in a string.](#count-vowels-and-non-vowels-in-a-string)
- [Count the frequency of a letter in a string.](#count-the-frequency-of-a-letter-in-a-string)
- [Fibonacci series.](#fibonacci-series)
- [Check if a number is an Armstrong number.](#check-if-a-number-is-an-armstrong-number)
- [Sort an `Array` in ascending order.](#sort-an-array-in-ascending-order)
- [Separate numbers and alphabets from a mixed string.](#separate-numbers-and-alphabets-from-a-mixed-string)
- [Count digits of 'a' in a sentence (Input: "My name is vaishnavi and I am working in Wipro").](#count-digits-of-a-in-a-sentence-input-my-name-is-vaishnavi-and-i-am-working-in-wipro)
- [How to replace '.' with a space in an email only between names (not after @).](#how-to-replace--with-a-space-in-an-email-only-between-names-not-after-)
- [Reverse a string in different ways: "Deepak Kumar" -> "Kumar Deepak" (Swap words).](#reverse-a-string-in-different-ways-deepak-kumar-kumar-deepak-swap-words)
- [Write a class for: `const b1 = new Book("Stephen Hawking"); const b2 = new Book(6);`.](#write-a-class-for-const-b1--new-bookstephen-hawking-const-b2--new-book6)

## Advanced (Algorithms & Complex Challenges)
- [Reverse each word in a string but keep the word position (Input: "Java is a programming language").](#reverse-each-word-in-a-string-but-keep-the-word-position-input-java-is-a-programming-language)
- [Reverse a string (Input: "Deepak Kumar", Output: "kapeed ramuk").](#reverse-a-string-input-deepak-kumar-output-kapeed-ramuk)
- [Count the occurrence of each character in a string.](#count-the-occurrence-of-each-character-in-a-string)
- [Remove all special characters from a string and print only alphanumeric characters.](#remove-all-special-characters-from-a-string-and-print-only-alphanumeric-characters)
- [Remove duplicates from a string without using Set or built-in methods.](#remove-duplicates-from-a-string-without-using-set-or-built-in-methods)
- [Input: `const name = a2b3c2`, Output: `aabbbcc`.](#input-const-name--a2b3c2-output-aabbbcc)
- [Sort a 2D array: `number[][]={{2,4,5},{3,4,7},{1,2,9}}`.](#sort-a-2d-array-number245347129)
- [Can you execute a method without writing a `main` function (top-level code)?](#can-you-execute-a-method-without-writing-a-main-function-top-level-code)
- [Logic to count duplicates in "babcadaefhef".](#logic-to-count-duplicates-in-babcadaefhef)

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
const num = 12345;
console.log(parseInt(num.toString().split("").reverse().join(""))); // 54321
```
[Back to Top](#beginner-basics)

### <a id="count-the-number-of-letters-in-a-given-string-eg-hello-5"></a>Count the number of letters in a given string (e.g., "Hello" -> 5).
```typescript
const str = "Hello";
console.log(str.length); // 5
```
[Back to Top](#beginner-basics)

### <a id="factorial-program"></a>Factorial program.
```typescript
function factorial(n: number): number {
    return n <= 1 ? 1 : n * factorial(n - 1);
}
console.log(factorial(5)); // 120
```
[Back to Top](#beginner-basics)

### <a id="swap-two-variables-without-using-a-3rd-variable"></a>Swap two variables without using a 3rd variable.
```typescript
let a = 1, b = 2;
[a, b] = [b, a];
console.log(a, b); // 2 1
```
[Back to Top](#beginner-basics)

### <a id="find-the-minimum-and-maximum-value-in-a-collection-of-numbers"></a>Find the minimum and maximum value in a collection of numbers.
```typescript
const nums = [1, 5, 2, 8, 3];
console.log(Math.min(...nums), Math.max(...nums)); // 1 8
```
[Back to Top](#beginner-basics)

### <a id="check-if-a-number-is-a-palindrome"></a>Check if a number is a Palindrome.
```typescript
const num = 121;
console.log(num.toString() === num.toString().split("").reverse().join("")); // true
```
[Back to Top](#beginner-basics)

### <a id="check-if-a-string-is-a-palindrome"></a>Check if a string is a Palindrome.
```typescript
const str = "madam";
console.log(str === str.split("").reverse().join("")); // true
```
[Back to Top](#beginner-basics)

### <a id="check-if-a-number-is-a-prime-number"></a>Check if a number is a Prime number.
```typescript
function isPrime(n: number): boolean {
    if (n < 2) return false;
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) return false;
    }
    return true;
}
console.log(isPrime(7)); // true
```
[Back to Top](#beginner-basics)

### <a id="write-code-to-read-data-from-a-json-or-configuration-file"></a>Write code to read data from a JSON or configuration file.
```typescript
import * as fs from 'fs';
try {
    const data = fs.readFileSync('config.json', 'utf8');
    const config = JSON.parse(data);
    console.log(config);
} catch (err) {
    console.error(err);
}
```
[Back to Top](#beginner-basics)

## Intermediate (Intermediate Logic)

### <a id="count-vowels-and-non-vowels-in-a-string"></a>Count vowels and non-vowels in a string.
```typescript
const str = "hello world";
const vowels = str.match(/[aeiou]/gi)?.length || 0;
const nonVowels = str.replace(/[^a-z]/gi, "").length - vowels;
console.log(`Vowels: ${vowels}, Non-vowels: ${nonVowels}`); // Vowels: 3, Non-vowels: 7
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="count-the-frequency-of-a-letter-in-a-string"></a>Count the frequency of a letter in a string.
```typescript
const str = "hello";
console.log(str.split("l").length - 1); // 2
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="fibonacci-series"></a>Fibonacci series.
```typescript
const fib = [0, 1];
for (let i = 2; i < 10; i++) fib.push(fib[i - 1] + fib[i - 2]);
console.log(fib);
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="check-if-a-number-is-an-armstrong-number"></a>Check if a number is an Armstrong number.
```typescript
const num = 153;
const sum = num.toString().split("").reduce((acc, digit) => acc + Math.pow(parseInt(digit), 3), 0);
console.log(sum === num); // true
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="sort-an-array-in-ascending-order"></a>Sort an `Array` in ascending order.
```typescript
const arr = [3, 1, 4, 1, 5];
console.log(arr.sort((a, b) => a - b)); // [1, 1, 3, 4, 5]
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="separate-numbers-and-alphabets-from-a-mixed-string"></a>Separate numbers and alphabets from a mixed string.
```typescript
const str = "a1b2c3";
const nums = str.replace(/\D/g, "");
const alphas = str.replace(/\d/g, "");
console.log(nums, alphas); // "123" "abc"
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="count-digits-of-a-in-a-sentence-input-my-name-is-vaishnavi-and-i-am-working-in-wipro"></a>Count digits of 'a' in a sentence (Input: "My name is vaishnavi and I am working in Wipro").
```typescript
const str = "My name is vaishnavi and I am working in Wipro";
console.log(str.toLowerCase().split("a").length - 1); // 4
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="how-to-replace--with-a-space-in-an-email-only-between-names-not-after-"></a>How to replace '.' with a space in an email only between names (not after @).
```typescript
const email = "john.doe@example.com";
const [namePart, domainPart] = email.split("@");
const newNamePart = namePart.replace(/\./g, " ");
console.log(`${newNamePart}@${domainPart}`); // "john doe@example.com"
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="reverse-a-string-in-different-ways-deepak-kumar-kumar-deepak-swap-words"></a>Reverse a string in different ways: "Deepak Kumar" -> "Kumar Deepak" (Swap words).
```typescript
const name = "Deepak Kumar";
console.log(name.split(" ").reverse().join(" ")); // "Kumar Deepak"
```
[Back to Top](#intermediate-intermediate-logic)

### <a id="write-a-class-for-const-b1--new-bookstephen-hawking-const-b2--new-book6"></a>Write a class for: `const b1 = new Book("Stephen Hawking"); const b2 = new Book(6);`.
```typescript
class Book {
    constructor(arg: string | number) {
        console.log(`Book created with: ${arg}`);
    }
}
const b1 = new Book("Stephen Hawking");
const b2 = new Book(6);
```
[Back to Top](#intermediate-intermediate-logic)

## Advanced (Algorithms & Complex Challenges)

### <a id="reverse-each-word-in-a-string-but-keep-the-word-position-input-java-is-a-programming-language"></a>Reverse each word in a string but keep the word position (Input: "Java is a programming language").
```typescript
const str = "Java is a programming language";
console.log(str.split(" ").map(w => w.split("").reverse().join("")).join(" ")); // "avaJ si a gnimmargorp egaugnal"
```
[Back to Top](#advanced-algorithms--complex-challenges)

### <a id="reverse-a-string-input-deepak-kumar-output-kapeed-ramuk"></a>Reverse a string (Input: "Deepak Kumar", Output: "kapeed ramuk").
```typescript
const str = "Deepak Kumar";
// This is effectively the same as "Reverse each word"
console.log(str.split(" ").map(w => w.split("").reverse().join("")).join(" "));
```
[Back to Top](#advanced-algorithms--complex-challenges)

### <a id="count-the-occurrence-of-each-character-in-a-string"></a>Count the occurrence of each character in a string.
```typescript
const str = "hello";
const counts: any = {};
for (const char of str) counts[char] = (counts[char] || 0) + 1;
console.log(counts);
```
[Back to Top](#advanced-algorithms--complex-challenges)

### <a id="remove-all-special-characters-from-a-string-and-print-only-alphanumeric-characters"></a>Remove all special characters from a string and print only alphanumeric characters.
```typescript
const str = "Hello@#$World123";
console.log(str.replace(/[^a-z0-9]/gi, "")); // "HelloWorld123"
```
[Back to Top](#advanced-algorithms--complex-challenges)

### <a id="remove-duplicates-from-a-string-without-using-set-or-built-in-methods"></a>Remove duplicates from a string without using Set or built-in methods.
```typescript
const str = "hello";
let unique = "";
for (const char of str) {
    if (unique.indexOf(char) === -1) unique += char;
}
console.log(unique); // "helo"
```
[Back to Top](#advanced-algorithms--complex-challenges)

### <a id="input-const-name--a2b3c2-output-aabbbcc"></a>Input: `const name = a2b3c2`, Output: `aabbbcc`.
```typescript
const input = "a2b3c2";
let output = "";
for (let i = 0; i < input.length; i += 2) {
    const char = input[i];
    const count = parseInt(input[i + 1]);
    output += char.repeat(count);
}
console.log(output); // "aabbbcc"
```
[Back to Top](#advanced-algorithms--complex-challenges)

### <a id="sort-a-2d-array-number245347129"></a>Sort a 2D array: `number[][]={{2,4,5},{3,4,7},{1,2,9}}`.
```typescript
const arr = [[2, 4, 5], [3, 4, 7], [1, 2, 9]];
// Flatten, sort, then reconstruct or sort rows based on a criteria?
// Usually means sorting based on first element of each row
arr.sort((a, b) => a[0] - b[0]);
console.log(arr); // [[1, 2, 9], [2, 4, 5], [3, 4, 7]]
```
[Back to Top](#advanced-algorithms--complex-challenges)

### <a id="can-you-execute-a-method-without-writing-a-main-function-top-level-code"></a>Can you execute a method without writing a `main` function (top-level code)?
```typescript
// In TypeScript/JS, yes, code executes top-down.
// Also, static blocks in classes execute when class is loaded.
class Test {
    static {
        console.log("Static initialization block executed");
    }
}
```
[Back to Top](#advanced-algorithms--complex-challenges)

### <a id="logic-to-count-duplicates-in-babcadaefhef"></a>Logic to count duplicates in "babcadaefhef".
```typescript
const str = "babcadaefhef";
const counts: any = {};
for (const char of str) counts[char] = (counts[char] || 0) + 1;
const duplicates = Object.keys(counts).filter(k => counts[k] > 1);
console.log(duplicates); // ["b", "a", "e", "f"] (approx)
```
[Back to Top](#advanced-algorithms--complex-challenges)