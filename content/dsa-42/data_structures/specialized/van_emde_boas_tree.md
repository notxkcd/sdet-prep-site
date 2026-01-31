---
title: "Van Emde Boas Tree"
---

A `Van Emde Boas Tree (vEB Tree)` is a specialized tree data structure that implements an associative array (or dictionary) with integer `keys`. It is particularly notable for achieving exceptionally fast worst-case time complexities for its operations: `O(log log U)`, where `U` is the maximum possible value of a `key` (the size of the universe of `keys`), rather than `N` (the number of `elements` actually stored).

This makes `vEB Trees` incredibly efficient for operations like finding the next or previous `element` in a large range of `keys`, especially when `U` is much larger than `N`. However, this comes at the cost of high space complexity and increased implementation complexity compared to more general-purpose data structures.

## How it Works

### How it Works (Expanded)

A `vEB Tree` for a universe of size `U` (where `U` is a power of 2, typically `2^k`) recursively divides the universe into `sqrt(U)` "`clusters`" and a "`summary`" `vEB Tree`.

---

Conceptual vEB Tree for Universe size U:

        vEB(U)
       /  |  \
      /   |   \
     /    |    \
   Summary  Clusters (sqrt(U) of them)
  (vEB(sqrt(U)))  (vEB(sqrt(U))) ...

Key Ideas:
- Store min/max of current set.
- Recursively manage 'clusters' and a 'summary' tree.
- The 'summary' tree stores which clusters are non-empty.

## Implementation {#implementation}

### Python

```python
# Conceptual Van Emde Boas Tree in Python (highly simplified)
# A full implementation is very complex, especially managing recursive structures and edge cases.
# This code aims to illustrate the class structure and basic recursive idea.

class VEBTree:
    def __init__(self, U):
        if U == 2: # Base case for universe size 2
            self.min = None
            self.max = None
            self.summary = None # Not needed for U=2
            self.clusters = [None, None] # Two clusters for values 0 and 1
            return
        
        self.U = U
        self.min = None
        self.max = None
        
        self.sqrt_U = int(U*<em>0.5)
        self.low_sqrt_U = self.sqrt_U # For ceiling in original paper

        self.summary = VEBTree(self.sqrt_U) # Summary VEB tree for clusters
        self.clusters = [None] </em> self.sqrt_U # Array of child VEB trees (clusters)
        for i in range(self.sqrt_U):
            self.clusters[i] = VEBTree(self.low_sqrt_U)

    def _high(self, x):
        return x // self.low_sqrt_U

    def _low(self, x):
        return x % self.low_sqrt_U

    def _index(self, high, low):
        return high <em> self.low_sqrt_U + low

    def is_empty(self):
        return self.min is None

    def insert(self, x):
        if self.is_empty():
            self.min = x
            self.max = x
            return

        if x < self.min:
            self.min, x = x, self.min # Swap min and x

        if self.U > 2: # Recursive step for U > 2
            # Insert x into its cluster
            cluster_idx = self._high(x)
            if self.clusters[cluster_idx].is_empty():
                self.summary.insert(cluster_idx) # Mark cluster as non-empty
                self.clusters[cluster_idx].min = self._low(x)
                self.clusters[cluster_idx].max = self._low(x)
            else:
                self.clusters[cluster_idx].insert(self._low(x))
        
        if x > self.max:
            self.max = x

    def find_next(self, x):
        if self.U == 2: # Base case
            if x == 0 and self.max == 1:
                return 1
            else:
                return None
        
        if x < self.min:
            return self.min
        
        # Find x's cluster
        cluster_idx = self._high(x)
        if self.clusters[cluster_idx].max is not None and self._low(x) < self.clusters[cluster_idx].max:
            # Next element is in the same cluster
            return self._index(cluster_idx, self.clusters[cluster_idx].find_next(self._low(x)))
        
        # Next element is in a subsequent cluster
        next_cluster_idx = self.summary.find_next(cluster_idx)
        if next_cluster_idx is None:
            return None # No subsequent non-empty clusters
        
        return self._index(next_cluster_idx, self.clusters[next_cluster_idx].min)

    # Delete is even more complex and omitted for conceptual simplicity.

# Example Usage (conceptual, as full delete is very complex)
# v = VEBTree(16) # Universe size 16 (0-15)
# v.insert(2)
# v.insert(3)
# v.insert(4)
# v.insert(14)
# v.insert(15)

# print("Min:", v.min) # 2
# print("Max:", v.max) # 15

# print("Find next for 3:", v.find_next(3)) # Expected: 4
# print("Find next for 10:", v.find_next(10)) # Expected: 14
# print("Find next for 15:", v.find_next(15)) # Expected: None
```

