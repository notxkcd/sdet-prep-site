---
title: "Knapsack Problem (0/1 Knapsack)"
---

The `Knapsack Problem` is a classic optimization problem, particularly in the realm of `dynamic programming`. Given a set of `items`, each with a specific `weight` and `value`, and a `knapsack` with a maximum `weight capacity`, the goal is to choose a subset of `items` to put into the `knapsack` such that the total `value` is maximized, and the total `weight` does not exceed the `capacity`.

The "`0/1`" in `0/1 Knapsack` refers to the constraint that for each `item`, you must either take the whole `item` (1) or leave it entirely (0); you cannot take a fraction of an `item`.

## How it Works

### How it Works (Expanded)

The `0/1 Knapsack Problem` is typically solved using `dynamic programming` due to its optimal substructure and overlapping subproblems properties. We build a 2D `DP table` (matrix) where `dp[i][w]` represents the maximum `value` that can be obtained from the first `i` items with a `knapsack capacity` of `w`.

---

Example: Items = {(W=1, V=1), (W=3, V=4), (W=4, V=5), (W=5, V=7)}, Capacity = 7

Initialize dp[i][w] table (items x capacity) with zeros.

For each item `i` and each capacity `w`:
- If current item's weight > `w`: dp[i][w] = dp[i-1][w] (cannot take item)
- Else: dp[i][w] = max(dp[i-1][w], // Don't take item
                      dp[i-1][w - current_item_weight] + current_item_value) // Take item

The final dp[num_items][capacity] will be the max value.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
def knapsack_01(weights, values, capacity):
    num_items = len(weights)
    
    # dp[i][w] stores the maximum value for first i items with capacity w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(num_items + 1)]

    # Fill dp table
    for i in range(1, num_items + 1):
        for w in range(1, capacity + 1):
            current_item_weight = weights[i - 1]
            current_item_value = values[i - 1]

            if current_item_weight > w:
                # Cannot include current item, take value from above
                dp[i][w] = dp[i - 1][w]
            else:
                # Max of (don't include, include)
                dp[i][w] = max(dp[i - 1][w],                          # Don't include item i
                               dp[i - 1][w - current_item_weight] + current_item_value) # Include item i
    
    return dp[num_items][capacity]

# Example
# weights = [1, 3, 4, 5]
# values = [1, 4, 5, 7]
# capacity = 7
# print(knapsack_01(weights, values, capacity)) # Expected: 9 (items with weights 3 and 4, values 4 and 5)
```

### Javascript

```javascript
function knapsack01(weights, values, capacity) {
    const numItems = weights.length;
    
    // dp[i][w] stores the maximum value for first i items with capacity w
    const dp = Array(numItems + 1).fill(0).map(() => Array(capacity + 1).fill(0));

    // Fill dp table
    for (let i = 1; i <= numItems; i++) {
        for (let w = 1; w <= capacity; w++) {
            const currentItemWeight = weights[i - 1];
            const currentItemValue = values[i - 1];

            if (currentItemWeight > w) {
                // Cannot include current item, take value from above
                dp[i][w] = dp[i - 1][w];
            } else {
                // Max of (don't include, include)
                dp[i][w] = Math.max(dp[i - 1][w],                          // Don't include item i
                                    dp[i - 1][w - currentItemWeight] + currentItemValue); // Include item i
            }
        }
    }
    
    return dp[numItems][capacity];
}

// const weights = [1, 3, 4, 5];
// const values = [1, 4, 5, 7];
// const capacity = 7;
// console.log(knapsack01(weights, values, capacity)); // Expected: 9
```

### Typescript

```typescript
function knapsack01TS(weights: number[], values: number[], capacity: number): number {
    const numItems = weights.length;
    
    // dp[i][w] stores the maximum value for first i items with capacity w
    const dp: number[][] = Array(numItems + 1).fill(0).map(() => Array(capacity + 1).fill(0));

    // Fill dp table
    for (let i = 1; i <= numItems; i++) {
        for (let w = 1; w <= capacity; w++) {
            const currentItemWeight = weights[i - 1];
            const currentItemValue = values[i - 1];

            if (currentItemWeight > w) {
                // Cannot include current item, take value from above
                dp[i][w] = dp[i - 1][w];
            } else {
                // Max of (don't include, include)
                dp[i][w] = Math.max(dp[i - 1][w],                          // Don't include item i
                                    dp[i - 1][w - currentItemWeight] + currentItemValue); // Include item i
            }
        }
    }
    
    return dp[numItems][capacity];
}

// const weightsTS = [1, 3, 4, 5];
// const valuesTS = [1, 4, 5, 7];
// const capacityTS = 7;
// console.log(knapsack01TS(weightsTS, valuesTS, capacityTS)); // Expected: 9
```

### Cpp

```cpp
#include <vector>
#include <iostream>
#include <algorithm> // For std::max

int knapsack01(const std::vector<int>& weights, const std::vector<int>& values, int capacity) {
    int num_items = weights.size();
    
    // dp[i][w] stores the maximum value for first i items with capacity w
    std::vector<std::vector<int>> dp(num_items + 1, std::vector<int>(capacity + 1, 0));

    // Fill dp table
    for (int i = 1; i <= num_items; i++) {
        for (int w = 1; w <= capacity; w++) {
            int current_item_weight = weights[i - 1];
            int current_item_value = values[i - 1];

            if (current_item_weight > w) {
                // Cannot include current item, take value from above
                dp[i][w] = dp[i - 1][w];
            } else {
                // Max of (don't include, include)
                dp[i][w] = std::max(dp[i - 1][w],                          // Don't include item i
                                    dp[i - 1][w - current_item_weight] + current_item_value); // Include item i
            }
        }
    }
    
    return dp[num_items][capacity];
}

