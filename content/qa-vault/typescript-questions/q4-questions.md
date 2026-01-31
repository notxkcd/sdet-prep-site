---
title: "Questions - AiiTE Q Dump-Set_8_Update"
date: 2026-01-30
draft: false
---

# TypeScript Programming Interview Questions (Sorted by Difficulty) - AiiTE Q Dump-Set_8_Update.txt

## Beginner
- [Write a Palindrome program.](#write-a-palindrome-program)

## Intermediate
- [Input: `number[] = [1,0,0,2,0,0,0,3]`, Output: `[1,2,3,0,0,0]`. (Moving non-zero elements to the front).](#input-number--10020003-output-123000-moving-non-zero-elements-to-the-front)

---

# Answers

## Beginner

### <a id="write-a-palindrome-program"></a>Write a Palindrome program.
```typescript
function isPalindrome(str: string): boolean {
    const reversed = str.split("").reverse().join("");
    return str === reversed;
}
console.log(isPalindrome("madam")); // true
```
[Back to Top](#beginner)

## Intermediate

### <a id="input-number--10020003-output-123000-moving-non-zero-elements-to-the-front"></a>Input: `number[] = [1,0,0,2,0,0,0,3]`, Output: `[1,2,3,0,0,0]`. (Moving non-zero elements to the front).
```typescript
const arr = [1, 0, 0, 2, 0, 0, 0, 3];
const nonZeros = arr.filter(n => n !== 0);
const zeros = arr.filter(n => n === 0);
const result = [...nonZeros, ...zeros];
console.log(result); // [1, 2, 3, 0, 0, 0, 0, 0]
```
[Back to Top](#intermediate)