### Javascript

```javascript
class VEBTree {
    constructor(U) {
        if (U === 2) { // Base case for universe size 2
            this.min = null;
            this.max = null;
            this.summary = null; // Not needed for U=2
            this.clusters = [null, null]; // Two clusters for values 0 and 1
            return;
        }
        
        this.U = U;
        this.min = null;
        this.max = null;
        
        this.sqrtU = Math.floor(Math.sqrt(U));
        this.lowSqrtU = Math.floor(U / this.sqrtU); // Equivalent to ceil(U/sqrt(U)) in other contexts
        
        this.summary = new VEBTree(this.sqrtU); // Summary VEB tree for clusters
        this.clusters = new Array(this.sqrtU).fill(null); // Array of child VEB trees (clusters)
        for (let i = 0; i < this.sqrtU; i++) {
            this.clusters[i] = new VEBTree(this.lowSqrtU);
        }
    }

    _high(x) {
        return Math.floor(x / this.lowSqrtU);
    }

    _low(x) {
        return x % this.lowSqrtU;
    }

    _index(high, low) {
        return high </em> this.lowSqrtU + low;
    }

    isEmpty() {
        return this.min === null;
    }

    insert(x) {
        if (this.isEmpty()) {
            this.min = x;
            this.max = x;
            return;
        }

        if (x < this.min) {
            [this.min, x] = [x, this.min]; // Swap min and x
        }

        if (this.U > 2) { // Recursive step for U > 2
            // Insert x into its cluster
            const clusterIdx = this._high(x);
            if (this.clusters[clusterIdx].isEmpty()) {
                this.summary.insert(clusterIdx); // Mark cluster as non-empty
                this.clusters[clusterIdx].min = this._low(x);
                this.clusters[clusterIdx].max = this._low(x);
            } else {
                this.clusters[clusterIdx].insert(this._low(x));
            }
        }
        
        if (x > this.max) {
            this.max = x;
        }
    }

    findNext(x) {
        if (this.U === 2) { // Base case
            if (x === 0 && this.max === 1) {
                return 1;
            } else {
                return null;
            }
        }
        
        if (x < this.min) {
            return this.min;
        }
        
        // Find x's cluster
        const clusterIdx = this._high(x);
        if (this.clusters[clusterIdx].max !== null && this._low(x) < this.clusters[clusterIdx].max) {
            // Next element is in the same cluster
            return this._index(clusterIdx, this.clusters[clusterIdx].findNext(this._low(x)));
        }
        
        // Next element is in a subsequent cluster
        const nextClusterIdx = this.summary.findNext(clusterIdx);
        if (nextClusterIdx === null) {
            return null; // No subsequent non-empty clusters
        }
        
        return this._index(nextClusterIdx, this.clusters[nextClusterIdx].min);
    }

    // Delete is even more complex and omitted for conceptual simplicity.
}

// const v = new VEBTree(16); // Universe size 16 (0-15)
// v.insert(2);
// v.insert(3);
// v.insert(4);
// v.insert(14);
// v.insert(15);

// console.log("Min:", v.min); // 2
// console.log("Max:", v.max); // 15

// console.log("Find next for 3:", v.findNext(3)); // Expected: 4
// console.log("Find next for 10:", v.findNext(10)); // Expected: 14
// console.log("Find next for 15:", v.findNext(15)); // Expected: null
```

### Typescript

