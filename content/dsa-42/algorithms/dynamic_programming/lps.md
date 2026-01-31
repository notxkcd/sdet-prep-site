---
title: "Longest Palindromic Subsequence"
---

The `Longest Palindromic Subsequence (LPS)` problem is a classic problem in `dynamic programming`. Given a string `S`, the goal is to find the longest `subsequence` of `S` that is also a `palindrome`. A `palindrome` is a sequence that reads the same forwards and backward (e.g., "racecar", "madam"). A `subsequence` is formed by deleting zero or more `elements` from a sequence without changing the order of the remaining `elements`.

For example, in the string `S = "BBABCBCAB"`, one `LPS` is `"BABCBAB"` with a length of 7.

## How it Works

### How it Works (Expanded)

The `LPS problem` can be efficiently solved using `dynamic programming`. We build a 2D table `dp` where `dp[i][j]` stores the length of the `Longest Palindromic Subsequence` of the substring `S[i...j]` (from `index i` to `index j`, inclusive).

---

Example: LPS of S = "BBABCBCAB"

Initialize a DP table (matrix) of size n x n.

dp[i][i] = 1 (single character is a palindrome of length 1)

For a substring S[i...j]:
- If S[i] == S[j]: dp[i][j] = 2 + dp[i+1][j-1]
  (If characters match, they extend the LPS of the inner substring)
