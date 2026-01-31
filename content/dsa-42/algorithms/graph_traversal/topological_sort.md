---
title: "Topological Sort"
---

`Topological Sort` is a linear ordering of `nodes` such that for every directed `edge` from `node u` to `node v`, `u` comes before `v` in the ordering. It is applicable only to **Directed Acyclic Graphs (DAGs)**. If a graph contains a `cycle`, a `topological sort` is not possible.

This algorithm is widely used in scheduling problems where tasks have dependencies, such as course prerequisites, build systems, or task queues. The result of a `topological sort` is one of many possible valid orderings.

## How it Works

### How it Works (Expanded)

A common and intuitive way to implement `Topological Sort` is **Kahn's Algorithm**, which uses a `queue`-based approach. It works by identifying `nodes` with no incoming `edges` ("in-degree" of 0) and adding them to the sorted list. As these `nodes` are processed, their outgoing `edges` are conceptually "removed", and the `in-degrees` of their neighboring `nodes` are decremented. If a neighbor's `in-degree` becomes 0, it is added to the `queue` to be processed.

---

Example: Graph representing course prerequisites
(0->1, 0->2, 1->3, 2->3, 3->4)

1. Calculate in-degrees:
- 0: 0
- 1: 1 (from 0)
- 2: 1 (from 0)
- 3: 2 (from 1, 2)
- 4: 1 (from 3)

2. Initialize queue with nodes with in-degree 0:
- Queue: [0]

3. Process queue:
- Dequeue 0. Add to sorted list. List: [0].
- "Remove" edges from 0:
- Decrement in-degree of 1. In-degree(1) becomes 0. Enqueue 1.
- Decrement in-degree of 2. In-degree(2) becomes 0. Enqueue 2.
- Queue: [1, 2].
- Dequeue 1. Add to sorted list. List: [0, 1].
- "Remove" edges from 1:
- Decrement in-degree of 3. In-degree(3) becomes 1.
- Queue: [2].
- Dequeue 2. Add to sorted list. List: [0, 1, 2].
- "Remove" edges from 2:
- Decrement in-degree of 3. In-degree(3) becomes 0. Enqueue 3.
- Queue: [3].
- ... and so on.

Final Sorted Order (one possibility): [0, 1, 2, 3, 4]

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
from collections import deque

