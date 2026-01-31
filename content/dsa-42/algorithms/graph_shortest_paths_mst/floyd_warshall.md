---
title: "Floyd-Warshall Algorithm"
---

The `Floyd-Warshall Algorithm` is a classic algorithm for finding the shortest paths between **all pairs** of `nodes` in a weighted graph. It works for both directed and undirected graphs, and it can handle graphs with negative edge weights, but it cannot handle negative cycles (a cycle where the sum of its edge weights is negative), as the shortest path in such a cycle would be undefined.

It is an example of `dynamic programming` and is conceptually simple to understand and implement. The algorithm iteratively considers all possible intermediate `nodes` to find the shortest path between any two `nodes`.

## How it Works

### How it Works (Expanded)

The `Floyd-Warshall Algorithm` uses a 2D `DP table` (distance matrix) where `dist[i][j]` stores the shortest distance from `node i` to `node j`. The algorithm performs `N` phases (where `N` is the number of `nodes`), and in the `k`-th phase, it considers all paths that use only `nodes` from `1` to `k` as intermediate `nodes`.

---

Example: Graph with 4 nodes (0, 1, 2, 3)

Initial Distance Matrix:
   0  1  2  3
0 [0, 3, inf, 7]
1 [8, 0, 2, inf]
2 [5, inf, 0, 1]
3 [2, inf, inf, 0]

Iteration k=0 (consider node 0 as intermediate):
   0  1  2  3
0 [0, 3, inf, 7]  (e.g., dist[0][1] = min(dist[0][1], dist[0][0]+dist[0][1]) = 3)
1 [8, 0, 2, 9]    (e.g., dist[1][3] = min(dist[1][3], dist[1][0]+dist[0][3]) = min(inf, 8+7) = 15 -> Error in example, correct would be 9: 1->0->3 with 8+7=15. Example is wrong)

Corrected for k=0 path 1->0->3
 dist[1][3] = min(dist[1][3], dist[1][0]+dist[0][3]) = min(inf, 8+7) = 15

The general recurrence relation is:
dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
import math

def floyd_warshall(graph_matrix):
    n = len(graph_matrix)
    
    # Initialize dist matrix (same as graph_matrix initially)
    dist = [row[:] for row in graph_matrix]

    # Algorithm core
    # k is the intermediate vertex
    for k in range(n):
        # i is the source vertex
        for i in range(n):
            # j is the destination vertex
            for j in range(n):
                # If vertex k is on the shortest path from i to j,
                # then update the value of dist[i][j]
                if dist[i][k] != math.inf and dist[k][j] != math.inf:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    # Check for negative cycles (optional, if original problem allows)
    # If dist[i][i] < 0 for any i, then there is a negative cycle.
    # for i in range(n):
    #     if dist[i][i] < 0:
    #         # Handle negative cycle (e.g., return error or specific value)
    #         pass # This implementation just returns the matrix, possibly with -inf

    return dist

