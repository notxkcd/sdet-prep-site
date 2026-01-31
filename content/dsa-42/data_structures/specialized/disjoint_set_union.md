---
title: "Disjoint Set Union"
---

A `Disjoint Set Union (DSU)` data structure, also known as `Union-Find`, is a data structure that keeps track of a set of `elements` partitioned into a number of disjoint (non-overlapping) subsets. It performs two primary operations:
- **`Find`:** Determines which subset a particular `element` is in. It returns a "representative" (or "`root`") of that subset.
- **`Union`:** Merges two subsets into a single subset.

`DSU` is widely used in algorithms that involve grouping `elements`, such as finding `connected components` in a `graph`, `Kruskal's algorithm` for `Minimum Spanning Tree (MST)`, and solving various grouping or connectivity problems.

## How it Works

### How it Works (Expanded)

The `DSU data structure` is typically implemented using `arrays` to represent the `parent` of each `element`. Initially, each `element` is in its own `set`, meaning it is its own `parent`.

---

Key Ideas:

1.  **Representation:** Each element has a 'parent' pointer. If an element's parent is itself, it's the root (representative) of its set.
    Array `parent`: [0, 1, 2, 3, 4, 5]  (Initially, each element is its own parent)
    Indices:       0  1  2  3  4  5

2.  **Find Operation:** To find the representative of an element, follow its parent pointers until a root is reached.
    (Example: `Find(3)` where `parent[3]=1`, `parent[1]=root(0)` -> returns 0)

3.  **Union Operation:** To `union` two sets (represented by elements `A` and `B`), find the `roots` of `A` and `B`. If they are different, make one `root` the `parent` of the other.
    (Example: `Union(2,3)` where `root(2)=2`, `root(3)=0`. Make 0 parent of 2. `parent[2]=0`)

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n)) # Each element is initially its own parent
        self.rank = [0] * n          # Used for union by rank optimization

    def find(self, i):
        # Path compression
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        # Union by rank
        i_root = self.find(i)
        j_root = self.find(j)

        if i_root != j_root:
            if self.rank[i_root] < self.rank[j_root]:
                self.parent[i_root] = j_root
            elif self.rank[i_root] > self.rank[j_root]:
                self.parent[j_root] = i_root
            else:
                self.parent[j_root] = i_root
                self.rank[i_root] += 1
            return True # Successfully merged
        return False # Already in the same set

# Example Usage:
# dsu = DisjointSetUnion(5) # Elements 0, 1, 2, 3, 4

# dsu.union(0, 1) # Merge set of 0 and set of 1
# dsu.union(2, 3) # Merge set of 2 and set of 3
# dsu.union(0, 2) # Merge set containing {0,1} and set containing {2,3}

# print("Parent array:", dsu.parent) # Example output: [0, 0, 0, 0, 4] (after path compression)
# print("Find(3):", dsu.find(3))     # Expected: 0
# print("Find(4):", dsu.find(4))     # Expected: 4
# print("Are 1 and 3 connected?", dsu.find(1) == dsu.find(3)) # True
# print("Are 1 and 4 connected?", dsu.find(1) == dsu.find(4)) # False
```

### Javascript

```javascript
class DisjointSetUnion {
    constructor(n) {
        this.parent = Array.from({ length: n }, (_, i) => i); // Each element is initially its own parent
        this.rank = new Array(n).fill(0); // Used for union by rank optimization
    }

    find(i) {
        // Path compression
        if (this.parent[i] === i) {
            return i;
        }
        this.parent[i] = this.find(this.parent[i]);
        return this.parent[i];
    }

    union(i, j) {
        // Union by rank
        let iRoot = this.find(i);
        let jRoot = this.find(j);

        if (iRoot !== jRoot) {
            if (this.rank[iRoot] < this.rank[jRoot]) {
                this.parent[iRoot] = jRoot;
            } else if (this.rank[iRoot] > this.rank[jRoot]) {
                this.parent[jRoot] = iRoot;
            } else {
                this.parent[jRoot] = iRoot;
                this.rank[iRoot]++;
            }
            return true; // Successfully merged
        }
        return false; // Already in the same set
    }
}

// Example Usage:
// const dsu = new DisjointSetUnion(5); // Elements 0, 1, 2, 3, 4

// dsu.union(0, 1); // Merge set of 0 and set of 1
// dsu.union(2, 3); // Merge set of 2 and set of 3
// dsu.union(0, 2); // Merge set containing {0,1} and set containing {2,3}

