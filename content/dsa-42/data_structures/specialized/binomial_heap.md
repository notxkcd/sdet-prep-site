---
title: "Binomial Heap"
---

A `Binomial Heap` is a collection of `binomial trees` that satisfies the `min-heap property` (or `max-heap property`). Like `Fibonacci Heaps` and `Pairing Heaps`, it is a `mergeable heap`, designed for efficient `merge` operations, alongside `insertion` and `extract-min`.

Each `binomial tree` in the collection has a specific structure defined by its "`order`". The number of `nodes` in a `binomial tree` of `order k` is `2^k`, and it has `k children`. The arrangement of these `trees` within the `heap` resembles the binary representation of the total number of `elements`.

## How it Works

### How it Works (Expanded)

A `Binomial Heap` is a `forest` (collection) of `binomial trees`. A `binomial tree` of `order 0 (B0)` is a single `node`. A `binomial tree` of `order k (Bk)` is formed by linking two `Bk-1` trees: making one `root` the `leftmost child` of the other `root`, ensuring the `min-heap property` is maintained.

---

Conceptual Binomial Trees:

B0:  (Node)

B1:  (Node)
     |
    (Node)

B2:  (Node)
     |
     | (Node)
     |  |
     | (Node)
     (Node)
      |
     (Node)

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
class BinomialNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None    # Pointer to leftmost child
        self.sibling = None  # Pointer to next sibling

class BinomialHeap:
    def __init__(self):
        self.trees = [] # List of roots of binomial trees
        self.min_node = None
        self.n = 0 # Number of nodes

    def _link_trees(self, h1, h2):
        # Link two binomial trees of the same degree
        # h2 becomes child of h1
        h2.parent = h1
        h2.sibling = h1.child
        h1.child = h2
        h1.degree += 1
        return h1

    def merge(self, other_heap):
        # Merge two lists of binomial trees
        merged_trees = []
        i, j = 0, 0
        
        # Combine lists of trees, keeping them sorted by degree
        while i < len(self.trees) and j < len(other_heap.trees):
            if self.trees[i].degree < other_heap.trees[j].degree:
                merged_trees.append(self.trees[i])
                i += 1
            else:
                merged_trees.append(other_heap.trees[j])
                j += 1
        merged_trees.extend(self.trees[i:])
        merged_trees.extend(other_heap.trees[j:])
        
        self.trees = []
        self.n += other_heap.n
        other_heap.n = 0 # Other heap is now empty
        other_heap.trees = []

        if not merged_trees:
            self.min_node = None
            return

        # Actual merge (like binary addition)
        i = 0
        while i < len(merged_trees):
            if i + 1 < len(merged_trees) and merged_trees[i].degree == merged_trees[i+1].degree:
                # Two trees of same degree
                if (i + 2 < len(merged_trees) and 
                    merged_trees[i+1].degree == merged_trees[i+2].degree):
                    # Three trees of same degree, skip first and resolve later
                    self.trees.append(merged_trees[i])
                    i += 1
                else:
                    # Merge two trees
                    if merged_trees[i].key < merged_trees[i+1].key:
                        self.trees.append(self._link_trees(merged_trees[i], merged_trees[i+1]))
                    else:
                        self.trees.append(self._link_trees(merged_trees[i+1], merged_trees[i]))
                    i += 2
            else:
                self.trees.append(merged_trees[i])
                i += 1
        
        self._update_min_node()

    def insert(self, key):
        new_node = BinomialNode(key)
        temp_heap = BinomialHeap()
        temp_heap.trees.append(new_node)
        temp_heap.n = 1
        self.merge(temp_heap)

    def find_min(self):
        return self.min_node.key if self.min_node else None

    def extract_min(self):
        if not self.min_node:
            return None
        
        min_key = self.min_node.key
        
        # Remove min_node from root list
        self.trees.remove(self.min_node)
        
        # Create a new heap from min_node's children
        min_children_heap = BinomialHeap()
        
        # Reverse the order of children to maintain degree ordering for merge
        children_list = []
        current_child = self.min_node.child
        while current_child:
            next_child = current_child.sibling
            current_child.parent = None
            current_child.sibling = None
            children_list.append(current_child)
            current_child = next_child
        min_children_heap.trees = list(reversed(children_list))
        min_children_heap.n = sum(2*<em>t.degree for t in min_children_heap.trees) # Recalculate n for children

        # Merge with remaining trees
        self.merge(min_children_heap)
        self.n -= 1 # Min node was removed
        self._update_min_node()
        
        return min_key

    def _update_min_node(self):
        self.min_node = None
        if self.trees:
            self.min_node = self.trees[0]
            for tree_root in self.trees:
                if tree_root.key < self.min_node.key:
                    self.min_node = tree_root

