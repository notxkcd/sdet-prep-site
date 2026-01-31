---
title: "Bellman Ford"
---

The `Bellman-Ford Algorithm` is a versatile algorithm used to find the shortest paths from a single source `node` to all other `nodes` in a weighted graph. Unlike `Dijkstra's Algorithm`, `Bellman-Ford` can handle graphs with negative edge weights. However, it can also detect the presence of negative cycles (a cycle where the sum of its edge weights is negative), which would imply that there is no shortest path.

Its ability to handle negative weights makes it a valuable tool in scenarios where edge costs can represent penalties or benefits, and the shortest path might involve traversing such negative-weight edges.

## How it Works

### How it Works (Expanded)

`Bellman-Ford` works on the principle of **relaxation**. It iteratively relaxes all `edges` in the graph `V-1` times (where `V` is the number of `nodes`). Each relaxation step potentially updates the shortest distance to a `node` if a shorter path is found. After `V-1` iterations, if a graph contains no negative cycles, all shortest paths should have been found.

---

Example: Finding shortest paths from Source A in a graph with negative weights
Graph (Edges: u,v,w): (A,B,-1), (A,C,4), (B,C,3), (B,D,2), (B,E,2), (D,B,1), (D,C,5), (E,D,-3)

1. Initialize distances: {A:0, B:inf, C:inf, D:inf, E:inf}.
2. Repeat V-1 (5-1=4) times:
- For each edge (u,v,w):
- If dist[u] + w < dist[v]: dist[v] = dist[u] + w

   After 1st pass: A:0, B:-1, C:4, D:inf, E:inf
   After 2nd pass: A:0, B:-1, C:2, D:1, E:1
   After 3rd pass: A:0, B:-1, C:2, D:-2, E:1
   After 4th pass: A:0, B:-1, C:2, D:-2, E:-1

3. Final check for negative cycles: Repeat one more time (Vth pass).
- If any dist[v] is updated, a negative cycle exists.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
import math

def bellman_ford(num_vertices, edges, start_node):
    """
    Finds the shortest paths from a single start_node in a weighted graph.
    Can handle negative edge weights and detect negative cycles.
    <code>num_vertices</code>: total number of vertices (0 to num_vertices-1)
    <code>edges</code>: list of (u, v, weight) tuples
    <code>start_node</code>: the source node
    """
    
    # Initialize distances: all to infinity, start_node to 0
    distances = {i: math.inf for i in range(num_vertices)}
    distances[start_node] = 0

    # Relax all edges num_vertices - 1 times
    for _ in range(num_vertices - 1):
        for u, v, weight in edges:
            if distances[u] != math.inf and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
    
    # Check for negative cycles
    for u, v, weight in edges:
        if distances[u] != math.inf and distances[u] + weight < distances[v]:
            return "Graph contains a negative cycle accessible from start_node"

    return distances

# Example Graph (from Wikipedia, for 0 to 4 nodes)
# Edges: (u, v, weight)
# num_vertices = 5
# edges = [
#     (0, 1, -1), (0, 2, 4),
#     (1, 2, 3), (1, 3, 2), (1, 4, 2),
#     (3, 2, 5), (3, 1, 1),
#     (4, 3, -3)
# ]
# start_node = 0
# # Expected output: {0: 0, 1: -1, 2: 2, 3: -2, 4: 1}
# print(bellman_ford(num_vertices, edges, start_node))

# Example with negative cycle
# edges_neg_cycle = [
#     (0, 1, 1), (1, 2, -1), (2, 0, -1)
# ]
# print(bellman_ford(3, edges_neg_cycle, 0)) # Graph contains a negative cycle...
```

### Javascript

```javascript
function bellmanFord(numVertices, edges, startNode) {
    // Initialize distances: all to infinity, startNode to 0
    const distances = {};
    for (let i = 0; i < numVertices; i++) {
        distances[i] = Infinity;
    }
    distances[startNode] = 0;

    // Relax all edges numVertices - 1 times
    for (let i = 0; i < numVertices - 1; i++) {
        for (const [u, v, weight] of edges) {
            if (distances[u] !== Infinity && distances[u] + weight < distances[v]) {
                distances[v] = distances[u] + weight;
            }
        }
    }
    
    // Check for negative cycles
    for (const [u, v, weight] of edges) {
        if (distances[u] !== Infinity && distances[u] + weight < distances[v]) {
            return "Graph contains a negative cycle accessible from start_node";
        }
    }

    return distances;
}

// const numVertices = 5;
// const edges = [
//     [0, 1, -1], [0, 2, 4],
//     [1, 2, 3], [1, 3, 2], [1, 4, 2],
//     [3, 2, 5], [3, 1, 1],
//     [4, 3, -3]
// ];
// const startNode = 0;
// console.log(bellmanFord(numVertices, edges, startNode)); // { '0': 0, '1': -1, '2': 2, '3': -2, '4': 1 }
```

### Typescript

```typescript
type Edge = [number, number, number]; // [u, v, weight]

