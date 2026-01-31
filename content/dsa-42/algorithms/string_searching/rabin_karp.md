---
title: "Rabin-Karp Algorithm"
---

The `Rabin-Karp Algorithm` is a string searching algorithm that uses `hashing` to find any one of a set of `pattern` strings in a `text`. Instead of directly comparing the `pattern` with every substring of the `text`, it computes a `hash value` for the `pattern` and for each substring of the `text` of the same length. If the `hash values` match, it then performs a full character-by-character comparison to confirm a true match.

Its primary advantage lies in its ability to efficiently find *multiple* patterns simultaneously and in its generally good average-case performance. Its average-case time complexity is `O(N + M)`, where `N` is the length of the text and `M` is the length of the pattern, but its worst-case can be `O(N <em> M)` due to hash collisions.

## How it Works

### How it Works (Expanded)

The key to `Rabin-Karp` is the use of a "`rolling hash`" (also known as a "`polynomial hashing`") function. A `rolling hash` allows the hash of a substring to be updated in constant time as the window slides, without recomputing the hash from scratch.

---

Example: Search for Pattern "abc" in Text "ababcab"

1. Pattern Hash: h("abc") = (a</em>p^2 + b*p^1 + c*p^0) mod Q
   (e.g., if p=31, Q=101, then h("abc") = (97*31^2 + 98*31^1 + 99<em>31^0) mod 101)

2. Text Substring Hashes (sliding window):
- h("aba") = (a</em>p^2 + b*p^1 + a*p^0) mod Q
- h("bab") = (b*p^2 + a*p^1 + b<em>p^0) mod Q (derived from h("aba") in O(1))
- h("abc") = ... Match! Then verify character by character.
- ... and so on.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
def rabin_karp_search(text, pattern, prime=101, base=256):
    n = len(text)
    m = len(pattern)
    if m == 0 or m > n:
        return []

    pattern_hash = 0
    text_hash = 0
    h = 1 # h = base^(m-1) % prime
    
    results = []

    # Precompute h
    for i in range(m - 1):
        h = (h <em> base) % prime

    # Compute hash of pattern and first text window
    for i in range(m):
        pattern_hash = (pattern_hash </em> base + ord(pattern[i])) % prime
        text_hash = (text_hash <em> base + ord(text[i])) % prime

    # Slide the pattern over text
    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            # Check for character-by-character match to avoid spurious hits
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                results.append(i)

        # Calculate hash for next window of text
        if i < n - m:
            text_hash = (text_hash - ord(text[i]) </em> h) % prime
            text_hash = (text_hash <em> base + ord(text[i + m])) % prime
            text_hash = (text_hash + prime) % prime # Ensure positive hash

    return results

# Example
# text = "GEEKS FOR GEEKS"
# pattern = "GEEK"
# print(rabin_karp_search(text, pattern)) # [0, 10]

# text2 = "AAAAA"
# pattern2 = "AAA"
# print(rabin_karp_search(text2, pattern2)) # [0, 1, 2]
```

### Javascript

```javascript
function rabinKarpSearch(text, pattern, prime = 101, base = 256) {
    const n = text.length;
    const m = pattern.length;
    if (m === 0 || m > n) {
        return [];
    }

    let patternHash = 0;
    let textHash = 0;
    let h = 1; // h = base^(m-1) % prime
    
    const results = [];

    // Precompute h (base^(m-1) % prime)
    for (let i = 0; i < m - 1; i++) {
        h = (h </em> base) % prime;
    }

    // Compute hash of pattern and first text window
    for (let i = 0; i < m; i++) {
        patternHash = (patternHash <em> base + text.charCodeAt(i)) % prime;
        textHash = (textHash </em> base + pattern.charCodeAt(i)) % prime; // Fixed: pattern.charCodeAt(i)
    }
    
    // Corrected to reflect pattern_hash and text_hash usage
    let correctPatternHash = 0;
    for (let i = 0; i < m; i++) {
        correctPatternHash = (correctPatternHash <em> base + pattern.charCodeAt(i)) % prime;
    }
    
    let currentTextHash = 0;
    for (let i = 0; i < m; i++) {
        currentTextHash = (currentTextHash </em> base + text.charCodeAt(i)) % prime;
    }


    // Slide the pattern over text
    for (let i = 0; i <= n - m; i++) {
        if (correctPatternHash === currentTextHash) {
            // Check for character-by-character match to avoid spurious hits
            let match = true;
            for (let j = 0; j < m; j++) {
                if (text[i + j] !== pattern[j]) {
                    match = false;
                    break;
                }
            }
            if (match) {
                results.push(i);
            }
        }

        // Calculate hash for next window of text
        if (i < n - m) {
            currentTextHash = (currentTextHash - text.charCodeAt(i) <em> h) % prime;
            currentTextHash = (currentTextHash </em> base + text.charCodeAt(i + m)) % prime;
            currentTextHash = (currentTextHash + prime) % prime; // Ensure positive hash
        }
    }

    return results;
}