# Example Usage:
# bh = BinomialHeap()
# bh.insert(10)
# bh.insert(20)
# bh.insert(5)
# bh.insert(3)
# print("Min:", bh.find_min()) # Expected: 3
# print("Extract Min:", bh.extract_min()) # Expected: 3
# print("Min after extract:", bh.find_min()) # Expected: 5
```

### Javascript

```javascript
class BinomialNode {
    constructor(key) {
        this.key = key;
        this.degree = 0;
        this.parent = null;
        this.child = null;    // Pointer to leftmost child
        this.sibling = null;  // Pointer to next sibling
    }
}

class BinomialHeap {
    constructor() {
        this.trees = []; // List of roots of binomial trees
        this.minNode = null;
        this.n = 0; // Number of nodes
    }

    _linkTrees(h1, h2) {
        // Link two binomial trees of the same degree
        // h2 becomes child of h1
        h2.parent = h1;
        h2.sibling = h1.child;
        h1.child = h2;
        h1.degree++;
        return h1;
    }

    merge(otherHeap) {
        let mergedTrees = [];
        let i = 0;
        let j = 0;
        
        // Combine lists of trees, keeping them sorted by degree
        while (i < this.trees.length && j < otherHeap.trees.length) {
            if (this.trees[i].degree < otherHeap.trees[j].degree) {
                mergedTrees.push(this.trees[i]);
                i++;
            } else {
                mergedTrees.push(otherHeap.trees[j]);
                j++;
            }
        }
        mergedTrees.push(...this.trees.slice(i));
        mergedTrees.push(...otherHeap.trees.slice(j));
        
        this.trees = []; // Clear current trees
        this.n += otherHeap.n;
        otherHeap.n = 0;
        otherHeap.trees = [];

        if (!mergedTrees.length) {
            this.minNode = null;
            return;
        }

        // Actual merge (like binary addition)
        let k = 0;
        while (k < mergedTrees.length) {
            if (k + 1 < mergedTrees.length && mergedTrees[k].degree === mergedTrees[k+1].degree) {
                if (k + 2 < mergedTrees.length && 
                    mergedTrees[k+1].degree === mergedTrees[k+2].degree) {
                    // Three trees of same degree, skip first and resolve later
                    this.trees.push(mergedTrees[k]);
                    k++;
                } else {
                    // Merge two trees
                    if (mergedTrees[k].key < mergedTrees[k+1].key) {
                        this.trees.push(this._linkTrees(mergedTrees[k], mergedTrees[k+1]));
                    } else {
                        this.trees.push(this._linkTrees(mergedTrees[k+1], mergedTrees[k]));
                    }
                    k += 2;
                }
            } else {
                this.trees.push(mergedTrees[k]);
                k++;
            }
        }
        
        this._updateMinNode();
    }

    insert(key) {
        const newNode = new BinomialNode(key);
        const tempHeap = new BinomialHeap();
        tempHeap.trees.push(newNode);
        tempHeap.n = 1;
        this.merge(tempHeap);
    }

    findMin() {
        return this.minNode ? this.minNode.key : null;
    }