// console.log("Parent array:", dsu.parent); // Example output: [0, 0, 0, 0, 4] (after path compression)
// console.log("Find(3):", dsu.find(3));     // Expected: 0
// console.log("Find(4):", dsu.find(4));     // Expected: 4
// console.log("Are 1 and 3 connected?", dsu.find(1) === dsu.find(3)); // true
// console.log("Are 1 and 4 connected?", dsu.find(1) === dsu.find(4)); // false
```

### Cpp

```cpp
#include <vector>
#include <numeric> // For std::iota
#include <iostream>

class DisjointSetUnion {
private:
    std::vector<int> parent;
    std::vector<int> rank; // Used for union by rank optimization
    int num_sets;

public:
    DisjointSetUnion(int n) : num_sets(n) {
        parent.resize(n);
        std::iota(parent.begin(), parent.end(), 0); // Each element is initially its own parent
        rank.assign(n, 0); // Initialize ranks to 0
    }

    int find(int i) {
        // Path compression
        if (parent[i] == i) {
            return i;
        }
        return parent[i] = find(parent[i]);
    }

    bool unite(int i, int j) { // Using 'unite' to avoid conflict with 'union' keyword
        // Union by rank
        int i_root = find(i);
        int j_root = find(j);

        if (i_root != j_root) {
            if (rank[i_root] < rank[j_root]) {
                parent[i_root] = j_root;
            } else if (rank[i_root] > rank[j_root]) {
                parent[j_root] = i_root;
            } else {
                parent[j_root] = i_root;
                rank[i_root]++;
            }
            num_sets--;
            return true; // Successfully merged
        }
        return false; // Already in the same set
    }

    int getNumSets() const {
        return num_sets;
    }
};

// Example Usage:
// int main() {
//     DisjointSetUnion dsu(5); // Elements 0, 1, 2, 3, 4

//     dsu.unite(0, 1); // Merge set of 0 and set of 1
//     dsu.unite(2, 3); // Merge set of 2 and set of 3
//     dsu.unite(0, 2); // Merge set containing {0,1} and set containing {2,3}

//     std::cout << "Find(3): " << dsu.find(3) << std::endl; // Expected: 0
//     std::cout << "Find(4): " << dsu.find(4) << std::endl; // Expected: 4
//     std::cout << "Are 1 and 3 connected? " << (dsu.find(1) == dsu.find(3) ? "True" : "False") << std::endl; // True
//     std::cout << "Are 1 and 4 connected? " << (dsu.find(1) == dsu.find(4) ? "True" : "False") << std::endl; // False
//     std::cout << "Number of sets: " << dsu.getNumSets() << std::endl; // Expected: 2
//     return 0;
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

A `Disjoint Set Union` implementation primarily consists of the `parent array` and optimized `Find` and `Union` operations.

---

**`DisjointSetUnion` Class:**
- `parent`: An `array` where `parent[i]` stores the `parent` of `element i`. If `parent[i] == i`, then `i` is the `root` of its `set`.
- `rank` (or `size`): An `array` used for the `union by rank` (or `size`) optimization. It stores the `rank` (or `size`) of the `tree` rooted at each `element`.
- `num_sets`: Keeps track of the total number of disjoint sets.
- **`find(i)`:**
- If `element i` is its own `parent`, it is the `root`, so return `i`.
- Otherwise, recursively call `find` on its `parent`, and during the return path, update `parent[i]` to point directly to the `root` (`path compression`).

    </li>
- **`union(i, j)` (or `unite` in C++):**
- Find the `roots` of `element i` and `element j` using the `find` operation.
- If the `roots` are different, merge the two `sets`. This is done by making the `root` of the `tree` with smaller `rank` (or `size`) a child of the `root` of the `tree` with larger `rank` (or `size`). If `ranks` are equal, one `root` becomes the `parent` of the other, and its `rank` is incremented.
- Decrement `num_sets`.

    </li>

[Back to Implementation](#implementation)

## Applications

### Application

The Disjoint Set Union (DSU) data structure is fundamental in graph theory and computational geometry. Its most classic application is in **Kruskal's algorithm** for finding a Minimum Spanning Tree (MST), where it's used to keep track of the sets of vertices connected by the edges selected so far. It is also used for efficiently **detecting cycles in an undirected graph**. In computer networks, it can be used to determine if two computers are on the same network. In image processing, it can be used for image segmentation by grouping neighboring pixels with similar properties into disjoint sets.