- Else (S[i] != S[j]): dp[i][j] = max(dp[i][j-1], dp[i+1][j])
  (If characters don't match, take the max LPS from excluding S[i] or S[j])

The final dp[0][n-1] value will be the length of the LPS for the entire string.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
def longest_palindromic_subsequence(s):
    n = len(s)

    # dp[i][j] stores the length of LPS of substring s[i..j]
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # Base case: Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1

    # Fill dp table
    # L is length of substring (from 2 to n)
    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            if s[i] == s[j]:
                # Characters match, extend LPS from inner substring
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                # Characters don't match, take max from excluding s[i] or s[j]
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
    
    return dp[0][n - 1]

# Example
# s1 = "BBABCBCAB"
# print(longest_palindromic_subsequence(s1)) # Expected: 7 (BABCBAB)

# s2 = "GEEKSFORGEEKS"
# print(longest_palindromic_subsequence(s2)) # Expected: 5 (EEKEE)
```

### Javascript

```javascript
function longestPalindromicSubsequence(s) {
    const n = s.length;

    // dp[i][j] stores the length of LPS of substring s[i..j]
    const dp = Array(n).fill(0).map(() => Array(n).fill(0));

    // Base case: Every single character is a palindrome of length 1
    for (let i = 0; i < n; i++) {
        dp[i][i] = 1;
    }

    // Fill dp table
    // L is length of substring (from 2 to n)
    for (let L = 2; L <= n; L++) {
        for (let i = 0; i <= n - L; i++) {
            const j = i + L - 1;
            if (s[i] === s[j]) {
                // Characters match, extend LPS from inner substring
                dp[i][j] = 2 + (L === 2 ? 0 : dp[i + 1][j - 1]);
            } else {
                // Characters don't match, take max from excluding s[i] or s[j]
                dp[i][j] = Math.max(dp[i][j - 1], dp[i + 1][j]);
            }
        }
    }
    
    return dp[0][n - 1];
}

// const s1 = "BBABCBCAB";
// console.log(longestPalindromicSubsequence(s1)); // Expected: 7

// const s2 = "GEEKSFORGEEKS";
// console.log(longestPalindromicSubsequence(s2)); // Expected: 5
```

### Typescript

```typescript
function longestPalindromicSubsequenceTS(s: string): number {
    const n = s.length;

    // dp[i][j] stores the length of LPS of substring s[i..j]
    const dp: number[][] = Array(n).fill(0).map(() => Array(n).fill(0));

    // Base case: Every single character is a palindrome of length 1
    for (let i = 0; i < n; i++) {
        dp[i][i] = 1;
    }

    // Fill dp table
    // L is length of substring (from 2 to n)
    for (let L = 2; L <= n; L++) {
        for (let i = 0; i <= n - L; i++) {
            const j = i + L - 1;
            if (s[i] === s[j]) {
                // Characters match, extend LPS from inner substring
                dp[i][j] = 2 + (L === 2 ? 0 : dp[i + 1][j - 1]);
            } else {
                // Characters don't match, take max from excluding s[i] or s[j]
                dp[i][j] = Math.max(dp[i][j - 1], dp[i + 1][j]);
            }
        }
    }
    
    return dp[0][n - 1];
}

// const s1TS = "BBABCBCAB";
// console.log(longestPalindromicSubsequenceTS(s1TS)); // Expected: 7

// const s2TS = "GEEKSFORGEEKS";
// console.log(longestPalindromicSubsequenceTS(s2TS)); // Expected: 5
```

### Cpp

```cpp
#include <string>
#include <vector>
#include <iostream>
#include <algorithm> // For std::max

int longestPalindromicSubsequence(const std::string& s) {
    int n = s.length();

    // dp[i][j] stores the length of LPS of substring s[i..j]
    std::vector<std::vector<int>> dp(n, std::vector<int>(n, 0));

    // Base case: Every single character is a palindrome of length 1
    for (int i = 0; i < n; i++) {
        dp[i][i] = 1;
    }

    // Fill dp table
    // L is length of substring (from 2 to n)
    for (int L = 2; L <= n; L++) {
        for (int i = 0; i <= n - L; i++) {
            int j = i + L - 1;
            if (s[i] == s[j]) {
                // Characters match, extend LPS from inner substring
                // If L == 2, then dp[i+1][j-1] would be dp[i+1][i], which is 0 for length.
                // It should be 0 because an empty string between two matching characters forms a LPS of length 2.
                dp[i][j] = 2 + dp[i + 1][j - 1];
            } else {
                // Characters don't match, take max from excluding s[i] or s[j]
                dp[i][j] = std::max(dp[i][j - 1], dp[i + 1][j]);
            }
        }
    }
    
    return dp[0][n - 1];
}

// int main() {
//     std::string s1 = "BBABCBCAB";
//     std::cout << "LPS length for " << s1 << ": " << longestPalindromicSubsequence(s1) << std::endl; // 7

//     std::string s2 = "GEEKSFORGEEKS";
//     std::cout << "LPS length for " << s2 << ": " << longestPalindromicSubsequence(s2) << std::endl; // 5
//     return 0;
// }
```

### Go

```go
package main

import "fmt"

func longestPalindromicSubsequence(s string) int {
    n := len(s)

    // dp[i][j] stores the length of LPS of substring s[i..j]
    dp := make([][]int, n)
    for i := range dp {
        dp[i] = make([]int, n)
    }

    // Base case: Every single character is a palindrome of length 1
    for i := 0; i < n; i++ {
        dp[i][i] = 1
    }

    // Fill dp table
    // L is length of substring (from 2 to n)
    for L := 2; L <= n; L++ {
        for i := 0; i <= n - L; i++ {
            j := i + L - 1
            if s[i] == s[j] {
                // Characters match, extend LPS from inner substring
                // If L == 2, then dp[i+1][j-1] would be dp[i+1][i], which is 0 for length.
                // This correctly adds 2 for the two matching characters.
                dp[i][j] = 2 + dp[i+1][j-1]
            } else {
                // Characters don't match, take max from excluding s[i] or s[j]
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])
            }
        }
    }
    
    return dp[0][n-1]
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

// func main() {
//     s1 := "BBABCBCAB"
//     fmt.Printf("LPS length for %s: %d\n", s1, longestPalindromicSubsequence(s1)) // 7

//     s2 := "GEEKSFORGEEKS"
//     fmt.Printf("LPS length for %s: %d\n", s2, longestPalindromicSubsequence(s2)) // 5
// }
```

### D

```d
import std.stdio;
import std.array;
import std.algorithm; // For std.algorithm.max