    extractMin() {
        if (!this.minNode) {
            return null;
        }
        
        const minKey = this.minNode.key;
        
        // Remove minNode from root list
        this.trees = this.trees.filter(tree => tree !== this.minNode);
        
        // Create a new heap from minNode's children
        const minChildrenHeap = new BinomialHeap();
        
        // Reverse the order of children to maintain degree ordering for merge
        let childrenList = [];
        let currentChild = this.minNode.child;
        while (currentChild) {
            const nextChild = currentChild.sibling;
            currentChild.parent = null;
            currentChild.sibling = null;
            childrenList.push(currentChild);
            currentChild = nextChild;
        }
        minChildrenHeap.trees = childrenList.reverse();
        minChildrenHeap.n = minChildrenHeap.trees.reduce((sum, tree) => sum + Math.pow(2, tree.degree), 0);

        // Merge with remaining trees
        this.merge(minChildrenHeap);
        this.n--; // Min node was removed
        this._updateMinNode();
        
        return minKey;
    }

    _updateMinNode() {
        this.minNode = null;
        if (this.trees.length > 0) {
            this.minNode = this.trees[0];
            for (const treeRoot of this.trees) {
                if (treeRoot.key < this.minNode.key) {
                    this.minNode = treeRoot;
                }
            }
        }
    }

    // DecreaseKey is complex and omitted for conceptual simplicity.
}

// const bh = new BinomialHeap();
// bh.insert(10);
// bh.insert(20);
// bh.insert(5);
// bh.insert(3);
// console.log("Min:", bh.findMin()); // Expected: 3
// console.log("Extract Min:", bh.extractMin()); // Expected: 3
// console.log("Min after extract:", bh.findMin()); // Expected: 5
```

### Typescript

```typescript
class BinomialNodeTS {
    public key: number;
    public degree: number;
    public parent: BinomialNodeTS | null;
    public child: BinomialNodeTS | null;    // Pointer to leftmost child
    public sibling: BinomialNodeTS | null;  // Pointer to next sibling

    constructor(key: number) {
        this.key = key;
        this.degree = 0;
        this.parent = null;
        this.child = null;
        this.sibling = null;
    }
}

class BinomialHeapTS {
    public trees: BinomialNodeTS[]; // List of roots of binomial trees
    public minNode: BinomialNodeTS | null;
    public n: number; // Number of nodes

    constructor() {
        this.trees = [];
        this.minNode = null;
        this.n = 0;
    }

    private _linkTrees(h1: BinomialNodeTS, h2: BinomialNodeTS): BinomialNodeTS {
        // Link two binomial trees of the same degree
        // h2 becomes child of h1
        h2.parent = h1;
        h2.sibling = h1.child;
        h1.child = h2;
        h1.degree++;
        return h1;
    }

    public merge(otherHeap: BinomialHeapTS): void {
        let mergedTrees: BinomialNodeTS[] = [];
        let i = 0;
        let j = 0;
        
        // Combine lists of trees, keeping them sorted by degree
        while (i < this.trees.length && j < otherHeap.trees.length) {
            if (this.trees[i].degree < otherHeap.trees[j].degree) {
                mergedTrees.push(this.trees[i]);
                i++;
            } else {
                mergedTrees.push(otherHeap.trees[j]);
                j++;
            }
        }
        mergedTrees.push(...this.trees.slice(i));
        mergedTrees.push(...otherHeap.trees.slice(j));
        
        this.trees = []; // Clear current trees
        this.n += otherHeap.n;
        otherHeap.n = 0;
        otherHeap.trees = [];

        if (!mergedTrees.length) {
            this.minNode = null;
            return;
        }

        // Actual merge (like binary addition)
        let k = 0;
        while (k < mergedTrees.length) {
            if (k + 1 < mergedTrees.length && mergedTrees[k].degree === mergedTrees[k+1].degree) {
                if (k + 2 < mergedTrees.length && 
                    mergedTrees[k+1].degree === mergedTrees[k+2].degree) {
                    // Three trees of same degree, skip first and resolve later
                    this.trees.push(mergedTrees[k]);
                    k++;
                } else {
                    // Merge two trees
                    if (mergedTrees[k].key < mergedTrees[k+1].key) {
                        this.trees.push(this._linkTrees(mergedTrees[k], mergedTrees[k+1]));
                    } else {
                        this.trees.push(this._linkTrees(mergedTrees[k+1], mergedTrees[k]));
                    }
                    k += 2;
                }
            } else {
                this.trees.push(mergedTrees[k]);
                k++;
            }
        }
        
        this._updateMinNode();
    }

