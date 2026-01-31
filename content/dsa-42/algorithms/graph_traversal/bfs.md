---
title: "Breadth-First Search (BFS)"
---

`Breadth-First Search (BFS)` is a fundamental graph traversal algorithm that explores a graph "layer by layer". Starting from a given source `node`, it explores all of its immediate neighbors first, before moving on to the next level of neighbors. It is often used to find the shortest path between two `nodes` in an unweighted graph.

The algorithm uses a `queue` to keep track of the `nodes` to visit next. This ensures that `nodes` are visited in the order of their distance from the source, guaranteeing that the first time a `node` is reached, it is via the shortest path.

## How it Works

### How it Works (Expanded)

`BFS` maintains a `queue` of `nodes` to visit and a set of `visited` nodes to avoid cycles and redundant processing.

---

Example: Traverse a simple graph
Graph: A -> B, A -> C, B -> D

1. Start at A. Queue: [A]. Visited: {A}.
2. Dequeue A. Visit its neighbors B and C.
- Enqueue B. Visited: {A, B}. Queue: [B].
- Enqueue C. Visited: {A, B, C}. Queue: [B, C].
3. Dequeue B. Visit its neighbor D.
- Enqueue D. Visited: {A, B, C, D}. Queue: [C, D].
4. Dequeue C. No unvisited neighbors.
5. Dequeue D. No unvisited neighbors.
6. Queue is empty. Search is complete.

Traversal Order: A, B, C, D

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
from collections import deque

def bfs(graph, start_node):
    """
    Performs BFS on a graph represented as an adjacency list.
    <code>graph</code> is a dict where keys are nodes and values are lists of neighbors.
    """
    if start_node not in graph:
        return []

    visited = {start_node}
    queue = deque([start_node])
    traversal_order = []

    while queue:
        current_node = queue.popleft()
        traversal_order.append(current_node)

        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return traversal_order

# Example
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D'],
#     'C': [],
#     'D': []
# }
# print(bfs(graph, 'A')) # ['A', 'B', 'C', 'D']
```

### Javascript

```javascript
function bfs(graph, startNode) {
    if (!graph[startNode]) {
        return [];
    }

    const visited = new Set([startNode]);
    const queue = [startNode];
    const traversalOrder = [];

    while (queue.length > 0) {
        const currentNode = queue.shift(); // Dequeue
        traversalOrder.push(currentNode);

        const neighbors = graph[currentNode] || [];
        for (const neighbor of neighbors) {
            if (!visited.has(neighbor)) {
                visited.add(neighbor);
                queue.push(neighbor); // Enqueue
            }
        }
    }
    
    return traversalOrder;
}

// const graph = {
//     'A': ['B', 'C'],
//     'B': ['D'],
//     'C': [],
//     'D': []
// };
// console.log(bfs(graph, 'A')); // ['A', 'B', 'C', 'D']
```

### Typescript

```typescript
function bfsTS(graph: Record<string, string[]>, startNode: string): string[] {
    if (!graph[startNode]) {
        return [];
    }

    const visited = new Set<string>([startNode]);
    const queue: string[] = [startNode];
    const traversalOrder: string[] = [];

    while (queue.length > 0) {
        const currentNode = queue.shift()!; // Dequeue
        traversalOrder.push(currentNode);

        const neighbors = graph[currentNode] || [];
        for (const neighbor of neighbors) {
            if (!visited.has(neighbor)) {
                visited.add(neighbor);
                queue.push(neighbor); // Enqueue
            }
        }
    }
    
    return traversalOrder;
}

// const graphTS: Record<string, string[]> = {
//     'A': ['B', 'C'],
//     'B': ['D'],
//     'C': [],
//     'D': []
// };
// console.log(bfsTS(graphTS, 'A')); // ['A', 'B', 'C', 'D']
```

### Cpp

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <set>

std::vector<char> bfs(const std::map<char, std::vector<char>>& graph, char startNode) {
    if (graph.find(startNode) == graph.end()) {
        return {};
    }

    std::set<char> visited;
    std::queue<char> q;
    std::vector<char> traversalOrder;

    visited.insert(startNode);
    q.push(startNode);

    while (!q.empty()) {
        char currentNode = q.front();
        q.pop();
        traversalOrder.push_back(currentNode);

        auto it = graph.find(currentNode);
        if (it != graph.end()) {
            for (char neighbor : it->second) {
                if (visited.find(neighbor) == visited.end()) {
                    visited.insert(neighbor);
                    q.push(neighbor);
                }
            }
        }
    }
    
    return traversalOrder;
}

// int main() {
//     std::map<char, std::vector<char>> graph = {
//         {'A', {'B', 'C'}},
//         {'B', {'D'}},
//         {'C', {}},
//         {'D', {}}
//     };
//     std::vector<char> result = bfs(graph, 'A');
//     for(char node : result) {
//         std::cout << node << " "; // A B C D
//     }
//     std::cout << std::endl;
// }
```

