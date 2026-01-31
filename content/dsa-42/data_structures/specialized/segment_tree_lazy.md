---
title: "Segment Tree with Lazy Propagation"
---

A `Segment Tree with Lazy Propagation` is an advanced variation of the `Segment Tree` data structure designed to efficiently handle `range updates` (applying an update to an entire segment of the `array`) in addition to `range queries` and `point updates`. Without lazy propagation, a `range update` could take `O(N)` time in the worst case, as every affected `leaf node` would need to be updated.

`Lazy propagation` optimizes `range updates` by deferring the updates to child `nodes` until they are actually needed for a `query` or another `update`. This allows both `range updates` and `range queries` to maintain an `O(log N)` time complexity.

## How it Works

### How it Works (Expanded)

The core idea of `lazy propagation` is to not immediately update all the `leaf nodes` covered by a `range update`. Instead, when a `node`'s segment is completely contained within the `update range`, we apply the update to that `node` and mark it as "`lazy`". This `lazy mark` signifies that its children's information is outdated and needs to be propagated downwards before being used.

---

Conceptual Segment Tree Node with Lazy Tag:

        [Node: Value=X, Range=[L,R], LazyTag=Y]
       /                        \
      /                          \
LeftChild (if not lazy)   RightChild (if not lazy)
- When an update covers a node completely, update Node's value, apply LazyTag.
- When traversing a node for query/update:
- If Node has LazyTag, push it down to children.
- Clear LazyTag from Node.

## Implementation {#implementation}

### Python

```python
class SegmentTreeLazy:
    def __init__(self, arr, op=lambda x, y: x + y, identity_element=0):
        self.n = len(arr)
        self.tree = [identity_element] <em> (4 </em> self.n)
        self.lazy = [0] <em> (4 </em> self.n) # Lazy tag array
        self.arr = arr # Original array (for initial build)
        self.op = op # Operation (e.g., sum, min, max)
        self.identity_element = identity_element # Identity for op

        self._build(0, 0, self.n - 1)

    def _build(self, node_idx, low, high):
        if low == high:
            self.tree[node_idx] = self.arr[low]
            return
        
        mid = (low + high) // 2
        self._build(2 <em> node_idx + 1, low, mid)
        self._build(2 </em> node_idx + 2, mid + 1, high)
        self.tree[node_idx] = self.op(self.tree[2 <em> node_idx + 1], self.tree[2 </em> node_idx + 2])

    def _push_down_lazy(self, node_idx, low, high):
        if self.lazy[node_idx] != 0: # If there's a pending update
            # Apply lazy tag to current node's value (adjust for range size if sum)
            self.tree[node_idx] += self.lazy[node_idx] <em> (high - low + 1) # Example: range sum update
            
            if low != high: # Not a leaf node
                # Propagate lazy tag to children
                self.lazy[2 </em> node_idx + 1] += self.lazy[node_idx]
                self.lazy[2 <em> node_idx + 2] += self.lazy[node_idx]
            
            self.lazy[node_idx] = 0 # Clear lazy tag

    def update_range(self, q_low, q_high, val):
        self._update_range_recursive(0, 0, self.n - 1, q_low, q_high, val)

    def _update_range_recursive(self, node_idx, low, high, q_low, q_high, val):
        self._push_down_lazy(node_idx, low, high) # Push down any pending lazy updates first

        # No overlap
        if q_low > high or q_high < low:
            return
        
        # Complete overlap
        if q_low <= low and high <= q_high:
            self.lazy[node_idx] += val # Apply lazy tag
            self._push_down_lazy(node_idx, low, high) # Apply and push down immediately
            return

        # Partial overlap
        mid = (low + high) // 2
        self._update_range_recursive(2 </em> node_idx + 1, low, mid, q_low, q_high, val)
        self._update_range_recursive(2 <em> node_idx + 2, mid + 1, high, q_low, q_high, val)
        self.tree[node_idx] = self.op(self.tree[2 </em> node_idx + 1], self.tree[2 <em> node_idx + 2])

    def query_range(self, q_low, q_high):
        return self._query_range_recursive(0, 0, self.n - 1, q_low, q_high)

    def _query_range_recursive(self, node_idx, low, high, q_low, q_high):
        self._push_down_lazy(node_idx, low, high) # Push down any pending lazy updates first

        # No overlap
        if q_low > high or q_high < low:
            return self.identity_element
        
        # Complete overlap
        if q_low <= low and high <= q_high:
            return self.tree[node_idx]
        
        # Partial overlap
        mid = (low + high) // 2
        left_val = self._query_range_recursive(2 </em> node_idx + 1, low, mid, q_low, q_high)
        right_val = self._query_range_recursive(2 <em> node_idx + 2, mid + 1, high, q_low, q_high)
        
        return self.op(left_val, right_val)

# Example Usage (Range Sum Query with Lazy Propagation)
# arr = [1, 2, 3, 4, 5] # Sums
# stl = SegmentTreeLazy(arr)
# print("Initial sum of [0, 4]:", stl.query_range(0, 4)) # Expected: 15
# print("Initial sum of [1, 3]:", stl.query_range(1, 3)) # Expected: 9 (2+3+4)

# stl.update_range(1, 3, 10) # Add 10 to elements at indices 1, 2, 3
# # Conceptual array: [1, 12, 13, 14, 5]
# print("Sum of [0, 4] after update:", stl.query_range(0, 4)) # Expected: 1+12+13+14+5 = 45
# print("Sum of [1, 3] after update:", stl.query_range(1, 3)) # Expected: 12+13+14 = 39
# print("Sum of [0, 1] after update:", stl.query_range(0, 1)) # Expected: 1+12 = 13
```

