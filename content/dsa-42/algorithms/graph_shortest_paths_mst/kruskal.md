---
title: "Kruskal"
---

`Kruskal's Algorithm` is a greedy algorithm that finds a `minimum spanning tree (MST)` for a connected, undirected, weighted graph. Similar to `Prim's Algorithm`, an `MST` is a subset of the `edges` that connects all the `vertices` together, without any `cycles` and with the minimum possible total `edge weight`.

Unlike Prim's, which grows the `MST` from a starting `vertex`, Kruskal's algorithm considers `edges` in increasing order of their `weights` and adds them to the `MST` if they do not form a `cycle`. It uses a `Disjoint Set Union (DSU)` data structure to efficiently detect cycles.

## How it Works

### How it Works (Expanded)

`Kruskal's Algorithm` operates on the entire graph at once, focusing on individual `edges`. The crucial part is checking for `cycles`, which is where the `DSU` data structure comes in handy. A `DSU` can tell us if two `vertices` are already connected (i.e., part of the same component) in near-constant time on average.

---

Example: Finding MST using Kruskal's
Graph Edges: (A,B,4), (A,C,2), (B,C,1), (B,D,5), (C,D,8)

1. Sort edges by weight: (B,C,1), (A,C,2), (A,B,4), (B,D,5), (C,D,8)

2. Process sorted edges:
- (B,C,1): B and C not connected. Add to MST. DSU: {A},{B,C},{D}. MST: {(B,C,1)}.
- (A,C,2): A and C not connected. Add to MST. DSU: {A,B,C},{D}. MST: {(B,C,1), (A,C,2)}.
- (A,B,4): A and B ARE connected (in {A,B,C}). Skip (would form a cycle).
- (B,D,5): B and D not connected. Add to MST. DSU: {A,B,C,D}. MST: {(B,C,1), (A,C,2), (B,D,5)}.
- (C,D,8): C and D ARE connected (in {A,B,C,D}). Skip.

All vertices connected. MST formed. Total weight = 1+2+5=8.

## Implementation {#implementation}

### Python

```python
# Disjoint Set Union (DSU) helper class
class DSU:
    def __init__(self, n_nodes):
        self.parent = list(range(n_nodes))
        self.rank = [0] <em> n_nodes # Used for union by rank optimization

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i]) # Path compression
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # Union by rank
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False

def kruskal_algorithm(num_vertices, edges):
    """
    Finds the Minimum Spanning Tree (MST) of a connected, undirected graph
    using Kruskal's algorithm.
    <code>num_vertices</code>: total number of vertices (e.g., 4 for A, B, C, D)
    <code>edges</code>: list of (weight, u, v) tuples
    """
    
    # 1. Sort all edges by their weights
    edges.sort()
    
    dsu = DSU(num_vertices)
    mst_edges = []
    min_cost = 0
    num_edges_in_mst = 0

    # 2. Iterate through sorted edges
    for weight, u, v in edges:
        if dsu.union(u, v): # If adding this edge does not form a cycle
            mst_edges.append((u, v, weight))
            min_cost += weight
            num_edges_in_mst += 1
            
            # Optimization: If MST has V-1 edges, it's complete
            if num_edges_in_mst == num_vertices - 1:
                break
    
    # Check if all vertices were connected
    if num_edges_in_mst != num_vertices - 1:
        return "Graph is not connected, MST not possible"

    return mst_edges, min_cost

# Example
# num_vertices = 4 (for A, B, C, D, mapped to 0, 1, 2, 3)
# edges = [
#     (1, 1, 2), # B-C, weight 1
#     (2, 0, 2), # A-C, weight 2
#     (4, 0, 1), # A-B, weight 4
#     (5, 1, 3), # B-D, weight 5
#     (8, 2, 3)  # C-D, weight 8
# ]
# # Expected MST edges: [(1, 1, 2), (2, 0, 2), (5, 1, 3)] (total weight 8)
# mst, cost = kruskal_algorithm(num_vertices, edges)
# print("MST Edges:", mst)
# print("Minimum Cost:", cost)
```

