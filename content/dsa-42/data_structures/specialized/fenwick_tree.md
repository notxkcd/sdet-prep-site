---
title: "Fenwick Tree"
---

A `Fenwick Tree`, also known as a `Binary Indexed Tree (BIT)`, is a data structure that can efficiently update `elements` and calculate `prefix sums` (the sum of `elements` from the beginning of an `array` up to a given `index`) in a `table` of numbers.

It achieves `O(log N)` time complexity for both `updates` and `prefix sum queries`, making it much faster than a naive approach (`O(N)` for each `query` or `update`) and competitive with `Segment Trees` for these specific operations, often with less memory and simpler implementation.

## How it Works

### How it Works (Expanded)

The core idea of a `Fenwick Tree` is to represent an `array` as a `tree`-like structure where each `node` stores the sum of a certain range of `elements`. The magic lies in how these ranges are determined. Each `node` at `index i` in the `Fenwick Tree` stores the sum of `elements` from `index (i - (i & -i) + 1)` to `index i`.

---

Example: Array A = [1, 2, 3, 4, 5, 6, 7, 8]
Fenwick Tree (BIT) for Prefix Sums:

Indices:  1  2  3  4  5  6  7  8  (1-indexed for BIT)
Elements: A1 A2 A3 A4 A5 A6 A7 A8

BIT[1] stores A1
BIT[2] stores A1 + A2
BIT[3] stores A3
BIT[4] stores A1 + A2 + A3 + A4
BIT[5] stores A5
BIT[6] stores A5 + A6
BIT[7] stores A7
BIT[8] stores A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8

The key insight is `i & -i`, which isolates the rightmost set bit in the binary representation of `i`.
This value represents the size of the range covered by `BIT[i]`.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
class FenwickTree:
    def __init__(self, size):
        self.bit = [0] <em> (size + 1) # Fenwick Tree is 1-indexed
        self.size = size

    def update(self, index, delta):
        """Adds delta to element at index."""
        # Fenwick Tree is 1-indexed, so adjust index
        index += 1 
        while index <= self.size:
            self.bit[index] += delta
            index += index & (-index) # Move to parent

    def query(self, index):
        """Returns the sum of elements from index 0 up to index (inclusive)."""
        # Fenwick Tree is 1-indexed, so adjust index
        index += 1
        total_sum = 0
        while index > 0:
            total_sum += self.bit[index]
            index -= index & (-index) # Move to parent
        return total_sum

    def range_query(self, left, right):
        """Returns sum of elements from index left to right (inclusive)."""
        return self.query(right) - self.query(left - 1)

# Example Usage:
# arr = [1, 2, 3, 4, 5]
# ft = FenwickTree(len(arr))

# # Initialize Fenwick Tree with array elements
# for i, val in enumerate(arr):
#     ft.update(i, val)

# print("Prefix sum up to index 2 (0-indexed) [1,2,3]:", ft.query(2)) # Expected: 6
# print("Value at index 3 (0-indexed) [4]:", ft.range_query(3, 3)) # Expected: 4

# ft.update(0, 5) # arr becomes [6, 2, 3, 4, 5] (add 5 to arr[0])
# print("Prefix sum up to index 2 after update [6,2,3]:", ft.query(2)) # Expected: 11
```

### Javascript

```javascript
class FenwickTree {
    constructor(size) {
        this.bit = new Array(size + 1).fill(0); // Fenwick Tree is 1-indexed
        this.size = size;
    }

    update(index, delta) {
        /</em><em> Adds delta to element at index. </em>/
        // Fenwick Tree is 1-indexed, so adjust index
        index += 1; 
        while (index <= this.size) {
            this.bit[index] += delta;
            index += index & (-index); // Move to parent
        }
    }

