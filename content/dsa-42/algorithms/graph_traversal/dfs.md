---
title: "Depth-First Search (DFS)"
---

`Depth-First Search (DFS)` is a fundamental graph traversal algorithm that explores as far as possible along each branch before backtracking. Starting from a source `node`, it explores one of its neighbors, then that neighbor's neighbor, and so on, going deeper and deeper into the graph until it hits a `node` with no unvisited neighbors. It then backtracks to the previous 
`node` and explores another path.

The algorithm can be implemented using recursion (which implicitly uses a stack) or an explicit `stack` data structure. This "deep dive" approach gives it a different set of properties and applications compared to the "layer by layer" approach of `BFS`.

## How it Works

### How it Works (Expanded)

`DFS` maintains a set of `visited` nodes to avoid cycles. Unlike `BFS`'s `queue`, `DFS` uses a `stack` (either the program's call stack via recursion or an explicit stack data structure) to keep track of the path it is currently exploring.

---

Example: Traverse a simple graph
Graph: A -> B, A -> C, B -> D

1. Start at A. Push A to stack. Stack: [A]. Visited: {A}.
2. Pop A. Visit its neighbor B. Push B. Stack: [B]. Visited: {A, B}.
3. Pop B. Visit its neighbor D. Push D. Stack: [D]. Visited: {A, B, D}.
4. Pop D. No unvisited neighbors. Backtrack. Stack: [].
5. No more neighbors for B. Backtrack to A.
6. Visit A's other neighbor C. Push C. Stack: [C]. Visited: {A, B, D, C}.
7. Pop C. No unvisited neighbors. Backtrack.
8. Stack is empty. Search is complete.

Traversal Order (can vary): A, B, D, C

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
# Recursive DFS Implementation
def dfs_recursive(graph, start_node, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start_node)
    traversal_order = [start_node]

    for neighbor in graph.get(start_node, []):
        if neighbor not in visited:
            traversal_order.extend(dfs_recursive(graph, neighbor, visited))
            
    return traversal_order

