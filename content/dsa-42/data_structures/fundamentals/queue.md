---
title: "Queue"
---

Imagine a line at a ticket counter. The first person to get in line is the first person to get served. A Queue data structure works exactly like this, following the `FIFO` (`First-In, First-Out`) principle.

It's used for any situation where you need to process things in the order they were received, like a print queue or a server handling requests.

## How it Works

### How it Works (Expanded)

A Queue is an abstract data type (ADT) that maintains a collection of elements. It has two primary operations:
- **`Enqueue`:** Adds an element to the back (or '`tail`') of the queue.
- **`Dequeue`:** Removes and returns the element from the front (or '`head`') of the queue.

The `FIFO` principle means the first element added is always the first one to be removed.

---

 FRONT                                      BACK
   |                                          |
   v                                          v
   [ A ] -> [ B ] -> [ C ] -> [ D ]

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
from collections import deque

# Python's deque is an efficient double-ended queue.
my_queue = deque()

# Enqueue (O(1))
my_queue.append('A')
my_queue.append('B')
my_queue.append('C')
print("Queue after enqueues:", my_queue)

# Dequeue (O(1))
front_item = my_queue.popleft()
print("Dequeued item:", front_item)
print("Queue after dequeue:", my_queue)

# Peek (O(1))
if my_queue:
    print("Front item (peek):", my_queue[0])
```

### Javascript

```javascript
// JavaScript's Array can be used as a queue, but shift() can be O(n).
// For high-performance queues, a linked list is better.
let myQueue = [];

// Enqueue (O(1))
myQueue.push('A');
myQueue.push('B');
myQueue.push('C');
console.log("Queue after enqueues:", myQueue); // Output: ["A", "B", "C"]

// Dequeue (O(n) for Array, O(1) for Linked List)
let frontItem = myQueue.shift();
console.log("Dequeued item:", frontItem); // Output: A
console.log("Queue after dequeue:", myQueue); // Output: ["B", "C"]

// Peek (O(1))
if (myQueue.length > 0) {
    console.log("Front item (peek):", myQueue[0]); // Output: B
}
```

### Cpp

```cpp
#include <iostream>
#include <queue> // Standard Library Queue

int main() {
    std::queue<char> myQueue;

    // Enqueue (O(1))
    myQueue.push('A');
    myQueue.push('B');
    myQueue.push('C');
    std::cout << "Queue size after enqueues: " << myQueue.size() << std::endl;

    // Dequeue (O(1))
    char frontItem = myQueue.front(); // Get front element
    myQueue.pop();                 // Remove front element
    std::cout << "Dequeued item: " << frontItem << std::endl;
    std::cout << "Queue size after dequeue: " << myQueue.size() << std::endl;

    // Peek (O(1))
    if (!myQueue.empty()) {
        std::cout << "Front item (peek): " << myQueue.front() << std::endl;
    }
    return 0;
}
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

Implementing a queue efficiently requires care. A standard array/list is okay for `enqueue`, but removing from the start is often slow.

---

**Python:** Uses `collections.deque`, a double-ended queue optimized for fast `appends` and `pops` from both ends. `append()` `enqueues` and `popleft()` `dequeues`, both in `O(1)` time.

**JavaScript:** Using `push()` to `enqueue` is `O(1)`, but using `shift()` to `dequeue` is an `O(n)` operation because all other elements must be shifted. For performance-critical applications, a custom linked-list based queue is preferred.

**C++:** The STL `std::queue` is an adapter that uses a `std::deque` by default. `push()` `enqueues`, `pop()` `dequeues`, and `front()` peeks at the first item. All are `O(1)` operations.

[Back to Implementation](#implementation)

