---
title: "Radix Sort"
---

`Radix Sort` is a non-comparative sorting algorithm that sorts integers by processing individual digits. It groups `keys` by the individual digits which share the same significant position and value. `Radix sort` can be applied to data that can be sorted lexicographically, such as integers, words, and email addresses.

For `elements` with `d` digits (or characters) and a `radix` (base) of `b`, `Radix Sort` can sort in `O(d <em> (n + b))` time, which can be faster than comparison-based sorts like `Quick Sort` or `Merge Sort` (`O(N log N)`) for certain datasets.

## How it Works

### How it Works (Expanded)

`Radix Sort` works by sorting the input array digit by digit, starting from the least significant digit to the most significant digit (`LSD Radix Sort`), or vice-versa (`MSD Radix Sort`). The `LSD` approach is more common.

---

Example: Sort [170, 45, 75, 90, 802, 24, 2, 66] (LSD Radix Sort)

Original Array: [170, 45, 75, 90, 802, 24, 2, 66]

1. Sort by the last digit (1s place):
- Buckets:
- 0: [170, 90]
- 2: [802, 2]
- 4: [24]
- 5: [45, 75]
- 6: [66]
- Resulting array: [170, 90, 802, 2, 24, 45, 75, 66]

2. Sort by the second to last digit (10s place):
- Buckets:
- 0: [802, 2]
- 2: [24]
- 4: [45]
- 6: [66]
- 7: [170, 75]
- 9: [90]
- Resulting array: [802, 2, 24, 45, 66, 170, 75, 90]

3. Sort by the most significant digit (100s place):
- Buckets:
- 0: [2, 24, 45, 66, 75, 90]
- 1: [170]
- 8: [802]
- Resulting array: [2, 24, 45, 66, 75, 90, 170, 802] (Sorted!)

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] <em> n
    count = [0] </em> 10

    # Store count of occurrences in count[]
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the output array to arr[], so that arr now
    # contains sorted numbers according to current digit
    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    # Find the maximum number to know number of digits
    if not arr:
        return arr
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number.
    exp = 1
    while max1 // exp > 0:
        counting_sort(arr, exp)
        exp <em>= 10
    return arr

# Example
# my_arr = [170, 45, 75, 90, 802, 24, 2, 66]
# print(radix_sort(my_arr)) # [2, 24, 45, 66, 75, 90, 170, 802]
```

### Javascript

```javascript
function countingSort(arr, exp) {
    let n = arr.length;
    let output = new Array(n).fill(0);
    let count = new Array(10).fill(0);

    // Store count of occurrences
    for (let i = 0; i < n; i++) {
        let index = Math.floor(arr[i] / exp);
        count[index % 10]++;
    }

    // Change count[i] to store actual position
    for (let i = 1; i < 10; i++) {
        count[i] += count[i - 1];
    }

    // Build the output array
    for (let i = n - 1; i >= 0; i--) {
        let index = Math.floor(arr[i] / exp);
        output[count[index % 10] - 1] = arr[i];
        count[index % 10]--;
    }

    // Copy output array to arr
    for (let i = 0; i < n; i++) {
        arr[i] = output[i];
    }
}

function radixSort(arr) {
    if (arr.length === 0) {
        return arr;
    }
    // Find the maximum number
    let max1 = Math.max(...arr);

    // Do counting sort for every digit
    for (let exp = 1; Math.floor(max1 / exp) > 0; exp </em>= 10) {
        countingSort(arr, exp);
    }
    return arr;
}

// const myArr = [170, 45, 75, 90, 802, 24, 2, 66];
// console.log(radixSort(myArr)); // [2, 24, 45, 66, 75, 90, 170, 802]
```

### Typescript

```typescript
function countingSortTS(arr: number[], exp: number): void {
    let n = arr.length;
    let output: number[] = new Array(n).fill(0);
    let count: number[] = new Array(10).fill(0);

    // Store count of occurrences
    for (let i = 0; i < n; i++) {
        let index = Math.floor(arr[i] / exp);
        count[index % 10]++;
    }

    // Change count[i] to store actual position
    for (let i = 1; i < 10; i++) {
        count[i] += count[i - 1];
    }

    // Build the output array
    for (let i = n - 1; i >= 0; i--) {
        let index = Math.floor(arr[i] / exp);
        output[count[index % 10] - 1] = arr[i];
        count[index % 10]--;
    }

    // Copy output array to arr
    for (let i = 0; i < n; i++) {
        arr[i] = output[i];
    }
}

function radixSortTS(arr: number[]): number[] {
    if (arr.length === 0) {
        return arr;
    }
    // Find the maximum number
    let max1 = Math.max(...arr);

    // Do counting sort for every digit
    for (let exp = 1; Math.floor(max1 / exp) > 0; exp <em>= 10) {
        countingSortTS(arr, exp);
    }
    return arr;
}

// const myArrTS: number[] = [170, 45, 75, 90, 802, 24, 2, 66];
// console.log(radixSortTS(myArrTS)); // [2, 24, 45, 66, 75, 90, 170, 802]
```

### Cpp

```cpp
#include <vector>
#include <iostream>
#include <algorithm> // For std::max_element

