---
title: "Fibonacci Heap"
---

A `Fibonacci Heap` is a collection of disjoint heaps (min-heap ordered trees). It is an advanced heap data structure that implements a `priority queue`, providing better amortized time complexity than a traditional `binary heap` for some operations, notably `decrease-key` and `merge`.

It was developed by Michael `L. Fredman` and Robert `Tarjan` in 1987. While its constant factors are large, making it impractical for many applications, its theoretical efficiency makes it invaluable for proving the time complexity bounds of algorithms like `Dijkstra's shortest path algorithm` and `Prim's minimum spanning tree algorithm` when applied to dense graphs.

## How it Works

### How it Works (Expanded)

A `Fibonacci Heap` is a forest of trees satisfying the `min-heap` property. Each `node` stores a `key`, pointers to its parent, children (via a child pointer and a circular doubly linked list of siblings), and a `mark` bit. The `root nodes` of all the trees are linked together in a circular doubly linked list.

---

Conceptual structure of a Fibonacci Heap:

          (Min Node)
            /
(Root List) - A <-> B <-> C - (Root List)
              |     |
              D     E
              |     |
              F     G
                  ...

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
# Conceptual / Pseudocode for Fibonacci Heap operations in Python.
# A full implementation is very complex and typically not required for general purposes.
# This code aims to illustrate the class structure and the spirit of operations.

class FibonacciHeapNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.parent = None
        self.child = None # Pointer to any one of its children
        self.left = self # Pointers for circular doubly linked list of siblings
        self.right = self
        self.degree = 0
        self.mark = False

class FibonacciHeap:
    def __init__(self):
        self.min_node = None # Pointer to the node with the minimum key
        self.n = 0 # Number of nodes in the heap

    def insert(self, key, value=None):
        node = FibonacciHeapNode(key, value)
        if self.min_node is None:
            self.min_node = node
        else:
            self._add_to_root_list(node)
            if node.key < self.min_node.key:
                self.min_node = node
        self.n += 1
        return node # Return node for decrease_key reference

    def find_min(self):
        return self.min_node

    def extract_min(self):
        # Very complex operation, simplified for conceptual understanding.
        # Involves removing min_node, adding its children to root list,
        # and then consolidating the root list.
        if self.min_node is None:
            return None

        z = self.min_node
        if z.child is not None:
            children_to_add = []
            curr_child = z.child
            while True: # Iterate through z's children (circular list)
                children_to_add.append(curr_child)
                curr_child.parent = None # Remove parent link
                curr_child = curr_child.right
                if curr_child == z.child:
                    break
            for child in children_to_add:
                self._add_to_root_list(child)
        
        # Remove z from root list
        self._remove_from_root_list(z)
        self.n -= 1

        if self.n == 0:
            self.min_node = None
        else:
            self.min_node = z.right # Pick an arbitrary new min_node
            # self._consolidate() # This is the most complex part, omitted for brevity

        return z

    def _add_to_root_list(self, node):
        if self.min_node is None:
            self.min_node = node
            node.left = node
            node.right = node
        else:
            # Insert node next to min_node in the circular list
            node.left = self.min_node
            node.right = self.min_node.right
            self.min_node.right.left = node
            self.min_node.right = node

    def _remove_from_root_list(self, node):
        node.left.right = node.right
        node.right.left = node.left

    # Conceptual decrease_key (full implementation very involved)
    def decrease_key(self, node, new_key):
        if new_key > node.key:
            raise ValueError("New key is greater than current key")
        
        node.key = new_key
        y = node.parent
        if y is not None and node.key < y.key:
            # Cut node from its parent
            # self._cut(node, y) # Complex operation, omitted
            # self._cascading_cut(y) # Complex operation, omitted
            pass # Placeholder for cut and cascading_cut
        if node.key < self.min_node.key:
            self.min_node = node

    def merge(self, other_heap):
        # Simply concatenate root lists
        if self.min_node is None:
            self.min_node = other_heap.min_node
        elif other_heap.min_node is not None:
            # Splice other_heap's root list into self.min_node's root list
            self.min_node.right.left = other_heap.min_node.left
            other_heap.min_node.left.right = self.min_node.right
            self.min_node.right = other_heap.min_node
            other_heap.min_node.left = self.min_node
            if other_heap.min_node.key < self.min_node.key:
                self.min_node = other_heap.min_node
        self.n += other_heap.n

