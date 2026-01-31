---
title: "Fractional Knapsack Problem"
---

The `Fractional Knapsack Problem` is an optimization problem that can be solved using a `greedy approach`. Given a set of `items`, each with a specific `weight` and `value`, and a `knapsack` with a maximum `weight capacity`, the goal is to choose a subset of `items` (or fractions of `items`) to put into the `knapsack` such that the total `value` is maximized, and the total `weight` does not exceed the `capacity`.

Unlike the `0/1 Knapsack Problem` where items must be taken whole or not at all, the "`fractional`" aspect means we can take portions of items. This crucial difference allows for a simpler, greedy solution rather than a `dynamic programming` approach.

## How it Works

### How it Works (Expanded)

Because we can take fractions of items, the optimal strategy for the `Fractional Knapsack Problem` is to prioritize items that give the most `value per unit of weight` (i.e., the highest `value/weight ratio`). This greedy choice always leads to the optimal solution.

---

Example: Items = [(W=10, V=60), (W=20, V=100), (W=30, V=120)], Capacity = 50

1. Calculate Value/Weight Ratio:
- Item 1: 60/10 = 6
- Item 2: 100/20 = 5
- Item 3: 120/30 = 4

2. Sort items by Value/Weight Ratio (descending):
- [(W=10, V=60, Ratio=6), (W=20, V=100, Ratio=5), (W=30, V=120, Ratio=4)]

3. Fill knapsack greedily:
- Take Item 1 (10kg, 60 value). Remaining capacity = 50 - 10 = 40. Total value = 60.
- Take Item 2 (20kg, 100 value). Remaining capacity = 40 - 20 = 20. Total value = 60 + 100 = 160.
- For Item 3 (30kg, 120 value), only 20kg capacity left. Take (20/30) fraction.
- Value from fraction = (20/30) <em> 120 = 80.
- Remaining capacity = 20 - 20 = 0. Total value = 160 + 80 = 240.

Maximum value = 240.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
def fractional_knapsack(capacity, items):
    """
    Solves the Fractional Knapsack Problem.
    <code>capacity</code>: maximum weight capacity of the knapsack.
    <code>items</code>: a list of tuples, where each tuple is (weight, value).
    """
    if not items or capacity <= 0:
        return 0.0

    # 1. Calculate value/weight ratio for each item and sort in descending order
    # item_with_ratios = [(weight, value, value/weight)]
    items_with_ratios = []
    for w, v in items:
        items_with_ratios.append((w, v, v / w))
    
    # Sort by ratio in descending order
    items_with_ratios.sort(key=lambda x: x[2], reverse=True)

    total_value = 0.0
    current_weight = 0

    # 2. Iterate through sorted items and fill knapsack greedily
    for weight, value, ratio in items_with_ratios:
        if current_weight + weight <= capacity:
            # Take the whole item
            current_weight += weight
            total_value += value
        else:
            # Take a fraction of the item
            remaining_capacity = capacity - current_weight
            fraction = remaining_capacity / weight
            total_value += fraction </em> value
            current_weight += remaining_capacity # Knapsack is full
            break # Knapsack is full

    return total_value

