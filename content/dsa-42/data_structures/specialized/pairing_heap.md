---
title: "Pairing Heap"
---

A `Pairing Heap` is a simple, efficient, and highly practical type of `mergeable heap` data structure. It supports operations like `insert`, `extract-min`, `decrease-key`, and `merge` with excellent amortized time complexities, often outperforming `Fibonacci Heaps` in practice despite having worse theoretical worst-case bounds for some operations.

Its "`pairing`" property comes from how it combines sub-heaps during its `merge` operation, resulting in a relatively flat tree structure that is easy to implement.

## How it Works

### How it Works (Expanded)

A `Pairing Heap` is a `min-heap` (or `max-heap`) ordered `multi-way tree`. Each `node` contains a `key` and a `list` of its children. There are no explicit `rank` or `npl (null path length)` values. Its efficiency comes from a specific `merge` operation that is used as a building block for most other operations.

---

Conceptual Pairing Heap Node:

      (Key=10)
     / | \
   (20)(30)(40) (Children list)

## Implementation {#implementation}

### Python

```python
class PairingNode:
    def __init__(self, key):
        self.key = key
        self.child = None    # Pointer to first child
        self.sibling = None  # Pointer to next sibling (in child list)
        self.prev = None     # Pointer to previous sibling/parent (for decrease-key)

class PairingHeap:
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
        
        # Make h2 a child of h1
        h2.prev = h1
        h2.sibling = h1.child
        if h1.child:
            h1.child.prev = h2
        h1.child = h2
        
        return h1

    def insert(self, key):
        new_node = PairingNode(key)
        self.root = self._merge_recursive(self.root, new_node)
        return new_node # Return new_node for decrease_key reference

    def extract_min(self):
        if not self.root:
            return None
        
        min_key = self.root.key
        
        # Merge children of the root
        if self.root.child:
            self._merge_pairs(self.root.child)
        else:
            new_root = None
        
        # Clear old root (in Python, GC handles it)
        # self.root = None # For explicit deletion
        
        self.root = new_root
        return min_key

    def _merge_pairs(self, child_list_head):
        if not child_list_head or not child_list_head.sibling:
            return child_list_head
        
        # First pass: merge children in pairs
        h1 = child_list_head
        h2 = child_list_head.sibling
        h3 = h2.sibling # Remaining list
        
        h1.prev = None
        h2.prev = None
        h1.sibling = None # Detach h1 from h2
        h2.sibling = None # Detach h2 from h3 (if h3 exists) 
        
        return self._merge_recursive(self._merge_recursive(h1, h2), self._merge_pairs(h3))

    def decrease_key(self, node, new_key):
        if not node or new_key > node.key:
            raise ValueError("New key is greater than current key or node is invalid.")
        
        node.key = new_key
        # If node is not the root and its key is smaller than its parent's key
        if node.prev: # node.prev could be parent or sibling
            # Cut node from its parent/sibling list
            if node.prev.child == node: # node is first child
                node.prev.child = node.sibling
            else: # node is a sibling
                node.prev.sibling = node.sibling
            if node.sibling:
                node.sibling.prev = node.prev
            
            node.prev = None
            node.sibling = None
            
            # Merge the cut node with the main heap
            self.root = self._merge_recursive(self.root, node)

    def find_min(self):
        return self.root.key if self.root else None

    def merge(self, other_heap):
        self.root = self._merge_recursive(self.root, other_heap.root)
        other_heap.root = None # Other heap is now empty

# Example Usage:
# ph = PairingHeap()
# node1 = ph.insert(10)
# node2 = ph.insert(30)
# node3 = ph.insert(5) # min
# node4 = ph.insert(20)

# print("Min:", ph.find_min()) # 5
# ph.decrease_key(node2, 2) # Change 30 to 2
# print("Min after decrease_key (30->2):", ph.find_min()) # 2

# extracted = ph.extract_min() # Extract 2
# print("Extracted:", extracted) # 2
# print("Min after extract:", ph.find_min()) # 5
```

### Javascript