    query(index) {
        /*<em> Returns the sum of elements from index 0 up to index (inclusive). </em>/
        // Fenwick Tree is 1-indexed, so adjust index
        index += 1;
        let totalSum = 0;
        while (index > 0) {
            totalSum += this.bit[index];
            index -= index & (-index); // Move to parent
        }
        return totalSum;
    }

    rangeQuery(left, right) {
        /*<em> Returns sum of elements from index left to right (inclusive). </em>/
        return this.query(right) - this.query(left - 1);
    }
}

// Example Usage:
// const arr = [1, 2, 3, 4, 5];
// const ft = new FenwickTree(arr.length);

// // Initialize Fenwick Tree with array elements
// for (let i = 0; i < arr.length; i++) {
//     ft.update(i, arr[i]);
// }

// console.log("Prefix sum up to index 2 (0-indexed) [1,2,3]:", ft.query(2)); // Expected: 6
// console.log("Value at index 3 (0-indexed) [4]:", ft.rangeQuery(3, 3)); // Expected: 4

// ft.update(0, 5); // arr becomes [6, 2, 3, 4, 5] (add 5 to arr[0])
// console.log("Prefix sum up to index 2 after update [6,2,3]:", ft.query(2)); // Expected: 11
```

### Typescript

```typescript
class FenwickTreeTS {
    private bit: number[];
    private size: number;

    constructor(size: number) {
        this.bit = new Array(size + 1).fill(0); // Fenwick Tree is 1-indexed
        this.size = size;
    }

    update(index: number, delta: number): void {
        /*<em> Adds delta to element at index. </em>/
        // Fenwick Tree is 1-indexed, so adjust index
        index += 1; 
        while (index <= this.size) {
            this.bit[index] += delta;
            index += index & (-index); // Move to parent
        }
    }

    query(index: number): number {
        /*<em> Returns the sum of elements from index 0 up to index (inclusive). </em>/
        // Fenwick Tree is 1-indexed, so adjust index
        index += 1;
        let totalSum = 0;
        while (index > 0) {
            totalSum += this.bit[index];
            index -= index & (-index); // Move to parent
        }
        return totalSum;
    }

    rangeQuery(left: number, right: number): number {
        /*<em> Returns sum of elements from index left to right (inclusive). </em>/
        return this.query(right) - this.query(left - 1);
    }
}

// Example Usage:
// const arrTS = [1, 2, 3, 4, 5];
// const ftTS = new FenwickTreeTS(arrTS.length);

// // Initialize Fenwick Tree with array elements
// for (let i = 0; i < arrTS.length; i++) {
//     ftTS.update(i, arrTS[i]);
// }

// console.log("Prefix sum up to index 2 (0-indexed) [1,2,3]:", ftTS.query(2)); // Expected: 6
// console.log("Value at index 3 (0-indexed) [4]:", ftTS.rangeQuery(3, 3)); // Expected: 4

// ftTS.update(0, 5); // arr becomes [6, 2, 3, 4, 5] (add 5 to arr[0])
// console.log("Prefix sum up to index 2 after update [6,2,3]:", ftTS.query(2)); // Expected: 11
```

### Cpp

```cpp
#include <vector>
#include <numeric> // For std::accumulate (if needed for initial array sum)
#include <iostream>

class FenwickTree {
private:
    std::vector<int> bit; // Fenwick Tree is 1-indexed
    int size;

public:
    FenwickTree(int s) : size(s) {
        bit.resize(size + 1, 0);
    }

    void update(int index, int delta) {
        /*<em> Adds delta to element at index. </em>/
        // Fenwick Tree is 1-indexed, so adjust index
        index += 1; 
        while (index <= size) {
            bit[index] += delta;
            index += index & (-index); // Move to parent
        }
    }

    int query(int index) {
        /*<em> Returns the sum of elements from index 0 up to index (inclusive). </em>/
        // Fenwick Tree is 1-indexed, so adjust index
        index += 1;
        int total_sum = 0;
        while (index > 0) {
            total_sum += bit[index];
            index -= index & (-index); // Move to parent
        }
        return total_sum;
    }

    int range_query(int left, int right) {
        /*<em> Returns sum of elements from index left to right (inclusive). </em>/
        return query(right) - query(left - 1);
    }
};

// Example Usage:
// int main() {
//     std::vector<int> arr = {1, 2, 3, 4, 5};
//     FenwickTree ft(arr.size());

//     // Initialize Fenwick Tree with array elements
//     for (int i = 0; i < arr.size(); ++i) {
//         ft.update(i, arr[i]);
//     }

//     std::cout << "Prefix sum up to index 2 (0-indexed) [1,2,3]: " << ft.query(2) << std::endl; // Expected: 6
//     std::cout << "Value at index 3 (0-indexed) [4]: " << ft.range_query(3, 3) << std::endl; // Expected: 4

//     ft.update(0, 5); // arr becomes conceptually [6, 2, 3, 4, 5] (add 5 to arr[0])
//     std::cout << "Prefix sum up to index 2 after update [6,2,3]: " << ft.query(2) << std::endl; // Expected: 11
//     return 0;
// }
```

### Go

```go
package main

import "fmt"

type FenwickTree struct {
    bit  []int // Fenwick Tree is 1-indexed
    size int
}

func NewFenwickTree(size int) <em>FenwickTree {
    return &FenwickTree{
        bit:  make([]int, size+1),
        size: size,
    }
}

func (ft </em>FenwickTree) Update(index, delta int) {
    /*<em> Adds delta to element at index. </em>/
    // Fenwick Tree is 1-indexed, so adjust index
    index += 1 
    for index <= ft.size {
        ft.bit[index] += delta
        index += index & (-index) // Move to parent
    }
}

func (ft <em>FenwickTree) Query(index int) int {
    /</em><em> Returns the sum of elements from index 0 up to index (inclusive). </em>/
    // Fenwick Tree is 1-indexed, so adjust index
    index += 1
    totalSum := 0
    for index > 0 {
        totalSum += ft.bit[index]
        index -= index & (-index) // Move to parent
    }
    return totalSum
}

func (ft <em>FenwickTree) RangeQuery(left, right int) int {
    /</em><em> Returns sum of elements from index left to right (inclusive). </em>/
    return ft.Query(right) - ft.Query(left-1)
}

// func main() {
//     arr := []int{1, 2, 3, 4, 5}
//     ft := NewFenwickTree(len(arr))

//     // Initialize Fenwick Tree with array elements
//     for i, val := range arr {
//         ft.Update(i, val)
//     }

//     fmt.Println("Prefix sum up to index 2 (0-indexed) [1,2,3]:", ft.Query(2)) // Expected: 6
//     fmt.Println("Value at index 3 (0-indexed) [4]:", ft.RangeQuery(3, 3))    // Expected: 4

//     ft.Update(0, 5) // arr becomes conceptually [6, 2, 3, 4, 5] (add 5 to arr[0])
//     fmt.Println("Prefix sum up to index 2 after update [6,2,3]:", ft.Query(2)) // Expected: 11
// }
```

### D

```d
import std.stdio;
import std.array;
import std.sum;

class FenwickTree {
    private int[] bit; // Fenwick Tree is 1-indexed
    private int _size;

    this(int size) {
        this._size = size;
        this.bit = new int[size + 1]; // Initialize with zeros
    }

    void update(int index, int delta) {
        /*<em> Adds delta to element at index. </em>/
        // Fenwick Tree is 1-indexed, so adjust index
        index += 1; 
        while (index <= _size) {
            this.bit[index] += delta;
            index += index & (-index); // Move to parent
        }
    }

    int query(int index) {
        /*<em> Returns the sum of elements from index 0 up to index (inclusive). </em>/
        // Fenwick Tree is 1-indexed, so adjust index
        index += 1;
        int totalSum = 0;
        while (index > 0) {
            totalSum += this.bit[index];
            index -= index & (-index); // Move to parent
        }
        return totalSum;
    }

    int rangeQuery(int left, int right) {
        /*<em> Returns sum of elements from index left to right (inclusive). </em>/
        return this.query(right) - this.query(left - 1);
    }
}

// void main() {
//     int[] arr = [1, 2, 3, 4, 5];
//     auto ft = new FenwickTree(arr.length);

//     // Initialize Fenwick Tree with array elements
//     foreach (i, val; arr) {
//         ft.update(cast(int)i, val);
//     }

//     writefln("Prefix sum up to index 2 (0-indexed) [1,2,3]: %s", ft.query(2)); // Expected: 6
//     writefln("Value at index 3 (0-indexed) [4]: %s", ft.rangeQuery(3, 3));    // Expected: 4

//     ft.update(0, 5); // arr becomes conceptually [6, 2, 3, 4, 5] (add 5 to arr[0])
//     writefln("Prefix sum up to index 2 after update [6,2,3]: %s", ft.query(2)); // Expected: 11
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

A `Fenwick Tree` is implemented as an `array`, but with an unconventional way of storing sums that allows for efficient `updates` and `queries`. It often uses 1-based indexing internally for simpler bitwise operations.

---

**`FenwickTree` Class:**
- `bit`: The underlying `array` that stores the computed sums. Its size is `N+1` for 1-based indexing.
- `size`: The size of the original `array` that the `Fenwick Tree` represents.
- **`update(index, delta)`:**
- Takes a 0-indexed `index` and a `delta` value to add to the `element` at that `index`.
- Converts the `index` to 1-based.
- It then iterates, adding `delta` to `bit[index]`, and moves to the next `node` to update by adding `index & (-index)` to the current `index`. This effectively propagates the `delta` up the implicit `tree`.

    </li>
- **`query(index)`:**
- Takes a 0-indexed `index`.
- Converts the `index` to 1-based.
- It iterates, adding `bit[index]` to a `total sum`, and moves to the next `node` to query by subtracting `index & (-index)` from the current `index`. This effectively sums up the relevant ranges down the implicit `tree`.

    </li>
- **`range_query(left, right)`:** Uses the `prefix sum` property to find the sum of `elements` within a given `range [left, right]` by calculating `query(right) - query(left - 1)`.

[Back to Implementation](#implementation)

## Applications

### Application

Fenwick Trees are a versatile tool in competitive programming and any application requiring efficient **dynamic prefix sums** and single-element updates. They are used in:
- **Data Analysis:** For quickly calculating running totals or sums of intervals in data streams that are frequently updated.
- **Financial Applications:** For tracking cumulative values over time or across various segments, where both updates and sum queries need to be fast.
- **Image Processing:** For certain operations involving summing pixel values in rectangular regions.
- **Online Gaming Leaderboards:** If players' scores are constantly updating and you need to query rank ranges efficiently.

