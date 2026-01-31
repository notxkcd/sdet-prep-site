---
title: "Z-Algorithm"
---

The `Z-Algorithm` is a linear-time string searching algorithm that is often used as a preprocessing step for other string algorithms. For a given string `S`, it constructs a "`Z-array`" (also known as a "`Z-function`") where `Z[i]` is the length of the longest substring starting at `S[i]` that is also a prefix of `S`.

This array provides insights into the structure of the string `S` and can be used to efficiently find all occurrences of a `pattern P` within a `text T` in `O(N + M)` time, where `N` is the length of the text and `M` is the length of the pattern.

## How it Works

### How it Works (Expanded)

The core idea of the `Z-Algorithm` is to compute the `Z-array` efficiently. `Z[0]` is typically defined as `0` or `N` (the length of the string), as the entire string is a prefix of itself starting at `S[0]`.

---

Example: Z-array for string S = "abacaba"
- S[0] = "abacaba" (prefix "abacaba") -> Z[0] = 7 (or 0)
- S[1] = "bacaba"  (no prefix match) -> Z[1] = 0
- S[2] = "acaba"   (prefix "aba") -> Z[2] = 3
- S[3] = "caba"    (no prefix match) -> Z[3] = 0
- S[4] = "aba"     (prefix "aba") -> Z[4] = 3
- S[5] = "ba"      (no prefix match) -> Z[5] = 0
- S[6] = "a"       (prefix "a") -> Z[6] = 1

Z-array: [7, 0, 3, 0, 3, 0, 1]

