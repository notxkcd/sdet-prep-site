---
title: "Linked List"
---

Imagine a treasure hunt. Each clue tells you where the next one is. A Linked List is just like that. It's a chain of nodes, where each node contains some data and a pointer to the next node in the chain.

Unlike an array, the elements are not stored in contiguous memory locations. This gives it flexibility – it's easy to add or remove items without reorganizing the entire structure. But it also means you can't instantly jump to the 10th item; you have to follow the chain from the beginning.

## How it Works

### How it Works (Expanded)

A Linked List is a dynamic data structure, meaning its size can change during runtime. Each 'node' in the list typically holds two things:
- The actual `data` or value.
- A `reference` (or link) to the next node in the sequence.

The very first node is called the `head`. If the list is empty, the `head` is usually `null`. The last node's `next` reference points to `null`, signifying the end of the list.

---

[Data|Next] -> [Data|Next] -> [Data|Next] -> null
  ^                                         ^
  |                                         |
 Head                                       Tail (Next is null)

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self, node=None): # Added node=None for proper iteration in display
        if node is None:
            node = self.head
        elements = []
        current_node = node
        while current_node:
            elements.append(str(current_node.data))
            current_node = current_node.next
        print(" -> ".join(elements))
```

### Javascript

```javascript
class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
    }

    append(data) {
        const newNode = new Node(data);
        if (!this.head) {
            this.head = newNode;
            return;
        }
        let currentNode = this.head;
        while (currentNode.next) {
            currentNode = currentNode.next;
        }
        currentNode.next = newNode;
    }

    display() {
        const elements = [];
        let currentNode = this.head;
        while (currentNode) {
            elements.push(currentNode.data);
            currentNode = currentNode.next;
        }
        console.log(elements.join(' -> '));
    }
}
```

### Cpp

```cpp
#include <iostream>

class Node {
public:
    int data;
    Node<em> next;

    Node(int val) : data(val), next(nullptr) {}
};

class LinkedList {
public:
    Node</em> head;

    LinkedList() : head(nullptr) {}

    void append(int data) {
        Node<em> newNode = new Node(data);
        if (!head) {
            head = newNode;
            return;
        }
        Node</em> currentNode = head;
        while (currentNode->next) {
            currentNode = currentNode->next;
        }
        currentNode->next = newNode;
    }

    void display() {
        Node* currentNode = head;
        while (currentNode) {
            std::cout << currentNode->data << " -> ";
            currentNode = currentNode->next;
        }
        std::cout << "null" << std::endl;
    }
};
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

The code defines two main components:

---

**`Node` Class:** Represents an individual element.
- `data`: The value stored in the node.
- `next`: A pointer to the next node in the chain.

**`LinkedList` Class:** Manages the chain of nodes.
- `head`: A pointer to the very first node.
- `append(data)`: Adds a new node to the end.
- `display()`: Traverses the list and prints values.

[Back to Implementation](#implementation)

