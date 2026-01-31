---
title: "Edit Distance (Levenshtein Distance)"
---

The `Edit Distance`, often known as `Levenshtein Distance`, is a metric for measuring the difference between two sequences (typically strings). It quantifies how dissimilar two strings are by counting the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one word into the other.

This problem is a classic application of `dynamic programming`, where the solution builds upon the optimal solutions of smaller subproblems. It's widely used in spell checkers, DNA sequence analysis, and natural language processing.

## How it Works

### How it Works (Expanded)

The `Edit Distance` algorithm uses a 2D `DP table` (matrix) to store the minimum `edit distance` between all possible prefixes of the two input strings. `dp[i][j]` represents the `Levenshtein distance` between `string1[0...i-1]` and `string2[0...j-1]`.

---

Example: Edit Distance between "kitten" and "sitting"

Initialize a DP table (matrix) of size (m+1) x (n+1)
- dp[i][0] = i (cost of deleting all chars from string1)
- dp[0][j] = j (cost of inserting all chars from string2)

For dp[i][j]:
- If string1[i-1] == string2[j-1]: dp[i][j] = dp[i-1][j-1] (no cost if characters match)
- Else: dp[i][j] = 1 + min(dp[i-1][j],   // Deletion
                          dp[i][j-1],   // Insertion
                          dp[i-1][j-1]) // Substitution

The final dp[m][n] value is the edit distance.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
def edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)

    # dp[i][j] stores the edit distance between str1[0..i-1] and str2[0..j-1]
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Initialize base cases
    # If str1 is empty, distance is number of insertions to get str2
    for i in range(m + 1):
        dp[i][0] = i
    # If str2 is empty, distance is number of deletions to get str1
    for j in range(n + 1):
        dp[0][j] = j

    # Fill dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] # Characters match, no cost
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],      # Deletion
                                   dp[i][j - 1],      # Insertion
                                   dp[i - 1][j - 1])  # Substitution
    
    return dp[m][n]

# Example
# str1 = "kitten"
# str2 = "sitting"
# print(edit_distance(str1, str2)) # 3 (k -> s, e -> i, _ -> g)
```

### Javascript

```javascript
function editDistance(str1, str2) {
    const m = str1.length;
    const n = str2.length;

    // dp[i][j] stores the edit distance between str1[0..i-1] and str2[0..j-1]
    const dp = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));

    // Initialize base cases
    // If str1 is empty, distance is number of insertions to get str2
    for (let i = 0; i <= m; i++) {
        dp[i][0] = i;
    }
    // If str2 is empty, distance is number of deletions to get str1
    for (let j = 0; j <= n; j++) {
        dp[0][j] = j;
    }

    // Fill dp table
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (str1[i - 1] === str2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1]; // Characters match, no cost
            } else {
                dp[i][j] = 1 + Math.min(dp[i - 1][j],      // Deletion
                                        dp[i][j - 1],      // Insertion
                                        dp[i - 1][j - 1]);  // Substitution
            }
        }
    }
    
    return dp[m][n];
}

// const str1 = "kitten";
// const str2 = "sitting";
// console.log(editDistance(str1, str2)); // 3
```

### Typescript

```typescript
function editDistanceTS(str1: string, str2: string): number {
    const m = str1.length;
    const n = str2.length;

    // dp[i][j] stores the edit distance between str1[0..i-1] and str2[0..j-1]
    const dp: number[][] = Array(m + 1).fill(0).map(() => Array(n + 1).fill(0));

    // Initialize base cases
    // If str1 is empty, distance is number of insertions to get str2
    for (let i = 0; i <= m; i++) {
        dp[i][0] = i;
    }
    // If str2 is empty, distance is number of deletions to get str1
    for (let j = 0; j <= n; j++) {
        dp[0][j] = j;
    }

    // Fill dp table
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (str1[i - 1] === str2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1]; // Characters match, no cost
            } else {
                dp[i][j] = 1 + Math.min(dp[i - 1][j],      // Deletion
                                        dp[i][j - 1],      // Insertion
                                        dp[i - 1][j - 1]);  // Substitution
            }
        }
    }
    
    return dp[m][n];
}

// const str1TS = "kitten";
// const str2TS = "sitting";
// console.log(editDistanceTS(str1TS, str2TS)); // 3
```

### Cpp

```cpp
#include <string>
#include <vector>
#include <iostream>
#include <algorithm> // For std::min

int editDistance(const std::string& str1, const std::string& str2) {
    int m = str1.length();
    int n = str2.length();

    // dp[i][j] stores the edit distance between str1[0..i-1] and str2[0..j-1]
    std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1));

    // Initialize base cases
    // If str1 is empty, distance is number of insertions to get str2
    for (int i = 0; i <= m; i++) {
        dp[i][0] = i;
    }
    // If str2 is empty, distance is number of deletions to get str1
    for (int j = 0; j <= n; j++) {
        dp[0][j] = j;
    }

    // Fill dp table
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (str1[i - 1] == str2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1]; // Characters match, no cost
            } else {
                dp[i][j] = 1 + std::min({dp[i - 1][j],      // Deletion
                                        dp[i][j - 1],      // Insertion
                                        dp[i - 1][j - 1]});  // Substitution
            }
        }
    }
    
    return dp[m][n];
}