```javascript
class PairingNode {
    constructor(key) {
        this.key = key;
        this.child = null;
        this.sibling = null;
        this.prev = null;
    }
}

class PairingHeap {
    constructor() {
        this.root = null;
    }

    _mergeRecursive(h1, h2) {
        if (!h1) return h2;
        if (!h2) return h1;
        
        if (h1.key > h2.key) {
            [h1, h2] = [h2, h1];
        }
        
        h2.prev = h1;
        h2.sibling = h1.child;
        if (h1.child) {
            h1.child.prev = h2;
        }
        h1.child = h2;
        
        return h1;
    }

    insert(key) {
        const newNode = new PairingNode(key);
        this.root = this._mergeRecursive(this.root, newNode);
        return newNode;
    }

    extractMin() {
        if (!this.root) {
            return null;
        }
        
        const minKey = this.root.key;
        
        if (this.root.child) {
            this.root.child.prev = null;
            this.root = this._mergePairs(this.root.child);
        } else {
            this.root = null;
        }
        
        return minKey;
    }

    _mergePairs(childListHead) {
        if (!childListHead || !childListHead.sibling) {
            return childListHead;
        }
        
        const h1 = childListHead;
        const h2 = childListHead.sibling;
        const h3 = h2.sibling;
        
        h1.prev = null;
        h2.prev = null;
        h1.sibling = null;
        h2.sibling = null;
        
        return this._mergeRecursive(this._mergeRecursive(h1, h2), this._mergePairs(h3));
    }

    decreaseKey(node, newKey) {
        if (!node || newKey > node.key) {
            throw new Error("New key is greater than current key or node is invalid.");
        }
        
        node.key = newKey;
        if (node.prev) {
            if (node.prev.child === node) {
                node.prev.child = node.sibling;
            } else {
                node.prev.sibling = node.sibling;
            }
            if (node.sibling) {
                node.sibling.prev = node.prev;
            }
            
            node.prev = null;
            node.sibling = null;
            
            this.root = this._mergeRecursive(this.root, node);
        }
    }

    findMin() {
        return this.root ? this.root.key : null;
    }

    merge(otherHeap) {
        this.root = this._mergeRecursive(this.root, otherHeap.root);
        otherHeap.root = null;
    }
}

// const ph = new PairingHeap();
// const node1 = ph.insert(10);
// const node2 = ph.insert(30);
// const node3 = ph.insert(5); // min
// const node4 = ph.insert(20);

// console.log("Min:", ph.findMin()); // 5
// ph.decreaseKey(node2, 2); // Change 30 to 2
// console.log("Min after decrease_key (30->2):", ph.findMin()); // 2

// const extracted = ph.extractMin(); // Extract 2
// console.log("Extracted:", extracted); // 2
// console.log("Min after extract:", ph.findMin()); // 5
```

### Typescript

```typescript
class PairingNodeTS {
    public key: number;
    public child: PairingNodeTS | null;
    public sibling: PairingNodeTS | null;
    public prev: PairingNodeTS | null;

    constructor(key: number) {
        this.key = key;
        this.child = null;
        this.sibling = null;
        this.prev = null;
    }
}

class PairingHeapTS {
    public root: PairingNodeTS | null = null;

    private _mergeRecursive(h1: PairingNodeTS | null, h2: PairingNodeTS | null): PairingNodeTS | null {
        if (!h1) return h2;
        if (!h2) return h1;
        
        if (h1.key > h2.key) {
            [h1, h2] = [h2, h1];
        }
        
        h2.prev = h1;
        h2.sibling = h1.child;
        if (h1.child) {
            h1.child.prev = h2;
        }
        h1.child = h2;
        
        return h1;
    }

    public insert(key: number): PairingNodeTS {
        const newNode = new PairingNodeTS(key);
        this.root = this._mergeRecursive(this.root, newNode);
        return newNode;
    }

    public extractMin(): number | null {
        if (!this.root) {
            return null;
        }
        
        const minKey = this.root.key;
        
        if (this.root.child) {
            this.root.child.prev = null;
            this.root = this._mergePairs(this.root.child);
        } else {
            this.root = null;
        }
        
        return minKey;
    }

    private _mergePairs(childListHead: PairingNodeTS | null): PairingNodeTS | null {
        if (!childListHead || !childListHead.sibling) {
            return childListHead;
        }
        
        const h1 = childListHead;
        const h2 = childListHead.sibling;
        const h3 = h2.sibling;
        
        h1.prev = null;
        h2.prev = null;
        h1.sibling = null;
        h2.sibling = null;
        
        return this._mergeRecursive(this._mergeRecursive(h1, h2), this._mergePairs(h3));
    }

    public decreaseKey(node: PairingNodeTS, newKey: number): void {
        if (!node || newKey > node.key) {
            throw new Error("New key is greater than current key or node is invalid.");
        }
        
        node.key = newKey;
        if (node.prev) {
            if (node.prev.child === node) {
                node.prev.child = node.sibling;
            } else {
                node.prev.sibling = node.sibling;
            }
            if (node.sibling) {
                node.sibling.prev = node.prev;
            }
            
            node.prev = null;
            node.sibling = null;
            
            this.root = this._mergeRecursive(this.root, node);
        }
    }

    public findMin(): number | null {
        return this.root ? this.root.key : null;
    }

    public merge(otherHeap: PairingHeapTS): void {
        this.root = this._mergeRecursive(this.root, otherHeap.root);
        otherHeap.root = null;
    }
}

// const phTS = new PairingHeapTS();
// const node1TS = phTS.insert(10);
// const node2TS = phTS.insert(30);
// const node3TS = phTS.insert(5);
// const node4TS = phTS.insert(20);

// console.log("Min:", phTS.findMin()); // 5
// phTS.decreaseKey(node2TS, 2); // Change 30 to 2
// console.log("Min after decrease_key (30->2):", phTS.findMin()); // 2

// const extractedTS = phTS.extractMin(); // Extract 2
// console.log("Extracted:", extractedTS); // 2
// console.log("Min after extract:", phTS.findMin()); // 5
```

