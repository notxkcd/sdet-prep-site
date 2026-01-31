---
title: "Skip List"
---

A `Skip List` is a probabilistic data structure that allows `O(log n)` average time complexity for `search`, `insertion`, and `deletion` operations, similar to a balanced `binary search tree`. However, it is much simpler to implement than balanced `BSTs` like `AVL trees` or `Red-Black trees`.

It consists of multiple layers of sorted `linked lists`. Each layer acts as an "express lane" for the layer below it, allowing for quicker traversal. `Skip Lists` are often used in concurrent data structures and databases where their simplicity and good performance characteristics are advantageous.

## How it Works

### How it Works (Expanded)

A `Skip List` is built upon a base sorted `linked list` (Level 0). Higher levels contain "express lanes" by having a subset of the `nodes` from the level below. When a `node` is inserted, its `height` (number of layers it participates in) is chosen randomly, typically using a coin flip.

---

Example Skip List:

Level 2: HEAD --- 30 ------------------------------- TAIL
                 / \
Level 1: HEAD -- 10 -- 20 -- 30 ----------- 50 ----- TAIL
                 / \   / \   / \          / \
Level 0: HEAD -- 10 -- 20 -- 30 -- 40 -- 50 -- 60 --- TAIL

Searching for 40:
- Start at HEAD of Level 2. Next is 30. (30 < 40) -> Move right to 30.
- At 30, Level 2. Next is TAIL. (TAIL > 40) -> Drop down to Level 1.
- At 30, Level 1. Next is 50. (50 > 40) -> Drop down to Level 0.
- At 30, Level 0. Next is 40. (40 == 40) -> Found!

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
import random

MAX_LEVEL = 16 # A reasonable maximum level for a skip list

class SkipListNode:
    def __init__(self, key, level):
        self.key = key
        self.forward = [None] <em> (level + 1) # Pointers to next node at each level

