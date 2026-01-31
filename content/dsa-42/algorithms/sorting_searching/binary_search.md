---
title: "Binary Search"
---

`Binary Search` is a highly efficient algorithm for finding an item from a **sorted** list of items. It works by repeatedly dividing the search interval in half. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half.

This "divide and conquer" strategy makes it significantly faster than a linear search, which checks every item one by one.

## How it Works

### How it Works (Expanded)

For `Binary Search` to work, the data must be sorted. The algorithm maintains two pointers, a `low` pointer at the start of the array and a `high` pointer at the end.

---

Example: Search for 23 in [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

1. low=0, high=9. mid = (0+9)/2 = 4. Array[4] is 16.
   16 < 23, so the target must be in the right half.
   New range: low=5, high=9.

2. low=5, high=9. mid = (5+9)/2 = 7. Array[7] is 56.
   56 > 23, so the target must be in the left half.
   New range: low=5, high=6.

3. low=5, high=6. mid = (5+6)/2 = 5. Array[5] is 23.
   23 == 23. Found at index 5!

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1 # Not found

# Example
# sorted_arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
# print(binary_search(sorted_arr, 23)) # 5
```

### Javascript

```javascript
function binarySearch(arr, target) {
    let low = 0;
    let high = arr.length - 1;
    while (low <= high) {
        let mid = Math.floor(low + (high - low) / 2);
        if (arr[mid] === target) {
            return mid;
        } else if (arr[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1; // Not found
}

// const sortedArr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91];
// console.log(binarySearch(sortedArr, 23)); // 5
```

### Typescript

```typescript
function binarySearchTS(arr: number[], target: number): number {
    let low = 0;
    let high = arr.length - 1;
    while (low <= high) {
        let mid = Math.floor(low + (high - low) / 2);
        if (arr[mid] === target) {
            return mid;
        } else if (arr[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1; // Not found
}

// const sortedArrTS: number[] = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91];
// console.log(binarySearchTS(sortedArrTS, 23)); // 5
```

### Cpp

```cpp
#include <vector>

int binarySearch(const std::vector<int>& arr, int target) {
    int low = 0;
    int high = arr.size() - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1; // Not found
}

// #include <iostream>
// int main() {
//     std::vector<int> sortedArr = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
//     std::cout << binarySearch(sortedArr, 23) << std::endl; // 5
// }
```

### Go

```go
package main

func binarySearch(arr []int, target int) int {
    low, high := 0, len(arr)-1
    for low <= high {
        mid := low + (high-low)/2
        if arr[mid] == target {
            return mid
        } else if arr[mid] < target {
            low = mid + 1
        } else {
            high = mid - 1
        }
    }
    return -1 // Not found
}

// import "fmt"
// func main() {
//     sortedArr := []int{2, 5, 8, 12, 16, 23, 38, 56, 72, 91}
//     fmt.Println(binarySearch(sortedArr, 23)) // 5
// }
```

### D

```d
import std.stdio;

int binarySearch(const int[] arr, int target) {
    int low = 0;
    int high = cast(int)arr.length - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1; // Not found
}

// void main() {
//     auto sortedArr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91];
//     writeln(binarySearch(sortedArr, 23)); // 5
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

The iterative implementation of `Binary Search` is efficient and avoids the potential for stack overflow that can occur in a recursive implementation with very large arrays.

---

**Key Variables:**
- `low`: The starting index of the current search interval.
- `high`: The ending index of the current search interval.
- `mid`: The middle index of the current interval.

**Logic Flow:**
- Initialize `low` to the start of the array (0) and `high` to the end (`length - 1`).
- The `while` loop continues as long as the search interval is valid (i.e., `low <= high`).
- Inside the loop, the `mid` point is calculated. Using `low + (high - low) / 2` is a safe way to prevent potential integer overflow if `low` and `high` are very large numbers.
- The element at the `mid` index is compared to the `target`.
- If they match, the search is successful, and the `index` is returned.
- If the `mid` element is smaller than the `target`, we know the `target` must be in the upper half of the interval, so we discard the lower half by setting `low = mid + 1`.
- If the `mid` element is larger, we discard the upper half by setting `high = mid - 1`.
- If the loop terminates without finding the element, it means the `target` is not in the array, and we return -1.

[Back to Implementation](#implementation)

## Applications

### Application

Binary Search is a fundamental algorithm used whenever you need to find an element in a sorted collection. Its applications are vast:
- **Searching in Databases:** Finding a record in a sorted index.
- **Autocomplete Features:** Finding the range of possible suggestions for a given prefix.
- **Git Bisect:** The `git bisect` command uses binary search to efficiently find the commit that introduced a bug.
- **Problem Solving:** It is often used to solve problems that involve finding a minimum or maximum value that satisfies a certain condition by searching over the range of possible answers.

