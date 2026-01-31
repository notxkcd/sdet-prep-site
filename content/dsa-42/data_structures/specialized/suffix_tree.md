---
title: "Suffix Tree"
---

A `Suffix Tree` is a data structure that stores all the suffixes of a given string in a compressed trie-like structure. It's a powerful tool for solving a wide range of string problems, often in linear time relative to the length of the string.

Each path from the `root` of the `tree` to a `leaf` represents a unique suffix of the string. The edges of the `tree` are labeled with substrings of the original string. This compression is what makes it highly efficient for complex text processing.

## How it Works

### How it Works (Expanded)

A `Suffix Tree` for a string `S` of length `N` has exactly `N` leaves, each corresponding to a unique suffix of `S`. The edges are labeled such that following a path from the `root` to a `leaf` spells out a suffix of `S`. Crucially, common prefixes among suffixes share common paths from the `root`, leading to compression.

To ensure every suffix ends at a leaf and to handle cases where one suffix is a prefix of another, a unique terminator character (e.g., `$`) is usually appended to the string `S` before building the `Suffix Tree`.

---

Example: S = "banana$"

Suffixes:
banana$
anana$
nana$
ana$
na$
a$
$

The Suffix Tree (conceptual, not actual build):

        (root)
       /  \  \  \
      $    a   b  n
          /|\   |  |
         ...   ... ...
        /  \
       na   nana$
      / \
     na$ anana$

## Implementation {#implementation}

### Python

```python
# Conceptual Suffix Tree in Python (simplified, full implementation is very complex)
# This shows the basic Node structure and search idea for understanding.

class SuffixTreeNode:
    def __init__(self):
        self.children = {} # Map char to SuffixTreeNode
        self.suffix_indices = [] # List of starting indices of suffixes passing through this node

    def insert(self, suffix, start_index):
        self.suffix_indices.append(start_index)
        if not suffix: # End of a suffix
            return

        char = suffix[0]
        if char not in self.children:
            self.children[char] = SuffixTreeNode()
        self.children[char].insert(suffix[1:], start_index)

    def search(self, pattern):
        node = self
        for char in pattern:
            if char in node.children:
                node = node.children[char]
            else:
                return [] # Pattern not found
        return node.suffix_indices # Return all occurrences (start indices)

# Main function to build a conceptual Suffix Tree
def build_conceptual_suffix_tree(text):
    root = SuffixTreeNode()
    for i in range(len(text)):
        root.insert(text[i:], i)
    return root

# Example Usage:
# text = "banana$"
# st = build_conceptual_suffix_tree(text)

# print(st.search("ana")) # Expected to return indices where "ana" starts, e.g., [1, 3]
# print(st.search("nan")) # Expected: [2]
# print(st.search("apple")) # Expected: []
```

### Javascript

```javascript
// Conceptual Suffix Tree in JavaScript (simplified)

class SuffixTreeNode {
    constructor() {
        this.children = new Map(); // Map char to SuffixTreeNode
        this.suffixIndices = []; // List of starting indices of suffixes passing through this node
    }

    insert(suffix, startIndex) {
        this.suffixIndices.push(startIndex);
        if (!suffix) { // End of a suffix
            return;
        }

        const char = suffix[0];
        if (!this.children.has(char)) {
            this.children.set(char, new SuffixTreeNode());
        }
        this.children.get(char).insert(suffix.substring(1), startIndex);
    }

    search(pattern) {
        let node = this;
        for (const char of pattern) {
            if (node.children.has(char)) {
                node = node.children.get(char);
            } else {
                return []; // Pattern not found
            }
        }
        return node.suffixIndices; // Return all occurrences (start indices)
    }
}

// Main function to build a conceptual Suffix Tree
function buildConceptualSuffixTree(text) {
    const root = new SuffixTreeNode();
    for (let i = 0; i < text.length; i++) {
        root.insert(text.substring(i), i);
    }
    return root;
}

// const text = "banana$";
// const st = buildConceptualSuffixTree(text);

// console.log(st.search("ana")); // Expected: [1, 3]
// console.log(st.search("nan")); // Expected: [2]
// console.log(st.search("apple")); // Expected: []
```

### Typescript

