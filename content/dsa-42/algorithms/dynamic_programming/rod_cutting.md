---
title: "Rod Cutting Problem"
---

The `Rod Cutting Problem` is a classic optimization problem that can be efficiently solved using `dynamic programming`. Given a rod of length `N` and a table of `prices` for `pieces` of various lengths, the goal is to cut the rod into smaller `pieces` to maximize the total `price` obtained. Each `piece` of length `i` has a corresponding `price[i-1]` (assuming 0-indexed `prices` array).

The key challenge is that we can cut the rod into any number of `pieces`, and `pieces` of the same length can be used multiple times.

## How it Works

### How it Works (Expanded)

The `Rod Cutting Problem` has optimal substructure and overlapping subproblems, making it suitable for `dynamic programming`. We define `dp[i]` as the maximum `price` obtainable from a rod of length `i`.

---

Example: Rod Length = 4, Prices = [1, 5, 8, 9] (i.e., length 1 = 1, length 2 = 5, length 3 = 8, length 4 = 9)

dp array of size (N+1), initialized with zeros.
dp = [0, 0, 0, 0, 0]

Iterate for each rod length 'i' from 1 to 4:
  Iterate for each possible cut length 'j' from 1 to i:
    dp[i] = max(dp[i], prices[j-1] + dp[i-j])

Trace:
- dp[0] = 0
- dp[1]: max(prices[0] + dp[0]) = 1 + 0 = 1. dp = [0, 1, 0, 0, 0]
- dp[2]:
- cut 1: prices[0] + dp[1] = 1 + 1 = 2
- cut 2: prices[1] + dp[0] = 5 + 0 = 5
- dp[2] = max(2, 5) = 5. dp = [0, 1, 5, 0, 0]
- dp[3]:
- cut 1: prices[0] + dp[2] = 1 + 5 = 6
- cut 2: prices[1] + dp[1] = 5 + 1 = 6
- cut 3: prices[2] + dp[0] = 8 + 0 = 8
- dp[3] = max(6, 6, 8) = 8. dp = [0, 1, 5, 8, 0]
- dp[4]:
- cut 1: prices[0] + dp[3] = 1 + 8 = 9
- cut 2: prices[1] + dp[2] = 5 + 5 = 10
- cut 3: prices[2] + dp[1] = 8 + 1 = 9
- cut 4: prices[3] + dp[0] = 9 + 0 = 9
- dp[4] = max(9, 10, 9, 9) = 10. dp = [0, 1, 5, 8, 10]

Final dp[4] = 10

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
def rod_cutting(prices, N):
    # dp[i] will store the maximum profit obtainable from a rod of length i
    dp = [0] * (N + 1)
    
    # dp[0] is 0 as no profit from rod of length 0

    # Fill dp table for all rod lengths from 1 to N
    for i in range(1, N + 1):
        max_val = 0
        # For each length i, consider all possible first cuts of length j
        for j in range(1, i + 1):
            # prices array is 0-indexed, so price of length j is prices[j-1]
            max_val = max(max_val, prices[j - 1] + dp[i - j])
        dp[i] = max_val
            
    return dp[N]

# Example
# prices = [1, 5, 8, 9, 10, 17, 17, 20] (prices for lengths 1 to 8)
# N = 4 # Rod length
# print(rod_cutting(prices, N)) # Expected: 10 (cut into two pieces of length 2, 5+5=10)
```

### Javascript

```javascript
function rodCutting(prices, N) {
    // dp[i] will store the maximum profit obtainable from a rod of length i
    const dp = Array(N + 1).fill(0);
    
    // dp[0] is 0 as no profit from rod of length 0

    // Fill dp table for all rod lengths from 1 to N
    for (let i = 1; i <= N; i++) {
        let maxVal = 0;
        // For each length i, consider all possible first cuts of length j
        for (let j = 1; j <= i; j++) {
            // prices array is 0-indexed, so price of length j is prices[j-1]
            maxVal = Math.max(maxVal, prices[j - 1] + dp[i - j]);
        }
        dp[i] = maxVal;
    }
            
    return dp[N];
}

// const prices = [1, 5, 8, 9, 10, 17, 17, 20]; // prices for lengths 1 to 8
// const N = 4; // Rod length
// console.log(rodCutting(prices, N)); // Expected: 10
```

### Typescript

```typescript
function rodCuttingTS(prices: number[], N: number): number {
    // dp[i] will store the maximum profit obtainable from a rod of length i
    const dp: number[] = Array(N + 1).fill(0);
    
    // dp[0] is 0 as no profit from rod of length 0

    // Fill dp table for all rod lengths from 1 to N
    for (let i = 1; i <= N; i++) {
        let maxVal = 0;
        // For each length i, consider all possible first cuts of length j
        for (let j = 1; j <= i; j++) {
            // prices array is 0-indexed, so price of length j is prices[j-1]
            maxVal = Math.max(maxVal, prices[j - 1] + dp[i - j]);
        }
        dp[i] = maxVal;
    }
            
    return dp[N];
}

// const pricesTS = [1, 5, 8, 9, 10, 17, 17, 20]; // prices for lengths 1 to 8
// const NTS = 4; // Rod length
// console.log(rodCuttingTS(pricesTS, NTS)); // Expected: 10
```

### Cpp

```cpp
#include <vector>
#include <iostream>
#include <algorithm> // For std::max

