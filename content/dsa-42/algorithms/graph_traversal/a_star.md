---
title: "A* Search"
---

The `A<em> (A-Star) Search Algorithm` is a popular and widely used pathfinding and graph traversal algorithm, known for its performance and accuracy. It is an extension of `Dijkstra's Algorithm`, but it improves upon it by using a `heuristic` to guide its search towards the goal `node`. This makes it significantly faster for finding a single shortest path between two points.

`A</em>` achieves this by combining the cost to reach the current `node` (like Dijkstra's) with an estimated cost from the current `node` to the goal. This "informed search" strategy allows it to prioritize paths that are more likely to be optimal.

## How it Works

### How it Works (Expanded)

`A<em>` maintains a `priority queue` of nodes to visit, but it prioritizes them based on a function `f(n) = g(n) + h(n)`, where:
- `g(n)` is the actual cost of the path from the start `node` to the current `node <code>n`</code>.
- `h(n)` is the **heuristic** estimated cost from the current `node <code>n`</code> to the goal `node`.

The quality of the `heuristic` is crucial. For `A</em>` to find the actual shortest path, the `heuristic` must be **admissible**, meaning it never overestimates the true cost. A common heuristic for grid-based pathfinding is the **Euclidean distance** or **Manhattan distance**.

---

Example: Pathfinding on a grid
- Start at A, Goal at B.
- g(n) = cost of path from A to n.
- h(n) = straight-line distance from n to B.

A<em> will prioritize exploring nodes that have both a low cost to reach (g(n)) and appear to be close to the goal (h(n)).

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
import heapq

# This is a conceptual implementation. A full implementation would need
# a graph representation (e.g., adjacency list) and a heuristic function.
# Here, we assume a grid where nodes are (x, y) tuples.

def heuristic(a, b):
    # Manhattan distance on a grid
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(graph, start, goal):
    """
    Finds the shortest path from start to goal using A</em>.
    <code>graph</code> is a dict of nodes with their neighbors.
    """
    open_set = [(0, start)]  # (f_score, node)
    came_from = {}
    
    g_score = {node: float('infinity') for node in graph}
    g_score[start] = 0
    
    f_score = {node: float('infinity') for node in graph}
    f_score[start] = heuristic(start, goal)

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor in graph[current]:
            # Assume weight between neighbors is 1 for grid
            tentative_g_score = g_score[current] + 1
            
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                if neighbor not in [i[1] for i in open_set]:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None # No path found

# Example
# grid_graph = {
#     (0, 0): [(0, 1), (1, 0)],
#     (0, 1): [(0, 0), (1, 1)],
#     (1, 0): [(0, 0), (1, 1)],
#     (1, 1): [(0, 1), (1, 0)]
# }
# start_node = (0, 0)
# goal_node = (1, 1)
# print(a_star(grid_graph, start_node, goal_node)) # e.g., [(0, 0), (0, 1), (1, 1)]
```

### Javascript

```javascript
// Conceptual A<em> Search in JS. A proper PQ is needed for performance.

function heuristic(a, b) {
    // Manhattan distance
    return Math.abs(a.x - b.x) + Math.abs(a.y - b.y);
}

function aStar(graph, start, goal) {
    const openSet = [{ node: start, fScore: heuristic(start, goal) }];
    const cameFrom = new Map();
    
    const gScore = new Map();
    for (const nodeKey in graph) {
        gScore.set(graph[nodeKey], Infinity);
    }
    gScore.set(start, 0);

    while (openSet.length > 0) {
        // Sort to simulate priority queue (inefficient)
        openSet.sort((a, b) => a.fScore - b.fScore);
        const current = openSet.shift().node;

        if (current === goal) {
            // Reconstruct path
            const path = [current];
            let temp = current;
            while (cameFrom.has(temp)) {
                temp = cameFrom.get(temp);
                path.unshift(temp);
            }
            return path;
        }

        for (const neighbor of graph[current.id]) {
            // Assuming weight is 1
            const tentativeGScore = gScore.get(current) + 1;
            
            if (tentativeGScore < (gScore.get(neighbor) || Infinity)) {
                cameFrom.set(neighbor, current);
                gScore.set(neighbor, tentativeGScore);
                const fScore = tentativeGScore + heuristic(neighbor, goal);
                
                if (!openSet.some(item => item.node === neighbor)) {
                    openSet.push({ node: neighbor, fScore: fScore });
                }
            }
        }
    }
    
    return null; // No path found
}
```

### Typescript

```typescript
interface GridNode {
    id: string;
    x: number;
    y: number;
    neighbors: GridNode[];
}

function heuristicTS(a: GridNode, b: GridNode): number {
    return Math.abs(a.x - b.x) + Math.abs(a.y - b.y);
}

function aStarTS(start: GridNode, goal: GridNode): GridNode[] | null {
    const openSet: { node: GridNode; fScore: number }[] = [{ node: start, fScore: heuristicTS(start, goal) }];
    const cameFrom: Map<GridNode, GridNode> = new Map();
    
    const gScore: Map<GridNode, number> = new Map();
    gScore.set(start, 0);

    while (openSet.length > 0) {
        openSet.sort((a, b) => a.fScore - b.fScore);
        const current = openSet.shift()!.node;

        if (current === goal) {
            const path = [current];
            let temp = current;
            while (cameFrom.has(temp)) {
                temp = cameFrom.get(temp)!;
                path.unshift(temp);
            }
            return path;
        }

        for (const neighbor of current.neighbors) {
            const tentativeGScore = (gScore.get(current) ?? Infinity) + 1;
            
            if (tentativeGScore < (gScore.get(neighbor) ?? Infinity)) {
                cameFrom.set(neighbor, current);
                gScore.set(neighbor, tentativeGScore);
                const fScore = tentativeGScore + heuristicTS(neighbor, goal);
                
                if (!openSet.some(item => item.node === neighbor)) {
                    openSet.push({ node: neighbor, fScore: fScore });
                }
            }
        }
    }
    
    return null;
}
```

### Cpp

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <cmath> // For abs
#include <algorithm> // For std::reverse

// Node for grid-based A</em>
struct Node {
    int y, x;
    bool operator==(const Node& other) const { return y == other.y && x == other.x; }
    bool operator<(const Node& other) const { // For map keys
        return y < other.y || (y == other.y && x < other.x);
    }
};

int heuristic(Node a, Node b) {
    return std::abs(a.x - b.x) + std::abs(a.y - b.y);
}

std::vector<Node> aStar(const std::map<Node, std::vector<Node>>& graph, Node start, Node goal) {
    using PQElement = std::pair<int, Node>;
    std::priority_queue<PQElement, std::vector<PQElement>, std::greater<PQElement>> open_set;

    std::map<Node, Node> came_from;
    std::map<Node, int> g_score;
    for(const auto& pair : graph) {
        g_score[pair.first] = 1e9; // Infinity
    }
    g_score[start] = 0;

    open_set.push({heuristic(start, goal), start});

    while (!open_set.empty()) {
        Node current = open_set.top().second;
        open_set.pop();

        if (current == goal) {
            std::vector<Node> path;
            while (came_from.count(current)) {
                path.push_back(current);
                current = came_from[current];
            }
            path.push_back(start);
            std::reverse(path.begin(), path.end());
            return path;
        }

        for (const auto& neighbor : graph.at(current)) {
            int tentative_g_score = g_score[current] + 1; // Assume weight is 1
            if (tentative_g_score < g_score[neighbor]) {
                came_from[neighbor] = current;
                g_score[neighbor] = tentative_g_score;
                int f_score = tentative_g_score + heuristic(neighbor, goal);
                open_set.push({f_score, neighbor});
            }
        }
    }
    return {}; // No path found
}
```

### Go

```go
package main

import (
    "container/heap"
    "fmt"
    "math"
)

// Node represents a point on a grid
type Node struct {
    X, Y int
}

// Item for the priority queue
type AStarItem struct {
    node   Node
    fScore int
    index  int
}

// AStarPriorityQueue implements heap.Interface
type AStarPriorityQueue []<em>AStarItem

func (pq AStarPriorityQueue) Len() int { return len(pq) }
func (pq AStarPriorityQueue) Less(i, j int) bool { return pq[i].fScore < pq[j].fScore }
func (pq AStarPriorityQueue) Swap(i, j int) {
    pq[i], pq[j] = pq[j], pq[i]
    pq[i].index = i
    pq[j].index = j
}
func (pq </em>AStarPriorityQueue) Push(x interface{}) {
    n := len(<em>pq)
    item := x.(</em>AStarItem)
    item.index = n
    <em>pq = append(</em>pq, item)
}
func (pq <em>AStarPriorityQueue) Pop() interface{} {
    old := </em>pq
    n := len(old)
    item := old[n-1]
    <em>pq = old[0 : n-1]
    return item
}

func heuristic(a, b Node) int {
    return int(math.Abs(float64(a.X-b.X)) + math.Abs(float64(a.Y-b.Y)))
}

func aStar(graph map[Node][]Node, start, goal Node) []Node {
    openSet := &AStarPriorityQueue{}
    heap.Init(openSet)

    cameFrom := make(map[Node]Node)
    gScore := make(map[Node]int)
    for node := range graph {
        gScore[node] = math.MaxInt32
    }
    gScore[start] = 0

    heap.Push(openSet, &AStarItem{node: start, fScore: heuristic(start, goal)})

    for openSet.Len() > 0 {
        current := heap.Pop(openSet).(</em>AStarItem).node

        if current == goal {
            path := []Node{current}
            for {
                prev, ok := cameFrom[current]
                if !ok { break }
                path = append([]Node{prev}, path...)
                current = prev
            }
            return path
        }

        for _, neighbor := range graph[current] {
            tentativeGScore := gScore[current] + 1 // Assume weight 1
            if tentativeGScore < gScore[neighbor] {
                cameFrom[neighbor] = current
                gScore[neighbor] = tentativeGScore
                fScore := tentativeGScore + heuristic(neighbor, goal)
                heap.Push(openSet, &AStarItem{node: neighbor, fScore: fScore})
            }
        }
    }
    return nil // No path
}
```

### D

```d
import std.stdio;
import std.container.binaryheap;
import std.typecons;
import std.math; // For abs

struct Node {
    int y, x;
}

int heuristic(Node a, Node b) {
    return abs(a.x - b.x) + abs(a.y - b.y);
}

Node[] aStar(Node[][Node] graph, Node start, Node goal) {
    alias PQElement = Tuple!(int, "fScore", Node, "node");
    auto openSet = binaryHeap!PQElement((a, b) => a.fScore < b.fScore)();
    
    auto cameFrom = new Node[Node];
    auto gScore = new int[Node];

    foreach(node; graph.keys) {
        gScore[node] = int.max;
    }
    gScore[start] = 0;

    openSet.insert(PQElement(heuristic(start, goal), start));

    while (!openSet.empty) {
        auto current = openSet.front.node;
        openSet.removeFront();

        if (current == goal) {
            Node[] path;
            auto temp = current;
            while(auto p = temp in cameFrom) {
                path ~= temp;
                temp = <em>p;
            }
            path ~= start;
            return path.reverse.array;
        }

        foreach(neighbor; graph[current]) {
            int tentativeGScore = gScore[current] + 1; // Assume weight 1
            if (tentativeGScore < gScore.get(neighbor, int.max)) {
                cameFrom[neighbor] = current;
                gScore[neighbor] = tentativeGScore;
                int fScore = tentativeGScore + heuristic(neighbor, goal);
                openSet.insert(PQElement(fScore, neighbor));
            }
        }
    }
    return []; // No path found
}
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

`A</em>` is an "informed" search algorithm that builds on `Dijkstra's`. It uses a `heuristic` to prioritize nodes that seem closer to the goal.

---

**Key Data Structures:**
- **`openSet` (Priority Queue):** Stores nodes that have been discovered but not yet fully explored. Nodes are prioritized by their `fScore`.
- **`gScore` Map:** Stores the cost of the cheapest path from the start node to each node found so far.
- **`cameFrom` Map:** Stores the preceding node on the cheapest path to the current node. This is used to reconstruct the final path.

**Algorithm Steps:**
- Initialize `gScore` for all nodes to infinity and `gScore[start]` to 0. Add the `start` node to the `openSet` with its initial `fScore` (which is just the heuristic cost).
- **Main Loop:** Continue as long as `openSet` is not empty.
- Extract the node with the lowest `fScore` from `openSet`. This is `current`.
- If `current` is the `goal`, the shortest path has been found. The path is reconstructed by backtracking using the `cameFrom` map.
- For each `neighbor` of `current`:
- Calculate `tentative_gScore`, the cost to reach the `neighbor` via `current`.
- If this `tentative_gScore` is better (lower) than the `gScore` currently recorded for the `neighbor`, it means we've found a better path.
- Update the `neighbor`'s records: set `cameFrom` to `current`, update its `gScore`, and calculate its new `fScore`.
- Add the `neighbor` to the `openSet` so it can be explored later.

            </li>

    </li>
- If the loop finishes without reaching the goal, no path exists.

[Back to Implementation](#implementation)

## Applications

### Application

`A*` is the go-to algorithm for pathfinding in many applications, especially where the search space is large and a good heuristic is available.
- **Video Games:** The most common use case is for character and AI navigation in games. It's used to find paths around obstacles on a grid or navigation mesh.
- **Robotics and Autonomous Vehicles:** Used for path planning, from warehouse robots to self-driving cars.
- **Network Routing:** Can be used for finding optimal paths in computer networks, though other algorithms like Dijkstra's are also common.
- **Natural Language Processing:** Used in some parsing and machine translation algorithms where finding the "best" sequence of operations is required.
- **Computational Biology:** For sequence alignment problems.