```typescript
class VEBTreeTS {
    public U: number;
    public min: number | null;
    public max: number | null;
    
    private sqrtU: number;
    private lowSqrtU: number;

    private summary: VEBTreeTS | null;
    private clusters: (VEBTreeTS | null)[];

    constructor(U: number) {
        if (U <= 1) { // Handle U=0 or U=1 (empty or single element universe)
             this.U = U;
             this.min = null;
             this.max = null;
             this.summary = null;
             this.clusters = [];
             return;
        }
        if (U === 2) { // Base case for universe size 2
            this.U = U;
            this.min = null;
            this.max = null;
            this.summary = null; // Not strictly needed for U=2, can be null
            this.clusters = [null, null]; // Two clusters for values 0 and 1
            return;
        }
        
        this.U = U;
        this.min = null;
        this.max = null;
        
        this.sqrtU = Math.floor(Math.sqrt(U));
        this.lowSqrtU = Math.floor(U / this.sqrtU);
        
        this.summary = new VEBTreeTS(this.sqrtU);
        this.clusters = new Array(this.sqrtU).fill(null);
        for (let i = 0; i < this.sqrtU; i++) {
            this.clusters[i] = new VEBTreeTS(this.lowSqrtU);
        }
    }

    private _high(x: number): number {
        return Math.floor(x / this.lowSqrtU);
    }

    private _low(x: number): number {
        return x % this.lowSqrtU;
    }

    private _index(high: number, low: number): number {
        return high <em> this.lowSqrtU + low;
    }

    public isEmpty(): boolean {
        return this.min === null;
    }

    public insert(x: number): void {
        if (this.isEmpty()) {
            this.min = x;
            this.max = x;
            return;
        }

        if (x < this.min!) {
            [this.min, x] = [x, this.min!]; // Swap min and x
        }

        if (this.U > 2) {
            const clusterIdx = this._high(x);
            const lowVal = this._low(x);
            
            if (this.clusters[clusterIdx]!.isEmpty()) {
                this.summary!.insert(clusterIdx);
                this.clusters[clusterIdx]!.min = lowVal;
                this.clusters[clusterIdx]!.max = lowVal;
            } else {
                this.clusters[clusterIdx]!.insert(lowVal);
            }
        }
        
        if (x > this.max!) {
            this.max = x;
        }
    }

    public findNext(x: number): number | null {
        if (this.U === 2) {
            if (x === 0 && this.max === 1) {
                return 1;
            } else {
                return null;
            }
        }
        
        if (x < this.min!) {
            return this.min;
        }
        
        const clusterIdx = this._high(x);
        const lowVal = this._low(x);

        if (this.clusters[clusterIdx]!.max !== null && lowVal < this.clusters[clusterIdx]!.max!) {
            return this._index(clusterIdx, this.clusters[clusterIdx]!.findNext(lowVal)!);
        }
        
        const nextClusterIdx = this.summary!.findNext(clusterIdx);
        if (nextClusterIdx === null) {
            return null;
        }
        
        return this._index(nextClusterIdx, this.clusters[nextClusterIdx]!.min!);
    }
}

// const vTS = new VEBTreeTS(16);
// vTS.insert(2);
// vTS.insert(3);
// vTS.insert(4);
// vTS.insert(14);
// vTS.insert(15);

// console.log("Min:", vTS.min); // 2
// console.log("Max:", vTS.max); // 15

// console.log("Find next for 3:", vTS.findNext(3)); // Expected: 4
// console.log("Find next for 10:", vTS.findNext(10)); // Expected: 14
// console.log("Find next for 15:", vTS.findNext(15)); // Expected: null
```

### Cpp

