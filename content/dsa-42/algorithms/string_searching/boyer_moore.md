---
title: "Boyer-Moore Algorithm"
---

The `Boyer-Moore Algorithm` is an efficient string searching algorithm that is often cited as the most efficient practical string-matching algorithm. Unlike naive approaches that compare characters from left to right, `Boyer-Moore` starts comparing from the rightmost character of the `pattern`.

Its main advantage comes from two `heuristics`: the **bad-character heuristic** and the **good-suffix heuristic**, which allow it to skip large portions of the `text`, especially when the alphabet size is large. This often results in sublinear time complexity in the average case.

## How it Works

### How it Works (Expanded)

The `Boyer-Moore Algorithm` preprocesses the `pattern` (but not the `text`) to generate two tables: the **bad-character shift table** and the **good-suffix shift table**. During searching, when a mismatch occurs, it calculates a shift for the pattern based on both `heuristics` and applies the larger of the two shifts.

---

Example: Search for Pattern "EXAMPLE" in Text "HERE IS A SIMPLE EXAMPLE"

1. Mismatch:
   Text:   ... SIMPLE EXA_MPLE
   Pattern:    EXAMPLE
                      ^
   'M' in text mismatches 'L' in pattern.

2. Bad-Character Heuristic:
- 'M' (bad character) is not in "EXAMPLE".
- Shift pattern past 'M' in text.

3. Good-Suffix Heuristic:
- "LE" (matched suffix) has an occurrence of "LE" elsewhere in "EXAMPLE".
- Shift pattern to align matched suffix.

The algorithm takes the maximum of the shifts proposed by these two heuristics.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
# Simple Boyer-Moore implementation focusing on the Bad Character Heuristic
# (Good Suffix Heuristic is more complex and often omitted for basic demos)

def build_bad_char_table(pattern):
    """
    Builds the bad character shift table.
    For each character, stores the index of its rightmost occurrence in the pattern.
    If a character is not in the pattern, it's considered to be -1.
    """
    bad_char = {}
    m = len(pattern)
    for i in range(m - 1): # Exclude last character for shifts
        bad_char[pattern[i]] = i
    return bad_char