    public insert(key: number): void {
        const newNode = new BinomialNodeTS(key);
        const tempHeap = new BinomialHeapTS();
        tempHeap.trees.push(newNode);
        tempHeap.n = 1;
        this.merge(tempHeap);
    }

    public findMin(): number | null {
        return this.minNode ? this.minNode.key : null;
    }

    public extractMin(): number | null {
        if (!this.minNode) {
            return null;
        }
        
        const minKey = this.minNode.key;
        
        // Remove minNode from root list
        this.trees = this.trees.filter(tree => tree !== this.minNode);
        
        // Create a new heap from minNode's children
        const minChildrenHeap = new BinomialHeapTS();
        
        // Reverse the order of children to maintain degree ordering for merge
        let childrenList: BinomialNodeTS[] = [];
        let currentChild = this.minNode.child;
        while (currentChild) {
            const nextChild = currentChild.sibling;
            currentChild.parent = null;
            currentChild.sibling = null;
            childrenList.push(currentChild);
            currentChild = nextChild;
        }
        minChildrenHeap.trees = childrenList.reverse();
        minChildrenHeap.n = minChildrenHeap.trees.reduce((sum, tree) => sum + Math.pow(2, tree.degree), 0);

        // Merge with remaining trees
        this.merge(minChildrenHeap);
        this.n--; // Min node was removed
        this._updateMinNode();
        
        return minKey;
    }

    private _updateMinNode(): void {
        this.minNode = null;
        if (this.trees.length > 0) {
            this.minNode = this.trees[0];
            for (const treeRoot of this.trees) {
                if (treeRoot.key < this.minNode.key) {
                    this.minNode = treeRoot;
                }
            }
        }
    }

    // DecreaseKey is complex and omitted for conceptual simplicity.
}

// const bhTS = new BinomialHeapTS();
// bhTS.insert(10);
// bhTS.insert(20);
// bhTS.insert(5);
// bhTS.insert(3);
// console.log("Min:", bhTS.findMin()); // Expected: 3
// console.log("Extract Min:", bhTS.extractMin()); // Expected: 3
// console.log("Min after extract:", bhTS.findMin()); // Expected: 5
```

### Cpp

```cpp
#include <iostream>
#include <vector>
#include <algorithm> // For std::reverse
#include <limits>    // For std::numeric_limits
#include <numeric>   // For std::accumulate

class BinomialNode {
public:
    int key;
    int degree;
    BinomialNode</em> parent;
    BinomialNode<em> child;    // Pointer to leftmost child
    BinomialNode</em> sibling;  // Pointer to next sibling

    BinomialNode(int k) : key(k), degree(0), parent(nullptr), child(nullptr), sibling(nullptr) {}
};

class BinomialHeap {
public:
    std::vector<BinomialNode<em>> trees; // List of roots of binomial trees
    BinomialNode</em> min_node;
    int n; // Number of nodes

    BinomialHeap() : min_node(nullptr), n(0) {}

    // Helper to link two binomial trees of the same degree
    BinomialNode<em> _link_trees(BinomialNode</em> h1, BinomialNode<em> h2) {
        // Ensure h1->key <= h2->key (min-heap property)
        if (h1->key > h2->key) {
            std::swap(h1, h2);
        }
        h2->parent = h1;
        h2->sibling = h1->child;
        h1->child = h2;
        h1->degree++;
        return h1;
    }