void countingSort(std::vector<int>& arr, int exp) {
    int n = arr.size();
    std::vector<int> output(n);
    std::vector<int> count(10, 0);

    // Store count of occurrences
    for (int i = 0; i < n; i++) {
        int index = arr[i] / exp;
        count[index % 10]++;
    }

    // Change count[i] to store actual position
    for (int i = 1; i < 10; i++) {
        count[i] += count[i - 1];
    }

    // Build the output array
    for (int i = n - 1; i >= 0; i--) {
        int index = arr[i] / exp;
        output[count[index % 10] - 1] = arr[i];
        count[index % 10]--;
    }

    // Copy output array to arr
    for (int i = 0; i < n; i++) {
        arr[i] = output[i];
    }
}

void radixSort(std::vector<int>& arr) {
    if (arr.empty()) {
        return;
    }
    // Find the maximum number
    int max1 = </em>std::max_element(arr.begin(), arr.end());

    // Do counting sort for every digit
    for (int exp = 1; max1 / exp > 0; exp <em>= 10) {
        countingSort(arr, exp);
    }
}

// int main() {
//     std::vector<int> myArr = {170, 45, 75, 90, 802, 24, 2, 66};
//     radixSort(myArr);
//     for(int val : myArr) {
//         std::cout << val << " "; // 2 24 45 66 75 90 170 802
//     }
//     std::cout << std::endl;
// }
```

### Go

```go
package main

import "fmt"

func countingSort(arr []int, exp int) {
    n := len(arr)
    output := make([]int, n)
    count := make([]int, 10)

    // Store count of occurrences
    for i := 0; i < n; i++ {
        index := arr[i] / exp
        count[index%10]++
    }

    // Change count[i] to store actual position
    for i := 1; i < 10; i++ {
        count[i] += count[i-1]
    }

    // Build the output array
    for i := n - 1; i >= 0; i-- {
        index := arr[i] / exp
        output[count[index%10]-1] = arr[i]
        count[index%10]--
    }

    // Copy output array to arr
    for i := 0; i < n; i++ {
        arr[i] = output[i]
    }
}

func radixSort(arr []int) []int {
    if len(arr) == 0 {
        return arr
    }
    // Find the maximum number
    max1 := arr[0]
    for _, val := range arr {
        if val > max1 {
            max1 = val
        }
    }

    // Do counting sort for every digit
    for exp := 1; max1/exp > 0; exp </em>= 10 {
        countingSort(arr, exp)
    }
    return arr
}

// func main() {
//     myArr := []int{170, 45, 75, 90, 802, 24, 2, 66}
//     fmt.Println(radixSort(myArr)) // [2 24 45 66 75 90 170 802]
// }
```

### D

```d
import std.stdio;
import std.array;
import std.algorithm;

void countingSort(ref int[] arr, int exp) {
    auto n = arr.length;
    auto output = new int[n];
    auto count = new int[10]; // Initialize with zeros

    // Store count of occurrences
    foreach (i; 0..n) {
        auto index = arr[i] / exp;
        count[index % 10]++;
    }

    // Change count[i] to store actual position
    foreach (i; 1..10) {
        count[i] += count[i - 1];
    }

    // Build the output array
    for (int i = cast(int)n - 1; i >= 0; i--) {
        auto index = arr[i] / exp;
        output[count[index % 10] - 1] = arr[i];
        count[index % 10]--;
    }

    // Copy output array to arr
    arr[] = output[];
}

void radixSort(ref int[] arr) {
    if (arr.empty) {
        return;
    }
    // Find the maximum number
    auto max1 = arr.maxElement();

    // Do counting sort for every digit
    for (int exp = 1; max1 / exp > 0; exp *= 10) {
        countingSort(arr, exp);
    }
}

// void main() {
//     auto myArr = [170, 45, 75, 90, 802, 24, 2, 66];
//     radixSort(myArr);
//     writeln(myArr); // [2, 24, 45, 66, 75, 90, 170, 802]
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

`Radix Sort` relies on a stable sorting subroutine, typically `Counting Sort`, to sort the numbers based on each digit's place value.

---

**`radixSort(arr)` Function:**
- Finds the maximum number in the `array` to determine how many digits we need to sort by (i.e., how many passes are needed).
- It iterates from the least significant digit (LSD) to the most significant digit (MSD). It uses an `exponent` variable (`exp`) that starts at 1 and is multiplied by 10 in each iteration to isolate the 1s place, 10s place, 100s place, and so on.
- In each iteration, it calls `countingSort` on the entire `array`, passing the current `exponent` to tell `countingSort` which digit to sort by.

**`countingSort(arr, exp)` Function:**
- Creates a `count` array of size 10 to store the frequencies of each digit (0-9).
- Populates the `count` array by iterating through the input `array`. For each number, it isolates the relevant digit using `(number / exp) % 10`.
- Modifies the `count` array into a cumulative sum. Now, `count[i]` stores the final position in the `output` array of the last number with digit `i`.
- Builds the `output` array by iterating through the input `array` in reverse (to maintain stability). For each number, it places it in its correct sorted position in the `output` array based on the `count` array.
- Finally, it copies the `output` array back to the original `array`.

[Back to Implementation](#implementation)

## Applications

### Application

Radix Sort is extremely efficient for sorting integers or strings with fixed-size keys.
- **Sorting Large Integer Sets:** It's a common choice in applications that need to sort a large number of integers, especially when the range of numbers is known.
- **Suffix Array Construction:** Some advanced algorithms for constructing Suffix Arrays use Radix Sort as a subroutine.
- **Data Processing:** In ETL (Extract, Transform, Load) pipelines, it can be used to sort large datasets of integer or string keys before further processing.
- **Parallel Sorting:** Radix Sort can be parallelized effectively, as each digit-based pass can be distributed across multiple processors.

