---
title: "Huffman Coding Algorithm"
---

`Huffman Coding` is a lossless data compression algorithm. It is a greedy algorithm that achieves optimal prefix codes (a type of variable-length code where no codeword is a prefix of any other codeword). The idea is to assign shorter codes to characters that appear more frequently and longer codes to characters that appear less frequently.

The algorithm builds a binary tree, called a **Huffman tree** or **Huffman code tree**, where each leaf node represents a character and its frequency. The path from the root to a leaf defines the code for that character.

## How it Works

### How it Works (Expanded)

The `Huffman Coding` algorithm constructs a binary tree in a bottom-up manner, ensuring that the most frequent characters are closer to the root, resulting in shorter codes.

---

Example: Build Huffman Tree for text "AAAAABBCD"
Frequencies: A:5, B:2, C:1, D:1

1. Initial Nodes (sorted by frequency):
   C:1, D:1, B:2, A:5

2. Phase 1: Combine C and D (lowest frequencies)
- Create internal node CD with frequency 1+1=2.
- Assign C, D as children.
- Nodes: B:2, CD:2, A:5

3. Phase 2: Combine B and CD (lowest frequencies)
- Create internal node BCD with frequency 2+2=4.
- Assign B, CD as children.
- Nodes: A:5, BCD:4

4. Phase 3: Combine BCD and A
- Create internal node Root with frequency 4+5=9.
- Assign BCD, A as children.
- Nodes: Root:9

Huffman Tree (example codes):
       Root (9)
      /      \
   BCD (4)   A (5) (Code: 1)
  /    \
 B (2)  CD (2) (Code: 00)
       /  \
      C(1) D(1) (Code: 010) (Code: 011)

Resulting Codes:
A: 1
B: 00
C: 010
D: 011

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # For heapq to work as a min-priority queue based on frequency
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    if not text:
        return None, {}

    # 1. Calculate frequencies
    frequency = Counter(text)
    
    # 2. Create leaf nodes and add to priority queue
    priority_queue = []
    for char, freq in frequency.items():
        heapq.heappush(priority_queue, HuffmanNode(char, freq))
    
    # 3. Build tree
    while len(priority_queue) > 1:
        left_node = heapq.heappop(priority_queue)
        right_node = heapq.heappop(priority_queue)
        
        # Create new internal node
        merged_freq = left_node.freq + right_node.freq
        merged_node = HuffmanNode(None, merged_freq) # Internal node has no char
        merged_node.left = left_node
        merged_node.right = right_node
        
        heapq.heappush(priority_queue, merged_node)
        
    if not priority_queue: # Handle empty text case (if text only has unique chars, it could be len 1 pq after all, but general empty text)
        return None, {}

    huffman_root = heapq.heappop(priority_queue)
    
    # 4. Generate codes
    huffman_codes = {}
    
    def generate_codes_recursive(node, current_code):
        if node is None:
            return
        
        # If it's a leaf node, assign the code
        if node.char is not None:
            huffman_codes[node.char] = current_code
            return
        
        # Traverse left (0) and right (1)
        generate_codes_recursive(node.left, current_code + "0")
        generate_codes_recursive(node.right, current_code + "1")
    
    generate_codes_recursive(huffman_root, "")

    return huffman_root, huffman_codes

def huffman_encode(text, huffman_codes):
    if not text or not huffman_codes:
        return ""
    
    encoded_text = "".join(huffman_codes[char] for char in text)
    return encoded_text

def huffman_decode(encoded_text, huffman_root):
    if not encoded_text or huffman_root is None:
        return ""
    
    decoded_text = []
    current_node = huffman_root
    
    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        else: # bit == '1'
            current_node = current_node.right
        
        # If it's a leaf node, we found a character
        if current_node.char is not None:
            decoded_text.append(current_node.char)
            current_node = huffman_root # Reset to root for next character
            
    return "".join(decoded_text)

# Example
# text_to_compress = "AAAAABBCD"
# h_root, h_codes = build_huffman_tree(text_to_compress)
# print("Huffman Codes:", h_codes)
# # Expected: {'A': '1', 'B': '00', 'C': '010', 'D': '011'} (order and exact bit string might vary based on tie-breaking)

# encoded = huffman_encode(text_to_compress, h_codes)
# print("Encoded text:", encoded) # e.g., 111110000010011

