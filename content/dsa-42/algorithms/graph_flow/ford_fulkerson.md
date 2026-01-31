---
title: "Ford-Fulkerson Algorithm"
---

The `Ford-Fulkerson Algorithm` is a classic algorithm used to find the maximum flow in a flow network. A `flow network` is a directed graph where each `edge` has a `capacity` and each `edge` receives a `flow`. The goal is to maximize the total `flow` from a designated `source` `node` to a designated `sink` `node`, respecting the `capacity constraints` of each `edge` and `flow conservation` at intermediate `nodes`.

The algorithm uses the concept of "`augmenting paths`" in a "`residual graph`". It repeatedly finds a path from the `source` to the `sink` in the `residual graph` along which more `flow` can be sent, and then increases the `flow` along that path, updating the capacities of the edges.

## How it Works

### How it Works (Expanded)

The `Ford-Fulkerson Algorithm` relies on the **Max-Flow Min-Cut Theorem**, which states that the maximum `flow` through a network is equal to the capacity of the minimum `cut` (a partition of `vertices` into two sets, one containing the `source` and the other containing the `sink`).

---

Key Concepts:

1.  **Flow Network:** A directed graph G = (V, E) where each edge (u, v) ∈ E has a non-negative capacity c(u, v) ≥ 0.
2.  **Flow:** A function f: V × V → R, where f(u, v) represents the flow from u to v.
- Capacity Constraint: f(u, v) ≤ c(u, v)
- Skew Symmetry: f(u, v) = -f(v, u)
- Flow Conservation: For any vertex v ≠ source, sink, Σ f(u, v) = 0
3.  **Residual Graph:** For a given flow f, the residual graph Gf has edges with residual capacities.
- If c(u, v) - f(u, v) > 0, an edge (u, v) exists with residual capacity c(u, v) - f(u, v).
- If f(v, u) > 0, an edge (u, v) exists (backward edge) with residual capacity f(v, u).
4.  **Augmenting Path:** A path from source to sink in the residual graph.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
from collections import deque

def bfs_find_augmenting_path(residual_graph, source, sink, parent):
    """
    Finds an augmenting path from source to sink in the residual graph using BFS.
    Returns True if a path is found, False otherwise.
    Fills the parent array to reconstruct the path.
    """
    n = len(residual_graph)
    visited = [False] <em> n
    queue = deque()

    queue.append(source)
    visited[source] = True
    parent[source] = -1 # Source has no parent

    while queue:
        u = queue.popleft()

        for v in range(n):
            # If v is not visited and there is residual capacity from u to v
            if not visited[v] and residual_graph[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == sink: # Found path to sink
                    return True
    return False

def ford_fulkerson(graph, source, sink):
    """
    Finds the maximum flow from source to sink in a flow network.
    <code>graph</code> is an adjacency matrix representation of the capacities.
    """
    n = len(graph) # Number of vertices
    
    # Initialize residual graph (initially same as original graph capacities)
    residual_graph = [row[:] for row in graph]
    
    # parent array to store path found by BFS
    parent = [-1] </em> n
    
    max_flow = 0

    # While there is an augmenting path from source to sink
    while bfs_find_augmenting_path(residual_graph, source, sink, parent):
        # Find the bottleneck capacity of the path found by BFS
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]
        
        # Add path flow to overall flow
        max_flow += path_flow
        
        # Update residual capacities along the path
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow # Decrease capacity of forward edge
            residual_graph[v][u] += path_flow # Increase capacity of backward edge
            v = parent[v]
            
    return max_flow

# Example: (from CLRS, Figure 26.1)
# 0: source, 5: sink
# graph = [
#     [0, 16, 13, 0, 0, 0],  # 0->1(16), 0->2(13)
#     [0, 0, 10, 12, 0, 0],  # 1->2(10), 1->3(12)
#     [0, 4, 0, 0, 14, 0],   # 2->1(4), 2->4(14)
#     [0, 0, 9, 0, 0, 20],   # 3->2(9), 3->5(20)
#     [0, 0, 0, 7, 0, 4],    # 4->3(7), 4->5(4)
#     [0, 0, 0, 0, 0, 0]     # 5: sink
# ]
# source = 0
# sink = 5
# print(ford_fulkerson(graph, source, sink)) # Expected: 23
```

### Javascript

```javascript
function bfsFindAugmentingPath(residualGraph, source, sink, parent) {
    const n = residualGraph.length;
    const visited = new Array(n).fill(false);
    const queue = [];

    queue.push(source);
    visited[source] = true;
    parent[source] = -1; // Source has no parent

    while (queue.length > 0) {
        const u = queue.shift();

        for (let v = 0; v < n; v++) {
            // If v is not visited and there is residual capacity from u to v
            if (!visited[v] && residualGraph[u][v] > 0) {
                queue.push(v);
                visited[v] = true;
                parent[v] = u;
                if (v === sink) { // Found path to sink
                    return true;
                }
            }
        }
    }
    return false;
}