# Example Usage (highly conceptual due to complexity of full implementation):
# f_heap = FibonacciHeap()
# node1 = f_heap.insert(10)
# node2 = f_heap.insert(3)
# f_heap.insert(15)
# print("Min node:", f_heap.find_min().key) # Expected: 3
# f_heap.decrease_key(node1, 2)
# print("Min node after decrease_key:", f_heap.find_min().key) # Expected: 2 (if cut logic was full)
# extracted_min = f_heap.extract_min()
# print("Extracted min:", extracted_min.key) # Expected: 2
```

### Javascript

```javascript
// Conceptual / Pseudocode for Fibonacci Heap operations in JavaScript.
// A full implementation is very complex and typically not required for general purposes.

class FibonacciHeapNode {
    constructor(key, value = null) {
        this.key = key;
        this.value = value;
        this.parent = null;
        this.child = null; // Pointer to any one of its children
        this.left = this;  // Pointers for circular doubly linked list of siblings
        this.right = this;
        this.degree = 0;
        this.mark = false;
    }
}

class FibonacciHeap {
    constructor() {
        this.minNode = null; // Pointer to the node with the minimum key
        this.n = 0; // Number of nodes in the heap
    }

    insert(key, value = null) {
        const node = new FibonacciHeapNode(key, value);
        if (this.minNode === null) {
            this.minNode = node;
        } else {
            this._addToRootList(node);
            if (node.key < this.minNode.key) {
                this.minNode = node;
            }
        }
        this.n++;
        return node; // Return node for decreaseKey reference
    }

    findMin() {
        return this.minNode;
    }

    extractMin() {
        // Very complex operation, simplified for conceptual understanding.
        // Involves removing minNode, adding its children to root list,
        // and then consolidating the root list.
        if (this.minNode === null) {
            return null;
        }

        const z = this.minNode;
        if (z.child !== null) {
            let childrenToAdd = [];
            let currChild = z.child;
            do { // Iterate through z's children (circular list)
                childrenToAdd.push(currChild);
                currChild.parent = null; // Remove parent link
                currChild = currChild.right;
            } while (currChild !== z.child);

            for (const child of childrenToAdd) {
                this._addToRootList(child);
            }
        }
        
        // Remove z from root list
        this._removeFromRootList(z);
        this.n--;

        if (this.n === 0) {
            this.minNode = null;
        } else {
            this.minNode = z.right; // Pick an arbitrary new minNode
            // this._consolidate(); // This is the most complex part, omitted for brevity
        }

        return z;
    }

    _addToRootList(node) {
        if (this.minNode === null) {
            this.minNode = node;
            node.left = node;
            node.right = node;
        } else {
            // Insert node next to minNode in the circular list
            node.left = this.minNode;
            node.right = this.minNode.right;
            this.minNode.right.left = node;
            this.minNode.right = node;
        }
    }

    _removeFromRootList(node) {
        node.left.right = node.right;
        node.right.left = node.left;
    }

    // Conceptual decreaseKey (full implementation very involved)
    decreaseKey(node, newKey) {
        if (newKey > node.key) {
            throw new Error("New key is greater than current key");
        }
        
        node.key = newKey;
        const y = node.parent;
        if (y !== null && node.key < y.key) {
            // Cut node from its parent
            // this._cut(node, y); // Complex operation, omitted
            // this._cascadingCut(y); // Complex operation, omitted
        }
        if (node.key < this.minNode.key) {
            this.minNode = node;
        }
    }

    merge(otherHeap) {
        // Simply concatenate root lists
        if (this.minNode === null) {
            this.minNode = otherHeap.minNode;
        } else if (otherHeap.minNode !== null) {
            // Splice otherHeap's root list into self.minNode's root list
            this.minNode.right.left = otherHeap.minNode.left;
            otherHeap.minNode.left.right = this.minNode.right;
            this.minNode.right = otherHeap.minNode;
            otherHeap.minNode.left = this.minNode;
            if (otherHeap.minNode.key < this.minNode.key) {
                this.minNode = otherHeap.minNode;
            }
        }
        this.n += otherHeap.n;
    }
}

