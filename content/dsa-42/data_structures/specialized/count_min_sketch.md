---
title: "Count-Min Sketch"
---

A `Count-Min Sketch` is a probabilistic data structure used to estimate the frequencies of `elements` in a data stream. It's particularly useful for handling massive datasets where storing exact counts for every unique `element` is infeasible due to memory constraints.

Like a `Bloom Filter`, it provides a space-efficient approximation, with a tunable trade-off between accuracy and memory usage. It never overestimates an `element`'s frequency by more than a small, known error margin, but it can overestimate. It never underestimates.

## How it Works

### How it Works (Expanded)

A `Count-Min Sketch` consists of a `2D array` (or matrix) of counters, typically initialized to zeros. The dimensions of this matrix are `width (w)` and `depth (d)`:
- `depth (d)`: The number of independent `hash functions` used. Determines the probability of overestimation.
- `width (w)`: The size of each `hash table`. Determines the maximum possible overestimation error.

---

Conceptual Count-Min Sketch:

      Hash Function 1 (h1) -> min(counter[0][h1(item)],
      Hash Function 2 (h2) ->             counter[1][h2(item)],
      Hash Function 3 (h3) ->             counter[2][h3(item)])

Matrix of Counters (w x d):
      w -> width
    +---+---+---+---+
d=0 | 0 | 0 | 0 | 0 |
    +---+---+---+---+
d=1 | 0 | 0 | 0 | 0 |
    +---+---+---+---+
d=2 | 0 | 0 | 0 | 0 |
    +---+---+---+---+

Adding an item "x":
- h1(x) = 1, h2(x) = 3, h3(x) = 0
- Increment counter[0][1], counter[1][3], counter[2][0]

Querying for "x":
- Look up counter[0][1], counter[1][3], counter[2][0]
- The estimate is the minimum of these values.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
import hashlib
import sys

class CountMinSketch:
    def __init__(self, width, depth):
        self.width = width # w: number of columns
        self.depth = depth # d: number of rows (hash functions)
        self.table = [[0] </em> width for _ in range(depth)]
        
        # Seeds for hash functions. A better approach would be to use universal hashing.
        self.seeds = [i <em> 997 + 1 for i in range(depth)] # Random seeds

    def _hash(self, item, seed_idx):
        # Using a simple hash function with different seeds
        # For production, use better hash functions like MurmurHash
        h = hashlib.sha256(f"{item}-{self.seeds[seed_idx]}".encode('utf-8')).hexdigest()
        return int(h, 16) % self.width

    def add(self, item, count=1):
        for i in range(self.depth):
            col = self._hash(item, i)
            self.table[i][col] += count

    def estimate(self, item):
        min_count = sys.maxsize # Initialize with a very large number
        for i in range(self.depth):
            col = self._hash(item, i)
            min_count = min(min_count, self.table[i][col])
        return min_count

# Example Usage:
# sketch = CountMinSketch(width=100, depth=5) # w=100, d=5
# stream_data = ["apple", "banana", "apple", "cherry", "banana", "apple", "date"]

# for item in stream_data:
#     sketch.add(item)

# print("Estimated frequency of 'apple':", sketch.estimate("apple"))   # Expected: ~3
# print("Estimated frequency of 'banana':", sketch.estimate("banana")) # Expected: ~2
# print("Estimated frequency of 'date':", sketch.estimate("date"))     # Expected: ~1
# print("Estimated frequency of 'grape':", sketch.estimate("grape"))   # Expected: ~0 (or small non-zero due to collisions)
```

### Javascript

```javascript
class CountMinSketch {
    constructor(width, depth) {
        this.width = width; // w: number of columns
        this.depth = depth; // d: number of rows (hash functions)
        this.table = Array(depth).fill(0).map(() => new Array(width).fill(0));
        
        // Seeds for hash functions. A better approach would be to use universal hashing.
        this.seeds = Array(depth).fill(0).map((_, i) => i </em> 997 + 1);
    }