# Example
# INF = math.inf
# graph = [
#     [0, 3, INF, 7],
#     [8, 0, 2, INF],
#     [5, INF, 0, 1],
#     [2, INF, INF, 0]
# ]
# # Expected output:
# # [[0, 3, 5, 6],
# #  [8, 0, 2, 3],
# #  [5, 8, 0, 1],
# #  [2, 5, 7, 0]]
# print(floyd_warshall(graph))
```

### Javascript

```javascript
function floydWarshall(graphMatrix) {
    const n = graphMatrix.length;
    const INF = Infinity; // Represents unreachable path

    // Initialize dist matrix (same as graphMatrix initially)
    const dist = graphMatrix.map(row => [...row]);

    // Algorithm core
    // k is the intermediate vertex
    for (let k = 0; k < n; k++) {
        // i is the source vertex
        for (let i = 0; i < n; i++) {
            // j is the destination vertex
            for (let j = 0; j < n; j++) {
                // If vertex k is on the shortest path from i to j,
                // then update the value of dist[i][j]
                if (dist[i][k] !== INF && dist[k][j] !== INF) {
                    dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }
    
    // Check for negative cycles (optional)
    // for (let i = 0; i < n; i++) {
    //     if (dist[i][i] < 0) {
    //         // Graph contains a negative cycle
    //         // Can return an error or special value
    //     }
    // }

    return dist;
}

// const INF = Infinity;
// const graph = [
//     [0, 3, INF, 7],
//     [8, 0, 2, INF],
//     [5, INF, 0, 1],
//     [2, INF, INF, 0]
// ];
// // Expected output:
// // [[0, 3, 5, 6],
// //  [8, 0, 2, 3],
// //  [5, 8, 0, 1],
// //  [2, 5, 7, 0]]
// console.log(floydWarshall(graph));
```

### Typescript

```typescript
function floydWarshallTS(graphMatrix: number[][]): number[][] {
    const n = graphMatrix.length;
    const INF = Infinity; // Represents unreachable path

    // Initialize dist matrix (same as graphMatrix initially)
    const dist: number[][] = graphMatrix.map(row => [...row]);

    // Algorithm core
    // k is the intermediate vertex
    for (let k = 0; k < n; k++) {
        // i is the source vertex
        for (let i = 0; i < n; i++) {
            // j is the destination vertex
            for (let j = 0; j < n; j++) {
                // If vertex k is on the shortest path from i to j,
                // then update the value of dist[i][j]
                if (dist[i][k] !== INF && dist[k][j] !== INF) {
                    dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }
    
    // Check for negative cycles (optional)
    // for (let i = 0; i < n; i++) {
    //     if (dist[i][i] < 0) {
    //         // Graph contains a negative cycle
    //         // Can return an error or special value
    //     }
    // }

    return dist;
}

// const INF_TS = Infinity;
// const graphTS = [
//     [0, 3, INF_TS, 7],
//     [8, 0, 2, INF_TS],
//     [5, INF_TS, 0, 1],
//     [2, INF_TS, INF_TS, 0]
// ];
// // Expected output:
// // [[0, 3, 5, 6],
// //  [8, 0, 2, 3],
// //  [5, 8, 0, 1],
// //  [2, 5, 7, 0]]
// console.log(floydWarshallTS(graphTS));
```

### Cpp

```cpp
#include <vector>
#include <iostream>
#include <algorithm> // For std::min
#include <limits>    // For std::numeric_limits

const int INF = std::numeric_limits<int>::max();

std::vector<std::vector<int>> floydWarshall(std::vector<std::vector<int>>& graph_matrix) {
    int n = graph_matrix.length();
    
    // Initialize dist matrix (same as graph_matrix initially)
    std::vector<std::vector<int>> dist = graph_matrix;

    // Algorithm core
    // k is the intermediate vertex
    for (int k = 0; k < n; k++) {
        // i is the source vertex
        for (int i = 0; i < n; i++) {
            // j is the destination vertex
            for (int j = 0; j < n; j++) {
                // If dist[i][k] or dist[k][j] is INF, then there is no path through k
                // We need to check to prevent INF + value from wrapping around or becoming negative
                if (dist[i][k] != INF && dist[k][j] != INF) {
                    dist[i][j] = std::min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }
    
    // Check for negative cycles (optional)
    // for (int i = 0; i < n; i++) {
    //     if (dist[i][i] < 0) {
    //         // Graph contains a negative cycle
    //         // Can return an error or special value
    //     }
    // }

    return dist;
}

// int main() {
//     std::vector<std::vector<int>> graph = {
//         {0, 3, INF, 7},
//         {8, 0, 2, INF},
//         {5, INF, 0, 1},
//         {2, INF, INF, 0}
//     };
//     std::vector<std::vector<int>> result = floydWarshall(graph);
//     for (const auto& row : result) {
//         for (int val : row) {
//             if (val == INF) std::cout << "INF ";
//             else std::cout << val << "   ";
//         }
//         std::cout << std::endl;
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

const INF_GO = math.MaxInt32

func floydWarshall(graphMatrix [][]int) [][]int {
    n := len(graphMatrix)
    
    // Initialize dist matrix (same as graphMatrix initially)
    dist := make([][]int, n)
    for i := range dist {
        dist[i] = make([]int, n)
        copy(dist[i], graphMatrix[i])
    }

    // Algorithm core
    // k is the intermediate vertex
    for k := 0; k < n; k++ {
        // i is the source vertex
        for i := 0; i < n; i++ {
            // j is the destination vertex
            for j := 0; j < n; j++ {
                // If dist[i][k] or dist[k][j] is INF_GO, then there is no path through k
                // We need to check to prevent INF_GO + value from wrapping around or becoming negative
                if dist[i][k] != INF_GO && dist[k][j] != INF_GO {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                }
            }
        }
    }
    
    // Check for negative cycles (optional)
    // for i := 0; i < n; i++ {
    //     if dist[i][i] < 0 {
    //         // Graph contains a negative cycle
    //         // Can return an error or special value
    //     }
    // }

    return dist
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

// func main() {
//     graph := [][]int{
//         {0, 3, INF_GO, 7},
//         {8, 0, 2, INF_GO},
//         {5, INF_GO, 0, 1},
//         {2, INF_GO, INF_GO, 0},
//     }
//     result := floydWarshall(graph)
//     for _, row := range result {
//         for _, val := range row {
//             if val == INF_GO {
//                 fmt.Print("INF ")
//             } else {
//                 fmt.Printf("%d   ", val)
//             }
//         }
//         fmt.Println()
//     }
// }
```

### D

```d
import std.stdio;
import std.array;
import std.algorithm; // For std.algorithm.min
import std.traits; // For isInfinity

const int INF_D = int.max;

int[][] floydWarshall(int[][] graphMatrix) {
    auto n = graphMatrix.length;
    
    // Initialize dist matrix (same as graphMatrix initially)
    auto dist = new int[][](n, n);
    foreach (i; 0 .. n) {
        foreach (j; 0 .. n) {
            dist[i][j] = graphMatrix[i][j];
        }
    }

    // Algorithm core
    // k is the intermediate vertex
    foreach (k; 0 .. n) {
        // i is the source vertex
        foreach (i; 0 .. n) {
            // j is the destination vertex
            foreach (j; 0 .. n) {
                // If dist[i][k] or dist[k][j] is INF_D, then there is no path through k
                if (dist[i][k] != INF_D && dist[k][j] != INF_D) {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }
    }
    
    // Check for negative cycles (optional)
    // foreach (i; 0 .. n) {
    //     if (dist[i][i] < 0) {
    //         // Graph contains a negative cycle
    //         // Can return an error or special value
    //     }
    // }

    return dist;
}

// void main() {
//     int[][] graph = [
//         [0, 3, INF_D, 7],
//         [8, 0, 2, INF_D],
//         [5, INF_D, 0, 1],
//         [2, INF_D, INF_D, 0]
//     ];
//     auto result = floydWarshall(graph);
//     foreach (row; result) {
//         foreach (val; row) {
//             if (val == INF_D) write("INF ");
//             else writef("%d   ", val);
//         }
//         writeln();
//     }
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

The `Floyd-Warshall Algorithm` uses three nested loops to build up the all-pairs shortest path information. It's a prime example of a `dynamic programming` approach to graph problems.

---

**Initialization:**
- `n`: The number of `nodes` in the graph.
- A `dist` matrix is created, initially a copy of the `graph_matrix`.
- `dist[i][j]` is the direct weight of the edge from `i` to `j`.
- If there is no direct edge, `dist[i][j]` is set to `infinity`.
- `dist[i][i]` is 0.

    </li>

**Algorithm Core (Three Nested Loops):**
- The outermost loop iterates `k` from 0 to `n-1`. `k` represents the "intermediate node" being considered. In each `k` iteration, the algorithm tries to improve the shortest paths between all pairs `(i, j)` by potentially routing them through `node k`.
- The middle loop iterates `i` (the source `node`) from 0 to `n-1`.
- The innermost loop iterates `j` (the destination `node`) from 0 to `n-1`.
- Inside the innermost loop, the core update happens:
        `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`</li>
- This means: The shortest path from `i` to `j` is either the path found so far (not using `k` as an intermediate), or it is a path from `i` to `k` and then from `k` to `j`. We take the minimum of these two options.
- It's important to ensure that `dist[i][k]` and `dist[k][j]` are not `infinity` before summing them to avoid `overflows` or incorrect calculations.

**Result:**
- After all three loops complete, `dist[i][j]` contains the shortest path from `node i` to `node j` for all pairs `(i, j)`.

[Back to Implementation](#implementation)

## Applications

### Application

The `Floyd-Warshall Algorithm` is highly versatile for problems requiring all-pairs shortest paths:
- **Routing in Networks:** Finding the shortest path between all pairs of devices in a network (e.g., computer networks, telecommunications).
- **Transitive Closure:** Determining if there is a path (of any length) between every pair of `nodes` in a graph. This can be adapted by changing the `min` operation to `OR` and `sum` to `AND`.
- **Analyzing Road Networks:** Computing the shortest travel times or distances between all intersections in a city.
- **Biology:** In some biological network analyses, such as protein-protein interaction networks, to understand connectivity.
- **Graph Analytics:** A foundational algorithm for various graph-theoretic problems and analyses.

