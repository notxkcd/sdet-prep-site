---
title: "Selection Sort"
---

`Selection Sort` is an in-place comparison sorting algorithm. It has an `O(N^2)` time complexity, which makes it inefficient on large lists, and generally performs worse than the similar `Insertion Sort`. `Selection Sort` is noted for its simplicity and has performance advantages over more complicated algorithms in certain situations, particularly where auxiliary memory is limited.

The algorithm divides the input list into two parts: a sorted sublist of items which is built up from left to right at the front (left) of the list and a sublist of the remaining unsorted items that occupy the rest of the list.

## How it Works

### How it Works (Expanded)

The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, swapping it with the leftmost unsorted element, and moving the sublist boundaries one element to the right.

---

Example: Sort [64, 25, 12, 22, 11]

Pass 1:
- Find the minimum element in [64, 25, 12, 22, 11]. The minimum is 11 at index 4.
- Swap arr[0] with arr[4]: (11, 25, 12, 22, 64)
- Sorted sublist: [11] | Unsorted sublist: [25, 12, 22, 64]

Pass 2:
- Find the minimum element in [25, 12, 22, 64]. The minimum is 12 at index 2.
- Swap arr[1] with arr[2]: (11, 12, 25, 22, 64)
- Sorted sublist: [11, 12] | Unsorted sublist: [25, 22, 64]

Pass 3:
- Find the minimum element in [25, 22, 64]. The minimum is 22 at index 3.
- Swap arr[2] with arr[3]: (11, 12, 22, 25, 64)
- Sorted sublist: [11, 12, 22] | Unsorted sublist: [25, 64]

...and so on, until the entire array is sorted.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
def selection_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example
# my_arr = [64, 25, 12, 22, 11]
# print(selection_sort(my_arr)) # [11, 12, 22, 25, 64]
```

### Javascript

```javascript
function selectionSort(arr) {
    const n = arr.length;
    for (let i = 0; i < n; i++) {
        // Find the minimum element in the remaining unsorted array
        let minIdx = i;
        for (let j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        
        // Swap the found minimum element with the first element
        if (minIdx !== i) {
            [arr[i], arr[minIdx]] = [arr[minIdx], arr[i]];
        }
    }
    return arr;
}

// const myArr = [64, 25, 12, 22, 11];
// console.log(selectionSort(myArr)); // [11, 12, 22, 25, 64]
```

### Typescript

```typescript
function selectionSortTS(arr: number[]): number[] {
    const n = arr.length;
    for (let i = 0; i < n; i++) {
        // Find the minimum element in the remaining unsorted array
        let minIdx = i;
        for (let j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        
        // Swap the found minimum element with the first element
        if (minIdx !== i) {
            [arr[i], arr[minIdx]] = [arr[minIdx], arr[i]];
        }
    }
    return arr;
}

// const myArrTS: number[] = [64, 25, 12, 22, 11];
// console.log(selectionSortTS(myArrTS)); // [11, 12, 22, 25, 64]
```

### Cpp

```cpp
#include <vector>
#include <utility> // For std::swap

void selectionSort(std::vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; ++i) {
        // Find the minimum element in the remaining unsorted array
        int min_idx = i;
        for (int j = i + 1; j < n; ++j) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        
        // Swap the found minimum element with the first element
        if (min_idx != i) {
            std::swap(arr[i], arr[min_idx]);
        }
    }
}

// #include <iostream>
// int main() {
//     std::vector<int> myArr = {64, 25, 12, 22, 11};
//     selectionSort(myArr);
//     for(int val : myArr) {
//         std::cout << val << " "; // 11 12 22 25 64
//     }
//     std::cout << std::endl;
// }
```

### Go

```go
package main

func selectionSort(arr []int) []int {
    n := len(arr)
    for i := 0; i < n; i++ {
        // Find the minimum element in the remaining unsorted array
        minIdx := i
        for j := i + 1; j < n; j++ {
            if arr[j] < arr[minIdx] {
                minIdx = j
            }
        }
        
        // Swap the found minimum element with the first element
        arr[i], arr[minIdx] = arr[minIdx], arr[i]
    }
    return arr
}

// import "fmt"
// func main() {
//     myArr := []int{64, 25, 12, 22, 11}
//     fmt.Println(selectionSort(myArr)) // [11 12 22 25 64]
// }
```

### D

```d
import std.algorithm;

void selectionSort(int[] arr) {
    auto n = arr.length;
    for (int i = 0; i < n; i++) {
        // Find the minimum element in the remaining unsorted array
        int minIdx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        
        // Swap the found minimum element with the first element
        if (minIdx != i) {
            swap(arr[i], arr[minIdx]);
        }
    }
}

// import std.stdio;
// void main() {
//     auto myArr = [64, 25, 12, 22, 11];
//     selectionSort(myArr);
//     writeln(myArr); // [11, 12, 22, 25, 64]
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

`Selection Sort`'s logic is based on dividing the array into sorted and unsorted portions and progressively expanding the sorted part.

---

**Outer Loop (`i`):** This loop iterates from the start of the array to the end. The index `i` represents the boundary between the sorted sub-array (from 0 to `i-1`) and the unsorted sub-array (from `i` to `n-1`).

**Finding the Minimum:** Inside the outer loop, we assume the first element of the unsorted portion (`arr[i]`) is the minimum. The inner loop (`j`) then iterates through the rest of the unsorted portion (`i+1` to `n-1`) to find the actual minimum element. The index of this minimum element is stored in `min_idx`.

**Swapping:** After the inner loop completes, `min_idx` holds the index of the smallest element in the unsorted part of the array. This element is then swapped with the element at the current boundary position, `arr[i]`. This effectively moves the smallest unsorted element into its final sorted position.

**Progression:** The outer loop index `i` is incremented, and the process repeats, with the sorted portion of the array growing by one element in each pass.

[Back to Implementation](#implementation)

## Applications

### Application

Like `Bubble Sort`, `Selection Sort` is primarily used for educational purposes due to its inefficiency on large datasets. However, its property of minimizing the number of swaps (at most `N-1`) can be useful in very specific scenarios where the cost of writing to memory is extremely high, such as with certain types of flash memory.

