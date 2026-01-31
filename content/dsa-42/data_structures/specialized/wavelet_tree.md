---
title: "Wavelet Tree"
---

A `Wavelet Tree` is a compact data structure used to represent a sequence of symbols from a finite alphabet, enabling efficient solutions to a variety of string and sequence-related queries. It essentially stores a compressed representation of the sequence, allowing for fast `rank`, `select`, and `range` queries.

It's particularly useful in bioinformatics and text processing, where large sequences need to be analyzed efficiently. It can be seen as an extension of the idea of storing a `bit vector` to represent a sequence, but with a recursive structure that handles larger alphabets.

## How it Works

### How it Works (Expanded)

A `Wavelet Tree` is built over a sequence of symbols from an alphabet. The root `node` of the `tree` represents the entire sequence and the entire alphabet. It splits the alphabet into two halves and creates a `bit vector` where each bit indicates whether the corresponding symbol in the sequence belongs to the `left` or `right` half of the alphabet. The `tree` is then built recursively on these two sub-sequences.

---

Example: Build a Wavelet Tree for S = "banana" (alphabet {a,b,n})
- Root (alphabet {a,b,n}):
- Splits alphabet into {a} (left) and {b,n} (right)
- Bit vector: b->1, a->0, n->1, a->0, n->1, a->0 -> [1,0,1,0,1,0]
- Left sub-sequence: [a,a,a]
- Right sub-sequence: [b,n,n]
- Left child (for {a,a,a}) -> base case, leaf
- Right child (for {b,n,n}):
- Splits alphabet into {b} (left) and {n} (right)
- Bit vector: b->0, n->1, n->1 -> [0,1,1]
- ... and so on.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
# Conceptual Wavelet Tree in Python (simplified, full implementation is very complex)
# This focuses on the Node structure and recursive build concept.

class WaveletTreeNode:
    def __init__(self, alphabet, bit_vector):
        self.alphabet = alphabet
        self.bit_vector = bit_vector
        self.left_child = None
        self.right_child = None
        # In a real implementation, bit_vector would be a structure supporting fast rank/select.

class WaveletTree:
    def __init__(self):
        self.root = None
        self.alphabet = []

    def build(self, sequence):
        self.alphabet = sorted(list(set(sequence)))
        if not self.alphabet:
            return
        
        self.root = self._build_recursive(sequence, self.alphabet)

    def _build_recursive(self, sequence, alphabet):
        if not sequence or not alphabet or len(alphabet) == 1:
            return None # Leaf node (or single-symbol sequence)

        # Split alphabet
        mid = len(alphabet) // 2
        left_alphabet = alphabet[:mid]
        right_alphabet = alphabet[mid:]
        
        # Create bit vector and sub-sequences
        bit_vector = []
        left_sequence = []
        right_sequence = []
        
        for symbol in sequence:
            if symbol in left_alphabet:
                bit_vector.append(0)
                left_sequence.append(symbol)
            else:
                bit_vector.append(1)
                right_sequence.append(symbol)

        node = WaveletTreeNode(alphabet, bit_vector)
        node.left_child = self._build_recursive(left_sequence, left_alphabet)
        node.right_child = self._build_recursive(right_sequence, right_alphabet)
        return node
    
    # rank, select, and access methods are complex and omitted for this conceptual demo.
    # They would involve traversing the tree and using rank/select on bit vectors.

# Example Usage:
# wt = WaveletTree()
# wt.build("banana")
# print("Root alphabet:", wt.root.alphabet)
# print("Root bit vector:", wt.root.bit_vector)

# # Expected root alphabet: ['a', 'b', 'n']
# # Expected mid split: left={'a'}, right={'b','n'}
# # 'b'->1, 'a'->0, 'n'->1, 'a'->0, 'n'->1, 'a'->0
# # Expected root bit vector: [1, 0, 1, 0, 1, 0]
```

### Javascript

```javascript
class WaveletTreeNode {
    constructor(alphabet, bitVector) {
        this.alphabet = alphabet;
        this.bitVector = bitVector;
        this.leftChild = null;
        this.rightChild = null;
        // In a real implementation, bitVector would be a structure supporting fast rank/select.
    }
}

class WaveletTree {
    constructor() {
        this.root = null;
        this.alphabet = [];
    }

    build(sequence) {
        this.alphabet = [...new Set(sequence)].sort();
        if (this.alphabet.length === 0) {
            return;
        }
        
        this.root = this._buildRecursive(sequence, this.alphabet);
    }

