---
title: "Heap Sort"
---

`Heap Sort` is a comparison-based sorting algorithm that uses a `binary heap` data structure. It can be thought of as an improved version of `selection sort`, where instead of linearly scanning the unsorted part to find the maximum element, it uses a `heap` to find the maximum in `O(log N)` time.

It has an `O(N log N)` time complexity in all cases (best, average, and worst) and is an in-place sorting algorithm, meaning it requires only a constant amount of extra memory space.

## How it Works

### How it Works (Expanded)

The `Heap Sort` algorithm works in two main phases:
- **Build a Max-Heap:** The first step is to build a `max-heap` from the input array. A `max-heap` is a `binary tree` where the value of each `parent node` is greater than or equal to the value of its children. This ensures that the root of the `heap` is always the largest element in the array.
- **Repeatedly Extract Maximum:** The algorithm then repeatedly extracts the maximum element from the `heap` (which is always at the root) and moves it to the end of the array. The heap is then rebuilt with the remaining elements, and the process is repeated until the entire array is sorted.

---

Example: Sort [4, 10, 3, 5, 1]

1. Build Max-Heap:
- Rearrange array into a max-heap: [10, 5, 3, 4, 1]

2. Extract-Max Phase:
- Swap root (10) with last element (1): [1, 5, 3, 4, 10]
- Heapify the reduced heap [1, 5, 3, 4]. New heap: [5, 4, 3, 1]. Array: [5, 4, 3, 1, 10]
- Swap root (5) with last element (1): [1, 4, 3, 5, 10]
- Heapify the reduced heap [1, 4, 3]. New heap: [4, 1, 3]. Array: [4, 1, 3, 5, 10]
   ...and so on, until the array is fully sorted.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 <em> i + 1
    right = 2 </em> i + 2

    # See if left child of root exists and is greater than root
    if left < n and arr[i] < arr[left]:
        largest = left

    # See if right child of root exists and is greater than root
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        # Heapify the root.
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a max-heap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
    return arr

# Example
# my_arr = [38, 27, 43, 3, 9, 82, 10]
# print(heap_sort(my_arr)) # [3, 9, 10, 27, 38, 43, 82]
```

### Javascript

```javascript
function heapSort(arr) {
    let n = arr.length;

    // Build a max-heap (rearrange array)
    for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {
        heapify(arr, n, i);
    }

    // One by one extract an element from heap
    for (let i = n - 1; i > 0; i--) {
        // Move current root to end
        [arr[0], arr[i]] = [arr[i], arr[0]];

        // call max heapify on the reduced heap
        heapify(arr, i, 0);
    }
    return arr;
}

function heapify(arr, n, i) {
    let largest = i; // Initialize largest as root
    let left = 2 <em> i + 1;
    let right = 2 </em> i + 2;

    // If left child is larger than root
    if (left < n && arr[left] > arr[largest]) {
        largest = left;
    }

    // If right child is larger than largest so far
    if (right < n && arr[right] > arr[largest]) {
        largest = right;
    }

    // If largest is not root
    if (largest !== i) {
        [arr[i], arr[largest]] = [arr[largest], arr[i]]; // swap

        // Recursively heapify the affected sub-tree
        heapify(arr, n, largest);
    }
}

// const myArr = [38, 27, 43, 3, 9, 82, 10];
// console.log(heapSort(myArr)); // [3, 9, 10, 27, 38, 43, 82]
```

### Typescript

```typescript
function heapSortTS(arr: number[]): number[] {
    let n = arr.length;

    // Build a max-heap (rearrange array)
    for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {
        heapifyTS(arr, n, i);
    }

    // One by one extract an element from heap
    for (let i = n - 1; i > 0; i--) {
        // Move current root to end
        [arr[0], arr[i]] = [arr[i], arr[0]];

        // call max heapify on the reduced heap
        heapifyTS(arr, i, 0);
    }
    return arr;
}

function heapifyTS(arr: number[], n: number, i: number): void {
    let largest = i; // Initialize largest as root
    let left = 2 <em> i + 1;
    let right = 2 </em> i + 2;

    // If left child is larger than root
    if (left < n && arr[left] > arr[largest]) {
        largest = left;
    }

    // If right child is larger than largest so far
    if (right < n && arr[right] > arr[largest]) {
        largest = right;
    }

    // If largest is not root
    if (largest !== i) {
        [arr[i], arr[largest]] = [arr[largest], arr[i]]; // swap

        // Recursively heapify the affected sub-tree
        heapifyTS(arr, n, largest);
    }
}

// const myArrTS: number[] = [38, 27, 43, 3, 9, 82, 10];
// console.log(heapSortTS(myArrTS)); // [3, 9, 10, 27, 38, 43, 82]
```

### Cpp

```cpp
#include <vector>
#include <utility> // For std::swap
#include <iostream>

void heapify(std::vector<int>& arr, int n, int i) {
    int largest = i; // Initialize largest as root
    int left = 2 <em> i + 1;
    int right = 2 </em> i + 2;

    // If left child is larger than root
    if (left < n && arr[left] > arr[largest]) {
        largest = left;
    }

    // If right child is larger than largest so far
    if (right < n && arr[right] > arr[largest]) {
        largest = right;
    }

    // If largest is not root
    if (largest != i) {
        std::swap(arr[i], arr[largest]);
        
        // Recursively heapify the affected sub-tree
        heapify(arr, n, largest);
    }
}

