---
title: "B-Tree"
---

A `B-Tree` is a self-balancing tree data structure that maintains sorted data and allows searches, sequential access, insertions, and deletions in logarithmic time. It is specifically designed for disk-based storage systems, where accessing data from disk is much slower than accessing data from main memory.

The primary goal of a `B-Tree` is to reduce the number of disk I/O operations by ensuring that related data is stored close together on disk, allowing large blocks of data to be read efficiently.

## How it Works

### How it Works (Expanded)

Unlike `binary search trees`, `B-Trees` can have many children per `node`. Each `node` can hold a large number of `keys` and pointers to children, chosen to match the size of a disk block.

---

Example B-Tree (Order M=3, max 2 keys per node, max 3 children per node)

              [ 50, 80 ]
             /    |     \
            /     |      \
       [20,30] [60,70] [90,100]
       / | \   / | \   / | \
      L  M  R L  M  R L  M  R (Leaf nodes with data)

Key Properties:
- All leaves are at the same level.
- A node with K keys has K+1 children.
- All keys within a node are sorted.
- All keys in a child subtree are between the parent keys defining that subtree's range.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
# Conceptual B-Tree implementation (simplified, as full B-Trees are complex)
# This example illustrates the structure and basic search idea.

class BTreeNode:
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.keys = [] # List of keys
        self.children = [] # List of BTreeNodes (children)

class BTree:
    def __init__(self, t): # t is minimum degree (t-1 keys, t children)
        self.root = BTreeNode(leaf=True)
        self.t = t # Minimum degree

    # Simplified search: returns (node, index) if key found
    def search(self, x, k): # x is node, k is key
        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i += 1
        
        if i < len(x.keys) and k == x.keys[i]:
            return x, i # Found
        elif x.leaf:
            return None # Not found
        else:
            # In a real B-Tree, we'd fetch x.children[i] from disk
            return self.search(x.children[i], k)

    # Simplified insert: Assumes root is never full (in real B-Tree, root splits)
    # Full insertion logic is extensive.
    def insert(self, k):
        r = self.root
        if len(r.keys) == (2 <em> self.t) - 1: # Root is full
            s = BTreeNode()
            self.root = s
            s.leaf = False
            s.children.append(r)
            self._split_child(s, 0, r)
            self._insert_non_full(s, k)
        else:
            self._insert_non_full(r, k)

    def _insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(0) # Placeholder
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            # In real B-Tree, read x.children[i] from disk
            if len(x.children[i].keys) == (2 </em> self.t) - 1: # Child is full
                self._split_child(x, i, x.children[i])
                if k > x.keys[i]:
                    i += 1
            self._insert_non_full(x.children[i], k)

    def _split_child(self, x, i, y):
        z = BTreeNode(leaf=y.leaf)
        x.keys.insert(i, y.keys[self.t - 1])
        x.children.insert(i + 1, z)
        z.keys = y.keys[self.t:]
        y.keys = y.keys[:self.t - 1]
        if not y.leaf:
            z.children = y.children[self.t:]
            y.children = y.children[:self.t]

# Example Usage (conceptual, insertion is not fully working here without full split/merge)
# b_tree = BTree(t=2) # A 2-3 tree
# b_tree.insert(10)
# b_tree.insert(20)
# b_tree.insert(5)
# b_tree.insert(30)
# print(b_tree.search(b_tree.root, 20)) # Expected: (node_with_20, 0)
```

### Javascript

```javascript
// Conceptual B-Tree implementation in JavaScript (simplified)
// Full B-Tree implementation is extensive and typically involves disk I/O simulation.

class BTreeNode {
    constructor(leaf = true) {
        this.leaf = leaf;
        this.keys = []; // Array of keys
        this.children = []; // Array of BTreeNodes (children)
    }
}

class BTree {
    constructor(t) { // t is minimum degree (t-1 keys, t children)
        this.root = new BTreeNode(true);
        this.t = t; // Minimum degree
    }

    // Simplified search
    search(x, k) { // x is node, k is key
        let i = 0;
        while (i < x.keys.length && k > x.keys[i]) {
            i++;
        }

        if (i < x.keys.length && k === x.keys[i]) {
            return { node: x, index: i }; // Found
        } else if (x.leaf) {
            return null; // Not found
        } else {
            // In a real B-Tree, we'd simulate fetching x.children[i] from disk
            return this.search(x.children[i], k);
        }
    }

