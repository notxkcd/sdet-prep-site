---
title: "Coin Change Problem (Minimum Coins)"
---

The `Coin Change Problem` is a classic problem in `dynamic programming` that asks for the minimum number of coins needed to make a given amount of change. Given a set of coin denominations and a target amount, the goal is to find the fewest coins that sum up to that amount.

This problem assumes an infinite supply of each coin denomination. If a specific amount cannot be made, the algorithm should indicate that (e.g., return -1 or infinity).

## How it Works

### How it Works (Expanded)

The `Coin Change Problem` exhibits optimal substructure and overlapping subproblems, making it well-suited for `dynamic programming`. We build a 1D `DP array` where `dp[i]` stores the minimum number of coins required to make the amount `i`.

---

Example: Coins = [1, 2, 5], Amount = 11

dp array of size (Amount + 1), initialized with infinity, dp[0] = 0.
dp = [0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]

Iterate for each amount 'i' from 1 to 11:
  Iterate for each coin 'c' in coins:
    If c <= i:
      dp[i] = min(dp[i], 1 + dp[i - c])

Trace:
- dp[1]: coins[1] = 1 -> min(inf, 1 + dp[0]) = 1
- dp[2]: coins[1] = 1 -> min(inf, 1 + dp[1]) = 2
         coins[2] = 2 -> min(2, 1 + dp[0]) = 1
- dp[3]: coins[1] = 1 -> min(inf, 1 + dp[2]) = 2
         coins[2] = 2 -> min(2, 1 + dp[1]) = 2
- ...
- dp[11]: coins[1]=1 -> 1+dp[10]=1+2=3
          coins[2]=2 -> 1+dp[9]=1+2=3
          coins[5]=5 -> 1+dp[6]=1+2=3

Final dp[11] = 3 (e.g., 5+5+1 or 5+2+2+2 or ...)

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
def coin_change_min_coins(coins, amount):
    # dp[i] will be storing the minimum number of coins
    # required for amount i.
    dp = [float('inf')] </em> (amount + 1)
    
    # Base case: 0 coins needed for amount 0
    dp[0] = 0

    # Fill dp table for all amounts from 1 to amount
    for i in range(1, amount + 1):
        # For each amount, iterate through all coins
        for coin in coins:
            # If current coin can be used
            if coin <= i:
                # Update dp[i] with the minimum of its current value
                # and 1 (for the current coin) + dp[i - coin]
                dp[i] = min(dp[i], 1 + dp[i - coin])
                
    # If dp[amount] is still infinity, it means amount cannot be made
    return dp[amount] if dp[amount] != float('inf') else -1

# Example
# coins = [1, 2, 5]
# amount = 11
# print(coin_change_min_coins(coins, amount)) # Expected: 3 (5+5+1)

# coins2 = [2]
# amount2 = 3
# print(coin_change_min_coins(coins2, amount2)) # Expected: -1
```

### Javascript

```javascript
function coinChangeMinCoins(coins, amount) {
    // dp[i] will be storing the minimum number of coins
    // required for amount i.
    const dp = Array(amount + 1).fill(Infinity);
    
    // Base case: 0 coins needed for amount 0
    dp[0] = 0;

    // Fill dp table for all amounts from 1 to amount
    for (let i = 1; i <= amount; i++) {
        // For each amount, iterate through all coins
        for (const coin of coins) {
            // If current coin can be used
            if (coin <= i) {
                // Update dp[i] with the minimum of its current value
                // and 1 (for the current coin) + dp[i - coin]
                dp[i] = Math.min(dp[i], 1 + dp[i - coin]);
            }
        }
    }
    
    // If dp[amount] is still infinity, it means amount cannot be made
    return dp[amount] === Infinity ? -1 : dp[amount];
}

// const coins = [1, 2, 5];
// const amount = 11;
// console.log(coinChangeMinCoins(coins, amount)); // Expected: 3

