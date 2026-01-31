---
title: "Skew Heap"
---

A `Skew Heap` is a self-adjusting (or self-modifying) `heap` data structure, similar to a `Leftist Heap`, that provides efficient `merge (meld)` operations. It guarantees `O(log N)` amortized time complexity for all major operations: `insertion`, `extract-min`, and `merge`.

Unlike `Leftist Heaps`, `Skew Heaps` do not maintain any explicit balance information (like `null path length` or `ranks`). Instead, they perform a simple, unconditional `swap` of `left` and `right children` after each recursive `merge` call, which implicitly keeps the `heap` balanced over a sequence of operations.

## How it Works

### How it Works (Expanded)

A `Skew Heap` is a `binary tree` that satisfies the `heap property` (e.g., `min-heap`: parent's `key` <= children's `keys`). Its self-adjusting nature comes from a simple rule applied during its fundamental `merge` operation:

---

Conceptual Skew Heap:

          (Key=10)
         /      \
    (Key=20) (Key=30)
   /      \      \
(Key=40) (Key=50) (Key=60)

Merging two heaps (H1 and H2):
- Always ensure H1.key <= H2.key.
- Recursively merge H1.right with H2.
- Then, unconditionally swap H1.left and H1.right.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
class SkewNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class SkewHeap:
    def __init__(self):
        self.root = None

    def _merge_recursive(self, h1, h2):
        if not h1:
            return h2
        if not h2:
            return h1
        
        # Ensure h1.key <= h2.key (min-heap property)
        if h1.key > h2.key:
            h1, h2 = h2, h1
        
        # Merge h1's right child with h2
        h1.right = self._merge_recursive(h1.right, h2)
        
        # Unconditionally swap h1's left and right children
        h1.left, h1.right = h1.right, h1.left
        
        return h1

    def insert(self, key):
        new_node = SkewNode(key)
        self.root = self._merge_recursive(self.root, new_node)

    def extract_min(self):
        if not self.root:
            return None
        
        min_key = self.root.key
        self.root = self._merge_recursive(self.root.left, self.root.right)
        return min_key

    def find_min(self):
        return self.root.key if self.root else None

    def merge(self, other_heap):
        self.root = self._merge_recursive(self.root, other_heap.root)
        other_heap.root = None # Other heap is now empty

# Example Usage:
# heap1 = SkewHeap()
# heap1.insert(10)
# heap1.insert(30)
# heap1.insert(5)
# print("Heap1 min:", heap1.find_min()) # Expected: 5

# heap2 = SkewHeap()
# heap2.insert(20)
# heap2.insert(2)
# print("Heap2 min:", heap2.find_min()) # Expected: 2

# heap1.merge(heap2)
# print("Merged heap min:", heap1.find_min()) # Expected: 2
# print("Extract min:", heap1.extract_min()) # Expected: 2
# print("Merged heap min after extract:", heap1.find_min()) # Expected: 5
```

### Javascript

```javascript
class SkewNode {
    constructor(key) {
        this.key = key;
        this.left = null;
        this.right = null;
    }
}

class SkewHeap {
    constructor() {
        this.root = null;
    }

    _mergeRecursive(h1, h2) {
        if (!h1) return h2;
        if (!h2) return h1;
        
        // Ensure h1.key <= h2.key (min-heap property)
        if (h1.key > h2.key) {
            [h1, h2] = [h2, h1]; // Swap h1 and h2
        }
        
        // Merge h1's right child with h2
        h1.right = this._mergeRecursive(h1.right, h2);
        
        // Unconditionally swap h1's left and right children
        [h1.left, h1.right] = [h1.right, h1.left]; // Swap children
        
        return h1;
    }

    insert(key) {
        const newNode = new SkewNode(key);
        this.root = this._mergeRecursive(this.root, newNode);
    }

    extractMin() {
        if (!this.root) {
            return null;
        }
        
        const minKey = this.root.key;
        this.root = this._mergeRecursive(this.root.left, this.root.right);
        return minKey;
    }

    findMin() {
        return this.root ? this.root.key : null;
    }

    merge(otherHeap) {
        this.root = this._mergeRecursive(this.root, otherHeap.root);
        otherHeap.root = null; // Other heap is now empty
    }
}

