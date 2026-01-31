---
title: "Splay Tree"
---

A `Splay Tree` is a self-balancing `binary search tree` (`BST`) with an additional property: recently accessed `nodes` are moved to the `root` of the `tree` through a series of rotations (splay operations). This "self-organizing" behavior means that frequently accessed `elements` can be found quickly, as they tend to stay near the `root`.

While worst-case operations can be `O(N)`, the amortized time complexity for most operations (`insertion`, `search`, `deletion`) is `O(log N)`. `Splay Trees` are often simpler to implement than other self-balancing `BSTs` like `AVL trees` or `Red-Black trees`, and can perform better in practice for certain access patterns (e.g., when some `elements` are accessed much more frequently than others).

## How it Works

### How it Works (Expanded)

The core idea of a `Splay Tree` is that every time a `node` is accessed (read, inserted, or deleted), that `node` is "splayed" to the `root` of the `tree`. This splay operation involves a sequence of `tree rotations`: `zig`, `zig-zig`, and `zig-zag`.

---

Splay Operations (moving X to the root):

1.  **Zig Rotation:** If X is a child of the root, rotate X with the root.
    (Simple case: X is child of P, P is root)
          P          X
         / \        / \
        X   C  ->  A   P
       / \            / \
      A   B          B   C

2.  **Zig-Zig Rotation:** If X and its parent P are both left children (or both right children).
    (Case: X is left child of P, P is left child of G)
          G                 X
         / \
        P   D             A   P
       / \        ->         / \
      X   C                 B   G
     / \                       / \
    A   B                     C   D

3.  **Zig-Zag Rotation:** If X is a left child and its parent P is a right child (or vice-versa).
    (Case: X is left child of P, P is right child of G)
          G                X
         / \
        A   P     ->     P   G
           / \          / \ / \
          B   X        A  B C  D
             / \
            C   D

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
# Conceptual Splay Tree implementation (Simplified for clarity)
# A full implementation involves precise handling of pointers during rotations.

class SplayTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None # Parent pointer simplifies rotations

class SplayTree:
    def __init__(self):
        self.root = None

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def _splay(self, node):
        while node.parent:
            parent = node.parent
            grandparent = parent.parent

            if not grandparent: # Zig rotation
                if node == parent.left:
                    self._rotate_right(parent)
                else:
                    self._rotate_left(parent)
            elif (node == parent.left and parent == grandparent.left): # Zig-zig left
                self._rotate_right(grandparent)
                self._rotate_right(parent)
            elif (node == parent.right and parent == grandparent.right): # Zig-zig right
                self._rotate_left(grandparent)
                self._rotate_left(parent)
            elif (node == parent.left and parent == grandparent.right): # Zig-zag left-right
                self._rotate_right(parent)
                self._rotate_left(grandparent)
            else: # Zig-zag right-left
                self._rotate_left(parent)
                self._rotate_right(grandparent)

    def insert(self, key):
        if not self.root:
            self.root = SplayTreeNode(key)
            return

        current = self.root
        parent = None
        while current:
            parent = current
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else: # Key already exists
                self._splay(current)
                return

        new_node = SplayTreeNode(key)
        new_node.parent = parent
        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
        self._splay(new_node) # Splay the newly inserted node to root

    def search(self, key):
        current = self.root
        last_visited = None
        while current:
            last_visited = current
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else: # Found
                self._splay(current)
                return current
        
        if last_visited: # Splay the last node visited if key not found
            self._splay(last_visited)
        return None # Not found

# Example Usage (simplified, deletion is even more complex):
# splay_tree = SplayTree()
# keys = [10, 20, 5, 30, 15, 25]
# for key in keys:
#     splay_tree.insert(key)

# print("Search for 25:")
# node_25 = splay_tree.search(25) # 25 should be root
# print(f"Root after searching 25: {splay_tree.root.key if splay_tree.root else None}") # Expected: 25

# print("Search for 5:")
# node_5 = splay_tree.search(5) # 5 should be root
# print(f"Root after searching 5: {splay_tree.root.key if splay_tree.root else None}") # Expected: 5
```

### Javascript

```javascript
// Conceptual Splay Tree implementation in JavaScript (Simplified)

class SplayTreeNode {
    constructor(key) {
        this.key = key;
        this.left = null;
        this.right = null;
        this.parent = null; // Parent pointer simplifies rotations
    }
}

class SplayTree {
    constructor() {
        this.root = null;
    }

    _rotateLeft(x) {
        let y = x.right;
        x.right = y.left;
        if (y.left) {
            y.left.parent = x;
        }
        y.parent = x.parent;
        if (!x.parent) {
            this.root = y;
        } else if (x === x.parent.left) {
            x.parent.left = y;
        } else {
            x.parent.right = y;
        }
        y.left = x;
        x.parent = y;
    }

