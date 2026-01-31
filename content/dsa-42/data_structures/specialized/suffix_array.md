---
title: "Suffix Array"
---

A `Suffix Array` is a sorted array of all suffixes of a given string. It is a simple, yet powerful data structure used for a wide variety of string processing problems. It provides a more space-efficient alternative to a `Suffix Tree` while still enabling many of the same operations.

By pairing a `Suffix Array` with an `LCP (Longest Common Prefix) array`, one can solve complex problems like finding the longest repeated substring, finding the longest common substring between two strings, and more.

## How it Works

### How it Works (Expanded)

The construction of a `Suffix Array` involves two main steps:
- **Generate all suffixes:** For a string `S` of length `N`, generate all `N` suffixes.
- **Sort the suffixes:** Sort these suffixes lexicographically (alphabetically). The `Suffix Array` itself stores the starting indices of these sorted suffixes.

---

Example for string S = "banana$":

Suffixes:
0: banana$
1: anana$
2: nana$
3: ana$
4: na$
5: a$
6: $

Sorted Suffixes:      Suffix Array (SA):
$:                 6
a$:                5
ana$:              3
anana$:            1
banana$:           0
na$:               4
nana$:             2

## Implementation {#implementation}

### Python

```python
# Simple (naive) Suffix Array construction in Python

def build_suffix_array(s):
    """
    Builds a suffix array for the given string in a simple, readable way.
    Time complexity: O(n^2 <em> log n) due to slicing and sorting.
    """
    # Create a list of all suffixes
    suffixes = [(s[i:], i) for i in range(len(s))]
    
    # Sort the suffixes lexicographically
    suffixes.sort(key=lambda x: x[0])
    
    # Extract the original indices to form the suffix array
    suffix_array = [suffix[1] for suffix in suffixes]
    
    return suffix_array

# Example Usage:
# text = "banana"
# sa = build_suffix_array(text + "$") # Add a special char smaller than any other
# print(f"Suffix Array for 'banana$': {sa}") # Expected: [6, 5, 3, 1, 0, 4, 2]
```

### Javascript

```javascript
// Simple (naive) Suffix Array construction in JavaScript

function buildSuffixArray(s) {
    /</em><em>
     </em> Builds a suffix array for the given string in a simple, readable way.
     <em> Time complexity: O(n^2 </em> log n) due to slicing and sorting.
     <em>/
    // Create an array of all suffixes
    const suffixes = [];
    for (let i = 0; i < s.length; i++) {
        suffixes.push({ suffix: s.substring(i), index: i });
    }

    // Sort the suffixes lexicographically
    suffixes.sort((a, b) => {
        if (a.suffix < b.suffix) return -1;
        if (a.suffix > b.suffix) return 1;
        return 0;
    });

    // Extract the original indices to form the suffix array
    const suffixArray = suffixes.map(item => item.index);

    return suffixArray;
}

// Example Usage:
// const text = "banana";
// const sa = buildSuffixArray(text + "$"); // Add a special char smaller than any other
// console.log(<code>Suffix Array for 'banana$':</code>, sa); // Expected: [6, 5, 3, 1, 0, 4, 2]
```

### Typescript

```typescript
// Simple (naive) Suffix Array construction in TypeScript

function buildSuffixArrayTS(s: string): number[] {
    /</em><em>
     </em> Builds a suffix array for the given string in a simple, readable way.
     <em> Time complexity: O(n^2 </em> log n) due to slicing and sorting.
     */
    interface Suffix {
        suffix: string;
        index: number;
    }

    // Create an array of all suffixes
    const suffixes: Suffix[] = [];
    for (let i = 0; i < s.length; i++) {
        suffixes.push({ suffix: s.substring(i), index: i });
    }

    // Sort the suffixes lexicographically
    suffixes.sort((a, b) => {
        if (a.suffix < b.suffix) return -1;
        if (a.suffix > b.suffix) return 1;
        return 0;
    });

    // Extract the original indices to form the suffix array
    const suffixArray: number[] = suffixes.map(item => item.index);

    return suffixArray;
}

// Example Usage:
// const textTS = "banana";
// const saTS = buildSuffixArrayTS(textTS + "$"); // Add a special char smaller than any other
// console.log(<code>Suffix Array for 'banana$':</code>, saTS); // Expected: [6, 5, 3, 1, 0, 4, 2]
```