### Cpp

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <stdexcept>

class PairingNode {
public:
    int key;
    PairingNode <em>child;
    PairingNode </em>sibling;
    PairingNode <em>prev;

    PairingNode(int k) : key(k), child(nullptr), sibling(nullptr), prev(nullptr) {}
};

class PairingHeap {
public:
    PairingNode</em> root;

    PairingHeap() : root(nullptr) {}

    PairingNode<em> mergeRecursive(PairingNode</em> h1, PairingNode<em> h2) {
        if (!h1) return h2;
        if (!h2) return h1;

        if (h1->key > h2->key) {
            std::swap(h1, h2);
        }

        h2->prev = h1;
        h2->sibling = h1->child;
        if (h1->child) {
            h1->child->prev = h2;
        }
        h1->child = h2;
        
        return h1;
    }

    PairingNode</em> mergePairs(PairingNode<em> child_list_head) {
        if (!child_list_head || !child_list_head->sibling) {
            return child_list_head;
        }
        
        PairingNode</em> h1 = child_list_head;
        PairingNode<em> h2 = child_list_head->sibling;
        PairingNode</em> h3 = h2->sibling;
        
        h1->prev = nullptr;
        h2->prev = nullptr;
        h1->sibling = nullptr;
        h2->sibling = nullptr;
        
        return mergeRecursive(mergeRecursive(h1, h2), mergePairs(h3));
    }

    PairingNode<em> insert(int key) {
        PairingNode</em> newNode = new PairingNode(key);
        root = mergeRecursive(root, newNode);
        return newNode;
    }

    int extractMin() {
        if (!root) {
            throw std::runtime_error("Heap is empty");
        }
        
        int minKey = root->key;
        PairingNode<em> oldRoot = root;
        
        if (root->child) {
            root->child->prev = nullptr;
            root = mergePairs(root->child);
        } else {
            root = nullptr;
        }
        
        delete oldRoot;
        return minKey;
    }

    void decreaseKey(PairingNode</em> node, int newKey) {
        if (!node || newKey > node->key) {
            throw std::runtime_error("New key is greater than current key or node is invalid.");
        }
        
        node->key = newKey;
        if (node->prev) {
            if (node->prev->child == node) {
                node->prev->child = node->sibling;
            } else {
                node->prev->sibling = node->sibling;
            }
            if (node->sibling) {
                node->sibling->prev = node->prev;
            }
            
            node->prev = nullptr;
            node->sibling = nullptr;
            
            root = mergeRecursive(root, node);
        }
    }

    int findMin() {
        if (!root) {
            throw std::runtime_error("Heap is empty");
        }
        return root->key;
    }

    void merge(PairingHeap& other_heap) {
        root = mergeRecursive(root, other_heap.root);
        other_heap.root = nullptr;
    }
};