# Iterative DFS Implementation
def dfs_iterative(graph, start_node):
    if start_node not in graph:
        return []

    visited = set()
    stack = [start_node]
    traversal_order = []

    while stack:
        current_node = stack.pop()
        
        if current_node not in visited:
            visited.add(current_node)
            traversal_order.append(current_node)
            
            # Add neighbors to the stack in reverse order to visit them alphabetically
            for neighbor in reversed(graph.get(current_node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
                    
    return traversal_order

# Example
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D'],
#     'C': [],
#     'D': []
# }
# print("Recursive:", dfs_recursive(graph, 'A')) # ['A', 'B', 'D', 'C']
# print("Iterative:", dfs_iterative(graph, 'A')) # ['A', 'B', 'D', 'C']
```

### Javascript

```javascript
function dfsRecursive(graph, startNode, visited = new Set()) {
    visited.add(startNode);
    let traversalOrder = [startNode];

    const neighbors = graph[startNode] || [];
    for (const neighbor of neighbors) {
        if (!visited.has(neighbor)) {
            traversalOrder = traversalOrder.concat(dfsRecursive(graph, neighbor, visited));
        }
    }
    return traversalOrder;
}

function dfsIterative(graph, startNode) {
    if (!graph[startNode]) {
        return [];
    }

    const visited = new Set();
    const stack = [startNode];
    const traversalOrder = [];

    while (stack.length > 0) {
        const currentNode = stack.pop();
        
        if (!visited.has(currentNode)) {
            visited.add(currentNode);
            traversalOrder.push(currentNode);

            const neighbors = graph[currentNode] || [];
            // Add neighbors to the stack in reverse order
            for (let i = neighbors.length - 1; i >= 0; i--) {
                const neighbor = neighbors[i];
                if (!visited.has(neighbor)) {
                    stack.push(neighbor);
                }
            }
        }
    }
    return traversalOrder;
}

// const graph = { 'A': ['B', 'C'], 'B': ['D'], 'C': [], 'D': [] };
// console.log("Recursive:", dfsRecursive(graph, 'A')); // ['A', 'B', 'D', 'C']
// console.log("Iterative:", dfsIterative(graph, 'A')); // ['A', 'B', 'D', 'C']
```

### Typescript

```typescript
function dfsRecursiveTS(graph: Record<string, string[]>, startNode: string, visited: Set<string> = new Set()): string[] {
    visited.add(startNode);
    let traversalOrder: string[] = [startNode];

    const neighbors = graph[startNode] || [];
    for (const neighbor of neighbors) {
        if (!visited.has(neighbor)) {
            traversalOrder = traversalOrder.concat(dfsRecursiveTS(graph, neighbor, visited));
        }
    }
    return traversalOrder;
}

function dfsIterativeTS(graph: Record<string, string[]>, startNode: string): string[] {
    if (!graph[startNode]) {
        return [];
    }

    const visited = new Set<string>();
    const stack: string[] = [startNode];
    const traversalOrder: string[] = [];

    while (stack.length > 0) {
        const currentNode = stack.pop()!;
        
        if (!visited.has(currentNode)) {
            visited.add(currentNode);
            traversalOrder.push(currentNode);

            const neighbors = graph[currentNode] || [];
            // Add neighbors to the stack in reverse order
            for (let i = neighbors.length - 1; i >= 0; i--) {
                const neighbor = neighbors[i];
                if (!visited.has(neighbor)) {
                    stack.push(neighbor);
                }
            }
        }
    }
    return traversalOrder;
}

// const graphTS: Record<string, string[]> = { 'A': ['B', 'C'], 'B': ['D'], 'C': [], 'D': [] };
// console.log("Recursive:", dfsRecursiveTS(graphTS, 'A')); // ['A', 'B', 'D', 'C']
// console.log("Iterative:", dfsIterativeTS(graphTS, 'A')); // ['A', 'B', 'D', 'C']
```

### Cpp

```cpp
#include <iostream>
#include <vector>
#include <stack>
#include <map>
#include <set>
#include <algorithm> // For std::reverse

// Recursive DFS
void dfsRecursiveHelper(const std::map<char, std::vector<char>>& graph, char node, std::set<char>& visited, std::vector<char>& order) {
    visited.insert(node);
    order.push_back(node);

    auto it = graph.find(node);
    if (it != graph.end()) {
        for (char neighbor : it->second) {
            if (visited.find(neighbor) == visited.end()) {
                dfsRecursiveHelper(graph, neighbor, visited, order);
            }
        }
    }
}

std::vector<char> dfsRecursive(const std::map<char, std::vector<char>>& graph, char startNode) {
    std::vector<char> order;
    std::set<char> visited;
    dfsRecursiveHelper(graph, startNode, visited, order);
    return order;
}

// Iterative DFS
std::vector<char> dfsIterative(const std::map<char, std::vector<char>>& graph, char startNode) {
    if (graph.find(startNode) == graph.end()) return {};

    std::set<char> visited;
    std::stack<char> s;
    std::vector<char> order;

    s.push(startNode);

    while (!s.empty()) {
        char currentNode = s.top();
        s.pop();

        if (visited.find(currentNode) == visited.end()) {
            visited.insert(currentNode);
            order.push_back(currentNode);

            auto it = graph.find(currentNode);
            if (it != graph.end()) {
                // Push neighbors in reverse order to visit them alphabetically
                std::vector<char> neighbors = it->second;
                std::reverse(neighbors.begin(), neighbors.end());
                for (char neighbor : neighbors) {
                    if (visited.find(neighbor) == visited.end()) {
                        s.push(neighbor);
                    }
                }
            }
        }
    }
    return order;
}

// int main() {
//     std::map<char, std::vector<char>> graph = {{'A', {'B', 'C'}}, {'B', {'D'}}, {'C', {}}, {'D', {}}};
//     // ... test functions
// }
```

### Go

```go
package main

import "fmt"

// Recursive DFS
func dfsRecursive(graph map[string][]string, startNode string, visited map[string]bool) []string {
    if visited == nil {
        visited = make(map[string]bool)
    }
    
    visited[startNode] = true
    order := []string{startNode}

    for _, neighbor := range graph[startNode] {
        if !visited[neighbor] {
            order = append(order, dfsRecursive(graph, neighbor, visited)...)
        }
    }
    return order
}

// Iterative DFS
func dfsIterative(graph map[string][]string, startNode string) []string {
    if _, ok := graph[startNode]; !ok {
        return nil
    }

    visited := make(map[string]bool)
    stack := []string{startNode}
    order := []string{}

    for len(stack) > 0 {
        node := stack[len(stack)-1]
        stack = stack[:len(stack)-1] // Pop

        if !visited[node] {
            visited[node] = true
            order = append(order, node)

            // Push neighbors in reverse to approximate recursive order
            neighbors := graph[node]
            for i := len(neighbors) - 1; i >= 0; i-- {
                neighbor := neighbors[i]
                if !visited[neighbor] {
                    stack = append(stack, neighbor) // Push
                }
            }
        }
    }
    return order
}

// func main() {
//     graph := map[string][]string{"A": {"B", "C"}, "B": {"D"}, "C": {}, "D": {}}
//     fmt.Println("Recursive:", dfsRecursive(graph, "A", nil)) // [A B D C]
//     fmt.Println("Iterative:", dfsIterative(graph, "A"))   // [A B D C]
// }
```

### D

```d
import std.stdio;
import std.collections;
import std.algorithm;

// Recursive DFS
void dfsRecursiveHelper(string[][string] graph, string node, ref bool[string] visited, ref string[] order) {
    visited[node] = true;
    order ~= node;

    if (auto neighbors = node in graph) {
        foreach (neighbor; <em>neighbors) {
            if (neighbor !in visited) {
                dfsRecursiveHelper(graph, neighbor, visited, order);
            }
        }
    }
}

string[] dfsRecursive(string[][string] graph, string startNode) {
    string[] order;
    bool[string] visited;
    dfsRecursiveHelper(graph, startNode, visited, order);
    return order;
}

// Iterative DFS
string[] dfsIterative(string[][string] graph, string startNode) {
    if (startNode !in graph) return [];

    bool[string] visited;
    string[] stack = [startNode];
    string[] order;

    while (!stack.empty) {
        string node = stack.back;
        stack.popBack();

        if (node !in visited) {
            visited[node] = true;
            order ~= node;

            if (auto pNeighbors = node in graph) {
                // Push neighbors in reverse
                foreach_reverse (neighbor; </em>pNeighbors) {
                    if (neighbor !in visited) {
                        stack ~= neighbor;
                    }
                }
            }
        }
    }
    return order;
}

// void main() {
//     auto graph = ["A": ["B", "C"], "B": ["D"], "C": [], "D": []];
//     writeln("Recursive:", dfsRecursive(graph, "A")); // ["A", "B", "D", "C"]
//     writeln("Iterative:", dfsIterative(graph, "A")); // ["A", "B", "D", "C"]
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

`DFS` can be implemented elegantly with recursion or iteratively with a `stack`. Both approaches achieve the same goal of exploring a branch completely before backtracking.

---

**Recursive Implementation:**
- The main function initializes a `visited` set.
- A helper function `dfsRecursiveHelper` is called with the starting `node`.
- Inside the helper, the current `node` is marked as `visited` and added to the result.
- It then iterates through its neighbors. If a neighbor has not been `visited`, the helper function calls itself with the neighbor as the new `node`.
- This creates a call stack that naturally handles the "go deep, then backtrack" logic.

**Iterative Implementation:**
- A `stack` is initialized with the `startNode`.
- A `visited` set is used to track `nodes` whose neighbors have been pushed to the `stack`.
- The loop continues while the `stack` is not empty.
- A `node` is popped from the `stack`. If it hasn't been processed, it's marked as `visited`, and its neighbors are pushed onto the `stack`.
- Pushing neighbors in reverse order (as shown in the code) ensures that the traversal order more closely mimics the typical recursive implementation (e.g., visiting 'B' before 'C' if `graph['A'] = ['B', 'C']`).

[Back to Implementation](#implementation)

## Applications

### Application

The "deep dive" nature of `DFS` makes it suitable for problems where you need to explore a path to its conclusion before trying another.
- **Topological Sorting:** `DFS` is the basis for Kahn's algorithm and other methods for topologically sorting a directed acyclic graph (DAG), which is used in scheduling tasks with dependencies.
- **Finding Connected Components:** Similar to `BFS`, `DFS` can be used to find all nodes connected to a source node.
- **Pathfinding and Mazes:** Finding a path between two nodes in a maze or a graph. While `BFS` is guaranteed to find the shortest path in an unweighted graph, `DFS` is simpler to implement and can find *a* path very quickly.
- **Detecting Cycles:** By keeping track of the nodes currently in the recursion stack, `DFS` can be adapted to detect cycles in a graph.
- **Solving Puzzles:** Many puzzles that can be represented as a state graph (like Sudoku or finding a way out of a maze) can be solved with a `DFS`-based backtracking approach.