### Javascript

```javascript
// Disjoint Set Union (DSU) helper class
class DSU {
    constructor(nNodes) {
        this.parent = Array.from({ length: nNodes }, (_, i) => i);
        this.rank = new Array(nNodes).fill(0);
    }

    find(i) {
        if (this.parent[i] === i) {
            return i;
        }
        this.parent[i] = this.find(this.parent[i]); // Path compression
        return this.parent[i];
    }

    union(i, j) {
        const rootI = this.find(i);
        const rootJ = this.find(j);

        if (rootI !== rootJ) {
            // Union by rank
            if (this.rank[rootI] < this.rank[rootJ]) {
                this.parent[rootI] = rootJ;
            } else if (this.rank[rootI] > this.rank[rootJ]) {
                this.parent[rootJ] = rootI;
            } else {
                this.parent[rootJ] = rootI;
                this.rank[rootI]++;
            }
            return true;
        }
        return false;
    }
}

function kruskalAlgorithm(numVertices, edges) {
    // 1. Sort all edges by their weights
    edges.sort((a, b) => a[0] - b[0]); // Edges format: [weight, u, v]
    
    const dsu = new DSU(numVertices);
    const mstEdges = [];
    let minCost = 0;
    let numEdgesInMst = 0;

    // 2. Iterate through sorted edges
    for (const [weight, u, v] of edges) {
        if (dsu.union(u, v)) { // If adding this edge does not form a cycle
            mstEdges.push([u, v, weight]);
            minCost += weight;
            numEdgesInMst++;
            
            // Optimization: If MST has V-1 edges, it's complete
            if (numEdgesInMst === numVertices - 1) {
                break;
            }
        }
    }
    
    // Check if all vertices were connected
    if (numEdgesInMst !== numVertices - 1) {
        return "Graph is not connected, MST not possible";
    }

    return { mstEdges, minCost };
}

// const numVertices = 4; // for A, B, C, D (mapped to 0, 1, 2, 3)
// const edges = [
//     [1, 1, 2], // B-C, weight 1
//     [2, 0, 2], // A-C, weight 2
//     [4, 0, 1], // A-B, weight 4
//     [5, 1, 3], // B-D, weight 5
//     [8, 2, 3]  // C-D, weight 8
// ];
// const { mstEdges, minCost } = kruskalAlgorithm(numVertices, edges);
// console.log("MST Edges:", mstEdges);
// console.log("Minimum Cost:", minCost); // Expected: 8
```

### Typescript