// int main() {
//     PairingHeap ph;
//     PairingNode<em> node1 = ph.insert(10);
//     PairingNode</em> node2 = ph.insert(30);
//     PairingNode<em> node3 = ph.insert(5); // min
//     PairingNode</em> node4 = ph.insert(20);

//     std::cout << "Min: " << ph.findMin() << std::endl; // 5
//     ph.decreaseKey(node2, 2); // Change 30 to 2
//     std::cout << "Min after decrease_key (30->2): " << ph.findMin() << std::endl; // 2

//     int extracted = ph.extractMin(); // Extract 2
//     std::cout << "Extracted: " << extracted << std::endl; // 2
//     std::cout << "Min after extract: " << ph.findMin() << std::endl; // 5
//     return 0;
// }
```

### Go

```go
package main

import (
    "fmt"
)

type PairingNode struct {
    Key     int
    Child   <em>PairingNode
    Sibling </em>PairingNode
    Prev    <em>PairingNode
}

func NewPairingNode(key int) </em>PairingNode {
    return &PairingNode{Key: key}
}

type PairingHeap struct {
    Root <em>PairingNode
}

func (ph </em>PairingHeap) mergeRecursive(h1, h2 <em>PairingNode) </em>PairingNode {
    if h1 == nil {
        return h2
    }
    if h2 == nil {
        return h1
    }

    if h1.Key > h2.Key {
        h1, h2 = h2, h1
    }

    h2.Prev = h1
    h2.Sibling = h1.Child
    if h1.Child != nil {
        h1.Child.Prev = h2
    }
    h1.Child = h2

    return h1
}

func (ph <em>PairingHeap) Insert(key int) </em>PairingNode {
    newNode := NewPairingNode(key)
    ph.Root = ph.mergeRecursive(ph.Root, newNode)
    return newNode
}

func (ph <em>PairingHeap) ExtractMin() (int, error) {
    if ph.Root == nil {
        return 0, fmt.Errorf("heap is empty")
    }

    minKey := ph.Root.Key
    
    if ph.Root.Child != nil {
        ph.Root.Child.Prev = nil
        ph.Root = ph.mergePairs(ph.Root.Child)
    } else {
        ph.Root = nil
    }

    return minKey, nil
}

func (ph </em>PairingHeap) mergePairs(childListHead <em>PairingNode) </em>PairingNode {
    if childListHead == nil || childListHead.Sibling == nil {
        return childListHead
    }

    h1 := childListHead
    h2 := childListHead.Sibling
    h3 := h2.Sibling

    h1.Prev = nil
    h2.Prev = nil
    h1.Sibling = nil
    h2.Sibling = nil

    return ph.mergeRecursive(ph.mergeRecursive(h1, h2), ph.mergePairs(h3))
}

func (ph <em>PairingHeap) DecreaseKey(node </em>PairingNode, newKey int) error {
    if node == nil || newKey > node.Key {
        return fmt.Errorf("new key is greater than current key or node is invalid")
    }

    node.Key = newKey
    if node.Prev != nil {
        if node.Prev.Child == node {
            node.Prev.Child = node.Sibling
        } else {
            node.Prev.Sibling = node.Sibling
        }
        if node.Sibling != nil {
            node.Sibling.Prev = node.Prev
        }

        node.Prev = nil
        node.Sibling = nil

        ph.Root = ph.mergeRecursive(ph.Root, node)
    }
    return nil
}

func (ph <em>PairingHeap) FindMin() (int, error) {
    if ph.Root == nil {
        return 0, fmt.Errorf("heap is empty")
    }
    return ph.Root.Key, nil
}

func (ph </em>PairingHeap) Merge(otherHeap *PairingHeap) {
    ph.Root = ph.mergeRecursive(ph.Root, otherHeap.Root)
    otherHeap.Root = nil
}

// func main() {
//     ph := &PairingHeap{}
//     node1 := ph.Insert(10)
//     node2 := ph.Insert(30)
//     node3 := ph.Insert(5) // min
//     node4 := ph.Insert(20)

//     minVal, _ := ph.FindMin()
//     fmt.Println("Min:", minVal) // 5
//     ph.DecreaseKey(node2, 2) // Change 30 to 2
//     minVal, _ = ph.FindMin()
//     fmt.Println("Min after DecreaseKey (30->2):", minVal) // 2