    void merge(BinomialHeap& other_heap) {
        std::vector<BinomialNode</em>> merged_list;
        int i = 0, j = 0;
        
        // Combine lists of trees, keeping them sorted by degree
        while (i < trees.size() && j < other_heap.trees.size()) {
            if (trees[i]->degree < other_heap.trees[j]->degree) {
                merged_list.push_back(trees[i]);
                i++;
            } else {
                merged_list.push_back(other_heap.trees[j]);
                j++;
            }
        }
        // Add remaining trees
        while (i < trees.size()) {
            merged_list.push_back(trees[i]);
            i++;
        }
        while (j < other_heap.trees.size()) {
            merged_list.push_back(other_heap.trees[j]);
            j++;
        }
        
        trees.clear(); // Clear current trees
        n += other_heap.n;
        other_heap.n = 0;
        other_heap.trees.clear();

        if (merged_list.empty()) {
            min_node = nullptr;
            return;
        }

        // Actual merge (like binary addition)
        BinomialNode<em> current_tree = nullptr;
        for (BinomialNode</em> next_tree : merged_list) {
            if (current_tree == nullptr) {
                current_tree = next_tree;
            } else if (current_tree->degree == next_tree->degree) {
                // Check if there's a third tree of same degree
                if (!trees.empty() && trees.back()->degree == current_tree->degree) {
                    trees.push_back(current_tree);
                    current_tree = next_tree;
                } else {
                    current_tree = _link_trees(current_tree, next_tree);
                }
            } else {
                trees.push_back(current_tree);
                current_tree = next_tree;
            }
        }
        if (current_tree) {
            trees.push_back(current_tree);
        }
        
        _update_min_node();
    }

    void insert(int key) {
        BinomialNode<em> newNode = new BinomialNode(key);
        BinomialHeap tempHeap;
        tempHeap.trees.push_back(newNode);
        tempHeap.n = 1;
        merge(tempHeap);
    }

    int findMin() {
        if (!min_node) {
            throw std::runtime_error("Heap is empty");
        }
        return min_node->key;
    }

    int extractMin() {
        if (!min_node) {
            throw std::runtime_error("Heap is empty");
        }
        
        int min_key = min_node->key;
        
        // Remove min_node from root list
        trees.erase(std::remove(trees.begin(), trees.end(), min_node), trees.end());
        
        // Create a new heap from min_node's children
        BinomialHeap minChildrenHeap;
        
        // Collect children and reverse order (for merge)
        std::vector<BinomialNode</em>> children_list;
        BinomialNode<em> current_child = min_node->child;
        while (current_child) {
            BinomialNode</em> next_child = current_child->sibling;
            current_child->parent = nullptr;
            current_child->sibling = nullptr;
            children_list.push_back(current_child);
            current_child = next_child;
        }
        std::reverse(children_list.begin(), children_list.end());
        minChildrenHeap.trees = children_list;
        
        // Merge with remaining trees
        merge(minChildrenHeap);
        n--; // Min node was removed
        _update_min_node();
        
        return min_key;
    }

    void _update_min_node() {
        min_node = nullptr;
        if (!trees.empty()) {
            min_node = trees[0];
            for (BinomialNode<em> tree_root : trees) {
                if (tree_root->key < min_node->key) {
                    min_node = tree_root;
                }
            }
        }
    }
    // DecreaseKey is complex and omitted for conceptual simplicity.
};

// int main() {
//     BinomialHeap bh;
//     bh.insert(10);
//     bh.insert(20);
//     bh.insert(5);
//     bh.insert(3);
//     std::cout << "Min: " << bh.findMin() << std::endl; // Expected: 3
//     std::cout << "Extract Min: " << bh.extractMin() << std::endl; // Expected: 3
//     std::cout << "Min after extract: " << bh.findMin() << std::endl; // Expected: 5
//     return 0;
// }
```

### Go

```go
package main

import (
    "fmt"
    "math"
    "sort"
)

type BinomialNode struct {
    Key    int
    Degree int
    Parent </em>BinomialNode
    Child  <em>BinomialNode   // Pointer to leftmost child
    Sibling </em>BinomialNode   // Pointer to next sibling
}

func NewBinomialNode(key int) <em>BinomialNode {
    return &BinomialNode{Key: key}
}

type BinomialHeap struct {
    Trees   []</em>BinomialNode // List of roots of binomial trees
    MinNode <em>BinomialNode
    N       int // Number of nodes
}

func (bh </em>BinomialHeap) linkTrees(h1, h2 <em>BinomialNode) </em>BinomialNode {
    // Link two binomial trees of the same degree
    // h2 becomes child of h1
    if h1.Key > h2.Key {
        h1, h2 = h2, h1 // Ensure h1.Key <= h2.Key
    }
    h2.Parent = h1
    h2.Sibling = h1.Child
    h1.Child = h2
    h1.Degree++
    return h1
}