### Javascript

```javascript
class SegmentTreeLazy {
    constructor(arr, op = (x, y) => x + y, identityElement = 0) {
        this.n = arr.length;
        this.tree = new Array(4 </em> this.n).fill(identityElement);
        this.lazy = new Array(4 <em> this.n).fill(0); // Lazy tag array (e.g., for sum, value to add)
        this.arr = arr; // Original array (for initial build)
        this.op = op;
        this.identityElement = identityElement;

        this._build(0, 0, this.n - 1);
    }

    _build(nodeIdx, low, high) {
        if (low === high) {
            this.tree[nodeIdx] = this.arr[low];
            return;
        }
        
        const mid = Math.floor((low + high) / 2);
        this._build(2 </em> nodeIdx + 1, low, mid);
        this._build(2 <em> nodeIdx + 2, mid + 1, high);
        this.tree[nodeIdx] = this.op(this.tree[2 </em> nodeIdx + 1], this.tree[2 <em> nodeIdx + 2]);
    }

    _pushDownLazy(nodeIdx, low, high) {
        if (this.lazy[nodeIdx] !== 0) { // If there's a pending update
            // Apply lazy tag to current node's value (adjust for range size if sum)
            this.tree[nodeIdx] += this.lazy[nodeIdx] </em> (high - low + 1); // Example: range sum update
            
            if (low !== high) { // Not a leaf node
                // Propagate lazy tag to children
                this.lazy[2 <em> nodeIdx + 1] += this.lazy[nodeIdx];
                this.lazy[2 </em> nodeIdx + 2] += this.lazy[nodeIdx];
            }
            
            this.lazy[nodeIdx] = 0; // Clear lazy tag
        }
    }

    updateRange(qLow, qHigh, val) {
        this._updateRangeRecursive(0, 0, this.n - 1, qLow, qHigh, val);
    }

    _updateRangeRecursive(nodeIdx, low, high, qLow, qHigh, val) {
        this._pushDownLazy(nodeIdx, low, high); // Push down any pending lazy updates first

        // No overlap
        if (qLow > high || qHigh < low) {
            return;
        }
        
        // Complete overlap
        if (qLow <= low && high <= qHigh) {
            this.lazy[nodeIdx] += val; // Apply lazy tag
            this._pushDownLazy(nodeIdx, low, high); // Apply and push down immediately
            return;
        }

        // Partial overlap
        const mid = Math.floor((low + high) / 2);
        this._updateRangeRecursive(2 <em> nodeIdx + 1, low, mid, qLow, qHigh, val);
        this._updateRangeRecursive(2 </em> nodeIdx + 2, mid + 1, high, qLow, qHigh, val);
        this.tree[nodeIdx] = this.op(this.tree[2 <em> nodeIdx + 1], this.tree[2 </em> nodeIdx + 2]);
    }

    queryRange(qLow, qHigh) {
        return this._queryRangeRecursive(0, 0, this.n - 1, qLow, qHigh);
    }

    _queryRangeRecursive(nodeIdx, low, high, qLow, qHigh) {
        this._pushDownLazy(nodeIdx, low, high); // Push down any pending lazy updates first

        // No overlap
        if (qLow > high || qHigh < low) {
            return this.identityElement;
        }
        
        // Complete overlap
        if (qLow <= low && high <= qHigh) {
            return this.tree[nodeIdx];
        }
        
        // Partial overlap
        const mid = Math.floor((low + high) / 2);
        const leftVal = this._queryRangeRecursive(2 <em> nodeIdx + 1, low, mid, qLow, qHigh);
        const rightVal = this._queryRangeRecursive(2 </em> nodeIdx + 2, mid + 1, high, qLow, qHigh);
        
        return this.op(leftVal, rightVal);
    }
}

// const arr = [1, 2, 3, 4, 5]; // Sums
// const stl = new SegmentTreeLazy(arr);
// console.log("Initial sum of [0, 4]:", stl.queryRange(0, 4)); // Expected: 15
// console.log("Initial sum of [1, 3]:", stl.queryRange(1, 3)); // Expected: 9 (2+3+4)

// stl.updateRange(1, 3, 10); // Add 10 to elements at indices 1, 2, 3
// console.log("Sum of [0, 4] after update:", stl.queryRange(0, 4)); // Expected: 1+12+13+14+5 = 45
// console.log("Sum of [1, 3] after update:", stl.queryRange(1, 3)); // Expected: 12+13+14 = 39
// console.log("Sum of [0, 1] after update:", stl.queryRange(0, 1)); // Expected: 1+12 = 13
```

