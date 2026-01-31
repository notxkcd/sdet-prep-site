---
title: "B+ Tree"
---

A `B+ Tree` is a tree data structure that is a variation of the `B-Tree`, primarily optimized for efficient retrieval of records in `block-oriented storage` (like disk or flash memory). Its key distinction is that all data records (or pointers to them) are stored only in the `leaf nodes`, and these `leaf nodes` are linked together to form a sequential `list`.

This structure makes `B+ Trees` exceptionally good for `range queries` and for providing fast sequential access to records, which is crucial for `database systems` and `file systems`.

## How it Works

### How it Works (Expanded)

The differences between a `B-Tree` and a `B+ Tree` are subtle but significant for performance in `disk-based storage`:

---

Conceptual B+ Tree (Order M=3, max 2 keys per node, max 3 children)

          Internal Node (index keys only)
              [ 50, 80 ]
             /    |     \
            /     |      \
       [20,30] [60,70] [90,100]
       / | \   / | \   / | \
      /  |  \ /  |  \ /  |  \
     V   V   V   V   V   V   V
     [Leaf Node 1]<->[Leaf Node 2]<->[Leaf Node 3] ... (Actual data/records)
     (20,data)(30,data) (50,data)(60,data) (80,data)(90,data)

## Implementation {#implementation}

### Python

```python
# Conceptual B+ Tree in Python (simplified, full implementation is very complex and disk-oriented)
# This focuses on the structural differences from a B-Tree: data only in leaves.

class BPlusTreeNode:
    def __init__(self, is_leaf=True, order=3):
        self.is_leaf = is_leaf
        self.keys = [] # Keys (for indexing in internal nodes, for data in leaf nodes)
        self.children = [] # Pointers to child BPlusTreeNodes (internal nodes only)
        self.next_leaf = None # Pointer to next leaf node (leaf nodes only)
        self.parent = None # Parent pointer (optional, but simplifies implementation)
        self.order = order # Minimum degree

# Conceptual B+ Tree class
class BPlusTree:
    def __init__(self, order=3):
        self.order = order # Max children (order)
        self.root = BPlusTreeNode(is_leaf=True, order=order)

    def _find_leaf(self, key):
        current = self.root
        while not current.is_leaf:
            # Find the appropriate child to descend into
            idx = 0
            while idx < len(current.keys) and key >= current.keys[idx]:
                idx += 1
            current = current.children[idx]
        return current

    def insert(self, key, data_payload):
        leaf = self._find_leaf(key)
        # Simplified insert: Assumes no splitting or rebalancing for conceptual demo.
        # In a real B+Tree, you insert, then check for overflow, split node, and propagate.
        
        # Insert key and data into leaf (conceptually)
        inserted = False
        for i in range(len(leaf.keys)):
            if key < leaf.keys[i]:
                leaf.keys.insert(i, key)
                # Assume data_payload inserted here as well
                inserted = True
                break
        if not inserted:
            leaf.keys.append(key)
            # Assume data_payload appended here as well
        
        # print(f"Inserted {key} into leaf. Leaf keys: {leaf.keys}")
        
        # Full insert would handle splits, promoting keys, and linking leaves.
        # This is where complexity arises.

    def search(self, key):
        leaf = self._find_leaf(key)
        # Search linearly in the leaf for the key
        for k in leaf.keys:
            if k == key:
                # In real B+Tree, return data_payload associated with key
                return f"Found key {key} with associated data"
        return f"Key {key} not found"

    def range_query(self, start_key, end_key):
        # Find the starting leaf
        current_leaf = self._find_leaf(start_key)
        results = []
        
        while current_leaf is not None:
            for key_in_leaf in current_leaf.keys:
                if key_in_leaf >= start_key and key_in_leaf <= end_key:
                    results.append(key_in_leaf)
                elif key_in_leaf > end_key: # Optimization: keys are sorted
                    return results # Range exceeded
            
            # Move to next leaf (via linked list)
            current_leaf = current_leaf.next_leaf
            # Stop if the next leaf is outside the range (e.g., its first key is > end_key)
            if current_leaf and current_leaf.keys and current_leaf.keys[0] > end_key:
                break
        return results

# Example Usage:
# bp_tree = BPlusTree(order=3) # Max 2 keys, 3 children
# keys_data = [(10, "data10"), (20, "data20"), (5, "data5"), (30, "data30"), (15, "data15")]
# for k, d in keys_data:
#     bp_tree.insert(k, d) # Conceptual insert

# print(bp_tree.search(20))
# print(bp_tree.search(25))
# print("Range query [10, 25]:", bp_tree.range_query(10, 25))
```

