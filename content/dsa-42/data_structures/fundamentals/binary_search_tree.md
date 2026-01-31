---
title: "Binary Search Tree"
---

Imagine organizing a massive library. You wouldn't put every book on a single, long shelf. Instead, you'd use a hierarchical system, like a card catalog, to quickly find what you're looking for. A Binary Search Tree (`BST`) works similarly, organizing data in a way that allows for efficient searching, insertion, and deletion.

It's a tree-like structure where each '`node`' has at most two children: a '`left`' child and a '`right`' child. The `key` property is that all values in the `left` subtree are less than the `node`'s `value`, and all values in the `right` subtree are greater.

## How it Works

### How it Works (Expanded)

A `BST` maintains elements in a sorted order, which is crucial for its performance. Here are the core rules:
- Each `node` has a `value`.
- The `left` child's `value` (if it exists) is always less than the parent's `value`.
- The `right` child's `value` (if it exists) is always greater than the parent's `value`.

This recursive definition allows you to quickly navigate the tree:

---

    ( 10 )
   /    \
  ( 5 ) ( 15 )
 / \   /  \
( 2 )( 7 )( 12 )( 18 )

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        return node

    def search(self, key):
        return self._search_recursive(self.root, key) is not None

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def inorder_traversal(self):
        elements = []
        self._inorder_recursive(self.root, elements)
        return elements

    def _inorder_recursive(self, node, elements):
        if node:
            self._inorder_recursive(node.left, elements)
            elements.append(node.key)
            self._inorder_recursive(node.right, elements)
```

### Javascript

```javascript
class Node {
    constructor(key) {
        this.key = key;
        this.left = null;
        this.right = null;
    }
}

class BST {
    constructor() {
        this.root = null;
    }

    insert(key) {
        this.root = this._insertRecursive(this.root, key);
    }

    _insertRecursive(node, key) {
        if (node === null) {
            return new Node(key);
        }
        if (key < node.key) {
            node.left = this._insertRecursive(node.left, key);
        } else if (key > node.key) {
            node.right = this._insertRecursive(node.right, key);
        }
        return node;
    }

    search(key) {
        return this._searchRecursive(this.root, key) !== null;
    }

    _searchRecursive(node, key) {
        if (node === null || node.key === key) {
            return node;
        }
        if (key < node.key) {
            return this._searchRecursive(node.left, key);
        }
        return this._searchRecursive(node.right, key);
    }

    inorderTraversal() {
        const elements = [];
        this._inorderRecursive(this.root, elements);
        return elements;
    }

    _inorderRecursive(node, elements) {
        if (node) {
            this._inorderRecursive(node.left, elements);
            elements.push(node.key);
            this._inorderRecursive(node.right, elements);
        }
    }
}
```

### Cpp

```cpp
#include <iostream>

class Node {
public:
    int key;
    Node <em>left, </em>right;

    Node(int item) {
        key = item;
        left = right = nullptr;
    }
};

class BST {
public:
    Node<em> root;

    BST() {
        root = nullptr;
    }

    // Insert operation
    Node</em> insertRecursive(Node<em> node, int key) {
        if (node == nullptr) {
            return new Node(key);
        }
        if (key < node->key) {
            node->left = insertRecursive(node->left, key);
        } else if (key > node->key) {
            node->right = insertRecursive(node->right, key);
        }
        return node;
    }

    void insert(int key) {
        root = insertRecursive(root, key);
    }

    // Search operation
    Node</em> searchRecursive(Node<em> node, int key) {
        if (node == nullptr || node->key == key) {
            return node;
        }
        if (key < node->key) {
            return searchRecursive(node->left, key);
        }
        return searchRecursive(node->right, key);
    }

    bool search(int key) {
        return searchRecursive(root, key) != nullptr;
    }

    // Inorder traversal (for printing sorted elements)
    void inorderRecursive(Node</em> node) {
        if (node) {
            inorderRecursive(node->left);
            std::cout << node->key << " ";
            inorderRecursive(node->right);
        }
    }

    void inorderTraversal() {
        inorderRecursive(root);
        std::cout << std::endl;
    }
};
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

A `BST` is typically implemented using custom `Node` objects and recursive functions for operations.

---

**`Node` Class:** Each `Node` holds a `key` (the `value`) and two pointers, `left` and `right`, initially `null`.

**`BST` Class:** Manages the tree, primarily through its `root` `node`.
- **`insert(key)`:** Public method that calls a private recursive helper. The helper finds the correct spot to insert the new `key` while maintaining the `BST` property.
- **`search(key)`:** Public method calling a private recursive helper. The helper traverses the tree, going `left` or `right` based on the `key`'s `value` compared to the current `node`, until the `key` is found or a `null` `node` is reached.
- **`inorder_traversal()`:** A common way to visit all `nodes`. It recursively visits the `left` subtree, then the current `node`, then the `right` subtree, resulting in an output of sorted elements.

[Back to Implementation](#implementation)

