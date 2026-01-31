---
title: "Lis"
---

The `Longest Increasing Subsequence (LIS)` problem is a classic problem in `dynamic programming`. Given an `array` of `numbers`, the goal is to find the length of the longest `subsequence` such that all `elements` of the `subsequence` are in increasing order. A `subsequence` is a sequence that can be derived from another sequence by deleting some or no `elements` without changing the order of the remaining `elements`.

For example, in the `array` `[3, 10, 2, 1, 20]`, the `LIS` is `[3, 10, 20]` with a length of 3.

## How it Works

### How it Works (Expanded)

There are multiple ways to solve the `LIS` problem. The most straightforward approach uses `dynamic programming` with a time complexity of `O(N^2)`. A more optimized approach uses `dynamic programming` with `binary search`, achieving `O(N log N)` time complexity.

---

Example (O(N^2) DP): Array = [3, 10, 2, 1, 20]

dp array will store the length of LIS ending at each index.
- dp[0] for 3:  [3] -> length 1. dp = [1]
- dp[1] for 10: [3, 10] -> length 2. dp = [1, 2]
- dp[2] for 2:  [2] -> length 1. dp = [1, 2, 1]
- dp[3] for 1:  [1] -> length 1. dp = [1, 2, 1, 1]
- dp[4] for 20: [3, 10, 20] or [2, 20] or [1, 20] -> length 3. dp = [1, 2, 1, 1, 3]

Maximum value in dp array is the length of LIS.

Example (O(N log N) with Binary Search): Array = [3, 10, 2, 1, 20]

tails array will store the smallest tail of all increasing subsequences of length i+1.
- [3]: tails = [3]
- [3, 10]: tails = [3, 10]
- [2]: 2 < 3. Replace 3 with 2. tails = [2, 10]
- [1]: 1 < 2. Replace 2 with 1. tails = [1, 10]
- [1, 20]: 20 > 10. Append 20. tails = [1, 10, 20]

Length of LIS is tails.length = 3.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
import bisect

def longest_increasing_subsequence_n_log_n(arr):
    if not arr:
        return 0

    tails = [] # tails[k] is the smallest tail of all increasing subsequences of length k+1

    for num in arr:
        # If num is greater than any tail, it can extend the longest subsequence
        if not tails or num > tails[-1]:
            tails.append(num)
        else:
            # Find the smallest tail that is greater than or equal to num
            # Use bisect_left for binary search: returns insertion point
            idx = bisect.bisect_left(tails, num)
            tails[idx] = num # Replace that tail with num

    return len(tails)

# Example
# arr1 = [3, 10, 2, 1, 20]
# print(longest_increasing_subsequence_n_log_n(arr1)) # Expected: 3 ([3, 10, 20] or [2, 20] or [1, 20])