void heapSort(std::vector<int>& arr) {
    int n = arr.size();

    // Build a max-heap (rearrange array)
    for (int i = n / 2 - 1; i >= 0; i--) {
        heapify(arr, n, i);
    }

    // One by one extract an element from heap
    for (int i = n - 1; i > 0; i--) {
        // Move current root to end
        std::swap(arr[0], arr[i]);

        // call max heapify on the reduced heap
        heapify(arr, i, 0);
    }
}

// int main() {
//     std::vector<int> myArr = {38, 27, 43, 3, 9, 82, 10};
//     heapSort(myArr);
//     for(int val : myArr) {
//         std::cout << val << " "; // 3 9 10 27 38 43 82
//     }
//     std::cout << std::endl;
// }
```

### Go

```go
package main

import "fmt"

func heapify(arr []int, n, i int) {
    largest := i // Initialize largest as root
    left := 2<em>i + 1
    right := 2</em>i + 2

    // If left child is larger than root
    if left < n && arr[left] > arr[largest] {
        largest = left
    }

    // If right child is larger than largest so far
    if right < n && arr[right] > arr[largest] {
        largest = right
    }

    // If largest is not root
    if largest != i {
        arr[i], arr[largest] = arr[largest], arr[i] // swap

        // Recursively heapify the affected sub-tree
        heapify(arr, n, largest)
    }
}

func heapSort(arr []int) []int {
    n := len(arr)

    // Build a max-heap (rearrange array)
    for i := n/2 - 1; i >= 0; i-- {
        heapify(arr, n, i)
    }

    // One by one extract an element from heap
    for i := n - 1; i > 0; i-- {
        // Move current root to end
        arr[0], arr[i] = arr[i], arr[0]

        // call max heapify on the reduced heap
        heapify(arr, i, 0)
    }
    return arr
}

// func main() {
//     myArr := []int{38, 27, 43, 3, 9, 82, 10}
//     fmt.Println(heapSort(myArr)) // [3 9 10 27 38 43 82]
// }
```

### D

```d
import std.algorithm;
import std.stdio;

void heapify(int[] arr, int n, int i) {
    int largest = i; // Initialize largest as root
    int left = 2 <em> i + 1;
    int right = 2 </em> i + 2;

    // If left child is larger than root
    if (left < n && arr[left] > arr[largest]) {
        largest = left;
    }

    // If right child is larger than largest so far
    if (right < n && arr[right] > arr[largest]) {
        largest = right;
    }

    // If largest is not root
    if (largest != i) {
        swap(arr[i], arr[largest]);
        
        // Recursively heapify the affected sub-tree
        heapify(arr, n, largest);
    }
}

void heapSort(int[] arr) {
    int n = cast(int)arr.length;

    // Build a max-heap (rearrange array)
    for (int i = n / 2 - 1; i >= 0; i--) {
        heapify(arr, n, i);
    }

    // One by one extract an element from heap
    for (int i = n - 1; i > 0; i--) {
        // Move current root to end
        swap(arr[0], arr[i]);

        // call max heapify on the reduced heap
        heapify(arr, i, 0);
    }
}

// void main() {
//     auto myArr = [38, 27, 43, 3, 9, 82, 10];
//     heapSort(myArr);
//     writeln(myArr); // [3, 9, 10, 27, 38, 43, 82]
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

`Heap Sort` uses a helper function, `heapify`, to maintain the `heap property` within a subtree of the `array`. The main function orchestrates the two main phases: building the `heap` and extracting `elements`.

---

**`heapify(arr, n, i)` Function:**
- Assumes the subtrees rooted at the children of `index i` are already valid `max-heaps`.
- Compares `arr[i]` with its `left` and `right children` to find the largest of the three.
- If the `largest` element is not the current `root` `i`, it swaps them.
- After the swap, the `heap property` might be violated in the subtree where the swap occurred. Therefore, it makes a recursive call to `heapify` on that subtree to fix it.

**`heapSort(arr)` Function:**
- **Build Max-Heap:** It iterates backwards from the last non-leaf `node` (`n/2 - 1`) to the `root` (0), calling `heapify` on each one. This ensures that the entire `array` is structured as a `max-heap`.
- **Extract Elements:** It then iterates backwards from the end of the `array` to the beginning.
- In each iteration, it swaps the current `root` (`arr[0]`, which is the largest remaining `element`) with the element at the end of the unsorted portion (`arr[i]`).
- This moves the largest `element` into its final sorted position.
- It then calls `heapify` on the reduced `heap` (of size `i`) to restore the `max-heap property` for the remaining `elements`.

    </li>

[Back to Implementation](#implementation)

## Applications

### Application

`Heap Sort` is a reliable, in-place sorting algorithm with guaranteed `O(N log N)` performance.
- **Priority Queues:** It is the algorithm used to implement `Heaps`, which are themselves used to implement `Priority Queues`.
- **Selection Algorithms:** It is efficient for finding the "k-th" smallest or largest element in an array, as you only need to `extract` from the `heap` `k` times.
- **Embedded Systems:** Its `O(1)` space complexity makes it suitable for memory-constrained environments where out-of-place algorithms like `Merge Sort` might not be feasible.
- **Robust Sorting:** When a guaranteed worst-case `O(N log N)` performance is needed (unlike `Quick Sort`, which can degrade to `O(N^2)`), `Heap Sort` is a good choice.

