---
title: "Boruvka"
---

`Boruvka's Algorithm` is a greedy algorithm for finding a `minimum spanning tree (MST)` in a connected, undirected, weighted graph. Like `Prim's` and `Kruskal's`, it identifies a subset of `edges` that forms a tree connecting all the `vertices`, with the minimum possible total `edge weight` and no `cycles`.

What makes Boruvka's distinct is its approach: it starts with each `vertex` as its own component and in each phase, it finds the cheapest `edge` for **each component** that connects it to a different component. All these cheapest `edges` are added to the `MST`, merging components. This process effectively reduces the number of components in each phase.

## How it Works

### How it Works (Expanded)

`Boruvka's Algorithm` proceeds in phases. In each phase, every connected component identifies its cheapest outgoing `edge`. All such cheapest `edges` are then added to the `MST`, merging components. This is repeated until only one component remains.

It typically uses a `Disjoint Set Union (DSU)` data structure to keep track of connected components and efficiently detect cycles when adding edges.

---

Example: Graph with 4 nodes (0, 1, 2, 3)
Edges: (0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)

Initial state: Components = {0},{1},{2},{3}. MST = {}.

Phase 1:
- For {0}: cheapest edge is (0,3,5). Mark it.
- For {1}: cheapest edge is (0,1,10). Mark it.
- For {2}: cheapest edge is (0,2,6) or (2,3,4). (2,3,4) is cheaper. Mark it.
- For {3}: cheapest edge is (2,3,4). Mark it.

Add marked edges to MST, unless they connect components already merged by another marked edge.
- Add (0,3,5). Union(0,3). Components: {0,3},{1},{2}. MST: {(0,3,5)}.
- Add (2,3,4). (2,3) connects new {2} to {0,3}. Union(2,3). Components: {0,2,3},{1}. MST: {(0,3,5), (2,3,4)}.
- Add (0,1,10). (0,1) connects {0,2,3} to {1}. Union(0,1). Components: {0,1,2,3}. MST: {(0,3,5), (2,3,4), (0,1,10)}.

All nodes in one component. MST found. Total weight = 5+4+10=19.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
# DSU (Disjoint Set Union) helper class
class DSU:
    def __init__(self, n_nodes):
        self.parent = list(range(n_nodes))
        self.rank = [0] <em> n_nodes
        self.num_components = n_nodes

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            self.num_components -= 1
            return True
        return False

import math

def boruvka_algorithm(num_vertices, edges):
    """
    Finds the Minimum Spanning Tree (MST) using Boruvka's algorithm.
    <code>num_vertices</code>: total number of vertices (0 to num_vertices-1)
    <code>edges</code>: list of (u, v, weight) tuples
    """
    
    dsu = DSU(num_vertices)
    mst_edges = []
    min_cost = 0

    # Sort edges for easier processing within phases (optional, not strictly necessary for correctness, but helps)
    # This sorting is not part of the O(E log V) complexity, as it's done repeatedly or per-component.
    # For a clean conceptual approach, simply iterating all edges per phase is clearer.
    
    while dsu.num_components > 1:
        cheapest_edge_for_component = [None] </em> num_vertices
        
        # Find the cheapest outgoing edge for each component
        for u, v, weight in edges:
            root_u = dsu.find(u)
            root_v = dsu.find(v)

            if root_u != root_v: # If u and v are in different components
                # Check for root_u's component
                if cheapest_edge_for_component[root_u] is None or \
                   weight < cheapest_edge_for_component[root_u][2]:
                    cheapest_edge_for_component[root_u] = (u, v, weight)
                
                # Check for root_v's component
                if cheapest_edge_for_component[root_v] is None or \
                   weight < cheapest_edge_for_component[root_v][2]:
                    cheapest_edge_for_component[root_v] = (u, v, weight)
        
        # Add all selected cheapest edges to MST and unite components
        edges_added_in_phase = 0
        for i in range(num_vertices):
            if cheapest_edge_for_component[i] is not None:
                u, v, weight = cheapest_edge_for_component[i]
                
                # Re-check if u and v are still in different components
                # This is important as other components might have merged in this phase
                if dsu.find(u) != dsu.find(v):
                    if dsu.union(u, v):
                        mst_edges.append((u, v, weight))
                        min_cost += weight
                        edges_added_in_phase += 1
        
        # If no edges were added in a phase, but multiple components remain,
        # the graph is disconnected.
        if edges_added_in_phase == 0 and dsu.num_components > 1:
            return "Graph is not connected, MST not possible"

    return mst_edges, min_cost