//     extracted, _ := ph.ExtractMin() // Extract 2
//     fmt.Println("Extracted:", extracted) // 2
//     minVal, _ = ph.FindMin()
//     fmt.Println("Min after extract:", minVal) // 5
// }
```

### D

```d
import std.stdio;
import std.algorithm;
import std.conv;
import std.string;

class PairingNode {
    int key;
    PairingNode child;
    PairingNode sibling;
    PairingNode prev;

    this(int k) {
        key = k;
        child = null;
        sibling = null;
        prev = null;
    }
}

class PairingHeap {
    PairingNode root;

    this() {
        root = null;
    }

private:
    PairingNode mergeRecursive(PairingNode h1, PairingNode h2) {
        if (h1 is null) return h2;
        if (h2 is null) return h1;
        
        if (h1.key > h2.key) {
            swap(h1, h2);
        }
        
        h2.prev = h1;
        h2.sibling = h1.child;
        if (h1.child !is null) {
            h1.child.prev = h2;
        }
        h1.child = h2;
        
        return h1;
    }

    PairingNode mergePairs(PairingNode child_list_head) {
        if (child_list_head is null || child_list_head.sibling is null) {
            return child_list_head;
        }
        
        PairingNode h1 = child_list_head;
        PairingNode h2 = child_list_head.sibling;
        PairingNode h3 = h2.sibling;
        
        h1.prev = null;
        h2.prev = null;
        h1.sibling = null;
        h2.sibling = null;
        
        return mergeRecursive(mergeRecursive(h1, h2), mergePairs(h3));
    }

public:
    PairingNode insert(int key) {
        PairingNode new_node = new PairingNode(key);
        root = mergeRecursive(root, new_node);
        return new_node;
    }

    int extractMin() {
        if (root is null) {
            throw new Exception("Heap is empty");
        }
        
        int min_key = root.key;
        PairingNode old_root = root;
        
        if (root.child !is null) {
            root.child.prev = null;
            root = mergePairs(root.child);
        } else {
            root = null;
        }
        
        return min_key;
    }

    void decreaseKey(PairingNode node, int new_key) {
        if (node is null || new_key > node.key) {
            throw new Exception("New key is greater than current key or node is invalid.");
        }
        
        node.key = new_key;
        if (node.prev !is null) {
            if (node.prev.child is node) {
                node.prev.child = node.sibling;
            } else {
                node.prev.sibling = node.sibling;
            }
            if (node.sibling !is null) {
                node.sibling.prev = node.prev;
            }
            
            node.prev = null;
            node.sibling = null;
            
            root = mergeRecursive(root, node);
        }
    }

    int findMin() {
        if (root is null) {
            throw new Exception("Heap is empty");
        }
        return root.key;
    }

    void merge(PairingHeap other_heap) {
        root = mergeRecursive(root, other_heap.root);
        other_heap.root = null;
    }
}

// void main() {
//     auto ph = new PairingHeap();
//     auto node1 = ph.insert(10);
//     auto node2 = ph.insert(30);
//     auto node3 = ph.insert(5); // min
//     auto node4 = ph.insert(20);

//     writefln("Min: %s", ph.findMin()); // 5
//     ph.decreaseKey(node2, 2); // Change 30 to 2
//     writefln("Min after decrease_key (30->2): %s", ph.findMin()); // 2

//     auto extracted = ph.extractMin(); // Extract 2
//     writefln("Extracted: %s", extracted); // 2
//     writefln("Min after extract: %s", ph.findMin()); // 5
// }
```

## Applications

### Application

Pairing Heaps are excellent general-purpose mergeable heaps, offering a good balance of theoretical efficiency and practical performance. They are particularly suited for applications requiring frequent `decrease-key` and `merge` operations.
- **Graph Algorithms:** Used in efficient implementations of `Dijkstra's shortest path algorithm` (especially with dense graphs) and `Prim's minimum spanning tree algorithm`, where `decrease-key` is a bottleneck for `binary heaps`.
- **Event-Driven Simulations:** Managing events with varying priorities, where events might be dynamically re-prioritized or event queues merged.
- **Network Routing Protocols:** Optimizing routing tables that involve dynamically changing costs and merging routing information.
- **Anywhere efficient mergeable `priority queues` are needed:** Providing a strong alternative to `Fibonacci Heaps` when practical speed matters more than the absolute theoretical worst-case guarantee.