def topological_sort(graph):
    """
    Performs a topological sort on a directed acyclic graph (DAG) using Kahn's algorithm.
    <code>graph</code> is an adjacency list: {node: [neighbor1, neighbor2, ...]}
    """
    n = len(graph)
    if n == 0:
        return []

    in_degree = {i: 0 for i in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    
    # Initialize queue with nodes having an in-degree of 0
    queue = deque([u for u in graph if in_degree[u] == 0])
    
    topological_order = []
    
    while queue:
        u = queue.popleft()
        topological_order.append(u)
        
        # For each neighbor of the dequeued node, decrement its in-degree
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    # If the number of nodes in the topological order is not equal to the
    # total number of nodes, there is a cycle.
    if len(topological_order) != n:
        return "Graph has a cycle, topological sort not possible"
    
    return topological_order

# Example:
# graph = {
#     0: [1, 2],
#     1: [3],
#     2: [3],
#     3: [4],
#     4: []
# }
# print(topological_sort(graph)) # Expected: [0, 1, 2, 3, 4] or [0, 2, 1, 3, 4]

# graph_with_cycle = {
#     0: [1],
#     1: [2],
#     2: [0]
# }
# print(topological_sort(graph_with_cycle)) # "Graph has a cycle..."
```

### Javascript

```javascript
function topologicalSort(graph) {
    const n = Object.keys(graph).length;
    if (n === 0) {
        return [];
    }

    const inDegree = {};
    for (const u in graph) {
        inDegree[u] = 0;
    }
    
    for (const u in graph) {
        for (const v of graph[u]) {
            inDegree[v]++;
        }
    }
    
    const queue = [];
    for (const u in inDegree) {
        if (inDegree[u] === 0) {
            queue.push(u);
        }
    }
    
    const topologicalOrder = [];
    
    while (queue.length > 0) {
        const u = queue.shift();
        topologicalOrder.push(u);
        
        // For each neighbor, decrement its in-degree
        for (const v of graph[u]) {
            inDegree[v]--;
            if (inDegree[v] === 0) {
                queue.push(v);
            }
        }
    }
    
    if (topologicalOrder.length !== n) {
        return "Graph has a cycle, topological sort not possible";
    }
    
    return topologicalOrder;
}

// const graph = {
//     '0': ['1', '2'],
//     '1': ['3'],
//     '2': ['3'],
//     '3': ['4'],
//     '4': []
// };
// console.log(topologicalSort(graph)); // e.g., ['0', '1', '2', '3', '4']

// const graphWithCycle = {
//     '0': ['1'],
//     '1': ['2'],
//     '2': ['0']
// };
// console.log(topologicalSort(graphWithCycle)); // "Graph has a cycle..."
```

### Typescript

```typescript
function topologicalSortTS(graph: Record<string, string[]>): string[] | string {
    const n = Object.keys(graph).length;
    if (n === 0) {
        return [];
    }

    const inDegree: Record<string, number> = {};
    for (const u in graph) {
        inDegree[u] = 0;
    }
    
    for (const u in graph) {
        for (const v of graph[u]) {
            inDegree[v]++;
        }
    }
    
    const queue: string[] = [];
    for (const u in inDegree) {
        if (inDegree[u] === 0) {
            queue.push(u);
        }
    }
    
    const topologicalOrder: string[] = [];
    
    while (queue.length > 0) {
        const u = queue.shift()!;
        topologicalOrder.push(u);
        
        // For each neighbor, decrement its in-degree
        for (const v of graph[u]) {
            inDegree[v]--;
            if (inDegree[v] === 0) {
                queue.push(v);
            }
        }
    }
    
    if (topologicalOrder.length !== n) {
        return "Graph has a cycle, topological sort not possible";
    }
    
    return topologicalOrder;
}

// const graphTS: Record<string, string[]> = {
//     '0': ['1', '2'],
//     '1': ['3'],
//     '2': ['3'],
//     '3': ['4'],
//     '4': []
// };
// console.log(topologicalSortTS(graphTS)); // e.g., ['0', '1', '2', '3', '4']
```

### Cpp

```cpp
#include <vector>
#include <queue>
#include <map>
#include <iostream>

using GraphAdjList = std::map<int, std::vector<int>>;

std::vector<int> topologicalSort(const GraphAdjList& graph) {
    int n = graph.size();
    if (n == 0) {
        return {};
    }

    std::map<int, int> in_degree;
    for(const auto& pair : graph) {
        in_degree[pair.first] = 0;
    }

    for (const auto& pair : graph) {
        for (int v : pair.second) {
            in_degree[v]++;
        }
    }
    
    std::queue<int> q;
    for (const auto& pair : in_degree) {
        if (pair.second == 0) {
            q.push(pair.first);
        }
    }
    
    std::vector<int> topological_order;
    
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        topological_order.push_back(u);
        
        // For each neighbor, decrement its in-degree
        auto it = graph.find(u);
        if (it != graph.end()) {
            for (int v : it->second) {
                in_degree[v]--;
                if (in_degree[v] == 0) {
                    q.push(v);
                }
            }
        }
    }
    
    if (topological_order.size() != n) {
        // Graph has a cycle, clear the result or throw an exception
        return {}; 
    }
    
    return topological_order;
}

// int main() {
//     GraphAdjList graph = {
//         {0, {1, 2}},
//         {1, {3}},
//         {2, {3}},
//         {3, {4}},
//         {4, {}}
//     };
//     std::vector<int> result = topologicalSort(graph);
//     for (int node : result) {
//         std::cout << node << " "; // 0 1 2 3 4 or 0 2 1 3 4
//     }
//     std::cout << std::endl;
//     return 0;
// }
```

### Go

```go
package main

import (
    "container/list"
    "fmt"
)

func topologicalSort(graph map[int][]int) ([]int, error) {
    n := len(graph)
    if n == 0 {
        return []int{}, nil
    }

    inDegree := make(map[int]int)
    for u := range graph {
        inDegree[u] = 0
    }
    
    for _, neighbors := range graph {
        for _, v := range neighbors {
            inDegree[v]++
        }
    }
    
    queue := list.New()
    for u, degree := range inDegree {
        if degree == 0 {
            queue.PushBack(u)
        }
    }
    
    topologicalOrder := []int{}
    
    for queue.Len() > 0 {
        u := queue.Remove(queue.Front()).(int)
        topologicalOrder = append(topologicalOrder, u)
        
        // For each neighbor, decrement its in-degree
        for _, v := range graph[u] {
            inDegree[v]--
            if inDegree[v] == 0 {
                queue.PushBack(v)
            }
        }
    }
    
    if len(topologicalOrder) != n {
        return nil, fmt.Errorf("graph has a cycle, topological sort not possible")
    }
    
    return topologicalOrder, nil
}

