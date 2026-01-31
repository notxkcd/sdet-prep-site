---
title: "Leftist Heap"
---



## How it Works

### How it Works (Expanded)

A `Leftist Heap` is a `binary tree` that satisfies two main properties:
- **`Heap Property`:** The `key` of each `node` is less than or equal to the `keys` of its children (for a `min-heap`).
- **`Leftist Property`:** For every `node X`, the `null path length (npl)` of its `left child` is greater than or equal to the `null path length` of its `right child`. The `npl` of a `node` is the length of the shortest path from that `node` to a `node` that has less than two children (i.e., a `leaf` or a `node` with only one child). An empty `node` has an `npl` of `-1`, a `leaf node` has an `npl` of `0`.

---

Conceptual Leftist Heap: (npl values shown)

          (Key=10, npl=2)
         /             \
    (Key=20, npl=1) (Key=30, npl=0)
   /      \           /
(Key=40, npl=0) (Key=50, npl=0) (Key=60, npl=-1)

## Implementation {#implementation}

### Python

```python
class LeftistNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.npl = 0 # Null Path Length

class LeftistHeap:
    def __init__(self):
        self.root = None

    def _npl(self, node):
        return node.npl if node else -1

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
        
        # Restore leftist property: ensure npl(left) >= npl(right)
        if self._npl(h1.left) < self._npl(h1.right):
            h1.left, h1.right = h1.right, h1.left
        
        # Update npl of h1
        h1.npl = self._npl(h1.right) + 1
        
        return h1

    def insert(self, key):
        new_node = LeftistNode(key)
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
# heap1 = LeftistHeap()
# heap1.insert(10)
# heap1.insert(30)
# heap1.insert(5)
# print("Heap1 min:", heap1.find_min()) # Expected: 5

# heap2 = LeftistHeap()
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
class LeftistNode {
    constructor(key) {
        this.key = key;
        this.left = null;
        this.right = null;
        this.npl = 0; // Null Path Length
    }
}

class LeftistHeap {
    constructor() {
        this.root = null;
    }

    _npl(node) {
        return node ? node.npl : -1;
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
        
        // Restore leftist property: ensure npl(left) >= npl(right)
        if (this._npl(h1.left) < this._npl(h1.right)) {
            [h1.left, h1.right] = [h1.right, h1.left]; // Swap children
        }
        
        // Update npl of h1
        h1.npl = this._npl(h1.right) + 1;
        
        return h1;
    }

    insert(key) {
        const newNode = new LeftistNode(key);
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

// const heap1 = new LeftistHeap();
// heap1.insert(10);
// heap1.insert(30);
// heap1.insert(5);
// console.log("Heap1 min:", heap1.findMin()); // Expected: 5

// const heap2 = new LeftistHeap();
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
class LeftistNodeTS {
    public key: number;
    public left: LeftistNodeTS | null;
    public right: LeftistNodeTS | null;
    public npl: number; // Null Path Length

    constructor(key: number) {
        this.key = key;
        this.left = null;
        this.right = null;
        this.npl = 0;
    }
}

class LeftistHeapTS {
    public root: LeftistNodeTS | null = null;

    private _npl(node: LeftistNodeTS | null): number {
        return node ? node.npl : -1;
    }

    private _mergeRecursive(h1: LeftistNodeTS | null, h2: LeftistNodeTS | null): LeftistNodeTS | null {
        if (!h1) return h2;
        if (!h2) return h1;
        
        // Ensure h1.key <= h2.key (min-heap property)
        if (h1.key > h2.key) {
            [h1, h2] = [h2, h1]; // Swap h1 and h2
        }
        
        // Merge h1's right child with h2
        h1.right = this._mergeRecursive(h1.right, h2);
        
        // Restore leftist property: ensure npl(left) >= npl(right)
        if (this._npl(h1.left) < this._npl(h1.right)) {
            [h1.left, h1.right] = [h1.right, h1.left]; // Swap children
        }
        
        // Update npl of h1
        h1.npl = this._npl(h1.right) + 1;
        
        return h1;
    }

    public insert(key: number): void {
        const newNode = new LeftistNodeTS(key);
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

    public merge(otherHeap: LeftistHeapTS): void {
        this.root = this._mergeRecursive(this.root, otherHeap.root);
        otherHeap.root = null; // Other heap is now empty
    }
}

// const heap1TS = new LeftistHeapTS();
// heap1TS.insert(10);
// heap1TS.insert(30);
// heap1TS.insert(5);
// console.log("Heap1 min:", heap1TS.findMin()); // Expected: 5

// const heap2TS = new LeftistHeapTS();
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

class LeftistNode {
public:
    int key;
    LeftistNode <em>left;
    LeftistNode </em>right;
    int npl; // Null Path Length

    LeftistNode(int k) : key(k), left(nullptr), right(nullptr), npl(0) {}
};

class LeftistHeap {
public:
    LeftistNode<em> root;

    LeftistHeap() : root(nullptr) {}

    // Helper to get Null Path Length (NPL)
    int getNpl(LeftistNode</em> node) {
        return node ? node->npl : -1;
    }

    // Main merge function
    LeftistNode<em> mergeRecursive(LeftistNode</em> h1, LeftistNode<em> h2) {
        if (!h1) return h2;
        if (!h2) return h1;

        // Ensure h1.key <= h2.key (min-heap property)
        if (h1->key > h2->key) {
            std::swap(h1, h2);
        }

        // Merge h1's right child with h2
        h1->right = mergeRecursive(h1->right, h2);

        // Restore leftist property: ensure npl(left) >= npl(right)
        if (getNpl(h1->left) < getNpl(h1->right)) {
            std::swap(h1->left, h1->right);
        }

        // Update npl of h1
        h1->npl = getNpl(h1->right) + 1;

        return h1;
    }

    void insert(int key) {
        LeftistNode</em> newNode = new LeftistNode(key);
        root = mergeRecursive(root, newNode);
    }

    int extractMin() {
        if (!root) {
            // Handle error or return a sentinel value
            return -1; // Or throw an exception
        }
        
        int minKey = root->key;
        LeftistNode<em> oldRoot = root;
        root = mergeRecursive(root->left, root->right);
        delete oldRoot; // Free the old root node
        return minKey;
    }

    int findMin() {
        return root ? root->key : -1; // Or throw an exception
    }

    void merge(LeftistHeap& other_heap) {
        root = mergeRecursive(root, other_heap.root);
        other_heap.root = nullptr; // Other heap is now empty
    }
};

// int main() {
//     LeftistHeap heap1;
//     heap1.insert(10);
//     heap1.insert(30);
//     heap1.insert(5);
//     std::cout << "Heap1 min: " << heap1.findMin() << std::endl; // Expected: 5

//     LeftistHeap heap2;
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

type LeftistNode struct {
    Key   int
    Left  </em>LeftistNode
    Right <em>LeftistNode
    Npl   int // Null Path Length
}

func NewLeftistNode(key int) </em>LeftistNode {
    return &LeftistNode{Key: key, Npl: 0}
}

type LeftistHeap struct {
    Root <em>LeftistNode
}

func (lh </em>LeftistHeap) npl(node <em>LeftistNode) int {
    if node == nil {
        return -1
    }
    return node.Npl
}

func (lh </em>LeftistHeap) mergeRecursive(h1, h2 <em>LeftistNode) </em>LeftistNode {
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
    h1.Right = lh.mergeRecursive(h1.Right, h2)

    // Restore leftist property: ensure npl(left) >= npl(right)
    if lh.npl(h1.Left) < lh.npl(h1.Right) {
        h1.Left, h1.Right = h1.Right, h1.Left // Swap children
    }

    // Update npl of h1
    h1.Npl = lh.npl(h1.Right) + 1

    return h1
}

func (lh <em>LeftistHeap) Insert(key int) {
    newNode := NewLeftistNode(key)
    lh.Root = lh.mergeRecursive(lh.Root, newNode)
}

func (lh </em>LeftistHeap) ExtractMin() (int, error) {
    if lh.Root == nil {
        return 0, fmt.Errorf("heap is empty")
    }

    minKey := lh.Root.Key
    lh.Root = lh.mergeRecursive(lh.Root.Left, lh.Root.Right)
    return minKey, nil
}

func (lh <em>LeftistHeap) FindMin() (int, error) {
    if lh.Root == nil {
        return 0, fmt.Errorf("heap is empty")
    }
    return lh.Root.Key, nil
}

func (lh </em>LeftistHeap) Merge(otherHeap *LeftistHeap) {
    lh.Root = lh.mergeRecursive(lh.Root, otherHeap.Root)
    otherHeap.Root = nil // Other heap is now empty
}

// func main() {
//     heap1 := &LeftistHeap{}
//     heap1.Insert(10)
//     heap1.Insert(30)
//     heap1.insert(5)
//     min1, _ := heap1.FindMin()
//     fmt.Println("Heap1 min:", min1) // Expected: 5

//     heap2 := &LeftistHeap{}
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
import std.algorithm; // For std.algorithm.swap
import std.conv; // For to!string

class LeftistNode {
    int key;
    LeftistNode left;
    LeftistNode right;
    int npl; // Null Path Length

    this(int k) {
        key = k;
        left = null;
        right = null;
        npl = 0;
    }
}

class LeftistHeap {
    LeftistNode root;

    this() {
        root = null;
    }

private:
    int getNpl(LeftistNode node) {
        return node ? node.npl : -1;
    }

    LeftistNode mergeRecursive(LeftistNode h1, LeftistNode h2) {
        if (h1 is null) return h2;
        if (h2 is null) return h1;
        
        // Ensure h1.key <= h2.key (min-heap property)
        if (h1.key > h2.key) {
            swap(h1, h2);
        }
        
        // Merge h1's right child with h2
        h1.right = mergeRecursive(h1.right, h2);
        
        // Restore leftist property: ensure npl(left) >= npl(right)
        if (getNpl(h1.left) < getNpl(h1.right)) {
            swap(h1.left, h1.right);
        }
        
        // Update npl of h1
        h1.npl = getNpl(h1.right) + 1;
        
        return h1;
    }

public:
    void insert(int key) {
        LeftistNode new_node = new LeftistNode(key);
        root = mergeRecursive(root, new_node);
    }

    int extractMin() {
        if (root is null) {
            throw new Exception("Heap is empty");
        }
        
        int min_key = root.key;
        LeftistNode old_root = root;
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

    void merge(LeftistHeap other_heap) {
        root = mergeRecursive(root, other_heap.root);
        other_heap.root = null; // Other heap is now empty
    }
}

// void main() {
//     auto heap1 = new LeftistHeap();
//     heap1.insert(10);
//     heap1.insert(30);
//     heap1.insert(5);
//     writefln("Heap1 min: %s", heap1.findMin()); // Expected: 5

//     auto heap2 = new LeftistHeap();
//     heap2.insert(20);
//     heap2.insert(2);
//     writefln("Heap2 min: %s", heap2.findMin()); // Expected: 2

//     heap1.merge(heap2);
//     writefln("Merged heap min: %s", heap1.findMin()); // Expected: 2
//     writefln("Extract min: %s", heap1.extractMin()); // Expected: 2
//     writefln("Merged heap min after extract: %s", heap1.findMin()); // Expected: 5
// }
```

## Applications

### Application

Leftist Heaps are a type of mergeable `priority queue`, meaning they efficiently support the operation of combining two heaps into one. This makes them suitable for applications where merging heaps is a common or critical operation.
- **Event Simulation:** Managing events with different priorities, especially when events might be generated by multiple sources and their respective `priority queues` need to be combined.
- **Graph Algorithms:** Can be used in algorithms like `Dijkstra's` or `Prim's` where `priority queues` are used, and especially if intermediate `priority queues` need to be merged.
- **Distributed Systems:** Where `priority queues` might exist on different nodes and need to be periodically synchronized or merged.
- **Parallel Algorithms:** Efficiently combining results from parallel computations that produce separate `priority queues`.