```typescript
// Conceptual Suffix Tree in TypeScript (simplified)

class SuffixTreeNodeTS {
    public children: Map<string, SuffixTreeNodeTS>; // Map char to SuffixTreeNode
    public suffixIndices: number[]; // List of starting indices of suffixes passing through this node

    constructor() {
        this.children = new Map();
        this.suffixIndices = [];
    }

    public insert(suffix: string, startIndex: number): void {
        this.suffixIndices.push(startIndex);
        if (!suffix) { // End of a suffix
            return;
        }

        const char = suffix[0];
        if (!this.children.has(char)) {
            this.children.set(char, new SuffixTreeNodeTS());
        }
        this.children.get(char)!.insert(suffix.substring(1), startIndex);
    }

    public search(pattern: string): number[] {
        let node: SuffixTreeNodeTS = this;
        for (const char of pattern) {
            if (node.children.has(char)) {
                node = node.children.get(char)!;
            } else {
                return []; // Pattern not found
            }
        }
        return node.suffixIndices; // Return all occurrences (start indices)
    }
}

// Main function to build a conceptual Suffix Tree
function buildConceptualSuffixTreeTS(text: string): SuffixTreeNodeTS {
    const root = new SuffixTreeNodeTS();
    for (let i = 0; i < text.length; i++) {
        root.insert(text.substring(i), i);
    }
    return root;
}

// const textTS = "banana$";
// const stTS = buildConceptualSuffixTreeTS(textTS);

// console.log(stTS.search("ana")); // Expected: [1, 3]
// console.log(stTS.search("nan")); // Expected: [2]
// console.log(stTS.search("apple")); // Expected: []
```

### Cpp

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <map>

// Conceptual Suffix Tree Node (simplified)
class SuffixTreeNode {
public:
    std::map<char, SuffixTreeNode<em>> children; // Map char to SuffixTreeNode
    std::vector<int> suffix_indices;          // List of starting indices of suffixes passing through this node

    SuffixTreeNode() {}

    ~SuffixTreeNode() {
        // Proper memory management for large trees can be complex.
        // For this conceptual example, a simple destructor to avoid immediate leaks.
        for (auto const& [key, val] : children) {
            delete val;
        }
    }

    void insert(const std::string& suffix, int start_index) {
        suffix_indices.push_back(start_index);
        if (suffix.empty()) { // End of a suffix
            return;
        }

        char char_to_insert = suffix[0];
        if (children.find(char_to_insert) == children.end()) {
            children[char_to_insert] = new SuffixTreeNode();
        }
        children[char_to_insert]->insert(suffix.substr(1), start_index);
    }

    std::vector<int> search(const std::string& pattern) {
        SuffixTreeNode</em> node = this;
        for (char char_to_find : pattern) {
            if (node->children.find(char_to_find) != node->children.end()) {
                node = node->children[char_to_find];
            } else {
                return {}; // Pattern not found
            }
        }
        return node->suffix_indices; // Return all occurrences (start indices)
    }
};

// Main function to build a conceptual Suffix Tree
SuffixTreeNode<em> buildConceptualSuffixTree(const std::string& text) {
    SuffixTreeNode</em> root = new SuffixTreeNode();
    for (int i = 0; i < text.length(); ++i) {
        root->insert(text.substr(i), i);
    }
    return root;
}

// int main() {
//     std::string text = "banana$";
//     SuffixTreeNode<em> st = buildConceptualSuffixTree(text);

//     std::vector<int> ana_indices = st->search("ana");
//     std::cout << "Search 'ana': "; // Expected: 1 3
//     for (int idx : ana_indices) std::cout << idx << " ";
//     std::cout << std::endl;

//     std::vector<int> nan_indices = st->search("nan");
//     std::cout << "Search 'nan': "; // Expected: 2
//     for (int idx : nan_indices) std::cout << idx << " ";
//     std::cout << std::endl;

//     std::vector<int> apple_indices = st->search("apple");
//     std::cout << "Search 'apple': "; // Expected: (empty)
//     for (int idx : apple_indices) std::cout << idx << " ";
//     std::cout << std::endl;

//     delete st; // Clean up memory
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

// Conceptual Suffix Tree Node (simplified)
type SuffixTreeNode struct {
    Children     map[rune]</em>SuffixTreeNode // Map char to SuffixTreeNode
    SuffixIndices []int                    // List of starting indices of suffixes passing through this node
}