function bellmanFordTS(numVertices: number, edges: Edge[], startNode: number): Record<number, number> | string {
    // Initialize distances: all to infinity, startNode to 0
    const distances: Record<number, number> = {};
    for (let i = 0; i < numVertices; i++) {
        distances[i] = Infinity;
    }
    distances[startNode] = 0;

    // Relax all edges numVertices - 1 times
    for (let i = 0; i < numVertices - 1; i++) {
        for (const [u, v, weight] of edges) {
            if (distances[u] !== Infinity && distances[u] + weight < distances[v]) {
                distances[v] = distances[u] + weight;
            }
        }
    }
    
    // Check for negative cycles
    for (const [u, v, weight] of edges) {
        if (distances[u] !== Infinity && distances[u] + weight < distances[v]) {
            return "Graph contains a negative cycle accessible from start_node";
        }
    }

    return distances;
}

// const numVerticesTS = 5;
// const edgesTS: Edge[] = [
//     [0, 1, -1], [0, 2, 4],
//     [1, 2, 3], [1, 3, 2], [1, 4, 2],
//     [3, 2, 5], [3, 1, 1],
//     [4, 3, -3]
// ];
// const startNodeTS = 0;
// console.log(bellmanFordTS(numVerticesTS, edgesTS, startNodeTS)); // { '0': 0, '1': -1, '2': 2, '3': -2, '4': 1 }
```

### Cpp

```cpp
#include <vector>
#include <iostream>
#include <limits> // For std::numeric_limits
#include <map>    // For mapping node indices to chars if needed, or just use 0..N-1

struct Edge {
    int u, v, weight;
};

std::map<int, int> bellmanFord(int num_vertices, const std::vector<Edge>& edges, int start_node) {
    // Initialize distances: all to infinity, start_node to 0
    std::map<int, int> distances;
    for (int i = 0; i < num_vertices; ++i) {
        distances[i] = std::numeric_limits<int>::max();
    }
    distances[start_node] = 0;

    // Relax all edges num_vertices - 1 times
    for (int i = 0; i < num_vertices - 1; ++i) {
        for (const auto& edge : edges) {
            if (distances[edge.u] != std::numeric_limits<int>::max() &&
                distances[edge.u] + edge.weight < distances[edge.v]) {
                distances[edge.v] = distances[edge.u] + edge.weight;
            }
        }
    }
    
    // Check for negative cycles
    for (const auto& edge : edges) {
        if (distances[edge.u] != std::numeric_limits<int>::max() &&
            distances[edge.u] + edge.weight < distances[edge.v]) {
            // A negative cycle is detected and is reachable from start_node
            // For simplicity, we return an empty map or throw an exception.
            // A more robust implementation might return a special error code.
            distances.clear(); // Clear distances to indicate error
            distances[-1] = -1; // Special indicator for negative cycle
            return distances;
        }
    }

    return distances;
}

// int main() {
//     int num_vertices = 5;
//     std::vector<Edge> edges = {
//         {0, 1, -1}, {0, 2, 4},
//         {1, 2, 3}, {1, 3, 2}, {1, 4, 2},
//         {3, 2, 5}, {3, 1, 1},
//         {4, 3, -3}
//     };
//     int start_node = 0;
//     std::map<int, int> result = bellmanFord(num_vertices, edges, start_node);
//     if (result.count(-1)) {
//         std::cout << "Graph contains a negative cycle." << std::endl;
//     } else {
//         for (const auto& pair : result) {
//             std::cout << "Distance to node " << pair.first << ": " << pair.second << std::endl;
//         }
//     }
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

type BellmanFordEdge struct {
    U, V   int
    Weight int
}

func bellmanFord(numVertices int, edges []BellmanFordEdge, startNode int) (map[int]int, error) {
    // Initialize distances: all to infinity, startNode to 0
    distances := make(map[int]int)
    for i := 0; i < numVertices; i++ {
        distances[i] = math.MaxInt32
    }
    distances[startNode] = 0

    // Relax all edges numVertices - 1 times
    for i := 0; i < numVertices-1; i++ {
        for _, edge := range edges {
            if distances[edge.U] != math.MaxInt32 && distances[edge.U]+edge.Weight < distances[edge.V] {
                distances[edge.V] = distances[edge.U] + edge.Weight
            }
        }
    }
    
    // Check for negative cycles
    for _, edge := range edges {
        if distances[edge.U] != math.MaxInt32 && distances[edge.U]+edge.Weight < distances[edge.V] {
            return nil, fmt.Errorf("graph contains a negative cycle accessible from start_node")
        }
    }

    return distances, nil
}