# arr2 = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
# print(longest_increasing_subsequence_n_log_n(arr2)) # Expected: 6 ([0, 2, 6, 9, 11, 15] etc.)
```

### Javascript

```javascript
function longestIncreasingSubsequenceNLogN(arr) {
    if (arr.length === 0) {
        return 0;
    }

    const tails = []; // tails[k] is the smallest tail of all increasing subsequences of length k+1

    for (const num of arr) {
        if (tails.length === 0 || num > tails[tails.length - 1]) {
            tails.push(num);
        } else {
            // Find the smallest tail that is greater than or equal to num
            // Binary search to find the index to replace
            let low = 0;
            let high = tails.length - 1;
            let idx = -1;

            while (low <= high) {
                const mid = Math.floor((low + high) / 2);
                if (tails[mid] >= num) {
                    idx = mid;
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }
            if (idx !== -1) {
                tails[idx] = num;
            }
        }
    }

    return tails.length;
}

// const arr1 = [3, 10, 2, 1, 20];
// console.log(longestIncreasingSubsequenceNLogN(arr1)); // Expected: 3

// const arr2 = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15];
// console.log(longestIncreasingSubsequenceNLogN(arr2)); // Expected: 6
```

### Typescript

```typescript
function longestIncreasingSubsequenceNLogNTS(arr: number[]): number {
    if (arr.length === 0) {
        return 0;
    }

    const tails: number[] = []; // tails[k] is the smallest tail of all increasing subsequences of length k+1

    for (const num of arr) {
        if (tails.length === 0 || num > tails[tails.length - 1]) {
            tails.push(num);
        } else {
            // Find the smallest tail that is greater than or equal to num
            // Binary search to find the index to replace
            let low = 0;
            let high = tails.length - 1;
            let idx = -1;

            while (low <= high) {
                const mid = Math.floor((low + high) / 2);
                if (tails[mid] >= num) {
                    idx = mid;
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }
            if (idx !== -1) {
                tails[idx] = num;
            }
        }
    }

    return tails.length;
}

// const arr1TS = [3, 10, 2, 1, 20];
// console.log(longestIncreasingSubsequenceNLogNTS(arr1TS)); // Expected: 3

// const arr2TS = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15];
// console.log(longestIncreasingSubsequenceNLogNTS(arr2TS)); // Expected: 6
```

### Cpp

```cpp
#include <vector>
#include <iostream>
#include <algorithm> // For std::lower_bound

int longestIncreasingSubsequenceNLogN(const std::vector<int>& arr) {
    if (arr.empty()) {
        return 0;
    }

    std::vector<int> tails; // tails[k] is the smallest tail of all increasing subsequences of length k+1

    for (int num : arr) {
        // If num is greater than any tail, it can extend the longest subsequence
        if (tails.empty() || num > tails.back()) {
            tails.push_back(num);
        } else {
            // Find the smallest tail that is greater than or equal to num
            // std::lower_bound returns an iterator to the first element not less than num
            auto it = std::lower_bound(tails.begin(), tails.end(), num);
            <em>it = num; // Replace that tail with num
        }
    }

    return tails.size();
}

// int main() {
//     std::vector<int> arr1 = {3, 10, 2, 1, 20};
//     std::cout << "LIS length for arr1: " << longestIncreasingSubsequenceNLogN(arr1) << std::endl; // 3

//     std::vector<int> arr2 = {0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15};
//     std::cout << "LIS length for arr2: " << longestIncreasingSubsequenceNLogN(arr2) << std::endl; // 6
//     return 0;
// }
```

### Go

```go
package main

import (
    "fmt"
    "sort"
)

func longestIncreasingSubsequenceNLogN(arr []int) int {
    if len(arr) == 0 {
        return 0
    }

    tails := []int{} // tails[k] is the smallest tail of all increasing subsequences of length k+1

    for _, num := range arr {
        if len(tails) == 0 || num > tails[len(tails)-1] {
            tails = append(tails, num)
        } else {
            // Find the smallest tail that is greater than or equal to num
            // using binary search (sort.SearchInts returns the index to insert)
            idx := sort.SearchInts(tails, num)
            tails[idx] = num // Replace that tail with num
        }
    }

    return len(tails)
}

// func main() {
//     arr1 := []int{3, 10, 2, 1, 20}
//     fmt.Println("LIS length for arr1:", longestIncreasingSubsequenceNLogN(arr1)) // 3

//     arr2 := []int{0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15}
//     fmt.Println("LIS length for arr2:", longestIncreasingSubsequenceNLogN(arr2)) // 6
// }
```

### D

```d
import std.stdio;
import std.array;
import std.algorithm; // For std.algorithm.lowerBound

int longestIncreasingSubsequenceNLogN(int[] arr) {
    if (arr.empty) {
        return 0;
    }

    int[] tails; // tails[k] is the smallest tail of all increasing subsequences of length k+1

    foreach (num; arr) {
        // If num is greater than any tail, it can extend the longest subsequence
        if (tails.empty || num > tails.back) {
            tails ~= num;
        } else {
            // Find the smallest tail that is greater than or equal to num
            // lowerBound returns an iterator to the first element not less than num
            auto it = tails.lowerBound(num);
            if (it != tails.end) { // Ensure element found
                </em>it = num; // Replace that tail with num
            }
        }
    }

    return cast(int)tails.length;
}

// void main() {
//     auto arr1 = [3, 10, 2, 1, 20];
//     writeln("LIS length for arr1: ", longestIncreasingSubsequenceNLogN(arr1)); // 3

//     auto arr2 = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15];
//     writeln("LIS length for arr2: ", longestIncreasingSubsequenceNLogN(arr2)); // 6
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

The `Longest Increasing Subsequence` problem can be solved in `O(N log N)` time using a combination of `dynamic programming` and `binary search`. This is a significant optimization over the `O(N^2)` DP approach.

---

**Key Idea (`tails` array):**
- We maintain a `tails array` (or `list`). `tails[k]` stores the smallest *ending element* of all `increasing subsequences` of `length k+1` found so far.
- It's crucial to understand that the `tails` array itself is not an `increasing subsequence`. Instead, its length is the `length` of the `LIS`, and its elements are just the smallest tails.
- The `tails` array will always be sorted in `increasing order`.

**Algorithm Steps:**
- Initialize an empty `tails` array.
- Iterate through each `num` in the input `array`:
- **Case 1: `tails` is empty or `num` is greater than the last element of `tails`.**
- If this is true, `num` can extend the longest `increasing subsequence` found so far. We append `num` to `tails`.

            </li>
- **Case 2: `num` is not greater than the last element of `tails`.**
- This means `num` cannot extend the `LIS` to a new longer length immediately. However, it might be able to form an `increasing subsequence` of the *same length* but with a *smaller tail*. A smaller tail is always better, as it allows more numbers to extend the subsequence later.
- We use `binary search` (`bisect_left` in Python, `lower_bound` in C++, `sort.SearchInts` in Go) to find the smallest `element` in `tails` that is greater than or equal to `num`.
- We replace that `element` with `num`. This operation maintains the sorted property of `tails` and ensures that `tails[k]` always holds the smallest tail for `LIS` of length `k+1`.

            </li>

    </li>

**Result:**
- The final length of the `tails` array is the length of the `Longest Increasing Subsequence`.

[Back to Implementation](#implementation)

## Applications

### Application

The `Longest Increasing Subsequence (LIS)` problem has applications in various fields:
- **Bioinformatics:** Used in analyzing DNA or protein sequences to identify common patterns or structures.
- **Data Mining:** Finding patterns or trends in sequential data, such as stock prices or sensor readings.
- **Job Scheduling:** Optimizing the order of tasks to maximize efficiency, where tasks have dependencies.
- **File Versioning:** Comparing different versions of a file to find out how they evolved, or to reconstruct a sequence of changes.
- **Card Games:** In certain card games, finding the `LIS` can be part of strategy optimization.
- **Compiler Optimization:** In some cases, instruction reordering can be optimized by finding the `LIS` to improve cache performance or reduce dependencies.