### Cpp

```cpp
#include <vector>
#include <functional> // For std::function
#include <limits>     // For std::numeric_limits
#include <iostream>   // For example usage

// Identity element for sum operation
const int SUM_IDENTITY_LAZY = 0;

class SegmentTreeLazy {
private:
    std::vector<int> tree;
    std::vector<int> lazy; // Lazy tag array
    int n;
    std::function<int(int, int)> op; // Operation (e.g., sum)
    int identity_element;

    void _build(int node_idx, int low, int high, const std::vector<int>& arr) {
        if (low == high) {
            tree[node_idx] = arr[low];
            return;
        }
        
        int mid = low + (high - low) / 2;
        _build(2 <em> node_idx + 1, low, mid, arr);
        _build(2 </em> node_idx + 2, mid + 1, high, arr);
        tree[node_idx] = op(tree[2 <em> node_idx + 1], tree[2 </em> node_idx + 2]);
    }

    void _push_down_lazy(int node_idx, int low, int high) {
        if (lazy[node_idx] != 0) { // If there's a pending update
            // Apply lazy tag to current node's value (adjust for range size if sum)
            tree[node_idx] += lazy[node_idx] <em> (high - low + 1); // Example: range sum update
            
            if (low != high) { // Not a leaf node
                // Propagate lazy tag to children
                lazy[2 </em> node_idx + 1] += lazy[node_idx];
                lazy[2 <em> node_idx + 2] += lazy[node_idx];
            }
            
            lazy[node_idx] = 0; // Clear lazy tag
        }
    }

    void _update_range_recursive(int node_idx, int low, int high, int q_low, int q_high, int val) {
        _push_down_lazy(node_idx, low, high); // Push down any pending lazy updates first

        // No overlap
        if (q_low > high || q_high < low) {
            return;
        }
        
        // Complete overlap
        if (q_low <= low && high <= q_high) {
            lazy[node_idx] += val; // Apply lazy tag
            _push_down_lazy(node_idx, low, high); // Apply and push down immediately
            return;
        }

        // Partial overlap
        int mid = low + (high - low) / 2;
        _update_range_recursive(2 </em> node_idx + 1, low, mid, q_low, q_high, val);
        _update_range_recursive(2 <em> node_idx + 2, mid + 1, high, q_low, q_high, val);
        tree[node_idx] = op(tree[2 </em> node_idx + 1], tree[2 <em> node_idx + 2]);
    }

    int _query_range_recursive(int node_idx, int low, int high, int q_low, int q_high) {
        _push_down_lazy(node_idx, low, high); // Push down any pending lazy updates first

        // No overlap
        if (q_low > high || q_high < low) {
            return identity_element;
        }
        
        // Complete overlap
        if (q_low <= low && high <= q_high) {
            return tree[node_idx];
        }
        
        // Partial overlap
        int mid = low + (high - low) / 2;
        int left_val = _query_range_recursive(2 </em> node_idx + 1, low, mid, q_low, q_high);
        int right_val = _query_range_recursive(2 <em> node_idx + 2, mid + 1, high, q_low, q_high);
        
        return op(left_val, right_val);
    }

public:
    SegmentTreeLazy(const std::vector<int>& arr, std::function<int(int, int)> operation = [](int a, int b){ return a + b; }, int id_elem = SUM_IDENTITY_LAZY)
        : n(arr.size()), op(operation), identity_element(id_elem) {
        tree.resize(4 </em> n);
        lazy.resize(4 <em> n, 0);
        _build(0, 0, n - 1, arr);
    }

    void updateRange(int q_low, int q_high, int val) {
        _update_range_recursive(0, 0, n - 1, q_low, q_high, val);
    }

    int queryRange(int q_low, int q_high) {
        return _query_range_recursive(0, 0, n - 1, q_low, q_high);
    }
};

// int main() {
//     std::vector<int> arr = {1, 2, 3, 4, 5}; // Sums
//     SegmentTreeLazy stl(arr);
//     std::cout << "Initial sum of [0, 4]: " << stl.queryRange(0, 4) << std::endl; // Expected: 15
//     std::cout << "Initial sum of [1, 3]: " << stl.queryRange(1, 3) << std::endl; // Expected: 9 (2+3+4)

//     stl.updateRange(1, 3, 10); // Add 10 to elements at indices 1, 2, 3
//     // Conceptual array: [1, 12, 13, 14, 5]
//     std::cout << "Sum of [0, 4] after update: " << stl.queryRange(0, 4) << std::endl; // Expected: 1+12+13+14+5 = 45
//     std::cout << "Sum of [1, 3] after update: " << stl.queryRange(1, 3) << std::endl; // Expected: 12+13+14 = 39
//     std::cout << "Sum of [0, 1] after update: " << stl.queryRange(0, 1) << std::endl; // Expected: 1+12 = 13
//     return 0;
// }
```