How to find a pattern P in text T using Z-Algorithm:
1. Construct a new string S = P + "$" + T (where "$" is a unique delimiter not in P or T).
2. Compute the Z-array for S.
3. Any Z[i] that equals the length of P indicates an occurrence of P in T.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
def compute_z_array(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0

    # Z[0] can be n, or 0 depending on convention. Here we use 0, and handle later.
    # The actual algorithm usually means Z[i] is the length of the longest
    # substring starting at s[i] that is also a prefix of s.
    # z[0] is typically not part of this definition or is set to 0.

    for i in range(1, n):
        if i <= r:
            # i is inside the current Z-box [L, R]
            z[i] = min(r - i + 1, z[i - l])
        
        # Extend z[i] by brute force if necessary (or if i > R)
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        
        # If z[i] extends beyond R, update Z-box [L, R]
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    
    z[0] = n # Convention: Z[0] is the length of the string itself

    return z

def z_algorithm_search(text, pattern):
    """
    Finds all occurrences of pattern in text using the Z-Algorithm.
    """
    n = len(text)
    m = len(pattern)
    if m == 0: return []
    if n == 0: return []

    combined_string = pattern + "$" + text # "$" is a unique delimiter
    z_array = compute_z_array(combined_string)
    
    results = []
    # Any Z[i] that equals the length of P indicates an occurrence
    for i in range(m + 1, len(combined_string)): # Start search after pattern + delimiter
        if z_array[i] == m:
            results.append(i - (m + 1)) # Adjust index back to original text
            
    return results

# Example
# text = "abacaba"
# pattern = "aba"
# print(z_algorithm_search(text, pattern)) # [0, 4]
```

### Javascript

```javascript
function computeZArray(s) {
    const n = s.length;
    const z = new Array(n).fill(0);
    let l = 0, r = 0;

    // z[0] is typically not part of this definition or is set to 0.
    // We set it to n at the end for pattern searching convention.

    for (let i = 1; i < n; i++) {
        if (i <= r) {
            z[i] = Math.min(r - i + 1, z[i - l]);
        }
        
        while (i + z[i] < n && s[z[i]] === s[i + z[i]]) {
            z[i]++;
        }
        
        if (i + z[i] - 1 > r) {
            l = i;
            r = i + z[i] - 1;
        }
    }
    
    z[0] = n; // Convention for pattern searching

    return z;
}

function zAlgorithmSearch(text, pattern) {
    const n = text.length;
    const m = pattern.length;
    if (m === 0) return [];
    if (n === 0) return [];

    const combinedString = pattern + "$" + text;
    const zArray = computeZArray(combinedString);
    
    const results = [];
    for (let i = m + 1; i < combinedString.length; i++) {
        if (zArray[i] === m) {
            results.push(i - (m + 1));
        }
    }
    return results;
}

// const text = "abacaba";
// const pattern = "aba";
// console.log(zAlgorithmSearch(text, pattern)); // [0, 4]
```

### Typescript

```typescript
function computeZArrayTS(s: string): number[] {
    const n = s.length;
    const z: number[] = new Array(n).fill(0);
    let l = 0, r = 0;

    for (let i = 1; i < n; i++) {
        if (i <= r) {
            z[i] = Math.min(r - i + 1, z[i - l]);
        }
        
        while (i + z[i] < n && s[z[i]] === s[i + z[i]]) {
            z[i]++;
        }
        
        if (i + z[i] - 1 > r) {
            l = i;
            r = i + z[i] - 1;
        }
    }
    
    z[0] = n; // Convention for pattern searching

    return z;
}

function zAlgorithmSearchTS(text: string, pattern: string): number[] {
    const n = text.length;
    const m = pattern.length;
    if (m === 0) return [];
    if (n === 0) return [];

    const combinedString = pattern + "$" + text;
    const zArray = computeZArrayTS(combinedString);
    
    const results: number[] = [];
    for (let i = m + 1; i < combinedString.length; i++) {
        if (zArray[i] === m) {
            results.push(i - (m + 1));
        }
    }
    return results;
}

// const textTS = "abacaba";
// const patternTS = "aba";
// console.log(zAlgorithmSearchTS(textTS, patternTS)); // [0, 4]
```

### Cpp

```cpp
#include <vector>
#include <string>
#include <iostream>
#include <algorithm> // For std::min

std::vector<int> computeZArray(const std::string& s) {
    int n = s.length();
    std::vector<int> z(n);
    int l = 0, r = 0;

    z[0] = n; // Convention: Z[0] is the length of the string itself

    for (int i = 1; i < n; ++i) {
        if (i <= r) {
            z[i] = std::min(r - i + 1, z[i - l]);
        }
        
        while (i + z[i] < n && s[z[i]] == s[i + z[i]]) {
            z[i]++;
        }
        
        if (i + z[i] - 1 > r) {
            l = i;
            r = i + z[i] - 1;
        }
    }
    return z;
}

std::vector<int> zAlgorithmSearch(const std::string& text, const std::string& pattern) {
    int n = text.length();
    int m = pattern.length();
    if (m == 0) return {};
    if (n == 0) return {};

    std::string combined_string = pattern + "$" + text;
    std::vector<int> z_array = computeZArray(combined_string);
    
    std::vector<int> results;
    // Any Z[i] that equals the length of P indicates an occurrence
    for (int i = m + 1; i < combined_string.length(); ++i) { // Start search after pattern + delimiter
        if (z_array[i] == m) {
            results.push_back(i - (m + 1)); // Adjust index back to original text
        }
    }
    return results;
}

// int main() {
//     std::string text = "abacaba";
//     std::string pattern = "aba";
//     std::vector<int> matches = zAlgorithmSearch(text, pattern);
//     for (int pos : matches) {
//         std::cout << "Pattern found at index " << pos << std::endl; // 0, 4
//     }
//     return 0;
// }
```

### Go

```go
package main

import (
    "fmt"
    "strings"
)

func computeZArray(s string) []int {
    n := len(s)
    z := make([]int, n)
    l, r := 0, 0

    // z[0] is typically not part of this definition or is set to 0.
    // We set it to n at the end for pattern searching convention.

    for i := 1; i < n; i++ {
        if i <= r {
            z[i] = min(r - i + 1, z[i - l])
        }
        
        for i + z[i] < n && s[z[i]] == s[i + z[i]] {
            z[i]++
        }
        
        if i + z[i] - 1 > r {
            l = i
            r = i + z[i] - 1
        }
    }
    
    z[0] = n // Convention for pattern searching

    return z
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func zAlgorithmSearch(text, pattern string) []int {
    n := len(text)
    m := len(pattern)
    if m == 0 { return []int{} }
    if n == 0 { return []int{} }

    combinedString := pattern + "$" + text
    zArray := computeZArray(combinedString)
    
    results := []int{}
    // Any Z[i] that equals the length of P indicates an occurrence
    for i := m + 1; i < len(combinedString); i++ { // Start search after pattern + delimiter
        if zArray[i] == m {
            results = append(results, i - (m + 1)) // Adjust index back to original text
        }
    }
    return results
}

// func main() {
//     text := "abacaba"
//     pattern := "aba"
//     fmt.Println(zAlgorithmSearch(text, pattern)) // [0 4]
// }
```

### D

```d
import std.stdio;
import std.array;
import std.string;
import std.algorithm; // For std.algorithm.min

int[] computeZArray(string s) {
    auto n = s.length;
    auto z = new int[n];
    int l = 0, r = 0;

    // z[0] is typically not part of this definition or is set to 0.
    // We set it to n at the end for pattern searching convention.

    foreach (i; 1..n) {
        if (i <= r) {
            z[i] = min(r - i + 1, z[i - l]);
        }
        
        while (i + z[i] < n && s[z[i]] == s[i + z[i]]) {
            z[i]++;
        }
        
        if (i + z[i] - 1 > r) {
            l = i;
            r = i + z[i] - 1;
        }
    }
    
    z[0] = n; // Convention for pattern searching

    return z;
}

int[] zAlgorithmSearch(string text, string pattern) {
    auto n = text.length;
    auto m = pattern.length;
    if (m == 0) return [];
    if (n == 0) return [];

    auto combinedString = pattern ~ "$" ~ text; // "$" is a unique delimiter
    auto zArray = computeZArray(combinedString);
    
    int[] results;
    // Any Z[i] that equals the length of P indicates an occurrence
    foreach (i; m + 1 .. combinedString.length) { // Start search after pattern + delimiter
        if (zArray[i] == m) {
            results ~= (i - (m + 1)); // Adjust index back to original text
        }
    }
    return results;
}

// void main() {
//     string text = "abacaba";
//     string pattern = "aba";
//     writeln(zAlgorithmSearch(text, pattern)); // [0, 4]
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

The `Z-Algorithm` is primarily known for its efficient computation of the `Z-array`. This array is then used to find pattern occurrences.

---

**`computeZArray(s)` Function:**
- `n`: The length of the input string `s`.
- `z`: The `Z-array` to be computed.
- `l`, `r`: Pointers defining the current `Z-box` `[L, R]`, which is the longest substring starting at `L` that is also a prefix of `S` and extends furthest to the right.

**Algorithm for Z-array:**
- `Z[0]` is typically defined as `n` for pattern searching, as the entire string `S` matches `S` starting at `index 0`.
- The loop iterates from `i = 1` to `n-1`.
- **Case 1: `i` is outside the current `Z-box` (`i > r`).**
- No prefix information can be reused. `Z[i]` is computed by brute-force comparison of `S[i...]` with `S[0...]`.
- If a new `Z-box` is found (i.e., `Z[i] > 0`), update `L = i` and `R = i + Z[i] - 1`.

    </li>
- **Case 2: `i` is inside the current `Z-box` (`i <= r`).**
- Let `k = i - L`. This `Z[k]` value is for a string that is a substring of the current `Z-box`.
- If `Z[k]` is strictly less than the remaining length of the current `Z-box` (`r - i + 1`), then `Z[i]` can simply be set to `Z[k]`.
- If `Z[k]` is greater than or equal to `r - i + 1`, it means `Z[i]` might extend beyond `R`. We can reuse the `Z[k]` value up to `R`, and then extend by brute-force comparison beyond `R`. Update `L=i` and `R=i + Z[i] - 1`.

    </li>

**`zAlgorithmSearch(text, pattern)` Function:**
- Constructs a new `combined_string` by concatenating `pattern`, a unique delimiter (like `$`), and `text`.
- Computes the `Z-array` for this `combined_string`.
- Any `Z[i]` value in the `Z-array` that is equal to the length of the `pattern` `m`, and whose `index i` is past the delimiter, indicates an occurrence of the `pattern` in the `text`. The corresponding `index` in the original `text` is `i - (m + 1)`.

[Back to Implementation](#implementation)

## Applications

### Application

The `Z-Algorithm` is a versatile string matching algorithm often favored for its simplicity in implementation and linear time complexity.
- **Pattern Searching:** Finds all occurrences of a `pattern` in a `text` in linear time, competing with KMP.
- **Longest Common Prefix for Suffixes:** The `Z-array` itself gives insights into how well various suffixes match the original string's prefix, which is useful in certain string algorithms.
- **String Periodicity:** Can be used to efficiently determine the periodicity of a string.
- **Shortest Unique Substring:** Useful in finding the shortest substring that uniquely identifies a larger string within a set.
- **Bioinformatics:** Utilized in sequence analysis and alignment, particularly in scenarios where finding repetitions and overlaps quickly is important.