    _rotateRight(x) {
        let y = x.left;
        x.left = y.right;
        if (y.right) {
            y.right.parent = x;
        }
        y.parent = x.parent;
        if (!x.parent) {
            this.root = y;
        } else if (x === x.parent.right) {
            x.parent.right = y;
        } else {
            x.parent.left = y;
        }
        y.right = x;
        x.parent = y;
    }

    _splay(node) {
        while (node.parent) {
            let parent = node.parent;
            let grandparent = parent.parent;

            if (!grandparent) { // Zig rotation
                if (node === parent.left) {
                    this._rotateRight(parent);
                } else {
                    this._rotateLeft(parent);
                }
            } else if (
                (node === parent.left && parent === grandparent.left) || // Zig-zig left
                (node === parent.right && parent === grandparent.right)    // Zig-zig right
            ) {
                if (node === parent.left) { // Zig-zig left
                    this._rotateRight(grandparent);
                    this._rotateRight(parent);
                } else { // Zig-zig right
                    this._rotateLeft(grandparent);
                    this._rotateLeft(parent);
                }
            } else { // Zig-zag
                if (node === parent.left) { // Zig-zag left-right
                    this._rotateRight(parent);
                    this._rotateLeft(grandparent);
                } else { // Zig-zag right-left
                    this._rotateLeft(parent);
                    this._rotateRight(grandparent);
                }
            }
        }
    }

    insert(key) {
        if (!this.root) {
            this.root = new SplayTreeNode(key);
            return;
        }

        let current = this.root;
        let parent = null;
        while (current) {
            parent = current;
            if (key < current.key) {
                current = current.left;
            } else if (key > current.key) {
                current = current.right;
            } else { // Key already exists
                this._splay(current);
                return;
            }
        }

        const newNode = new SplayTreeNode(key);
        newNode.parent = parent;
        if (key < parent.key) {
            parent.left = newNode;
        } else {
            parent.right = newNode;
        }
        this._splay(newNode); // Splay the newly inserted node to root
    }

    search(key) {
        let current = this.root;
        let lastVisited = null;
        while (current) {
            lastVisited = current;
            if (key < current.key) {
                current = current.left;
            } else if (key > current.key) {
                current = current.right;
            } else { // Found
                this._splay(current);
                return current;
            }
        }
        
        if (lastVisited) { // Splay the last node visited if key not found
            this._splay(lastVisited);
        }
        return null; // Not found
    }
}

// Example Usage (simplified, deletion is even more complex):
// const splayTree = new SplayTree();
// const keys = [10, 20, 5, 30, 15, 25];
// for (const key of keys) {
//     splayTree.insert(key);
// }

// console.log("Search for 25:");
// let node25 = splayTree.search(25); // 25 should be root
// console.log(<code>Root after searching 25: ${splayTree.root ? splayTree.root.key : null}</code>); // Expected: 25

