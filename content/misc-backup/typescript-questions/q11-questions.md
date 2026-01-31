---
title: "Questions - Java Q_Set_1_and_2"
date: 2026-01-30
draft: false
---

# TypeScript Programming Interview Questions (Sorted by Difficulty) - Java Q_Set_1_and_2.txt

## Intermediate
- [Write a program to convert a `Map` (or Object) to an `Array`.](#write-a-program-to-convert-a-map-or-object-to-an-array)

## Advanced
- [Write a program using a `Map` (or Object) to find the number of occurrences of each character in a string.](#write-a-program-using-a-map-or-object-to-find-the-number-of-occurrences-of-each-character-in-a-string)

---

# Answers

## Intermediate

### <a id="write-a-program-to-convert-a-map-or-object-to-an-array"></a>Write a program to convert a `Map` (or Object) to an `Array`.
```typescript
// Object to Array
const obj = { a: 1, b: 2 };
console.log(Object.entries(obj)); // [["a", 1], ["b", 2]]
console.log(Object.keys(obj));    // ["a", "b"]
console.log(Object.values(obj));  // [1, 2]

// Map to Array
const map = new Map<string, number>();
map.set("a", 1);
map.set("b", 2);
console.log(Array.from(map)); // [["a", 1], ["b", 2]]
```
[Back to Top](#intermediate)

## Advanced

### <a id="write-a-program-using-a-map-or-object-to-find-the-number-of-occurrences-of-each-character-in-a-string"></a>Write a program using a `Map` (or Object) to find the number of occurrences of each character in a string.
```typescript
const str = "hello world";
const countMap = new Map<string, number>();

for (const char of str) {
    countMap.set(char, (countMap.get(char) || 0) + 1);
}

console.log(countMap); 
// Map { 'h' => 1, 'e' => 1, 'l' => 3, 'o' => 2, ' ' => 1, 'w' => 1, 'r' => 1, 'd' => 1 }
```
[Back to Top](#advanced)