class SkipList:
    def __init__(self):
        self.level = 0 # Current maximum level of the skip list
        self.head = SkipListNode(-float('inf'), MAX_LEVEL) # Head node with -infinity key

    def _random_level(self):
        # Randomly choose a level for a new node
        lvl = 0
        while random.random() < 0.5 and lvl < MAX_LEVEL:
            lvl += 1
        return lvl

    def search(self, key):
        current = self.head
        for i in range(self.level, -1, -1): # Start from highest level down
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
        
        # After traversing, current.forward[0] is the node at level 0 immediately
        # after current. Check if this is the key we're looking for.
        current = current.forward[0]
        if current and current.key == key:
            return current
        return None

    def insert(self, key):
        update = [None] </em> (MAX_LEVEL + 1) # To store pointers to update
        current = self.head

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current
        
        # Current is now the node just before the insertion point at level 0
        current = current.forward[0]

        if current and current.key == key: # Key already exists
            return

        # Generate a random level for the new node
        new_level = self._random_level()

        # If new_level is greater than current skip list level, update head
        if new_level > self.level:
            for i in range(self.level + 1, new_level + 1):
                update[i] = self.head
            self.level = new_level
        
        # Create new node
        new_node = SkipListNode(key, new_level)

        # Insert new node into list
        for i in range(new_level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def delete(self, key):
        update = [None] <em> (MAX_LEVEL + 1)
        current = self.head

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current
        
        current = current.forward[0]

        if current and current.key == key: # Key found, proceed with deletion
            for i in range(self.level + 1):
                if update[i].forward[i] != current: # If current node is not in this level, break
                    break
                update[i].forward[i] = current.forward[i]
            
            # Remove levels that no longer have elements
            while self.level > 0 and self.head.forward[self.level] is None:
                self.level -= 1
            return True
        return False # Key not found

# Example Usage:
# skip_list = SkipList()
# elements = [30, 10, 50, 20, 40, 60]
# for e in elements:
#     skip_list.insert(e)

# print("Search 40:", skip_list.search(40).key if skip_list.search(40) else None) # Expected: 40
# print("Search 70:", skip_list.search(70)) # Expected: None

# skip_list.delete(40)
# print("Search 40 after deletion:", skip_list.search(40)) # Expected: None
```

### Javascript

```javascript
const MAX_LEVEL = 16; // A reasonable maximum level for a skip list

class SkipListNode {
    constructor(key, level) {
        this.key = key;
        this.forward = new Array(level + 1).fill(null); // Pointers to next node at each level
    }
}

class SkipList {
    constructor() {
        this.level = 0; // Current maximum level of the skip list
        this.head = new SkipListNode(-Infinity, MAX_LEVEL); // Head node with -infinity key
    }

    _randomLevel() {
        // Randomly choose a level for a new node
        let lvl = 0;
        while (Math.random() < 0.5 && lvl < MAX_LEVEL) {
            lvl++;
        }
        return lvl;
    }

    search(key) {
        let current = this.head;
        for (let i = this.level; i >= 0; i--) { // Start from highest level down
            while (current.forward[i] && current.forward[i].key < key) {
                current = current.forward[i];
            }
        }
        
        // After traversing, current.forward[0] is the node at level 0 immediately
        // after current. Check if this is the key we're looking for.
        current = current.forward[0];
        if (current && current.key === key) {
            return current;
        }
        return null;
    }

    insert(key) {
        const update = new Array(MAX_LEVEL + 1).fill(null); // To store pointers to update
        let current = this.head;

        for (let i = this.level; i >= 0; i--) {
            while (current.forward[i] && current.forward[i].key < key) {
                current = current.forward[i];
            }
            update[i] = current;
        }
        
        // Current is now the node just before the insertion point at level 0
        current = current.forward[0];

        if (current && current.key === key) { // Key already exists
            return;
        }

        // Generate a random level for the new node
        const newLevel = this._randomLevel();

        // If newLevel is greater than current skip list level, update head
        if (newLevel > this.level) {
            for (let i = this.level + 1; i <= newLevel; i++) {
                update[i] = this.head;
            }
            this.level = newLevel;
        }
        
        // Create new node
        const newNode = new SkipListNode(key, newLevel);

        // Insert new node into list
        for (let i = 0; i <= newLevel; i++) {
            newNode.forward[i] = update[i].forward[i];
            update[i].forward[i] = newNode;
        }
    }

    delete(key) {
        const update = new Array(MAX_LEVEL + 1).fill(null);
        let current = this.head;

        for (let i = this.level; i >= 0; i--) {
            while (current.forward[i] && current.forward[i].key < key) {
                current = current.forward[i];
            }
            update[i] = current;
        }
        
        current = current.forward[0];

        if (current && current.key === key) { // Key found, proceed with deletion
            for (let i = 0; i <= this.level; i++) {
                if (update[i].forward[i] !== current) { // If current node is not in this level, break
                    break;
                }
                update[i].forward[i] = current.forward[i];
            }
            
            // Remove levels that no longer have elements
            while (this.level > 0 && this.head.forward[this.level] === null) {
                this.level--;
            }
            return true;
        }
        return false; // Key not found
    }
}

// Example Usage:
// const skipList = new SkipList();
// const elements = [30, 10, 50, 20, 40, 60];
// for (const e of elements) {
//     skipList.insert(e);
// }

// console.log("Search 40:", skipList.search(40)?.key); // Expected: 40
// console.log("Search 70:", skipList.search(70)); // Expected: null

// skipList.delete(40);
// console.log("Search 40 after deletion:", skipList.search(40)); // Expected: null
```

### Cpp

```cpp
#include <iostream>
#include <vector>
#include <random>   // For std::mt19937, std::uniform_real_distribution
#include <limits>   // For std::numeric_limits

const int MAX_LEVEL = 16; // A reasonable maximum level for a skip list

// Forward declaration
class SkipListNode;

class SkipList {
private:
    std::mt19937 gen; // Random number generator
    std::uniform_real_distribution<double>& dis; // For coin flip

    int level; // Current maximum level of the skip list
    SkipListNode</em> head; // Head node of the skip list

    int _randomLevel() {
        int lvl = 0;
        while (dis(gen) < 0.5 && lvl < MAX_LEVEL) { // Coin flip for level
            lvl++;
        }
        return lvl;
    }

public:
    SkipList();
    ~SkipList();

    SkipListNode<em> search(int key);
    void insert(int key);
    void remove(int key); // Renamed to remove to avoid conflict with C++ keyword
    void display();
};

class SkipListNode {
public:
    int key;
    std::vector<SkipListNode</em>> forward; // Pointers to next node at each level

    SkipListNode(int k, int lvl) : key(k), forward(lvl + 1, nullptr) {}
    
    // Destructor to prevent memory leaks in a chain
    ~SkipListNode() {
        // This destructor is tricky in a SkipList due to shared pointers.
        // A proper destructor would need to handle deletion carefully
        // to avoid double-freeing or missing nodes.
        // For this conceptual example, we'll rely on the main SkipList
        // destructor (if implemented fully) or manual management.
    }
};

SkipList::SkipList() : level(0), gen(std::random_device{}()), dis(0.0, 1.0) {
    head = new SkipListNode(std::numeric_limits<int>::min(), MAX_LEVEL); // Head node with -infinity key
}

SkipList::~SkipList() {
    SkipListNode<em> current = head->forward[0];
    while (current != nullptr) {
        SkipListNode</em> next = current->forward[0];
        delete current;
        current = next;
    }
    delete head;
}

SkipListNode<em> SkipList::search(int key) {
    SkipListNode</em> current = head;
    for (int i = level; i >= 0; i--) {
        while (current->forward[i] != nullptr && current->forward[i]->key < key) {
            current = current->forward[i];
        }
    }
    
    current = current->forward[0]; // Move to level 0 and check the next node
    if (current != nullptr && current->key == key) {
        return current;
    }
    return nullptr; // Key not found
}

void SkipList::insert(int key) {
    std::vector<SkipListNode<em>> update(MAX_LEVEL + 1); // To store pointers to update
    SkipListNode</em> current = head;

    for (int i = level; i >= 0; i--) {
        while (current->forward[i] != nullptr && current->forward[i]->key < key) {
            current = current->forward[i];
        }
        update[i] = current;
    }
    
    current = current->forward[0]; // Move to level 0, check for existing key
    if (current != nullptr && current->key == key) { // Key already exists
        return;
    }

    int new_level = _randomLevel(); // Generate a random level for the new node

    if (new_level > level) { // If new level is greater than current skip list level
        for (int i = level + 1; i <= new_level; i++) {
            update[i] = head; // Update pointers for new levels starting from head
        }
        level = new_level; // Update overall skip list level
    }
    
    SkipListNode<em> new_node = new SkipListNode(key, new_level); // Create new node

    // Insert new node into list
    for (int i = 0; i <= new_level; i++) {
        new_node->forward[i] = update[i]->forward[i];
        update[i]->forward[i] = new_node;
    }
}

void SkipList::remove(int key) {
    std::vector<SkipListNode</em>> update(MAX_LEVEL + 1);
    SkipListNode* current = head;

    for (int i = level; i >= 0; i--) {
        while (current->forward[i] != nullptr && current->forward[i]->key < key) {
            current = current->forward[i];
        }
        update[i] = current;
    }
    
    current = current->forward[0]; // Move to level 0 and check the node

    if (current != nullptr && current->key == key) { // Key found, proceed with deletion
        for (int i = 0; i <= level; i++) {
            if (update[i]->forward[i] != current) { // If current node is not in this level, break
                break;
            }
            update[i]->forward[i] = current->forward[i];
        }
        
        delete current; // Free the memory for the deleted node

        // Remove levels that no longer have elements
        while (level > 0 && head->forward[level] == nullptr) {
            level--;
        }
    }
}

// Example Usage:
// int main() {
//     SkipList skip_list;
//     std::vector<int> elements = {30, 10, 50, 20, 40, 60};
//     for (int e : elements) {
//         skip_list.insert(e);
//     }

//     std::cout << "Search 40: " << (skip_list.search(40) ? std::to_string(skip_list.search(40)->key) : "None") << std::endl; // Expected: 40
//     std::cout << "Search 70: " << (skip_list.search(70) ? std::to_string(skip_list.search(70)->key) : "None") << std::endl; // Expected: None

//     skip_list.remove(40);
//     std::cout << "Search 40 after deletion: " << (skip_list.search(40) ? std::to_string(skip_list.search(40)->key) : "None") << std::endl; // Expected: None
//     return 0;
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

A `Skip List` implementation requires managing `nodes` with multiple `forward` pointers and a probabilistic approach to `level` assignment.

---

**`SkipListNode` Class:** Represents a `node` in the `Skip List`.
- `key`: The value stored in the `node`.
- `forward`: A `list`/`vector` of pointers, where `forward[i]` points to the next `node` in `level i`.

**`SkipList` Class:** Manages the overall `Skip List` structure.
- `level`: The current maximum `level` of any `node` in the `Skip List`.
- `head`: A special `head node` (often with a `key` of `-infinity`) that has `forward` pointers for all possible `levels`.
- `_randomLevel()`: A private helper function that probabilistically determines the `level` (`height`) of a new `node`. Typically, a coin flip is used: if heads, increase `level`; repeat until tails or `MAX_LEVEL` is reached.
- **`search(key)`:**
- Starts from the `head node` at the highest current `level`.
- Traverses right as long as the next `node` exists and its `key` is less than the target `key`.
- If the next `node`'s `key` is greater or it's `None`/`nullptr`, it drops down to the next lower `level` and continues.
- Once `level 0` is reached, it checks if the `node` directly to its right is the target `key`.

    </li>
- **`insert(key)`:**
- Performs a `search`-like traversal, but instead of stopping, it stores the last visited `node` at each `level` in an `update array`. These are the `nodes` whose `forward` pointers will need to be updated.
- Generates a `random level` for the new `node`.
- If the `new node`'s `level` is higher than the current `Skip List`'s maximum `level`, the `head`'s `forward` pointers for those new `levels` are updated.
- Creates the new `SkipListNode` and inserts it into all relevant `linked lists` using the stored `update pointers`.

    </li>
- **`delete(key)`:**
- Similar to `insert`, it performs a `search` traversal and stores `update pointers`.
- If the `node` with the target `key` is found, it updates the `forward` pointers of the `nodes` in the `update array` to bypass the deleted `node`.
- Finally, it checks if any `levels` have become empty (only `head` and `tail` remain) and removes them.

    </li>

[Back to Implementation](#implementation)

## Applications

### Application

Skip Lists are a powerful alternative to balanced trees, offering similar performance with a simpler implementation. They are famously used in **Redis** to implement sorted sets. In concurrent programming, their structure allows for the creation of **lock-free data structures**, which are highly efficient in multi-threaded environments. They are also used in databases and network applications where data needs to be sorted and quickly accessible, but the complexity of a balanced tree is undesirable.

