---
title: "Quick Sort"
---

`Quick Sort` is a highly efficient, in-place sorting algorithm. It is a "`divide and conquer`" algorithm that works by selecting a '`pivot`' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the `pivot`. The sub-arrays are then sorted recursively.

Its average-case time complexity is `O(N log N)`, which makes it one of the fastest sorting algorithms in practice. However, its worst-case performance is `O(N^2)`, though this can be mitigated with good pivot selection strategies.

## How it Works

### How it Works (Expanded)

The core of `Quick Sort` is the **partitioning** step. Given an array and an element `x` (the `pivot`), `partitioning` rearranges the array so that all elements less than `x` come before `x`, and all elements greater than `x` come after `x`.

---

Example: Partitioning [38, 27, 43, 3, 9, 82, 10] with pivot 38
- Partitioning can result in: [10, 27, 3, 9] | 38 | [82, 43]
  (Order within sub-arrays doesn't matter yet)

Then, recursively sort the sub-arrays.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
def quick_sort_recursive(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr, low, high)

        # Separately sort elements before partition and after partition
        quick_sort_recursive(arr, low, pi - 1)
        quick_sort_recursive(arr, pi + 1, high)

def partition(arr, low, high):
    # Choosing the last element as pivot
    pivot = arr[high]
    
    # Index of smaller element
    i = low - 1
    
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr):
    quick_sort_recursive(arr, 0, len(arr) - 1)
    return arr

# Example
# my_arr = [38, 27, 43, 3, 9, 82, 10]
# print(quick_sort(my_arr)) # [3, 9, 10, 27, 38, 43, 82]
```

### Javascript

```javascript
function quickSortRecursive(arr, low, high) {
    if (low < high) {
        // pi is partitioning index, arr[p] is now at right place
        let pi = partition(arr, low, high);

        // Separately sort elements before partition and after partition
        quickSortRecursive(arr, low, pi - 1);
        quickSortRecursive(arr, pi + 1, high);
    }
}

function partition(arr, low, high) {
    // Choosing the last element as pivot
    let pivot = arr[high];
    
    // Index of smaller element
    let i = low - 1;
    
    for (let j = low; j < high; j++) {
        // If current element is smaller than or equal to pivot
        if (arr[j] <= pivot) {
            i++;
            [arr[i], arr[j]] = [arr[j], arr[i]]; // Swap
        }
    }
    
    [arr[i + 1], arr[high]] = [arr[high], arr[i + 1]];
    return i + 1;
}

function quickSort(arr) {
    quickSortRecursive(arr, 0, arr.length - 1);
    return arr;
}

// const myArr = [38, 27, 43, 3, 9, 82, 10];
// console.log(quickSort(myArr)); // [3, 9, 10, 27, 38, 43, 82]
```

### Typescript

```typescript
function quickSortRecursiveTS(arr: number[], low: number, high: number): void {
    if (low < high) {
        // pi is partitioning index, arr[p] is now at right place
        let pi = partitionTS(arr, low, high);

        // Separately sort elements before partition and after partition
        quickSortRecursiveTS(arr, low, pi - 1);
        quickSortRecursiveTS(arr, pi + 1, high);
    }
}

function partitionTS(arr: number[], low: number, high: number): number {
    // Choosing the last element as pivot
    let pivot = arr[high];
    
    // Index of smaller element
    let i = low - 1;
    
    for (let j = low; j < high; j++) {
        // If current element is smaller than or equal to pivot
        if (arr[j] <= pivot) {
            i++;
            [arr[i], arr[j]] = [arr[j], arr[i]]; // Swap
        }
    }
    
    [arr[i + 1], arr[high]] = [arr[high], arr[i + 1]];
    return i + 1;
}

function quickSortTS(arr: number[]): number[] {
    quickSortRecursiveTS(arr, 0, arr.length - 1);
    return arr;
}

// const myArrTS: number[] = [38, 27, 43, 3, 9, 82, 10];
// console.log(quickSortTS(myArrTS)); // [3, 9, 10, 27, 38, 43, 82]
```

### Cpp

```cpp
#include <vector>
#include <utility> // For std::swap

// Partition the array using the last element as the pivot
int partition(std::vector<int>& arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1; // Index of smaller element

    for (int j = low; j < high; j++) {
        // If current element is smaller than or equal to pivot
        if (arr[j] <= pivot) {
            i++;
            std::swap(arr[i], arr[j]);
        }
    }
    std::swap(arr[i + 1], arr[high]);
    return i + 1;
}

