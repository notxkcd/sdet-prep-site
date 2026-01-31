---
title: "Longest Common Subsequence (LCS)"
---

The `Longest Common Subsequence (LCS)` problem is a classic problem in `computer science` and `dynamic programming`. Given two sequences (e.g., strings or arrays), the goal is to find the longest sequence that is a `subsequence` of both. A `subsequence` is formed by deleting zero or more `elements` from a sequence without changing the order of the remaining `elements`.

Unlike the `longest common substring` problem (where characters must be consecutive), `LCS` does not require consecutive characters. It has numerous applications in bioinformatics (e.g., comparing DNA sequences) and text analysis (e.g., diff utilities).

## How it Works

### How it Works (Expanded)

The `LCS problem` can be efficiently solved using `dynamic programming`. We build a 2D table (or matrix) where `dp[i][j]` stores the length of the `LCS` of the prefixes `X[0...i-1]` and `Y[0...j-1]` of the two input sequences `X` and `Y`.

---

Example: LCS of X = "AGGTAB" and Y = "GXTXAYB"

Initialize a DP table (matrix) of size (m+1) x (n+1) with zeros.

Table Cells:
- If X[i-1] == Y[j-1]: dp[i][j] = 1 + dp[i-1][j-1]
  (Characters match, so extend the LCS from diagonal)
- Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
  (Characters don't match, take max LCS from previous row/column)

The final dp[m][n] value will be the length of the LCS.
To reconstruct the LCS itself, backtrack from dp[m][n] using the rules.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)

    # dp[i][j] stores the length of LCS of X[0..i-1] and Y[0..j-1]
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Fill dp table in bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # dp[m][n] contains the length of LCS
    length_lcs = dp[m][n]

    # Reconstruct the LCS string
    lcs_string = [""] * length_lcs
    i, j = m, n
    k = length_lcs - 1

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_string[k] = X[i - 1]
            i -= 1
            j -= 1
            k -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
            
    return "".join(lcs_string)

# Example
# X = "AGGTAB"
# Y = "GXTXAYB"
# print(longest_common_subsequence(X, Y)) # GTAB
```

### Javascript

```javascript
function longestCommonSubsequence(X, Y) {
    const m = X.length;
    const n = Y.length;

    // dp[i][j] stores the length of LCS of X[0..i-1] and Y[0..j-1]
    const dp = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));

    // Fill dp table in bottom-up manner
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (X[i - 1] === Y[j - 1]) {
                dp[i][j] = 1 + dp[i - 1][j - 1];
            } else {
                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    
    // dp[m][n] contains the length of LCS
    const lengthLCS = dp[m][n];

    // Reconstruct the LCS string
    let lcsString = Array(lengthLCS);
    let i = m, j = n;
    let k = lengthLCS - 1;

    while (i > 0 && j > 0) {
        if (X[i - 1] === Y[j - 1]) {
            lcsString[k] = X[i - 1];
            i--;
            j--;
            k--;
        } else if (dp[i - 1][j] > dp[i][j - 1]) {
            i--;
        } else {
            j--;
        }
    }
            
    return lcsString.join("");
}

// const X = "AGGTAB";
// const Y = "GXTXAYB";
// console.log(longestCommonSubsequence(X, Y)); // GTAB
```

### Typescript

```typescript
function longestCommonSubsequenceTS(X: string, Y: string): string {
    const m = X.length;
    const n = Y.length;

    // dp[i][j] stores the length of LCS of X[0..i-1] and Y[0..j-1]
    const dp: number[][] = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));

    // Fill dp table in bottom-up manner
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (X[i - 1] === Y[j - 1]) {
                dp[i][j] = 1 + dp[i - 1][j - 1];
            } else {
                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    
    // dp[m][n] contains the length of LCS
    const lengthLCS = dp[m][n];

    // Reconstruct the LCS string
    const lcsString: string[] = Array(lengthLCS);
    let i = m, j = n;
    let k = lengthLCS - 1;

    while (i > 0 && j > 0) {
        if (X[i - 1] === Y[j - 1]) {
            lcsString[k] = X[i - 1];
            i--;
            j--;
            k--;
        } else if (dp[i - 1][j] > dp[i][j - 1]) {
            i--;
        } else {
            j--;
        }
    }
            
    return lcsString.join("");
}

// const XTS = "AGGTAB";
// const YTS = "GXTXAYB";
// console.log(longestCommonSubsequenceTS(XTS, YTS)); // GTAB
```

### Cpp

```cpp
#include <string>
#include <vector>
#include <iostream>
#include <algorithm> // For std::max

std::string longestCommonSubsequence(const std::string& X, const std::string& Y) {
    int m = X.length();
    int n = Y.length();

    // dp[i][j] stores the length of LCS of X[0..i-1] and Y[0..j-1]
    std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1, 0));

    // Fill dp table in bottom-up manner
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (X[i - 1] == Y[j - 1]) {
                dp[i][j] = 1 + dp[i - 1][j - 1];
            } else {
                dp[i][j] = std::max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    
    // dp[m][n] contains the length of LCS
    int length_lcs = dp[m][n];

    // Reconstruct the LCS string
    std::string lcs_string(length_lcs, ' '); // Initialize with spaces
    int i = m, j = n;
    int k = length_lcs - 1;

    while (i > 0 && j > 0) {
        if (X[i - 1] == Y[j - 1]) {
            lcs_string[k] = X[i - 1];
            i--;
            j--;
            k--;
        } else if (dp[i - 1][j] > dp[i][j - 1]) {
            i--;
        } else {
            j--;
        }
    }
            
    return lcs_string;
}