// console.log("Search for 5:");
// let node5 = splayTree.search(5); // 5 should be root
// console.log(<code>Root after searching 5: ${splayTree.root ? splayTree.root.key : null}</code>); // Expected: 5
```

### Cpp

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm> // For std::max

// A SplayTreeNode represents a single node in the Splay tree
class SplayTreeNode {
public:
    int key;
    SplayTreeNode <em>left, </em>right, <em>parent;

    SplayTreeNode(int k) : key(k), left(nullptr), right(nullptr), parent(nullptr) {}
};

// A SplayTree
class SplayTree {
public:
    SplayTreeNode</em> root;

    SplayTree() : root(nullptr) {}

    ~SplayTree() {
        // Implement a proper tree destructor for production code
        // For this conceptual example, a simple approach is omitted
        // as recursive deletion can be tricky with parent pointers.
    }

private:
    void _rotate_left(SplayTreeNode<em> x) {
        SplayTreeNode</em> y = x->right;
        x->right = y->left;
        if (y->left != nullptr) {
            y->left->parent = x;
        }
        y->parent = x->parent;
        if (x->parent == nullptr) { // x was root
            root = y;
        } else if (x == x->parent->left) { // x was left child
            x->parent->left = y;
        } else { // x was right child
            x->parent->right = y;
        }
        y->left = x;
        x->parent = y;
    }

    void _rotate_right(SplayTreeNode<em> x) {
        SplayTreeNode</em> y = x->left;
        x->left = y->right;
        if (y->right != nullptr) {
            y->right->parent = x;
        }
        y->parent = x->parent;
        if (x->parent == nullptr) { // x was root
            root = y;
        } else if (x == x->parent->right) { // x was right child
            x->parent->right = y;
        } else { // x was left child
            x->parent->left = y;
        }
        y->right = x;
        x->parent = y;
    }

    void _splay(SplayTreeNode<em> node) {
        while (node->parent != nullptr) {
            SplayTreeNode</em> parent = node->parent;
            SplayTreeNode<em> grandparent = parent->parent;

            if (grandparent == nullptr) { // Zig rotation
                if (node == parent->left) {
                    _rotate_right(parent);
                } else {
                    _rotate_left(parent);
                }
            } else if ((node == parent->left && parent == grandparent->left) || // Zig-zig left
                       (node == parent->right && parent == grandparent->right)) { // Zig-zig right
                if (node == parent->left) { // Zig-zig left
                    _rotate_right(grandparent);
                    _rotate_right(parent);
                } else { // Zig-zig right
                    _rotate_left(grandparent);
                    _rotate_left(parent);
                }
            } else { // Zig-zag
                if (node == parent->left) { // Zig-zag left-right
                    _rotate_right(parent);
                    _rotate_left(grandparent);
                } else { // Zig-zag right-left
                    _rotate_left(parent);
                    _rotate_right(grandparent);
                }
            }
        }
    }

public:
    void insert(int key) {
        SplayTreeNode</em> new_node = new SplayTreeNode(key);
        if (root == nullptr) {
            root = new_node;
            return;
        }

        SplayTreeNode<em> current = root;
        SplayTreeNode</em> parent = nullptr;
        while (current != nullptr) {
            parent = current;
            if (key < current->key) {
                current = current->left;
            } else if (key > current->key) {
                current = current->right;
            } else { // Key already exists
                _splay(current);
                delete new_node; // Avoid memory leak
                return;
            }
        }

        new_node->parent = parent;
        if (key < parent->key) {
            parent->left = new_node;
        } else {
            parent->right = new_node;
        }
        _splay(new_node); // Splay the newly inserted node to root
    }

    SplayTreeNode<em> search(int key) {
        SplayTreeNode</em> current = root;
        SplayTreeNode<em> last_visited = nullptr;
        while (current != nullptr) {
            last_visited = current;
            if (key < current->key) {
                current = current->left;
            } else if (key > current->key) {
                current = current->right;
            } else { // Found
                _splay(current);
                return current;
            }
        }
        
        if (last_visited != nullptr) { // Splay the last node visited if key not found
            _splay(last_visited);
        }
        return nullptr; // Not found
    }

    // Deletion is complex in Splay trees, simplified for this conceptual example.
    // Generally, splay the node to delete to the root, remove it, and then
    // merge the two resulting subtrees (left and right).
};

// Example Usage:
// int main() {
//     SplayTree splay_tree;
//     std::vector<int> keys = {10, 20, 5, 30, 15, 25};
//     for (int key : keys) {
//         splay_tree.insert(key);
//     }

//     std::cout << "Search for 25:" << std::endl;
//     SplayTreeNode</em> node_25 = splay_tree.search(25); // 25 should be root
//     if (splay_tree.root) {
//         std::cout << "Root after searching 25: " << splay_tree.root->key << std::endl; // Expected: 25
//     }

//     std::cout << "Search for 5:" << std::endl;
//     SplayTreeNode* node_5 = splay_tree.search(5); // 5 should be root
//     if (splay_tree.root) {
//         std::cout << "Root after searching 5: " << splay_tree.root->key << std::endl; // Expected: 5
//     }
//     return 0;
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

A `Splay Tree`'s implementation revolves around its `node` structure and the specialized `splay` operation, which involves `tree rotations`.

---

**`SplayTreeNode` Class:**
- `key`: The value stored in the `node`.
- `left`, `right`: Pointers to child `nodes`.
- `parent`: A crucial pointer to the parent `node`, which simplifies rotations significantly.

**`SplayTree` Class:**
- `root`: A pointer to the `root SplayTreeNode`.
- **`_rotate_left(x)` and `_rotate_right(x)`:** Standard `binary search tree rotation` operations. These functions take a `node x` and rotate it with its `right` or `left child` respectively. They update all necessary `parent` and child `pointers` to maintain `tree integrity`.
- **`_splay(node)`:** The core of the `Splay Tree`. This function moves the given `node` to the `root` of the `tree` through a series of `zig`, `zig-zig`, and `zig-zag rotations`. The specific rotation pattern depends on the `node`'s position relative to its `parent` and `grandparent`.
- **`insert(key)`:**
- Inserts the new `key` as in a regular `BST`, creating a new `SplayTreeNode`.
- After insertion, calls `_splay()` on the newly inserted `node` to move it to the `root`.

    </li>
- **`search(key)`:**
- Searches for the `key` as in a regular `BST`.
- If the `key` is found, `_splay()` is called on the found `node` to bring it to the `root`.
- If the `key` is not found, `_splay()` is called on the last `node` visited during the unsuccessful search, bringing that `node` to the `root`.

    </li>

[Back to Implementation](#implementation)

## Applications

### Application

Splay Trees are particularly effective in applications where there is a high locality of reference, meaning that a small set of elements is accessed much more frequently than others. They are used in **cache implementations** (where recently accessed data should be quick to find again), **network routers** for routing tables, and in memory allocators and **garbage collectors** to manage memory blocks. Their self-organizing property makes them adaptive to changing access patterns without the strict balancing rules of AVL or Red-Black trees.