// const text = "GEEKS FOR GEEKS";
// const pattern = "GEEK";
// console.log(rabinKarpSearch(text, pattern)); // [0, 10]

// const text2 = "AAAAA";
// const pattern2 = "AAA";
// console.log(rabinKarpSearch(text2, pattern2)); // [0, 1, 2]
```

### Typescript

```typescript
function rabinKarpSearchTS(text: string, pattern: string, prime: number = 101, base: number = 256): number[] {
    const n = text.length;
    const m = pattern.length;
    if (m === 0 || m > n) {
        return [];
    }

    let patternHash = 0;
    let textHash = 0;
    let h = 1; // h = base^(m-1) % prime
    
    const results: number[] = [];

    // Precompute h (base^(m-1) % prime)
    for (let i = 0; i < m - 1; i++) {
        h = (h <em> base) % prime;
    }

    // Compute hash of pattern and first text window
    for (let i = 0; i < m; i++) {
        patternHash = (patternHash </em> base + pattern.charCodeAt(i)) % prime;
        textHash = (textHash <em> base + text.charCodeAt(i)) % prime;
    }

    // Slide the pattern over text
    for (let i = 0; i <= n - m; i++) {
        if (patternHash === textHash) {
            // Check for character-by-character match to avoid spurious hits
            let match = true;
            for (let j = 0; j < m; j++) {
                if (text[i + j] !== pattern[j]) {
                    match = false;
                    break;
                }
            }
            if (match) {
                results.push(i);
            }
        }

        // Calculate hash for next window of text
        if (i < n - m) {
            textHash = (textHash - text.charCodeAt(i) </em> h) % prime;
            textHash = (textHash <em> base + text.charCodeAt(i + m)) % prime;
            textHash = (textHash + prime) % prime; // Ensure positive hash
        }
    }

    return results;
}

// const textTS = "GEEKS FOR GEEKS";
// const patternTS = "GEEK";
// console.log(rabinKarpSearchTS(textTS, patternTS)); // [0, 10]

// const text2TS = "AAAAA";
// const pattern2TS = "AAA";
// console.log(rabinKarpSearchTS(text2TS, pattern2TS)); // [0, 1, 2]
```

### Cpp

```cpp
#include <string>
#include <vector>
#include <iostream>

// d is the number of characters in the input alphabet
// For ASCII characters, d can be 256
const int BASE = 256;

