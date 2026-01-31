---
title: "Merge Sort"
---

`Merge Sort` is a highly efficient, general-purpose, comparison-based sorting algorithm. It is a "`divide and conquer`" algorithm, which means it breaks a problem down into smaller, more manageable subproblems, solves them, and then combines the solutions to solve the original problem.

Unlike `Bubble Sort`, `Selection Sort`, or `Insertion Sort`, `Merge Sort` has a time complexity of `O(N log N)` in all cases (best, average, and worst). Its main disadvantage is that it requires additional memory space to store the sub-arrays, making it an "out-of-place" sorting algorithm.

## How it Works

### How it Works (Expanded)

The `Merge Sort` algorithm works in two main phases: the **Divide** phase and the **Conquer (Merge)** phase.

---

Example: Sort [38, 27, 43, 3, 9, 82, 10]

1. Divide Phase:
- Split: [38, 27, 43, 3] and [9, 82, 10]
- Split: [38, 27], [43, 3] and [9, 82], [10]
- Split: [38], [27], [43], [3] and [9], [82], [10]
   (Now we have arrays of size 1, which are trivially sorted)

2. Conquer (Merge) Phase:
- Merge [38] and [27] -> [27, 38]
- Merge [43] and [3]  -> [3, 43]
- Merge [9] and [82]  -> [9, 82]
- [10] is already sorted.
- Merge [27, 38] and [3, 43] -> [3, 27, 38, 43]
- Merge [9, 82] and [10]    -> [9, 10, 82]
- Merge [3, 27, 38, 43] and [9, 10, 82] -> [3, 9, 10, 27, 38, 43, 82] (Final sorted array)

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive call on each half
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the two sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# Example
# my_arr = [38, 27, 43, 3, 9, 82, 10]
# print(merge_sort(my_arr)) # [3, 9, 10, 27, 38, 43, 82]
```

### Javascript

```javascript
function mergeSort(arr) {
    if (arr.length <= 1) {
        return arr;
    }

    const mid = Math.floor(arr.length / 2);
    const leftHalf = arr.slice(0, mid);
    const rightHalf = arr.slice(mid);

    // Recursive call on each half
    const sortedLeft = mergeSort(leftHalf);
    const sortedRight = mergeSort(rightHalf);

    // Merge the two sorted halves
    return merge(sortedLeft, sortedRight);
}

function merge(left, right) {
    let resultArray = [], leftIndex = 0, rightIndex = 0;

    while (leftIndex < left.length && rightIndex < right.length) {
        if (left[leftIndex] < right[rightIndex]) {
            resultArray.push(left[leftIndex]);
            leftIndex++;
        } else {
            resultArray.push(right[rightIndex]);
            rightIndex++;
        }
    }
    
    // Concatenate remaining elements
    return resultArray
        .concat(left.slice(leftIndex))
        .concat(right.slice(rightIndex));
}

// const myArr = [38, 27, 43, 3, 9, 82, 10];
// console.log(mergeSort(myArr)); // [3, 9, 10, 27, 38, 43, 82]
```

### Typescript

```typescript
function mergeSortTS(arr: number[]): number[] {
    if (arr.length <= 1) {
        return arr;
    }

    const mid = Math.floor(arr.length / 2);
    const leftHalf = arr.slice(0, mid);
    const rightHalf = arr.slice(mid);

    // Recursive call on each half
    const sortedLeft = mergeSortTS(leftHalf);
    const sortedRight = mergeSortTS(rightHalf);

    // Merge the two sorted halves
    return mergeTS(sortedLeft, sortedRight);
}

function mergeTS(left: number[], right: number[]): number[] {
    let resultArray: number[] = [], leftIndex = 0, rightIndex = 0;

    while (leftIndex < left.length && rightIndex < right.length) {
        if (left[leftIndex] < right[rightIndex]) {
            resultArray.push(left[leftIndex]);
            leftIndex++;
        } else {
            resultArray.push(right[rightIndex]);
            rightIndex++;
        }
    }
    
    // Concatenate remaining elements
    return resultArray
        .concat(left.slice(leftIndex))
        .concat(right.slice(rightIndex));
}

// const myArrTS: number[] = [38, 27, 43, 3, 9, 82, 10];
// console.log(mergeSortTS(myArrTS)); // [3, 9, 10, 27, 38, 43, 82]
```

### Cpp

```cpp
#include <vector>
#include <iostream>