### Javascript

```javascript
// Conceptual B+ Tree in JavaScript (simplified, full implementation is very complex)
// Focuses on structural differences: data only in leaves, linked leaves.

class BPlusTreeNode {
    constructor(isLeaf = true, order = 3) {
        this.isLeaf = isLeaf;
        this.keys = []; // Keys (for indexing in internal nodes, for data in leaf nodes)
        this.children = []; // Pointers to child BPlusTreeNodes (internal nodes only)
        this.nextLeaf = null; // Pointer to next leaf node (leaf nodes only)
        this.parent = null; // Parent pointer (optional)
        this.order = order;
    }
}

class BPlusTree {
    constructor(order = 3) {
        this.order = order;
        this.root = new BPlusTreeNode(true, order);
    }

    _findLeaf(key) {
        let current = this.root;
        while (!current.isLeaf) {
            let idx = 0;
            while (idx < current.keys.length && key >= current.keys[idx]) {
                idx++;
            }
            current = current.children[idx];
        }
        return current;
    }

    insert(key, dataPayload) {
        let leaf = this._findLeaf(key);
        // Simplified insert: no splitting or rebalancing for conceptual demo.
        // In a real B+Tree, you insert, then check for overflow, split node, and propagate.
        
        // Insert key and data into leaf (conceptually)
        let inserted = false;
        for (let i = 0; i < leaf.keys.length; i++) {
            if (key < leaf.keys[i]) {
                leaf.keys.splice(i, 0, key);
                // Assume dataPayload inserted here as well
                inserted = true;
                break;
            }
        }
        if (!inserted) {
            leaf.keys.push(key);
            // Assume dataPayload appended here as well
        }
        // console.log(<code>Inserted ${key} into leaf. Leaf keys: ${leaf.keys}</code>);
    }

    search(key) {
        let leaf = this._findLeaf(key);
        for (const k of leaf.keys) {
            if (k === key) {
                return <code>Found key ${key} with associated data</code>;
            }
        }
        return <code>Key ${key} not found</code>;
    }

    rangeQuery(startKey, endKey) {
        let currentLeaf = this._findLeaf(startKey);
        const results = [];
        
        while (currentLeaf !== null) {
            for (const keyInLeaf of currentLeaf.keys) {
                if (keyInLeaf >= startKey && keyInLeaf <= endKey) {
                    results.push(keyInLeaf);
                } else if (keyInLeaf > endKey) {
                    return results; // Range exceeded
                }
            }
            currentLeaf = currentLeaf.nextLeaf;
            // Stop if next leaf is outside the range
            if (currentLeaf && currentLeaf.keys.length > 0 && currentLeaf.keys[0] > endKey) {
                break;
            }
        }
        return results;
    }
}

// const bpTree = new BPlusTree(3); // Max 2 keys, 3 children
// const keysData = [[10, "data10"], [20, "data20"], [5, "data5"], [30, "data30"], [15, "data15"]];
// for (const [k, d] of keysData) {
//     bpTree.insert(k, d);
// }

// console.log(bpTree.search(20));
// console.log(bpTree.search(25));
// console.log("Range query [10, 25]:", bpTree.rangeQuery(10, 25));
```

### Typescript