# Example
# num_vertices = 4 (0, 1, 2, 3)
# edges = [
#     (0, 1, 10), (0, 2, 6), (0, 3, 5),
#     (1, 3, 15),
#     (2, 3, 4)
# ]
# # Expected MST edges (order might vary):
# # [(0, 3, 5), (2, 3, 4), (0, 1, 10)] Total cost: 19
# mst, cost = boruvka_algorithm(num_vertices, edges)
# print("MST Edges:", mst)
# print("Minimum Cost:", cost)
```

### Javascript

```javascript
// DSU (Disjoint Set Union) helper class
class DSU {
    constructor(nNodes) {
        this.parent = Array.from({ length: nNodes }, (_, i) => i);
        this.rank = new Array(nNodes).fill(0);
        this.numComponents = nNodes;
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
            if (this.rank[rootI] < this.rank[rootJ]) {
                this.parent[rootI] = rootJ;
            } else if (this.rank[rootI] > this.rank[rootJ]) {
                this.parent[rootJ] = rootI;
            } else {
                this.parent[rootJ] = rootI;
                this.rank[rootI]++;
            }
            this.numComponents--;
            return true;
        }
        return false;
    }
}

function boruvkaAlgorithm(numVertices, edges) {
    const dsu = new DSU(numVertices);
    const mstEdges = [];
    let minCost = 0;

    while (dsu.numComponents > 1) {
        // cheapestEdgeForComponent stores [u, v, weight]
        // Initialize with null or a sentinel value indicating no edge found yet
        const cheapestEdgeForComponent = new Array(numVertices).fill(null);
        
        // Find the cheapest outgoing edge for each component
        for (const [u, v, weight] of edges) {
            const rootU = dsu.find(u);
            const rootV = dsu.find(v);

            if (rootU !== rootV) { // If u and v are in different components
                // Check for rootU's component
                if (cheapestEdgeForComponent[rootU] === null || 
                    weight < cheapestEdgeForComponent[rootU][2]) {
                    cheapestEdgeForComponent[rootU] = [u, v, weight];
                }
                
                // Check for rootV's component (important as edge might be cheaper for this side too)
                if (cheapestEdgeForComponent[rootV] === null || 
                    weight < cheapestEdgeForComponent[rootV][2]) {
                    cheapestEdgeForComponent[rootV] = [u, v, weight];
                }
            }
        }
        
        let edgesAddedInPhase = 0;
        for (let i = 0; i < numVertices; i++) {
            const edge = cheapestEdgeForComponent[i];
            if (edge !== null) {
                const [u, v, weight] = edge;
                
                // Re-check if u and v are still in different components
                // This is important as other components might have merged in this phase
                if (dsu.find(u) !== dsu.find(v)) {
                    if (dsu.union(u, v)) {
                        mstEdges.push([u, v, weight]);
                        minCost += weight;
                        edgesAddedInPhase++;
                    }
                }
            }
        }
        
        // If no edges were added in a phase, but multiple components remain,
        // the graph is disconnected.
        if (edgesAddedInPhase === 0 && dsu.numComponents > 1) {
            return "Graph is not connected, MST not possible";
        }
    }

    return { mstEdges, minCost };
}

// const numVertices = 4; // for 0, 1, 2, 3
// const edges = [
//     [0, 1, 10], [0, 2, 6], [0, 3, 5],
//     [1, 3, 15],
//     [2, 3, 4]
// ];
// const { mstEdges, minCost } = boruvkaAlgorithm(numVertices, edges);
// console.log("MST Edges:", mstEdges);
// console.log("Minimum Cost:", minCost); // Expected: 19
```

### Typescript

```typescript
// DSU (Disjoint Set Union) helper class
class DSU {
    public parent: number[];
    public rank: number[];
    public numComponents: number;