    _hash(item, seedIdx) {
        // Simple string hash function (FNV-1a variant) combined with a seed
        // Not cryptographically secure, but often good enough for sketches.
        const str = <code>${item}-${this.seeds[seedIdx]}</code>;
        let hash = 0x811c9dc5; // FNV-1a offset basis
        for (let i = 0; i < str.length; i++) {
            hash ^= str.charCodeAt(i);
            hash += (hash << 1) + (hash << 4) + (hash << 7) + (hash << 8) + (hash << 24);
        }
        return (hash >>> 0) % this.width; // Ensure positive and within width
    }

    add(item, count = 1) {
        for (let i = 0; i < this.depth; i++) {
            const col = this._hash(item, i);
            this.table[i][col] += count;
        }
    }

    estimate(item) {
        let minCount = Infinity;
        for (let i = 0; i < this.depth; i++) {
            const col = this._hash(item, i);
            minCount = Math.min(minCount, this.table[i][col]);
        }
        return minCount;
    }
}

// const sketch = new CountMinSketch(100, 5); // w=100, d=5
// const streamData = ["apple", "banana", "apple", "cherry", "banana", "apple", "date"];

// for (const item of streamData) {
//     sketch.add(item);
// }

// console.log("Estimated frequency of 'apple':", sketch.estimate("apple"));   // Expected: ~3
// console.log("Estimated frequency of 'banana':", sketch.estimate("banana")); // Expected: ~2
// console.log("Estimated frequency of 'date':", sketch.estimate("date"));     // Expected: ~1
// console.log("Estimated frequency of 'grape':", sketch.estimate("grape"));   // Expected: ~0 (or small non-zero due to collisions)
```

### Typescript

```typescript
class CountMinSketchTS {
    private width: number;
    private depth: number;
    private table: number[][];
    private seeds: number[];

    constructor(width: number, depth: number) {
        this.width = width;
        this.depth = depth;
        this.table = Array(depth).fill(0).map(() => new Array(width).fill(0));
        this.seeds = Array(depth).fill(0).map((_, i) => i <em> 997 + 1);
    }

    private _hash(item: string | number, seedIdx: number): number {
        const str = <code>${item}-${this.seeds[seedIdx]}</code>;
        let hash = 0x811c9dc5; // FNV-1a offset basis
        for (let i = 0; i < str.length; i++) {
            hash ^= str.charCodeAt(i);
            hash += (hash << 1) + (hash << 4) + (hash << 7) + (hash << 8) + (hash << 24);
        }
        return (hash >>> 0) % this.width;
    }

    public add(item: string | number, count: number = 1): void {
        for (let i = 0; i < this.depth; i++) {
            const col = this._hash(item, i);
            this.table[i][col] += count;
        }
    }

    public estimate(item: string | number): number {
        let minCount = Infinity;
        for (let i = 0; i < this.depth; i++) {
            const col = this._hash(item, i);
            minCount = Math.min(minCount, this.table[i][col]);
        }
        return minCount;
    }
}

// const sketchTS = new CountMinSketchTS(100, 5);
// const streamDataTS: (string | number)[] = ["apple", "banana", "apple", "cherry", "banana", "apple", "date"];

// for (const item of streamDataTS) {
//     sketchTS.add(item);
// }

// console.log("Estimated frequency of 'apple':", sketchTS.estimate("apple"));
// console.log("Estimated frequency of 'banana':", sketchTS.estimate("banana"));
// console.log("Estimated frequency of 'date':", sketchTS.estimate("date"));
// console.log("Estimated frequency of 'grape':", sketchTS.estimate("grape"));
```

### Cpp

```cpp
#include <vector>
#include <string>
#include <algorithm> // For std::min
#include <limits>    // For std::numeric_limits
#include <functional> // For std::hash
#include <iostream>

// A simple hash function (for demonstration)
// In a real Count-Min Sketch, you'd use k independent universal hash functions.
unsigned int custom_hash(const std::string& s, unsigned int seed, unsigned int width) {
    unsigned int hash_val = seed;
    for (char c : s) {
        hash_val = (hash_val </em> 31) + c;
    }
    return hash_val % width;
}