```typescript
// Conceptual B+ Tree in TypeScript (simplified)

class BPlusTreeNodeTS {
    public isLeaf: boolean;
    public keys: number[];
    public children: BPlusTreeNodeTS[];
    public nextLeaf: BPlusTreeNodeTS | null;
    public parent: BPlusTreeNodeTS | null;
    public order: number;

    constructor(isLeaf: boolean = true, order: number = 3) {
        this.isLeaf = isLeaf;
        this.keys = [];
        this.children = [];
        this.nextLeaf = null;
        this.parent = null;
        this.order = order;
    }
}

class BPlusTreeTS {
    public root: BPlusTreeNodeTS;
    public order: number;

    constructor(order: number = 3) {
        this.order = order;
        this.root = new BPlusTreeNodeTS(true, order);
    }

    private _findLeaf(key: number): BPlusTreeNodeTS {
        let current: BPlusTreeNodeTS = this.root;
        while (!current.isLeaf) {
            let idx = 0;
            while (idx < current.keys.length && key >= current.keys[idx]) {
                idx++;
            }
            current = current.children[idx];
        }
        return current;
    }

    public insert(key: number, dataPayload: any): void {
        let leaf = this._findLeaf(key);
        // Simplified insert: no splitting or rebalancing for conceptual demo.
        
        let inserted = false;
        for (let i = 0; i < leaf.keys.length; i++) {
            if (key < leaf.keys[i]) {
                leaf.keys.splice(i, 0, key);
                // Assume dataPayload associated with key is inserted here as well
                inserted = true;
                break;
            }
        }
        if (!inserted) {
            leaf.keys.push(key);
            // Assume dataPayload appended here as well
        }
    }

    public search(key: number): string {
        let leaf = this._findLeaf(key);
        for (const k of leaf.keys) {
            if (k === key) {
                return <code>Found key ${key} with associated data</code>;
            }
        }
        return <code>Key ${key} not found</code>;
    }

    public rangeQuery(startKey: number, endKey: number): number[] {
        let currentLeaf: BPlusTreeNodeTS | null = this._findLeaf(startKey);
        const results: number[] = [];
        
        while (currentLeaf !== null) {
            for (const keyInLeaf of currentLeaf.keys) {
                if (keyInLeaf >= startKey && keyInLeaf <= endKey) {
                    results.push(keyInLeaf);
                } else if (keyInLeaf > endKey) {
                    return results;
                }
            }
            currentLeaf = currentLeaf.nextLeaf;
            if (currentLeaf && currentLeaf.keys.length > 0 && currentLeaf.keys[0] > endKey) {
                break;
            }
        }
        return results;
    }
}

// const bpTreeTS = new BPlusTreeTS(3);
// const keysDataTS: [number, any][] = [[10, "data10"], [20, "data20"], [5, "data5"], [30, "data30"], [15, "data15"]];
// for (const [k, d] of keysDataTS) {
//     bpTreeTS.insert(k, d);
// }

// console.log(bpTreeTS.search(20));
// console.log(bpTreeTS.search(25));
// console.log("Range query [10, 25]:", bpTreeTS.rangeQuery(10, 25));
```

### Cpp