```cpp
#include <iostream>
#include <vector>
#include <cmath>    // For sqrt, floor
#include <algorithm> // For std::swap
#include <stdexcept> // For std::invalid_argument

// Forward declaration
class VEBTree;

class VEBTree {
public:
    int U; // Size of the universe
    int min_val;
    int max_val;

    // For U > 2
    int sqrt_U;
    int low_sqrt_U;
    VEBTree</em> summary;
    std::vector<VEBTree<em>> clusters;

    VEBTree(int universe_size) : U(universe_size), min_val(-1), max_val(-1), summary(nullptr) {
        if (U < 0) {
            throw std::invalid_argument("Universe size U must be non-negative.");
        }
        if (U == 0 || U == 1) { // Empty or single element universe
            // min_val and max_val remain -1 (or some indicator of empty)
            // No summary or clusters needed
            return;
        }
        if (U == 2) { // Base case for U=2 (universe {0, 1})
            // min_val and max_val remain -1
            clusters.resize(2, nullptr); // Two conceptual clusters for 0 and 1
            return;
        }

        sqrt_U = static_cast<int>(std::floor(std::sqrt(U)));
        low_sqrt_U = static_cast<int>(std::ceil(static_cast<double>U / sqrt_U));

        summary = new VEBTree(sqrt_U);
        clusters.resize(sqrt_U, nullptr);
        for (int i = 0; i < sqrt_U; ++i) {
            clusters[i] = new VEBTree(low_sqrt_U);
        }
    }

    ~VEBTree() {
        if (summary) delete summary;
        for (VEBTree</em> cluster : clusters) {
            if (cluster) delete cluster;
        }
    }

    bool isEmpty() const {
        return min_val == -1; // -1 indicates empty for integer keys
    }

    int high(int x) const {
        return x / low_sqrt_U;
    }

    int low(int x) const {
        return x % low_sqrt_U;
    }

    int index(int high_val, int low_val) const {
        return high_val <em> low_sqrt_U + low_val;
    }

    void insert(int x) {
        if (isEmpty()) {
            min_val = x;
            max_val = x;
            return;
        }

        if (x < min_val) {
            std::swap(min_val, x);
        }

        if (U > 2) {
            int cluster_idx = high(x);
            int low_val = low(x);

            if (clusters[cluster_idx]->isEmpty()) {
                summary->insert(cluster_idx);
                clusters[cluster_idx]->min_val = low_val;
                clusters[cluster_idx]->max_val = low_val;
            } else {
                clusters[cluster_idx]->insert(low_val);
            }
        }
        
        if (x > max_val) {
            max_val = x;
        }
    }

    int findNext(int x) const {
        if (U == 0 || x >= max_val) {
            return -1; // -1 indicates no next element
        }
        if (U == 1) { // For universe size 1, if 0 is stored, then no next
            return -1;
        }
        if (x < min_val) {
            return min_val;
        }
        
        int cluster_idx = high(x);
        int low_val = low(x);

        if (clusters[cluster_idx] != nullptr && !clusters[cluster_idx]->isEmpty() && low_val < clusters[cluster_idx]->max_val) {
            // Next element is in the same cluster
            int next_low = clusters[cluster_idx]->findNext(low_val);
            if (next_low != -1) {
                return index(cluster_idx, next_low);
            }
        }
        
        // Next element is in a subsequent cluster
        int next_cluster_idx = summary->findNext(cluster_idx);
        if (next_cluster_idx == -1) {
            return -1; // No subsequent non-empty clusters
        }
        
        return index(next_cluster_idx, clusters[next_cluster_idx]->min_val);
    }
    
    // Delete is even more complex and omitted for conceptual simplicity.
};

// int main() {
//     VEBTree v(16); // Universe size 16 (0-15)
//     v.insert(2);
//     v.insert(3);
//     v.insert(4);
//     v.insert(14);
//     v.insert(15);

//     std::cout << "Min: " << v.min_val << std::endl; // 2
//     std::cout << "Max: " << v.max_val << std::endl; // 15

//     std::cout << "Find next for 3: " << v.findNext(3) << std::endl; // Expected: 4
//     std::cout << "Find next for 10: " << v.findNext(10) << std::endl; // Expected: 14
//     std::cout << "Find next for 15: " << v.findNext(15) << std::endl; // Expected: -1
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

type VEBTree struct {
    U       int
    MinVal  int
    MaxVal  int
    
    SqrtU     int
    LowSqrtU int

    Summary  </em>VEBTree
    Clusters []<em>VEBTree
}

func NewVEBTree(universeSize int) </em>VEBTree {
    if universeSize < 0 {
        panic("Universe size U must be non-negative.")
    }
    if universeSize == 0 || universeSize == 1 {
        return &VEBTree{U: universeSize, MinVal: -1, MaxVal: -1} // -1 indicates empty
    }
    if universeSize == 2 {
        return &VEBTree{U: universeSize, MinVal: -1, MaxVal: -1, Clusters: make([]<em>VEBTree, 2)}
    }

    sqrtU := int(math.Floor(math.Sqrt(float64(universeSize))))
    lowSqrtU := int(math.Ceil(float64(universeSize) / float64(sqrtU)))

    v := &VEBTree{
        U:        universeSize,
        MinVal:   -1, // -1 indicates empty
        MaxVal:   -1, // -1 indicates empty
        SqrtU:    sqrtU,
        LowSqrtU: lowSqrtU,
        Summary:  NewVEBTree(sqrtU),
        Clusters: make([]</em>VEBTree, sqrtU),
    }
    for i := 0; i < sqrtU; i++ {
        v.Clusters[i] = NewVEBTree(lowSqrtU)
    }
    return v
}

func (v <em>VEBTree) high(x int) int {
    return x / v.LowSqrtU
}

func (v </em>VEBTree) low(x int) int {
    return x % v.LowSqrtU
}

func (v <em>VEBTree) index(highVal, lowVal int) int {
    return highVal</em>v.LowSqrtU + lowVal
}

func (v <em>VEBTree) IsEmpty() bool {
    return v.MinVal == -1
}

func (v </em>VEBTree) Insert(x int) {
    if v.IsEmpty() {
        v.MinVal = x
        v.MaxVal = x
        return
    }

    if x < v.MinVal {
        v.MinVal, x = x, v.MinVal // Swap min_val and x
    }

    if v.U > 2 {
        clusterIdx := v.high(x)
        lowVal := v.low(x)

        if v.Clusters[clusterIdx].IsEmpty() {
            v.Summary.Insert(clusterIdx)
            v.Clusters[clusterIdx].MinVal = lowVal
            v.Clusters[clusterIdx].MaxVal = lowVal
        } else {
            v.Clusters[clusterIdx].Insert(lowVal)
        }
    }

    if x > v.MaxVal {
        v.MaxVal = x
    }
}

func (v <em>VEBTree) FindNext(x int) int {
    if v.U == 0 || x >= v.MaxVal {
        return -1
    }
    if v.U == 1 {
        return -1
    }
    if x < v.MinVal {
        return v.MinVal
    }

    clusterIdx := v.high(x)
    lowVal := v.low(x)

    if v.Clusters[clusterIdx].MaxVal != -1 && lowVal < v.Clusters[clusterIdx].MaxVal {
        // Next element is in the same cluster
        nextLow := v.Clusters[clusterIdx].FindNext(lowVal)
        if nextLow != -1 {
            return v.index(clusterIdx, nextLow)
        }
    }

    // Next element is in a subsequent cluster
    nextClusterIdx := v.Summary.FindNext(clusterIdx)
    if nextClusterIdx == -1 {
        return -1
    }

    return v.index(nextClusterIdx, v.Clusters[nextClusterIdx].MinVal)
}

// Delete is even more complex and omitted for conceptual simplicity.

// func main() {
//     v := NewVEBTree(16) // Universe size 16 (0-15)
//     v.Insert(2)
//     v.Insert(3)
//     v.Insert(4)
//     v.Insert(14)
//     v.Insert(15)

//     fmt.Println("Min:", v.MinVal) // 2
//     fmt.Println("Max:", v.MaxVal) // 15

//     fmt.Println("Find next for 3:", v.FindNext(3))   // Expected: 4
//     fmt.Println("Find next for 10:", v.FindNext(10)) // Expected: 14
//     fmt.Println("Find next for 15:", v.FindNext(15)) // Expected: -1
// }
```