```typescript
// Disjoint Set Union (DSU) helper class
class DSU {
    public parent: number[];
    public rank: number[];

    constructor(nNodes: number) {
        this.parent = Array.from({ length: nNodes }, (_, i) => i);
        this.rank = new Array(nNodes).fill(0);
    }

    find(i: number): number {
        if (this.parent[i] === i) {
            return i;
        }
        this.parent[i] = this.find(this.parent[i]); // Path compression
        return this.parent[i];
    }

    union(i: number, j: number): boolean {
        const rootI = this.find(i);
        const rootJ = this.find(j);

        if (rootI !== rootJ) {
            // Union by rank
            if (this.rank[rootI] < this.rank[rootJ]) {
                this.parent[rootI] = rootJ;
            } else if (this.rank[rootI] > this.rank[rootJ]) {
                this.parent[rootJ] = rootI;
            } else {
                this.parent[rootJ] = rootI;
                this.rank[rootI]++;
            }
            return true;
        }
        return false;
    }
}

type Edge = [number, number, number]; // [weight, u, v]

function kruskalAlgorithmTS(numVertices: number, edges: Edge[]): { mstEdges: Edge[]; minCost: number } | string {
    // 1. Sort all edges by their weights
    edges.sort((a, b) => a[0] - b[0]);
    
    const dsu = new DSU(numVertices);
    const mstEdges: Edge[] = [];
    let minCost = 0;
    let numEdgesInMst = 0;

    // 2. Iterate through sorted edges
    for (const [weight, u, v] of edges) {
        if (dsu.union(u, v)) { // If adding this edge does not form a cycle
            mstEdges.push([u, v, weight]);
            minCost += weight;
            numEdgesInMst++;
            
            // Optimization: If MST has V-1 edges, it's complete
            if (numEdgesInMst === numVertices - 1) {
                break;
            }
        }
    }
    
    // Check if all vertices were connected
    if (numEdgesInMst !== numVertices - 1) {
        return "Graph is not connected, MST not possible";
    }

    return { mstEdges, minCost };
}

// const numVerticesTS = 4; // for A, B, C, D (mapped to 0, 1, 2, 3)
// const edgesTS: Edge[] = [
//     [1, 1, 2], // B-C, weight 1
//     [2, 0, 2], // A-C, weight 2
//     [4, 0, 1], // A-B, weight 4
//     [5, 1, 3], // B-D, weight 5
//     [8, 2, 3]  // C-D, weight 8
// ];
// const resultTS = kruskalAlgorithmTS(numVerticesTS, edgesTS);
// if (typeof resultTS !== 'string') {
//     console.log("MST Edges:", resultTS.mstEdges);
//     console.log("Minimum Cost:", resultTS.minCost); // Expected: 8
// } else {
//     console.log(resultTS);
// }
```

### Cpp

```cpp
#include <vector>
#include <iostream>
#include <algorithm> // For std::sort

// Edge structure
struct Edge {
    int weight;
    int u, v;

    bool operator<(const Edge& other) const {
        return weight < other.weight;
    }
};

// Disjoint Set Union (DSU) helper class
class DSU {
public:
    std::vector<int> parent;
    std::vector<int> rank;

    DSU(int n_nodes) {
        parent.resize(n_nodes);
        for (int i = 0; i < n_nodes; ++i) {
            parent[i] = i;
        }
        rank.assign(n_nodes, 0);
    }

    int find(int i) {
        if (parent[i] == i) {
            return i;
        }
        return parent[i] = find(parent[i]); // Path compression
    }

    bool unite(int i, int j) { // Changed name from union to unite to avoid keyword conflict
        int root_i = find(i);
        int root_j = find(j);

        if (root_i != root_j) {
            // Union by rank
            if (rank[root_i] < rank[root_j]) {
                parent[root_i] = root_j;
            } else if (rank[root_i] > rank[root_j]) {
                parent[root_j] = root_i;
            } else {
                parent[root_j] = root_i;
                rank[root_i]++;
            }
            return true;
        }
        return false;
    }
};

std::pair<std::vector<Edge>, int> kruskalAlgorithm(int num_vertices, std::vector<Edge> edges) {
    // 1. Sort all edges by their weights
    std::sort(edges.begin(), edges.end());
    
    DSU dsu(num_vertices);
    std::vector<Edge> mst_edges;
    int min_cost = 0;
    int num_edges_in_mst = 0;

    // 2. Iterate through sorted edges
    for (const auto& edge : edges) {
        if (dsu.unite(edge.u, edge.v)) { // If adding this edge does not form a cycle
            mst_edges.push_back(edge);
            min_cost += edge.weight;
            num_edges_in_mst++;
            
            // Optimization: If MST has V-1 edges, it's complete
            if (num_edges_in_mst == num_vertices - 1) {
                break;
            }
        }
    }
    
    // Check if all vertices were connected
    if (num_edges_in_mst != num_vertices - 1) {
        // Return an empty MST and 0 cost, or throw an exception
        return {{}, -1}; 
    }

    return {mst_edges, min_cost};
}

// int main() {
//     int num_vertices = 4; // for A, B, C, D (mapped to 0, 1, 2, 3)
//     std::vector<Edge> edges = {
//         {1, 1, 2}, // B-C, weight 1
//         {2, 0, 2}, // A-C, weight 2
//         {4, 0, 1}, // A-B, weight 4
//         {5, 1, 3}, // B-D, weight 5
//         {8, 2, 3}  // C-D, weight 8
//     };
//     auto result = kruskalAlgorithm(num_vertices, edges);
//     std::cout << "Minimum Cost: " << result.second << std::endl; // 8
//     for(const auto& edge : result.first) {
//         std::cout << edge.u << "-" << edge.v << " (" << edge.weight << ")" << std::endl;
//     }
//     return 0;
// }
```