# decoded = huffman_decode(encoded, h_root)
# print("Decoded text:", decoded) # Expected: AAAAABBCD
```

### Javascript

```javascript
class HuffmanNode {
    constructor(char, freq, left = null, right = null) {
        this.char = char;
        this.freq = freq;
        this.left = left;
        this.right = right;
    }
}

// Simple Priority Queue (min-heap) implementation for demonstration.
// For production, use a more efficient data structure or library.
class MinPriorityQueue {
    constructor() {
        this.heap = [];
    }

    push(item) {
        this.heap.push(item);
        this.heap.sort((a, b) => a.freq - b.freq); // Keep sorted
    }

    pop() {
        return this.heap.shift(); // Remove smallest
    }

    size() {
        return this.heap.length;
    }
}

function buildHuffmanTree(text) {
    if (!text) {
        return { root: null, codes: {} };
    }

    // 1. Calculate frequencies
    const frequency = {};
    for (const char of text) {
        frequency[char] = (frequency[char] || 0) + 1;
    }
    
    // 2. Create leaf nodes and add to priority queue
    const pq = new MinPriorityQueue();
    for (const char in frequency) {
        pq.push(new HuffmanNode(char, frequency[char]));
    }
    
    // Handle single character edge case
    if (pq.size() === 1) {
        const node = pq.pop();
        const root = new HuffmanNode(null, node.freq, node, null); // Create an artificial parent
        const codes = {};
        codes[node.char] = "0"; // Assign a code
        return { root, codes };
    }
    
    // 3. Build tree
    while (pq.size() > 1) {
        const leftNode = pq.pop();
        const rightNode = pq.pop();
        
        // Create new internal node
        const mergedFreq = leftNode.freq + rightNode.freq;
        const mergedNode = new HuffmanNode(null, mergedFreq, leftNode, rightNode);
        
        pq.push(mergedNode);
    }
    
    const huffmanRoot = pq.pop();
    
    // 4. Generate codes
    const huffmanCodes = {};
    
    function generateCodesRecursive(node, currentCode) {
        if (!node) {
            return;
        }
        
        // If it's a leaf node, assign the code
        if (node.char !== null) {
            huffmanCodes[node.char] = currentCode;
            return;
        }
        
        // Traverse left (0) and right (1)
        generateCodesRecursive(node.left, currentCode + "0");
        generateCodesRecursive(node.right, currentCode + "1");
    }
    
    generateCodesRecursive(huffmanRoot, "");

    return { root: huffmanRoot, codes: huffmanCodes };
}

function huffmanEncode(text, huffmanCodes) {
    if (!text || Object.keys(huffmanCodes).length === 0) {
        return "";
    }
    
    let encodedText = "";
    for (const char of text) {
        encodedText += huffmanCodes[char];
    }
    return encodedText;
}

function huffmanDecode(encodedText, huffmanRoot) {
    if (!encodedText || huffmanRoot === null) {
        return "";
    }
    
    let decodedText = [];
    let currentNode = huffmanRoot;
    
    for (const bit of encodedText) {
        if (bit === '0') {
            currentNode = currentNode.left;
        } else { // bit === '1'
            currentNode = currentNode.right;
        }
        
        // If it's a leaf node, we found a character
        if (currentNode.char !== null) {
            decodedText.push(currentNode.char);
            currentNode = huffmanRoot; // Reset to root for next character
        }
            
    }
    return decodedText.join("");
}

// const textToCompress = "AAAAABBCD";
// const { root, codes } = buildHuffmanTree(textToCompress);
// console.log("Huffman Codes:", codes);
// const encoded = huffmanEncode(textToCompress, codes);
// console.log("Encoded text:", encoded);
// const decoded = huffmanDecode(encoded, root);
// console.log("Decoded text:", decoded);
```

### Typescript

```typescript
class HuffmanNode {
    public char: string | null;
    public freq: number;
    public left: HuffmanNode | null;
    public right: HuffmanNode | null;

    constructor(char: string | null, freq: number, left: HuffmanNode | null = null, right: HuffmanNode | null = null) {
        this.char = char;
        this.freq = freq;
        this.left = left;
        this.right = right;
    }
}