class CountMinSketch {
private:
    std::vector<std::vector<int>> table;
    int width;
    int depth;
    std::vector<unsigned int> seeds; // Seeds for hash functions

public:
    CountMinSketch(int w, int d) : width(w), depth(d) {
        table.resize(depth, std::vector<int>(width, 0));
        seeds.resize(depth);
        // Initialize seeds (simple, for demo)
        for (int i = 0; i < depth; ++i) {
            seeds[i] = i <em> 997 + 1; // Arbitrary seeds
        }
    }

    void add(const std::string& item, int count = 1) {
        for (int i = 0; i < depth; ++i) {
            unsigned int col = custom_hash(item, seeds[i], width);
            table[i][col] += count;
        }
    }

    int estimate(const std::string& item) {
        int min_count = std::numeric_limits<int>::max();
        for (int i = 0; i < depth; ++i) {
            unsigned int col = custom_hash(item, seeds[i], width);
            min_count = std::min(min_count, table[i][col]);
        }
        return min_count;
    }
};

// int main() {
//     CountMinSketch sketch(100, 5); // w=100, d=5
//     std::vector<std::string> stream_data = {"apple", "banana", "apple", "cherry", "banana", "apple", "date"};

//     for (const auto& item : stream_data) {
//         sketch.add(item);
//     }

//     std::cout << "Estimated frequency of 'apple': " << sketch.estimate("apple") << std::endl;   // Expected: ~3
//     std::cout << "Estimated frequency of 'banana': " << sketch.estimate("banana") << std::endl; // Expected: ~2
//     std::cout << "Estimated frequency of 'date': " << sketch.estimate("date") << std::endl;     // Expected: ~1
//     std::cout << "Estimated frequency of 'grape': " << sketch.estimate("grape") << std::endl;   // Expected: ~0 (or small non-zero)
//     return 0;
// }
```

### Go

```go
package main

import (
    "fmt"
    "hash/fnv"
    "math"
)

type CountMinSketch struct {
    width  int
    depth  int
    table  [][]int
    seeds  []uint32 // Seeds for hash functions
}

func (cms </em>CountMinSketch) hash(item string, seed uint32) uint32 {
    h := fnv.New32a()
    h.Write([]byte(item))
    h.Write([]byte(fmt.Sprintf("%d", seed))) // Mix in the seed
    return h.Sum32() % uint32(cms.width)
}

func NewCountMinSketch(width, depth int) <em>CountMinSketch {
    table := make([][]int, depth)
    for i := range table {
        table[i] = make([]int, width)
    }

    seeds := make([]uint32, depth)
    for i := range seeds {
        seeds[i] = uint32(i</em>997 + 1) // Simple seed generation
    }

    return &CountMinSketch{
        width:  width,
        depth:  depth,
        table:  table,
        seeds:  seeds,
    }
}

func (cms <em>CountMinSketch) Add(item string, count int) {
    for i := 0; i < cms.depth; i++ {
        col := cms.hash(item, cms.seeds[i])
        cms.table[i][col] += count
    }
}

func (cms </em>CountMinSketch) Estimate(item string) int {
    minCount := math.MaxInt32
    for i := 0; i < cms.depth; i++ {
        col := cms.hash(item, cms.seeds[i])
        if cms.table[i][col] < minCount {
            minCount = cms.table[i][col]
        }
    }
    return minCount
}

// func main() {
//     sketch := NewCountMinSketch(100, 5) // w=100, d=5
//     streamData := []string{"apple", "banana", "apple", "cherry", "banana", "apple", "date"}

//     for _, item := range streamData {
//         sketch.Add(item, 1)
//     }

//     fmt.Println("Estimated frequency of 'apple':", sketch.Estimate("apple"))   // Expected: ~3
//     fmt.Println("Estimated frequency of 'banana':", sketch.Estimate("banana")) // Expected: ~2
//     fmt.Println("Estimated frequency of 'date':", sketch.Estimate("date"))     // Expected: ~1
//     fmt.Println("Estimated frequency of 'grape':", sketch.Estimate("grape"))   // Expected: ~0 (or small non-zero)
// }
```

### D

```d
import std.stdio;
import std.array;
import std.algorithm;
import std.string;
import std.conv;
import std.numeric; // For std.numeric.min

