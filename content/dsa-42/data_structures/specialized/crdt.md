---
title: "CRDT"
---

A `CRDT (Conflict-free Replicated Data Type)` is a data structure that is designed to be replicated across multiple computers in a network, where updates can be made independently and concurrently without the need for complex synchronization or consensus mechanisms. The mathematical properties of `CRDTs` guarantee that these concurrent updates will eventually converge to a consistent state.

This makes them "amazing" for building collaborative applications like online text editors, shared whiteboards, and distributed databases where multiple users can make changes simultaneously without conflicts.

## How it Works

### How it Works (Expanded)

There are two main types of `CRDTs`: `State-based (CvRDTs)` and `Operation-based (CmRDTs)`.
- **`State-based (Convergent Replicated Data Types)`:** Each replica merges its state with the state of other replicas. The merge function must be commutative, associative, and idempotent.
- **`Operation-based (Commutative Replicated Data Types)`:** Operations (updates) are sent to other replicas and applied. The operations must be commutative, meaning they can be applied in any order and still result in the same final state.

A simple example is the **`G-Counter (Grow-Only Counter)`**, a state-based `CRDT`.

---

Example G-Counter (3 replicas):

Replica A: [0, 0, 0]
Replica B: [0, 0, 0]
Replica C: [0, 0, 0]
- Replica A increments its own count: A -> [1, 0, 0]
- Replica C increments its own count: C -> [0, 0, 1]

Now, A and C sync. The merge operation is a pairwise maximum of the vectors:
- Merge(A, C) -> [max(1,0), max(0,0), max(0,1)] -> [1, 0, 1]
- Both A and C now have the state [1, 0, 1].
- Replica B increments its own count twice: B -> [0, 2, 0]
- B syncs with A: Merge(B, A) -> [max(0,1), max(2,0), max(0,1)] -> [1, 2, 1]
- Both A and B now have the state [1, 2, 1].

The total value of the counter is the sum of the vector: 1 + 2 + 1 = 4.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
# Conceptual implementation of a G-Counter (Grow-Only Counter) CRDT in Python

class GCounter:
    def __init__(self, num_replicas, replica_id):
        self.num_replicas = num_replicas
        self.replica_id = replica_id
        self.payload = [0] * num_replicas # Vector of counts for each replica

    def increment(self):
        # Only increment the count for this replica's index
        self.payload[self.replica_id] += 1

    @property
    def value(self):
        # The total value is the sum of all counts in the payload vector
        return sum(self.payload)

    def merge(self, other_gcounter):
        # Merge by taking the pairwise maximum of the payloads
        if self.num_replicas != other_gcounter.num_replicas:
            raise ValueError("Counters must have the same number of replicas to merge.")
        
        for i in range(self.num_replicas):
            self.payload[i] = max(self.payload[i], other_gcounter.payload[i])

# Example Usage:
# Imagine 3 replicas (A, B, C)
# replica_a = GCounter(num_replicas=3, replica_id=0)
# replica_b = GCounter(num_replicas=3, replica_id=1)
# replica_c = GCounter(num_replicas=3, replica_id=2)

# replica_a.increment()
# print(f"Replica A value: {replica_a.value}") # 1

# replica_b.increment()
# replica_b.increment()
# print(f"Replica B value: {replica_b.value}") # 2

# replica_a.merge(replica_b)
# print(f"Replica A after merging with B: {replica_a.value}") # 3
# print(f"Replica B after merging with A (state unchanged): {replica_b.value}") # 2

# replica_b.merge(replica_a)
# print(f"Replica B after merging with A: {replica_b.value}") # 3
```

### Javascript

```javascript
// Conceptual implementation of a G-Counter (Grow-Only Counter) CRDT in JavaScript

class GCounter {
    constructor(numReplicas, replicaId) {
        this.numReplicas = numReplicas;
        this.replicaId = replicaId;
        this.payload = new Array(numReplicas).fill(0); // Vector of counts for each replica
    }

    increment() {
        // Only increment the count for this replica's index
        this.payload[this.replicaId]++;
    }

    getValue() {
        // The total value is the sum of all counts in the payload vector
        return this.payload.reduce((sum, val) => sum + val, 0);
    }