// const heap1 = new SkewHeap();
// heap1.insert(10);
// heap1.insert(30);
// heap1.insert(5);
// console.log("Heap1 min:", heap1.findMin()); // Expected: 5

// const heap2 = new SkewHeap();
// heap2.insert(20);
// heap2.insert(2);
// console.log("Heap2 min:", heap2.findMin()); // Expected: 2

// heap1.merge(heap2);
// console.log("Merged heap min:", heap1.findMin()); // Expected: 2
// console.log("Extract min:", heap1.extractMin()); // Expected: 2
// console.log("Merged heap min after extract:", heap1.findMin()); // Expected: 5
```

### Typescript

```typescript
class SkewNodeTS {
    public key: number;
    public left: SkewNodeTS | null;
    public right: SkewNodeTS | null;

    constructor(key: number) {
        this.key = key;
        this.left = null;
        this.right = null;
    }
}

class SkewHeapTS {
    public root: SkewNodeTS | null = null;

    private _mergeRecursive(h1: SkewNodeTS | null, h2: SkewNodeTS | null): SkewNodeTS | null {
        if (!h1) return h2;
        if (!h2) return h1;
        
        // Ensure h1.key <= h2.key (min-heap property)
        if (h1.key > h2.key) {
            [h1, h2] = [h2, h1]; // Swap h1 and h2
        }
        
        // Merge h1's right child with h2
        h1.right = this._mergeRecursive(h1.right, h2);
        
        // Unconditionally swap h1's left and right children
        [h1.left, h1.right] = [h1.right, h1.left]; // Swap children
        
        return h1;
    }

    public insert(key: number): void {
        const newNode = new SkewNodeTS(key);
        this.root = this._mergeRecursive(this.root, newNode);
    }

    public extractMin(): number | null {
        if (!this.root) {
            return null;
        }
        
        const minKey = this.root.key;
        this.root = this._mergeRecursive(this.root.left, this.root.right);
        return minKey;
    }

    public findMin(): number | null {
        return this.root ? this.root.key : null;
    }

    public merge(otherHeap: SkewHeapTS): void {
        this.root = this._mergeRecursive(this.root, otherHeap.root);
        otherHeap.root = null; // Other heap is now empty
    }
}

// const heap1TS = new SkewHeapTS();
// heap1TS.insert(10);
// heap1TS.insert(30);
// heap1TS.insert(5);
// console.log("Heap1 min:", heap1TS.findMin()); // Expected: 5

// const heap2TS = new SkewHeapTS();
// heap2TS.insert(20);
// heap2TS.insert(2);
// console.log("Heap2 min:", heap2TS.findMin()); // Expected: 2

// heap1TS.merge(heap2TS);
// console.log("Merged heap min:", heap1TS.findMin()); // Expected: 2
// console.log("Extract min:", heap1TS.extractMin()); // Expected: 2
// console.log("Merged heap min after extract:", heap1TS.findMin()); // Expected: 5
```

### Cpp

```cpp
#include <iostream>
#include <algorithm> // For std::swap

class SkewNode {
public:
    int key;
    SkewNode <em>left;
    SkewNode </em>right;

    SkewNode(int k) : key(k), left(nullptr), right(nullptr) {}
};

class SkewHeap {
public:
    SkewNode<em> root;

    SkewHeap() : root(nullptr) {}

    // Main merge function
    SkewNode</em> mergeRecursive(SkewNode<em> h1, SkewNode</em> h2) {
        if (!h1) return h2;
        if (!h2) return h1;

        // Ensure h1.key <= h2.key (min-heap property)
        if (h1->key > h2->key) {
            std::swap(h1, h2);
        }

        // Merge h1's right child with h2
        h1->right = mergeRecursive(h1->right, h2);

        // Unconditionally swap h1's left and right children
        std::swap(h1->left, h1->right);
        
        return h1;
    }

    void insert(int key) {
        SkewNode<em> newNode = new SkewNode(key);
        root = mergeRecursive(root, newNode);
    }

    int extractMin() {
        if (!root) {
            // Handle error or return a sentinel value
            return -1; // Or throw an exception
        }
        
        int minKey = root->key;
        SkewNode</em> oldRoot = root;
        root = mergeRecursive(root->left, root->right);
        delete oldRoot; // Free the old root node
        return minKey;
    }