### Cpp

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

struct Suffix {
    int index;
    std::string suff;
};

// Comparison function for sorting suffixes
bool compareSuffixes(const Suffix& a, const Suffix& b) {
    return a.suff < b.suff;
}

// Simple (naive) Suffix Array construction
std::vector<int> buildSuffixArray(const std::string& s) {
    int n = s.length();
    std::vector<Suffix> suffixes(n);

    // Create a vector of all suffixes
    for (int i = 0; i < n; ++i) {
        suffixes[i].index = i;
        suffixes[i].suff = s.substr(i);
    }

    // Sort the suffixes lexicographically
    std::sort(suffixes.begin(), suffixes.end(), compareSuffixes);

    // Extract the original indices to form the suffix array
    std::vector<int> suffixArray(n);
    for (int i = 0; i < n; ++i) {
        suffixArray[i] = suffixes[i].index;
    }

    return suffixArray;
}

// Example Usage:
// int main() {
//     std::string text = "banana$";
//     std::vector<int> sa = buildSuffixArray(text);
//     std::cout << "Suffix Array for 'banana$': ";
//     for (int index : sa) {
//         std::cout << index << " ";
//     }
//     std::cout << std::endl; // Expected: 6 5 3 1 0 4 2
//     return 0;
// }
```

### Go

```go
package main

import (
    "fmt"
    "sort"
)

// A struct to hold a suffix and its original index
type Suffix struct {
    Index  int
    Suffix string
}

// A slice of Suffixes that implements sort.Interface
type SuffixSlice []Suffix

func (s SuffixSlice) Len() int           { return len(s) }
func (s SuffixSlice) Less(i, j int) bool { return s[i].Suffix < s[j].Suffix }
func (s SuffixSlice) Swap(i, j int)      { s[i], s[j] = s[j], s[i] }

// Simple (naive) Suffix Array construction
func buildSuffixArray(s string) []int {
    n := len(s)
    suffixes := make(SuffixSlice, n)

    // Create a slice of all suffixes
    for i := 0; i < n; i++ {
        suffixes[i] = Suffix{Index: i, Suffix: s[i:]}
    }

    // Sort the suffixes lexicographically
    sort.Sort(suffixes)

    // Extract the original indices to form the suffix array
    suffixArray := make([]int, n)
    for i := 0; i < n; i++ {
        suffixArray[i] = suffixes[i].Index
    }

    return suffixArray
}

// func main() {
//     text := "banana$"
//     sa := buildSuffixArray(text)
//     fmt.Printf("Suffix Array for '%s': %v\n", text, sa) // Expected: [6 5 3 1 0 4 2]
// }
```

### D

```d
import std.stdio;
import std.algorithm;
import std.array;
import std.range;

struct Suffix {
    int index;
    string suffix;
}

// Simple (naive) Suffix Array construction
int[] buildSuffixArray(string s) {
    auto n = s.length;
    auto suffixes = new Suffix[n];

    // Create an array of all suffixes
    foreach (i; 0..n) {
        suffixes[i] = Suffix(cast(int)i, s[i..$]);
    }

    // Sort the suffixes lexicographically
    sort!((a, b) => a.suffix < b.suffix)(suffixes);

    // Extract the original indices to form the suffix array
    auto suffixArray = new int[n];
    foreach (i, suf; suffixes) {
        suffixArray[i] = suf.index;
    }

    return suffixArray;
}

// void main() {
//     auto text = "banana$";
//     auto sa = buildSuffixArray(text);
//     writefln("Suffix Array for '%s': %s", text, sa); // Expected: [6, 5, 3, 1, 0, 4, 2]
// }
```

## Applications

### Application
    <p>Suffix Arrays are a fundamental tool in stringology and bioinformatics. Their primary use is for **fast substring searching** (finding if a pattern exists in a text). They are the core of many full-text search utilities like `grep`. In **bioinformatics**, they are used to find long repeated sequences or commonalities within DNA or protein sequences. They are also used in **data compression** algorithms and for problems like finding the longest repeated substring or the longest common substring between two strings.</p>