### Go

```go
package main

import "fmt"

// DSU (Disjoint Set Union) helper struct
type DSU struct {
    parent []int
    rank   []int
}

func NewDSU(nNodes int) </em>DSU {
    parent := make([]int, nNodes)
    for i := range parent {
        parent[i] = i
    }
    return &DSU{
        parent: parent,
        rank:   make([]int, nNodes),
    }
}

func (d <em>DSU) Find(i int) int {
    if d.parent[i] == i {
        return i
    }
    d.parent[i] = d.Find(d.parent[i]) // Path compression
    return d.parent[i]
}

func (d </em>DSU) Union(i, j int) bool {
    rootI := d.Find(i)
    rootJ := d.Find(j)

    if rootI != rootJ {
        // Union by rank
        if d.rank[rootI] < d.rank[rootJ] {
            d.parent[rootI] = rootJ
        } else if d.rank[rootI] > d.rank[rootJ] {
            d.parent[rootJ] = rootI
        } else {
            d.parent[rootJ] = rootI
            d.rank[rootI]++
        }
        return true
    }
    return false
}

// Edge structure
type KruskalEdge struct {
    Weight int
    U, V   int
}

// Custom sort for Kruskal's edges
type ByWeight []KruskalEdge

func (a ByWeight) Len() int           { return len(a) }
func (a ByWeight) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a ByWeight) Less(i, j int) bool { return a[i].Weight < a[j].Weight }

func kruskalAlgorithm(numVertices int, edges []KruskalEdge) ([]KruskalEdge, int, error) {
    // 1. Sort all edges by their weights
    sort.Sort(ByWeight(edges))
    
    dsu := NewDSU(numVertices)
    mstEdges := []KruskalEdge{}
    minCost := 0
    numEdgesInMst := 0

    // 2. Iterate through sorted edges
    for _, edge := range edges {
        if dsu.Union(edge.U, edge.V) { // If adding this edge does not form a cycle
            mstEdges = append(mstEdges, edge)
            minCost += edge.Weight
            numEdgesInMst++
            
            // Optimization: If MST has V-1 edges, it's complete
            if numEdgesInMst == numVertices - 1 {
                break
            }
        }
    }
    
    // Check if all vertices were connected
    if numEdgesInMst != numVertices - 1 {
        return nil, 0, fmt.Errorf("Graph is not connected, MST not possible")
    }

    return mstEdges, minCost, nil
}

// func main() {
//     numVertices := 4 // for A, B, C, D (mapped to 0, 1, 2, 3)
//     edges := []KruskalEdge{
//         {Weight: 1, U: 1, V: 2}, // B-C
//         {Weight: 2, U: 0, V: 2}, // A-C
//         {Weight: 4, U: 0, V: 1}, // A-B
//         {Weight: 5, U: 1, V: 3}, // B-D
//         {Weight: 8, U: 2, V: 3}, // C-D
//     }
//     mst, cost, err := kruskalAlgorithm(numVertices, edges)
//     if err != nil {
//         fmt.Println(err)
//     } else {
//         fmt.Println("Minimum Cost:", cost) // 8
//         for _, edge := range mst {
//             fmt.Printf("%d-%d (%d)\n", edge.U, edge.V, edge.Weight)
//         }
//     }
// }
```