function fordFulkerson(graph, source, sink) {
    const n = graph.length; // Number of vertices
    
    // Initialize residual graph (initially same as original graph capacities)
    const residualGraph = graph.map(row => [...row]);
    
    // parent array to store path found by BFS
    const parent = new Array(n).fill(-1);
    
    let maxFlow = 0;

    // While there is an augmenting path from source to sink
    while (bfsFindAugmentingPath(residualGraph, source, sink, parent)) {
        // Find the bottleneck capacity of the path found by BFS
        let pathFlow = Infinity;
        let s = sink;
        while (s !== source) {
            pathFlow = Math.min(pathFlow, residualGraph[parent[s]][s]);
            s = parent[s];
        }
        
        // Add path flow to overall flow
        maxFlow += pathFlow;
        
        // Update residual capacities along the path
        let v = sink;
        while (v !== source) {
            const u = parent[v];
            residualGraph[u][v] -= pathFlow; // Decrease capacity of forward edge
            residualGraph[v][u] += pathFlow; // Increase capacity of backward edge
            v = parent[v];
        }
            
    }
    return maxFlow;
}

// const graph = [
//     [0, 16, 13, 0, 0, 0],
//     [0, 0, 10, 12, 0, 0],
//     [0, 4, 0, 0, 14, 0],
//     [0, 0, 9, 0, 0, 20],
//     [0, 0, 0, 7, 0, 4],
//     [0, 0, 0, 0, 0, 0]
// ];
// const source = 0;
// const sink = 5;
// console.log(fordFulkerson(graph, source, sink)); // Expected: 23
```

### Typescript

```typescript
function bfsFindAugmentingPathTS(residualGraph: number[][], source: number, sink: number, parent: number[]): boolean {
    const n = residualGraph.length;
    const visited: boolean[] = new Array(n).fill(false);
    const queue: number[] = [];

    queue.push(source);
    visited[source] = true;
    parent[source] = -1; // Source has no parent

    while (queue.length > 0) {
        const u = queue.shift()!;

        for (let v = 0; v < n; v++) {
            // If v is not visited and there is residual capacity from u to v
            if (!visited[v] && residualGraph[u][v] > 0) {
                queue.push(v);
                visited[v] = true;
                parent[v] = u;
                if (v === sink) { // Found path to sink
                    return true;
                }
            }
        }
    }
    return false;
}

function fordFulkersonTS(graph: number[][], source: number, sink: number): number {
    const n = graph.length; // Number of vertices
    
    // Initialize residual graph (initially same as original graph capacities)
    const residualGraph: number[][] = graph.map(row => [...row]);
    
    // parent array to store path found by BFS
    const parent: number[] = new Array(n).fill(-1);
    
    let maxFlow = 0;

    // While there is an augmenting path from source to sink
    while (bfsFindAugmentingPathTS(residualGraph, source, sink, parent)) {
        // Find the bottleneck capacity of the path found by BFS
        let pathFlow = Infinity;
        let s = sink;
        while (s !== source) {
            pathFlow = Math.min(pathFlow, residualGraph[parent[s]][s]);
            s = parent[s];
        }
        
        // Add path flow to overall flow
        maxFlow += pathFlow;
        
        // Update residual capacities along the path
        let v = sink;
        while (v !== source) {
            const u = parent[v];
            residualGraph[u][v] -= pathFlow; // Decrease capacity of forward edge
            residualGraph[v][u] += pathFlow; // Increase capacity of backward edge
            v = parent[v];
        }
            
    }
    return maxFlow;
}

// const graphTS = [
//     [0, 16, 13, 0, 0, 0],
//     [0, 0, 10, 12, 0, 0],
//     [0, 4, 0, 0, 14, 0],
//     [0, 0, 9, 0, 0, 20],
//     [0, 0, 0, 7, 0, 4],
//     [0, 0, 0, 0, 0, 0]
// ];
// const sourceTS = 0;
// const sinkTS = 5;
// console.log(fordFulkersonTS(graphTS, sourceTS, sinkTS)); // Expected: 23
```

### Cpp

```cpp
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm> // For std::min

bool bfsFindAugmentingPath(const std::vector<std::vector<int>>& residual_graph, int source, int sink, std::vector<int>& parent) {
    int n = residual_graph.size();
    std::vector<bool> visited(n, false);
    std::queue<int> q;

    q.push(source);
    visited[source] = true;
    parent[source] = -1; // Source has no parent

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v = 0; v < n; v++) {
            // If v is not visited and there is residual capacity from u to v
            if (!visited[v] && residual_graph[u][v] > 0) {
                q.push(v);
                visited[v] = true;
                parent[v] = u;
                if (v == sink) { // Found path to sink
                    return true;
                }
            }
        }
    }
    return false;
}