    _buildRecursive(sequence, alphabet) {
        if (!sequence || sequence.length === 0 || alphabet.length <= 1) {
            return null; // Leaf node (or single-symbol sequence)
        }

        // Split alphabet
        const mid = Math.floor(alphabet.length / 2);
        const leftAlphabet = alphabet.slice(0, mid);
        const rightAlphabet = alphabet.slice(mid);
        const leftAlphabetSet = new Set(leftAlphabet);
        
        // Create bit vector and sub-sequences
        const bitVector = [];
        const leftSequence = [];
        const rightSequence = [];
        
        for (const symbol of sequence) {
            if (leftAlphabetSet.has(symbol)) {
                bitVector.push(0);
                leftSequence.push(symbol);
            } else {
                bitVector.push(1);
                rightSequence.push(symbol);
            }
        }

        const node = new WaveletTreeNode(alphabet, bitVector);
        node.leftChild = this._buildRecursive(leftSequence, leftAlphabet);
        node.rightChild = this._buildRecursive(rightSequence, rightAlphabet);
        return node;
    }
    
    // rank, select, and access methods are complex and omitted for this conceptual demo.
}

// const wt = new WaveletTree();
// wt.build("banana");
// console.log("Root alphabet:", wt.root.alphabet);
// console.log("Root bit vector:", wt.root.bitVector);

// // Expected root alphabet: ['a', 'b', 'n']
// // Expected mid split: left={'a'}, right={'b','n'}
// // 'b'->1, 'a'->0, 'n'->1, 'a'->0, 'n'->1, 'a'->0
// // Expected root bit vector: [1, 0, 1, 0, 1, 0]
```

### Typescript

```typescript
class WaveletTreeNodeTS {
    public alphabet: string[];
    public bitVector: number[];
    public leftChild: WaveletTreeNodeTS | null;
    public rightChild: WaveletTreeNodeTS | null;

    constructor(alphabet: string[], bitVector: number[]) {
        this.alphabet = alphabet;
        this.bitVector = bitVector;
        this.leftChild = null;
        this.rightChild = null;
    }
}

class WaveletTreeTS {
    public root: WaveletTreeNodeTS | null = null;
    public alphabet: string[] = [];

    public build(sequence: string): void {
        this.alphabet = [...new Set(sequence)].sort();
        if (this.alphabet.length === 0) {
            return;
        }
        
        this.root = this._buildRecursive(sequence, this.alphabet);
    }

    private _buildRecursive(sequence: string, alphabet: string[]): WaveletTreeNodeTS | null {
        if (!sequence || sequence.length === 0 || alphabet.length <= 1) {
            return null; // Leaf node (or single-symbol sequence)
        }

        // Split alphabet
        const mid = Math.floor(alphabet.length / 2);
        const leftAlphabet = alphabet.slice(0, mid);
        const rightAlphabet = alphabet.slice(mid);
        const leftAlphabetSet = new Set(leftAlphabet);
        
        // Create bit vector and sub-sequences
        const bitVector: number[] = [];
        let leftSequence = "";
        let rightSequence = "";
        
        for (const symbol of sequence) {
            if (leftAlphabetSet.has(symbol)) {
                bitVector.push(0);
                leftSequence += symbol;
            } else {
                bitVector.push(1);
                rightSequence += symbol;
            }
        }

        const node = new WaveletTreeNodeTS(alphabet, bitVector);
        node.leftChild = this._buildRecursive(leftSequence, leftAlphabet);
        node.rightChild = this._buildRecursive(rightSequence, rightAlphabet);
        return node;
    }
    
    // rank, select, and access methods are complex and omitted for this conceptual demo.
}