### Go

```go
package main

import (
    "fmt"
)

type SegmentLazyOp func(x, y int) int

const (
    SumIdentityLazy = 0
    // For min/max, identity would be math.MaxInt32 / math.MinInt32
)

type SegmentTreeLazy struct {
    tree           []int
    lazy           []int // Lazy tag array
    n              int
    op             SegmentLazyOp
    identityElement int
}

func NewSegmentTreeLazy(arr []int, operation SegmentLazyOp, identityElement int) </em>SegmentTreeLazy {
    stl := &SegmentTreeLazy{
        n:              len(arr),
        op:             operation,
        identityElement: identityElement,
    }
    stl.tree = make([]int, 4<em>stl.n)
    stl.lazy = make([]int, 4</em>stl.n)
    stl.build(0, 0, stl.n-1, arr)
    return stl
}

func (stl <em>SegmentTreeLazy) build(nodeIdx, low, high int, arr []int) {
    if low == high {
        stl.tree[nodeIdx] = arr[low]
        return
    }

    mid := low + (high-low)/2
    stl.build(2</em>nodeIdx+1, low, mid, arr)
    stl.build(2<em>nodeIdx+2, mid+1, high, arr)
    stl.tree[nodeIdx] = stl.op(stl.tree[2</em>nodeIdx+1], stl.tree[2<em>nodeIdx+2])
}

func (stl </em>SegmentTreeLazy) pushDownLazy(nodeIdx, low, high int) {
    if stl.lazy[nodeIdx] != 0 { // If there's a pending update
        // Apply lazy tag to current node's value (adjust for range size if sum)
        stl.tree[nodeIdx] += stl.lazy[nodeIdx] <em> (high - low + 1) // Example: range sum update

        if low != high { // Not a leaf node
            // Propagate lazy tag to children
            stl.lazy[2</em>nodeIdx+1] += stl.lazy[nodeIdx]
            stl.lazy[2<em>nodeIdx+2] += stl.lazy[nodeIdx]
        }

        stl.lazy[nodeIdx] = 0 // Clear lazy tag
    }
}

func (stl </em>SegmentTreeLazy) updateRangeRecursive(nodeIdx, low, high, qLow, qHigh, val int) {
    stl.pushDownLazy(nodeIdx, low, high) // Push down any pending lazy updates first

    // No overlap
    if qLow > high || qHigh < low {
        return
    }

    // Complete overlap
    if qLow <= low && high <= qHigh {
        stl.lazy[nodeIdx] += val // Apply lazy tag
        stl.pushDownLazy(nodeIdx, low, high) // Apply and push down immediately
        return
    }

    // Partial overlap
    mid := low + (high-low)/2
    stl.updateRangeRecursive(2<em>nodeIdx+1, low, mid, qLow, qHigh, val)
    stl.updateRangeRecursive(2</em>nodeIdx+2, mid+1, high, qLow, qHigh, val)
    stl.tree[nodeIdx] = stl.op(stl.tree[2<em>nodeIdx+1], stl.tree[2</em>nodeIdx+2])
}

func (stl <em>SegmentTreeLazy) queryRangeRecursive(nodeIdx, low, high, qLow, qHigh int) int {
    stl.pushDownLazy(nodeIdx, low, high) // Push down any pending lazy updates first

    // No overlap
    if qLow > high || qHigh < low {
        return stl.identityElement
    }

    // Complete overlap
    if qLow <= low && high <= qHigh {
        return stl.tree[nodeIdx]
    }

    // Partial overlap
    mid := low + (high-low)/2
    leftVal := stl.queryRangeRecursive(2</em>nodeIdx+1, low, mid, qLow, qHigh)
    rightVal := stl.queryRangeRecursive(2<em>nodeIdx+2, mid+1, high, qLow, qHigh)

    return stl.op(leftVal, rightVal)
}

func (stl </em>SegmentTreeLazy) UpdateRange(qLow, qHigh, val int) {
    stl.updateRangeRecursive(0, 0, stl.n-1, qLow, qHigh, val)
}

func (stl <em>SegmentTreeLazy) QueryRange(qLow, qHigh int) int {
    return stl.queryRangeRecursive(0, 0, stl.n-1, qLow, qHigh)
}

// func main() {
//     arr := []int{1, 2, 3, 4, 5} // Sums
//     sumOp := func(x, y int) int { return x + y }
//     stl := NewSegmentTreeLazy(arr, sumOp, SumIdentityLazy)
//     fmt.Println("Initial sum of [0, 4]:", stl.QueryRange(0, 4)) // Expected: 15
//     fmt.Println("Initial sum of [1, 3]:", stl.QueryRange(1, 3)) // Expected: 9 (2+3+4)

//     stl.UpdateRange(1, 3, 10) // Add 10 to elements at indices 1, 2, 3
//     // Conceptual array: [1, 12, 13, 14, 5]
//     fmt.Println("Sum of [0, 4] after update:", stl.QueryRange(0, 4)) // Expected: 1+12+13+14+5 = 45
//     fmt.Println("Sum of [1, 3] after update:", stl.QueryRange(1, 3)) // Expected: 12+13+14 = 39
//     fmt.Println("Sum of [0, 1] after update:", stl.QueryRange(0, 1)) // Expected: 1+12 = 13
// }
```

