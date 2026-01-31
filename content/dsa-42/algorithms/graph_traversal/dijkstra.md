---
title: "Dijkstra"
---

`Dijkstra's Algorithm` is a classic and widely used algorithm for finding the shortest paths between `nodes` in a graph, which may represent, for example, road networks. It was conceived by computer scientist Edsger W. Dijkstra in 1956. The algorithm finds the shortest path from a given "source" `node` to all other _nodes_ in a weighted graph with non-negative edge weights.

It works by maintaining a set of visited `nodes` and their shortest known distances from the source. It iteratively selects the unvisited `node` with the smallest known distance, marks it as visited, and updates the distances of its neighbors.

## How it Works

### How it Works (Expanded)

`Dijkstra's Algorithm` uses a `priority queue` to efficiently select the unvisited `node` with the smallest distance at each step. This ensures that once a _node_ is marked as visited, the path found to it is the shortest possible one.

---

Example: Find shortest paths from A
Graph: A-B(1), A-C(4), B-C(2), B-D(5), C-D(1)

1. Start at A. Distances: {A:0, B:inf, C:inf, D:inf}. Priority Queue (PQ): [(0,A)].
2. Pop (0,A). Path to A is 0.
- Visit neighbors B, C.
- Update dist(B): 0+1=1. Push (1,B) to PQ.
- Update dist(C): 0+4=4. Push (4,C) to PQ.
- PQ: [(1,B), (4,C)].
3. Pop (1,B). Path to B is 1.
- Visit neighbors C, D.
- Update dist(C): 1+2=3 < 4. Update. Push (3,C) to PQ.
- Update dist(D): 1+5=6. Push (6,D) to PQ.
- PQ: [(3,C), (4,C - stale), (6,D)].
4. Pop (3,C). Path to C is 3.
- Visit neighbor D.
- Update dist(D): 3+1=4 < 6. Update. Push (4,D) to PQ.
- PQ: [(4,C), (4,D), (6,D - stale)].
5. Pop (4,C). C already visited with shorter path. Ignore.
6. Pop (4,D). Path to D is 4.
- All neighbors visited.
7. ... and so on until PQ is empty.

Final shortest paths from A: A:0, B:1, C:3, D:4

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
import heapq