// int main() {
//     std::string X = "AGGTAB";
//     std::string Y = "GXTXAYB";
//     std::cout << "LCS: " << longestCommonSubsequence(X, Y) << std::endl; // GTAB
//     return 0;
// }
```

### Go

```go
package main

import "fmt"

func longestCommonSubsequence(X, Y string) string {
    m := len(X)
    n := len(Y)

    // dp[i][j] stores the length of LCS of X[0..i-1] and Y[0..j-1]
    dp := make([][]int, m+1)
    for i := range dp {
        dp[i] = make([]int, n+1)
    }

    // Fill dp table in bottom-up manner
    for i := 1; i <= m; i++ {
        for j := 1; j <= n; j++ {
            if X[i-1] == Y[j-1] {
                dp[i][j] = 1 + dp[i-1][j-1]
            } else {
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            }
        }
    }
    
    // dp[m][n] contains the length of LCS
    lengthLCS := dp[m][n]

    // Reconstruct the LCS string
    lcsString := make([]byte, lengthLCS)
    i, j := m, n
    k := lengthLCS - 1

    for i > 0 && j > 0 {
        if X[i-1] == Y[j-1] {
            lcsString[k] = X[i-1]
            i--
            j--
            k--
        } else if dp[i-1][j] > dp[i][j-1] {
            i--
        } else {
            j--
        }
    }
            
    return string(lcsString)
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

// func main() {
//     X := "AGGTAB"
//     Y := "GXTXAYB"
//     fmt.Println("LCS:", longestCommonSubsequence(X, Y)) // GTAB
// }
```

### D

```d
import std.stdio;
import std.array;
import std.algorithm; // For std.algorithm.max

string longestCommonSubsequence(string X, string Y) {
    auto m = X.length;
    auto n = Y.length;

    // dp[i][j] stores the length of LCS of X[0..i-1] and Y[0..j-1]
    auto dp = new int[m + 1][n + 1];

    // Fill dp table in bottom-up manner
    foreach (i; 1 .. m + 1) {
        foreach (j; 1 .. n + 1) {
            if (X[i - 1] == Y[j - 1]) {
                dp[i][j] = 1 + dp[i - 1][j - 1];
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    
    // dp[m][n] contains the length of LCS
    auto lengthLCS = dp[m][n];

    // Reconstruct the LCS string
    auto lcsString = new char[lengthLCS];
    int i = cast(int)m, j = cast(int)n;
    int k = cast(int)lengthLCS - 1;

    while (i > 0 && j > 0) {
        if (X[i - 1] == Y[j - 1]) {
            lcsString[k] = X[i - 1];
            i--;
            j--;
            k--;
        } else if (dp[i - 1][j] > dp[i][j - 1]) {
            i--;
        } else {
            j--;
        }
    }
            
    return cast(string)lcsString;
}

// void main() {
//     string X = "AGGTAB";
//     string Y = "GXTXAYB";
//     writeln("LCS: ", longestCommonSubsequence(X, Y)); // GTAB
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

The `Longest Common Subsequence` problem is a prime example of `dynamic programming`, building up a solution from smaller subproblems.

---

**Initialization:**
- A 2D `dp` table (`m+1` rows, `n+1` columns) is created and initialized with zeros. `dp[i][j]` will store the length of the `LCS` for prefixes of length `i` from `X` and `j` from `Y`.

**Filling the DP Table (Calculating LCS Length):**
- The `dp` table is filled iteratively, typically from `dp[1][1]` up to `dp[m][n]`.
- For each cell `dp[i][j]`:
- If `X[i-1]` (the `i`-th character of `X`) matches `Y[j-1]` (the `j`-th character of `Y`), then the `LCS` length is `1` plus the `LCS` length of the previous prefixes (`dp[i-1][j-1]`). This means we've found one more matching character.
- If they don't match, the `LCS` length for `dp[i][j]` is the maximum of:
- `dp[i-1][j]` (LCS of `X[0...i-2]` and `Y[0...j-1]`, effectively skipping `X[i-1]`).
- `dp[i][j-1]` (LCS of `X[0...i-1]` and `Y[0...j-2]`, effectively skipping `Y[j-1]`).

            </li>

    </li>

**Reconstructing the LCS String:**
- After the `dp` table is filled, `dp[m][n]` holds the length of the `LCS`.
- To reconstruct the string, we start from `dp[m][n]` and backtrack to `dp[0][0]`.
- If `X[i-1] == Y[j-1]`, it means these characters contributed to the `LCS`. We add `X[i-1]` to our `LCS string` and move diagonally up-left (`i--`, `j--`).
- If `X[i-1] != Y[j-1]`, we move to the cell (either `dp[i-1][j]` or `dp[i][j-1]`) that has the larger `LCS` length, indicating which character was "skipped".
- The `LCS string` is built in reverse order, so it needs to be reversed or assembled by prepending characters.

[Back to Implementation](#implementation)

## Applications

### Application

The `Longest Common Subsequence (LCS)` problem and its solution using `dynamic programming` have widespread applications:
- **Bioinformatics:** Comparing DNA, RNA, or protein sequences to find similarities. The `LCS` provides a measure of how related two biological sequences are.
- **Diff Utilities:** The `diff` command (and similar version control tools like `Git`) use algorithms based on `LCS` to find the differences between two files. This helps in identifying minimal changes.
- **Plagiarism Detection:** Finding common subsequences between two documents can indicate potential plagiarism.
- **Text Editing and Spell Checkers:** Can be used to suggest corrections by finding the `LCS` between a misspelled word and dictionary words, or to determine edit distance.
- **Data Compression:** In some forms of data compression, finding recurring patterns (or subsequences) can be beneficial.