```cpp
#include <iostream>
#include <vector>
#include <algorithm> // For std::lower_bound

// Conceptual B+ Tree Node (simplified)
class BPlusTreeNode {
public:
    std::vector<int> keys;     // Keys
    std::vector<BPlusTreeNode<em>> children; // Pointers to child nodes (internal nodes)
    std::vector<std::string> data_payloads; // Data associated with keys (leaf nodes only)
    BPlusTreeNode</em> next_leaf;  // Pointer to next leaf node (leaf nodes only)
    bool is_leaf;
    int order; // Maximum children (also max keys + 1 in internal nodes)

    BPlusTreeNode(bool leaf_node = true, int t_order = 3) :
        is_leaf(leaf_node), order(t_order), next_leaf(nullptr) {}

    // For simplicity, no explicit destructor in this conceptual example. 
    // In a real implementation, children should be deleted recursively.
};

// Conceptual B+ Tree
class BPlusTree {
public:
    BPlusTreeNode<em> root;
    int order; // Maximum children (also max keys + 1 in internal nodes)

    BPlusTree(int t_order = 3) : order(t_order) {
        root = new BPlusTreeNode(true, order); // Root is initially a leaf
    }
    // For simplicity, no explicit destructor.

private:
    BPlusTreeNode</em> findLeaf(int key) {
        BPlusTreeNode<em> current = root;
        while (!current->is_leaf) {
            auto it = std::lower_bound(current->keys.begin(), current->keys.end(), key);
            int idx = std::distance(current->keys.begin(), it);
            current = current->children[idx];
        }
        return current;
    }

public:
    void insert(int key, const std::string& data_payload) {
        BPlusTreeNode</em> leaf = findLeaf(key);
        
        // Simplified insert: no splitting or rebalancing for conceptual demo.
        // In a real B+Tree, you insert, then check for overflow, split node, and propagate.

        auto it_key = std::lower_bound(leaf->keys.begin(), leaf->keys.end(), key);
        int idx = std::distance(leaf->keys.begin(), it_key);
        
        // Assuming no duplicate keys for simplicity, or handling them by overwriting
        if (it_key != leaf->keys.end() && <em>it_key == key) {
            // Key already exists, update data
            leaf->data_payloads[idx] = data_payload;
        } else {
            leaf->keys.insert(it_key, key);
            leaf->data_payloads.insert(leaf->data_payloads.begin() + idx, data_payload);
        }
        // Full insert would handle splits, promoting keys, and linking leaves.
    }

    std::string search(int key) {
        BPlusTreeNode</em> leaf = findLeaf(key);
        auto it_key = std::lower_bound(leaf->keys.begin(), leaf->keys.end(), key);
        
        if (it_key != leaf->keys.end() && <em>it_key == key) {
            int idx = std::distance(leaf->keys.begin(), it_key);
            return "Found key " + std::to_string(key) + " with associated data: " + leaf->data_payloads[idx];
        }
        return "Key " + std::to_string(key) + " not found";
    }

    std::vector<std::string> rangeQuery(int start_key, int end_key) {
        BPlusTreeNode</em> current_leaf = findLeaf(start_key);
        std::vector<std::string> results;
        
        while (current_leaf != nullptr) {
            for (size_t i = 0; i < current_leaf->keys.size(); ++i) {
                if (current_leaf->keys[i] >= start_key && current_leaf->keys[i] <= end_key) {
                    results.push_back(current_leaf->data_payloads[i]);
                } else if (current_leaf->keys[i] > end_key) {
                    return results; // Range exceeded
                }
            }
            current_leaf = current_leaf->next_leaf;
            // Stop if the next leaf's first key is already out of range
            if (current_leaf && !current_leaf->keys.empty() && current_leaf->keys[0] > end_key) {
                break;
            }
        }
        return results;
    }
};

// int main() {
//     BPlusTree bp_tree(3);
//     bp_tree.insert(10, "data10");
//     bp_tree.insert(20, "data20");
//     bp_tree.insert(5, "data5");
//     bp_tree.insert(30, "data30");
//     bp_tree.insert(15, "data15");

//     std::cout << bp_tree.search(20) << std::endl;
//     std::cout << bp_tree.search(25) << std::endl;
//     
//     std::cout << "Range query [10, 25]:" << std::endl;
//     std::vector<std::string> range_results = bp_tree.rangeQuery(10, 25);
//     for(const auto& data : range_results) {
//         std::cout << "- " << data << std::endl;
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
)

// Conceptual BPlus Tree Node (simplified)
type BPlusTreeNode struct {
    IsLeaf       bool
    Keys         []int
    Children     []<em>BPlusTreeNode // Pointers to child BPlusTreeNodes (internal nodes)
    DataPayloads []string         // Data associated with keys (leaf nodes only)
    NextLeaf     </em>BPlusTreeNode   // Pointer to next leaf node (leaf nodes only)
    Parent       <em>BPlusTreeNode   // Parent pointer (optional)
    Order        int              // Maximum children (also max keys + 1 in internal nodes)
}

func NewBPlusTreeNode(isLeaf bool, order int) </em>BPlusTreeNode {
    return &BPlusTreeNode{
        IsLeaf:       isLeaf,
        Keys:         []int{},
        Children:     []<em>BPlusTreeNode{},
        DataPayloads: []string{},
        Order:        order,
    }
}

// Conceptual BPlus Tree
type BPlusTree struct {
    Root  </em>BPlusTreeNode
    Order int // Maximum children (also max keys + 1 in internal nodes)
}

func NewBPlusTree(order int) <em>BPlusTree {
    return &BPlusTree{
        Order: order,
        Root:  NewBPlusTreeNode(true, order), // Root is initially a leaf
    }
}

func (bpt </em>BPlusTree) findLeaf(key int) <em>BPlusTreeNode {
    current := bpt.Root
    for !current.IsLeaf {
        idx := sort.SearchInts(current.Keys, key)
        current = current.Children[idx]
    }
    return current
}

func (bpt </em>BPlusTree) Insert(key int, dataPayload string) {
    leaf := bpt.findLeaf(key)

    // Simplified insert: no splitting or rebalancing for conceptual demo.
    // In a real B+Tree, you insert, then check for overflow, split node, and propagate.

    // Find insertion point
    idx := sort.SearchInts(leaf.Keys, key)

    if idx < len(leaf.Keys) && leaf.Keys[idx] == key {
        // Key already exists, update data
        leaf.DataPayloads[idx] = dataPayload
    } else {
        // Insert new key and data
        leaf.Keys = append(leaf.Keys[:idx], append([]int{key}, leaf.Keys[idx:]...)...)
        leaf.DataPayloads = append(leaf.DataPayloads[:idx], append([]string{dataPayload}, leaf.DataPayloads[idx:]...)...)
    }
    // Full insert would handle splits, promoting keys, and linking leaves.
}

func (bpt <em>BPlusTree) Search(key int) string {
    leaf := bpt.findLeaf(key)
    idx := sort.SearchInts(leaf.Keys, key)

    if idx < len(leaf.Keys) && leaf.Keys[idx] == key {
        return fmt.Sprintf("Found key %d with associated data: %s", key, leaf.DataPayloads[idx])
    }
    return fmt.Sprintf("Key %d not found", key)
}

func (bpt </em>BPlusTree) RangeQuery(startKey, endKey int) []string {
    currentLeaf := bpt.findLeaf(startKey)
    var results []string

    for currentLeaf != nil {
        for i, keyInLeaf := range currentLeaf.Keys {
            if keyInLeaf >= startKey && keyInLeaf <= endKey {
                results = append(results, currentLeaf.DataPayloads[i])
            } else if keyInLeaf > endKey {
                return results // Range exceeded
            }
        }
        currentLeaf = currentLeaf.NextLeaf
        // Stop if the next leaf's first key is already out of range
        if currentLeaf != nil && len(currentLeaf.Keys) > 0 && currentLeaf.Keys[0] > endKey {
            break
        }
    }
    return results
}

// func main() {
//     bpTree := NewBPlusTree(3)
//     bpTree.Insert(10, "data10")
//     bpTree.Insert(20, "data20")
//     bpTree.Insert(5, "data5")
//     bpTree.Insert(30, "data30")
//     bpTree.Insert(15, "data15")

//     fmt.Println(bpTree.Search(20))
//     fmt.Println(bpTree.Search(25))

//     fmt.Println("Range query [10, 25]:")
//     rangeResults := bpTree.RangeQuery(10, 25)
//     for _, data := range rangeResults {
//         fmt.Printf("- %s\n", data)
//     }
// }
```