def dijkstra(graph, start_node):
    """
    Finds the shortest paths from a start_node to all other nodes in a weighted graph.
    <code>graph</code> is a dict of dicts: {node: {neighbor: weight}}.
    """
    distances = {node: float('infinity') for node in graph}
    distances[start_node] = 0
    
    priority_queue = [(0, start_node)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Nodes can be added to the priority queue multiple times. We only
        # process a node the first time we remove it from the priority queue.
        if current_distance > distances[current_node]:
            continue
            
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # If we found a shorter path to the neighbor
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

# Example
# graph = {
#     'A': {'B': 1, 'C': 4},
#     'B': {'A': 1, 'C': 2, 'D': 5},
#     'C': {'A': 4, 'B': 2, 'D': 1},
#     'D': {'B': 5, 'C': 1}
# }
# print(dijkstra(graph, 'A')) # {'A': 0, 'B': 1, 'C': 3, 'D': 4}
```

### Javascript

```javascript
// JavaScript doesn't have a built-in Priority Queue, so a simple array-based one is used.
// For production, a library like 'tinyqueue' or a custom min-heap implementation is better.

function dijkstra(graph, startNode) {
    const distances = {};
    const visited = new Set();
    const pq = []; // Simple priority queue (array)

    // Initialize distances
    for (const node in graph) {
        distances[node] = Infinity;
    }
    distances[startNode] = 0;
    
    pq.push({ node: startNode, distance: 0 });

    while (pq.length > 0) {
        // Sort to simulate priority queue (inefficient but simple for demo)
        pq.sort((a, b) => a.distance - b.distance);
        const { node: currentNode, distance: currentDistance } = pq.shift();

        if (visited.has(currentNode)) {
            continue;
        }
        visited.add(currentNode);

        if (currentDistance > distances[currentNode]) {
            continue;
        }

        const neighbors = graph[currentNode] || {};
        for (const neighbor in neighbors) {
            const weight = neighbors[neighbor];
            const distance = currentDistance + weight;

            if (distance < distances[neighbor]) {
                distances[neighbor] = distance;
                pq.push({ node: neighbor, distance: distance });
            }
        }
    }
    
    return distances;
}

// const graph = {
//     'A': { 'B': 1, 'C': 4 },
//     'B': { 'A': 1, 'C': 2, 'D': 5 },
//     'C': { 'A': 4, 'B': 2, 'D': 1 },
//     'D': { 'B': 5, 'C': 1 }
// };
// console.log(dijkstra(graph, 'A')); // { A: 0, B: 1, C: 3, D: 4 }
```

### Typescript

```typescript
interface Graph {
    [key: string]: { [key: string]: number };
}

interface Distance {
    [key: string]: number;
}

interface PQNode {
    node: string;
    distance: number;
}

function dijkstraTS(graph: Graph, startNode: string): Distance {
    const distances: Distance = {};
    const visited: Set<string> = new Set();
    const pq: PQNode[] = []; // Simple priority queue (array)

    // Initialize distances
    for (const node in graph) {
        distances[node] = Infinity;
    }
    distances[startNode] = 0;
    
    pq.push({ node: startNode, distance: 0 });

    while (pq.length > 0) {
        // Sort to simulate priority queue
        pq.sort((a, b) => a.distance - b.distance);
        const { node: currentNode, distance: currentDistance } = pq.shift()!;

        if (visited.has(currentNode)) {
            continue;
        }
        visited.add(currentNode);

        if (currentDistance > distances[currentNode]) {
            continue;
        }

        const neighbors = graph[currentNode] || {};
        for (const neighbor in neighbors) {
            const weight = neighbors[neighbor];
            const distance = currentDistance + weight;

            if (distance < distances[neighbor]) {
                distances[neighbor] = distance;
                pq.push({ node: neighbor, distance: distance });
            }
        }
    }
    
    return distances;
}

// const graphTS: Graph = {
//     'A': { 'B': 1, 'C': 4 },
//     'B': { 'A': 1, 'C': 2, 'D': 5 },
//     'C': { 'A': 4, 'B': 2, 'D': 1 },
//     'D': { 'B': 5, 'C': 1 }
// };
// console.log(dijkstraTS(graphTS, 'A')); // { A: 0, B: 1, C: 3, D: 4 }
```

### Cpp

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <limits> // For std::numeric_limits
#include <utility> // For std::pair

using Graph = std::map<char, std::map<char, int>>;
using Distances = std::map<char, int>;

Distances dijkstra(const Graph& graph, char startNode) {
    Distances distances;
    for (const auto& pair : graph) {
        distances[pair.first] = std::numeric_limits<int>::max();
    }
    distances[startNode] = 0;

    using PQElement = std::pair<int, char>;
    std::priority_queue<PQElement, std::vector<PQElement>, std::greater<PQElement>> pq;
    
    pq.push({0, startNode});

    while (!pq.empty()) {
        int currentDistance = pq.top().first;
        char currentNode = pq.top().second;
        pq.pop();

        if (currentDistance > distances[currentNode]) {
            continue;
        }

        auto it = graph.find(currentNode);
        if (it != graph.end()) {
            for (const auto& neighbor_pair : it->second) {
                char neighbor = neighbor_pair.first;
                int weight = neighbor_pair.second;
                int distance = currentDistance + weight;

                if (distance < distances[neighbor]) {
                    distances[neighbor] = distance;
                    pq.push({distance, neighbor});
                }
            }
        }
    }

    return distances;
}

// int main() {
//     Graph graph = {
//         {'A', {{'B', 1}, {'C', 4}}},
//         {'B', {{'A', 1}, {'C', 2}, {'D', 5}}},
//         {'C', {{'A', 4}, {'B', 2}, {'D', 1}}},
//         {'D', {{'B', 5}, {'C', 1}}}
//     };
//     Distances result = dijkstra(graph, 'A');
//     for (const auto& pair : result) {
//         std::cout << pair.first << ": " << pair.second << std::endl;
//     }
// }
```

### Go

```go
package main

import (
    "container/heap"
    "fmt"
    "math"
)

// Item for the priority queue
type Item struct {
    node     string
    distance int
    index    int // Index of the item in the heap
}

// A PriorityQueue implements heap.Interface and holds Items.
type PriorityQueue []<em>Item

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
    return pq[i].distance < pq[j].distance
}

func (pq PriorityQueue) Swap(i, j int) {
    pq[i], pq[j] = pq[j], pq[i]
    pq[i].index = i
    pq[j].index = j
}

func (pq </em>PriorityQueue) Push(x interface{}) {
    n := len(<em>pq)
    item := x.(</em>Item)
    item.index = n
    <em>pq = append(</em>pq, item)
}

func (pq <em>PriorityQueue) Pop() interface{} {
    old := </em>pq
    n := len(old)
    item := old[n-1]
    old[n-1] = nil  // avoid memory leak
    item.index = -1 // for safety
    <em>pq = old[0 : n-1]
    return item
}

func dijkstra(graph map[string]map[string]int, startNode string) map[string]int {
    distances := make(map[string]int)
    for node := range graph {
        distances[node] = math.MaxInt32
    }
    distances[startNode] = 0

    pq := make(PriorityQueue, 0)
    heap.Init(&pq)
    
    heap.Push(&pq, &Item{node: startNode, distance: 0})

    for pq.Len() > 0 {
        currentItem := heap.Pop(&pq).(</em>Item)
        currentNode := currentItem.node
        currentDistance := currentItem.distance

        if currentDistance > distances[currentNode] {
            continue
        }

        for neighbor, weight := range graph[currentNode] {
            distance := currentDistance + weight
            if distance < distances[neighbor] {
                distances[neighbor] = distance
                heap.Push(&pq, &Item{node: neighbor, distance: distance})
            }
        }
    }

    return distances
}

// func main() {
//     graph := map[string]map[string]int{
//         "A": {"B": 1, "C": 4},
//         "B": {"A": 1, "C": 2, "D": 5},
//         "C": {"A": 4, "B": 2, "D": 1},
//         "D": {"B": 5, "C": 1},
//     }
//     fmt.Println(dijkstra(graph, "A")) // map[A:0 B:1 C:3 D:4]
// }
```

### D

```d
import std.stdio;
import std.container.binaryheap;
import std.typecons;
import std.experimental.allocator;

auto dijkstra(int[string][string] graph, string startNode) {
    auto distances = new int[string];
    foreach (node; graph.keys) {
        distances[node] = int.max;
    }
    distances[startNode] = 0;

    alias PQElement = Tuple!(int, "distance", string, "node");
    auto pq = binaryHeap!PQElement((a, b) => a.distance < b.distance)();

    pq.insert(PQElement(0, startNode));
    
    auto visited = new bool[string];

    while (!pq.empty) {
        auto current = pq.front;
        pq.removeFront();

        int currentDistance = current.distance;
        string currentNode = current.node;

        if (currentNode in visited) continue;
        visited[currentNode] = true;
        
        if (currentDistance > distances[currentNode]) continue;

        if (auto pNeighbors = currentNode in graph) {
            foreach (neighbor, weight; *pNeighbors) {
                int distance = currentDistance + weight;
                if (distance < distances[neighbor]) {
                    distances[neighbor] = distance;
                    pq.insert(PQElement(distance, neighbor));
                }
            }
        }
    }

    return distances;
}

// void main() {
//     auto graph = [
//         "A": ["B": 1, "C": 4],
//         "B": ["A": 1, "C": 2, "D": 5],
//         "C": ["A": 4, "B": 2, "D": 1],
//         "D": ["B": 5, "C": 1]
//     ];
//     auto result = dijkstra(graph, "A");
//     writeln(result); // ["D":4, "C":3, "B":1, "A":0]
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

`Dijkstra's Algorithm` is most efficiently implemented using a `priority queue` to store unvisited nodes, prioritized by their current shortest distance from the source.

---

**Initialization:**
- A `distances` map or dictionary is created to store the shortest distance found so far from the `startNode` to every other `node`. It's initialized with `infinity` for all nodes except the `startNode`, which is 0.
- A `priority queue` (`pq`) is created. It will store pairs of `(distance, node)`. In languages without a native min-priority queue (like JavaScript), this is often simulated with a sorted array for simplicity, though a heap is far more efficient.
- The starting pair `(0, startNode)` is added to the `pq`.

**Main Loop:**
- The loop continues as long as the `pq` is not empty.
- **Extract Min:** The element with the smallest distance is extracted from the `pq`. This is `currentNode`.
- **Skip Stale Entries:** A crucial optimization is to check if the extracted `currentDistance` is greater than the `distance` already stored for `currentNode`. If it is, it means we've found a shorter path to this `node` already, so we can ignore this "stale" entry in the `pq` and continue.
- **Explore Neighbors:** For each `neighbor` of `currentNode`, calculate the new potential distance (`currentDistance + weight`).
- **Update and Enqueue:** If this new `distance` is shorter than the known `distance` to the `neighbor`, update the `distances` map and add the new, better path `(distance, neighbor)` to the `pq`.

[Back to Implementation](#implementation)

## Applications

### Application

`Dijkstra's Algorithm` is fundamental to solving shortest path problems in various domains, provided the edge weights are non-negative.
- **Routing and Navigation:** Used in GPS systems and network routing protocols (like OSPF) to find the shortest path between two points.
- **Network Analysis:** Finding the cheapest or fastest way to send data through a computer network.
- **Robotics and AI:** Pathfinding for autonomous vehicles or characters in a game world.
- **Bioinformatics:** Finding optimal alignments or pathways in metabolic networks.
- **Social Network Analysis:** Calculating the "degree of separation" between people.

