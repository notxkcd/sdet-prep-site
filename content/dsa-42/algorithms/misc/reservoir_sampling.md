---
title: "Reservoir Sampling"
---

`Reservoir Sampling` is a family of algorithms for selecting a simple random sample of `k` items from a `population` of `unknown size` `n`. This is particularly useful when the data comes in a stream and its total size is not known beforehand. It allows you to maintain a `sample` of `k` items such that at any point, the `sample` is a `uniform random sample` of the items seen so far.

The most common version, `Algorithm R` by Alan Waterman, is simple to implement and requires only `O(k)` space.

## How it Works

### How it Works (Expanded)

The `Reservoir Sampling (Algorithm R)` algorithm works by maintaining a "reservoir" `array` of size `k`. It processes the stream of items one by one. The first `k` items are placed directly into the reservoir. For each subsequent `item i` (where `i > k`), the algorithm generates a random number `j` between 0 and `i` (inclusive). If `j < k`, the `item` at `reservoir[j]` is replaced with `item i`.

---

Example: Select k=3 items from a stream [1, 2, 3, 4, 5, 6, 7, 8, ...]

1. Initialize reservoir:
- Reservoir = [1, 2, 3]

2. Process item i=4 (index 3):
- Generate random j from 0 to 3. Say j=1.
- j < k? (1 < 3) Yes.
- Reservoir[1] = 4. Reservoir becomes [1, 4, 3].

3. Process item i=5 (index 4):
- Generate random j from 0 to 4. Say j=4.
- j < k? (4 < 3) No.
- Reservoir remains [1, 4, 3].

4. Process item i=6 (index 5):
- Generate random j from 0 to 5. Say j=0.
- j < k? (0 < 3) Yes.
- Reservoir[0] = 6. Reservoir becomes [6, 4, 3].

... and so on. At any point, the reservoir holds a uniform random sample of size 3 from the items processed so far.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
import random

def reservoir_sampling(stream, k):
    """
    Selects k items from a stream of unknown size using Reservoir Sampling (Algorithm R).
    <code>stream</code>: an iterable of items.
    <code>k</code>: the size of the sample.
    """
    if k <= 0:
        return []

    reservoir = []
    
    # Fill the reservoir with the first k items
    for i, item in enumerate(stream):
        if i < k:
            reservoir.append(item)
        else:
            # Generate a random index j from 0 to i
            j = random.randint(0, i)
            # If j is within the reservoir size, replace the element
            if j < k:
                reservoir[j] = item
    
    return reservoir