### D

```d
import std.stdio;
import std.array;
import std.algorithm; // For std.algorithm.swap
import std.conv; // For to!string
import std.math; // For floor, sqrt, ceil

class VEBTree {
    int U; // Size of the universe
    int min_val;
    int max_val;

    // For U > 2
    int sqrt_U;
    int low_sqrt_U;
    VEBTree summary;
    VEBTree[] clusters;

    this(int universe_size) {
        if (universe_size < 0) {
            throw new Exception("Universe size U must be non-negative.");
        }
        if (universe_size == 0 || universe_size == 1) {
            this.U = universe_size;
            min_val = -1; // -1 indicates empty for integer keys
            max_val = -1;
            summary = null;
            clusters = [];
            return;
        }
        if (universe_size == 2) { // Base case for U=2 (universe {0, 1})
            this.U = universe_size;
            min_val = -1;
            max_val = -1;
            summary = null;
            clusters = new VEBTree[2]; // Two conceptual clusters for 0 and 1
            return;
        }

        this.U = universe_size;
        min_val = -1;
        max_val = -1;

        sqrt_U = cast(int)(floor(sqrt(cast(double)U)));
        low_sqrt_U = cast(int)(ceil(cast(double)U / sqrt_U));

        summary = new VEBTree(sqrt_U);
        clusters = new VEBTree[sqrt_U];
        foreach (i; 0..sqrt_U) {
            clusters[i] = new VEBTree(low_sqrt_U);
        }
    }

    // No explicit destructor needed for D due to GC.

    bool isEmpty() {
        return min_val == -1; // -1 indicates empty for integer keys
    }

    int high(int x) {
        return x / low_sqrt_U;
    }

    int low(int x) {
        return x % low_sqrt_U;
    }

    int index(int high_val, int low_val) {
        return high_val </em> low_sqrt_U + low_val;
    }

    void insert(int x) {
        if (isEmpty()) {
            min_val = x;
            max_val = x;
            return;
        }

        if (x < min_val) {
            swap(min_val, x);
        }

        if (U > 2) {
            int cluster_idx = high(x);
            int low_val = low(x);

            if (clusters[cluster_idx].isEmpty()) {
                summary.insert(cluster_idx);
                clusters[cluster_idx].min_val = low_val;
                clusters[cluster_idx].max_val = low_val;
            } else {
                clusters[cluster_idx].insert(low_val);
            }
        }
        
        if (x > max_val) {
            max_val = x;
        }
    }

    int findNext(int x) {
        if (U == 0 || x >= max_val) {
            return -1; // -1 indicates no next element
        }
        if (U == 1) {
            return -1;
        }
        if (x < min_val) {
            return min_val;
        }
        
        int cluster_idx = high(x);
        int low_val = low(x);

        if (clusters[cluster_idx] !is null && !clusters[cluster_idx].isEmpty() && low_val < clusters[cluster_idx].max_val) {
            // Next element is in the same cluster
            int next_low = clusters[cluster_idx].findNext(low_val);
            if (next_low != -1) {
                return index(cluster_idx, next_low);
            }
        }
        
        // Next element is in a subsequent cluster
        int next_cluster_idx = summary.findNext(cluster_idx);
        if (next_cluster_idx == -1) {
            return -1; // No subsequent non-empty clusters
        }
        
        return index(next_cluster_idx, clusters[next_cluster_idx].min_val);
    }
    
    // Delete is even more complex and omitted for conceptual simplicity.
}

// void main() {
//     auto v = new VEBTree(16); // Universe size 16 (0-15)
//     v.insert(2);
//     v.insert(3);
//     v.insert(4);
//     v.insert(14);
//     v.insert(15);

//     writeln("Min: ", v.min_val); // 2
//     writeln("Max: ", v.max_val); // 15

//     writeln("Find next for 3: ", v.findNext(3)); // Expected: 4
//     writeln("Find next for 10: ", v.findNext(10)); // Expected: 14
//     writeln("Find next for 15: ", v.findNext(15)); // Expected: -1
// }
```

## Applications

### Application

Van Emde Boas Trees are a theoretical marvel known for their extremely fast worst-case time complexities for successor, predecessor, insert, and delete operations on integer keys. While their complexity and space overhead limit their direct practical use compared to hash tables or balanced BSTs for general-purpose tasks, they are significant in:
- **Theoretical Computer Science:** Used as a building block for other advanced data structures and algorithms, especially in proofs of lower bounds for certain problems.
- **Large Integer Universes:** When dealing with very large integer keys (e.g., 64-bit integers) where the universe size U is huge, and N (number of elements stored) is much smaller than U.
- **Specialized Database Systems:** Some highly optimized in-memory database or indexing systems might use vEB trees for specific integer key lookups or range queries.
- **Router Tables:** Potentially in high-performance network routers where integer IP addresses need extremely fast lookups and range queries.