int rodCutting(const std::vector<int>& prices, int N) {
    // dp[i] will store the maximum profit obtainable from a rod of length i
    std::vector<int> dp(N + 1, 0);
    
    // dp[0] is 0 as no profit from rod of length 0

    // Fill dp table for all rod lengths from 1 to N
    for (int i = 1; i <= N; i++) {
        int max_val = 0;
        // For each length i, consider all possible first cuts of length j
        for (int j = 1; j <= i; j++) {
            // prices array is 0-indexed, so price of length j is prices[j-1]
            max_val = std::max(max_val, prices[j - 1] + dp[i - j]);
        }
        dp[i] = max_val;
    }
            
    return dp[N];
}

// int main() {
//     std::vector<int> prices = {1, 5, 8, 9, 10, 17, 17, 20}; // prices for lengths 1 to 8
//     int N = 4; // Rod length
//     std::cout << "Max profit for rod of length 4: " << rodCutting(prices, N) << std::endl; // 10
//     return 0;
// }
```

### Go

```go
package main

import "fmt"

func rodCutting(prices []int, N int) int {
    // dp[i] will store the maximum profit obtainable from a rod of length i
    dp := make([]int, N+1)
    
    // dp[0] is 0 as no profit from rod of length 0

    // Fill dp table for all rod lengths from 1 to N
    for i := 1; i <= N; i++ {
        maxVal := 0
        // For each length i, consider all possible first cuts of length j
        for j := 1; j <= i; j++ {
            // prices array is 0-indexed, so price of length j is prices[j-1]
            maxVal = max(maxVal, prices[j-1] + dp[i-j])
        }
        dp[i] = maxVal
    }
            
    return dp[N]
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

// func main() {
//     prices := []int{1, 5, 8, 9, 10, 17, 17, 20} // prices for lengths 1 to 8
//     N := 4 // Rod length
//     fmt.Println("Max profit for rod of length 4:", rodCutting(prices, N)) // 10
// }
```

### D

```d
import std.stdio;
import std.array;
import std.algorithm; // For std.algorithm.max

int rodCutting(int[] prices, int N) {
    // dp[i] will store the maximum profit obtainable from a rod of length i
    auto dp = new int[N + 1]; // Initialize with zeros
    
    // dp[0] is 0 as no profit from rod of length 0

    // Fill dp table for all rod lengths from 1 to N
    foreach (i; 1 .. N + 1) {
        int maxVal = 0;
        // For each length i, consider all possible first cuts of length j
        foreach (j; 1 .. i + 1) {
            // prices array is 0-indexed, so price of length j is prices[j-1]
            maxVal = max(maxVal, prices[j - 1] + dp[i - j]);
        }
        dp[i] = maxVal;
    }
            
    return dp[N];
}

// void main() {
//     auto prices = [1, 5, 8, 9, 10, 17, 17, 20]; // prices for lengths 1 to 8
//     int N = 4; // Rod length
//     writeln("Max profit for rod of length 4: ", rodCutting(prices, N)); // 10
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

The `Rod Cutting Problem` is solved using a 1D `dynamic programming` array, where each element represents the maximum profit for a rod of a specific length.

---

**Initialization:**
- `N`: The total length of the rod.
- `prices`: An array where `prices[k]` is the price for a piece of length `k+1`.
- A 1D `dp` array of size `N + 1` is created. `dp[i]` will store the maximum profit obtainable from a rod of length `i`.
- `dp[0]` is initialized to 0 (a rod of length 0 yields no profit).
- All other `dp[i]` values are initialized to 0.

**Filling the DP Table:**
- The `dp` table is filled iteratively for `i` (representing the current rod length) from 1 to `N`.
- For each `rod length i`, the algorithm aims to find the maximum profit by considering all possible ways to make the first cut.
- It iterates `j` (representing the length of the first piece cut) from 1 to `i`.
- For each `j`, it calculates a potential profit: `prices[j-1]` (the price of the first piece of length `j`) plus `dp[i-j]` (the maximum profit from the remaining rod of length `i-j`).
- `max_val` tracks the highest profit found for the current `rod length i` by comparing all `j` options.
- `dp[i]` is then updated with this `max_val`.

**Result:**
- The final answer, the maximum profit for the original rod of length `N`, is stored in `dp[N]`.

[Back to Implementation](#implementation)

## Applications

### Application

The `Rod Cutting Problem` is a model for various optimization scenarios:
- **Resource Allocation:** Deciding how to best allocate a finite resource (e.g., time, budget, raw material) into smaller, valued units to maximize overall gain.
- **Production Planning:** Optimizing the cutting of raw materials (like metal bars, timber, fabric rolls) into smaller pieces to meet demand while maximizing revenue.
- **Manufacturing:** In industries where products are cut from larger stock, this problem helps determine the most profitable cutting patterns.
- **Service Provision:** Imagine selling services where longer service periods can be broken down into shorter, more profitable segments.
- **Project Management:** Breaking down a large project into smaller tasks with associated costs and benefits, and finding the optimal way to combine them.

