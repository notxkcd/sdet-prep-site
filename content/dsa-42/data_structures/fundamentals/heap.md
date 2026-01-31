---
title: "Heap"
---

Imagine a corporate hierarchy where the CEO is always at the top, and managers report to directors, who report to the CEO. A Heap data structure is similar: it's a tree-based structure (specifically a `binary tree`) that satisfies the '`heap property`'.

In a '`Max-Heap`', the `value` of each `node` is greater than or equal to the `value` of its children. In a '`Min-Heap`', the `value` of each `node` is less than or equal to the `value` of its children.

Heaps are commonly used to implement '`Priority Queues`' – queues where elements are dequeued based on priority, not just arrival order.

## How it Works

### How it Works (Expanded)

Heaps are typically implemented using an `array` because of their specific structure: a `complete binary tree`. This means all levels of the tree are fully filled, except possibly the last level, which is filled from `left` to `right`. This allows for efficient mapping of tree nodes to `array` indices.

---

Heap (Array Representation): 
Index:  0  1  2  3  4  5  6
Value: [10, 8, 9, 4, 5, 7, 3]  (Max-Heap example) 

Tree Representation:
        (10)
       /    \
      (8)    (9)
     /  \   /  \
    (4) (5)(7) (3)

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
import heapq

# Python's heapq module implements a min-heap.
# By default, it stores elements such that the smallest is always at index 0.

my_min_heap = []

# Insert (O(log n))
heapq.heappush(my_min_heap, 10)
heapq.heappush(my_min_heap, 8)
heapq.heappush(my_min_heap, 9)
heapq.heappush(my_min_heap, 4)
print("Heap after pushes:", my_min_heap) # Not necessarily sorted, but smallest is first: [4, 8, 9, 10]

# Pop (O(log n)) - removes and returns smallest element
smallest_item = heapq.heappop(my_min_heap)
print("Popped smallest item:", smallest_item) # Output: 4
print("Heap after pop:", my_min_heap) # [8, 10, 9]

# Peek (O(1)) - smallest element
if my_min_heap:
    print("Smallest item (peek):", my_min_heap[0]) # Output: 8

# To implement a max-heap, store negative of values:
my_max_heap = []
heapq.heappush(my_max_heap, -10)
heapq.heappush(my_max_heap, -8)
heapq.heappush(my_max_heap, -9)
print("Max-Heap (internal):", my_max_heap) # [-10, -8, -9]
max_item = -heapq.heappop(my_max_heap)
print("Popped largest item:", max_item) # Output: 10
```

### Javascript

```javascript
// JavaScript does not have a built-in Heap. 
// This is a simplified MinHeap implementation using an Array.

class MinHeap {
    constructor() {
        this.heap = [];
    }

    getParentIndex(i) { return Math.floor((i - 1) / 2); }
    getLeftChildIndex(i) { return 2 <em> i + 1; }
    getRightChildIndex(i) { return 2 </em> i + 2; }

    hasParent(i) { return this.getParentIndex(i) >= 0; }
    hasLeftChild(i) { return this.getLeftChildIndex(i) < this.heap.length; }
    hasRightChild(i) { return this.getRightChildIndex(i) < this.heap.length; }

    getParent(i) { return this.heap[this.getParentIndex(i)]; }
    getLeftChild(i) { return this.heap[this.getLeftChildIndex(i)]; }
    getRightChild(i) { return this.heap[this.getRightChildIndex(i)]; }

    swap(i, j) {
        [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
    }

    peek() {
        if (this.heap.length === 0) return null;
        return this.heap[0];
    }

    insert(item) {
        this.heap.push(item);
        this.heapifyUp();
    }

    extractMin() {
        if (this.heap.length === 0) return null;
        if (this.heap.length === 1) return this.heap.pop();

        const item = this.heap[0];
        this.heap[0] = this.heap.pop();
        this.heapifyDown();
        return item;
    }

    heapifyUp() {
        let index = this.heap.length - 1;
        while (this.hasParent(index) && this.getParent(index) > this.heap[index]) {
            this.swap(this.getParentIndex(index), index);
            index = this.getParentIndex(index);
        }
    }

    heapifyDown() {
        let index = 0;
        while (this.hasLeftChild(index)) {
            let smallerChildIndex = this.getLeftChildIndex(index);
            if (this.hasRightChild(index) && this.getRightChild(index) < this.getLeftChild(index)) {
                smallerChildIndex = this.getRightChildIndex(index);
            }

            if (this.heap[index] < this.heap[smallerChildIndex]) {
                break;
            } else {
                this.swap(index, smallerChildIndex);
            }
            index = smallerChildIndex;
        }
    }
}
```

### Cpp

```cpp
#include <iostream>
#include <vector>
#include <queue> // Standard Library Priority Queue (Max-Heap by default)

int main() {
    // Max-Heap example (default for std::priority_queue)
    std::priority_queue<int> maxHeap;

    // Insert (O(log n))
    maxHeap.push(10);
    maxHeap.push(8);
    maxHeap.push(9);
    maxHeap.push(4);
    std::cout << "Max-Heap top (peek): " << maxHeap.top() << std::endl; // Output: 10

    // Pop (O(log n))
    std::cout << "Popped largest item: " << maxHeap.top() << std::endl; // Output: 10
    maxHeap.pop();
    std::cout << "Max-Heap top after pop: " << maxHeap.top() << std::endl; // Output: 9

    std::cout << "--------------------" << std::endl;

    // Min-Heap example (using std::greater<int>)
    std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;

    minHeap.push(10);
    minHeap.push(8);
    minHeap.push(9);
    minHeap.push(4);
    std::cout << "Min-Heap top (peek): " << minHeap.top() << std::endl; // Output: 4

    std::cout << "Popped smallest item: " << minHeap.top() << std::endl; // Output: 4
    minHeap.pop();
    std::cout << "Min-Heap top after pop: " << minHeap.top() << std::endl; // Output: 8

    return 0;
}
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

Python and C++ offer built-in Heap/Priority Queue implementations, while JavaScript typically requires a custom class.

---

**Python:** The `heapq` module provides `min-heap` functionality. Elements are stored in a `list`, and `heappush`/`heappop` maintain the `heap property`. To simulate a `max-heap`, you push/pop the negative of `values`.

**JavaScript:** Requires a custom `MinHeap` (or `MaxHeap`) `class`. This involves implementing `insert` (`heapifyUp`) and `extractMin` (`heapifyDown`) methods that use an `array` and ensure the `heap property` is maintained by swapping elements.

**C++:** The STL provides `std::priority_queue`, which is a container adapter that uses a `heap` internally. By default, it's a `max-heap`. You can make it a `min-heap` by providing `std::greater<int>` as a `comparator`.

[Back to Implementation](#implementation)

