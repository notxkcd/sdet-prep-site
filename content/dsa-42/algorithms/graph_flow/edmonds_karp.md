---
title: "Edmonds-Karp Algorithm"
---

The `Edmonds-Karp Algorithm` is a specific implementation of the more general `Ford-Fulkerson Method` for computing the maximum flow in a flow network. It distinguishes itself by using `Breadth-First Search (BFS)` to find `augmenting paths` in the `residual graph`. This particular choice of path-finding guarantees that the algorithm terminates in polynomial time, making it a robust and widely used approach for maximum flow problems.

By always choosing the shortest augmenting path (in terms of number of edges), `Edmonds-Karp` ensures that the total number of augmentations is bounded, leading to its polynomial time complexity.

## How it Works

### How it Works (Expanded)

The core concepts of `flow networks`, `residual graphs`, and `augmenting paths` are shared with the `Ford-Fulkerson Method`. The crucial distinction of `Edmonds-Karp` lies in how it finds these `augmenting paths`.

---

Key Concepts (shared with Ford-Fulkerson):

1.  **Flow Network:** Directed graph with capacities.
2.  **Flow:** Function respecting capacity and conservation.
3.  **Residual Graph:** Graph showing how much more flow can be sent.
4.  **Augmenting Path:** Path in residual graph from source to sink.

Edmonds-Karp Specific:
- **BFS to find augmenting paths:** Always finds a path with the minimum number of edges. This is why it is called the Edmonds-Karp algorithm (named after Jack Edmonds and Richard Karp).

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
from collections import deque

