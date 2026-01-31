---
title: "Bubble Sort"
---

`Bubble Sort` is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted. The algorithm gets its name because smaller elements "bubble" to the top of the list.

While simple to understand and implement, `Bubble Sort` is too slow for most practical applications, with a time complexity of `O(N^2)`.

## How it Works

### How it Works (Expanded)

`Bubble Sort` works by repeatedly comparing adjacent elements and swapping them if they are out of order. After the first pass, the largest element will have "bubbled up" to the very end of the array. After the second pass, the second-largest element will be in its correct position, and so on.

---

Example: Sort [5, 1, 4, 2, 8]

Pass 1:
( 5 1 4 2 8 ) -> ( 1 5 4 2 8 ) Swap 5 and 1
( 1 5 4 2 8 ) -> ( 1 4 5 2 8 ) Swap 5 and 4
( 1 4 5 2 8 ) -> ( 1 4 2 5 8 ) Swap 5 and 2
( 1 4 2 5 8 ) -> ( 1 4 2 5 8 ) No swap (8 > 5)
Result after Pass 1: [1, 4, 2, 5, 8] (Largest element, 8, is at the end)

Pass 2:
( 1 4 2 5 8 ) -> ( 1 4 2 5 8 ) No swap
( 1 4 2 5 8 ) -> ( 1 2 4 5 8 ) Swap 4 and 2
( 1 2 4 5 8 ) -> ( 1 2 4 5 8 ) No swap
Result after Pass 2: [1, 2, 4, 5, 8] (Second largest, 5, is in place)

... and so on, until no swaps are needed in a full pass.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        swapped = False
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break
    return arr

# Example
# my_arr = [5, 1, 4, 2, 8]
# print(bubble_sort(my_arr)) # [1, 2, 4, 5, 8]
```

### Javascript

```javascript
function bubbleSort(arr) {
    const n = arr.length;
    for (let i = 0; i < n; i++) {
        // Last i elements are already in place
        let swapped = false;
        for (let j = 0; j < n - i - 1; j++) {
            // Traverse the array from 0 to n-i-1
            // Swap if the element found is greater than the next element
            if (arr[j] > arr[j + 1]) {
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]]; // ES6 destructuring swap
                swapped = true;
            }
        }
        // If no two elements were swapped by inner loop, then break
        if (!swapped) {
            break;
        }
    }
    return arr;
}

// const myArr = [5, 1, 4, 2, 8];
// console.log(bubbleSort(myArr)); // [1, 2, 4, 5, 8]
```

### Typescript

```typescript
function bubbleSortTS(arr: number[]): number[] {
    const n = arr.length;
    for (let i = 0; i < n; i++) {
        // Last i elements are already in place
        let swapped = false;
        for (let j = 0; j < n - i - 1; j++) {
            // Traverse the array from 0 to n-i-1
            // Swap if the element found is greater than the next element
            if (arr[j] > arr[j + 1]) {
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
                swapped = true;
            }
        }
        // If no two elements were swapped by inner loop, then break
        if (!swapped) {
            break;
        }
    }
    return arr;
}

// const myArrTS: number[] = [5, 1, 4, 2, 8];
// console.log(bubbleSortTS(myArrTS)); // [1, 2, 4, 5, 8]
```

### Cpp

```cpp
#include <vector>
#include <utility> // For std::swap

void bubbleSort(std::vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n; ++i) {
        // Last i elements are already in place
        bool swapped = false;
        for (int j = 0; j < n - i - 1; ++j) {
            // Traverse the array from 0 to n-i-1
            // Swap if the element found is greater than the next element
            if (arr[j] > arr[j + 1]) {
                std::swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        // If no two elements were swapped by inner loop, then break
        if (!swapped) {
            break;
        }
    }
}

// #include <iostream>
// int main() {
//     std::vector<int> myArr = {5, 1, 4, 2, 8};
//     bubbleSort(myArr);
//     for(int val : myArr) {
//         std::cout << val << " "; // 1 2 4 5 8
//     }
//     std::cout << std::endl;
// }
```

### Go

```go
package main

func bubbleSort(arr []int) []int {
    n := len(arr)
    for i := 0; i < n; i++ {
        // Last i elements are already in place
        swapped := false
        for j := 0; j < n-i-1; j++ {
            // Traverse the array from 0 to n-i-1
            // Swap if the element found is greater than the next element
            if arr[j] > arr[j+1] {
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = true
            }
        }
        // If no two elements were swapped by inner loop, then break
        if !swapped {
            break
        }
    }
    return arr
}

// import "fmt"
// func main() {
//     myArr := []int{5, 1, 4, 2, 8}
//     fmt.Println(bubbleSort(myArr)) // [1 2 4 5 8]
// }
```

### D

```d
import std.algorithm;

void bubbleSort(int[] arr) {
    auto n = arr.length;
    for (int i = 0; i < n; i++) {
        // Last i elements are already in place
        bool swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            // Traverse the array from 0 to n-i-1
            // Swap if the element found is greater than the next element
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        // If no two elements were swapped by inner loop, then break
        if (!swapped) {
            break;
        }
    }
}

// import std.stdio;
// void main() {
//     auto myArr = [5, 1, 4, 2, 8];
//     bubbleSort(myArr);
//     writeln(myArr); // [1, 2, 4, 5, 8]
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

The implementation of `Bubble Sort` uses two nested loops. The outer loop runs `N` times, and with each pass, it reduces the size of the inner loop's comparison range, since the largest elements are progressively moved to the end of the array.

---

**Outer Loop (`i`):** This loop controls the number of passes. After `i` passes, the last `i` elements of the array are guaranteed to be in their final sorted positions.

**Inner Loop (`j`):** This loop iterates from the beginning of the array up to `n-i-1`. It performs the core comparison and swap.

**Swap Condition:** If `arr[j]` is greater than its adjacent element `arr[j+1]`, their positions are swapped.

**Optimization:** A `swapped` flag is used. If the inner loop completes a full pass without making any swaps, it means the array is already sorted, and the outer loop can be terminated early using `break`. This gives `Bubble Sort` a best-case time complexity of `O(N)`.

[Back to Implementation](#implementation)

## Applications

### Application

Due to its poor performance, `Bubble Sort` is almost never used in production code. Its primary use is educational: it is often one of the first sorting algorithms taught because of its simplicity and the straightforward nature of its logic. It serves as a good introduction to the concept of sorting and the analysis of algorithm complexity before moving on to more efficient algorithms like `Merge Sort` or `Quick Sort`.