// const coins2 = [2];
// const amount2 = 3;
// console.log(coinChangeMinCoins(coins2, amount2)); // Expected: -1
```

### Typescript

```typescript
function coinChangeMinCoinsTS(coins: number[], amount: number): number {
    // dp[i] will be storing the minimum number of coins
    // required for amount i.
    const dp: number[] = Array(amount + 1).fill(Infinity);
    
    // Base case: 0 coins needed for amount 0
    dp[0] = 0;

    // Fill dp table for all amounts from 1 to amount
    for (let i = 1; i <= amount; i++) {
        // For each amount, iterate through all coins
        for (const coin of coins) {
            // If current coin can be used
            if (coin <= i) {
                // Update dp[i] with the minimum of its current value
                // and 1 (for the current coin) + dp[i - coin]
                dp[i] = Math.min(dp[i], 1 + dp[i - coin]);
            }
        }
    }
    
    // If dp[amount] is still infinity, it means amount cannot be made
    return dp[amount] === Infinity ? -1 : dp[amount];
}

// const coinsTS = [1, 2, 5];
// const amountTS = 11;
// console.log(coinChangeMinCoinsTS(coinsTS, amountTS)); // Expected: 3

// const coins2TS = [2];
// const amount2TS = 3;
// console.log(coinChangeMinCoinsTS(coins2TS, amount2TS)); // Expected: -1
```

### Cpp

```cpp
#include <vector>
#include <iostream>
#include <algorithm> // For std::min
#include <limits>    // For std::numeric_limits

int coinChangeMinCoins(const std::vector<int>& coins, int amount) {
    // dp[i] will be storing the minimum number of coins
    // required for amount i.
    std::vector<int> dp(amount + 1, std::numeric_limits<int>::max());
    
    // Base case: 0 coins needed for amount 0
    dp[0] = 0;

    // Fill dp table for all amounts from 1 to amount
    for (int i = 1; i <= amount; i++) {
        // For each amount, iterate through all coins
        for (int coin : coins) {
            // If current coin can be used
            if (coin <= i) {
                // Ensure dp[i - coin] is not infinity before adding 1
                if (dp[i - coin] != std::numeric_limits<int>::max()) {
                    // Update dp[i] with the minimum of its current value
                    // and 1 (for the current coin) + dp[i - coin]
                    dp[i] = std::min(dp[i], 1 + dp[i - coin]);
                }
            }
        }
    }
    
    // If dp[amount] is still infinity, it means amount cannot be made
    return dp[amount] == std::numeric_limits<int>::max() ? -1 : dp[amount];
}

// int main() {
//     std::vector<int> coins = {1, 2, 5};
//     int amount = 11;
//     std::cout << "Min coins for 11: " << coinChangeMinCoins(coins, amount) << std::endl; // 3

//     std::vector<int> coins2 = {2};
//     int amount2 = 3;
//     std::cout << "Min coins for 3: " << coinChangeMinCoins(coins2, amount2) << std::endl; // -1
//     return 0;
// }
```

### Go

```go
package main

import (
    "fmt"
    "math"
)