// Minimal Priority Queue (min-heap) interface for demonstration.
// For production, use a more efficient custom min-heap or a library.
class MinPriorityQueue {
    private heap: HuffmanNode[] = [];

    push(item: HuffmanNode) {
        this.heap.push(item);
        this.heap.sort((a, b) => a.freq - b.freq); // Keep sorted
    }

    pop(): HuffmanNode | undefined {
        return this.heap.shift(); // Remove smallest
    }

    size(): number {
        return this.heap.length;
    }
}

function buildHuffmanTreeTS(text: string): { root: HuffmanNode | null; codes: { [key: string]: string } } {
    if (!text) {
        return { root: null, codes: {} };
    }

    // 1. Calculate frequencies
    const frequency: { [key: string]: number } = {};
    for (const char of text) {
        frequency[char] = (frequency[char] || 0) + 1;
    }
    
    // 2. Create leaf nodes and add to priority queue
    const pq = new MinPriorityQueue();
    for (const char in frequency) {
        pq.push(new HuffmanNode(char, frequency[char]));
    }
    
    // Handle single character edge case
    if (pq.size() === 1) {
        const node = pq.pop()!;
        const root = new HuffmanNode(null, node.freq, node, null); // Create an artificial parent
        const codes: { [key: string]: string } = {};
        codes[node.char!] = "0"; // Assign a code
        return { root, codes };
    }

    // 3. Build tree
    while (pq.size() > 1) {
        const leftNode = pq.pop()!;
        const rightNode = pq.pop()!;
        
        // Create new internal node
        const mergedFreq = leftNode.freq + rightNode.freq;
        const mergedNode = new HuffmanNode(null, mergedFreq, leftNode, rightNode);
        
        pq.push(mergedNode);
    }
    
    const huffmanRoot = pq.pop()!;
    
    // 4. Generate codes
    const huffmanCodes: { [key: string]: string } = {};
    
    function generateCodesRecursive(node: HuffmanNode | null, currentCode: string): void {
        if (!node) {
            return;
        }
        
        // If it's a leaf node, assign the code
        if (node.char !== null) {
            huffmanCodes[node.char] = currentCode;
            return;
        }
        
        // Traverse left (0) and right (1)
        generateCodesRecursive(node.left, currentCode + "0");
        generateCodesRecursive(node.right, currentCode + "1");
    }
    
    generateCodesRecursive(huffmanRoot, "");

    return { root: huffmanRoot, codes: huffmanCodes };
}

function huffmanEncodeTS(text: string, huffmanCodes: { [key: string]: string }): string {
    if (!text || Object.keys(huffmanCodes).length === 0) {
        return "";
    }
    
    let encodedText = "";
    for (const char of text) {
        encodedText += huffmanCodes[char];
    }
    return encodedText;
}

function huffmanDecodeTS(encodedText: string, huffmanRoot: HuffmanNode | null): string {
    if (!encodedText || huffmanRoot === null) {
        return "";
    }
    
    let decodedText: string[] = [];
    let currentNode: HuffmanNode = huffmanRoot;
    
    for (const bit of encodedText) {
        if (bit === '0') {
            currentNode = currentNode.left!;
        } else { // bit === '1'
            currentNode = currentNode.right!;
        }
        
        // If it's a leaf node, we found a character
        if (currentNode.char !== null) {
            decodedText.push(currentNode.char);
            currentNode = huffmanRoot; // Reset to root for next character
        }
            
    }
    return decodedText.join("");
}

