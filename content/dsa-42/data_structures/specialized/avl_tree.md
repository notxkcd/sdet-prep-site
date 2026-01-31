---
title: "AVL Tree"
---

An `AVL Tree` is a self-balancing `binary search tree` (`BST`). It was the first such `tree` structure to be invented, named after its inventors `Georgy Adelson-Velsky` and `Evgenii Landis`, who published it in 1962.

The "`self-balancing`" property means that the heights of the two child subtrees of any `node` differ by at most one. This strict balancing ensures that `search`, `insertion`, and `deletion` operations always take `O(log N)` time, preventing the worst-case `O(N)` performance that an unbalanced `BST` might encounter.

## How it Works

### How it Works (Expanded)

The core concept of an `AVL Tree` is the **balance factor**. For every `node`, the `balance factor` is defined as the height of its `left subtree` minus the height of its `right subtree`. In an `AVL Tree`, the `balance factor` of any `node` must always be `-1`, `0`, or `1`.

---

Example: AVL Tree Node Structure

        (Node: Value=X, Height=H, BalanceFactor=B)
        / \
       /   \
LeftChild   RightChild
Height(LeftChild) - Height(RightChild) = B, where B is -1, 0, or 1.

## Implementation {#implementation}

### Python

```python
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1 # Height of the node

class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        
        # Perform rotation
        x.right = y
        y.left = T2
        
        # Update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        
        # Perform rotation
        y.left = x
        x.right = T2
        
        # Update heights
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        
        return y

    def insert(self, root, key):
        # 1. Perform standard BST insert
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        
        # 2. Update height of current node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        
        # 3. Get balance factor
        balance = self.get_balance(root)
        
        # 4. If unbalanced, perform rotations
        
        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        
        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        
        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root

    def pre_order(self, root):
        if not root:
            return
        print(f"{root.key} ", end="")
        self.pre_order(root.left)
        self.pre_order(root.right)

# Example Usage:
# my_tree = AVLTree()
# root = None
# keys = [10, 20, 30, 40, 50, 25]
# for key in keys:
#     root = my_tree.insert(root, key)
# print("Preorder traversal of constructed AVL tree is:")
# my_tree.pre_order(root) # Expected to be balanced
```

### Javascript

```javascript
class AVLNode {
    constructor(key) {
        this.key = key;
        this.left = null;
        this.right = null;
        this.height = 1; // Height of the node
    }
}

class AVLTree {
    getHeight(node) {
        if (!node) {
            return 0;
        }
        return node.height;
    }

    getBalance(node) {
        if (!node) {
            return 0;
        }
        return this.getHeight(node.left) - this.getHeight(node.right);
    }

    rightRotate(y) {
        let x = y.left;
        let T2 = x.right;
        
        // Perform rotation
        x.right = y;
        y.left = T2;
        
        // Update heights
        y.height = 1 + Math.max(this.getHeight(y.left), this.getHeight(y.right));
        x.height = 1 + Math.max(this.getHeight(x.left), this.getHeight(x.right));
        
        return x;
    }

    leftRotate(x) {
        let y = x.right;
        let T2 = y.left;
        
        // Perform rotation
        y.left = x;
        x.right = T2;
        
        // Update heights
        x.height = 1 + Math.max(this.getHeight(x.left), this.getHeight(x.right));
        y.height = 1 + Math.max(this.getHeight(y.left), this.getHeight(y.right));
        
        return y;
    }

    insert(root, key) {
        // 1. Perform standard BST insert
        if (!root) {
            return new AVLNode(key);
        } else if (key < root.key) {
            root.left = this.insert(root.left, key);
        } else if (key > root.key) {
            root.right = this.insert(root.right, key);
        } else { // Duplicate keys not allowed in this implementation
            return root;
        }
        
        // 2. Update height of current node
        root.height = 1 + Math.max(this.getHeight(root.left), this.getHeight(root.right));
        
        // 3. Get balance factor
        const balance = this.getBalance(root);
        
        // 4. If unbalanced, perform rotations
        
        // Left Left Case
        if (balance > 1 && key < root.left.key) {
            return this.rightRotate(root);
        }
        
        // Right Right Case
        if (balance < -1 && key > root.right.key) {
            return this.leftRotate(root);
        }
        
        // Left Right Case
        if (balance > 1 && key > root.left.key) {
            root.left = this.leftRotate(root.left);
            return this.rightRotate(root);
        }
        
        // Right Left Case
        if (balance < -1 && key < root.right.key) {
            root.right = this.rightRotate(root.right);
            return this.leftRotate(root);
        }
        
        return root;
    }

    preOrder(root) {
        if (root) {
            process.stdout.write(<code>${root.key} </code>);
            this.preOrder(root.left);
            this.preOrder(root.right);
        }
    }
}

// const myTree = new AVLTree();
// let root = null;
// const keys = [10, 20, 30, 40, 50, 25];
// for (const key of keys) {
//     root = myTree.insert(root, key);
// }
// console.log("Preorder traversal of constructed AVL tree is:");
// myTree.preOrder(root); // Expected to be balanced
```