# Example
# data_stream = [i for i in range(1, 101)] # Stream of numbers 1-100
# sample_size = 10
# sample = reservoir_sampling(data_stream, sample_size)
# print(f"Sample of size {sample_size}:", sample)
# print(f"Length of sample: {len(sample)}") # Expected: 10
```

### Javascript

```javascript
function reservoirSampling(stream, k) {
    /*<em>
     </em> Selects k items from a stream of unknown size using Reservoir Sampling.
     <em> <code>stream</code>: an array representing the data stream.
     </em> <code>k</code>: the size of the sample.
     <em>/
    if (k <= 0) {
        return [];
    }

    const reservoir = [];
    
    stream.forEach((item, i) => {
        if (i < k) {
            reservoir.push(item);
        } else {
            // Generate a random index j from 0 to i
            const j = Math.floor(Math.random() </em> (i + 1));
            // If j is within the reservoir size, replace the element
            if (j < k) {
                reservoir[j] = item;
            }
        }
    });
    
    return reservoir;
}

// const dataStream = Array.from({length: 100}, (_, i) => i + 1); // Stream of numbers 1-100
// const sampleSize = 10;
// const sample = reservoirSampling(dataStream, sampleSize);
// console.log(<code>Sample of size ${sampleSize}:</code>, sample);
// console.log(<code>Length of sample: ${sample.length}</code>); // Expected: 10
```

### Typescript

```typescript
function reservoirSamplingTS<T>(stream: T[], k: number): T[] {
    /*<em>
     </em> Selects k items from a stream of unknown size using Reservoir Sampling.
     <em> <code>stream</code>: an array representing the data stream.
     </em> <code>k</code>: the size of the sample.
     <em>/
    if (k <= 0) {
        return [];
    }

    const reservoir: T[] = [];
    
    stream.forEach((item, i) => {
        if (i < k) {
            reservoir.push(item);
        } else {
            // Generate a random index j from 0 to i
            const j = Math.floor(Math.random() </em> (i + 1));
            // If j is within the reservoir size, replace the element
            if (j < k) {
                reservoir[j] = item;
            }
        }
    });
    
    return reservoir;
}

// const dataStreamTS: number[] = Array.from({length: 100}, (_, i) => i + 1);
// const sampleSizeTS = 10;
// const sampleTS = reservoirSamplingTS(dataStreamTS, sampleSizeTS);
// console.log(<code>Sample of size ${sampleSizeTS}:</code>, sampleTS);
// console.log(<code>Length of sample: ${sampleTS.length}</code>); // Expected: 10
```

### Cpp

```cpp
#include <vector>
#include <iostream>
#include <random>    // For std::mt19937 and std::uniform_int_distribution

std::vector<int> reservoirSampling(const std::vector<int>& stream, int k) {
    if (k <= 0) {
        return {};
    }

    std::vector<int> reservoir;
    
    // Create a random number generator
    std::random_device rd;
    std::mt19937 g(rd());

    for (int i = 0; i < stream.size(); ++i) {
        if (i < k) {
            reservoir.push_back(stream[i]);
        } else {
            // Generate a random index j from 0 to i
            std::uniform_int_distribution<int> dist(0, i);
            int j = dist(g);
            // If j is within the reservoir size, replace the element
            if (j < k) {
                reservoir[j] = stream[i];
            }
        }
    }
    
    return reservoir;
}

// int main() {
//     std::vector<int> data_stream;
//     for(int i = 1; i <= 100; ++i) data_stream.push_back(i);
    
//     int sample_size = 10;
//     std::vector<int> sample = reservoirSampling(data_stream, sample_size);

//     std::cout << "Sample of size " << sample_size << ": ";
//     for(int val : sample) {
//         std::cout << val << " ";
//     }
//     std::cout << std::endl;
//     std::cout << "Length of sample: " << sample.size() << std::endl; // 10
//     return 0;
// }
```

### Go

```go
package main

import (
    "fmt"
    "math/rand"
    "time"
)

func reservoirSampling(stream []interface{}, k int) []interface{} {
    if k <= 0 {
        return nil
    }

    reservoir := make([]interface{}, 0, k)
    rand.Seed(time.Now().UnixNano())

    for i, item := range stream {
        if i < k {
            reservoir = append(reservoir, item)
        } else {
            // Generate a random index j from 0 to i
            j := rand.Intn(i + 1)
            // If j is within the reservoir size, replace the element
            if j < k {
                reservoir[j] = item
            }
        }
    }
    
    return reservoir
}

// func main() {
//     dataStream := make([]interface{}, 100)
//     for i := 0; i < 100; i++ {
//         dataStream[i] = i + 1
//     }
    
//     sampleSize := 10
//     sample := reservoirSampling(dataStream, sampleSize)
    
//     fmt.Printf("Sample of size %d: %v\n", sampleSize, sample)
//     fmt.Printf("Length of sample: %d\n", len(sample)) // 10
// }
```

### D

```d
import std.stdio;
import std.random;
import std.array;

T[] reservoirSampling(T)(T[] stream, int k) {
    if (k <= 0) {
        return [];
    }

    T[] reservoir;
    reservoir.reserve(k); // Pre-allocate capacity
    
    auto rnd = Random(unpredictableSeed);

    foreach (i, item; stream) {
        if (i < k) {
            reservoir ~= item;
        } else {
            // Generate a random index j from 0 to i
            auto j = uniform(0, i + 1, rnd);
            // If j is within the reservoir size, replace the element
            if (j < k) {
                reservoir[j] = item;
            }
        }
    }
    
    return reservoir;
}

// void main() {
//     int[] dataStream;
//     foreach (i; 1 .. 101) {
//         dataStream ~= i;
//     }
    
//     int sampleSize = 10;
//     auto sample = reservoirSampling(dataStream, sampleSize);

//     writefln("Sample of size %s: %s", sampleSize, sample);
//     writeln("Length of sample: ", sample.length); // 10
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

`Reservoir Sampling (Algorithm R)` is an elegant algorithm for selecting a random sample of `k` items from a data stream of unknown size `N`.

---

**`reservoir_sampling(stream, k)` Function:**
- `stream`: An iterable source of data.
- `k`: The desired size of the random sample.

**Algorithm Steps:**
- **Initialization:** An empty `reservoir` array is created.
- **Iterate Through Stream:** The algorithm iterates through the `stream`, keeping track of the current `index i`.
- **Fill Initial Reservoir:** For the first `k` items (`i < k`), they are directly added to the `reservoir`.
- **Process Subsequent Items:** For each `item i` from `k+1` onwards:
- A random integer `j` is generated between 0 and `i` (inclusive).
- **Replacement Logic:** If `j` is less than `k` (the size of the reservoir), the `item` at `reservoir[j]` is replaced with the current `item` from the stream.
- The probability of this replacement for any `item i` is `k / (i+1)`. This ensures that at any point `i`, any `item` from the beginning up to `i` has an equal probability (`k / (i+1)`) of being in the reservoir.

            </li>

    </li>

**Result:**
- After the entire `stream` has been processed, the `reservoir` contains a simple random sample of `k` items from the whole stream.

[Back to Implementation](#implementation)

## Applications

### Application

`Reservoir Sampling` is crucial in scenarios where data is too large to fit into memory or is arriving in a continuous stream, and a representative random sample is needed:
- **Big Data Analytics:** Sampling a small subset of a massive dataset (e.g., from a log file, a database query, or a sensor stream) for statistical analysis, machine learning model training, or data exploration.
- **Online Advertising:** Randomly selecting an ad to display from a large pool of eligible ads for a given user impression, where the pool size is unknown.
- **Network Traffic Monitoring:** Capturing a random sample of network packets for analysis without storing the entire traffic stream.
- **Streaming Algorithms:** As a fundamental building block in various streaming algorithms that need to maintain a random sample of the data seen so far.
- **Database Query Optimization:** Estimating query result sizes or data distributions by sampling from large tables.