// Example Usage (highly conceptual due to complexity of full implementation):
// const fHeap = new FibonacciHeap();
// const node1 = fHeap.insert(10);
// const node2 = fHeap.insert(3);
// fHeap.insert(15);
// console.log("Min node:", fHeap.findMin().key); // Expected: 3
// // fHeap.decreaseKey(node1, 2); // Requires full cut/cascading cut
// // console.log("Min node after decreaseKey:", fHeap.findMin().key);
// const extractedMin = fHeap.extractMin();
// console.log("Extracted min:", extractedMin.key); // Expected: 3
```

### Cpp

```cpp
#include <iostream>
#include <vector>
#include <algorithm> // For std::min
#include <limits>    // For std::numeric_limits

// Conceptual Fibonacci Heap Node
class FibonacciHeapNode {
public:
    int key;
    void<em> value; // Can store any associated value
    FibonacciHeapNode</em> parent;
    FibonacciHeapNode<em> child; // Pointer to any one of its children
    FibonacciHeapNode</em> left;  // Pointers for circular doubly linked list of siblings
    FibonacciHeapNode<em> right;
    int degree;
    bool mark;

    FibonacciHeapNode(int k, void</em> val = nullptr) :
        key(k), value(val), parent(nullptr), child(nullptr),
        left(this), right(this), degree(0), mark(false) {}
};

// Conceptual Fibonacci Heap (Simplified - full implementation is very complex)
class FibonacciHeap {
private:
    FibonacciHeapNode<em> min_node; // Pointer to the node with the minimum key
    int n; // Number of nodes in the heap

    // Helper to add a node to the root list (circular doubly linked list)
    void _add_to_root_list(FibonacciHeapNode</em> node) {
        if (min_node == nullptr) {
            min_node = node;
            node->left = node;
            node->right = node;
        } else {
            // Insert node next to min_node in the circular list
            node->left = min_node;
            node->right = min_node->right;
            min_node->right->left = node;
            min_node->right = node;
        }
    }

    // Helper to remove a node from the root list
    void _remove_from_root_list(FibonacciHeapNode<em> node) {
        node->left->right = node->right;
        node->right->left = node->left;
    }
    
    // Consolidate is the most complex part, omitted for brevity.
    // It reduces the number of trees in the heap after extract_min.
    void _consolidate() {
        // Pseudo-code:
        // Create an array of pointers to roots, indexed by degree.
        // Iterate through root list, linking trees of same degree.
        // Update min_node.
    }

    // Cut and Cascading Cut are complex, omitted for brevity.
    // They are used in decrease_key to maintain heap properties.
    void _cut(FibonacciHeapNode</em> x, FibonacciHeapNode<em> y) {
        // Remove x from y's child list
        // Add x to the root list
        // y.degree--
        // x.mark = false
    }

    void _cascading_cut(FibonacciHeapNode</em> y) {
        // if y has a parent and is marked, cut y from its parent
        // if y is unmarked, mark it
    }


public:
    FibonacciHeap() : min_node(nullptr), n(0) {}

    // Destructor (important for memory management in C++)
    ~FibonacciHeap() {
        // Proper recursive deletion of all nodes is complex for Fibonacci Heap
        // For conceptual simplicity, this is often a major challenge.
        // In a full implementation, you'd iterate through all nodes and delete them.
    }

    FibonacciHeapNode<em> insert(int key, void</em> value = nullptr) {
        FibonacciHeapNode<em> node = new FibonacciHeapNode(key, value);
        _add_to_root_list(node);
        if (node->key < min_node->key) {
            min_node = node;
        }
        n++;
        return node;
    }

    FibonacciHeapNode</em> find_min() const {
        return min_node;
    }