// int main() {
//     std::vector<int> weights = {1, 3, 4, 5};
//     std::vector<int> values = {1, 4, 5, 7};
//     int capacity = 7;
//     std::cout << "Max value: " << knapsack01(weights, values, capacity) << std::endl; // 9
//     return 0;
// }
```

### Go

```go
package main

import "fmt"

func knapsack01(weights, values []int, capacity int) int {
    numItems := len(weights)
    
    // dp[i][w] stores the maximum value for first i items with capacity w
    dp := make([][]int, numItems+1)
    for i := range dp {
        dp[i] = make([]int, capacity+1)
    }

    // Fill dp table
    for i := 1; i <= numItems; i++ {
        for w := 1; w <= capacity; w++ {
            currentItemWeight := weights[i-1]
            currentItemValue := values[i-1]

            if currentItemWeight > w {
                // Cannot include current item, take value from above
                dp[i][w] = dp[i-1][w]
            } else {
                // Max of (don't include, include)
                dp[i][w] = max(dp[i-1][w],                          // Don't include item i
                               dp[i-1][w-currentItemWeight] + currentItemValue) // Include item i
            }
        }
    }
    
    return dp[numItems][capacity]
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

// func main() {
//     weights := []int{1, 3, 4, 5}
//     values := []int{1, 4, 5, 7}
//     capacity := 7
//     fmt.Println("Max value:", knapsack01(weights, values, capacity)) // 9
// }
```

### D

```d
import std.stdio;
import std.array;
import std.algorithm; // For std.algorithm.max

int knapsack01(int[] weights, int[] values, int capacity) {
    auto numItems = weights.length;
    
    // dp[i][w] stores the maximum value for first i items with capacity w
    auto dp = new int[numItems + 1][capacity + 1];

    // Fill dp table
    foreach (i; 1 .. numItems + 1) {
        foreach (w; 1 .. capacity + 1) {
            auto currentItemWeight = weights[i - 1];
            auto currentItemValue = values[i - 1];

            if (currentItemWeight > w) {
                // Cannot include current item, take value from above
                dp[i][w] = dp[i - 1][w];
            } else {
                // Max of (don't include, include)
                dp[i][w] = max(dp[i - 1][w],                          // Don't include item i
                               dp[i - 1][w - currentItemWeight] + currentItemValue); // Include item i
            }
        }
    }
    
    return dp[numItems][capacity];
}

// void main() {
//     auto weights = [1, 3, 4, 5];
//     auto values = [1, 4, 5, 7];
//     int capacity = 7;
//     writeln("Max value: ", knapsack01(weights, values, capacity)); // 9
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

The `0/1 Knapsack Problem` is solved using a `dynamic programming` approach, building a 2D table to store optimal solutions for subproblems.

---

**Initialization:**
- `num_items`: The total number of items available.
- `capacity`: The maximum weight the knapsack can hold.
- A 2D `dp` table (`num_items+1` rows, `capacity+1` columns) is created and initialized with zeros.
- `dp[i][w]` will store the maximum `value` achievable using the first `i` items with a `knapsack capacity` of `w`.
- `dp[0][w]` and `dp[i][0]` are naturally 0 (no items or no capacity means no value).

    </li>

**Filling the DP Table:**
- The `dp` table is filled iteratively, considering each `item` (`i`) and each possible `capacity` (`w`).
- For each cell `dp[i][w]`:
- Get the `weight` and `value` of the `current item` (which is `item i-1` in the 0-indexed `weights` and `values` arrays).
- **Case 1: `current_item_weight > w`**
- If the `current item`'s `weight` exceeds the `current capacity w`, it cannot be included in the `knapsack`.
- Therefore, the maximum `value` `dp[i][w]` is the same as the maximum `value` without the `current item` (`dp[i-1][w]`).

            </li>
- **Case 2: `current_item_weight <= w`**
- The `current item` can potentially be included. We need to decide whether including it or not yields a better total `value`.
- `dp[i][w]` is the maximum of two options:
- **Option A (Don't include `item i`):** The `value` is `dp[i-1][w]` (the max value using the first `i-1` items with the same `capacity`).
- **Option B (Include `item i`):** The `value` is `current_item_value` plus the maximum `value` obtained from the first `i-1` items with the `remaining capacity` (`w - current_item_weight`).

                    </li>

            </li>

    </li>

**Result:**
- The final answer, the maximum `value` that can be put into the `knapsack`, is found at `dp[num_items][capacity]`.

[Back to Implementation](#implementation)

## Applications

### Application

The `0/1 Knapsack Problem` is a foundational problem in combinatorial optimization with numerous real-world applications:
- **Resource Allocation:** Deciding which projects or tasks to undertake given limited resources (e.g., budget, time, personnel), where each project has a cost (weight) and a benefit (value).
- **Cargo Loading:** Loading a ship or truck with items to maximize the total value of cargo without exceeding the weight limit.
- **Investment Decisions:** Selecting investments to maximize return while staying within a budget.
- **Cuttin Stock:** Optimizing the cutting of materials (e.g., wood, fabric) from larger pieces to minimize waste and maximize yield.
- **Cryptography:** Some cryptographic schemes (like the Merkle-Hellman knapsack cryptosystem, though broken) are based on variations of the knapsack problem.

