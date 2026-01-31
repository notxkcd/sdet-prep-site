---
title: "Stack"
---

Imagine a stack of plates: you can only put a new plate on top, and you can only take the top plate off. A Stack data structure works exactly like this, following the `LIFO` (`Last-In, First-Out`) principle.

It's used everywhere from managing function calls in a program (the `call stack`) to undo/redo features in software.

## How it Works

### How it Works (Expanded)

A Stack is an abstract data type (ADT) that maintains a collection of elements. It has two primary operations:
- **`Push`:** Adds an element to the top of the stack.
- **`Pop`:** Removes and returns the element from the top of the stack.

The `LIFO` principle means the last element added is always the first one to be removed. Think of a spring-loaded plate dispenser in a cafeteria.

---

    |   |    <- TOP
    | D |
    | C |
    | B |
    | A |
    -----

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
# Python's list can be used as a stack.
my_stack = []

# Push (O(1))
my_stack.append('A')
my_stack.append('B')
my_stack.append('C')
print("Stack after pushes:", my_stack)

# Pop (O(1))
top_item = my_stack.pop()
print("Popped item:", top_item)
print("Stack after pop:", my_stack)

# Peek/Top (O(1))
if my_stack:
    print("Top item (peek):", my_stack[-1])
```

### Javascript

```javascript
// JavaScript's Array can be used as a stack.
let myStack = [];

// Push (O(1))
myStack.push('A');
myStack.push('B');
myStack.push('C');
console.log("Stack after pushes:", myStack); // Output: ["A", "B", "C"]

// Pop (O(1))
let topItem = myStack.pop();
console.log("Popped item:", topItem); // Output: C
console.log("Stack after pop:", myStack); // Output: ["A", "B"]

// Peek/Top (O(1))
if (myStack.length > 0) {
    console.log("Top item (peek):", myStack[myStack.length - 1]); // Output: B
}
```

### Cpp

```cpp
#include <iostream>
#include <stack> // Standard Library Stack

int main() {
    std::stack<char> myStack;

    // Push (O(1))
    myStack.push('A');
    myStack.push('B');
    myStack.push('C');
    std::cout << "Stack size after pushes: " << myStack.size() << std::endl;

    // Pop (O(1))
    char topItem = myStack.top(); // Get top element
    myStack.pop();                 // Remove top element
    std::cout << "Popped item: " << topItem << std::endl;
    std::cout << "Stack size after pop: " << myStack.size() << std::endl;

    // Peek/Top (O(1))
    if (!myStack.empty()) {
        std::cout << "Top item (peek): " << myStack.top() << std::endl;
    }
    return 0;
}
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

Implementing a stack is straightforward in most languages, often using built-in array capabilities or a linked list.

---

**Python:** Uses a standard `list`. `append()` is used for `push`, and `pop()` for `pop`. `list[-1]` accesses the top element without removing it.

**JavaScript:** Uses a standard `Array`. `push()` for `push`, and `pop()` for `pop`. `array[array.length - 1]` accesses the top element.

**C++:** The Standard Template Library (STL) provides a dedicated `std::stack` adapter. `push()` for `push`, `pop()` for `pop` (removes, doesn't return), and `top()` to peek at the top element.

[Back to Implementation](#implementation)

