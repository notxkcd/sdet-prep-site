---
title: "Knuth-Morris-Pratt (KMP)"
---

The `Knuth-Morris-Pratt (KMP)` algorithm is a highly efficient string searching algorithm that finds the occurrences of a "`pattern`" within a "`text`". It is famous for its ability to avoid re-comparing characters that were already matched. When a mismatch occurs, it uses a precomputed table (often called a "`prefix function`" or "`LPS array`") to intelligently shift the pattern, rather than naively shifting by one position.

This preprocessing step allows the main search phase to run in `O(N)` time, where `N` is the length of the text, resulting in a total time complexity of `O(N + M)`, where `M` is the length of the pattern. This is a significant improvement over the naive `O(N<em>M)` approach.

## How it Works

### How it Works (Expanded)

The core idea of `KMP` is the "`Longest Proper Prefix that is also a Suffix`" (LPS) array. A "proper prefix" is any prefix of a string other than the string itself. The `LPS` array tells us, for each position in the pattern, the length of the longest proper prefix of the pattern's substring `pattern[0...i]` that is also a suffix of that substring.

---

Example: LPS array for pattern "ababaca"
- "a":       LPS = 0
- "ab":      LPS = 0
- "aba":     LPS = 1 ("a")
- "abab":    LPS = 2 ("ab")
- "ababa":   LPS = 3 ("aba")
- "ababac":  LPS = 0
- "ababaca": LPS = 1 ("a")

LPS Array: [0, 0, 1, 2, 3, 0, 1]

How it's used: If a mismatch occurs at `pattern[i]` while comparing against `text`, we don't have to go back in the `text`. We can consult `LPS[i-1]` to know how many characters we can "skip" in the pattern, as they are guaranteed to match.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
def compute_lps_array(pattern):
    m = len(pattern)
    lps = [0] </em> m
    length = 0  # Length of the previous longest prefix suffix
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps_array(pattern)
    i = 0  # index for text
    j = 0  # index for pattern
    results = []

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            results.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return results

# Example
# text = "ABABDABACDABABCABAB"
# pattern = "ABABCABAB"
# print(kmp_search(text, pattern)) # [10]
```

### Javascript

```javascript
function computeLPSArray(pattern) {
    const m = pattern.length;
    const lps = new Array(m).fill(0);
    let length = 0;
    let i = 1;

    while (i < m) {
        if (pattern[i] === pattern[length]) {
            length++;
            lps[i] = length;
            i++;
        } else {
            if (length !== 0) {
                length = lps[length - 1];
            } else {
                lps[i] = 0;
                i++;
            }
        }
    }
    return lps;
}

function kmpSearch(text, pattern) {
    const n = text.length;
    const m = pattern.length;
    if (m === 0) return [];
    
    const lps = computeLPSArray(pattern);
    let i = 0; // index for text
    let j = 0; // index for pattern
    const results = [];

    while (i < n) {
        if (pattern[j] === text[i]) {
            i++;
            j++;
        }

        if (j === m) {
            results.push(i - j);
            j = lps[j - 1];
        } else if (i < n && pattern[j] !== text[i]) {
            if (j !== 0) {
                j = lps[j - 1];
            } else {
                i++;
            }
        }
    }
    return results;
}

// const text = "ABABDABACDABABCABAB";
// const pattern = "ABABCABAB";
// console.log(kmpSearch(text, pattern)); // [10]
```

### Typescript

```typescript
function computeLPSArrayTS(pattern: string): number[] {
    const m = pattern.length;
    const lps: number[] = new Array(m).fill(0);
    let length = 0;
    let i = 1;

    while (i < m) {
        if (pattern[i] === pattern[length]) {
            length++;
            lps[i] = length;
            i++;
        } else {
            if (length !== 0) {
                length = lps[length - 1];
            } else {
                lps[i] = 0;
                i++;
            }
        }
    }
    return lps;
}

function kmpSearchTS(text: string, pattern: string): number[] {
    const n = text.length;
    const m = pattern.length;
    if (m === 0) return [];
    
    const lps = computeLPSArrayTS(pattern);
    let i = 0; // index for text
    let j = 0; // index for pattern
    const results: number[] = [];

    while (i < n) {
        if (pattern[j] === text[i]) {
            i++;
            j++;
        }

        if (j === m) {
            results.push(i - j);
            j = lps[j - 1];
        } else if (i < n && pattern[j] !== text[i]) {
            if (j !== 0) {
                j = lps[j - 1];
            } else {
                i++;
            }
        }
    }
    return results;
}

// const textTS = "ABABDABACDABABCABAB";
// const patternTS = "ABABCABAB";
// console.log(kmpSearchTS(textTS, patternTS)); // [10]
```

### Cpp

```cpp
#include <vector>
#include <string>
#include <iostream>

std::vector<int> computeLPSArray(const std::string& pattern) {
    int m = pattern.length();
    std::vector<int> lps(m, 0);
    int length = 0;
    int i = 1;

    while (i < m) {
        if (pattern[i] == pattern[length]) {
            length++;
            lps[i] = length;
            i++;
        } else {
            if (length != 0) {
                length = lps[length - 1];
            } else {
                lps[i] = 0;
                i++;
            }
        }
    }
    return lps;
}