    constructor(nNodes: number) {
        this.parent = Array.from({ length: nNodes }, (_, i) => i);
        this.rank = new Array(nNodes).fill(0);
        this.numComponents = nNodes;
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
            if (this.rank[rootI] < this.rank[rootJ]) {
                this.parent[rootI] = rootJ;
            } else if (this.rank[rootI] > this.rank[rootJ]) {
                this.parent[rootJ] = rootI;
            } else {
                this.parent[rootJ] = rootI;
                this.rank[rootI]++;
            }
            this.numComponents--;
            return true;
        }
        return false;
    }
}

type BoruvkaEdge = [number, number, number]; // [u, v, weight]

function boruvkaAlgorithmTS(numVertices: number, edges: BoruvkaEdge[]): { mstEdges: BoruvkaEdge[]; minCost: number } | string {
    const dsu = new DSU(numVertices);
    const mstEdges: BoruvkaEdge[] = [];
    let minCost = 0;

    while (dsu.numComponents > 1) {
        const cheapestEdgeForComponent: (BoruvkaEdge | null)[] = new Array(numVertices).fill(null);
        
        // Find the cheapest outgoing edge for each component
        for (const [u, v, weight] of edges) {
            const rootU = dsu.find(u);
            const rootV = dsu.find(v);

            if (rootU !== rootV) { // If u and v are in different components
                // Check for rootU's component
                if (cheapestEdgeForComponent[rootU] === null || 
                    weight < cheapestEdgeForComponent[rootU]![2]) {
                    cheapestEdgeForComponent[rootU] = [u, v, weight];
                }
                
                // Check for rootV's component
                if (cheapestEdgeForComponent[rootV] === null || 
                    weight < cheapestEdgeForComponent[rootV]![2]) {
                    cheapestEdgeForComponent[rootV] = [u, v, weight];
                }
            }
        }
        
        let edgesAddedInPhase = 0;
        for (let i = 0; i < numVertices; i++) {
            const edge = cheapestEdgeForComponent[i];
            if (edge !== null) {
                const [u, v, weight] = edge;
                
                // Re-check if u and v are still in different components
                if (dsu.find(u) !== dsu.find(v)) {
                    if (dsu.union(u, v)) {
                        mstEdges.push([u, v, weight]);
                        minCost += weight;
                        edgesAddedInPhase++;
                    }
                }
            }
        }
        
        if (edgesAddedInPhase === 0 && dsu.numComponents > 1) {
            return "Graph is not connected, MST not possible";
        }
    }

    return { mstEdges, minCost };
}

// const numVerticesTS = 4;
// const edgesTS: BoruvkaEdge[] = [
//     [0, 1, 10], [0, 2, 6], [0, 3, 5],
//     [1, 3, 15],
//     [2, 3, 4]
// ];
// const resultTS = boruvkaAlgorithmTS(numVerticesTS, edgesTS);
// if (typeof resultTS !== 'string') {
//     console.log("MST Edges:", resultTS.mstEdges);
//     console.log("Minimum Cost:", resultTS.minCost); // Expected: 19
// } else {
//     console.log(resultTS);
// }
```

### Cpp

```cpp
#include <vector>
#include <iostream>
#include <algorithm> // For std::min
#include <limits>    // For std::numeric_limits

// Edge structure
struct BoruvkaEdge {
    int u, v, weight;
};

// DSU (Disjoint Set Union) helper class
class DSU {
public:
    std::vector<int> parent;
    std::vector<int> rank;
    int num_components;

    DSU(int n_nodes) {
        parent.resize(n_nodes);
        for (int i = 0; i < n_nodes; ++i) {
            parent[i] = i;
        }
        rank.assign(n_nodes, 0);
        num_components = n_nodes;
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
            num_components--;
            return true;
        }
        return false;
    }
};