### Typescript

```typescript
class AVLNodeTS {
    public key: number;
    public left: AVLNodeTS | null;
    public right: AVLNodeTS | null;
    public height: number;

    constructor(key: number) {
        this.key = key;
        this.left = null;
        this.right = null;
        this.height = 1;
    }
}

class AVLTreeTS {
    public root: AVLNodeTS | null = null;

    private getHeight(node: AVLNodeTS | null): number {
        if (!node) {
            return 0;
        }
        return node.height;
    }

    private getBalance(node: AVLNodeTS | null): number {
        if (!node) {
            return 0;
        }
        return this.getHeight(node.left) - this.getHeight(node.right);
    }

    private rightRotate(y: AVLNodeTS): AVLNodeTS {
        let x = y.left!;
        let T2 = x.right;
        
        x.right = y;
        y.left = T2;
        
        y.height = 1 + Math.max(this.getHeight(y.left), this.getHeight(y.right));
        x.height = 1 + Math.max(this.getHeight(x.left), this.getHeight(x.right));
        
        return x;
    }

    private leftRotate(x: AVLNodeTS): AVLNodeTS {
        let y = x.right!;
        let T2 = y.left;
        
        y.left = x;
        x.right = T2;
        
        x.height = 1 + Math.max(this.getHeight(x.left), this.getHeight(x.right));
        y.height = 1 + Math.max(this.getHeight(y.left), this.getHeight(y.right));
        
        return y;
    }

    public insert(rootNode: AVLNodeTS | null, key: number): AVLNodeTS {
        if (!rootNode) {
            return new AVLNodeTS(key);
        } else if (key < rootNode.key) {
            rootNode.left = this.insert(rootNode.left, key);
        } else if (key > rootNode.key) {
            rootNode.right = this.insert(rootNode.right, key);
        } else {
            return rootNode;
        }
        
        rootNode.height = 1 + Math.max(this.getHeight(rootNode.left), this.getHeight(rootNode.right));
        
        const balance = this.getBalance(rootNode);
        
        if (balance > 1 && key < rootNode.left!.key) {
            return this.rightRotate(rootNode);
        }
        
        if (balance < -1 && key > rootNode.right!.key) {
            return this.leftRotate(rootNode);
        }
        
        if (balance > 1 && key > rootNode.left!.key) {
            rootNode.left = this.leftRotate(rootNode.left!);
            return this.rightRotate(rootNode);
        }
        
        if (balance < -1 && key < rootNode.right!.key) {
            rootNode.right = this.rightRotate(rootNode.right!);
            return this.leftRotate(rootNode);
        }
        
        return rootNode;
    }

    public preOrder(rootNode: AVLNodeTS | null): void {
        if (rootNode) {
            process.stdout.write(<code>${rootNode.key} </code>);
            this.preOrder(rootNode.left);
            this.preOrder(rootNode.right);
        }
    }
}

// const myTreeTS = new AVLTreeTS();
// let rootTS: AVLNodeTS | null = null;
// const keysTS: number[] = [10, 20, 30, 40, 50, 25];
// for (const key of keysTS) {
//     rootTS = myTreeTS.insert(rootTS, key);
// }
// console.log("Preorder traversal of constructed AVL tree is:");
// myTreeTS.preOrder(rootTS); // Expected to be balanced
```

### Cpp