// The main function that implements QuickSort
void quickSort(std::vector<int>& arr, int low, int high) {
    if (low < high) {
        // pi is partitioning index, arr[p] is now at right place
        int pi = partition(arr, low, high);

        // Separately sort elements before partition and after partition
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

// #include <iostream>
// int main() {
//     std::vector<int> myArr = {38, 27, 43, 3, 9, 82, 10};
//     quickSort(myArr, 0, myArr.size() - 1);
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

func quickSortRecursive(arr []int, low, high int) {
    if low < high {
        // pi is partitioning index, arr[p] is now at right place
        pi := partition(arr, low, high)

        // Separately sort elements before partition and after partition
        quickSortRecursive(arr, low, pi-1)
        quickSortRecursive(arr, pi+1, high)
    }
}

func partition(arr []int, low, high int) int {
    // Choosing the last element as pivot
    pivot := arr[high]
    
    // Index of smaller element
    i := low - 1
    
    for j := low; j < high; j++ {
        // If current element is smaller than or equal to pivot
        if arr[j] <= pivot {
            i++
            arr[i], arr[j] = arr[j], arr[i] // Swap
        }
    }
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1
}

func quickSort(arr []int) []int {
    quickSortRecursive(arr, 0, len(arr)-1)
    return arr
}

// func main() {
//     myArr := []int{38, 27, 43, 3, 9, 82, 10}
//     fmt.Println(quickSort(myArr)) // [3 9 10 27 38 43 82]
// }
```

### D

```d
import std.algorithm;

void quickSortRecursive(int[] arr, int low, int high) {
    if (low < high) {
        // pi is partitioning index, arr[p] is now at right place
        int pi = partition(arr, low, high);

        // Separately sort elements before partition and after partition
        quickSortRecursive(arr, low, pi - 1);
        quickSortRecursive(arr, pi + 1, high);
    }
}

int partition(int[] arr, int low, int high) {
    // Choosing the last element as pivot
    int pivot = arr[high];
    
    // Index of smaller element
    int i = low - 1;
    
    for (int j = low; j < high; j++) {
        // If current element is smaller than or equal to pivot
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quickSort(int[] arr) {
    quickSortRecursive(arr, 0, cast(int)arr.length - 1);
}

// import std.stdio;
// void main() {
//     auto myArr = [38, 27, 43, 3, 9, 82, 10];
//     quickSort(myArr);
//     writeln(myArr); // [3, 9, 10, 27, 38, 43, 82]
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

`Quick Sort` is typically implemented recursively. The main logic lies in the `partition` function.

---

**`quickSort(arr, low, high)` Function:**
- This is the recursive "driver" function.
- The base case for the recursion is `low >= high`, which means the sub-array has 0 or 1 elements and is already sorted.
- It calls the `partition` function to place a pivot element in its correct sorted position.
- It then recursively calls itself for the two sub-arrays on either side of the now-placed pivot.

**`partition(arr, low, high)` Function (Lomuto partition scheme):**
- Chooses a `pivot` (in this common implementation, the last element).
- Initializes an `index i` (the "wall") to `low - 1`. This `index` tracks the boundary of elements smaller than the pivot.
- Iterates through the array from `low` to `high-1` with another `index j`.
- If an element `arr[j]` is found to be less than or equal to the `pivot`, the "wall" `i` is incremented, and `arr[i]` is swapped with `arr[j]`. This moves the smaller element behind the wall.
- After the loop, the pivot element (originally at `arr[high]`) is swapped with the element at `arr[i + 1]`. This places the pivot correctly, with all smaller elements to its left and larger elements to its right.
- The function returns the final sorted position of the pivot (`i + 1`).

[Back to Implementation](#implementation)

## Applications

### Application

`Quick Sort` is one of the most widely used general-purpose sorting algorithms, often outperforming `Merge Sort` and `Heap Sort` in practice due to its smaller constant factors and good cache performance.
- **Standard Library Implementations:** Many standard library sort functions use a hybrid algorithm called `Introsort`, which starts with `Quick Sort` and switches to `Heap Sort` if the recursion depth gets too large (to avoid worst-case `O(N^2)`), and then switches to `Insertion Sort` for small partitions.
- **Large Datasets:** It's an excellent choice for sorting large arrays in-memory.
- **Recursive Algorithms:** Its "divide and conquer" nature makes it a useful building block in other algorithms, such as finding the k-th smallest element in an unsorted array (Quickselect).