std::pair<std::vector<BoruvkaEdge>, int> boruvkaAlgorithm(int num_vertices, const std::vector<BoruvkaEdge>& edges) {
    DSU dsu(num_vertices);
    std::vector<BoruvkaEdge> mst_edges;
    int min_cost = 0;

    while (dsu.num_components > 1) {
        // cheapestEdgeForComponent stores {u, v, weight}
        std::vector<BoruvkaEdge<em>> cheapest_edge_for_component(num_vertices, nullptr);
        
        // Find the cheapest outgoing edge for each component
        for (const auto& edge : edges) {
            int u = edge.u;
            int v = edge.v;
            int weight = edge.weight;

            int root_u = dsu.find(u);
            int root_v = dsu.find(v);

            if (root_u != root_v) { // If u and v are in different components
                // Check for root_u's component
                if (cheapest_edge_for_component[root_u] == nullptr || 
                    weight < cheapest_edge_for_component[root_u]->weight) {
                    cheapest_edge_for_component[root_u] = const_cast<BoruvkaEdge</em>>(&edge); // Use const_cast or copy for real
                }
                
                // Check for root_v's component
                if (cheapest_edge_for_component[root_v] == nullptr || 
                    weight < cheapest_edge_for_component[root_v]->weight) {
                    cheapest_edge_for_component[root_v] = const_cast<BoruvkaEdge<em>>(&edge); // Use const_cast or copy for real
                }
            }
        }
        
        int edges_added_in_phase = 0;
        for (int i = 0; i < num_vertices; i++) {
            BoruvkaEdge</em> edge_ptr = cheapest_edge_for_component[i];
            if (edge_ptr != nullptr) {
                const BoruvkaEdge& edge = <em>edge_ptr; // Dereference pointer
                
                // Re-check if u and v are still in different components
                if (dsu.find(edge.u) != dsu.find(edge.v)) {
                    if (dsu.unite(edge.u, edge.v)) {
                        mst_edges.push_back(edge);
                        min_cost += edge.weight;
                        edges_added_in_phase++;
                    }
                }
            }
        }
        
        if (edges_added_in_phase == 0 && dsu.num_components > 1) {
            // Graph is disconnected or no progress was made.
            return {{}, -1}; // Indicate error
        }
    }

    return {mst_edges, min_cost};
}

// int main() {
//     int num_vertices = 4;
//     std::vector<BoruvkaEdge> edges = {
//         {0, 1, 10}, {0, 2, 6}, {0, 3, 5},
//         {1, 3, 15},
//         {2, 3, 4}
//     };
//     auto result = boruvkaAlgorithm(num_vertices, edges);
//     if (result.second == -1) {
//         std::cout << "Graph is not connected, MST not possible" << std::endl;
//     } else {
//         std::cout << "Minimum Cost: " << result.second << std::endl; // 19
//         for(const auto& edge : result.first) {
//             std::cout << edge.u << "-" << edge.v << " (" << edge.weight << ")" << std::endl;
//         }
//     }
//     return 0;
// }
```

### D

```d
import std.stdio;
import std.array;
import std.algorithm; // For std.algorithm.min
import std.range; // For std.range.iota

// DSU (Disjoint Set Union) helper class
class DSU {
    int[] parent;
    int[] rank;
    int numComponents;

    this(int nNodes) {
        parent = iota(0, nNodes).array;
        rank = new int[nNodes].replicate(0).array;
        numComponents = nNodes;
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
            if (rank[rootI] < rank[rootJ]) {
                parent[rootI] = rootJ;
            } else if (rank[rootI] > rank[rootJ]) {
                parent[rootJ] = rootI;
            } else {
                parent[rootJ] = rootI;
                rank[rootI]++;
            }
            numComponents--;
            return true;
        }
        return false;
    }
}

// Edge structure
struct BoruvkaEdge {
    int u, v, weight;
}

