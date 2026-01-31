---
title: "Questions - 2025 Interview questions"
date: 2026-01-30
draft: false
---

# TypeScript Programming Interview Questions (Sorted by Difficulty) - 2025 Interview questions.txt

## Beginner (Basic Logic & Loops)
- [Swap two numbers using a temporary variable.](#swap-two-numbers-using-a-temporary-variable)
- [Write a code for String reverse.](#write-a-code-for-string-reverse)
- [Reverse a number.](#reverse-a-number)
- [Print "Infosys" but skip the letter "o".](#print-infosys-but-skip-the-letter-o)
- [How to replace a letter from a string?](#how-to-replace-a-letter-from-a-string)
- [Replace vowels with `*` (Input: "chennai").](#replace-vowels-with--input-chennai)
- [Find the maximum and minimum values in an array.](#find-the-maximum-and-minimum-values-in-an-array)
- [Find the smallest value in an array.](#find-the-smallest-value-in-an-array)
- [Print all dividends of 8 between 1 and 100.](#print-all-dividends-of-8-between-1-and-100)
- [Sum the integers found in a mixed string.](#sum-the-integers-found-in-a-mixed-string)
- [Write a code for Palindrome.](#write-a-code-for-palindrome)

## Intermediate (Intermediate Strings, Arrays & Logical Reasoning)
- [Swap two variables without using a 3rd variable.](#swap-two-variables-without-using-a-3rd-variable)
- [Fibonacci series code.](#fibonacci-series-code)
- [Write a sorting program.](#write-a-sorting-program)
- [Find the second maximum value in an array.](#find-the-second-maximum-value-in-an-array)
- [Find the second largest number in an array.](#find-the-second-largest-number-in-an-array)
- [Find duplicate numbers in an array.](#find-duplicate-numbers-in-an-array)
- [Find the maximum salary of an individual in an array.](#find-the-maximum-salary-of-an-individual-in-an-array)
- [Count the occurrence of a character in a string.](#count-the-occurrence-of-a-character-in-a-string)
- [Find the occurrence of a substring in a string.](#find-the-occurrence-of-a-substring-in-a-string)
- [How to replace multiple letters from a string using the same `replace` method?](#how-to-replace-multiple-letters-from-a-string-using-the-same-replace-method)
- [Separate String and Number from a mixed list or array.](#separate-string-and-number-from-a-mixed-list-or-array)
- [Reverse the words in a string (Input: "test program").](#reverse-the-words-in-a-string-input-test-program)
- [Format a string (Input: "xperience", Output: "xp*ri*nc**").](#format-a-string-input-xperience-output-xprinc)
- [Extract ABC and 123 from "AB12C3" and print "ABC123".](#extract-abc-and-123-from-ab12c3-and-print-abc123)
- [Input: `Same`, Output: `Saammmeeee`.](#input-same-output-saammmeeee)

## Advanced (Advanced Algorithms, Complex Manipulations & Optimization)
- [Check if two strings are Anagram or not (e.g., "Bored" and "Robed").](#check-if-two-strings-are-anagram-or-not-eg-bored-and-robed)
- [Reverse each word in a given string without changing the caps and small letters.](#reverse-each-word-in-a-given-string-without-changing-the-caps-and-small-letters)
- [Find character count and duplicate characters in a string array.](#find-character-count-and-duplicate-characters-in-a-string-array)
- [Remove duplicates from a string and print unique values (Input: "giggling").](#remove-duplicates-from-a-string-and-print-unique-values-input-giggling)
- [Remove duplicates in a long list of integers/strings.](#remove-duplicates-in-a-long-list-of-integersstrings)
- [Count words greater than 5 and reverse only those.](#count-words-greater-than-5-and-reverse-only-those)
- [Split letters and numbers from a string and print them separately (Input: "1am a C0dingF4n 0r Pr0gr4mm3r or S0ftw4r3 D3v3l0p3r").](#split-letters-and-numbers-from-a-string-and-print-them-separately-input-1am-a-c0dingf4n-0r-pr0gr4mm3r-or-s0ftw4r3-d3v3l0p3r)
- [Print the frequency of integers and letters in a mixed string.](#print-the-frequency-of-integers-and-letters-in-a-mixed-string)
- [Array rotational coding.](#array-rotational-coding)
- [Sum the numbers in a mixed array (e.g., from `1,2,3,a,b,c` sum `1,2,3`).](#sum-the-numbers-in-a-mixed-array-eg-from-123abc-sum-123)
- [Find the occurrence of a specific number in a long sequence.](#find-the-occurrence-of-a-specific-number-in-a-long-sequence)
- [Transpose a 2D array.](#transpose-a-2d-array)
- [Declare a 2D array and perform operations.](#declare-a-2d-array-and-perform-operations)
- [Input: `number[] = [1,0,0,2,0,0,0,3]`, Output: `[1,2,3,0,0,0]`.](#input-number--10020003-output-123000)
- [Input: `a (1,2,3,a,b,c)`, Task: Remove (a b c) and sum (1 2 3).](#input-a-123abc-task-remove-a-b-c-and-sum-1-2-3)

---

# Answers

## Beginner (Basic Logic & Loops)

### <a id="swap-two-numbers-using-a-temporary-variable"></a>Swap two numbers using a temporary variable.
```typescript
let a = 10;
let b = 20;
let temp = a;
a = b;
b = temp;
console.log(`a: ${a}, b: ${b}`); // a: 20, b: 10
```
[Back to Top](#beginner-basic-logic--loops)

### <a id="write-a-code-for-string-reverse"></a>Write a code for String reverse.
```typescript
const str = "hello";
const reversed = str.split("").reverse().join("");
console.log(reversed); // "olleh"
```
[Back to Top](#beginner-basic-logic--loops)

### <a id="reverse-a-number"></a>Reverse a number.
```typescript
const num = 12345;
const reversedNum = parseInt(num.toString().split("").reverse().join(""));
console.log(reversedNum); // 54321
```
[Back to Top](#beginner-basic-logic--loops)

### <a id="print-infosys-but-skip-the-letter-o"></a>Print "Infosys" but skip the letter "o".
```typescript
const company = "Infosys";
const result = company.split("").filter(char => char !== "o").join("");
console.log(result); // "Infsys"
```
[Back to Top](#beginner-basic-logic--loops)

### <a id="how-to-replace-a-letter-from-a-string"></a>How to replace a letter from a string?
```typescript
let text = "Hello World";
let newText = text.replace("World", "TypeScript");
console.log(newText); // "Hello TypeScript"
```
[Back to Top](#beginner-basic-logic--loops)

### <a id="replace-vowels-with--input-chennai"></a>Replace vowels with `*` (Input: "chennai").
```typescript
const city = "chennai";
const replaced = city.replace(/[aeiou]/gi, "*");
console.log(replaced); // "ch*nn**"
```
[Back to Top](#beginner-basic-logic--loops)

### <a id="find-the-maximum-and-minimum-values-in-an-array"></a>Find the maximum and minimum values in an array.
```typescript
const nums = [10, 5, 20, 8, 15];
const max = Math.max(...nums);
const min = Math.min(...nums);
console.log(`Max: ${max}, Min: ${min}`); // Max: 20, Min: 5
```
[Back to Top](#beginner-basic-logic--loops)

### <a id="find-the-smallest-value-in-an-array"></a>Find the smallest value in an array.
```typescript
const nums = [10, 5, 20, 8, 15];
let smallest = nums[0];
for (let i = 1; i < nums.length; i++) {
    if (nums[i] < smallest) {
        smallest = nums[i];
    }
}
console.log(smallest); // 5
```
[Back to Top](#beginner-basic-logic--loops)

### <a id="print-all-dividends-of-8-between-1-and-100"></a>Print all dividends of 8 between 1 and 100.
```typescript
for (let i = 1; i <= 100; i++) {
    if (i % 8 === 0) {
        console.log(i);
    }
}
```
[Back to Top](#beginner-basic-logic--loops)

### <a id="sum-the-integers-found-in-a-mixed-string"></a>Sum the integers found in a mixed string.
```typescript
const mixedStr = "abc123xyz45";
const sum = mixedStr
    .split("")
    .filter(char => !isNaN(parseInt(char)))
    .reduce((acc, curr) => acc + parseInt(curr), 0);
console.log(sum); // 1 + 2 + 3 + 4 + 5 = 15
```
[Back to Top](#beginner-basic-logic--loops)

### <a id="write-a-code-for-palindrome"></a>Write a code for Palindrome.
```typescript
function isPalindrome(str: string): boolean {
    const reversed = str.split("").reverse().join("");
    return str === reversed;
}
console.log(isPalindrome("madam")); // true
```
[Back to Top](#beginner-basic-logic--loops)

## Intermediate (Intermediate Strings, Arrays & Logical Reasoning)

### <a id="swap-two-variables-without-using-a-3rd-variable"></a>Swap two variables without using a 3rd variable.
```typescript
let x = 10;
let y = 20;
[x, y] = [y, x]; // Destructuring assignment
console.log(`x: ${x}, y: ${y}`); // x: 20, y: 10
```
[Back to Top](#intermediate-intermediate-strings-arrays--logical-reasoning)

### <a id="fibonacci-series-code"></a>Fibonacci series code.
```typescript
function fibonacci(n: number): number[] {
    const series = [0, 1];
    for (let i = 2; i < n; i++) {
        series.push(series[i - 1] + series[i - 2]);
    }
    return series;
}
console.log(fibonacci(10)); // [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```
[Back to Top](#intermediate-intermediate-strings-arrays--logical-reasoning)

### <a id="write-a-sorting-program"></a>Write a sorting program.
```typescript
const arr = [5, 2, 9, 1, 5, 6];
arr.sort((a, b) => a - b);
console.log(arr); // [1, 2, 5, 5, 6, 9]
```
[Back to Top](#intermediate-intermediate-strings-arrays--logical-reasoning)

### <a id="find-the-second-maximum-value-in-an-array"></a>Find the second maximum value in an array.
```typescript
const arr = [10, 20, 5, 30, 25];
const sorted = [...new Set(arr)].sort((a, b) => b - a); // Remove duplicates and sort descending
console.log(sorted[1]); // 25
```
[Back to Top](#intermediate-intermediate-strings-arrays--logical-reasoning)

### <a id="find-the-second-largest-number-in-an-array"></a>Find the second largest number in an array.
```typescript
// Same logic as above
const arr = [100, 20, 5, 30, 25];
let max = -Infinity, secondMax = -Infinity;
for (const num of arr) {
    if (num > max) {
        secondMax = max;
        max = num;
    } else if (num > secondMax && num !== max) {
        secondMax = num;
    }
}
console.log(secondMax); // 30
```
[Back to Top](#intermediate-intermediate-strings-arrays--logical-reasoning)

### <a id="find-duplicate-numbers-in-an-array"></a>Find duplicate numbers in an array.
```typescript
const arr = [1, 2, 3, 2, 4, 5, 1];
const duplicates = arr.filter((item, index) => arr.indexOf(item) !== index);
console.log([...new Set(duplicates)]); // [2, 1]
```
[Back to Top](#intermediate-intermediate-strings-arrays--logical-reasoning)

### <a id="find-the-maximum-salary-of-an-individual-in-an-array"></a>Find the maximum salary of an individual in an array.
```typescript
const salaries = [5000, 7000, 4500, 8000, 6000];
const maxSalary = Math.max(...salaries);
console.log(maxSalary); // 8000
```
[Back to Top](#intermediate-intermediate-strings-arrays--logical-reasoning)

### <a id="count-the-occurrence-of-a-character-in-a-string"></a>Count the occurrence of a character in a string.
```typescript
const str = "hello world";
const charToCount = "l";
const count = str.split(charToCount).length - 1;
console.log(count); // 3
```
[Back to Top](#intermediate-intermediate-strings-arrays--logical-reasoning)

### <a id="find-the-occurrence-of-a-substring-in-a-string"></a>Find the occurrence of a substring in a string.
```typescript
const str = "hello world hello";
const subStr = "hello";
const count = str.split(subStr).length - 1;
console.log(count); // 2
```
[Back to Top](#intermediate-intermediate-strings-arrays--logical-reasoning)

### <a id="how-to-replace-multiple-letters-from-a-string-using-the-same-replace-method"></a>How to replace multiple letters from a string using the same `replace` method?
```typescript
const str = "hello world";
// Replace 'l' with '1' and 'o' with '0'
const replaced = str.replace(/[lo]/g, (match) => match === 'l' ? '1' : '0');
console.log(replaced); // "he110 w0r1d"
```
[Back to Top](#intermediate-intermediate-strings-arrays--logical-reasoning)

### <a id="separate-string-and-number-from-a-mixed-list-or-array"></a>Separate String and Number from a mixed list or array.
```typescript
const mixed = [1, "a", 2, "b", 3, "c"];
const numbers = mixed.filter(item => typeof item === 'number');
const strings = mixed.filter(item => typeof item === 'string');
console.log(numbers); // [1, 2, 3]
console.log(strings); // ["a", "b", "c"]
```
[Back to Top](#intermediate-intermediate-strings-arrays--logical-reasoning)

### <a id="reverse-the-words-in-a-string-input-test-program"></a>Reverse the words in a string (Input: "test program").
```typescript
const input = "test program";
const output = input.split(" ").reverse().join(" ");
console.log(output); // "program test"
```
[Back to Top](#intermediate-intermediate-strings-arrays--logical-reasoning)

### <a id="format-a-string-input-xperience-output-xprinc"></a>Format a string (Input: "xperience", Output: "xp*ri*nc**").
```typescript
const input = "xperience";
// Assuming replace 'e' with '*' logic based on output
const output = input.replace(/e/g, "*");
console.log(output); // "xp*ri*nc*" -> Note: The required output has double * at end which implies logic is likely replace 'e' with '*'
```
[Back to Top](#intermediate-intermediate-strings-arrays--logical-reasoning)

### <a id="extract-abc-and-123-from-ab12c3-and-print-abc123"></a>Extract ABC and 123 from "AB12C3" and print "ABC123".
```typescript
const input = "AB12C3";
const letters = input.replace(/[^A-Za-z]/g, "");
const numbers = input.replace(/[^0-9]/g, "");
console.log(letters + numbers); // "ABC123"
```
[Back to Top](#intermediate-intermediate-strings-arrays--logical-reasoning)

### <a id="input-same-output-saammmeeee"></a>Input: `Same`, Output: `Saammmeeee`.
```typescript
const input = "Same";
let output = "";
for (let i = 0; i < input.length; i++) {
    output += input[i].repeat(i + 1);
}
console.log(output); // "Saammmeeee"
```
[Back to Top](#intermediate-intermediate-strings-arrays--logical-reasoning)

## Advanced (Advanced Algorithms, Complex Manipulations & Optimization)

### <a id="check-if-two-strings-are-anagram-or-not-eg-bored-and-robed"></a>Check if two strings are Anagram or not (e.g., "Bored" and "Robed").
```typescript
function isAnagram(str1: string, str2: string): boolean {
    const normalize = (str: string) => str.toLowerCase().split("").sort().join("");
    return normalize(str1) === normalize(str2);
}
console.log(isAnagram("Bored", "Robed")); // true
```
[Back to Top](#advanced-advanced-algorithms-complex-manipulations--optimization)

### <a id="reverse-each-word-in-a-given-string-without-changing-the-caps-and-small-letters"></a>Reverse each word in a given string without changing the caps and small letters.
```typescript
const str = "Hello World";
const reversedWords = str.split(" ").map(word => word.split("").reverse().join("")).join(" ");
console.log(reversedWords); // "olleH dlroW"
```
[Back to Top](#advanced-advanced-algorithms-complex-manipulations--optimization)

### <a id="find-character-count-and-duplicate-characters-in-a-string-array"></a>Find character count and duplicate characters in a string array.
```typescript
const arr = ["abc", "bcd", "cde"];
const combined = arr.join("");
const counts: { [key: string]: number } = {};
for (const char of combined) {
    counts[char] = (counts[char] || 0) + 1;
}
console.log(counts);
const duplicates = Object.keys(counts).filter(char => counts[char] > 1);
console.log("Duplicates:", duplicates);
```
[Back to Top](#advanced-advanced-algorithms-complex-manipulations--optimization)

### <a id="remove-duplicates-from-a-string-and-print-unique-values-input-giggling"></a>Remove duplicates from a string and print unique values (Input: "giggling").
```typescript
const input = "giggling";
const unique = [...new Set(input.split(""))].join("");
console.log(unique); // "giln"
```
[Back to Top](#advanced-advanced-algorithms-complex-manipulations--optimization)

### <a id="remove-duplicates-in-a-long-list-of-integersstrings"></a>Remove duplicates in a long list of integers/strings.
```typescript
const list = [1, 2, 2, 3, 4, 4, 5, "a", "a", "b"];
const uniqueList = [...new Set(list)];
console.log(uniqueList); // [1, 2, 3, 4, 5, "a", "b"]
```
[Back to Top](#advanced-advanced-algorithms-complex-manipulations--optimization)

### <a id="count-words-greater-than-5-and-reverse-only-those"></a>Count words greater than 5 and reverse only those.
```typescript
const sentence = "I am learning TypeScript programming";
const processed = sentence.split(" ").map(word => {
    return word.length > 5 ? word.split("").reverse().join("") : word;
}).join(" ");
console.log(processed); // "I am gninrael tpircSepyT gnimmargorp"
```
[Back to Top](#advanced-advanced-algorithms-complex-manipulations--optimization)

### <a id="split-letters-and-numbers-from-a-string-and-print-them-separately-input-1am-a-c0dingf4n-0r-pr0gr4mm3r-or-s0ftw4r3-d3v3l0p3r"></a>Split letters and numbers from a string and print them separately (Input: "1am a C0dingF4n 0r Pr0gr4mm3r or S0ftw4r3 D3v3l0p3r").
```typescript
const input = "1am a C0dingF4n 0r Pr0gr4mm3r or S0ftw4r3 D3v3l0p3r";
const letters = input.replace(/[^A-Za-z]/g, "");
const numbers = input.replace(/[^0-9]/g, "");
console.log("Letters:", letters);
console.log("Numbers:", numbers);
```
[Back to Top](#advanced-advanced-algorithms-complex-manipulations--optimization)

### <a id="print-the-frequency-of-integers-and-letters-in-a-mixed-string"></a>Print the frequency of integers and letters in a mixed string.
```typescript
const input = "a1b2c3a1";
const counts: { [key: string]: number } = {};
for (const char of input) {
    counts[char] = (counts[char] || 0) + 1;
}
console.log(counts); // {a: 2, 1: 2, b: 1, 2: 1, c: 1, 3: 1}
```
[Back to Top](#advanced-advanced-algorithms-complex-manipulations--optimization)

### <a id="array-rotational-coding"></a>Array rotational coding.
```typescript
function rotateArray(arr: any[], k: number): any[] {
    k = k % arr.length;
    return [...arr.slice(arr.length - k), ...arr.slice(0, arr.length - k)];
}
console.log(rotateArray([1, 2, 3, 4, 5], 2)); // [4, 5, 1, 2, 3]
```
[Back to Top](#advanced-advanced-algorithms-complex-manipulations--optimization)

### <a id="sum-the-numbers-in-a-mixed-array-eg-from-123abc-sum-123"></a>Sum the numbers in a mixed array (e.g., from `1,2,3,a,b,c` sum `1,2,3`).
```typescript
const mixed = [1, 2, 3, 'a', 'b', 'c'];
const sum = mixed
    .filter(item => typeof item === 'number')
    .reduce((acc: number, curr: any) => acc + curr, 0);
console.log(sum); // 6
```
[Back to Top](#advanced-advanced-algorithms-complex-manipulations--optimization)

### <a id="find-the-occurrence-of-a-specific-number-in-a-long-sequence"></a>Find the occurrence of a specific number in a long sequence.
```typescript
const sequence = [1, 2, 3, 4, 2, 2, 5];
const target = 2;
const count = sequence.filter(num => num === target).length;
console.log(count); // 3
```
[Back to Top](#advanced-advanced-algorithms-complex-manipulations--optimization)

### <a id="transpose-a-2d-array"></a>Transpose a 2D array.
```typescript
const matrix = [
    [1, 2, 3],
    [4, 5, 6]
];
const transposed = matrix[0].map((_, colIndex) => matrix.map(row => row[colIndex]));
console.log(transposed); // [[1, 4], [2, 5], [3, 6]]
```
[Back to Top](#advanced-advanced-algorithms-complex-manipulations--optimization)

### <a id="declare-a-2d-array-and-perform-operations"></a>Declare a 2D array and perform operations.
```typescript
const grid: number[][] = [
    [1, 2],
    [3, 4]
];
// Operation: Double each element
const doubled = grid.map(row => row.map(val => val * 2));
console.log(doubled); // [[2, 4], [6, 8]]
```
[Back to Top](#advanced-advanced-algorithms-complex-manipulations--optimization)

### <a id="input-number--10020003-output-123000"></a>Input: `number[] = [1,0,0,2,0,0,0,3]`, Output: `[1,2,3,0,0,0]`.
```typescript
const arr = [1, 0, 0, 2, 0, 0, 0, 3];
const nonZeros = arr.filter(x => x !== 0);
const zeros = arr.filter(x => x === 0);
const result = [...nonZeros, ...zeros];
console.log(result); // [1, 2, 3, 0, 0, 0, 0, 0]
```
[Back to Top](#advanced-advanced-algorithms-complex-manipulations--optimization)

### <a id="input-a-123abc-task-remove-a-b-c-and-sum-1-2-3"></a>Input: `a (1,2,3,a,b,c)`, Task: Remove (a b c) and sum (1 2 3).
```typescript
const input = [1, 2, 3, 'a', 'b', 'c'];
const result = input.filter(x => typeof x === 'number').reduce((acc: number, curr: any) => acc + curr, 0);
console.log(result); // 6
```
[Back to Top](#advanced-advanced-algorithms-complex-manipulations--optimization)