void rabinKarpSearch(const std::string& text, const std::string& pattern, int prime) {
    int n = text.length();
    int m = pattern.length();
    if (m == 0 || m > n) return;

    int pattern_hash = 0; // hash value for pattern
    int text_hash = 0;    // hash value for text
    int h = 1;            // h = BASE^(m-1) % prime

    // The value of h would be "pow(BASE, m-1)%prime"
    for (int i = 0; i < m - 1; i++) {
        h = (h </em> BASE) % prime;
    }

    // Calculate the hash value of pattern and first window of text
    for (int i = 0; i < m; i++) {
        pattern_hash = (BASE <em> pattern_hash + pattern[i]) % prime;
        text_hash = (BASE </em> text_hash + text[i]) % prime;
    }

    // Slide the pattern over text one by one
    for (int i = 0; i <= n - m; i++) {
        // Check if hash values match
        if (pattern_hash == text_hash) {
            // If hash values match, then only check characters one by one
            bool match = true;
            for (int j = 0; j < m; j++) {
                if (text[i + j] != pattern[j]) {
                    match = false;
                    break;
                }
            }
            if (match) {
                std::cout << "Pattern found at index " << i << std::endl;
            }
        }

        // Calculate hash value for next window of text: Remove leading digit, add trailing digit
        if (i < n - m) {
            text_hash = (BASE <em> (text_hash - text[i] </em> h) + text[i + m]) % prime;

            // We might get negative value of text_hash, converting it to positive
            if (text_hash < 0) {
                text_hash = (text_hash + prime);
            }
        }
    }
}

// int main() {
//     std::string text = "GEEKS FOR GEEKS";
//     std::string pattern = "GEEK";
//     rabinKarpSearch(text, pattern, 101); // 101 is a prime number

//     std::string text2 = "AAAAA";
//     std::string pattern2 = "AAA";
//     rabinKarpSearch(text2, pattern2, 101);
// }
```

### Go

```go
package main

import "fmt"

const BASE_GO = 256

func rabinKarpSearch(text, pattern string, prime int) []int {
    n := len(text)
    m := len(pattern)
    if m == 0 || m > n {
        return nil
    }

    patternHash := 0
    textHash := 0
    h := 1 // h = BASE^(m-1) % prime
    
    results := []int{}

    // Precompute h (BASE^(m-1) % prime)
    for i := 0; i < m-1; i++ {
        h = (h <em> BASE_GO) % prime
    }

    // Compute hash of pattern and first text window
    for i := 0; i < m; i++ {
        patternHash = (patternHash</em>BASE_GO + int(pattern[i])) % prime
        textHash = (textHash<em>BASE_GO + int(text[i])) % prime
    }

    // Slide the pattern over text
    for i := 0; i <= n-m; i++ {
        if patternHash == textHash {
            // Check for character-by-character match to avoid spurious hits
            match := true
            for j := 0; j < m; j++ {
                if text[i+j] != pattern[j] {
                    match = false
                    break
                }
            }
            if match {
                results = append(results, i)
            }
        }

        // Calculate hash for next window of text
        if i < n-m {
            textHash = (textHash - int(text[i])</em>h) % prime
            textHash = (textHash<em>BASE_GO + int(text[i+m])) % prime
            textHash = (textHash + prime) % prime // Ensure positive hash
        }
    }

    return results
}

// func main() {
//     text := "GEEKS FOR GEEKS"
//     pattern := "GEEK"
//     fmt.Println(rabinKarpSearch(text, pattern, 101)) // [0 10]

//     text2 := "AAAAA"
//     pattern2 := "AAA"
//     fmt.Println(rabinKarpSearch(text2, pattern2, 101)) // [0 1 2]
// }
```

### D

```d
import std.stdio;
import std.array;

enum int BASE_D = 256;