// func main() {
//     graph := map[int][]int{
//         0: {1, 2},
//         1: {3},
//         2: {3},
//         3: {4},
//         4: {},
//     }
//     order, err := topologicalSort(graph)
//     if err != nil {
//         fmt.Println(err)
//     } else {
//         fmt.Println("Topological Sort:", order) // e.g., [0 1 2 3 4]
//     }
// }
```

### D

```d
import std.stdio;
import std.array;
import std.algorithm;
import std.container.array;

string[] topologicalSort(string[][string] graph) {
    if (graph.length == 0) {
        return [];
    }

    int[string] inDegree;
    foreach (u; graph.keys) {
        inDegree[u] = 0;
    }
    
    foreach (u, neighbors; graph) {
        foreach (v; neighbors) {
            inDegree[v]++;
        }
    }
    
    auto queue = Array!string();
    foreach (u, degree; inDegree) {
        if (degree == 0) {
            queue.insertBack(u);
        }
    }
    
    string[] topologicalOrder;
    
    while (!queue.empty) {
        auto u = queue.removeFront();
        topologicalOrder ~= u;
        
        // For each neighbor, decrement its in-degree
        if (auto pNeighbors = u in graph) {
            foreach (v; *pNeighbors) {
                inDegree[v]--;
                if (inDegree[v] == 0) {
                    queue.insertBack(v);
                }
            }
        }
    }
    
    if (topologicalOrder.length != graph.length) {
        // Graph has a cycle, return an empty array or throw
        return []; 
    }
    
    return topologicalOrder;
}

// void main() {
//     auto graph = [
//         "0": ["1", "2"],
//         "1": ["3"],
//         "2": ["3"],
//         "3": ["4"],
//         "4": []
//     ];
//     writeln("Topological Sort: ", topologicalSort(graph)); // e.g., ["0", "1", "2", "3", "4"]
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

`Topological Sort` is typically implemented using `Kahn's Algorithm`, which relies on tracking the "in-degree" of each `node`.

---

**Initialization:**
- `graph`: An adjacency list representation of a directed graph.
- `in_degree`: A map or `array` to store the number of incoming `edges` for each `node`. This is computed by iterating through all `edges` in the graph.
- `queue`: A `queue` is initialized with all `nodes` that have an in-degree of 0. These are the starting points of our topological sort.
- `topological_order`: An empty list to store the sorted `nodes`.

**Main Loop:**
- The `while` loop continues as long as the `queue` is not empty.
- **Dequeue:** A `node u` is dequeued. This `node` is added to the `topological_order` list.
- **Process Neighbors:** For each `neighbor v` of `u`:
- The in-degree of `v` is decremented, as the `edge` from `u` to `v` has been "removed".
- If the in-degree of `v` becomes 0, it means all of its `prerequisites` have been met, so `v` is added to the `queue`.

    </li>

**Cycle Detection and Result:**
- After the loop, the algorithm checks if the number of `nodes` in `topological_order` is equal to the total number of `nodes` in the graph.
- If they are equal, the `topological_order` is a valid sorted sequence.
- If they are not equal, it means the `queue` became empty before all `nodes` were visited. This can only happen if there is a `cycle` in the graph, as the `cycle` would prevent the in-degrees of its `nodes` from ever reaching 0. In this case, a `topological sort` is not possible.

[Back to Implementation](#implementation)

## Applications

### Application

`Topological Sort` is fundamental in computer science for processing sequences with dependencies:
- **Task Scheduling:** Given a set of tasks with dependencies (e.g., task A must be completed before task B), `topological sort` provides a valid order of execution.
- **Course Prerequisites:** Determining the order in which to take university courses based on their prerequisites.
- **Build Systems:** In software development, build systems (like `make` or `Maven`) use `topological sort` to determine the order in which to compile source files and link libraries.
- **Spreadsheet Cell Evaluation:** Calculating the values of cells in a spreadsheet, where some cells depend on the values of others.
- **Data Serialization/Deserialization:** Resolving dependencies when serializing or deserializing complex data structures.