// const wtTS = new WaveletTreeTS();
// wtTS.build("banana");
// console.log("Root alphabet:", wtTS.root!.alphabet);
// console.log("Root bit vector:", wtTS.root!.bitVector);
```

### Cpp

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <map>

class WaveletTreeNode {
public:
    std::vector<char> alphabet;
    std::vector<bool> bit_vector; // bool vector is space-efficient in C++
    WaveletTreeNode<em> left_child;
    WaveletTreeNode</em> right_child;

    WaveletTreeNode(const std::vector<char>& alpha, const std::vector<bool>& bv)
        : alphabet(alpha), bit_vector(bv), left_child(nullptr), right_child(nullptr) {}

    ~WaveletTreeNode() {
        delete left_child;
        delete right_child;
    }
};

class WaveletTree {
public:
    WaveletTreeNode<em> root;
    std::vector<char> alphabet;

    WaveletTree() : root(nullptr) {}
    ~WaveletTree() {
        delete root;
    }

    void build(const std::string& sequence) {
        std::set<char> alpha_set(sequence.begin(), sequence.end());
        alphabet.assign(alpha_set.begin(), alpha_set.end());
        if (alphabet.empty()) {
            return;
        }
        
        root = _build_recursive(sequence, alphabet);
    }

private:
    WaveletTreeNode</em> _build_recursive(const std::string& sequence, const std::vector<char>& current_alphabet) {
        if (sequence.empty() || current_alphabet.size() <= 1) {
            return nullptr;
        }

        // Split alphabet
        int mid = current_alphabet.size() / 2;
        std::vector<char> left_alphabet(current_alphabet.begin(), current_alphabet.begin() + mid);
        std::vector<char> right_alphabet(current_alphabet.begin() + mid, current_alphabet.end());
        std::set<char> left_alphabet_set(left_alphabet.begin(), left_alphabet.end());
        
        // Create bit vector and sub-sequences
        std::vector<bool> bit_vector;
        std::string left_sequence, right_sequence;
        
        for (char symbol : sequence) {
            if (left_alphabet_set.count(symbol)) {
                bit_vector.push_back(false); // 0
                left_sequence += symbol;
            } else {
                bit_vector.push_back(true); // 1
                right_sequence += symbol;
            }
        }

        WaveletTreeNode<em> node = new WaveletTreeNode(current_alphabet, bit_vector);
        node->left_child = _build_recursive(left_sequence, left_alphabet);
        node->right_child = _build_recursive(right_sequence, right_alphabet);
        return node;
    }
    
    // rank, select, and access methods are complex and omitted for this conceptual demo.
};

// int main() {
//     WaveletTree wt;
//     wt.build("banana");
//     if (wt.root) {
//         std::cout << "Root bit vector: ";
//         for (bool b : wt.root->bit_vector) {
//             std::cout << b << " "; // 1 0 1 0 1 0
//         }
//         std::cout << std::endl;
//     }
//     return 0;
// }
```

### Go

```go
package main

import (
    "fmt"
    "sort"
    "strings"
)

type WaveletTreeNode struct {
    Alphabet   []rune
    BitVector  []bool
    LeftChild  </em>WaveletTreeNode
    RightChild <em>WaveletTreeNode
}

type WaveletTree struct {
    Root     </em>WaveletTreeNode
    Alphabet []rune
}

func (wt <em>WaveletTree) Build(sequence string) {
    // Find unique characters for alphabet
    charSet := make(map[rune]bool)
    for _, char := range sequence {
        charSet[char] = true
    }
    alphabet := make([]rune, 0, len(charSet))
    for char := range charSet {
        alphabet = append(alphabet, char)
    }
    sort.Slice(alphabet, func(i, j int) bool { return alphabet[i] < alphabet[j] })
    wt.Alphabet = alphabet

    if len(wt.Alphabet) == 0 {
        return
    }

    wt.Root = wt.buildRecursive([]rune(sequence), wt.Alphabet)
}

func (wt </em>WaveletTree) buildRecursive(sequence []rune, alphabet []rune) *WaveletTreeNode {
    if len(sequence) == 0 || len(alphabet) <= 1 {
        return nil
    }

    // Split alphabet
    mid := len(alphabet) / 2
    leftAlphabet := alphabet[:mid]
    rightAlphabet := alphabet[mid:]
    leftAlphabetSet := make(map[rune]bool)
    for _, char := range leftAlphabet {
        leftAlphabetSet[char] = true
    }

    // Create bit vector and sub-sequences
    bitVector := make([]bool, len(sequence))
    leftSequence := []rune{}
    rightSequence := []rune{}

    for i, symbol := range sequence {
        if leftAlphabetSet[symbol] {
            bitVector[i] = false // 0
            leftSequence = append(leftSequence, symbol)
        } else {
            bitVector[i] = true // 1
            rightSequence = append(rightSequence, symbol)
        }
    }

    node := &WaveletTreeNode{
        Alphabet:   alphabet,
        BitVector:  bitVector,
    }
    node.LeftChild = wt.buildRecursive(leftSequence, leftAlphabet)
    node.RightChild = wt.buildRecursive(rightSequence, rightAlphabet)
    return node
}

// func main() {
//     wt := &WaveletTree{}
//     wt.Build("banana")
//     if wt.Root != nil {
//         fmt.Println("Root bit vector:", wt.Root.BitVector)
//         // Convert bool slice to int slice for easier display
//         bitVectorInts := make([]int, len(wt.Root.BitVector))
//         for i, b := range wt.Root.BitVector {
//             if b {
//                 bitVectorInts[i] = 1
//             } else {
//                 bitVectorInts[i] = 0
//             }
//         }
//         fmt.Println("Root bit vector (as ints):", bitVectorInts) // [1 0 1 0 1 0]
//     }
// }
```