int[] rabinKarpSearch(string text, string pattern, int prime) {
    auto n = text.length;
    auto m = pattern.length;
    if (m == 0 || m > n) {
        return [];
    }

    int patternHash = 0;
    int textHash = 0;
    int h = 1; // h = BASE^(m-1) % prime
    
    int[] results;

    // Precompute h (BASE^(m-1) % prime)
    for (int i = 0; i < m - 1; i++) {
        h = (h </em> BASE_D) % prime;
    }

    // Compute hash of pattern and first text window
    for (int i = 0; i < m; i++) {
        patternHash = (patternHash <em> BASE_D + text[i]) % prime; // Use text[i] for character value
        textHash = (textHash </em> BASE_D + pattern[i]) % prime;     // Use pattern[i] for character value
    }
    
    // Recalculate based on corrected example
    int actualPatternHash = 0;
    for (int i = 0; i < m; i++) {
        actualPatternHash = (actualPatternHash <em> BASE_D + pattern[i]) % prime;
    }
    
    int currentTextHash = 0;
    for (int i = 0; i < m; i++) {
        currentTextHash = (currentTextHash </em> BASE_D + text[i]) % prime;
    }


    // Slide the pattern over text
    for (int i = 0; i <= n - m; i++) {
        if (actualPatternHash == currentTextHash) {
            // Check for character-by-character match to avoid spurious hits
            bool match = true;
            for (int j = 0; j < m; j++) {
                if (text[i + j] != pattern[j]) {
                    match = false;
                    break;
                }
            }
            if (match) {
                results ~= i;
            }
        }

        // Calculate hash for next window of text
        if (i < n - m) {
            currentTextHash = (currentTextHash - text[i] <em> h) % prime;
            currentTextHash = (currentTextHash </em> BASE_D + text[i + m]) % prime;
            currentTextHash = (currentTextHash + prime) % prime; // Ensure positive hash
        }
    }

    return results;
}

// void main() {
//     string text = "GEEKS FOR GEEKS";
//     string pattern = "GEEK";
//     writeln(rabinKarpSearch(text, pattern, 101)); // [0, 10]

//     string text2 = "AAAAA";
//     string pattern2 = "AAA";
//     writeln(rabinKarpSearch(text2, pattern2, 101)); // [0, 1, 2]
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

The `Rabin-Karp algorithm` leverages `hashing` and a "`rolling hash`" technique to quickly compare substrings, reducing the need for costly character-by-character comparisons.

---

**Initialization:**
- `n`, `m`: Lengths of `text` and `pattern`.
- `pattern_hash`, `text_hash`: Variables to store the calculated hash values.
- `prime`: A large prime number used for the modulo operation in hashing to reduce hash collisions.
- `base`: The size of the alphabet (e.g., 256 for ASCII).
- `h`: A precomputed value `base^(m-1) % prime`, used to efficiently remove the contribution of the leading character in the `rolling hash` calculation.

**Hash Calculation:**
- The `pattern_hash` and the `text_hash` for the first window of the `text` (of length `m`) are computed using the polynomial hashing formula. Each character's ASCII value contributes to the hash, weighted by powers of `base`.

**Sliding Window and Comparison:**
- The algorithm then slides a window of size `m` across the `text`.
- In each step, it compares `pattern_hash` with `text_hash`.
- **Hash Match:** If the hashes match, a potential match is found. A full character-by-character comparison is then performed to confirm it's not a `spurious hit` (a hash collision). If confirmed, the `index` is recorded.
- **Rolling Hash Update:** If it's not the last window, the `text_hash` is updated for the next window in `O(1)` time using the `rolling hash` formula:
- Subtract the contribution of the character leaving the window (`text[i] <em> h`).
- Multiply by `base` to shift the remaining characters' contributions.
- Add the contribution of the new character entering the window (`text[i + m]`).
- Apply the modulo `prime` at each step to keep the numbers manageable.
- A `prime` addition might be needed to handle negative results from the modulo operator in some languages.

    </li>

[Back to Implementation](#implementation)

## Applications

### Application

The `Rabin-Karp Algorithm` is particularly powerful for problems involving multiple pattern searches or when hash collisions are rare.
- **Plagiarism Detection:** Can be extended to find cases of plagiarism across many documents by hashing sentences or blocks of text.
- **Bioinformatics:** Searching for patterns in large biological sequences (DNA, RNA, protein).
- **File System Integrity:** Checking for duplicate files or identifying corrupted blocks by comparing hashes.
- **Network Intrusion Detection:** Scanning network packets for known attack signatures, especially when a large database of signatures needs to be checked against streaming data.
- **Finding Multiple Patterns:** It can be easily modified to find any one of `k` patterns in `O(N + M</em>K)` in the worst case, but `O(N + K)` on average, where `K` is the number of patterns and `M` is the pattern length.