    FibonacciHeapNode<em> extract_min() {
        if (min_node == nullptr) {
            return nullptr;
        }

        FibonacciHeapNode</em> z = min_node;

        // Add children of z to the root list
        if (z->child != nullptr) {
            FibonacciHeapNode<em> current_child = z->child;
            do {
                FibonacciHeapNode</em> next_child = current_child->right;
                _remove_from_root_list(current_child); // Temporarily remove from old child list
                _add_to_root_list(current_child); // Add to new root list
                current_child->parent = nullptr;
                current_child = next_child;
            } while (current_child != z->child); // Fixed: loop until we've processed all children
        }

        _remove_from_root_list(z);
        n--;

        if (n == 0) {
            min_node = nullptr;
        } else {
            // This is the most complex part: consolidate the root list
            // For conceptual code, we'll just pick a new min and skip consolidation.
            // In a real implementation, call _consolidate() here.
            min_node = min_node->right; // Arbitrary new min for demonstration
            // _consolidate(); // Placeholder
        }

        return z; // The extracted node (caller is responsible for deleting it)
    }

    void decrease_key(FibonacciHeapNode<em> x, int new_key) {
        if (new_key > x->key) {
            throw std::runtime_error("New key is greater than current key");
        }
        
        x->key = new_key;
        FibonacciHeapNode</em> y = x->parent;

        if (y != nullptr && x->key < y->key) {
            // _cut(x, y); // Placeholder for cut operation
            // _cascading_cut(y); // Placeholder for cascading cut operation
        }
        if (x->key < min_node->key) {
            min_node = x;
        }
    }

    void merge(FibonacciHeap<em> other_heap) {
        if (min_node == nullptr) {
            min_node = other_heap->min_node;
        } else if (other_heap->min_node != nullptr) {
            // Concatenate the root lists
            FibonacciHeapNode</em> this_right = min_node->right;
            FibonacciHeapNode* other_left = other_heap->min_node->left;

            min_node->right = other_heap->min_node;
            other_heap->min_node->left = min_node;
            this_right->left = other_left;
            other_left->right = this_right;

            if (other_heap->min_node->key < min_node->key) {
                min_node = other_heap->min_node;
            }
        }
        n += other_heap->n;
        other_heap->min_node = nullptr; // Ensure other_heap is empty
        other_heap->n = 0;
    }
};
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

A full `Fibonacci Heap` implementation is notoriously complex due to its intricate structure and '`lazy`' operations. The provided conceptual code highlights the main classes and the high-level steps of some operations.

---

**`FibonacciHeapNode` Class:** Represents a `node` in the heap.
- `key`, `value`: Data stored in the `node`.
- `parent`, `child`: Pointers to parent and one child.
- `left`, `right`: Pointers for the circular doubly linked list of siblings.
- `degree`: Number of children.
- `mark`: A boolean flag for `decrease-key` operations.

**`FibonacciHeap` Class:** Manages the collection of trees.
- `min_node`: Pointer to the `node` with the minimum `key` in the entire heap.
- `n`: Total number of `nodes` in the heap.
- **`insert(key, value)`:** Creates a new `FibonacciHeapNode` and adds it to the `root list` (a circular doubly linked list of tree `roots`). Updates `min_node` if the new `node`'s `key` is smaller. `O(1)` amortized.
- **`find_min()`:** Returns `min_node`. `O(1)`.
- **`extract_min()`:** The most complex operation. It removes the `min_node`, adds its children to the `root list`, and then (conceptually) calls a `consolidate` function. This `consolidate` operation reduces the number of trees in the `root list` by linking trees of the same degree. `O(log n)` amortized.
- **`decrease_key(node, new_key)`:** Decreases a `node`'s `key`. If this violates the `min-heap` property, the `node` is '`cut`' from its parent and moved to the `root list`. This can trigger '`cascading cuts`' up the tree if parents also violate their `min-heap` property. `O(1)` amortized.
- **`merge(other_heap)`:** Concatenates the `root lists` of two `Fibonacci Heaps`. `O(1)`.

[Back to Implementation](#implementation)

## Applications

### Application

Fibonacci Heaps are primarily of theoretical importance due to their excellent amortized time complexities. Their most famous application is in optimizing graph algorithms. For instance, they are used to improve the asymptotic running time of **Dijkstra's shortest path algorithm** to `O(E + V log V)` and **Prim's algorithm for minimum spanning trees** to `O(E + V log V)`, which is a significant improvement for dense graphs. While their high constant factors make them less practical for many real-world applications compared to simpler heaps, they are essential for theoretical computer science and in scenarios where the `decrease-key` operation is very frequent.