```cpp
#include <iostream>
#include <algorithm> // For std::max

class AVLNode {
public:
    int key;
    AVLNode <em>left;
    AVLNode </em>right;
    int height;

    AVLNode(int k) : key(k), left(nullptr), right(nullptr), height(1) {}
};

class AVLTree {
public:
    AVLNode<em> root;

    AVLTree() : root(nullptr) {}

    // Helper function to get the height of the node
    int height(AVLNode</em> node) {
        if (node == nullptr)
            return 0;
        return node->height;
    }

    // Helper function to get the balance factor of the node
    int getBalance(AVLNode<em> node) {
        if (node == nullptr)
            return 0;
        return height(node->left) - height(node->right);
    }

    // Right rotate subtree rooted with y
    AVLNode</em> rightRotate(AVLNode<em> y) {
        AVLNode</em> x = y->left;
        AVLNode<em> T2 = x->right;

        // Perform rotation
        x->right = y;
        y->left = T2;

        // Update heights
        y->height = 1 + std::max(height(y->left), height(y->right));
        x->height = 1 + std::max(height(x->left), height(x->right));

        // Return new root
        return x;
    }

    // Left rotate subtree rooted with x
    AVLNode</em> leftRotate(AVLNode<em> x) {
        AVLNode</em> y = x->right;
        AVLNode<em> T2 = y->left;

        // Perform rotation
        y->left = x;
        x->right = T2;

        // Update heights
        x->height = 1 + std::max(height(x->left), height(x->right));
        y->height = 1 + std::max(height(y->left), height(y->right));

        // Return new root
        return y;
    }

    // Insert a key into the AVL tree
    AVLNode</em> insert(AVLNode<em> node, int key) {
        // 1. Perform standard BST insert
        if (node == nullptr)
            return new AVLNode(key);
        if (key < node->key)
            node->left = insert(node->left, key);
        else if (key > node->key)
            node->right = insert(node->right, key);
        else // Duplicate keys not allowed
            return node;

        // 2. Update height of current node
        node->height = 1 + std::max(height(node->left), height(node->right));

        // 3. Get balance factor
        int balance = getBalance(node);

        // 4. If unbalanced, perform rotations

        // Left Left Case
        if (balance > 1 && key < node->left->key)
            return rightRotate(node);

        // Right Right Case
        if (balance < -1 && key > node->right->key)
            return leftRotate(node);

        // Left Right Case
        if (balance > 1 && key > node->left->key) {
            node->left = leftRotate(node->left);
            return rightRotate(node);
        }

        // Right Left Case
        if (balance < -1 && key < node->right->key) {
            node->right = rightRotate(node->right);
            return leftRotate(node);
        }

        return node;
    }

    // Function to print pre-order traversal of the AVL tree
    void preOrder(AVLNode</em> node) {
        if (node != nullptr) {
            std::cout << node->key << " ";
            preOrder(node->left);
            preOrder(node.right);
        }
    }
};

// int main() {
//     AVLTree tree;
//     tree.root = nullptr;
//     std::vector<int> keys = {10, 20, 30, 40, 50, 25};
//     for (int key : keys) {
//         tree.root = tree.insert(tree.root, key);
//     }
//     std::cout << "Preorder traversal of constructed AVL tree is:" << std::endl;
//     tree.preOrder(tree.root); // Expected to be balanced
//     std::cout << std::endl;
//     return 0;
// }
```

### Go

```go
package main

import (
    "fmt"
    "math"
)

type AVLNode struct {
    Key    int
    Left   <em>AVLNode
    Right  </em>AVLNode
    Height int
}

func NewAVLNode(key int) <em>AVLNode {
    return &AVLNode{Key: key, Height: 1}
}

type AVLTree struct {
    Root </em>AVLNode
}

func (tree <em>AVLTree) getHeight(node </em>AVLNode) int {
    if node == nil {
        return 0
    }
    return node.Height
}

func (tree <em>AVLTree) getBalance(node </em>AVLNode) int {
    if node == nil {
        return 0
    }
    return tree.getHeight(node.Left) - tree.getHeight(node.Right)
}

func (tree <em>AVLTree) rightRotate(y </em>AVLNode) <em>AVLNode {
    x := y.Left
    T2 := x.Right

    x.Right = y
    y.Left = T2

    y.Height = 1 + int(math.Max(float64(tree.getHeight(y.Left)), float64(tree.getHeight(y.Right))))
    x.Height = 1 + int(math.Max(float64(tree.getHeight(x.Left)), float64(tree.getHeight(x.Right))))

    return x
}

func (tree </em>AVLTree) leftRotate(x <em>AVLNode) </em>AVLNode {
    y := x.Right
    T2 := y.Left

    y.Left = x
    x.Right = T2

    x.Height = 1 + int(math.Max(float64(tree.getHeight(x.Left)), float64(tree.getHeight(x.Right))))
    y.Height = 1 + int(math.Max(float64(tree.getHeight(y.Left)), float64(tree.getHeight(y.Right))))

    return y
}

func (tree <em>AVLTree) Insert(node </em>AVLNode, key int) <em>AVLNode {
    if node == nil {
        return NewAVLNode(key)
    }

    if key < node.Key {
        node.Left = tree.Insert(node.Left, key)
    } else if key > node.Key {
        node.Right = tree.Insert(node.Right, key)
    } else { // Duplicate keys not allowed
        return node
    }

    node.Height = 1 + int(math.Max(float64(tree.getHeight(node.Left)), float64(tree.getHeight(node.Right))))

    balance := tree.getBalance(node)

    // Left Left Case
    if balance > 1 && key < node.Left.Key {
        return tree.rightRotate(node)
    }

    // Right Right Case
    if balance < -1 && key > node.Right.Key {
        return tree.leftRotate(node)
    }

    // Left Right Case
    if balance > 1 && key > node.Left.Key {
        node.Left = tree.leftRotate(node.Left)
        return tree.rightRotate(node)
    }

    // Right Left Case
    if balance < -1 && key < node.Right.Key {
        node.Right = tree.rightRotate(node.Right)
        return tree.leftRotate(node)
    }

    return node
}

func (tree </em>AVLTree) PreOrder(node *AVLNode) {
    if node != nil {
        fmt.Printf("%d ", node.Key) // Use Printf for formatted output
        tree.PreOrder(node.Left)
        tree.PreOrder(node.Right)
    }
}

// func main() {
//     myTree := &AVLTree{}
//     keys := []int{10, 20, 30, 40, 50, 25}
//     for _, key := range keys {
//         myTree.Root = myTree.Insert(myTree.Root, key)
//     }
//     fmt.Println("Preorder traversal of constructed AVL tree is:")
//     myTree.PreOrder(myTree.Root) // Expected to be balanced
//     fmt.Println()
// }
```