Tuple!(BoruvkaEdge[], int, string) boruvkaAlgorithm(int numVertices, BoruvkaEdge[] edges) {
    auto dsu = new DSU(numVertices);
    BoruvkaEdge[] mstEdges;
    int minCost = 0;

    while (dsu.numComponents > 1) {
        // cheapestEdgeForComponent stores a pointer to the cheapest edge
        // for each component. Null if no edge found yet.
        BoruvkaEdge</em>[numVertices] cheapestEdgeForComponent; // Array of pointers to edges
        
        // Initialize with nullptrs
        foreach (ref ptr; cheapestEdgeForComponent) {
            ptr = null;
        }

        // Find the cheapest outgoing edge for each component
        foreach (edge; edges) {
            int u = edge.u;
            int v = edge.v;
            int weight = edge.weight;

            int rootU = dsu.find(u);
            int rootV = dsu.find(v);

            if (rootU != rootV) { // If u and v are in different components
                // Check for rootU's component
                if (cheapestEdgeForComponent[rootU] is null || 
                    weight < cheapestEdgeForComponent[rootU].weight) {
                    cheapestEdgeForComponent[rootU] = &edge;
                }
                
                // Check for rootV's component
                if (cheapestEdgeForComponent[rootV] is null || 
                    weight < cheapestEdgeForComponent[rootV].weight) {
                    cheapestEdgeForComponent[rootV] = &edge;
                }
            }
        }
        
        int edgesAddedInPhase = 0;
        foreach (i; 0 .. numVertices) {
            auto edgePtr = cheapestEdgeForComponent[i];
            if (edgePtr !is null) {
                // Dereference the pointer to get the actual edge struct
                BoruvkaEdge edge = <em>edgePtr; 
                
                // Re-check if u and v are still in different components
                if (dsu.find(edge.u) != dsu.find(edge.v)) {
                    if (dsu.unionSets(edge.u, edge.v)) {
                        mstEdges ~= edge;
                        minCost += edge.weight;
                        edgesAddedInPhase++;
                    }
                }
            }
        }
        
        if (edgesAddedInPhase == 0 && dsu.numComponents > 1) {
            return typeof(return)(null, 0, "Graph is not connected, MST not possible");
        }
    }

    return typeof(return)(mstEdges, minCost, "");
}

// void main() {
//     int numVertices = 4;
//     BoruvkaEdge[] edges = [
//         BoruvkaEdge(0, 1, 10), BoruvkaEdge(0, 2, 6), BoruvkaEdge(0, 3, 5),
//         BoruvkaEdge(1, 3, 15),
//         BoruvkaEdge(2, 3, 4)
//     ];
//     auto result = boruvkaAlgorithm(numVertices, edges);
//     if (result.error.length > 0) {
//         writeln(result.error);
//     } else {
//         writeln("Minimum Cost: ", result.minCost); // 19
//         foreach (edge; result.mstEdges) {
//             writefln("%s-%s (%s)", edge.u, edge.v, edge.weight);
//         }
//     }
// }
```

### Go

```go
package main

import (
    "fmt"
)

// DSU (Disjoint Set Union) helper struct
type DSU struct {
    parent []int
    rank   []int
    numComponents int
}

func NewDSU(nNodes int) </em>DSU {
    parent := make([]int, nNodes)
    for i := range parent {
        parent[i] = i
    }
    return &DSU{
        parent: parent,
        rank:   make([]int, nNodes),
        numComponents: nNodes,
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
        if d.rank[rootI] < d.rank[rootJ] {
            d.parent[rootI] = rootJ
        } else if d.rank[rootI] > d.rank[rootJ] {
            d.parent[rootJ] = rootI
        } else {
            d.parent[rootJ] = rootI
            d.rank[rootI]++
        }
        d.numComponents--
        return true
    }
    return false
}

// Edge structure
type BoruvkaEdge struct {
    U, V   int
    Weight int
}

func boruvkaAlgorithm(numVertices int, edges []BoruvkaEdge) ([]BoruvkaEdge, int, error) {
    dsu := NewDSU(numVertices)
    mstEdges := []BoruvkaEdge{}
    minCost := 0

    for dsu.numComponents > 1 {
        // cheapestEdgeForComponent stores a pointer to the cheapest edge
        // for each component. Using pointers to avoid copying large edge structs.
        cheapestEdgeForComponent := make([]<em>BoruvkaEdge, numVertices)
        
        // Find the cheapest outgoing edge for each component
        for i := range edges {
            edge := &edges[i] // Get a pointer to the edge
            u, v, weight := edge.U, edge.V, edge.Weight

            rootU := dsu.Find(u)
            rootV := dsu.Find(v)

            if rootU != rootV { // If u and v are in different components
                // Check for rootU's component
                if cheapestEdgeForComponent[rootU] == nil || 
                    weight < cheapestEdgeForComponent[rootU].Weight {
                    cheapestEdgeForComponent[rootU] = edge
                }
                
                // Check for rootV's component
                if cheapestEdgeForComponent[rootV] == nil || 
                    weight < cheapestEdgeForComponent[rootV].Weight {
                    cheapestEdgeForComponent[rootV] = edge
                }
            }
        }
        
        edgesAddedInPhase := 0
        for i := 0; i < numVertices; i++ {
            edgePtr := cheapestEdgeForComponent[i]
            if edgePtr != nil {
                edge := </em>edgePtr // Dereference the pointer
                u, v, weight := edge.U, edge.V, edge.Weight
                
                // Re-check if u and v are still in different components
                if dsu.Find(u) != dsu.Find(v) {
                    if dsu.Union(u, v) {
                        mstEdges = append(mstEdges, edge)
                        minCost += weight
                        edgesAddedInPhase++
                    }
                }
            }
        }
        
        if edgesAddedInPhase == 0 && dsu.numComponents > 1 {
            return nil, 0, fmt.Errorf("graph is not connected, MST not possible")
        }
    }

    return mstEdges, minCost, nil
}