### Go

```go
package main

import "fmt"

func bfs(graph map[string][]string, startNode string) []string {
    if _, ok := graph[startNode]; !ok {
        return nil
    }

    visited := make(map[string]bool)
    queue := []string{startNode}
    traversalOrder := []string{}

    visited[startNode] = true

    for len(queue) > 0 {
        currentNode := queue[0]
        queue = queue[1:] // Dequeue
        traversalOrder = append(traversalOrder, currentNode)

        for _, neighbor := range graph[currentNode] {
            if !visited[neighbor] {
                visited[neighbor] = true
                queue = append(queue, neighbor) // Enqueue
            }
        }
    }
    
    return traversalOrder
}

// func main() {
//     graph := map[string][]string{
//         "A": {"B", "C"},
//         "B": {"D"},
//         "C": {},
//         "D": {},
//     }
//     fmt.Println(bfs(graph, "A")) // [A B C D]
// }
```

### D

```d
import std.stdio;
import std.collections;

string[] bfs(string[][string] graph, string startNode) {
    if (startNode !in graph) {
        return [];
    }

    bool[string] visited;
    ArrayQueue!string queue;
    string[] traversalOrder;

    visited[startNode] = true;
    queue.put(startNode);

    while (!queue.empty) {
        string currentNode = queue.get();
        traversalOrder ~= currentNode;

        if (auto neighbors = startNode in graph) {
             foreach (neighbor; *neighbors) {
                if (neighbor !in visited) {
                    visited[neighbor] = true;
                    queue.put(neighbor);
                }
            }
        }
    }
    
    return traversalOrder;
}

// void main() {
//     auto graph = [
//         "A": ["B", "C"],
//         "B": ["D"],
//         "C": [],
//         "D": []
//     ];
//     writeln(bfs(graph, "A")); // ["A", "B", "C", "D"]
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

The implementation of `BFS` is straightforward and relies on a `queue` and a way to track visited `nodes` to prevent infinite loops in graphs with cycles.

---
- **Initialization:**
- A `queue` is created to hold the `nodes` that are waiting to be processed. The `startNode` is added to it.
- A `visited` set (or hash map) is created to keep track of `nodes` that have already been enqueued. This is crucial to avoid processing the same `node` multiple times and getting stuck in cycles. The `startNode` is marked as visited.
- An `traversalOrder` array is initialized to store the result.

    </li>
- **Main Loop:** The loop continues as long as the `queue` is not empty.
- **Dequeue:** The `currentNode` is removed from the front of the `queue`.
- **Process:** The `currentNode` is added to the `traversalOrder`.
- **Explore Neighbors:** The algorithm iterates through the neighbors of the `currentNode`. For each `neighbor`:
- It checks if the `neighbor` has already been `visited`.
- If not, the `neighbor` is marked as `visited` and enqueued.

            </li>

    </li>
- **Return:** Once the `queue` is empty, it means all reachable `nodes` have been visited, and the `traversalOrder` is returned.

[Back to Implementation](#implementation)

## Applications

### Application

`BFS` is a fundamental algorithm with a wide range of applications in computer science and graph theory.
- **Shortest Path in Unweighted Graphs:** It is the standard algorithm for finding the shortest path from a source `node` to all other `nodes` in an unweighted graph. The first time `BFS` visits a `node`, it does so via the shortest possible path.
- **Network Broadcasting:** Simulating the broadcast of a message in a network to all connected devices.
- **Web Crawlers (Crawling):** Used to discover all pages on a website starting from a homepage. Each page is a `node`, and hyperlinks are edges.
- **Finding Connected Components:** By running `BFS` starting from an arbitrary `node`, you can find all `nodes` in its connected component. Repeating this for all unvisited `nodes` finds all components.
- **Solving Puzzles:** Finding the shortest number of steps to solve puzzles like Rubik's Cubes or finding the shortest path in a maze.