func NewSuffixTreeNode() <em>SuffixTreeNode {
    return &SuffixTreeNode{
        Children:      make(map[rune]</em>SuffixTreeNode),
        SuffixIndices: []int{},
    }
}

func (node <em>SuffixTreeNode) Insert(suffix string, startIndex int) {
    node.SuffixIndices = append(node.SuffixIndices, startIndex)
    if len(suffix) == 0 { // End of a suffix
        return
    }

    charToInsert := rune(suffix[0])
    if _, ok := node.Children[charToInsert]; !ok {
        node.Children[charToInsert] = NewSuffixTreeNode()
    }
    node.Children[charToInsert].Insert(suffix[1:], startIndex)
}

func (node </em>SuffixTreeNode) Search(pattern string) []int {
    currNode := node
    for _, charToFind := range pattern {
        if nextNode, ok := currNode.Children[charToFind]; ok {
            currNode = nextNode
        } else {
            return []int{} // Pattern not found
        }
    }
    return currNode.SuffixIndices // Return all occurrences (start indices)
}

// Main function to build a conceptual Suffix Tree
func BuildConceptualSuffixTree(text string) *SuffixTreeNode {
    root := NewSuffixTreeNode()
    for i := 0; i < len(text); i++ {
        root.Insert(text[i:], i)
    }
    return root
}

// func main() {
//     text := "banana$"
//     st := BuildConceptualSuffixTree(text)

//     fmt.Println("Search 'ana':", st.Search("ana"))   // Expected: [1 3]
//     fmt.Println("Search 'nan':", st.Search("nan"))   // Expected: [2]
//     fmt.Println("Search 'apple':", st.Search("apple")) // Expected: []
// }
```

### D

```d
import std.stdio;
import std.string;
import std.array;
import std.exception;
import std.container.array;

// Conceptual Suffix Tree Node (simplified)
class SuffixTreeNode {
    this() {
        children = new HashMap!(char, SuffixTreeNode)();
        suffixIndices = new Array!(int);
    }

    HashMap!(char, SuffixTreeNode) children; // Map char to SuffixTreeNode
    Array!(int) suffixIndices;                // List of starting indices of suffixes passing through this node

    void insert(string suffix, int startIndex) {
        suffixIndices.insertBack(startIndex);
        if (suffix.empty) { // End of a suffix
            return;
        }

        char charToInsert = suffix[0];
        if (!(charToInsert in children)) {
            children[charToInsert] = new SuffixTreeNode();
        }
        children[charToInsert].insert(suffix[1..$], cast(int)startIndex);
    }

    Array!(int) search(string pattern) {
        SuffixTreeNode node = this;
        foreach (char charToFind; pattern) {
            if (charToFind in node.children) {
                node = node.children[charToFind];
            } else {
                return new Array!(int); // Pattern not found
            }
        }
        return node.suffixIndices; // Return all occurrences (start indices)
    }
}

// Main function to build a conceptual Suffix Tree
SuffixTreeNode buildConceptualSuffixTree(string text) {
    auto root = new SuffixTreeNode();
    foreach (i; 0..text.length) {
        root.insert(text[i..$], cast(int)i);
    }
    return root;
}

// void main() {
//     string text = "banana$";
//     auto st = buildConceptualSuffixTree(text);

//     writeln("Search 'ana': ", st.search("ana"));   // Expected: [1, 3]
//     writeln("Search 'nan': ", st.search("nan"));   // Expected: [2]
//     writeln("Search 'apple': ", st.search("apple")); // Expected: []
// }
```

## Applications

### Application

Suffix Trees are incredibly powerful in computational biology, text processing, and data compression. They are used for:
- **Exact String Matching:** Finding all occurrences of a pattern in a text efficiently. This is faster than simple string searching algorithms for multiple searches.
- **Longest Repeated Substring:** Identifying the longest substring that appears at least twice in a text.
- **Longest Common Substring:** Finding the longest common substring between two or more texts (using a generalized Suffix Tree).
- **Bioinformatics:** Essential for genomic analysis, finding similar regions in DNA sequences, identifying gene patterns, and sequence alignment.
- **Data Compression:** Used in algorithms like LZW compression and Burrows-Wheeler Transform.
- **Spell Checkers and Autocomplete:** Though Tries are more common for simple cases, Suffix Trees can handle more complex variations.