// Merge two sorted subarrays into one sorted array
void merge(std::vector<int>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    // Create temp arrays
    std::vector<int> L(n1);
    std::vector<int> R(n2);

    // Copy data to temp arrays L[] and R[]
    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    // Merge the temp arrays back into arr[left..right]
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    // Copy the remaining elements of L[], if any
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    // Copy the remaining elements of R[], if any
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

// Main function that sorts arr[left..right] using merge()
void mergeSort(std::vector<int>& arr, int left, int right) {
    if (left < right) {
        // Same as (left+right)/2, but avoids overflow for large left and h
        int mid = left + (right - left) / 2;

        // Sort first and second halves
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        merge(arr, left, mid, right);
    }
}

// int main() {
//     std::vector<int> myArr = {38, 27, 43, 3, 9, 82, 10};
//     mergeSort(myArr, 0, myArr.size() - 1);
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

func mergeSort(arr []int) []int {
    if len(arr) <= 1 {
        return arr
    }

    mid := len(arr) / 2
    leftHalf := arr[:mid]
    rightHalf := arr[mid:]

    // Recursive call on each half
    sortedLeft := mergeSort(leftHalf)
    sortedRight := mergeSort(rightHalf)

    // Merge the two sorted halves
    return merge(sortedLeft, sortedRight)
}

func merge(left, right []int) []int {
    resultArray := make([]int, 0, len(left)+len(right))
    leftIndex, rightIndex := 0, 0

    for leftIndex < len(left) && rightIndex < len(right) {
        if left[leftIndex] < right[rightIndex] {
            resultArray = append(resultArray, left[leftIndex])
            leftIndex++
        } else {
            resultArray = append(resultArray, right[rightIndex])
            rightIndex++
        }
    }
    
    // Append remaining elements
    resultArray = append(resultArray, left[leftIndex:]...)
    resultArray = append(resultArray, right[rightIndex:]...)
    
    return resultArray
}

// func main() {
//     myArr := []int{38, 27, 43, 3, 9, 82, 10}
//     fmt.Println(mergeSort(myArr)) // [3 9 10 27 38 43 82]
// }
```

### D

```d
import std.stdio;
import std.array;

int[] mergeSort(int[] arr) {
    if (arr.length <= 1) {
        return arr;
    }

    auto mid = arr.length / 2;
    auto leftHalf = arr[0 .. mid];
    auto rightHalf = arr[mid .. $];

    // Recursive call on each half
    auto sortedLeft = mergeSort(leftHalf.dup); // Use .dup to create copies
    auto sortedRight = mergeSort(rightHalf.dup);

    // Merge the two sorted halves
    return merge(sortedLeft, sortedRight);
}

int[] merge(int[] left, int[] right) {
    int[] resultArray;
    int leftIndex = 0, rightIndex = 0;

    while (leftIndex < left.length && rightIndex < right.length) {
        if (left[leftIndex] < right[rightIndex]) {
            resultArray ~= left[leftIndex];
            leftIndex++;
        } else {
            resultArray ~= right[rightIndex];
            rightIndex++;
        }
    }

    // Append remaining elements
    resultArray ~= left[leftIndex .. $];
    resultArray ~= right[rightIndex .. $];
    
    return resultArray;
}

// void main() {
//     auto myArr = [38, 27, 43, 3, 9, 82, 10];
//     writeln(mergeSort(myArr.dup)); // [3, 9, 10, 27, 38, 43, 82]
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

`Merge Sort` is a classic example of a recursive "`divide and conquer`" algorithm. The core logic is split between the recursive division of the `array` and the merging of sorted sub-arrays.

---

**`mergeSort(arr)` Function:**
- **Base Case:** If the `array` has 0 or 1 `elements`, it is already sorted, so it is returned as is. This is the condition that stops the recursion.
- **Divide:** The `array` is split into two halves, `leftHalf` and `rightHalf`.
- **Conquer:** The `mergeSort` function is called recursively on both `leftHalf` and `rightHalf`. This continues until the base case is reached for all sub-arrays.
- **Combine:** Once the recursive calls return, we have two sorted sub-arrays (`sortedLeft` and `sortedRight`). These are then merged by the `merge` function.

**`merge(left, right)` Function:**
- Creates an empty `resultArray`.
- Uses two pointers, `leftIndex` and `rightIndex`, to iterate through the `left` and `right` sub-arrays.
- In a `while` loop, it compares `left[leftIndex]` and `right[rightIndex]`. The smaller of the two is pushed to `resultArray`, and its respective `index` is incremented.
- After the loop, one of the sub-arrays might still have remaining `elements` (because it contained the larger `values`). These remaining `elements` are concatenated to the end of `resultArray`.
- The fully merged and sorted `resultArray` is returned.

[Back to Implementation](#implementation)

## Applications

### Application

Merge Sort is a highly reliable and efficient sorting algorithm with a guaranteed `O(N log N)` performance. It is a stable sort, meaning it preserves the relative order of equal elements.
- **External Sorting:** Because it works by merging chunks, it is very effective for sorting large files that do not fit into memory. Data can be read from disk in chunks, sorted, and then merged back together.
- **General-Purpose Sorting in Standard Libraries:** It is often used in the implementation of standard library sorting functions, sometimes as part of a hybrid algorithm (like `Timsort`, used in Python and Java).
- **Inversion Counting:** The merge step can be easily adapted to count the number of inversions in an array.
- **Parallel and Distributed Computing:** The "divide and conquer" approach is naturally parallelizable, as the sub-arrays can be sorted independently on different threads or machines before the final merge.