// const textToCompressTS = "AAAAABBCD";
// const { root: h_root_ts, codes: h_codes_ts } = buildHuffmanTreeTS(textToCompressTS);
// console.log("Huffman Codes:", h_codes_ts);
// const encodedTS = huffmanEncodeTS(textToCompressTS, h_codes_ts);
// console.log("Encoded text:", encodedTS);
// const decodedTS = huffmanDecodeTS(encodedTS, h_root_ts);
// console.log("Decoded text:", decodedTS);
```

### Cpp

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <queue> // For std::priority_queue
#include <map>
#include <algorithm> // For std::reverse
#include <functional> // For std::function

// Huffman Node structure
struct HuffmanNode {
    char data;
    int freq;
    HuffmanNode <em>left, </em>right;

    HuffmanNode(char data, int freq) : data(data), freq(freq), left(nullptr), right(nullptr) {}

    // Destructor to free memory
    ~HuffmanNode() {
        delete left;
        delete right;
    }
};

// Custom comparator for min-priority queue (based on frequency)
struct CompareNodes {
    bool operator()(HuffmanNode<em> a, HuffmanNode</em> b) {
        return a->freq > b->freq;
    }
};

// Function to build Huffman Tree and generate codes
std::pair<HuffmanNode<em>, std::map<char, std::string>> buildHuffmanTree(const std::string& text) {
    if (text.empty()) {
        return {nullptr, {}};
    }

    // 1. Calculate frequencies
    std::map<char, int> frequency;
    for (char ch : text) {
        frequency[ch]++;
    }

    // 2. Create leaf nodes and add to priority queue
    std::priority_queue<HuffmanNode</em>, std::vector<HuffmanNode<em>>, CompareNodes> pq;
    for (auto const& [key, val] : frequency) {
        pq.push(new HuffmanNode(key, val));
    }
    
    // Handle single character edge case
    if (pq.size() == 1) {
        HuffmanNode</em> node = pq.top();
        pq.pop();
        HuffmanNode<em> root = new HuffmanNode('\0', node->freq); // Artificial parent for single char
        root->left = node; // Assign as left child
        
        std::map<char, std::string> codes;
        codes[node->data] = "0"; // Assign code "0"
        return {root, codes};
    }

    // 3. Build tree
    while (pq.size() > 1) {
        HuffmanNode </em>left = pq.top(); pq.pop();
        HuffmanNode <em>right = pq.top(); pq.pop();

        HuffmanNode </em>top = new HuffmanNode('\0', left->freq + right->freq);
        top->left = left;
        top->right = right;
        pq.push(top);
    }

    HuffmanNode <em>huffmanRoot = pq.top();
    
    // 4. Generate codes
    std::map<char, std::string> huffmanCodes;
    
    std::function<void(HuffmanNode</em>, std::string)> generateCodesRecursive = 
        [&](HuffmanNode<em> node, std::string current_code) {
        if (!node) {
            return;
        }
        
        // If it's a leaf node, assign the code
        if (node->data != '\0') { // Internal nodes have '\0' data
            huffmanCodes[node->data] = current_code;
            return;
        }
        
        // Traverse left (0) and right (1)
        generateCodesRecursive(node->left, current_code + "0");
        generateCodesRecursive(node->right, current_code + "1");
    };
    
    generateCodesRecursive(huffmanRoot, "");

    return {huffmanRoot, huffmanCodes};
}

// Function to encode text using Huffman codes
std::string huffmanEncode(const std::string& text, const std::map<char, std::string>& huffman_codes) {
    if (text.empty() || huffman_codes.empty()) {
        return "";
    }
    std::string encoded_text = "";
    for (char ch : text) {
        encoded_text += huffman_codes.at(ch);
    }
    return encoded_text;
}

// Function to decode encoded text
std::string huffmanDecode(const std::string& encoded_text, HuffmanNode</em> huffman_root) {
    if (encoded_text.empty() || huffman_root == nullptr) {
        return "";
    }
    std::string decoded_text = "";
    HuffmanNode<em> current_node = huffman_root;
    
    for (char bit : encoded_text) {
        if (bit == '0') {
            current_node = current_node->left;
        } else { // bit == '1'
            current_node = current_node->right;
        }
        
        // If it's a leaf node, we found a character
        if (current_node->data != '\0') {
            decoded_text += current_node->data;
            current_node = huffman_root; // Reset to root for next character
        }
            
    }
    return decoded_text;
}

// int main() {
//     std::string text_to_compress = "AAAAABBCD";
//     auto result = buildHuffmanTree(text_to_compress);
//     HuffmanNode</em> h_root = result.first;
//     std::map<char, std::string> h_codes = result.second;

//     std::cout << "Huffman Codes:" << std::endl;
//     for (auto const& [key, val] : h_codes) {
//         std::cout << key << ": " << val << std::endl;
//     }
//     // Expected: A:1, B:00, C:010, D:011 (order and exact bit string might vary)

//     std::string encoded = huffmanEncode(text_to_compress, h_codes);
//     std::cout << "Encoded text: " << encoded << std::endl; // e.g., 111110000010011

//     std::string decoded = huffmanDecode(encoded, h_root);
//     std::cout << "Decoded text: " << decoded << std::endl; // AAAAABBCD

//     delete h_root; // Free memory
//     return 0;
// }
```