### D

```d
import std.stdio;
import std.array;
import std.algorithm; // For std.algorithm.sort
import std.range; // For std.range.iota

// DSU (Disjoint Set Union) helper class
class DSU {
    int[] parent;
    int[] rank;

    this(int nNodes) {
        parent = iota(0, nNodes).array;
        rank = new int[nNodes].replicate(0).array;
    }

    int find(int i) {
        if (parent[i] == i) {
            return i;
        }
        parent[i] = find(parent[i]); // Path compression
        return parent[i];
    }

    bool unionSets(int i, int j) { // Changed name from union to unionSets to avoid keyword conflict
        int rootI = find(i);
        int rootJ = find(j);

        if (rootI != rootJ) {
            // Union by rank
            if (rank[rootI] < rank[rootJ]) {
                parent[rootI] = rootJ;
            } else if (rank[rootI] > rank[rootJ]) {
                parent[rootJ] = rootI;
            } else {
                parent[rootJ] = rootI;
                rank[rootI]++;
            }
            return true;
        }
        return false;
    }
}

// Edge structure
struct KruskalEdge {
    int weight;
    int u, v;

    int opCmp(const KruskalEdge other) const {
        return this.weight.cmp(other.weight);
    }
}

Tuple!(KruskalEdge[], int, string) kruskalAlgorithm(int numVertices, KruskalEdge[] edges) {
    // 1. Sort all edges by their weights
    edges.sort!((a, b) => a.weight < b.weight);
    
    auto dsu = new DSU(numVertices);
    KruskalEdge[] mstEdges;
    int minCost = 0;
    int numEdgesInMst = 0;

    // 2. Iterate through sorted edges
    foreach (edge; edges) {
        if (dsu.unionSets(edge.u, edge.v)) { // If adding this edge does not form a cycle
            mstEdges ~= edge;
            minCost += edge.weight;
            numEdgesInMst++;
            
            // Optimization: If MST has V-1 edges, it's complete
            if (numEdgesInMst == numVertices - 1) {
                break;
            }
        }
    }
    
    // Check if all vertices were connected
    if (numEdgesInMst != numVertices - 1) {
        return typeof(return)(null, 0, "Graph is not connected, MST not possible");
    }

    return typeof(return)(mstEdges, minCost, "");
}

// void main() {
//     int numVertices = 4; // for A, B, C, D (mapped to 0, 1, 2, 3)
//     KruskalEdge[] edges = [
//         KruskalEdge(1, 1, 2), // B-C
//         KruskalEdge(2, 0, 2), // A-C
//         KruskalEdge(4, 0, 1), // A-B
//         KruskalEdge(5, 1, 3), // B-D
//         KruskalEdge(8, 2, 3)  // C-D
//     ];
//     auto result = kruskalAlgorithm(numVertices, edges);
//     if (result.error.length > 0) {
//         writeln(result.error);
//     } else {
//         writeln("Minimum Cost: ", result.minCost); // 8
//         foreach (edge; result.mstEdges) {
//             writefln("%s-%s (%s)", edge.u, edge.v, edge.weight);
//         }
//     }
// }
```

## Applications

### Application

`Kruskal's Algorithm` is widely used for finding Minimum Spanning Trees in various applications, especially when the graph is sparse (has relatively few edges) or when a simple, globally optimal approach is preferred.
- **Network Design:** Laying out telecommunication or power grids with minimum cable/wire length.
- **Clustering:** In machine learning and data analysis, for grouping data points into clusters by building a graph where nodes are data points and edge weights are dissimilarity measures.
- **Circuit Design:** Optimizing connections on printed circuit boards to minimize wire usage.
- **Image Processing:** Image segmentation where pixels are nodes and edge weights represent dissimilarity between adjacent pixels.
- **Approximation Algorithms:** Used as a subroutine in some approximation algorithms for NP-hard problems, such as the Traveling Salesperson Problem.