### D

```d
import std.stdio;
import std.algorithm; // For std.algorithm.max

class AVLNode {
    int key;
    AVLNode left;
    AVLNode right;
    int height;

    this(int k) {
        key = k;
        left = null;
        right = null;
        height = 1;
    }
}

class AVLTree {
    AVLNode root;

    this() {
        root = null;
    }

    // Helper function to get the height of the node
    int getHeight(AVLNode node) {
        if (node is null)
            return 0;
        return node.height;
    }

    // Helper function to get the balance factor of the node
    int getBalance(AVLNode node) {
        if (node is null)
            return 0;
        return getHeight(node.left) - getHeight(node.right);
    }

    // Right rotate subtree rooted with y
    AVLNode rightRotate(AVLNode y) {
        AVLNode x = y.left;
        AVLNode T2 = x.right;

        // Perform rotation
        x.right = y;
        y.left = T2;

        // Update heights
        y.height = 1 + max(getHeight(y.left), getHeight(y.right));
        x.height = 1 + max(getHeight(x.left), getHeight(x.right));

        // Return new root
        return x;
    }

    // Left rotate subtree rooted with x
    AVLNode leftRotate(AVLNode x) {
        AVLNode y = x.right;
        AVLNode T2 = y.left;

        // Perform rotation
        y.left = x;
        x.right = T2;

        // Update heights
        x.height = 1 + max(getHeight(x.left), getHeight(x.right));
        y.height = 1 + max(getHeight(y.left), getHeight(y.right));

        // Return new root
        return y;
    }

    // Insert a key into the AVL tree
    AVLNode insert(AVLNode node, int key) {
        // 1. Perform standard BST insert
        if (node is null)
            return new AVLNode(key);
        if (key < node.key)
            node.left = insert(node.left, key);
        else if (key > node.key)
            node.right = insert(node.right, key);
        else // Duplicate keys not allowed
            return node;

        // 2. Update height of current node
        node.height = 1 + max(getHeight(node.left), getHeight(node.right));

        // 3. Get balance factor
        int balance = getBalance(node);

        // 4. If unbalanced, perform rotations
        
        // Left Left Case
        if (balance > 1 && key < node.left.key)
            return rightRotate(node);

        // Right Right Case
        if (balance < -1 && key > node.right.key)
            return leftRotate(node);

        // Left Right Case
        if (balance > 1 && key > node.left.key) {
            node.left = leftRotate(node.left);
            return rightRotate(node);
        }

        // Right Left Case
        if (balance < -1 && key < node.right.key) {
            node.right = rightRotate(node.right);
            return leftRotate(node);
        }

        return node;
    }

    // Function to print pre-order traversal of the AVL tree
    void preOrder(AVLNode node) {
        if (node !is null) {
            writef("%d ", node.key);
            preOrder(node.left);
            preOrder(node.right);
        }
    }
}

// void main() {
//     auto tree = new AVLTree();
//     int[] keys = [10, 20, 30, 40, 50, 25];
//     foreach (key; keys) {
//         tree.root = tree.insert(tree.root, key);
//     }
//     writeln("Preorder traversal of constructed AVL tree is:");
//     tree.preOrder(tree.root); // Expected to be balanced
//     writeln();
// }
```

## Applications

### Application

`AVL Trees` are used in applications where fast `search`, `insertion`, and `deletion` operations are all equally critical, and consistent `O(log N)` worst-case performance is required. They are often found in:
- **Database Indexing:** Providing reliable `O(log N)` lookup times for indexed records.
- **In-memory Sorting:** When elements are added and removed frequently, and the data needs to remain sorted.
- **Symbol Tables:** In compilers and interpreters, to efficiently manage identifiers and their properties.
- **Networking:** For routing tables where IP addresses (keys) need to be efficiently looked up and updated.
- **Anywhere balanced `BST` performance is needed:** Such as in some graphical algorithms or computational geometry problems.