int longestPalindromicSubsequence(string s) {
    auto n = s.length;

    // dp[i][j] stores the length of LPS of substring s[i..j]
    auto dp = new int[n][n];

    // Base case: Every single character is a palindrome of length 1
    foreach (i; 0 .. n) {
        dp[i][i] = 1;
    }

    // Fill dp table
    // L is length of substring (from 2 to n)
    foreach (L; 2 .. n + 1) {
        foreach (i; 0 .. n - L + 1) {
            auto j = i + L - 1;
            if (s[i] == s[j]) {
                // Characters match, extend LPS from inner substring
                // dp[i+1][j-1] will be 0 if L == 2 (i.e., i+1 > j-1), which is correct
                dp[i][j] = 2 + dp[i + 1][j - 1];
            } else {
                // Characters don't match, take max from excluding s[i] or s[j]
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j]);
            }
        }
    }
    
    return dp[0][n - 1];
}

// void main() {
//     string s1 = "BBABCBCAB";
//     writeln("LPS length for ", s1, ": ", longestPalindromicSubsequence(s1)); // 7

//     string s2 = "GEEKSFORGEEKS";
//     writeln("LPS length for ", s2, ": ", longestPalindromicSubsequence(s2)); // 5
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

The `Longest Palindromic Subsequence` problem is solved using `dynamic programming` to fill a 2D table where `dp[i][j]` represents the `LPS` length for the substring `s[i...j]`.

---

**Initialization:**
- `n`: The length of the input string `s`.
- A 2D `dp` table (`n x n`) is created and initialized with zeros. `dp[i][j]` will store the length of the `LPS` for the substring `s[i...j]`.
- **Base Case:** All `dp[i][i]` (single-character substrings) are initialized to 1, as a single character is a palindrome of length 1.

**Filling the DP Table:**
- The table is filled iteratively by considering substrings of increasing `length` (`L`). `L` goes from 2 to `n`.
- For each `length L`, `i` (the starting `index`) iterates from 0 to `n - L`.
- `j` (the ending `index`) is calculated as `i + L - 1`.
- For each substring `s[i...j]`:
- **Case 1: `s[i] == s[j]`**
- If the characters at the ends of the substring match, they can be part of the `LPS`. The length of the `LPS` for `s[i...j]` is 2 (for `s[i]` and `s[j]`) plus the `LPS` length of the inner substring `s[i+1...j-1]` (`dp[i+1][j-1]`).
- If `L` is 2 (e.g., "aa"), `dp[i+1][j-1]` refers to `dp[i+1][i]`, which is 0 for an empty inner substring, correctly resulting in `2 + 0 = 2`.

            </li>
- **Case 2: `s[i] != s[j]`**
- If the characters at the ends do not match, we cannot include both `s[i]` and `s[j]` in the `LPS`.
- We must choose the maximum `LPS` length from two options:
- Excluding `s[i]`: `dp[i][j-1]` (LPS of `s[i...j-1]`).
- Excluding `s[j]`: `dp[i+1][j]` (LPS of `s[i+1...j]`).

                    </li>

            </li>

    </li>

**Result:**
- The final answer, the length of the `Longest Palindromic Subsequence` for the entire string, is stored in `dp[0][n-1]`.

[Back to Implementation](#implementation)

## Applications

### Application

The `Longest Palindromic Subsequence (LPS)` problem has several applications in various fields:
- **Bioinformatics:** Analyzing DNA and protein sequences, where palindromic structures can indicate functional significance. Finding `LPS` can help identify regions with high symmetry.
- **Text Compression:** In some compression algorithms, identifying palindromic subsequences can help in representing data more compactly.
- **Speech Recognition:** Detecting palindromic patterns in speech signals.
- **Pattern Recognition:** Useful in generalized pattern matching tasks where identifying symmetric patterns in data is important.
- **String Similarity:** While not a direct measure of `edit distance`, the length of the `LPS` can provide insights into the structural similarity of a string to its reverse, or be a component in more complex string comparison metrics.