    // Simplified insert: assumes root is not full initially.
    // Full insertion logic is extensive.
    insert(k) {
        let r = this.root;
        if (r.keys.length === (2 <em> this.t) - 1) { // Root is full
            let s = new BTreeNode(false); // New root
            this.root = s;
            s.children.push(r);
            this._splitChild(s, 0, r);
            this._insertNonFull(s, k);
        } else {
            this._insertNonFull(r, k);
        }
    }

    _insertNonFull(x, k) {
        let i = x.keys.length - 1;
        if (x.leaf) {
            x.keys.splice(i + 1, 0, k); // Insert k at correct position
        } else {
            while (i >= 0 && k < x.keys[i]) {
                i--;
            }
            i++;
            // In real B-Tree, simulate disk read of x.children[i]
            if (x.children[i].keys.length === (2 </em> this.t) - 1) { // Child is full
                this._splitChild(x, i, x.children[i]);
                if (k > x.keys[i]) {
                    i++;
                }
            }
            this._insertNonFull(x.children[i], k);
        }
    }

    _splitChild(x, i, y) {
        let z = new BTreeNode(y.leaf);
        x.keys.splice(i, 0, y.keys[this.t - 1]); // Push median up to parent
        x.children.splice(i + 1, 0, z); // Add new child to parent

        z.keys = y.keys.splice(this.t); // Move t to 2t-1 keys from y to z
        y.keys.splice(this.t - 1);     // Remove keys from y

        if (!y.leaf) {
            z.children = y.children.splice(this.t); // Move children from y to z
        }
    }
}
```

### Cpp

```cpp
#include <iostream>
#include <vector>
#include <algorithm> // For std::sort

// A BTreeNode represents a single node in the B-tree
class BTreeNode {
public:
    std::vector<int> keys;     // Keys stored in this node
    std::vector<BTreeNode<em>> children; // Pointers to child nodes
    bool leaf;                  // Is true when node is leaf. Otherwise false
    int t;                      // Minimum degree (defines range for number of keys)

    BTreeNode(int t_val, bool leaf_val) : t(t_val), leaf(leaf_val) {}

    // Function to search key k in this node
    // Returns index of the first key greater than or equal to k
    int findKey(int k) {
        int idx = 0;
        while (idx < keys.size() && keys[idx] < k) {
            ++idx;
        }
        return idx;
    }

    // Function to insert a new key in the subtree rooted with this node
    void insertNonFull(int k) {
        int i = keys.size() - 1;

        if (leaf) {
            keys.push_back(0); // Make space for new key
            while (i >= 0 && keys[i] > k) {
                keys[i + 1] = keys[i];
                i--;
            }
            keys[i + 1] = k;
        } else {
            // Find child where new key is to be inserted
            while (i >= 0 && keys[i] > k) {
                i--;
            }
            i++;
            // In real B-Tree, read children[i] from disk
            if (children[i]->keys.size() == 2 </em> t - 1) { // Child is full
                splitChild(i, children[i]);
                if (keys[i] < k) {
                    i++;
                }
            }
            children[i]->insertNonFull(k);
        }
    }

    // Function to split the child y of this node x. i is index of y in children[].
    void splitChild(int i, BTreeNode<em> y) {
        // Create a new node which is going to store (t-1) keys of y
        BTreeNode</em> z = new BTreeNode(y->t, y->leaf);
        
        // Copy the last (t-1) keys of y to z
        for (int j = 0; j < t - 1; j++) {
            z->keys.push_back(y->keys[j + t]);
        }
        
        // If y is not leaf, copy the last t children of y to z
        if (!y->leaf) {
            for (int j = 0; j < t; j++) {
                z->children.push_back(y->children[j + t]);
            }
        }
        
        // Remove the last (t) keys from y
        y->keys.resize(t - 1);
        
        // Insert key from y to x
        keys.insert(keys.begin() + i, y->keys[t - 1]);
        
        // Insert new child z into x
        children.insert(children.begin() + i + 1, z);
    }
};