func coinChangeMinCoins(coins []int, amount int) int {
    // dp[i] will be storing the minimum number of coins
    // required for amount i.
    dp := make([]int, amount+1)
    for i := range dp {
        dp[i] = math.MaxInt32 // Represents infinity
    }
    
    // Base case: 0 coins needed for amount 0
    dp[0] = 0

    // Fill dp table for all amounts from 1 to amount
    for i := 1; i <= amount; i++ {
        // For each amount, iterate through all coins
        for _, coin := range coins {
            // If current coin can be used
            if coin <= i {
                // Ensure dp[i - coin] is not MaxInt32 before adding 1
                if dp[i-coin] != math.MaxInt32 {
                    // Update dp[i] with the minimum of its current value
                    // and 1 (for the current coin) + dp[i - coin]
                    dp[i] = min(dp[i], 1 + dp[i-coin])
                }
            }
        }
    }
    
    // If dp[amount] is still MaxInt32, it means amount cannot be made
    if dp[amount] == math.MaxInt32 {
        return -1
    }
    return dp[amount]
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

// func main() {
//     coins := []int{1, 2, 5}
//     amount := 11
//     fmt.Println("Min coins for 11:", coinChangeMinCoins(coins, amount)) // 3

//     coins2 := []int{2}
//     amount2 := 3
//     fmt.Println("Min coins for 3:", coinChangeMinCoins(coins2, amount2)) // -1
// }
```

### D

```d
import std.stdio;
import std.array;
import std.algorithm; // For std.algorithm.min
import std.traits; // For isInfinity

int coinChangeMinCoins(int[] coins, int amount) {
    // dp[i] will be storing the minimum number of coins
    // required for amount i.
    auto dp = new int[amount + 1];
    dp[] = int.max; // Represents infinity
    
    // Base case: 0 coins needed for amount 0
    dp[0] = 0;

    // Fill dp table for all amounts from 1 to amount
    foreach (i; 1 .. amount + 1) {
        // For each amount, iterate through all coins
        foreach (coin; coins) {
            // If current coin can be used
            if (coin <= i) {
                // Ensure dp[i - coin] is not int.max before adding 1
                if (dp[i - coin] != int.max) {
                    // Update dp[i] with the minimum of its current value
                    // and 1 (for the current coin) + dp[i - coin]
                    dp[i] = min(dp[i], 1 + dp[i - coin]);
                }
            }
        }
    }
    
    // If dp[amount] is still int.max, it means amount cannot be made
    return dp[amount] == int.max ? -1 : dp[amount];
}

// void main() {
//     auto coins = [1, 2, 5];
//     int amount = 11;
//     writeln("Min coins for 11: ", coinChangeMinCoins(coins, amount)); // 3

//     auto coins2 = [2];
//     int amount2 = 3;
//     writeln("Min coins for 3: ", coinChangeMinCoins(coins2, amount2)); // -1
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

The `Coin Change Problem` (minimum coins variant) is solved using a 1D `dynamic programming` array, where each element represents the minimum coins needed for a specific amount.

---

**Initialization:**
- `amount`: The target amount for which to make change.
- `coins`: An array of available coin denominations.
- A 1D `dp` array of size `amount + 1` is created. `dp[i]` will store the minimum number of coins to make amount `i`.
- `dp[0]` is initialized to 0 (no coins needed for amount 0).
- All other `dp[i]` values are initialized to infinity (or a very large number) to signify that they are currently unreachable.

**Filling the DP Table:**
- The `dp` table is filled iteratively for `i` from 1 to `amount`. Each `i` represents a sub-amount for which we are trying to find the minimum coins.
- For each `amount i`, the algorithm iterates through all available `coin denominations`.
- **Condition:** If `coin <= i` (meaning the current `coin` can be used to make up `amount i`):
- We consider using the current `coin`. If we use this `coin`, the remaining amount is `i - coin`.
- The minimum coins needed for `amount i` would then be `1` (for the current `coin`) plus `dp[i - coin]` (the minimum coins needed for the remaining amount).
- We update `dp[i]` with the minimum of its current value and `(1 + dp[i - coin])`. This ensures `dp[i]` always holds the minimum.
- A check `if dp[i - coin] != infinity` is important to avoid `infinity + 1` issues, ensuring we only consider valid previous states.

    </li>

**Result:**
- After filling the entire `dp` table, `dp[amount]` will contain the minimum number of coins required to make the target `amount`.
- If `dp[amount]` is still `infinity`, it means the target `amount` cannot be made with the given `coin` denominations, and -1 is returned.

[Back to Implementation](#implementation)

## Applications

### Application

The `Coin Change Problem`, especially the minimum coins variant, has practical applications beyond just currency:
- **Financial Systems:** Optimizing change-making processes in vending machines, cash registers, or for currency exchange.
- **Resource Optimization:** In scenarios where you need to combine discrete units (like containers of different sizes, standard parts) to reach a target quantity while minimizing the number of units used.
- **Inventory Management:** Determining the minimum number of different product packages to fulfill an order of a specific quantity.
- **Network Packet Optimization:** In some networking contexts, assembling data packets of various fixed sizes to efficiently transmit a total amount of data.
- **Combinatorial Problems:** Serves as a fundamental building block or a subproblem in more complex combinatorial optimization challenges.