// A simple hash function (for demonstration)
// In a real Count-Min Sketch, you'd use k independent universal hash functions.
uint custom_hash(string s, uint seed, uint width) {
    uint hash_val = seed;
    foreach (char c; s) {
        hash_val = (hash_val <em> 31) + c;
    }
    return hash_val % width;
}

class CountMinSketch {
private:
    int[][] table;
    int width;
    int depth;
    uint[] seeds; // Seeds for hash functions

public:
    this(int w, int d) {
        width = w;
        depth = d;
        table = new int[depth][width]; // Initialize with zeros
        seeds = new uint[depth];
        // Initialize seeds (simple, for demo)
        foreach (i; 0..depth) {
            seeds[i] = cast(uint)(i </em> 997 + 1); // Arbitrary seeds
        }
    }

    void add(string item, int count = 1) {
        foreach (i; 0..depth) {
            uint col = custom_hash(item, seeds[i], cast(uint)width);
            table[i][col] += count;
        }
    }

    int estimate(string item) {
        int min_count = int.max;
        foreach (i; 0..depth) {
            uint col = custom_hash(item, seeds[i], cast(uint)width);
            min_count = min(min_count, table[i][col]);
        }
        return min_count;
    }
}

// void main() {
//     auto sketch = new CountMinSketch(100, 5); // w=100, d=5
//     string[] stream_data = ["apple", "banana", "apple", "cherry", "banana", "apple", "date"];

//     foreach (item; stream_data) {
//         sketch.add(item);
//     }

//     writefln("Estimated frequency of 'apple': %s", sketch.estimate("apple"));   // Expected: ~3
//     writefln("Estimated frequency of 'banana': %s", sketch.estimate("banana")); // Expected: ~2
//     writefln("Estimated frequency of 'date': %s", sketch.estimate("date"));     // Expected: ~1
//     writefln("Estimated frequency of 'grape': %s", sketch.estimate("grape"));   // Expected: ~0 (or small non-zero)
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

A `Count-Min Sketch` is implemented using a `2D array` of counters and a set of independent `hash functions`. The core logic involves applying these `hash functions` to map incoming `items` to specific `columns` in each `row` of the `table`.

---

**Class Structure:**
- `table`: A `d x w` `matrix` (`2D array`) of integers, initialized to zeros. Each `row` corresponds to a different `hash function`.
- `width (w)`: The number of `columns` in the `table`. Affects the overestimation error.
- `depth (d)`: The number of `rows` in the `table`, which is also the number of independent `hash functions`. Affects the probability of the overestimation error occurring.
- `seeds`: A `list`/`vector`/`array` of random `seeds`, one for each `hash function`. Using different `seeds` makes the `hash functions` approximately independent.

**`_hash(item, seed_idx)`:** A helper function to generate a `hash value` for an `item` using a specific `seed` and mapping it to a `column index` within the `width`.

**`add(item, count=1)`:**
- For each of the `d hash functions` (i.e., for each `row` in the `table`):
- Calculate the `column index` by hashing the `item` with the respective `seed`.
- Increment the counter at `table[row][col]` by the `count_increment`.

    </li>

**`estimate(item)`:**
- Initializes `min_count` to a very large value.
- For each of the `d hash functions`:
- Calculate the `column index` by hashing the `item`.
- Retrieve the counter value `table[row][col]`.
- Update `min_count` to be the minimum of `min_count` and the retrieved counter value.

    </li>
- Returns `min_count` as the estimated `frequency`.

[Back to Implementation](#implementation)

## Applications

### Application

Count-Min Sketch is invaluable in big data analytics and network monitoring where exact counts are too expensive to maintain, but approximate frequencies are sufficient. Its applications include:
- **Network Traffic Analysis:** Estimating the number of packets from a specific IP address or destination, identifying "heavy hitters" (e.g., Denial of Service attacks, popular content).
- **Database Query Optimization:** Providing approximate answers to `GROUP BY` queries or estimating join sizes in very large databases.
- **Stream Analytics:** Tracking popular items or trends in real-time data streams (e.g., trending topics on social media).
- **Web Analytics:** Estimating frequencies of URL access, user actions, or search queries.
- **Anomaly Detection:** Identifying unusual patterns in data by flagging items with unexpectedly high or low frequencies.

