---
title: "Longest Common Substring"
---

The `Longest Common Substring (LCSUB)` problem is another classic problem in `dynamic programming`, closely related to the `Longest Common Subsequence (LCS)` problem. Given two strings, `string1` and `string2`, the goal is to find the longest string that is a `substring` of both. A `substring`, unlike a `subsequence`, requires consecutive characters.

For example, given `string1 = "ABABC"` and `string2 = "BABCA"`, the `Longest Common Substring`s are `"BABC"` (length 4) and `"ABA"` (length 3). The longest is `"BABC"`. It is important to distinguish this from the `LCS` problem, where "ABC" would be a common subsequence, but not a common substring, as its characters are not consecutive in `string2`.

## How it Works

### How it Works (Expanded)

The `LCSUB problem` can be solved using `dynamic programming` by building a 2D table (matrix) `dp` where `dp[i][j]` stores the length of the `longest common suffix` of `string1[0...i-1]` and `string2[0...j-1]`. The maximum value in the entire `dp` table will be the length of the `Longest Common Substring`.

---

Example: LCSUB of string1 = "ABABC" and string2 = "BABCA"

Initialize a DP table (matrix) of size (m+1) x (n+1) with zeros.

For dp[i][j]:
- If string1[i-1] == string2[j-1]: dp[i][j] = 1 + dp[i-1][j-1]
  (Characters match, extend the common suffix)
- Else: dp[i][j] = 0
  (Characters don't match, common suffix breaks, reset to 0)

The maximum value in the entire DP table is the length of LCSUB.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)

    # dp[i][j] stores the length of the longest common suffix of
    # str1[0..i-1] and str2[0..j-1]
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    max_length = 0      # Stores the length of the longest common substring
    end_index = 0       # Stores the ending index of the LCSUB in str1

    # Fill dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i - 1 # or j - 1, since it's a common substring
            else:
                dp[i][j] = 0 # Mismatch, common suffix breaks
    
    # Reconstruct the LCSUB
    if max_length == 0:
        return ""
    
    return str1[end_index - max_length + 1 : end_index + 1]

# Example
# str1 = "ABABC"
# str2 = "BABCA"
# print(longest_common_substring(str1, str2)) # BABC
```

### Javascript

```javascript
function longestCommonSubstring(str1, str2) {
    const m = str1.length;
    const n = str2.length;

    // dp[i][j] stores the length of the longest common suffix of
    // str1[0..i-1] and str2[0..j-1]
    const dp = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));

    let maxLength = 0;      // Stores the length of the longest common substring
    let endIndex = 0;       // Stores the ending index of the LCSUB in str1

    // Fill dp table
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (str1[i - 1] === str2[j - 1]) {
                dp[i][j] = 1 + dp[i - 1][j - 1];
                if (dp[i][j] > maxLength) {
                    maxLength = dp[i][j];
                    endIndex = i - 1; // or j - 1
                }
            } else {
                dp[i][j] = 0; // Mismatch, common suffix breaks
            }
        }
    }
    
    // Reconstruct the LCSUB
    if (maxLength === 0) {
        return "";
    }
    
    return str1.substring(endIndex - maxLength + 1, endIndex + 1);
}

// const str1 = "ABABC";
// const str2 = "BABCA";
// console.log(longestCommonSubstring(str1, str2)); // BABC
```

### Typescript

```typescript
function longestCommonSubstringTS(str1: string, str2: string): string {
    const m = str1.length;
    const n = str2.length;

    // dp[i][j] stores the length of the longest common suffix of
    // str1[0..i-1] and str2[0..j-1]
    const dp: number[][] = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));

    let maxLength = 0;      // Stores the length of the longest common substring
    let endIndex = 0;       // Stores the ending index of the LCSUB in str1

    // Fill dp table
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (str1[i - 1] === str2[j - 1]) {
                dp[i][j] = 1 + dp[i - 1][j - 1];
                if (dp[i][j] > maxLength) {
                    maxLength = dp[i][j];
                    endIndex = i - 1; // or j - 1
                }
            } else {
                dp[i][j] = 0; // Mismatch, common suffix breaks
            }
        }
    }
    
    // Reconstruct the LCSUB
    if (maxLength === 0) {
        return "";
    }
    
    return str1.substring(endIndex - maxLength + 1, endIndex + 1);
}

// const str1TS = "ABABC";
// const str2TS = "BABCA";
// console.log(longestCommonSubstringTS(str1TS, str2TS)); // BABC
```

### Cpp

```cpp
#include <string>
#include <vector>
#include <iostream>
#include <algorithm> // For std::max

std::string longestCommonSubstring(const std::string& str1, const std::string& str2) {
    int m = str1.length();
    int n = str2.length();

    // dp[i][j] stores the length of the longest common suffix of
    // str1[0..i-1] and str2[0..j-1]
    std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1, 0));

    int max_length = 0;      // Stores the length of the longest common substring
    int end_index = 0;       // Stores the ending index of the LCSUB in str1

    // Fill dp table
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (str1[i - 1] == str2[j - 1]) {
                dp[i][j] = 1 + dp[i - 1][j - 1];
                if (dp[i][j] > max_length) {
                    max_length = dp[i][j];
                    end_index = i - 1; // or j - 1
                }
            } else {
                dp[i][j] = 0; // Mismatch, common suffix breaks
            }
        }
    }
    
    // Reconstruct the LCSUB
    if (max_length == 0) {
        return "";
    }
    
    return str1.substr(end_index - max_length + 1, max_length);
}