### D

```d
import std.stdio;
import std.array;
import std.algorithm; // For std.algorithm.max

// Define aggregation function type
alias SegmentAggregationFunc = int delegate(int, int);

// Identity element for sum operation
enum int SUM_IDENTITY_LAZY = 0;

class SegmentTreeLazy {
private:
    int[] tree;
    int[] lazy; // Lazy tag array
    int n;
    SegmentAggregationFunc op; // Operation (e.g., sum)
    int identityElement;

    void build(int nodeIdx, int low, int high, int[] arr) {
        if (low == high) {
            tree[nodeIdx] = arr[low];
            return;
        }
        
        int mid = low + (high - low) / 2;
        build(2 </em> nodeIdx + 1, low, mid, arr);
        build(2 <em> nodeIdx + 2, mid + 1, high, arr);
        tree[nodeIdx] = op(tree[2 </em> nodeIdx + 1], tree[2 <em> nodeIdx + 2]);
    }

    void pushDownLazy(int nodeIdx, int low, int high) {
        if (lazy[nodeIdx] != 0) { // If there's a pending update
            // Apply lazy tag to current node's value (adjust for range size if sum)
            tree[nodeIdx] += lazy[nodeIdx] </em> (high - low + 1); // Example: range sum update
            
            if (low != high) { // Not a leaf node
                // Propagate lazy tag to children
                lazy[2 <em> nodeIdx + 1] += lazy[nodeIdx];
                lazy[2 </em> nodeIdx + 2] += lazy[nodeIdx];
            }
            
            lazy[nodeIdx] = 0; // Clear lazy tag
        }
    }

    void updateRangeRecursive(int nodeIdx, int low, int high, int qLow, int qHigh, int val) {
        pushDownLazy(nodeIdx, low, high); // Push down any pending lazy updates first

        // No overlap
        if (qLow > high || qHigh < low) {
            return;
        }
        
        // Complete overlap
        if (qLow <= low && high <= qHigh) {
            lazy[nodeIdx] += val; // Apply lazy tag
            pushDownLazy(nodeIdx, low, high); // Apply and push down immediately
            return;
        }

        // Partial overlap
        int mid = low + (high - low) / 2;
        updateRangeRecursive(2 <em> nodeIdx + 1, low, mid, qLow, qHigh, val);
        updateRangeRecursive(2 </em> nodeIdx + 2, mid + 1, high, qLow, qHigh, val);
        tree[nodeIdx] = op(tree[2 <em> nodeIdx + 1], tree[2 </em> nodeIdx + 2]);
    }

    int queryRangeRecursive(int nodeIdx, int low, int high, int qLow, int qHigh) {
        pushDownLazy(nodeIdx, low, high); // Push down any pending lazy updates first

        // No overlap
        if (qLow > high || qHigh < low) {
            return identityElement;
        }
        
        // Complete overlap
        if (qLow <= low && high <= qHigh) {
            return tree[nodeIdx];
        }
        
        // Partial overlap
        int mid = low + (high - low) / 2;
        int leftVal = queryRangeRecursive(2 <em> nodeIdx + 1, low, mid, qLow, qHigh);
        int rightVal = queryRangeRecursive(2 </em> nodeIdx + 2, mid + 1, high, qLow, qHigh);
        
        return op(leftVal, rightVal);
    }

public:
    this(int[] arr, SegmentAggregationFunc operation = (a, b) => a + b, int id_elem = SUM_IDENTITY_LAZY) {
        n = arr.length;
        op = operation;
        identityElement = id_elem;
        tree = new int[4 <em> n];
        lazy = new int[4 </em> n]; // Initialize with zeros
        build(0, 0, n - 1, arr);
    }

    void updateRange(int qLow, int qHigh, int val) {
        updateRangeRecursive(0, 0, n - 1, qLow, qHigh, val);
    }

    int queryRange(int qLow, int qHigh) {
        return queryRangeRecursive(0, 0, n - 1, qLow, qHigh);
    }
}

// void main() {
//     int[] arr = [1, 2, 3, 4, 5]; // Sums
//     SegmentAggregationFunc sumOp = (a, b) => a + b;
//     auto stl = new SegmentTreeLazy(arr, sumOp, SUM_IDENTITY_LAZY);
//     writefln("Initial sum of [0, 4]: %s", stl.queryRange(0, 4)); // Expected: 15
//     writefln("Initial sum of [1, 3]: %s", stl.queryRange(1, 3)); // Expected: 9 (2+3+4)

//     stl.updateRange(1, 3, 10); // Add 10 to elements at indices 1, 2, 3
//     // Conceptual array: [1, 12, 13, 14, 5]
//     writefln("Sum of [0, 4] after update: %s", stl.queryRange(0, 4)); // Expected: 1+12+13+14+5 = 45
//     writefln("Sum of [1, 3] after update: %s", stl.queryRange(1, 3)); // Expected: 12+13+14 = 39
//     writefln("Sum of [0, 1] after update: %s", stl.queryRange(0, 1)); // Expected: 1+12 = 13
// }
```