func (bh <em>BinomialHeap) Merge(otherHeap </em>BinomialHeap) {
    mergedTrees := []<em>BinomialNode{}
    i, j := 0, 0

    // Combine lists of trees, keeping them sorted by degree
    for i < len(bh.Trees) && j < len(otherHeap.Trees) {
        if bh.Trees[i].Degree < otherHeap.Trees[j].Degree {
            mergedTrees = append(mergedTrees, bh.Trees[i])
            i++
        } else {
            mergedTrees = append(mergedTrees, otherHeap.Trees[j])
            j++
        }
    }
    mergedTrees = append(mergedTrees, bh.Trees[i:]...)
    mergedTrees = append(mergedTrees, otherHeap.Trees[j:]...)

    bh.Trees = []</em>BinomialNode{} // Clear current trees
    bh.N += otherHeap.N
    otherHeap.N = 0
    otherHeap.Trees = []<em>BinomialNode{}

    if len(mergedTrees) == 0 {
        bh.MinNode = nil
        return
    }

    // Actual merge (like binary addition)
    var currentTree </em>BinomialNode
    for _, nextTree := range mergedTrees {
        if currentTree == nil {
            currentTree = nextTree
        } else if currentTree.Degree == nextTree.Degree {
            if len(bh.Trees) > 0 && bh.Trees[len(bh.Trees)-1].Degree == currentTree.Degree {
                // Three trees of same degree, append current and resolve next two
                bh.Trees = append(bh.Trees, currentTree)
                currentTree = nextTree
            } else {
                currentTree = bh.linkTrees(currentTree, nextTree)
            }
        } else {
            bh.Trees = append(bh.Trees, currentTree)
            currentTree = nextTree
        }
    }
    if currentTree != nil {
        bh.Trees = append(bh.Trees, currentTree)
    }

    bh.updateMinNode()
}

func (bh <em>BinomialHeap) Insert(key int) {
    newNode := NewBinomialNode(key)
    tempHeap := &BinomialHeap{}
    tempHeap.Trees = append(tempHeap.Trees, newNode)
    tempHeap.N = 1
    bh.Merge(tempHeap)
}

func (bh </em>BinomialHeap) FindMin() (int, error) {
    if bh.MinNode == nil {
        return 0, fmt.Errorf("heap is empty")
    }
    return bh.MinNode.Key, nil
}

func (bh <em>BinomialHeap) ExtractMin() (int, error) {
    if bh.MinNode == nil {
        return 0, fmt.Errorf("heap is empty")
    }

    minKey := bh.MinNode.Key

    // Remove minNode from root list
    var filteredTrees []</em>BinomialNode
    for _, tree := range bh.Trees {
        if tree != bh.MinNode {
            filteredTrees = append(filteredTrees, tree)
        }
    }
    bh.Trees = filteredTrees

    // Create a new heap from minNode's children
    minChildrenHeap := &BinomialHeap{}

    // Collect children and reverse order to maintain degree ordering for merge
    childrenList := []<em>BinomialNode{}
    currentChild := bh.MinNode.Child
    for currentChild != nil {
        nextChild := currentChild.Sibling
        currentChild.Parent = nil
        currentChild.Sibling = nil
        childrenList = append(childrenList, currentChild)
        currentChild = nextChild
    }
    // Reverse children list
    for i, j := 0, len(childrenList)-1; i < j; i, j = i+1, j-1 {
        childrenList[i], childrenList[j] = childrenList[j], childrenList[i]
    }
    minChildrenHeap.Trees = childrenList

    bh.Merge(minChildrenHeap)
    bh.N-- // Min node was removed
    bh.updateMinNode()

    return minKey, nil
}

func (bh </em>BinomialHeap) updateMinNode() {
    bh.MinNode = nil
    if len(bh.Trees) > 0 {
        bh.MinNode = bh.Trees[0]
        for _, treeRoot := range bh.Trees {
            if treeRoot.Key < bh.MinNode.Key {
                bh.MinNode = treeRoot
            }
        }
    }
}
// DecreaseKey is complex and omitted for conceptual simplicity.

