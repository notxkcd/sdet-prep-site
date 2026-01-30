---
title: "Capgemini-5"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

Capgemini L1 face to face interview(programing)
---------------------------------------------
1. Input= giggling remove duplicate and print unique value alone 
2. Input = make the future you want 
Count the word greater than 5 and reverse only that output: make the erutuf you want
3. Print min and Max value in array

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. Input= giggling remove duplicate and print unique value alone
This means finding the unique characters in a string and printing them. A `LinkedHashSet` is ideal as it preserves insertion order while ensuring uniqueness.

```java
import java.util.LinkedHashSet;
import java.util.Set;

public class UniqueChars {
    public static void printUniqueCharacters(String input) {
        if (input == null || input.isEmpty()) {
            System.out.println("No characters to process.");
            return;
        }

        Set<Character> uniqueChars = new LinkedHashSet<>(); // Preserves order
        for (char c : input.toCharArray()) {
            uniqueChars.add(c);
        }

        System.out.print("Unique characters: ");
        for (Character c : uniqueChars) {
            System.out.print(c); // Output for "giggling": giling
        }
        System.out.println();
    }

    public static void main(String[] args) {
        printUniqueCharacters("giggling");
    }
}
```

### 2. Input = make the future you want Count the word greater than 5 and reverse only that output: make the erutuf you want
This combines splitting a sentence, checking word length, and reversing specific words.

```java
public class TransformSentence {
    public static String transform(String sentence) {
        if (sentence == null || sentence.isEmpty()) {
            return sentence;
        }

        String[] words = sentence.split(" ");
        StringBuilder result = new StringBuilder();

        for (String word : words) {
            if (word.length() > 5) {
                // Reverse the word if its length is greater than 5
                result.append(new StringBuilder(word).reverse().toString());
            } else {
                // Otherwise, append the word as is
                result.append(word);
            }
            result.append(" "); // Add a space after each word
        }
        return result.toString().trim(); // Trim trailing space
    }

    public static void main(String[] args) {
        System.out.println(transform("make the future you want"));
        // Expected output: make the erutuf you want
    }
}
```

### 3. Print min and Max value in array
A classic coding problem.

```java
import java.util.Arrays;

public class ArrayMinMax {
    public static void findMinAndMax(int[] arr) {
        if (arr == null || arr.length == 0) {
            System.out.println("Array is empty or null.");
            return;
        }

        // Using Java 8 Streams API (most concise)
        int min = Arrays.stream(arr).min().getAsInt();
        int max = Arrays.stream(arr).max().getAsInt();
        System.out.println("Min: " + min + ", Max: " + max);

        /* // Traditional loop approach
        int currentMin = arr[0];
        int currentMax = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < currentMin) {
                currentMin = arr[i];
            }
            if (arr[i] > currentMax) {
                currentMax = arr[i];
            }
        }
        System.out.println("Min (loop): " + currentMin + ", Max (loop): " + currentMax);
        */
    }

    public static void main(String[] args) {
        int[] numbers = {3, 1, 4, 1, 5, 9, 2, 6};
        findMinAndMax(numbers);
    }
}
```
Showing the Streams API approach demonstrates modern Java knowledge.