    merge(otherGCounter) {
        // Merge by taking the pairwise maximum of the payloads
        if (this.numReplicas !== otherGCounter.numReplicas) {
            throw new Error("Counters must have the same number of replicas to merge.");
        }
        
        for (let i = 0; i < this.numReplicas; i++) {
            this.payload[i] = Math.max(this.payload[i], otherGCounter.payload[i]);
        }
    }
}

// Example Usage:
// Imagine 3 replicas (A, B, C)
// const replicaA = new GCounter(3, 0);
// const replicaB = new GCounter(3, 1);
// const replicaC = new GCounter(3, 2);

// replicaA.increment();
// console.log(<code>Replica A value: ${replicaA.getValue()}</code>); // 1

// replicaB.increment();
// replicaB.increment();
// console.log(<code>Replica B value: ${replicaB.getValue()}</code>); // 2

// replicaA.merge(replicaB);
// console.log(<code>Replica A after merging with B: ${replicaA.getValue()}</code>); // 3
// console.log(<code>Replica B after merging with A (state unchanged): ${replicaB.getValue()}</code>); // 2

// replicaB.merge(replicaA);
// console.log(<code>Replica B after merging with A: ${replicaB.getValue()}</code>); // 3
```

### Cpp

```cpp
#include <vector>
#include <numeric>   // For std::accumulate
#include <algorithm> // For std::max
#include <stdexcept>
#include <iostream>

// Conceptual implementation of a G-Counter (Grow-Only Counter) CRDT
class GCounter {
private:
    std::vector<int> payload;
    int num_replicas;
    int replica_id;

public:
    GCounter(int n_replicas, int r_id) : num_replicas(n_replicas), replica_id(r_id) {
        payload.resize(n_replicas, 0);
    }

    void increment() {
        // Only increment the count for this replica's index
        payload[replica_id]++;
    }

    int getValue() const {
        // The total value is the sum of all counts in the payload vector
        return std::accumulate(payload.begin(), payload.end(), 0);
    }

    void merge(const GCounter& other_gcounter) {
        // Merge by taking the pairwise maximum of the payloads
        if (num_replicas != other_gcounter.num_replicas) {
            throw std::runtime_error("Counters must have the same number of replicas to merge.");
        }
        
        for (int i = 0; i < num_replicas; ++i) {
            payload[i] = std::max(payload[i], other_gcounter.payload[i]);
        }
    }
};

// Example Usage:
// int main() {
//     // Imagine 3 replicas (A, B, C)
//     GCounter replicaA(3, 0);
//     GCounter replicaB(3, 1);
//     GCounter replicaC(3, 2);

//     replicaA.increment();
//     std::cout << "Replica A value: " << replicaA.getValue() << std::endl; // 1

//     replicaB.increment();
//     replicaB.increment();
//     std::cout << "Replica B value: " << replicaB.getValue() << std::endl; // 2

//     replicaA.merge(replicaB);
//     std::cout << "Replica A after merging with B: " << replicaA.getValue() << std::endl; // 3
//     std::cout << "Replica B after merging with A (state unchanged): " << replicaB.getValue() << std::endl; // 2

//     replicaB.merge(replicaA);
//     std::cout << "Replica B after merging with A: " << replicaB.getValue() << std::endl; // 3
//     return 0;
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

The code demonstrates a `G-Counter`, one of the simplest `CRDTs`. Each replica maintains a vector representing the state of the entire system from its perspective.

---

**`GCounter` Class:**
- `num_replicas`: The total number of participants (replicas) in the system.
- `replica_id`: The unique identifier (index) for the current replica.
- `payload`: A `vector` or `array` of size `num_replicas`. `payload[i]` stores the number of increments observed at replica `i`.
- **`increment()`:** The only update operation. A replica can only increment its own counter in the `payload` vector.
- **`value()` or `getValue()`:** The total value is the sum of all elements in the `payload` vector.
- **`merge(other)`:** Takes another `GCounter`'s state and merges it by taking the element-wise maximum of the two `payload` vectors. This ensures that no increment is ever lost.

[Back to Implementation](#implementation)

## Applications

### Application

CRDTs are the foundational technology for many modern real-time collaborative and distributed systems. Their primary application is in building applications where multiple users can edit shared data concurrently, such as **collaborative text editors (e.g., Google Docs, Figma)**, shared whiteboards, and multiplayer games. They are also used in distributed databases and caching systems (like **Riak**) to ensure high availability and eventual consistency across geographically distributed replicas without requiring expensive, real-time consensus.