// func main() {
//     bh := &BinomialHeap{}
//     bh.Insert(10)
//     bh.Insert(20)
//     bh.Insert(5)
//     bh.Insert(3)
//     minVal, _ := bh.FindMin()
//     fmt.Println("Min:", minVal) // Expected: 3
//     extracted, _ := bh.ExtractMin()
//     fmt.Println("Extract Min:", extracted) // Expected: 3
//     minVal, _ = bh.FindMin()
//     fmt.Println("Min after extract:", minVal) // Expected: 5
// }
```

### D

```d
import std.stdio;
import std.array;
import std.algorithm; // For std.algorithm.min, std.algorithm.swap
import std.conv; // For to!string
import std.sum; // For sum

class BinomialNode {
    int key;
    int degree;
    BinomialNode parent;
    BinomialNode child;    // Pointer to leftmost child
    BinomialNode sibling;  // Pointer to next sibling

    this(int k) {
        key = k;
        degree = 0;
        parent = null;
        child = null;
        sibling = null;
    }
}

class BinomialHeap {
    BinomialNode[] trees; // List of roots of binomial trees
    BinomialNode min_node;
    int n; // Number of nodes

    this() {
        trees = [];
        min_node = null;
        n = 0;
    }

private:
    BinomialNode linkTrees(BinomialNode h1, BinomialNode h2) {
        // Link two binomial trees of the same degree
        // h2 becomes child of h1
        if (h1.key > h2.key) {
            swap(h1, h2); // Ensure h1.key <= h2.key
        }
        h2.parent = h1;
        h2.sibling = h1.child;
        h1.child = h2;
        h1.degree++;
        return h1;
    }

public:
    void merge(BinomialHeap other_heap) {
        BinomialNode[] merged_trees_list;
        int i = 0, j = 0;
        
        // Combine lists of trees, keeping them sorted by degree
        while (i < trees.length && j < other_heap.trees.length) {
            if (trees[i].degree < other_heap.trees[j].degree) {
                merged_trees_list ~= trees[i];
                i++;
            } else {
                merged_trees_list ~= other_heap.trees[j];
                j++;
            }
        }
        merged_trees_list ~= trees[i..$];
        merged_trees_list ~= other_heap.trees[j..$];
        
        trees = []; // Clear current trees
        n += other_heap.n;
        other_heap.n = 0;
        other_heap.trees = [];

        if (merged_trees_list.empty) {
            min_node = null;
            return;
        }

        // Actual merge (like binary addition)
        BinomialNode current_tree = null;
        foreach (next_tree; merged_trees_list) {
            if (current_tree is null) {
                current_tree = next_tree;
            } else if (current_tree.degree == next_tree.degree) {
                // Check if there's a third tree of same degree
                if (!trees.empty && trees.back.degree == current_tree.degree) {
                    trees ~= current_tree;
                    current_tree = next_tree;
                } else {
                    current_tree = linkTrees(current_tree, next_tree);
                }
            } else {
                trees ~= current_tree;
                current_tree = next_tree;
            }
        }
        if (current_tree !is null) {
            trees ~= current_tree;
        }
        
        _updateMinNode();
    }

    void insert(int key) {
        BinomialNode new_node = new BinomialNode(key);
        BinomialHeap temp_heap = new BinomialHeap();
        temp_heap.trees ~= new_node;
        temp_heap.n = 1;
        this.merge(temp_heap);
    }

    int findMin() {
        if (min_node is null) {
            throw new Exception("Heap is empty");
        }
        return min_node.key;
    }