std::vector<int> kmpSearch(const std::string& text, const std::string& pattern) {
    int n = text.length();
    int m = pattern.length();
    if (m == 0) return {};
    
    std::vector<int> lps = computeLPSArray(pattern);
    int i = 0; // index for text
    int j = 0; // index for pattern
    std::vector<int> results;

    while (i < n) {
        if (pattern[j] == text[i]) {
            i++;
            j++;
        }

        if (j == m) {
            results.push_back(i - j);
            j = lps[j - 1];
        } else if (i < n && pattern[j] != text[i]) {
            if (j != 0) {
                j = lps[j - 1];
            } else {
                i++;
            }
        }
    }
    return results;
}

// int main() {
//     std::string text = "ABABDABACDABABCABAB";
//     std::string pattern = "ABABCABAB";
//     std::vector<int> result = kmpSearch(text, pattern);
//     for(int pos : result) {
//         std::cout << "Pattern found at index " << pos << std::endl; // 10
//     }
// }
```

### Go

```go
package main

import "fmt"

func computeLPSArray(pattern string) []int {
    m := len(pattern)
    lps := make([]int, m)
    length := 0
    i := 1

    for i < m {
        if pattern[i] == pattern[length] {
            length++
            lps[i] = length
            i++
        } else {
            if length != 0 {
                length = lps[length-1]
            } else {
                lps[i] = 0
                i++
            }
        }
    }
    return lps
}

func kmpSearch(text, pattern string) []int {
    n := len(text)
    m := len(pattern)
    if m == 0 {
        return nil
    }

    lps := computeLPSArray(pattern)
    i := 0 // index for text
    j := 0 // index for pattern
    results := []int{}

    for i < n {
        if pattern[j] == text[i] {
            i++
            j++
        }

        if j == m {
            results = append(results, i-j)
            j = lps[j-1]
        } else if i < n && pattern[j] != text[i] {
            if j != 0 {
                j = lps[j-1]
            } else {
                i++
            }
        }
    }
    return results
}

// func main() {
//     text := "ABABDABACDABABCABAB"
//     pattern := "ABABCABAB"
//     fmt.Println(kmpSearch(text, pattern)) // [10]
// }
```

### D

```d
import std.stdio;
import std.array;

int[] computeLPSArray(string pattern) {
    auto m = pattern.length;
    auto lps = new int[m];
    int length = 0;
    int i = 1;

    while (i < m) {
        if (pattern[i] == pattern[length]) {
            length++;
            lps[i] = length;
            i++;
        } else {
            if (length != 0) {
                length = lps[length - 1];
            } else {
                lps[i] = 0;
                i++;
            }
        }
    }
    return lps;
}

int[] kmpSearch(string text, string pattern) {
    auto n = text.length;
    auto m = pattern.length;
    if (m == 0) return [];

    auto lps = computeLPSArray(pattern);
    int i = 0; // index for text
    int j = 0; // index for pattern
    int[] results;

    while (i < n) {
        if (pattern[j] == text[i]) {
            i++;
            j++;
        }

        if (j == m) {
            results ~= (i - j);
            j = lps[j - 1];
        } else if (i < n && pattern[j] != text[i]) {
            if (j != 0) {
                j = lps[j - 1];
            } else {
                i++;
            }
        }
    }
    return results;
}

// void main() {
//     string text = "ABABDABACDABABCABAB";
//     string pattern = "ABABCABAB";
//     writeln(kmpSearch(text, pattern)); // [10]
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

The KMP algorithm is a two-stage process: preprocessing the pattern and then searching the text.

---

**`computeLPSArray(pattern)` Function:**
- Creates an `LPS` array, `lps`, filled with zeros.
- Uses two pointers: `length` (tracks the length of the current longest prefix-suffix) and `i` (iterates through the pattern).
- If `pattern[i]` and `pattern[length]` match, it means we've extended the current prefix-suffix. We increment `length`, store it in `lps[i]`, and move to the next character `i`.
- If they don't match:
- If `length` is not zero, we "fall back" by looking at the LPS value of the previous character (`length = lps[length - 1]`). This effectively tries a shorter prefix-suffix.
- If `length` is zero, it means there's no proper prefix-suffix to fall back on, so `lps[i]` is 0, and we move to the next character `i`.

    </li>

**`kmpSearch(text, pattern)` Function:**
- Uses two pointers: `i` for the `text` and `j` for the `pattern`.
- If `text[i]` and `pattern[j]` match, increment both pointers.
- If `j` reaches the end of the pattern (`j == m`), a full match is found. We record the starting index (`i - j`) and then update `j` using the `LPS` array (`j = lps[j-1]`) to continue searching for the next possible match.
- If there's a mismatch:
- If `j` is not at the start of the pattern, we consult `lps[j-1]` to find the length of the prefix we can skip. We update `j` to this value without incrementing `i`. This is the "magic shift" of KMP.
- If `j` is already at the start, we can't shift the pattern further, so we just move to the next character in the `text` by incrementing `i`.

    </li>

[Back to Implementation](#implementation)

## Applications

### Application

The KMP algorithm is a fundamental string-searching algorithm used in various applications where efficiency is critical.
- **Text Editors:** Used in "find and replace" functionality.
- **Bioinformatics:** Searching for specific gene sequences within a larger DNA strand.
- **Data Loss Prevention (DLP):** Scanning documents or network traffic for sensitive data patterns (like credit card numbers or social security numbers).
- **Intrusion Detection Systems (IDS):** Searching for known malicious patterns or signatures in network packets.
- **Plagiarism Detection:** Finding instances of a smaller document (the "pattern") within a larger corpus of documents (the "text").