int fordFulkerson(const std::vector<std::vector<int>>& graph, int source, int sink) {
    int n = graph.size(); // Number of vertices
    
    // Initialize residual graph (initially same as original graph capacities)
    std::vector<std::vector<int>> residual_graph = graph;
    
    // parent array to store path found by BFS
    std::vector<int> parent(n, -1);
    
    int max_flow = 0;

    // While there is an augmenting path from source to sink
    while (bfsFindAugmentingPath(residual_graph, source, sink, parent)) {
        // Find the bottleneck capacity of the path found by BFS
        int path_flow = std::numeric_limits<int>::max();
        int s = sink;
        while (s != source) {
            path_flow = std::min(path_flow, residual_graph[parent[s]][s]);
            s = parent[s];
        }
        
        // Add path flow to overall flow
        max_flow += path_flow;
        
        // Update residual capacities along the path
        int v = sink;
        while (v != source) {
            int u = parent[v];
            residual_graph[u][v] -= path_flow; // Decrease capacity of forward edge
            residual_graph[v][u] += path_flow; // Increase capacity of backward edge (for residual graph)
            v = parent[v];
        }
            
    }
    return max_flow;
}

// int main() {
//     // Example: (from CLRS, Figure 26.1)
//     // 0: source, 5: sink
//     std::vector<std::vector<int>> graph = {
//         {0, 16, 13, 0, 0, 0},
//         {0, 0, 10, 12, 0, 0},
//         {0, 4, 0, 0, 14, 0},
//         {0, 0, 9, 0, 0, 20},
//         {0, 0, 0, 7, 0, 4},
//         {0, 0, 0, 0, 0, 0}
//     };
//     int source = 0;
//     int sink = 5;
//     std::cout << "Max flow: " << fordFulkerson(graph, source, sink) << std::endl; // 23
//     return 0;
// }
```

### Go

```go
package main

import (
    "container/list"
    "fmt"
    "math"
)

func bfsFindAugmentingPath(residualGraph [][]int, source, sink int, parent []int) bool {
    n := len(residualGraph)
    visited := make([]bool, n)
    queue := list.New()

    queue.PushBack(source)
    visited[source] = true
    parent[source] = -1 // Source has no parent

    for queue.Len() > 0 {
        u := queue.Remove(queue.Front()).(int)

        for v := 0; v < n; v++ {
            // If v is not visited and there is residual capacity from u to v
            if !visited[v] && residualGraph[u][v] > 0 {
                queue.PushBack(v)
                visited[v] = true
                parent[v] = u
                if v == sink { // Found path to sink
                    return true
                }
            }
        }
    }
    return false
}