// func main() {
//     numVertices := 5
//     edges := []BellmanFordEdge{
//         {0, 1, -1}, {0, 2, 4},
//         {1, 2, 3}, {1, 3, 2}, {1, 4, 2},
//         {3, 2, 5}, {3, 1, 1},
//         {4, 3, -3},
//     }
//     startNode := 0
//     result, err := bellmanFord(numVertices, edges, startNode)
//     if err != nil {
//         fmt.Println(err)
//     } else {
//         fmt.Println("Shortest distances:", result) // map[0:0 1:-1 2:2 3:-2 4:1]
//     }
// }
```

### D

```d
import std.stdio;
import std.array;
import std.algorithm; // For std.algorithm.min
import std.conv; // For to!string

struct BellmanFordEdge {
    int u, v, weight;
}

Tuple!(int[int], string) bellmanFord(int numVertices, BellmanFordEdge[] edges, int startNode) {
    // Initialize distances: all to infinity, startNode to 0
    auto distances = new int[int];
    foreach (i; 0 .. numVertices) {
        distances[i] = int.max;
    }
    distances[startNode] = 0;

    // Relax all edges numVertices - 1 times
    foreach (i; 0 .. numVertices - 1) {
        foreach (edge; edges) {
            if (distances[edge.u] != int.max && distances[edge.u] + edge.weight < distances[edge.v]) {
                distances[edge.v] = distances[edge.u] + edge.weight;
            }
        }
    }
    
    // Check for negative cycles
    foreach (edge; edges) {
        if (distances[edge.u] != int.max && distances[edge.u] + edge.weight < distances[edge.v]) {
            return typeof(return)(null, "Graph contains a negative cycle accessible from start_node");
        }
    }

    return typeof(return)(distances, "");
}

// void main() {
//     int numVertices = 5;
//     BellmanFordEdge[] edges = [
//         BellmanFordEdge(0, 1, -1), BellmanFordEdge(0, 2, 4),
//         BellmanFordEdge(1, 2, 3), BellmanFordEdge(1, 3, 2), BellmanFordEdge(1, 4, 2),
//         BellmanFordEdge(3, 2, 5), BellmanFordEdge(3, 1, 1),
//         BellmanFordEdge(4, 3, -3)
//     ];
//     int startNode = 0;
//     auto result = bellmanFord(numVertices, edges, startNode);
//     if (result.error.length > 0) {
//         writeln(result.error);
//     } else {
//         writeln("Shortest distances: ", result.distances); // [0:0, 1:-1, 2:2, 3:-2, 4:1]
//     }
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

The `Bellman-Ford Algorithm` implements the relaxation principle iteratively to find shortest paths and detect negative cycles.

---

**Initialization:**
- `num_vertices`: The total number of `vertices` in the graph.
- `edges`: A list of `tuples/structs` in the format `(u, v, weight)`.
- `start_node`: The source `vertex` from which to find shortest paths.
- A `distances` map/array is created. `distances[i]` stores the shortest distance from `start_node` to `node i`. Initially, `distances[start_node]` is 0, and all other `distances` are `infinity`.

**Relaxation Phase:**
- This phase consists of `num_vertices - 1` iterations.
- In each iteration, the algorithm iterates through **all** `edges (u, v)` with `weight w` in the graph.
- For each `edge`, it performs a **relaxation** step:
- If the current shortest path to `u` (`distances[u]`) is not `infinity` (meaning `u` is reachable) and `distances[u] + w` (the path through `u` to `v`) is less than the current shortest path to `v` (`distances[v]`):
- `distances[v]` is updated to `distances[u] + w`. This means a shorter path to `v` has been found.

            </li>

    </li>

**Negative Cycle Detection Phase:**
- After `num_vertices - 1` iterations, all shortest paths (if no negative cycles exist) should be finalized.
- A `V`-th (or `num_vertices`-th) iteration is performed over all `edges`.
- If, during this `V`-th iteration, any `distance` `distances[v]` is still updated, it signifies that there is a negative cycle reachable from the `start_node`. This is because a path length would continue to decrease indefinitely due to the negative cycle.

**Result:**
- If no negative cycle is detected, the `distances` map/array contains the shortest paths from `start_node` to all other `vertices`.
- Otherwise, an indication of a negative cycle is returned.

[Back to Implementation](#implementation)

## Applications

### Application

The `Bellman-Ford Algorithm` is crucial in scenarios where negative edge weights are a possibility, and especially for detecting negative cycles.
- **Network Routing Protocols:** Used in protocols like the Distance Vector Routing Protocol (e.g., RIP) to compute shortest paths. The ability to handle negative weights is important, though negative cycles can cause issues if not detected.
- **Arbitrage Detection:** In financial markets, if currencies are nodes and exchange rates are edge weights (transformed logarithmically), a negative cycle indicates an arbitrage opportunity (a sequence of trades that yields a profit without risk).
- **Graph Analysis with Negative Costs:** Any problem where "costs" can represent benefits (negative costs) and you need to find the shortest path, such as optimizing resource usage or minimizing penalties.
- **Distributed Systems:** For certain synchronization and resource allocation problems where negative values might indicate resource availability or gain.