// int main() {
//     std::string str1 = "ABABC";
//     std::string str2 = "BABCA";
//     std::cout << "Longest Common Substring: " << longestCommonSubstring(str1, str2) << std::endl; // BABC
//     return 0;
// }
```

### Go

```go
package main

import "fmt"

func longestCommonSubstring(str1, str2 string) string {
    m := len(str1)
    n := len(str2)

    // dp[i][j] stores the length of the longest common suffix of
    // str1[0..i-1] and str2[0..j-1]
    dp := make([][]int, m+1)
    for i := range dp {
        dp[i] = make([]int, n+1)
    }

    maxLength := 0      // Stores the length of the longest common substring
    endIndex := 0       // Stores the ending index of the LCSUB in str1

    // Fill dp table
    for i := 1; i <= m; i++ {
        for j := 1; j <= n; j++ {
            if str1[i-1] == str2[j-1] {
                dp[i][j] = 1 + dp[i-1][j-1]
                if dp[i][j] > maxLength {
                    maxLength = dp[i][j]
                    endIndex = i - 1 // or j - 1
                }
            } else {
                dp[i][j] = 0 // Mismatch, common suffix breaks
            }
        }
    }
    
    // Reconstruct the LCSUB
    if maxLength == 0 {
        return ""
    }
    
    return str1[endIndex-maxLength+1 : endIndex+1]
}

// func main() {
//     str1 := "ABABC"
//     str2 := "BABCA"
//     fmt.Println("Longest Common Substring:", longestCommonSubstring(str1, str2)) // BABC
// }
```

### D

```d
import std.stdio;
import std.array;
import std.algorithm; // For std.algorithm.max

string longestCommonSubstring(string str1, string str2) {
    auto m = str1.length;
    auto n = str2.length;

    // dp[i][j] stores the length of the longest common suffix of
    // str1[0..i-1] and str2[0..j-1]
    auto dp = new int[m + 1][n + 1];

    int maxLength = 0;      // Stores the length of the longest common substring
    int endIndex = 0;       // Stores the ending index of the LCSUB in str1

    // Fill dp table
    foreach (i; 1 .. m + 1) {
        foreach (j; 1 .. n + 1) {
            if (str1[i - 1] == str2[j - 1]) {
                dp[i][j] = 1 + dp[i - 1][j - 1];
                if (dp[i][j] > maxLength) {
                    maxLength = dp[i][j];
                    endIndex = i - 1; // or j - 1
                }
            } else {
                dp[i][j] = 0; // Mismatch, common suffix breaks
            }
        }
    }
    
    // Reconstruct the LCSUB
    if (maxLength == 0) {
        return "";
    }
    
    return str1[endIndex - maxLength + 1 .. endIndex + 1];
}

// void main() {
//     string str1 = "ABABC";
//     string str2 = "BABCA";
//     writeln("Longest Common Substring: ", longestCommonSubstring(str1, str2)); // BABC
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

The `Longest Common Substring (LCSUB)` problem is solved using `dynamic programming` with a 2D table that tracks the length of common suffixes.

---

**Initialization:**
- `m`, `n`: Lengths of `str1` and `str2`.
- A 2D `dp` table (`m+1` rows, `n+1` columns) is created and initialized with zeros. `dp[i][j]` will store the length of the `longest common suffix` of `str1[0...i-1]` and `str2[0...j-1]`.
- `maxLength`: Tracks the maximum length found in the `dp` table, which will be the length of the `LCSUB`.
- `endIndex`: Tracks the ending `index` of the `LCSUB` in `str1` (or `str2`).

**Filling the DP Table:**
- The `dp` table is filled iteratively for `i` from 1 to `m` and `j` from 1 to `n`.
- For each cell `dp[i][j]`:
- If `str1[i-1]` (the `i`-th character of `str1`) matches `str2[j-1]` (the `j`-th character of `str2`):
- The `longest common suffix` is extended by 1. So, `dp[i][j] = 1 + dp[i-1][j-1]`.
- If this `new length` `dp[i][j]` is greater than `maxLength`, update `maxLength` and `endIndex`.

            </li>
- If the characters do not match:
- The common suffix is broken. So, `dp[i][j]` is reset to 0.

            </li>

    </li>

**Result:**
- After filling the entire `dp` table, `maxLength` will hold the length of the `Longest Common Substring`.
- The `LCSUB` can be extracted from `str1` (or `str2`) using `endIndex` and `maxLength`. For example, `str1[endIndex - maxLength + 1 : endIndex + 1]`.

[Back to Implementation](#implementation)

## Applications

### Application

The `Longest Common Substring` problem has several practical applications, particularly in areas involving sequence comparison and pattern recognition:
- **Plagiarism Detection:** Identifying verbatim copied segments of text between documents.
- **Bioinformatics:** Finding conserved regions or similar segments in DNA, RNA, or protein sequences.
- **File Comparison Utilities (`diff` tools):** While `diff` tools often use `LCS` (subsequence), `LCSUB` can be useful for finding contiguous blocks of identical text.
- **Version Control Systems:** Identifying common code blocks between different versions of a file.
- **Text Analysis:** Extracting repeated phrases or patterns in natural language texts.
- **Image Processing:** Pattern matching in images where contiguous blocks of pixels need to be similar.