def edmonds_karp(graph, source, sink):
    """
    Finds the maximum flow from source to sink in a flow network
    using the Edmonds-Karp algorithm (Ford-Fulkerson with BFS).
    <code>graph</code> is an adjacency matrix representation of the capacities.
    """
    n = len(graph) # Number of vertices
    
    # Initialize residual graph (initially same as original graph capacities)
    residual_graph = [row[:] for row in graph]
    
    max_flow = 0

    while True:
        # parent array to store path found by BFS for path reconstruction
        parent = [-1] </em> n
        
        # BFS to find an augmenting path
        queue = deque()
        queue.append(source)
        visited = [False] * n
        visited[source] = True
        
        while queue:
            u = queue.popleft()

            for v in range(n):
                if not visited[v] and residual_graph[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
        
        # If sink is not reachable, no more augmenting paths
        if not visited[sink]:
            break
            
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
# print(edmonds_karp(graph, source, sink)) # Expected: 23
```

### Javascript

```javascript
function edmondsKarp(graph, source, sink) {
    const n = graph.length; // Number of vertices
    
    // Initialize residual graph (initially same as original graph capacities)
    const residualGraph = graph.map(row => [...row]);
    
    let maxFlow = 0;

    while (true) {
        // parent array to store path found by BFS for path reconstruction
        const parent = new Array(n).fill(-1);
        
        // BFS to find an augmenting path
        const queue = [];
        queue.push(source);
        const visited = new Array(n).fill(false);
        visited[source] = true;
        
        while (queue.length > 0) {
            const u = queue.shift();

            for (let v = 0; v < n; v++) {
                if (!visited[v] && residualGraph[u][v] > 0) {
                    queue.push(v);
                    visited[v] = true;
                    parent[v] = u;
                }
            }
        }
        
        // If sink is not reachable, no more augmenting paths
        if (!visited[sink]) {
            break;
        }
            
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
// console.log(edmondsKarp(graph, source, sink)); // Expected: 23
```

### Typescript

```typescript
function edmondsKarpTS(graph: number[][], source: number, sink: number): number {
    const n = graph.length; // Number of vertices
    
    // Initialize residual graph (initially same as original graph capacities)
    const residualGraph: number[][] = graph.map(row => [...row]);
    
    let maxFlow = 0;

    while (true) {
        // parent array to store path found by BFS for path reconstruction
        const parent: number[] = new Array(n).fill(-1);
        
        // BFS to find an augmenting path
        const queue: number[] = [];
        queue.push(source);
        const visited: boolean[] = new Array(n).fill(false);
        visited[source] = true;
        
        while (queue.length > 0) {
            const u = queue.shift()!;

            for (let v = 0; v < n; v++) {
                if (!visited[v] && residualGraph[u][v] > 0) {
                    queue.push(v);
                    visited[v] = true;
                    parent[v] = u;
                }
            }
        }
        
        // If sink is not reachable, no more augmenting paths
        if (!visited[sink]) {
            break;
        }
            
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
// console.log(edmondsKarpTS(graphTS, sourceTS, sinkTS)); // Expected: 23
```

### Cpp

```cpp
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm> // For std::min
#include <limits>    // For std::numeric_limits

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

int edmondsKarp(const std::vector<std::vector<int>>& graph, int source, int sink) {
    int n = graph.size(); // Number of vertices
    
    // Initialize residual graph (initially same as original graph capacities)
    std::vector<std::vector<int>> residual_graph = graph;
    
    int max_flow = 0;

    while (true) {
        // parent array to store path found by BFS
        std::vector<int> parent(n, -1); // Reset parent array for each BFS
        
        // BFS to find an augmenting path
        if (!bfsFindAugmentingPath(residual_graph, source, sink, parent)) {
            break; // No more augmenting paths
        }
            
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
//     std::cout << "Max flow: " << edmondsKarp(graph, source, sink) << std::endl; // 23
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

func edmondsKarp(graph [][]int, source, sink int) int {
    n := len(graph) // Number of vertices
    
    // Initialize residual graph (initially same as original graph capacities)
    residualGraph := make([][]int, n)
    for i := range residualGraph {
        residualGraph[i] = make([]int, n)
        copy(residualGraph[i], graph[i])
    }
    
    maxFlow := 0

    // While there is an augmenting path from source to sink
    for {
        // parent array to store path found by BFS
        parent := make([]int, n) // Reset parent array for each BFS
        
        // BFS to find an augmenting path
        if !bfsFindAugmentingPath(residualGraph, source, sink, parent) {
            break // No more augmenting paths
        }
            
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
//     fmt.Println("Max flow:", edmondsKarp(graph, source, sink)) // 23
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

int edmondsKarp(int[][] graph, int source, int sink) {
    auto n = graph.length; // Number of vertices
    
    // Initialize residual graph (initially same as original graph capacities)
    auto residualGraph = graph.dup; // Create a deep copy
    
    int maxFlow = 0;

    // While there is an augmenting path from source to sink
    for (;;) {
        // parent array to store path found by BFS
        auto parent = new int[n]; // Reset parent array for each BFS
        parent[] = -1; // Fill with -1 for safety
        
        // BFS to find an augmenting path
        if (!bfsFindAugmentingPath(residualGraph, source, sink, parent)) {
            break; // No more augmenting paths
        }
            
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
//     writeln("Max flow: ", edmondsKarp(graph, source, sink)); // 23
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

The `Edmonds-Karp Algorithm` is a concrete implementation of the `Ford-Fulkerson Method`, specifically using `BFS` to find augmenting paths. This ensures polynomial time complexity.

---

**`bfsFindAugmentingPath(residual_graph, source, sink, parent)` Function:**
- This is a standard `BFS` implementation adapted for the `residual_graph`.
- It attempts to find any path from `source` to `sink` where `residual_graph[u][v] > 0` (meaning there's available capacity).
- The `parent` array is crucial: `parent[v] = u` means `v` was reached from `u`. This allows the path to be reconstructed.
- It returns `True` if a path is found, `False` otherwise.

**`edmondsKarp(graph, source, sink)` Function:**
- `n`: Number of `vertices`.
- `residual_graph`: A mutable copy of the original graph's `capacities`. This graph is updated as `flow` is pushed.
- `max_flow`: The total `flow` accumulated.

**Main Loop (`while true`):**
- **Find Augmenting Path:** In each iteration, `bfsFindAugmentingPath` is called. If no path is found (`visited[sink]` is `False` in JS/TS/Python, or `bfsFindAugmentingPath` returns `False`), the algorithm terminates.
- **Find Bottleneck Capacity:** If a path is found, the `path_flow` is determined. This is the minimum `residual capacity` of any `edge` along the path from `source` to `sink`. This `path_flow` represents how much more `flow` can be pushed through this specific path.
- **Update `max_flow`:** `path_flow` is added to `max_flow`.
- **Update Residual Capacities:**
- The algorithm then traverses the `augmenting path` from `sink` back to `source` using the `parent` array.
- For every `edge (u, v)` on the path:
- The `residual capacity` of the forward `edge (u, v)` is decreased by `path_flow`.
- The `residual capacity` of the backward `edge (v, u)` is increased by `path_flow`. This is vital for `Ford-Fulkerson` to work, as it allows the algorithm to "undo" or reroute `flow` if a better path is found later.

            </li>

    </li>

[Back to Implementation](#implementation)

## Applications

### Application

The `Edmonds-Karp Algorithm` is a fundamental solution for maximum flow problems, and due to its polynomial time complexity guarantee, it's widely used where the general `Ford-Fulkerson Method` might struggle.
- **Network Optimization:** Maximizing the throughput in communication networks, traffic networks, or supply chains.
- **Bipartite Matching:** Solving maximum bipartite matching problems (e.g., job assignment, resource allocation) can be efficiently reduced to a maximum flow problem solved by `Edmonds-Karp`.
- **Image Segmentation:** In computer vision, it's used to partition an image into segments (e.g., foreground/background) by modeling pixel connections as a flow network.
- **Airline Scheduling:** Optimizing flight schedules, crew assignments, and aircraft utilization.
- **Project Management:** Resource allocation and task scheduling where dependencies and resource limits can be modeled as flow capacities.
- **Minimum Cut Problems:** Directly used to find the minimum cut in a network, which has applications in network reliability and vulnerability analysis.

