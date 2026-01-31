---
title: "Insertion Sort"
---

`Insertion Sort` is a simple sorting algorithm that builds the final sorted `array` one `item` at a time. It iterates through an input `list` and removes one `element` per iteration, finds the location it belongs in the sorted part of the `list`, and inserts it there.

It is much less efficient on large `lists` than more advanced algorithms such as `quicksort`, `heapsort`, or `merge sort`, with a time complexity of `O(N^2)`. However, it is efficient for small datasets and is adaptive, meaning it is efficient for datasets that are already substantially sorted.

## How it Works

### How it Works (Expanded)

`Insertion Sort` works by dividing the `array` into a sorted and an unsorted part. It iterates from the second `element` (`index 1`) to the end of the `array`. In each iteration, it takes the current `element` and "inserts" it into its correct position within the already sorted part of the `array` (which is to the left of the current `element`).

---

Example: Sort [5, 2, 4, 6, 1, 3]

1. [5] | [2, 4, 6, 1, 3]  (Sorted | Unsorted)
- Take 2. Compare with 5. 2 < 5. Shift 5 right. Insert 2.
- Result: [2, 5] | [4, 6, 1, 3]

2. [2, 5] | [4, 6, 1, 3]
- Take 4. Compare with 5. 4 < 5. Shift 5 right. Compare with 2. 4 > 2. Insert 4.
- Result: [2, 4, 5] | [6, 1, 3]

3. [2, 4, 5] | [6, 1, 3]
- Take 6. Compare with 5. 6 > 5. No shift needed. Insert 6.
- Result: [2, 4, 5, 6] | [1, 3]

... and so on.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example
# my_arr = [5, 2, 4, 6, 1, 3]
# print(insertion_sort(my_arr)) # [1, 2, 3, 4, 5, 6]
```

### Javascript

```javascript
function insertionSort(arr) {
    const n = arr.length;
    for (let i = 1; i < n; i++) {
        let key = arr[i];
        let j = i - 1;
        
        // Move elements of arr[0..i-1], that are greater than key,
        // to one position ahead of their current position
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
    return arr;
}

// const myArr = [5, 2, 4, 6, 1, 3];
// console.log(insertionSort(myArr)); // [1, 2, 3, 4, 5, 6]
```

### Typescript

```typescript
function insertionSortTS(arr: number[]): number[] {
    const n = arr.length;
    for (let i = 1; i < n; i++) {
        let key = arr[i];
        let j = i - 1;
        
        // Move elements of arr[0..i-1], that are greater than key,
        // to one position ahead of their current position
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
    return arr;
}

// const myArrTS: number[] = [5, 2, 4, 6, 1, 3];
// console.log(insertionSortTS(myArrTS)); // [1, 2, 3, 4, 5, 6]
```

### Cpp

```cpp
#include <vector>
#include <utility> // For std::move

void insertionSort(std::vector<int>& arr) {
    for (int i = 1; i < arr.size(); ++i) {
        int key = arr[i];
        int j = i - 1;
        
        // Move elements of arr[0..i-1], that are greater than key,
        // to one position ahead of their current position
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

// #include <iostream>
// int main() {
//     std::vector<int> myArr = {5, 2, 4, 6, 1, 3};
//     insertionSort(myArr);
//     for(int val : myArr) {
//         std::cout << val << " "; // 1 2 3 4 5 6
//     }
//     std::cout << std::endl;
// }
```

### Go

```go
package main

func insertionSort(arr []int) []int {
    n := len(arr)
    for i := 1; i < n; i++ {
        key := arr[i]
        j := i - 1
        
        // Move elements of arr[0..i-1], that are greater than key,
        // to one position ahead of their current position
        for j >= 0 && arr[j] > key {
            arr[j+1] = arr[j]
            j--
        }
        arr[j+1] = key
    }
    return arr
}

// import "fmt"
// func main() {
//     myArr := []int{5, 2, 4, 6, 1, 3}
//     fmt.Println(insertionSort(myArr)) // [1 2 3 4 5 6]
// }
```

### D

```d
import std.algorithm;

void insertionSort(int[] arr) {
    for (int i = 1; i < arr.length; i++) {
        int key = arr[i];
        int j = i - 1;
        
        // Move elements of arr[0..i-1], that are greater than key,
        // to one position ahead of their current position
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

// import std.stdio;
// void main() {
//     auto myArr = [5, 2, 4, 6, 1, 3];
//     insertionSort(myArr);
//     writeln(myArr); // [1, 2, 3, 4, 5, 6]
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

`Insertion Sort`'s logic involves an outer loop that selects an `element` and an inner loop that shifts other `elements` to make space for it.

---

**Outer Loop (`i`):** Iterates from the second `element` (`index 1`) to the end of the `array`. `i` is the `index` of the current `element` (the `key`) to be inserted into the sorted portion.

**The `key`:** `arr[i]` is stored in a `key` variable. This is the `element` we are trying to place correctly.

**Inner Loop (`j`):** Starts from `i-1` and moves backward. It compares the `key` with each `element` in the sorted portion (`arr[0...i-1]`). As long as it finds an `element` `arr[j]` that is greater than the `key`, it shifts `arr[j]` one position to the right (`arr[j+1] = arr[j]`).

**Placement:** The inner loop stops when it finds an `element` smaller than or equal to the `key`, or when it reaches the beginning of the `array` (`j < 0`). The `key` is then placed at `arr[j+1]`, which is the first position where the `key` is not smaller than the `element` to its left.

[Back to Implementation](#implementation)

## Applications

### Application

Despite its `O(N^2)` complexity, `Insertion Sort` has some practical advantages:
- **Small Datasets:** It is one of the fastest algorithms for sorting very small arrays, often faster than "fast" algorithms like `Quicksort` or `Merge Sort` due to lower overhead.
- **Adaptive:** It is highly efficient for datasets that are already substantially sorted. If the input array is almost sorted, `Insertion Sort`'s performance approaches `O(N)`.
- **Online Sorting:** It can sort a list as it receives it.
- **Hybrid Sorts:** Because of its efficiency on small lists, `Insertion Sort` is often used as the final step in more complex sorting algorithms, such as `Timsort` (Python's default sort) and `Introsort`, which switch to `Insertion Sort` when the sub-array size becomes small.