### D

```d
import std.stdio;
import std.array;
import std.algorithm;
import std.container.array;
import std.bitmanip; // For BitArray

class WaveletTreeNode {
    char[] alphabet;
    BitArray bitVector;
    WaveletTreeNode leftChild;
    WaveletTreeNode rightChild;

    this(char[] alpha, BitArray bv) {
        this.alphabet = alpha;
        this.bitVector = bv;
        this.leftChild = null;
        this.rightChild = null;
    }
}

class WaveletTree {
    WaveletTreeNode root;
    char[] alphabet;

    void build(string sequence) {
        bool[char] charSet;
        foreach (c; sequence) {
            charSet[c] = true;
        }
        alphabet = charSet.keys.sort().array;

        if (alphabet.length == 0) {
            return;
        }
        
        this.root = buildRecursive(sequence.dup, alphabet);
    }

private:
    WaveletTreeNode buildRecursive(string sequence, char[] currentAlphabet) {
        if (sequence.length == 0 || currentAlphabet.length <= 1) {
            return null;
        }

        // Split alphabet
        auto mid = currentAlphabet.length / 2;
        auto leftAlphabet = currentAlphabet[0 .. mid];
        auto rightAlphabet = currentAlphabet[mid .. $];
        bool[char] leftAlphabetSet;
        foreach (c; leftAlphabet) {
            leftAlphabetSet[c] = true;
        }
        
        // Create bit vector and sub-sequences
        auto bitVector = BitArray(sequence.length);
        string leftSequence, rightSequence;
        
        foreach (i, symbol; sequence) {
            if (symbol in leftAlphabetSet) {
                bitVector[i] = 0;
                leftSequence ~= symbol;
            } else {
                bitVector[i] = 1;
                rightSequence ~= symbol;
            }
        }

        auto node = new WaveletTreeNode(currentAlphabet, bitVector);
        node.leftChild = buildRecursive(leftSequence, leftAlphabet);
        node.rightChild = buildRecursive(rightSequence, rightAlphabet);
        return node;
    }
}

// void main() {
//     auto wt = new WaveletTree();
//     wt.build("banana");
//     if (wt.root !is null) {
//         writefln("Root bit vector: %s", wt.root.bitVector); // 101010
//     }
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

A `Wavelet Tree` is built recursively. The provided conceptual code focuses on this recursive construction, which is the heart of the data structure.

---

**`WaveletTreeNode` Class:** Represents a `node` in the `Wavelet Tree`.
- `alphabet`: The subset of the alphabet this `node` is responsible for.
- `bit_vector`: A `list`/`vector` of bits, where `bit_vector[i]` is 0 if the `i`-th symbol in the sequence belongs to the `left` half of the alphabet, and 1 if it belongs to the `right` half.
- `left_child`, `right_child`: Pointers to child `WaveletTreeNode`s.

**`WaveletTree` Class:**
- `root`: The `root node` of the `Wavelet Tree`.
- `alphabet`: The sorted, unique symbols from the original sequence.
- **`build(sequence)`:** Initializes the alphabet and starts the recursive build process.
- **`_build_recursive(sequence, alphabet)`:**
- Handles the base case: if the sequence is empty or the alphabet has only one symbol, no further subdivision is needed, so return `null`.
- Splits the current `alphabet` into two halves.
- Creates a `bit_vector` by iterating through the current `sequence`. For each symbol, a 0 is appended if it belongs to the `left` half of the alphabet, and a 1 otherwise.
- Simultaneously, two new subsequences (`left_sequence` and `right_sequence`) are created, containing the symbols corresponding to the 0s and 1s, respectively.
- A new `WaveletTreeNode` is created with the current `alphabet` and the `bit_vector`.
- Recursively calls `_build_recursive` for the `left_sequence` and `right_sequence` to create the children of the current `node`.

    </li>

[Back to Implementation](#implementation)

## Applications

### Application

Wavelet Trees are powerful data structures for compressing sequences while supporting fast queries. They are used in:
- **Text Indexing and Search Engines:** For `rank` (count occurrences of a character up to a position) and `select` (find the position of the k-th occurrence of a character) queries on large texts.
- **Bioinformatics:** For analyzing DNA and protein sequences, where rank/select operations are fundamental for many alignment and search algorithms.
- **Data Compression:** The bit vectors at each level can be compressed, leading to a compact representation of the original sequence.
- **Computational Geometry:** For solving certain problems on point grids.