    int extractMin() {
        if (min_node is null) {
            throw new Exception("Heap is empty");
        }
        
        int min_key = min_node.key;
        
        // Remove min_node from root list
        trees = trees.filter!(t => t !is min_node).array;
        
        // Create a new heap from min_node's children
        BinomialHeap min_children_heap = new BinomialHeap();
        
        // Collect children and reverse order (for merge)
        BinomialNode[] children_list;
        BinomialNode current_child = min_node.child;
        while (current_child !is null) {
            BinomialNode next_child = current_child.sibling;
            current_child.parent = null;
            current_child.sibling = null;
            children_list ~= current_child;
            current_child = next_child;
        }
        min_children_heap.trees = children_list.reverse.array;
        
        // Merge with remaining trees
        merge(min_children_heap);
        n--; // Min node was removed
        _updateMinNode();
        
        return min_key;
    }

private:
    void _updateMinNode() {
        min_node = null;
        if (!trees.empty) {
            min_node = trees[0];
            foreach (tree_root; trees) {
                if (tree_root.key < min_node.key) {
                    min_node = tree_root;
                }
            }
        }
    }
    // DecreaseKey is complex and omitted for conceptual simplicity.

// void main() {
//     auto bh = new BinomialHeap();
//     bh.insert(10);
//     bh.insert(20);
//     bh.insert(5);
//     bh.insert(3);
//     writefln("Min: %s", bh.findMin()); // Expected: 3
//     writefln("Extract Min: %s", bh.extractMin()); // Expected: 3
//     writefln("Min after extract: %s", bh.findMin()); // Expected: 5
// }
}
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

A `Binomial Heap` implementation manages a `list` of `binomial trees`. The complexity comes from the `merge` operation, which acts like binary addition on the `trees`.

---

**`BinomialNode` Class:**
- `key`: The value stored in the `node`.
- `degree`: The `order` of the `binomial tree` rooted at this `node`.
- `parent`: Pointer to the `parent node`.
- `child`: Pointer to the `leftmost child` (`root` of a smaller `binomial tree`).
- `sibling`: Pointer to the next `sibling node` (`root` of a `binomial tree` of a different `order`).

**`BinomialHeap` Class:**
- `trees`: A `list`/`vector`/`array` of `BinomialNode`s, representing the `roots` of the `binomial trees` in the `heap`. These are typically stored in increasing `order` of `degree`.
- `min_node`: A pointer to the `root node` containing the minimum `key` in the entire `heap`.
- `n`: The total number of `nodes` in the `heap`.
- **`_link_trees(h1, h2)`:** A helper function to link two `binomial trees` of the same `degree`. It assumes `h1.key <= h2.key` and makes `h2` the `leftmost child` of `h1`.
- **`merge(other_heap)`:** The core operation. It combines the `lists` of `binomial trees` from the current `heap` and `other_heap` into a single `list`, similar to how binary numbers are added. If two `trees` of the same `degree` are encountered, they are linked using `_link_trees` to form a `tree` of the next higher `degree`, and the process continues.
- **`insert(key)`:** Creates a new `B0` (order 0) `binomial tree` with the new `key` and `merges` it with the existing `heap`.
- **`find_min()`:** Returns the `key` of the `min_node`. Requires `min_node` to be updated correctly.
- **`extract_min()`:**
- Removes the `min_node` from its `binomial tree`.
- Its children form a new `Binomial Heap` (after reversing their order to ensure correct merging by `degree`).
- This new `heap` is then `merged` with the remaining `trees` from the original `heap`.

    </li>
- **`_update_min_node()`:** A helper to scan the `roots` of all `binomial trees` to find the new `min_node`.

[Back to Implementation](#implementation)

## Applications

### Application

Binomial Heaps are a type of mergeable `priority queue`, similar to `Fibonacci Heaps` and `Pairing Heaps`. They are particularly useful in situations where efficient merging of heaps is a frequent operation.
- **Graph Algorithms:** Used in implementations of `Dijkstra's algorithm` and `Prim's algorithm` where `priority queues` are needed. While `Fibonacci Heaps` offer theoretically better asymptotic bounds, `Binomial Heaps` can be competitive or better in practice for some workloads.
- **Network Routing:** Managing packet queues with different priorities, especially in complex network topologies where queues might need to be combined.
- **Event Simulation:** Handling events in discrete event simulations where event lists may need to be merged.
- **Operating Systems:** In task scheduling where processes are queued by priority, and new process queues might arise and need to be integrated.