// func main() {
//     numVertices := 4
//     edges := []BoruvkaEdge{
//         {0, 1, 10}, {0, 2, 6}, {0, 3, 5},
//         {1, 3, 15},
//         {2, 3, 4},
//     }
//     mst, cost, err := boruvkaAlgorithm(numVertices, edges)
//     if err != nil {
//         fmt.Println(err)
//     } else {
//         fmt.Println("Minimum Cost:", cost) // 19
//         for _, edge := range mst {
//             fmt.Printf("%d-%d (%d)\n", edge.U, edge.V, edge.Weight)
//         }
//     }
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

`Boruvka's Algorithm` uses a phased approach, continually merging connected components by adding their cheapest outgoing edges. The `DSU` data structure is crucial for managing components.

---

**`DSU` Class (Helper):** (Same as for Kruskal's, with `num_components` tracker)
- `num_components`: Keeps track of how many distinct connected components currently exist. This is decremented during a successful `union` operation.

**`boruvka_algorithm(num_vertices, edges)` Function:**
- `num_vertices`: Total number of `vertices`.
- `edges`: List of `(u, v, weight)` tuples representing all edges in the graph.

**Algorithm Steps:**
- **Initialization:**
- A `DSU` object is created, with each `vertex` in its own component. `num_components` is set to `num_vertices`.
- `mst_edges`: An empty list to store the edges of the `MST`.
- `min_cost`: Total cost of the `MST`.

    </li>
- **Phases (while `dsu.num_components > 1`):**
- `cheapest_edge_for_component`: An array/list, initialized to `None`/`null` for each `vertex`, to store the cheapest outgoing `edge` found so far for the component represented by that `vertex`'s root.
- **Identify Cheapest Edges:** Iterate through all `edges` in the graph:
- For each `edge (u, v, weight)`:
- Find the `roots` of `u` and `v` using `dsu.find()`.
- If `root_u != root_v` (meaning `u` and `v` are in different components), compare `weight` with the current `cheapest_edge_for_component[root_u]` and `cheapest_edge_for_component[root_v]`. Update if a cheaper `edge` is found.

                    </li>

            </li>
- **Add Edges and Unite Components:** Iterate through `cheapest_edge_for_component`:
- If an `edge` was identified for component `i`:
- Re-check `dsu.find(u) != dsu.find(v)` (important because other components might have merged in this phase due to other `cheapest_edges`).
- If they are still in different components, add the `edge` to `mst_edges`, update `min_cost`, and perform `dsu.union(u, v)`.

                    </li>

            </li>
- **Disconnectivity Check:** If `edges_added_in_phase` is 0 but `dsu.num_components > 1`, the graph is disconnected.

    </li>

[Back to Implementation](#implementation)

## Applications

### Application

`Boruvka's Algorithm` is often less taught than `Prim's` or `Kruskal's`, but it holds significant theoretical and practical importance, especially in parallel computing contexts:
- **Parallel MST Algorithms:** Its core property of selecting the cheapest edge for each component simultaneously makes it highly amenable to parallelization. This is its most significant advantage in very large graphs.
- **Distributed Systems:** Finding MSTs in distributed graph environments where different parts of the graph are stored on different machines.
- **Initial Phase for Other MST Algorithms:** Sometimes used as an initial phase to reduce the number of components and vertices in a graph before applying `Prim's` or `Kruskal's` algorithm (e.g., in a hybrid MST algorithm).
- **Specialized Graph Problems:** In certain graph problems where reducing the number of connected components rapidly is beneficial.
- **Network Design:** Similar to other MST algorithms, for designing cost-effective networks where connections are built in parallel.