def boyer_moore_search(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0: return []
    if n == 0 or m > n: return []

    bad_char_table = build_bad_char_table(pattern)
    results = []
    
    s = 0 # s is shift of the pattern with respect to text
    while s <= (n - m):
        j = m - 1 # Start comparing from rightmost character of pattern

        # Keep reducing index j of pattern while characters are matching
        # and j is not -1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        
        # If the pattern is found (j becomes -1)
        if j < 0:
            results.append(s)
            # Shift the pattern so that the next character in text aligns
            # with its last occurrence in pattern. If there's no next character
            # or it's not in bad_char_table, shift by 1.
            s += (m - bad_char_table.get(text[s + m], -1) if s + m < n else 1)
        else:
            # Character at text[s+j] did not match with pattern[j].
            # Shift the pattern.
            # max(1, j - bad_char_table.get(text[s + j], -1)):
            # 1. If bad character is not in pattern, bad_char_table.get returns -1.
            #    Shift is j - (-1) = j + 1.
            # 2. If bad character is in pattern, shift is j - last_occurrence_index.
            #    Take max(1, ...) to ensure at least a shift of 1.
            s += max(1, j - bad_char_table.get(text[s + j], -1))

    return results

# Example
# text = "ABAAABCD"
# pattern = "ABC"
# print(boyer_moore_search(text, pattern)) # [4]

# text2 = "TESTTEXT"
# pattern2 = "TEXT"
# print(boyer_moore_search(text2, pattern2)) # [4]
```

### Javascript

```javascript
function buildBadCharTable(pattern) {
    const badChar = new Map();
    const m = pattern.length;
    for (let i = 0; i < m - 1; i++) { // Exclude last character for shifts
        badChar.set(pattern[i], i);
    }
    return badChar;
}

function boyerMooreSearch(text, pattern) {
    const n = text.length;
    const m = pattern.length;
    if (m === 0) return [];
    if (n === 0 || m > n) return [];

    const badCharTable = buildBadCharTable(pattern);
    const results = [];
    
    let s = 0; // s is shift of the pattern with respect to text
    while (s <= (n - m)) {
        let j = m - 1; // Start comparing from rightmost character of pattern

        // Keep reducing index j of pattern while characters are matching
        // and j is not -1
        while (j >= 0 && pattern[j] === text[s + j]) {
            j--;
        }
        
        // If the pattern is found (j becomes -1)
        if (j < 0) {
            results.push(s);
            // Shift the pattern. If there's a next character in text that could
            // align with a pattern character, align it. Otherwise, shift by 1.
            // Simplified shift for basic bad-character-only implementation.
            s += (s + m < n && badCharTable.has(text[s + m])) ? m - badCharTable.get(text[s + m]) : 1;

        } else {
            // Character at text[s+j] did not match with pattern[j].
            // Shift the pattern using bad character heuristic.
            // badCharTable.get(text[s+j]) || -1: if char not in pattern, use -1.
            const lastOcc = badCharTable.has(text[s + j]) ? badCharTable.get(text[s + j]) : -1;
            s += Math.max(1, j - lastOcc);
        }
    }

    return results;
}

// const text = "ABAAABCD";
// const pattern = "ABC";
// console.log(boyerMooreSearch(text, pattern)); // [4]

// const text2 = "TESTTEXT";
// const pattern2 = "TEXT";
// console.log(boyerMooreSearch(text2, pattern2)); // [4]
```

### Typescript

```typescript
function buildBadCharTableTS(pattern: string): Map<string, number> {
    const badChar = new Map<string, number>();
    const m = pattern.length;
    for (let i = 0; i < m - 1; i++) { // Exclude last character for shifts
        badChar.set(pattern[i], i);
    }
    return badChar;
}

function boyerMooreSearchTS(text: string, pattern: string): number[] {
    const n = text.length;
    const m = pattern.length;
    if (m === 0) return [];
    if (n === 0 || m > n) return [];

    const badCharTable = buildBadCharTableTS(pattern);
    const results: number[] = [];
    
    let s = 0; // s is shift of the pattern with respect to text
    while (s <= (n - m)) {
        let j = m - 1; // Start comparing from rightmost character of pattern

        while (j >= 0 && pattern[j] === text[s + j]) {
            j--;
        }
        
        if (j < 0) {
            results.push(s);
            s += (s + m < n && badCharTable.has(text[s + m])) ? m - badCharTable.get(text[s + m])! : 1;

        } else {
            const lastOcc = badCharTable.has(text[s + j]) ? badCharTable.get(text[s + j])! : -1;
            s += Math.max(1, j - lastOcc);
        }
    }

    return results;
}

// const textTS = "ABAAABCD";
// const patternTS = "ABC";
// console.log(boyerMooreSearchTS(textTS, patternTS)); // [4]

// const text2TS = "TESTTEXT";
// const pattern2TS = "TEXT";
// console.log(boyerMooreSearchTS(text2TS, pattern2TS)); // [4]
```

### Cpp

```cpp
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <algorithm> // For std::max

// Max characters in alphabet (for ASCII)
const int ALPHABET_SIZE = 256;

void buildBadCharTable(const std::string& pattern, std::map<char, int>& bad_char) {
    int m = pattern.length();
    for (int i = 0; i < m - 1; i++) { // Exclude last character for shifts
        bad_char[pattern[i]] = i;
    }
}

std::vector<int> boyerMooreSearch(const std::string& text, const std::string& pattern) {
    int n = text.length();
    int m = pattern.length();
    if (m == 0) return {};
    if (n == 0 || m > n) return {};

    std::map<char, int> bad_char_table;
    buildBadCharTable(pattern, bad_char_table);
    std::vector<int> results;
    
    int s = 0; // s is shift of the pattern with respect to text
    while (s <= (n - m)) {
        int j = m - 1; // Start comparing from rightmost character of pattern

        while (j >= 0 && pattern[j] == text[s + j]) {
            j--;
        }
        
        if (j < 0) {
            results.push_back(s);
            // Shift the pattern. If there's a next character in text that could
            // align with a pattern character, align it. Otherwise, shift by 1.
            s += (s + m < n && bad_char_table.count(text[s + m])) ? m - bad_char_table[text[s + m]] : 1;

        } else {
            // Character at text[s+j] did not match with pattern[j].
            // Shift the pattern using bad character heuristic.
            int last_occ = bad_char_table.count(text[s + j]) ? bad_char_table[text[s + j]] : -1;
            s += std::max(1, j - last_occ);
        }
    }
    return results;
}

// int main() {
//     std::string text = "ABAAABCD";
//     std::string pattern = "ABC";
//     std::vector<int> matches = boyerMooreSearch(text, pattern);
//     for(int pos : matches) {
//         std::cout << "Pattern found at index " << pos << std::endl; // 4
//     }

//     std::string text2 = "TESTTEXT";
//     std::string pattern2 = "TEXT";
//     matches = boyerMooreSearch(text2, pattern2);
//     for(int pos : matches) {
//         std::cout << "Pattern found at index " << pos << std::endl; // 4
//     }
//     return 0;
// }
```

### Go

```go
package main

import "fmt"

func buildBadCharTable(pattern string) map[rune]int {
    badChar := make(map[rune]int)
    m := len(pattern)
    for i := 0; i < m-1; i++ { // Exclude last character for shifts
        badChar[rune(pattern[i])] = i
    }
    return badChar
}

func boyerMooreSearch(text, pattern string) []int {
    n := len(text)
    m := len(pattern)
    if m == 0 {
        return []int{}
    }
    if n == 0 || m > n {
        return []int{}
    }

    badCharTable := buildBadCharTable(pattern)
    results := []int{}
    
    s := 0 // s is shift of the pattern with respect to text
    for s <= (n - m) {
        j := m - 1 // Start comparing from rightmost character of pattern

        for j >= 0 && pattern[j] == text[s+j] {
            j--
        }
        
        if j < 0 {
            results = append(results, s)
            // Shift the pattern. Simplified shift for basic bad-character-only.
            // If there's a next character in text that could align with a pattern character, align it.
            // Otherwise, shift by 1.
            var nextCharShift int = 1
            if s+m < n {
                if val, ok := badCharTable[rune(text[s+m])]; ok {
                    nextCharShift = m - val
                }
            }
            s += nextCharShift
        } else {
            // Character at text[s+j] did not match with pattern[j].
            // Shift the pattern using bad character heuristic.
            var lastOcc int = -1
            if val, ok := badCharTable[rune(text[s+j])]; ok {
                lastOcc = val
            }
            s += max(1, j-lastOcc)
        }
    }

    return results
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

// func main() {
//     text := "ABAAABCD"
//     pattern := "ABC"
//     fmt.Println(boyerMooreSearch(text, pattern)) // [4]

//     text2 := "TESTTEXT"
//     pattern2 := "TEXT"
//     fmt.Println(boyerMooreSearch(text2, pattern2)) // [4]
// }
```

### D

```d
import std.stdio;
import std.array;
import std.algorithm; // For std.algorithm.max

// Simple Boyer-Moore implementation focusing on the Bad Character Heuristic
// (Good Suffix Heuristic is more complex and often omitted for basic demos)

int[char] buildBadCharTable(string pattern) {
    int[char] badChar;
    auto m = pattern.length;
    foreach (i; 0 .. m - 1) { // Exclude last character for shifts
        badChar[pattern[i]] = i;
    }
    return badChar;
}

int[] boyerMooreSearch(string text, string pattern) {
    auto n = text.length;
    auto m = pattern.length;
    if (m == 0) return [];
    if (n == 0 || m > n) return [];

    auto badCharTable = buildBadCharTable(pattern);
    int[] results;
    
    int s = 0; // s is shift of the pattern with respect to text
    while (s <= (n - m)) {
        int j = m - 1; // Start comparing from rightmost character of pattern

        // Keep reducing index j of pattern while characters are matching
        // and j is not -1
        while (j >= 0 && pattern[j] == text[s + j]) {
            j--;
        }
        
        // If the pattern is found (j becomes -1)
        if (j < 0) {
            results ~= s;
            // Shift the pattern. Simplified shift for basic bad-character-only.
            // If there's a next character in text that could align with a pattern character, align it.
            // Otherwise, shift by 1.
            int nextCharShift = 1;
            if (s + m < n) {
                if (auto p = text[s + m] in badCharTable) {
                    nextCharShift = m - </em>p;
                }
            }
            s += nextCharShift;

        } else {
            // Character at text[s+j] did not match with pattern[j].
            // Shift the pattern using bad character heuristic.
            int lastOcc = -1;
            if (auto p = text[s + j] in badCharTable) {
                lastOcc = *p;
            }
            s += max(1, j - lastOcc);
        }
    }

    return results;
}

// void main() {
//     string text = "ABAAABCD";
//     string pattern = "ABC";
//     writeln(boyerMooreSearch(text, pattern)); // [4]

//     string text2 = "TESTTEXT";
//     string pattern2 = "TEXT";
//     writeln(boyerMooreSearch(text2, pattern2)); // [4]
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

The `Boyer-Moore Algorithm` often uses two preprocessing steps and two `heuristics`. The provided code focuses on the simpler **bad-character heuristic** for demonstration.

---

**`buildBadCharTable(pattern)` Function:**
- This function creates a map (or `array` if the alphabet is small) that stores the last occurrence of each character in the `pattern`.
- For a character `c`, `bad_char_table[c]` stores its rightmost `index` in the `pattern`.
- This table is used when a mismatch occurs to determine how far to shift the `pattern`.

**`boyerMooreSearch(text, pattern)` Function:**
- `n`, `m`: Lengths of `text` and `pattern`.
- `s`: The current shift of the `pattern` with respect to the `text`.

**Search Loop:**
- The `while` loop continues as long as the `pattern` can still fit within the `text`.
- **Comparison:** Characters are compared from right to left, starting at `pattern[m-1]` and `text[s + m - 1]`. The `j` pointer moves leftwards.
- **Match Found:** If `j` becomes less than 0, it means the entire `pattern` has matched. The starting `index` `s` is recorded. The `pattern` is then shifted to find the next possible match. (The shift logic after a full match can be complex; a simplified shift by 1 or by using the `bad-character heuristic` with the character `text[s+m]` is often used for basic implementations.)
- **Mismatch Occurred:** If a mismatch is found at `pattern[j]` with `text[s + j]`:
- Consult the `bad_char_table` for the character `text[s + j]` (the "bad character").
- If the `bad character` `c` is not in the `pattern` (or its last occurrence is `last_occ = -1`), the `pattern` can be shifted `j + 1` positions to the right.
- If `c` is in the `pattern` at `index last_occ`, the `pattern` is shifted such that `pattern[last_occ]` aligns with `text[s + j]`. The shift amount is `j - last_occ`.
- The algorithm always takes `max(1, calculated_shift)` to ensure progress.

    </li>

[Back to Implementation](#implementation)

## Applications

### Application

The `Boyer-Moore Algorithm` is one of the most efficient string-matching algorithms in practice, especially for long `texts` and `patterns` and large alphabets.
- **Text Editors and Word Processors:** Widely used for implementing "find" functionality due to its speed.
- **Command-Line Utilities:** Tools like `grep` often use `Boyer-Moore` or its variants for fast text searching.
- **Compiler/Interpreter Lexical Analysis:** Searching for keywords and identifiers in source code.
- **Intrusion Detection Systems (IDS):** Scanning network traffic for known attack signatures, where `patterns` can be quite long.
- **Bioinformatics:** Searching for genetic sequences.