class BTree {
public:
    BTreeNode<em> root;
    int t; // Minimum degree

    BTree(int t_val) : t(t_val) {
        root = new BTreeNode(t, true); // New B-tree is empty, root is leaf
    }

    // Function to search key in the B-tree
    BTreeNode</em> search(BTreeNode<em> x, int k) { // x is node, k is key
        int i = 0;
        while (i < x->keys.size() && k > x->keys[i]) {
            i++;
        }
        if (i < x->keys.size() && k == x->keys[i]) {
            return x; // Found
        }
        if (x->leaf) {
            return nullptr; // Not found
        }
        // In a real B-Tree, we'd fetch x->children[i] from disk
        return search(x->children[i], k);
    }

    void insert(int k) {
        BTreeNode</em> r = root;
        if (r->keys.size() == 2 <em> t - 1) { // Root is full
            BTreeNode</em> s = new BTreeNode(t, false);
            s->children.push_back(root);
            s->splitChild(0, r);
            int i = 0;
            if (s->keys[0] < k) {
                i++;
            }
            s->children[i]->insertNonFull(k);
            root = s;
        } else {
            r->insertNonFull(k);
        }
    }

    void traverse() {
        if (root != nullptr) {
            traverseRecursive(root);
            std::cout << std::endl;
        }
    }
    void traverseRecursive(BTreeNode* x) {
        for (int i = 0; i < x->keys.size(); ++i) {
            if (!x->leaf) {
                traverseRecursive(x->children[i]);
            }
            std::cout << x->keys[i] << " ";
        }
        if (x->leaf) {
            return;
        }
        traverseRecursive(x->children[x->keys.size()]);
    }

    ~BTree() {
        // Proper memory deallocation for a tree is complex
        // For simplicity in this conceptual demo, it's omitted
        // In real code, children should be deleted recursively
        delete root;
    }
};
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

Implementing a full, production-ready `B-Tree` is a significant task due to its disk-oriented nature and complex `insert`/`delete`/`split`/`merge` operations. The provided code is a conceptual illustration of its structure and the `search` operation.

---

**`BTreeNode` Class:** Represents a single `node` in the `B-Tree`.
- `keys`: A sorted `list`/`vector` of `keys` stored in this `node`.
- `children`: A `list`/`vector` of pointers to child `BTreeNode`s. A `node` with `K keys` has `K+1 children`.
- `leaf`: A boolean flag indicating if this is a `leaf node` (which holds the actual data) or an internal `node`.
- `t`: The minimum degree of the `B-Tree`, defining the minimum and maximum number of `keys` and `children` a `node` can have (e.g., `t-1` to `2t-1 keys`, `t` to `2t children`).
- **`findKey(k)`:** A helper function to find the appropriate position for a `key` within the `node`'s `keys`.
- **`insertNonFull(k)`:** A recursive helper for `inserting` a `key` into a `node` that is not full. It traverses to the correct `leaf`, or recursively calls itself on the appropriate child. If a child is full, it calls `splitChild`.
- **`splitChild(i, y)`:** Splits a full child `node` `y` (at `index` `i`) into two `nodes`, and moves the median `key` up to the parent `node`.

**`BTree` Class:**
- `root`: A pointer to the `root BTreeNode`.
- `t`: The minimum degree for the entire `B-Tree`.
- **`search(x, k)`:** Recursively traverses the `tree` to find a `key` `k` starting from `node x`. It efficiently determines which child `node` to descend into based on the `keys` within the current `node`.
- **`insert(k)`:** The main `insert` method. If the `root` is full, it creates a new `root` and splits the old `root`. Otherwise, it calls `_insertNonFull`.

[Back to Implementation](#implementation)

## Applications

### Application

B-Trees are the de facto standard for indexing in most relational databases (like **MySQL**, **PostgreSQL**, **Oracle**) and filesystems (like **NTFS** and **HFS+**). Their high fanout (many children per node) and self-balancing nature result in very shallow trees, which is crucial for minimizing slow disk I/O operations. When you run a query with a `WHERE` clause on an indexed column in a database, a B-Tree is almost certainly being used to find the data records efficiently.