// int main() {
//     std::string str1 = "kitten";
//     std::string str2 = "sitting";
//     std::cout << "Edit Distance: " << editDistance(str1, str2) << std::endl; // 3
//     return 0;
// }
```

### Go

```go
package main

import "fmt"

func editDistance(str1, str2 string) int {
    m := len(str1)
    n := len(str2)

    // dp[i][j] stores the edit distance between str1[0..i-1] and str2[0..j-1]
    dp := make([][]int, m+1)
    for i := range dp {
        dp[i] = make([]int, n+1)
    }

    // Initialize base cases
    // If str1 is empty, distance is number of insertions to get str2
    for i := 0; i <= m; i++ {
        dp[i][0] = i
    }
    // If str2 is empty, distance is number of deletions to get str1
    for j := 0; j <= n; j++ {
        dp[0][j] = j
    }

    // Fill dp table
    for i := 1; i <= m; i++ {
        for j := 1; j <= n; j++ {
            if str1[i-1] == str2[j-1] {
                dp[i][j] = dp[i-1][j-1] // Characters match, no cost
            } else {
                dp[i][j] = 1 + min(dp[i-1][j],      // Deletion
                                   dp[i][j-1],      // Insertion
                                   dp[i-1][j-1])  // Substitution
            }
        }
    }
    
    return dp[m][n]
}

func min(a, b, c int) int {
    if a < b {
        if a < c {
            return a
        }
        return c
    } else {
        if b < c {
            return b
        }
        return c
    }
}

// func main() {
//     str1 := "kitten"
//     str2 := "sitting"
//     fmt.Println("Edit Distance:", editDistance(str1, str2)) // 3
// }
```

### D

```d
import std.stdio;
import std.array;
import std.algorithm; // For std.algorithm.min

int editDistance(string str1, string str2) {
    auto m = str1.length;
    auto n = str2.length;

    // dp[i][j] stores the edit distance between str1[0..i-1] and str2[0..j-1]
    auto dp = new int[m + 1][n + 1];

    // Initialize base cases
    // If str1 is empty, distance is number of insertions to get str2
    foreach (i; 0 .. m + 1) {
        dp[i][0] = i;
    }
    // If str2 is empty, distance is number of deletions to get str1
    foreach (j; 0 .. n + 1) {
        dp[0][j] = j;
    }

    // Fill dp table
    foreach (i; 1 .. m + 1) {
        foreach (j; 1 .. n + 1) {
            if (str1[i - 1] == str2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1]; // Characters match, no cost
            } else {
                dp[i][j] = 1 + min(dp[i - 1][j],      // Deletion
                                   dp[i][j - 1],      // Insertion
                                   dp[i - 1][j - 1]);  // Substitution
            }
        }
    }
    
    return dp[m][n];
}

// void main() {
//     string str1 = "kitten";
//     string str2 = "sitting";
//     writeln("Edit Distance: ", editDistance(str1, str2)); // 3
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

The `Edit Distance` algorithm uses `dynamic programming` to fill a 2D table representing the `edit distance` between all prefixes of the two input strings.

---

**Initialization:**
- A 2D `dp` table (`m+1` rows, `n+1` columns) is created.
- The first row `dp[i][0]` is initialized from 0 to `m`, representing the cost of deleting `i` characters from `str1` to make it empty.
- The first column `dp[0][j]` is initialized from 0 to `n`, representing the cost of inserting `j` characters to make an empty string `str2`.

**Filling the DP Table:**
- The `dp` table is filled iteratively for `i` from 1 to `m` and `j` from 1 to `n`.
- For each cell `dp[i][j]`:
- If `str1[i-1]` (the `i`-th character of `str1`) matches `str2[j-1]` (the `j`-th character of `str2`), then no `edit` operation is needed for these characters. The `edit distance` is simply inherited from the previous diagonal cell: `dp[i-1][j-1]`.
- If the characters do not match, an `edit` operation (deletion, insertion, or substitution) is required. The cost of this operation is `1` plus the minimum `edit distance` from three possibilities:
- `dp[i-1][j]`: Cost of deleting `str1[i-1]`.
- `dp[i][j-1]`: Cost of inserting `str2[j-1]`.
- `dp[i-1][j-1]`: Cost of substituting `str1[i-1]` with `str2[j-1]`.

            </li>

    </li>

**Result:**
- The final `edit distance` between `str1` and `str2` is stored in `dp[m][n]`.

[Back to Implementation](#implementation)

## Applications

### Application

The `Edit Distance (Levenshtein Distance)` algorithm has a wide array of practical applications:
- **Spell Checkers and Autocorrection:** Suggesting corrections for misspelled words by finding dictionary words with the minimum `edit distance`.
- **DNA Sequence Alignment:** Measuring the similarity between biological sequences to understand evolutionary relationships or identify functional similarities.
- **Plagiarism Detection:** Quantifying the textual similarity between documents.
- **Optical Character Recognition (OCR) Error Correction:** Correcting errors introduced during the scanning of text.
- **Natural Language Processing (NLP):** Used in tasks like machine translation evaluation, fuzzy string matching, and text comparison.