### D

```d
import std.stdio;
import std.array;
import std.algorithm;
import std.string;
import std.conv;

// Conceptual B+ Tree Node (simplified)
class BPlusTreeNode {
    bool is_leaf;
    int[] keys;     // Keys
    BPlusTreeNode[] children; // Pointers to child BPlusTreeNodes (internal nodes)
    string[] data_payloads; // Data associated with keys (leaf nodes only)
    BPlusTreeNode next_leaf;  // Pointer to next leaf node (leaf nodes only)
    int order; // Maximum children (also max keys + 1 in internal nodes)

    this(bool leaf_node = true, int t_order = 3) {
        is_leaf = leaf_node;
        order = t_order;
        keys = [];
        children = [];
        data_payloads = [];
        next_leaf = null;
    }
    // Deallocation managed by GC, no explicit destructor needed for this example.
}

// Conceptual B+ Tree
class BPlusTree {
    BPlusTreeNode root;
    int order; // Maximum children (also max keys + 1 in internal nodes)

    this(int t_order = 3) {
        order = t_order;
        root = new BPlusTreeNode(true, order); // Root is initially a leaf
    }

private:
    BPlusTreeNode findLeaf(int key) {
        BPlusTreeNode current = root;
        while (!current.is_leaf) {
            int idx = lowerBound(current.keys, key) - current.keys.ptr;
            current = current.children[idx];
        }
        return current;
    }

public:
    void insert(int key, string data_payload) {
        BPlusTreeNode leaf = findLeaf(key);
        
        // Simplified insert: no splitting or rebalancing for conceptual demo.

        auto it_key = lowerBound(leaf.keys, key);
        int idx = cast(int)(it_key - leaf.keys.ptr);
        
        if (idx < leaf.keys.length && leaf.keys[idx] == key) {
            // Key already exists, update data
            leaf.data_payloads[idx] = data_payload;
        } else {
            leaf.keys.insert(idx, key);
            leaf.data_payloads.insert(idx, data_payload);
        }
        // Full insert would handle splits, promoting keys, and linking leaves.
    }

    string search(int key) {
        BPlusTreeNode leaf = findLeaf(key);
        auto it_key = lowerBound(leaf.keys, key);
        
        if (it_key < leaf.keys.ptr + leaf.keys.length && *it_key == key) {
            int idx = cast(int)(it_key - leaf.keys.ptr);
            return "Found key " ~ key.to!string ~ " with associated data: " ~ leaf.data_payloads[idx];
        }
        return "Key " ~ key.to!string ~ " not found";
    }

    string[] rangeQuery(int start_key, int end_key) {
        BPlusTreeNode current_leaf = findLeaf(start_key);
        string[] results = [];
        
        while (current_leaf !is null) {
            foreach (i, key_in_leaf; current_leaf.keys) {
                if (key_in_leaf >= start_key && key_in_leaf <= end_key) {
                    results ~= current_leaf.data_payloads[i];
                } else if (key_in_leaf > end_key) {
                    return results; // Range exceeded
                }
            }
            current_leaf = current_leaf.next_leaf;
            if (current_leaf !is null && current_leaf.keys.length > 0 && current_leaf.keys[0] > end_key) {
                break;
            }
        }
        return results;
    }
}

// void main() {
//     auto bp_tree = new BPlusTree(3);
//     bp_tree.insert(10, "data10");
//     bp_tree.insert(20, "data20");
//     bp_tree.insert(5, "data5");
//     bp_tree.insert(30, "data30");
//     bp_tree.insert(15, "data15");

//     writeln(bp_tree.search(20));
//     writeln(bp_tree.search(25));
//     
//     writeln("Range query [10, 25]:");
//     string[] range_results = bp_tree.rangeQuery(10, 25);
//     foreach(data; range_results) {
//         writeln("- ", data);
//     }
// }
```

## Applications

### Application

B+ Trees are the backbone of virtually all modern `relational database management systems (RDBMS)` and `file systems` due to their unparalleled efficiency for disk-based storage.
- **Database Indexing:** The primary use case. Indexes in databases like **MySQL (InnoDB)**, **PostgreSQL**, **SQL Server**, and **Oracle** are typically implemented using B+ Trees. This allows for very fast retrieval of records based on key values and highly efficient range queries.
- **File Systems:** Used in file systems (e.g., **APFS**, **Btrfs**, older versions of **NTFS**) for indexing file names and metadata, enabling quick file lookups.
- **Key-Value Stores:** Some key-value storage engines (especially those that need sorted key access) utilize B+ Trees.
- **Operating System Memory Management:** Can be used for managing virtual memory pages.

