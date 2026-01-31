---
title: "Graph"
---

Imagine a network of cities connected by roads, or a social network where people are connected by friendships. A `Graph` data structure is a way to model such relationships between objects.

It consists of a set of '`nodes`' (also called `vertices`) and a set of '`edges`' that connect pairs of `nodes`. `Graphs` are incredibly versatile and are used to solve a vast range of real-world problems.

## How it Works

### How it Works (Expanded)

`Graphs` can be either directed (`edges` have a specific flow, like one-way streets) or undirected (`edges` go both ways, like two-way roads). They can also be weighted (`edges` have a cost, like distance or time) or unweighted.

---

Undirected Graph:   A --- B
                    |  \  |
                    C --- D

Directed Graph:     A --> B
                    ^     |
                    |     v
                    C <-- D

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
# Adjacency List representation
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(vertices)} # Adjacency list

    def add_edge(self, u, v, weight=1):
        self.graph[u].append((v, weight))
        # For undirected graph, add: self.graph[v].append((u, weight))

    def print_graph(self):
        for i in range(self.V):
            print(f"Vertex {i}:", end="")
            for neighbor, weight in self.graph[i]:
                print(f" -> ({neighbor}, {weight})", end="")
            print()
```

### Javascript

```javascript
// Adjacency List representation
class Graph {
    constructor(vertices) {
        this.vertices = vertices;
        this.adjacencyList = new Map();

        for (let i = 0; i < vertices; i++) {
            this.adjacencyList.set(i, []);
        }
    }

    addEdge(u, v, weight = 1) {
        this.adjacencyList.get(u).push({ node: v, weight: weight });
        // For undirected graph, add: this.adjacencyList.get(v).push({ node: u, weight: weight });
    }

    printGraph() {
        for (let [vertex, neighbors] of this.adjacencyList) {
            let connections = neighbors.map(n => <code>(${n.node}, ${n.weight})</code>).join(" -> ");
            console.log(<code>Vertex ${vertex}: ${connections}</code>);
        }
    }
}
```

### Cpp

```cpp
#include <iostream>
#include <vector>
#include <list> // For adjacency list

class Graph {
public:
    int V; // Number of vertices
    std::vector<std::list<std::pair<int, int>>> adj; // Adjacency list

    Graph(int vertices) {
        V = vertices;
        adj.resize(V);
    }

    void addEdge(int u, int v, int weight = 1) {
        adj[u].push_back({v, weight});
        // For undirected graph, add: adj[v].push_back({u, weight});
    }

    void printGraph() {
        for (int i = 0; i < V; ++i) {
            std::cout << "Vertex " << i << ":";
            for (auto const& edge : adj[i]) {
                std::cout << " -> (" << edge.first << ", " << edge.second << ")";
            }
            std::cout << std::endl;
        }
    }
};
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

`Graphs` are abstract, so their implementation focuses on how to represent connections between `nodes`.

---

**`Adjacency List` (Python, JavaScript, C++):**
- Uses a `list` (Python, JS) or `vector` (C++) where each `index` represents a `vertex`.
- At each `index`, another `list` (or `std::list` in C++) stores the neighbors of that `vertex`, often as pairs of `(neighbor_node, weight)`.
- `add_edge(u, v, weight)`: Appends the new `edge` to the `adjacency list` of `vertex` `u`. For undirected `graphs`, an `edge` from `v` to `u` is also added.
- `print_graph()`: Iterates through each `vertex` and its `list` of neighbors to display the connections.

[Back to Implementation](#implementation)