func fordFulkerson(graph [][]int, source, sink int) int {
    n := len(graph) // Number of vertices
    
    // Initialize residual graph (initially same as original graph capacities)
    residualGraph := make([][]int, n)
    for i := range residualGraph {
        residualGraph[i] = make([]int, n)
        copy(residualGraph[i], graph[i])
    }
    
    // parent array to store path found by BFS
    parent := make([]int, n)
    
    maxFlow := 0

    // While there is an augmenting path from source to sink
    for bfsFindAugmentingPath(residualGraph, source, sink, parent) {
        // Find the bottleneck capacity of the path found by BFS
        pathFlow := math.MaxInt32
        s := sink
        for s != source {
            pathFlow = min(pathFlow, residualGraph[parent[s]][s])
            s = parent[s]
        }
        
        // Add path flow to overall flow
        maxFlow += pathFlow
        
        // Update residual capacities along the path
        v := sink
        for v != source {
            u := parent[v]
            residualGraph[u][v] -= pathFlow // Decrease capacity of forward edge
            residualGraph[v][u] += pathFlow // Increase capacity of backward edge
            v = parent[v]
        }
            
    }
    return maxFlow
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

// func main() {
//     graph := [][]int{
//         {0, 16, 13, 0, 0, 0},
//         {0, 0, 10, 12, 0, 0},
//         {0, 4, 0, 0, 14, 0},
//         {0, 0, 9, 0, 0, 20},
//         {0, 0, 0, 7, 0, 4},
//         {0, 0, 0, 0, 0, 0},
//     }
//     source := 0
//     sink := 5
//     fmt.Println("Max flow:", fordFulkerson(graph, source, sink)) // 23
// }
```

### D

```d
import std.stdio;
import std.array;
import std.algorithm; // For std.algorithm.min
import std.container.array; // For Array (queue)

bool bfsFindAugmentingPath(int[][] residualGraph, int source, int sink, ref int[] parent) {
    auto n = residualGraph.length;
    auto visited = new bool[n]; // Initialize with false
    auto queue = Array!int();

    queue.insertBack(source);
    visited[source] = true;
    parent[source] = -1; // Source has no parent

    while (!queue.empty) {
        auto u = queue.removeFront();

        foreach (v; 0 .. n) {
            // If v is not visited and there is residual capacity from u to v
            if (!visited[v] && residualGraph[u][v] > 0) {
                queue.insertBack(v);
                visited[v] = true;
                parent[v] = u;
                if (v == sink) { // Found path to sink
                    return true;
                }
            }
        }
    }
    return false;
}

int fordFulkerson(int[][] graph, int source, int sink) {
    auto n = graph.length; // Number of vertices
    
    // Initialize residual graph (initially same as original graph capacities)
    auto residualGraph = graph.dup; // Create a deep copy
    
    // parent array to store path found by BFS
    auto parent = new int[n]; // Initialize with -1, though not strictly needed

    int maxFlow = 0;

    // While there is an augmenting path from source to sink
    while (bfsFindAugmentingPath(residualGraph, source, sink, parent)) {
        // Find the bottleneck capacity of the path found by BFS
        int pathFlow = int.max;
        int s = sink;
        while (s != source) {
            pathFlow = min(pathFlow, residualGraph[parent[s]][s]);
            s = parent[s];
        }
        
        // Add path flow to overall flow
        maxFlow += pathFlow;
        
        // Update residual capacities along the path
        int v = sink;
        while (v != source) {
            int u = parent[v];
            residualGraph[u][v] -= pathFlow; // Decrease capacity of forward edge
            residualGraph[v][u] += pathFlow; // Increase capacity of backward edge
            v = parent[v];
        }
            
    }
    return maxFlow;
}

// void main() {
//     auto graph = [
//         [0, 16, 13, 0, 0, 0],
//         [0, 0, 10, 12, 0, 0],
//         [0, 4, 0, 0, 14, 0],
//         [0, 0, 9, 0, 0, 20],
//         [0, 0, 0, 7, 0, 4],
//         [0, 0, 0, 0, 0, 0]
//     ];
//     int source = 0;
//     int sink = 5;
//     writeln("Max flow: ", fordFulkerson(graph, source, sink)); // 23
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

The `Ford-Fulkerson Algorithm`, typically implemented with `BFS` (known as `Edmonds-Karp`), operates by iteratively finding paths in a `residual graph` and augmenting the `flow`.

---

**`bfs_find_augmenting_path(residual_graph, source, sink, parent)` Function:**
- This function uses `BFS` to find a path from the `source` to the `sink` in the `residual_graph`.
- `parent` array: Stores the parent of each `node` in the path, allowing path reconstruction.
- It returns `True` if a path is found (i.e., `sink` is reachable), `False` otherwise.

**`ford_fulkerson(graph, source, sink)` Function:**
- `n`: Number of `vertices` in the graph.
- `residual_graph`: A 2D array representing the `residual capacities` of `edges`. Initially, it's a copy of the original graph's `capacities`.
- `parent`: An array used by `bfs_find_augmenting_path` to reconstruct the path.
- `max_flow`: Stores the total `maximum flow` found so far, initialized to 0.

**Main Loop:**
- The `while` loop continues as long as `bfs_find_augmenting_path` finds an `augmenting path` from `source` to `sink`.
- **Find Bottleneck Capacity:** Once a path is found, `path_flow` is determined. This is the minimum `residual capacity` of any `edge` along the `augmenting path`. This `path_flow` is the maximum amount of `flow` that can be pushed through this specific path.
- **Update `max_flow`:** `path_flow` is added to `max_flow`.
- **Update Residual Capacities:**
- For every `edge (u, v)` on the `augmenting path`:
- The `residual capacity` of the forward `edge (u, v)` is decreased by `path_flow`.
- The `residual capacity` of the backward `edge (v, u)` is increased by `path_flow`. This is crucial for allowing `flow` to be "pushed back" or re-routed if a better path is found later.

            </li>

    </li>

[Back to Implementation](#implementation)

## Applications

### Application

The `Ford-Fulkerson Algorithm` (and its `Edmonds-Karp` variant) is a cornerstone algorithm in network flow theory with numerous applications:
- **Network Optimization:** Maximizing the throughput of data in communication networks, traffic flow on roads, or liquids through pipelines.
- **Bipartite Matching:** Solving maximum bipartite matching problems (e.g., assigning jobs to workers, students to projects) can be reduced to a maximum flow problem.
- **Image Segmentation:** Used in computer vision to segment images by modeling pixel connections as a flow network.
- **Airline Scheduling:** Optimizing flight assignments and crew scheduling.
- **Project Management:** Resource allocation and scheduling tasks with dependencies, where resources are capacities and tasks are flows.
- **Minimum Cut Problems:** By the Max-Flow Min-Cut Theorem, it can also be used to find the minimum cut in a network, which has applications in reliability analysis and image processing.