# Example
# capacity = 50
# items = [(10, 60), (20, 100), (30, 120)] # (weight, value)
# print(fractional_knapsack(capacity, items)) # Expected: 240.0
# (Take 10kg of item1, 20kg of item2, and 20kg of item3 (2/3 of item3))
```

### Javascript

```javascript
function fractionalKnapsack(capacity, items) {
    /*<em>
     </em> Solves the Fractional Knapsack Problem.
     <em> <code>capacity</code>: maximum weight capacity of the knapsack.
     </em> <code>items</code>: an array of objects, where each object is { weight: number, value: number }.
     <em>/
    if (items.length === 0 || capacity <= 0) {
        return 0.0;
    }

    // 1. Calculate value/weight ratio for each item and sort in descending order
    // Add ratio to each item object
    const itemsWithRatios = items.map(item => ({
        ...item,
        ratio: item.value / item.weight
    }));
    
    // Sort by ratio in descending order
    itemsWithRatios.sort((a, b) => b.ratio - a.ratio);

    let totalValue = 0.0;
    let currentWeight = 0;

    // 2. Iterate through sorted items and fill knapsack greedily
    for (const item of itemsWithRatios) {
        if (currentWeight + item.weight <= capacity) {
            // Take the whole item
            currentWeight += item.weight;
            totalValue += item.value;
        } else {
            // Take a fraction of the item
            const remainingCapacity = capacity - currentWeight;
            const fraction = remainingCapacity / item.weight;
            totalValue += fraction </em> item.value;
            currentWeight += remainingCapacity; // Knapsack is full
            break; // Knapsack is full
        }
    }

    return totalValue;
}

// const capacity = 50;
// const items = [
//     { weight: 10, value: 60 },
//     { weight: 20, value: 100 },
//     { weight: 30, value: 120 }
// ];
// console.log(fractionalKnapsack(capacity, items)); // Expected: 240.0
```

### Typescript

```typescript
interface Item {
    weight: number;
    value: number;
}

interface ItemWithRatio extends Item {
    ratio: number;
}

function fractionalKnapsackTS(capacity: number, items: Item[]): number {
    if (items.length === 0 || capacity <= 0) {
        return 0.0;
    }

    // 1. Calculate value/weight ratio for each item and sort in descending order
    // Add ratio to each item object
    const itemsWithRatios: ItemWithRatio[] = items.map(item => ({
        ...item,
        ratio: item.value / item.weight
    }));
    
    // Sort by ratio in descending order
    itemsWithRatios.sort((a, b) => b.ratio - a.ratio);

    let totalValue = 0.0;
    let currentWeight = 0;

    // 2. Iterate through sorted items and fill knapsack greedily
    for (const item of itemsWithRatios) {
        if (currentWeight + item.weight <= capacity) {
            // Take the whole item
            currentWeight += item.weight;
            totalValue += item.value;
        } else {
            // Take a fraction of the item
            const remainingCapacity = capacity - currentWeight;
            const fraction = remainingCapacity / item.weight;
            totalValue += fraction <em> item.value;
            currentWeight += remainingCapacity; // Knapsack is full
            break; // Knapsack is full
        }
    }

    return totalValue;
}

// const capacityTS = 50;
// const itemsTS: Item[] = [
//     { weight: 10, value: 60 },
//     { weight: 20, value: 100 },
//     { weight: 30, value: 120 }
// ];
// console.log(fractionalKnapsackTS(capacityTS, itemsTS)); // Expected: 240.0
```

### Cpp

```cpp
#include <vector>
#include <iostream>
#include <algorithm> // For std::sort
#include <numeric>   // For std::iota

// Struct to represent an item with its weight, value, and ratio
struct Item {
    int weight;
    int value;
    double ratio;

    // Constructor to calculate ratio
    Item(int w, int v) : weight(w), value(v) {
        ratio = static_cast<double>(value) / weight;
    }

    // Custom comparator for sorting by ratio in descending order
    bool operator<(const Item& other) const {
        return ratio > other.ratio; // Sort in descending order of ratio
    }
};

double fractionalKnapsack(int capacity, std::vector<Item> items) {
    if (items.empty() || capacity <= 0) {
        return 0.0;
    }

    // 1. Sort items by value/weight ratio in descending order
    std::sort(items.begin(), items.end());

    double total_value = 0.0;
    int current_weight = 0;

    // 2. Iterate through sorted items and fill knapsack greedily
    for (const auto& item : items) {
        if (current_weight + item.weight <= capacity) {
            // Take the whole item
            current_weight += item.weight;
            total_value += item.value;
        } else {
            // Take a fraction of the item
            int remaining_capacity = capacity - current_weight;
            double fraction = static_cast<double>(remaining_capacity) / item.weight;
            total_value += fraction </em> item.value;
            current_weight += remaining_capacity; // Knapsack is full
            break; // Knapsack is full
        }
    }

    return total_value;
}

// int main() {
//     int capacity = 50;
//     std::vector<Item> items = {
//         Item(10, 60),
//         Item(20, 100),
//         Item(30, 120)
//     };
//     std::cout << "Max value: " << fractionalKnapsack(capacity, items) << std::endl; // 240.0
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

type FractionalKnapsackItem struct {
    Weight int
    Value  int
    Ratio  float64
}

// Implement sort.Interface for []FractionalKnapsackItem
type ByRatio []FractionalKnapsackItem

func (a ByRatio) Len() int           { return len(a) }
func (a ByRatio) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a ByRatio) Less(i, j int) bool { return a[i].Ratio > a[j].Ratio } // Descending order

func fractionalKnapsack(capacity int, items []FractionalKnapsackItem) float64 {
    if len(items) == 0 || capacity <= 0 {
        return 0.0
    }

    // 1. Calculate value/weight ratio for each item and sort in descending order
    // (Ratios are calculated and added to the struct in main for simplicity of passing)
    sort.Sort(ByRatio(items))

    totalValue := 0.0
    currentWeight := 0

    // 2. Iterate through sorted items and fill knapsack greedily
    for _, item := range items {
        if currentWeight+item.Weight <= capacity {
            // Take the whole item
            currentWeight += item.Weight
            totalValue += float64(item.Value)
        } else {
            // Take a fraction of the item
            remainingCapacity := capacity - currentWeight
            fraction := float64(remainingCapacity) / float64(item.Weight)
            totalValue += fraction <em> float64(item.Value)
            currentWeight += remainingCapacity // Knapsack is full
            break // Knapsack is full
        }
    }

    return totalValue
}

// func main() {
//     capacity := 50
//     items := []FractionalKnapsackItem{
//         {Weight: 10, Value: 60},
//         {Weight: 20, Value: 100},
//         {Weight: 30, Value: 120},
//     }

//     // Calculate ratios manually for demonstration, in a real scenario this would be done dynamically
//     for i := range items {
//         items[i].Ratio = float64(items[i].Value) / float64(items[i].Weight)
//     }

//     fmt.Println("Max value:", fractionalKnapsack(capacity, items)) // 240.0
// }
```

### D

```d
import std.stdio;
import std.array;
import std.algorithm; // For std.algorithm.sort

// Struct to represent an item with its weight, value, and ratio
struct Item {
    int weight;
    int value;
    double ratio;

    this(int w, int v) {
        weight = w;
        value = v;
        ratio = cast(double)value / weight;
    }

    // Custom comparator for sorting by ratio in descending order
    int opCmp(const Item other) const {
        if (this.ratio > other.ratio) return 1;
        if (this.ratio < other.ratio) return -1;
        return 0;
    }
}

double fractionalKnapsack(int capacity, Item[] items) {
    if (items.empty || capacity <= 0) {
        return 0.0;
    }

    // 1. Calculate value/weight ratio for each item and sort in descending order
    // (Ratios are calculated in constructor or can be done here)
    items.sort!((a, b) => a.ratio > b.ratio); // Sort in descending order of ratio

    double totalValue = 0.0;
    int currentWeight = 0;

    // 2. Iterate through sorted items and fill knapsack greedily
    foreach (item; items) {
        if (currentWeight + item.weight <= capacity) {
            // Take the whole item
            currentWeight += item.weight;
            totalValue += item.value;
        } else {
            // Take a fraction of the item
            int remainingCapacity = capacity - currentWeight;
            double fraction = cast(double)remainingCapacity / item.weight;
            totalValue += fraction </em> item.value;
            currentWeight += remainingCapacity; // Knapsack is full
            break; // Knapsack is full
        }
    }

    return totalValue;
}

// void main() {
//     int capacity = 50;
//     Item[] items = [
//         Item(10, 60),
//         Item(20, 100),
//         Item(30, 120)
//     ];

//     writeln("Max value: ", fractionalKnapsack(capacity, items)); // 240.0
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

The `Fractional Knapsack Problem` is solvable with a straightforward `greedy approach` because items can be broken into fractions.

---

**`Item` Structure:**
- Each `item` is typically represented by its `weight`, `value`, and a calculated `value/weight ratio`.

**`fractional_knapsack(capacity, items)` Function:**
- `capacity`: The maximum `weight` the `knapsack` can hold.
- `items`: A list of `item` objects/tuples.

**Algorithm Steps:**
- **Calculate Ratios:** For each `item`, its `value/weight ratio` is calculated. This ratio indicates how much `value` each unit of `weight` provides.
- **Sort Items:** The `items` are then sorted in descending order based on this `value/weight ratio`. This is the crucial greedy step.
- **Initialize:**
- `total_value`: Stores the maximum `value` accumulated so far, initialized to 0.0.
- `current_weight`: Stores the current `weight` in the `knapsack`, initialized to 0.

    </li>
- **Fill Knapsack Greedily:** The algorithm iterates through the `items` in their sorted order (highest `ratio` first).
- For each `item`:
- **If `current_weight + item.weight <= capacity`:** The entire `item` can be added without exceeding `capacity`. The `item`'s `weight` and `value` are added to `current_weight` and `total_value` respectively.
- **Else (the `item` cannot be taken whole):**
- The `knapsack` can only accommodate a `fraction` of the `item`.
- The `remaining_capacity` is calculated.
- The `fraction` of the `item` that can be taken is `remaining_capacity / item.weight`.
- This `fraction` of the `item`'s `value` is added to `total_value`.
- The `current_weight` is set to `capacity` (the `knapsack` is now full).
- The loop breaks because the `knapsack` is full.

                    </li>

            </li>

    </li>

**Result:**
- The `total_value` will be the maximum possible `value` that can be obtained.

[Back to Implementation](#implementation)

## Applications

### Application

The `Fractional Knapsack Problem` and its greedy solution have various practical applications in resource allocation and optimization scenarios:
- **Resource Allocation:** Deciding how to allocate a limited budget to different projects or investments, where each project has a cost and a potential return, and partial investment is possible.
- **Loading Cargo:** Optimizing the loading of a ship, truck, or airplane with various goods to maximize the total value, assuming goods can be split or poured.
- **Cutting Stock Problems:** Determining how to cut raw materials (e.g., fabric, metal sheets) into smaller pieces of different values to maximize profit from a limited supply.
- **Fluid/Gas Transport:** Optimizing the transport of different types of fluids or gases through a pipeline system with limited capacity, where each fluid has a value per unit volume.
- **Agricultural Planning:** Allocating land to different crops to maximize yield or profit, considering varying needs and returns per unit area.