### Go

```go
package main

import (
    "container/heap"
    "fmt"
    "strings"
)

// HuffmanNode structure
type HuffmanNode struct {
    Char  rune
    Freq  int
    Left  <em>HuffmanNode
    Right </em>HuffmanNode
}

// IsLeaf checks if the node is a leaf node
func (node <em>HuffmanNode) IsLeaf() bool {
    return node.Left == nil && node.Right == nil
}

// A PriorityQueue implements heap.Interface for HuffmanNode pointers
type HuffmanPriorityQueue []</em>HuffmanNode

func (pq HuffmanPriorityQueue) Len() int { return len(pq) }

func (pq HuffmanPriorityQueue) Less(i, j int) bool {
    return pq[i].Freq < pq[j].Freq
}

func (pq HuffmanPriorityQueue) Swap(i, j int) {
    pq[i], pq[j] = pq[j], pq[i]
}

func (pq <em>HuffmanPriorityQueue) Push(x interface{}) {
    item := x.(</em>HuffmanNode)
    <em>pq = append(</em>pq, item)
}

func (pq <em>HuffmanPriorityQueue) Pop() interface{} {
    old := </em>pq
    n := len(old)
    item := old[n-1]
    <em>pq = old[0 : n-1]
    return item
}

// buildHuffmanTree builds the Huffman tree and generates codes
func buildHuffmanTree(text string) (</em>HuffmanNode, map[rune]string) {
    if len(text) == 0 {
        return nil, make(map[rune]string)
    }

    // 1. Calculate frequencies
    frequency := make(map[rune]int)
    for _, char := range text {
        frequency[char]++
    }

    // 2. Create leaf nodes and add to priority queue
    pq := make(HuffmanPriorityQueue, 0)
    for char, freq := range frequency {
        heap.Push(&pq, &HuffmanNode{Char: char, Freq: freq})
    }
    
    // Handle single character edge case
    if pq.Len() == 1 {
        node := heap.Pop(&pq).(<em>HuffmanNode)
        root := &HuffmanNode{Char: '\000', Freq: node.Freq, Left: node, Right: nil} // Artificial parent
        codes := make(map[rune]string)
        codes[node.Char] = "0" // Assign a code
        return root, codes
    }

    // 3. Build tree
    for pq.Len() > 1 {
        leftNode := heap.Pop(&pq).(</em>HuffmanNode)
        rightNode := heap.Pop(&pq).(<em>HuffmanNode)

        mergedFreq := leftNode.Freq + rightNode.Freq
        mergedNode := &HuffmanNode{Char: '\000', Freq: mergedFreq, Left: leftNode, Right: rightNode}
        heap.Push(&pq, mergedNode)
    }

    huffmanRoot := heap.Pop(&pq).(</em>HuffmanNode)

    // 4. Generate codes
    huffmanCodes := make(map[rune]string)
    
    var generateCodesRecursive func(node <em>HuffmanNode, currentCode string)
    generateCodesRecursive = func(node </em>HuffmanNode, currentCode string) {
        if node == nil {
            return
        }
        
        // If it's a leaf node, assign the code
        if node.IsLeaf() {
            huffmanCodes[node.Char] = currentCode
            return
        }
        
        // Traverse left (0) and right (1)
        generateCodesRecursive(node.Left, currentCode + "0")
        generateCodesRecursive(node.Right, currentCode + "1")
    }
    
    generateCodesRecursive(huffmanRoot, "")

    return huffmanRoot, huffmanCodes
}

// huffmanEncode encodes the text using the generated Huffman codes
func huffmanEncode(text string, huffmanCodes map[rune]string) string {
    if len(text) == 0 || len(huffmanCodes) == 0 {
        return ""
    }
    
    var encodedText strings.Builder
    for _, char := range text {
        encodedText.WriteString(huffmanCodes[char])
    }
    return encodedText.String()
}

// huffmanDecode decodes the encoded text using the Huffman tree
func huffmanDecode(encodedText string, huffmanRoot *HuffmanNode) string {
    if len(encodedText) == 0 || huffmanRoot == nil {
        return ""
    }
    
    var decodedText strings.Builder
    currentNode := huffmanRoot
    
    for _, bit := range encodedText {
        if bit == '0' {
            currentNode = currentNode.Left
        } else { // bit == '1'
            currentNode = currentNode.Right
        }
        
        // If it's a leaf node, we found a character
        if currentNode.IsLeaf() {
            decodedText.WriteRune(currentNode.Char)
            currentNode = huffmanRoot // Reset to root for next character
        }
            
    }
    return decodedText.String()
}

// func main() {
//     textToCompress := "AAAAABBCD"
//     hRoot, hCodes := buildHuffmanTree(textToCompress)
//     fmt.Println("Huffman Codes:", hCodes)
//     // Example: map[A:1 B:00 C:010 D:011]
//     // (order and exact bit string might vary based on tie-breaking)

//     encoded := huffmanEncode(textToCompress, hCodes)
//     fmt.Println("Encoded text:", encoded) // e.g., 111110000010011

//     decoded := huffmanDecode(encoded, hRoot)
//     fmt.Println("Decoded text:", decoded) // AAAAABBCD
// }
```