    int findMin() {
        return root ? root->key : -1; // Or throw an exception
    }

    void merge(SkewHeap& other_heap) {
        root = mergeRecursive(root, other_heap.root);
        other_heap.root = nullptr; // Other heap is now empty
    }
};

// int main() {
//     SkewHeap heap1;
//     heap1.insert(10);
//     heap1.insert(30);
//     heap1.insert(5);
//     std::cout << "Heap1 min: " << heap1.findMin() << std::endl; // Expected: 5

//     SkewHeap heap2;
//     heap2.insert(20);
//     heap2.insert(2);
//     std::cout << "Heap2 min: " << heap2.findMin() << std::endl; // Expected: 2

//     heap1.merge(heap2);
//     std::cout << "Merged heap min: " << heap1.findMin() << std::endl; // Expected: 2
//     std::cout << "Extract min: " << heap1.extractMin() << std::endl; // Expected: 2
//     std::cout << "Merged heap min after extract: " << heap1.findMin() << std::endl; // Expected: 5
//     return 0;
// }
```

### Go

```go
package main

import (
    "fmt"
)

type SkewNode struct {
    Key   int
    Left  <em>SkewNode
    Right </em>SkewNode
}

func NewSkewNode(key int) <em>SkewNode {
    return &SkewNode{Key: key}
}

type SkewHeap struct {
    Root </em>SkewNode
}

func (sh <em>SkewHeap) mergeRecursive(h1, h2 </em>SkewNode) <em>SkewNode {
    if h1 == nil {
        return h2
    }
    if h2 == nil {
        return h1
    }

    // Ensure h1.Key <= h2.Key (min-heap property)
    if h1.Key > h2.Key {
        h1, h2 = h2, h1 // Swap h1 and h2
    }

    // Merge h1's right child with h2
    h1.Right = sh.mergeRecursive(h1.Right, h2)

    // Unconditionally swap h1's left and right children
    h1.Left, h1.Right = h1.Right, h1.Left // Swap children

    return h1
}

func (sh </em>SkewHeap) Insert(key int) {
    newNode := NewSkewNode(key)
    sh.Root = sh.mergeRecursive(sh.Root, newNode)
}

func (sh <em>SkewHeap) ExtractMin() (int, error) {
    if sh.Root == nil {
        return 0, fmt.Errorf("heap is empty")
    }

    minKey := sh.Root.Key
    sh.Root = sh.mergeRecursive(sh.Root.Left, sh.Root.Right)
    return minKey, nil
}

func (sh </em>SkewHeap) FindMin() (int, error) {
    if sh.Root == nil {
        return 0, fmt.Errorf("heap is empty")
    }
    return sh.Root.Key, nil
}

func (sh <em>SkewHeap) Merge(otherHeap </em>SkewHeap) {
    sh.Root = sh.mergeRecursive(sh.Root, otherHeap.Root)
    otherHeap.Root = nil // Other heap is now empty
}

// func main() {
//     heap1 := &SkewHeap{}
//     heap1.Insert(10)
//     heap1.Insert(30)
//     heap1.Insert(5)
//     min1, _ := heap1.FindMin()
//     fmt.Println("Heap1 min:", min1) // Expected: 5

//     heap2 := &SkewHeap{}
//     heap2.Insert(20)
//     heap2.Insert(2)
//     min2, _ := heap2.FindMin()
//     fmt.Println("Heap2 min:", min2) // Expected: 2

//     heap1.Merge(heap2)
//     mergedMin, _ := heap1.FindMin()
//     fmt.Println("Merged heap min:", mergedMin) // Expected: 2
//     extractedMin, _ := heap1.ExtractMin()
//     fmt.Println("Extract min:", extractedMin) // Expected: 2
//     mergedMinAfterExtract, _ := heap1.FindMin()
//     fmt.Println("Merged heap min after extract:", mergedMinAfterExtract) // Expected: 5
// }
```

### D

```d
import std.stdio;
import std.algorithm;
import std.conv;

class SkewNode {
    int key;
    SkewNode left;
    SkewNode right;

    this(int k) {
        key = k;
        left = null;
        right = null;
    }
}

class SkewHeap {
    SkewNode root;

    this() {
        root = null;
    }

private:
    SkewNode mergeRecursive(SkewNode h1, SkewNode h2) {
        if (h1 is null) return h2;
        if (h2 is null) return h1;
        
        // Ensure h1.key <= h2.key (min-heap property)
        if (h1.key > h2.key) {
            swap(h1, h2);
        }
        
        // Merge h1's right child with h2
        h1.right = mergeRecursive(h1.right, h2);
        
        // Unconditionally swap h1's left and right children
        swap(h1.left, h1.right);
        
        return h1;
    }

public:
    void insert(int key) {
        SkewNode new_node = new SkewNode(key);
        root = mergeRecursive(root, new_node);
    }

    int extractMin() {
        if (root is null) {
            throw new Exception("Heap is empty");
        }
        
        int min_key = root.key;
        SkewNode old_root = root;
        root = mergeRecursive(root.left, root.right);
        // In D, old_root will be garbage collected if no other references.
        return min_key;
    }

    int findMin() {
        if (root is null) {
            throw new Exception("Heap is empty");
        }
        return root.key;
    }

    void merge(SkewHeap other_heap) {
        root = mergeRecursive(root, other_heap.root);
        other_heap.root = null; // Other heap is now empty
    }
}

// void main() {
//     auto heap1 = new SkewHeap();
//     heap1.insert(10);
//     heap1.insert(30);
//     heap1.insert(5);
//     writefln("Heap1 min: %s", heap1.findMin()); // Expected: 5

//     auto heap2 = new SkewHeap();
//     heap2.insert(20);
//     heap2.insert(2);
//     writefln("Heap2 min: %s", heap2.findMin()); // Expected: 2

//     heap1.merge(heap2);
//     writefln("Merged heap min: %s", heap1.findMin()); // Expected: 2
//     writefln("Extract min: %s", heap1.extractMin()); // Expected: 2
//     writefln("Merged heap min after extract: %s", heap1.findMin()); // Expected: 5
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

A `Skew Heap` implementation is remarkably simple due to its core `merge` operation, which implicitly balances the `heap` without explicit balance factors.

---

**`SkewNode` Class:**
- `key`: The value stored in the `node`.
- `left`, `right`: Pointers to child `nodes`.

**`SkewHeap` Class:**
- `root`: The `root node` of the `Skew Heap`.
- **`_merge_recursive(h1, h2)`:** This is the fundamental operation for merging two `Skew Heaps`.
- Handles base cases where one or both heaps are empty.
- Ensures the `min-heap property`: the `heap` with the smaller `root key` becomes `h1`.
- Recursively merges the `right child` of `h1` with `h2`.
- Crucially, after the recursive `merge` returns, it unconditionally `swaps` `h1`'s `left` and `right children`. This is the self-adjusting mechanism that provides amortized logarithmic time.
- Returns `h1` as the `root` of the new merged `heap`.

    </li>
- **`insert(key)`:** Creates a new `Skew Heap` containing only the new `key` and `merges` it with the existing `heap`.
- **`extract_min()`:** Retrieves the `minimum key` (from the `root`), then `merges` the `root`'s `left` and `right children` to form the new `heap`.
- **`find_min()`:** Returns the `key` of the `root node`.
- **`merge(other_heap)`:** Merges the current `heap` with `other_heap` by calling the recursive `_merge_recursive` function.

[Back to Implementation](#implementation)

## Applications

### Application

Skew Heaps are mergeable heaps, offering efficient merge operations crucial in certain algorithms and data processing scenarios. Their primary applications are similar to those of Leftist Heaps, but with an even simpler implementation.
- **Event Simulation:** Managing events from multiple sources that need to be prioritized and frequently combined.
- **Graph Algorithms:** In implementations of `Dijkstra's algorithm` or `Prim's algorithm`, particularly when an adjacency list representation is used and heap merging is performed to update priorities of neighboring vertices.
- **Network Routers:** For managing packet queues where packets from different incoming links might need to be merged and prioritized.
- **Parallel and Distributed Computing:** Efficiently combining priority queues from different threads or processes.
- **Anywhere mergeable `priority queues` are needed:** Where efficiency of merging is a primary concern, and the strict balance of other heaps (like Fibonacci) is not required.