### D

```d
import std.stdio;
import std.array;
import std.algorithm; // For std.algorithm.sort, min, max
import std.container.binaryheap; // For BinaryHeap
import std.sum;
import std.string; // For strip, join
import std.traits; // For isIntegral
import std.conv;

// Huffman Node structure
class HuffmanNode {
    char data;
    int freq;
    HuffmanNode left, right;

    this(char data, int freq, HuffmanNode left = null, HuffmanNode right = null) {
        this.data = data;
        this.freq = freq;
        this.left = left;
        this.right = right;
    }

    bool isLeaf() {
        return left is null && right is null;
    }

    // Custom comparison for BinaryHeap (min-priority queue based on frequency)
    int opCmp(const HuffmanNode other) const {
        return this.freq.cmp(other.freq);
    }
}

// buildHuffmanTree builds the Huffman tree and generates codes
Tuple!(HuffmanNode, int[char]) buildHuffmanTree(string text) {
    if (text.empty) {
        return typeof(return)(null, null);
    }

    // 1. Calculate frequencies
    int[char] frequency;
    foreach (ch; text) {
        frequency[ch]++;
    }

    // 2. Create leaf nodes and add to priority queue
    auto pq = new BinaryHeap!(HuffmanNode)();
    foreach (char, freq; frequency) {
        pq.insert(new HuffmanNode(char, freq));
    }
    
    // Handle single character edge case
    if (pq.length == 1) {
        auto node = pq.front;
        pq.removeFront();
        auto root = new HuffmanNode('\0', node.freq, node, null); // Artificial parent
        int[char] codes;
        codes[node.data] = "0"; // Assign a code
        return typeof(return)(root, codes);
    }

    // 3. Build tree
    while (pq.length > 1) {
        auto left = pq.front; pq.removeFront();
        auto right = pq.front; pq.removeFront();

        auto top = new HuffmanNode('\0', left.freq + right.freq, left, right);
        pq.insert(top);
    }

    auto huffmanRoot = pq.front;
    
    // 4. Generate codes
    int[char] huffmanCodes;
    
    void generateCodesRecursive(HuffmanNode node, string currentCode) {
        if (node is null) {
            return;
        }
        
        // If it's a leaf node, assign the code
        if (node.isLeaf()) {
            huffmanCodes[node.data] = currentCode;
            return;
        }
        
        // Traverse left (0) and right (1)
        generateCodesRecursive(node.left, currentCode ~ "0");
        generateCodesRecursive(node.right, currentCode ~ "1");
    }
    
    generateCodesRecursive(huffmanRoot, "");

    return typeof(return)(huffmanRoot, huffmanCodes);
}

// huffmanEncode encodes the text using the generated Huffman codes
string huffmanEncode(string text, int[char] huffmanCodes) {
    if (text.empty || huffmanCodes.empty) {
        return "";
    }
    
    string encodedText = "";
    foreach (ch; text) {
        encodedText ~= huffmanCodes[ch];
    }
    return encodedText;
}

// huffmanDecode decodes the encoded text using the Huffman tree
string huffmanDecode(string encodedText, HuffmanNode huffmanRoot) {
    if (encodedText.empty || huffmanRoot is null) {
        return "";
    }
    
    string decodedText = "";
    HuffmanNode currentNode = huffmanRoot;
    
    foreach (bit; encodedText) {
        if (bit == '0') {
            currentNode = currentNode.left;
        } else { // bit == '1'
            currentNode = currentNode.right;
        }
        
        // If it's a leaf node, we found a character
        if (currentNode.isLeaf()) {
            decodedText ~= currentNode.data;
            currentNode = huffmanRoot; // Reset to root for next character
        }
            
    }
    return decodedText;
}

// void main() {
//     string textToCompress = "AAAAABBCD";
//     auto result = buildHuffmanTree(textToCompress);
//     HuffmanNode hRoot = result._0;
//     int[char] hCodes = result._1;

//     writeln("Huffman Codes:");
//     foreach (key, val; hCodes) {
//         writefln("%s: %s", key, val);
//     }
//     // Expected: A:1, B:00, C:010, D:011 (order and exact bit string might vary)

//     string encoded = huffmanEncode(textToCompress, hCodes);
//     writeln("Encoded text: ", encoded); // e.g., 111110000010011

//     string decoded = huffmanDecode(encoded, hRoot);
//     writeln("Decoded text: ", decoded); // AAAAABBCD
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

`Huffman Coding` is a two-step process: building the Huffman tree and then using the tree to generate codes and encode/decode text.

---

**`HuffmanNode` Class:**
- `char`: The character (if it's a leaf node), or `None`/`\0` if it's an internal node.
- `freq`: The frequency of the character or the sum of frequencies of its children.
- `left`, `right`: Pointers to child `HuffmanNode`s.

**`buildHuffmanTree(text)` Function:**
- **Calculate Frequencies:** Counts the occurrences of each character in the input `text`.
- **Create Leaf Nodes and Priority Queue:** Each unique character becomes a `HuffmanNode` (a leaf node). These `nodes` are pushed into a `min-priority queue`, ordered by their `frequency`.
- **Build Tree:** While there is more than one `node` in the `priority queue`:
- Two `nodes` with the lowest `frequencies` are extracted.
- A new internal `HuffmanNode` is created. Its `frequency` is the sum of the two extracted `nodes`' `frequencies`. The two extracted `nodes` become its `left` and `right children`.
- This new internal `node` is pushed back into the `priority queue`.

    </li>
- The final `node` remaining in the `priority queue` is the `root` of the `Huffman tree`.
- **Generate Codes:** A recursive helper function `generate_codes_recursive` traverses the `Huffman tree`.
- If it reaches a leaf `node`, the `current_code` accumulated along the path is assigned to the `node`'s character.
- If it's an internal `node`, it recursively calls itself for the `left child` (appending '0' to `current_code`) and the `right child` (appending '1').

    </li>

**`huffman_encode(text, huffman_codes)` Function:**
- Takes the original `text` and the `huffman_codes` map.
- Iterates through the `text`, appending the `Huffman code` for each character to build the `encoded_text`.

**`huffman_decode(encoded_text, huffman_root)` Function:**
- Takes the `encoded_text` and the `huffman_root` (the Huffman tree).
- Starts at the `root` of the `Huffman tree`. For each bit in `encoded_text`:
- If the bit is '0', traverse to the `left child`.
- If the bit is '1', traverse to the `right child`.
- When a leaf `node` is reached, append its `character` to the `decoded_text` and reset `current_node` back to the `huffman_root` to start decoding the next character.

    </li>

[Back to Implementation](#implementation)

## Applications

### Application

`Huffman Coding` is a widely used algorithm for lossless data compression, which means no information is lost during compression. Its applications are extensive:
- **File Compression:** Used in various file formats like JPEG (for chrominance data), MP3, and many general-purpose compression tools (e.g., PKZIP, GZIP).
- **Fax Machines:** Early fax machines used Huffman coding to compress images.
- **Text and Document Archiving:** Efficiently storing large text files or documents.
- **Network Communication:** Reducing the amount of data transmitted over networks, improving bandwidth utilization.
- **Databases:** Compressing fields with highly skewed data distributions.
- **Embedded Systems:** In systems with limited memory and processing power, where efficient compression and decompression are crucial.

