---
title: "Prim"
---

`Prim's Algorithm` is a greedy algorithm that finds a `minimum spanning tree (MST)` for a connected, undirected, weighted graph. An `MST` is a subset of the `edges` of a connected, edge-weighted undirected graph that connects all the `vertices` together, without any `cycles` and with the minimum possible total `edge weight`.

The algorithm starts from an arbitrary `vertex` and grows the `MST` one `edge` at a time. It continuously adds the cheapest `edge` that connects a `vertex` in the growing `MST` to a `vertex` outside the `MST`, without forming a `cycle`.

## How it Works

### How it Works (Expanded)

`Prim's Algorithm` uses a `priority queue` to efficiently select the cheapest `edge` at each step. It maintains a set of `vertices` already included in the `MST` and for all other `vertices`, it stores the minimum `weight edge` connecting them to the `MST`.

---

Example: Finding MST starting from A
Graph: (A,B,4), (A,C,2), (B,C,1), (B,D,5), (C,D,8)

1. Start at A. MST edges: {}. PQ: [(0, A)]. Visited: {}.
2. Pop (0,A). Add A to Visited.
- Neighbors of A: B (cost 4), C (cost 2).
- Push (4,B), (2,C) to PQ. PQ: [(2,C), (4,B)]. Visited: {A}.
3. Pop (2,C). Add C to Visited.
- Neighbors of C: A (cost 2, visited), B (cost 1), D (cost 8).
- Cost to B via C is 1. Min(current B cost 4, new 1) = 1. Update (1,B) in PQ.
- Push (8,D) to PQ. PQ: [(1,B), (4,B - stale), (8,D)]. Visited: {A,C}.
4. Pop (1,B). Add B to Visited.
- Neighbors of B: A (cost 4, visited), C (cost 1, visited), D (cost 5).
- Cost to D via B is 5. Min(current D cost 8, new 5) = 5. Update (5,D) in PQ.
- PQ: [(4,B - stale), (5,D), (8,D - stale)]. Visited: {A,C,B}.
5. Pop (5,D). Add D to Visited.
- MST edges now connect all vertices. Stop.

MST Edges (and total cost): (A,C,2), (C,B,1), (B,D,5) -> Total = 8

## Implementation {#implementation}

### Python

```python
import heapq

def prim_algorithm(graph):
    """
    Finds the Minimum Spanning Tree (MST) of a connected, undirected graph
    using Prim's algorithm.
    <code>graph</code> is an adjacency list: {node: [(neighbor, weight), ...]}</code>
    """
    if not graph:
        return []

    # Start from an arbitrary node (e.g., the first node in the graph)
    start_node = next(iter(graph))
    
    # priority_queue stores (weight, u, v) edges
    priority_queue = []
    
    # visited_nodes tracks nodes included in MST
    visited_nodes = set()
    
    # mst_edges will store the edges of the MST
    mst_edges = []
    
    # To correctly start, add a dummy edge with weight 0 for the start_node
    # or just process its neighbors initially
    # This simplified version just adds all edges from the start_node to PQ
    
    # Add all edges from start_node to the priority queue
    # The format will be (weight, destination_node, source_node_in_mst)
    # This allows tracking the edge that connects to the MST.
    for neighbor, weight in graph[start_node]:
        heapq.heappush(priority_queue, (weight, start_node, neighbor))
    visited_nodes.add(start_node)

    while priority_queue and len(visited_nodes) < len(graph):
        weight, u, v = heapq.heappop(priority_queue)

        if v in visited_nodes:
            continue # Skip if node v is already in MST
        
        visited_nodes.add(v)
        mst_edges.append((u, v, weight))

        # Add all edges from new node v to the priority queue
        for neighbor_of_v, weight_of_edge in graph[v]:
            if neighbor_of_v not in visited_nodes:
                heapq.heappush(priority_queue, (weight_of_edge, v, neighbor_of_v))
                
    # Check if graph was connected
    if len(visited_nodes) != len(graph):
        return "Graph is not connected, MST not possible"

    return mst_edges

# Example
# graph = {
#     'A': [('B', 4), ('C', 2)],
#     'B': [('A', 4), ('C', 1), ('D', 5)],
#     'C': [('A', 2), ('B', 1), ('D', 8)],
#     'D': [('B', 5), ('C', 8)]
# }
# # Expected MST edges (order might vary, total weight 8):
# # [('A', 'C', 2), ('C', 'B', 1), ('B', 'D', 5)]
# print(prim_algorithm(graph))
```

### Javascript

```javascript
// JavaScript doesn't have a built-in Priority Queue.
// This implementation simulates a min-priority queue using an array and sorting,
// which is inefficient for large graphs (O(E log E) or O(E<em>V)).
// For optimal performance, a custom min-heap should be used.

function primAlgorithm(graph) {
    if (Object.keys(graph).length === 0) {
        return [];
    }

    const startNode = Object.keys(graph)[0];
    const visitedNodes = new Set();
    const mstEdges = [];
    
    // priorityQueue stores {weight, fromNode, toNode}
    const priorityQueue = []; 

    // Add all edges from the startNode to the priority queue
    for (const [neighbor, weight] of graph[startNode]) {
        priorityQueue.push({ weight, fromNode: startNode, toNode: neighbor });
    }
    visitedNodes.add(startNode);

    while (priorityQueue.length > 0 && visitedNodes.size < Object.keys(graph).length) {
        // Sort to simulate priority queue (extract min)
        priorityQueue.sort((a, b) => a.weight - b.weight);
        const { weight, fromNode, toNode } = priorityQueue.shift();

        if (visitedNodes.has(toNode)) {
            continue; // Skip if toNode is already in MST
        }
        
        visitedNodes.add(toNode);
        mstEdges.push([fromNode, toNode, weight]);

        // Add all edges from the newly added node (toNode)
        for (const [neighborOfNewNode, weightOfEdge] of graph[toNode]) {
            if (!visitedNodes.has(neighborOfNewNode)) {
                priorityQueue.push({ weight: weightOfEdge, fromNode: toNode, toNode: neighborOfNewNode });
            }
        }
    }
    
    if (visitedNodes.size !== Object.keys(graph).length) {
        return "Graph is not connected, MST not possible";
    }

    return mstEdges;
}

// const graph = {
//     'A': [['B', 4], ['C', 2]],
//     'B': [['A', 4], ['C', 1], ['D', 5]],
//     'C': [['A', 2], ['B', 1], ['D', 8]],
//     'D': [['B', 5], ['C', 8]]
// };
// console.log(primAlgorithm(graph)); // Expected: [['A', 'C', 2], ['C', 'B', 1], ['B', 'D', 5]] (order may vary)
```

### Typescript

```typescript
interface GraphAdjList {
    [node: string]: [string, number][];
}

interface MSTEdge {
    fromNode: string;
    toNode: string;
    weight: number;
}

// This implementation simulates a min-priority queue using an array and sorting,
// which is inefficient for large graphs (O(E log E) or O(E</em>V)).
// For optimal performance, a custom min-heap should be used.

function primAlgorithmTS(graph: GraphAdjList): MSTEdge[] | string {
    if (Object.keys(graph).length === 0) {
        return [];
    }

    const startNode = Object.keys(graph)[0];
    const visitedNodes = new Set<string>();
    const mstEdges: MSTEdge[] = [];
    
    // priorityQueue stores {weight, fromNode, toNode}
    const priorityQueue: MSTEdge[] = []; 

    // Add all edges from the startNode to the priority queue
    for (const [neighbor, weight] of graph[startNode]) {
        priorityQueue.push({ weight, fromNode: startNode, toNode: neighbor });
    }
    visitedNodes.add(startNode);

    while (priorityQueue.length > 0 && visitedNodes.size < Object.keys(graph).length) {
        // Sort to simulate priority queue (extract min)
        priorityQueue.sort((a, b) => a.weight - b.weight);
        const { weight, fromNode, toNode } = priorityQueue.shift()!;

        if (visitedNodes.has(toNode)) {
            continue; // Skip if toNode is already in MST
        }
        
        visitedNodes.add(toNode);
        mstEdges.push({ fromNode, toNode, weight });

        // Add all edges from the newly added node (toNode)
        for (const [neighborOfNewNode, weightOfEdge] of graph[toNode]) {
            if (!visitedNodes.has(neighborOfNewNode)) {
                priorityQueue.push({ weight: weightOfEdge, fromNode: toNode, toNode: neighborOfNewNode });
            }
        }
    }
    
    if (visitedNodes.size !== Object.keys(graph).length) {
        return "Graph is not connected, MST not possible";
    }

    return mstEdges;
}

// const graphTS: GraphAdjList = {
//     'A': [['B', 4], ['C', 2]],
//     'B': [['A', 4], ['C', 1], ['D', 5]],
//     'C': [['A', 2], ['B', 1], ['D', 8]],
//     'D': [['B', 5], ['C', 8]]
// };
// console.log(primAlgorithmTS(graphTS)); // Expected: [{ fromNode: 'A', toNode: 'C', weight: 2 }, ...]
```

### Cpp

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <limits> // For std::numeric_limits

// Edge structure to store in priority queue
struct Edge {
    int weight;
    char u, v; // fromNode, toNode

    // Custom comparator for min-priority queue
    bool operator>(const Edge& other) const {
        return weight > other.weight;
    }
};

using GraphAdjList = std::map<char, std::vector<std::pair<char, int>>>;
using MSTEdges = std::vector<Edge>;

MSTEdges primAlgorithm(const GraphAdjList& graph) {
    if (graph.empty()) {
        return {};
    }

    char startNode = graph.begin()->first;
    
    // Min-priority queue to store edges
    std::priority_queue<Edge, std::vector<Edge>, std::greater<Edge>> pq;
    
    // Set to keep track of visited nodes (nodes already in MST)
    std::set<char> visited_nodes;
    
    MSTEdges mst_edges;
    
    // Add start_node to visited
    visited_nodes.insert(startNode);

    // Add all edges from start_node to the priority queue
    for (const auto& neighbor_pair : graph.at(startNode)) {
        char neighbor = neighbor_pair.first;
        int weight = neighbor_pair.second;
        pq.push({weight, startNode, neighbor});
    }

    while (!pq.empty() && visited_nodes.size() < graph.size()) {
        Edge current_edge = pq.top();
        pq.pop();

        char u = current_edge.u;
        char v = current_edge.v;
        int weight = current_edge.weight;

        if (visited_nodes.count(v)) {
            continue; // Skip if node v is already in MST
        }
        
        visited_nodes.insert(v);
        mst_edges.push_back(current_edge); // Add edge to MST

        // Add all edges from new node v to the priority queue
        auto it = graph.find(v);
        if (it != graph.end()) {
            for (const auto& neighbor_pair : it->second) {
                char neighbor_of_v = neighbor_pair.first;
                int weight_of_edge = neighbor_pair.second;
                if (!visited_nodes.count(neighbor_of_v)) {
                    pq.push({weight_of_edge, v, neighbor_of_v});
                }
            }
        }
    }
    
    if (visited_nodes.size() != graph.size()) {
        // Handle disconnected graph: MST not possible for all vertices
        // For this example, we return empty if not connected.
        return {}; // Or throw an exception
    }

    return mst_edges;
}

// int main() {
//     GraphAdjList graph = {
//         {'A', {{'B', 4}, {'C', 2}}},
//         {'B', {{'A', 4}, {'C', 1}, {'D', 5}}},
//         {'C', {{'A', 2}, {'B', 1}, {'D', 8}}},
//         {'D', {{'B', 5}, {'C', 8}}}
//     };
//     MSTEdges mst = primAlgorithm(graph);
//     for (const auto& edge : mst) {
//         std::cout << edge.u << "-" << edge.v << " (" << edge.weight << ")" << std::endl;
//     }
//     return 0;
// }
```

### Go

```go
package main

import (
    "container/heap"
    "fmt"
)

// Edge for the priority queue
type PrimEdge struct {
    Weight int
    U, V   string // fromNode, toNode
    index  int
}

// A PriorityQueue implements heap.Interface for Prim's
type PrimPriorityQueue []<em>PrimEdge

func (pq PrimPriorityQueue) Len() int { return len(pq) }

func (pq PrimPriorityQueue) Less(i, j int) bool { 
    return pq[i].Weight < pq[j].Weight
}

func (pq PrimPriorityQueue) Swap(i, j int) {
    pq[i], pq[j] = pq[j], pq[i]
    pq[i].index = i
    pq[j].index = j
}

func (pq </em>PrimPriorityQueue) Push(x interface{}) {
    n := len(<em>pq)
    item := x.(</em>PrimEdge)
    item.index = n
    <em>pq = append(</em>pq, item)
}

func (pq <em>PrimPriorityQueue) Pop() interface{} {
    old := </em>pq
    n := len(old)
    item := old[n-1]
    old[n-1] = nil
    item.index = -1
    <em>pq = old[0 : n-1]
    return item
}

func primAlgorithm(graph map[string][][2]interface{}) [][3]interface{} {
    if len(graph) == 0 {
        return nil
    }

    startNode := ""
    for node := range graph { // Get an arbitrary start node
        startNode = node
        break
    }
    
    visitedNodes := make(map[string]bool)
    mstEdges := [][3]interface{}{}
    
    pq := make(PrimPriorityQueue, 0)
    heap.Init(&pq)

    // Add all edges from startNode to the priority queue
    // The format will be (weight, fromNode, toNode)
    visitedNodes[startNode] = true
    for _, edge := range graph[startNode] {
        neighbor := edge[0].(string)
        weight := edge[1].(int)
        heap.Push(&pq, &PrimEdge{Weight: weight, U: startNode, V: neighbor})
    }

    for pq.Len() > 0 && len(visitedNodes) < len(graph) {
        currentEdge := heap.Pop(&pq).(</em>PrimEdge)
        
        u := currentEdge.U
        v := currentEdge.V
        weight := currentEdge.Weight

        if visitedNodes[v] {
            continue // Skip if node v is already in MST
        }
        
        visitedNodes[v] = true
        mstEdges = append(mstEdges, [3]interface{}{u, v, weight})

        // Add all edges from new node v to the priority queue
        for _, edge := range graph[v] {
            neighborOfV := edge[0].(string)
            weightOfEdge := edge[1].(int)
            if !visitedNodes[neighborOfV] {
                heap.Push(&pq, &PrimEdge{Weight: weightOfEdge, U: v, V: neighborOfV})
            }
        }
    }
    
    if len(visitedNodes) != len(graph) {
        // Graph is not connected, MST not possible for all vertices
        return nil
    }

    return mstEdges
}

// func main() {
//     graph := map[string][][2]interface{}{
//         "A": {{"B", 4}, {"C", 2}},
//         "B": {{"A", 4}, {"C", 1}, {"D", 5}},
//         "C": {{"A", 2}, {"B", 1}, {"D", 8}},
//         "D": {{"B", 5}, {"C", 8}},
//     }
//     mst := primAlgorithm(graph)
//     if mst == nil {
//         fmt.Println("Graph is not connected or empty.")
//     } else {
//         for _, edge := range mst {
//             fmt.Printf("%v-%v (%v)\n", edge[0], edge[1], edge[2])
//         }
//     }
// }
```

### D

```d
import std.stdio;
import std.array;
import std.algorithm;
import std.container.binaryheap;
import std.typecons; // For Tuple

// Edge for the priority queue
struct PrimEdge {
    int weight;
    string u, v; // fromNode, toNode

    // Custom comparison for min-priority queue
    int opCmp(const PrimEdge other) const {
        return this.weight.cmp(other.weight);
    }
}

string[][int][string] primAlgorithm(int[][string][string] graph) {
    if (graph.empty) {
        return [];
    }

    // Get an arbitrary start node
    string startNode;
    foreach (node; graph.keys) {
        startNode = node;
        break;
    }
    
    bool[string] visitedNodes;
    string[][int][string] mstEdges; // Stores edges as {fromNode: {toNode: weight}}
    
    // Min-priority queue to store edges
    auto pq = binaryHeap!PrimEdge();

    // Add startNode to visited
    visitedNodes[startNode] = true;

    // Add all edges from startNode to the priority queue
    if (auto pNeighbors = startNode in graph) {
        foreach (neighbor, weight; <em>pNeighbors) {
            pq.insert(PrimEdge(weight, startNode, neighbor));
        }
    }

    while (!pq.empty && visitedNodes.length < graph.keys.length) {
        PrimEdge currentEdge = pq.front;
        pq.removeFront();

        string u = currentEdge.u;
        string v = currentEdge.v;
        int weight = currentEdge.weight;

        if (v in visitedNodes) {
            continue; // Skip if node v is already in MST
        }
        
        visitedNodes[v] = true;
        
        if (mstEdges.length == 0) { // First edge
            mstEdges = [u: [v: weight]];
        } else { // Subsequent edges
            // Need to add edge to a map, not just append
            if (u in mstEdges) {
                mstEdges[u][v] = weight;
            } else {
                mstEdges[u] = [v: weight];
            }
        }

        // Add all edges from new node v to the priority queue
        if (auto pNeighbors = v in graph) {
            foreach (neighborOfV, weightOfEdge; </em>pNeighbors) {
                if (neighborOfV !in visitedNodes) {
                    pq.insert(PrimEdge(weightOfEdge, v, neighborOfV));
                }
            }
        }
    }
    
    if (visitedNodes.length != graph.keys.length) {
        // Graph is not connected, MST not possible for all vertices
        // For this example, we return empty if not connected.
        return null; // Or throw an exception
    }

    return mstEdges;
}

// void main() {
//     auto graph = [
//         "A": ["B": 4, "C": 2],
//         "B": ["A": 4, "C": 1, "D": 5],
//         "C": ["A": 2, "B": 1, "D": 8],
//         "D": ["B": 5, "C": 8]
//     ];
//     auto mst = primAlgorithm(graph);
//     if (mst is null) {
//         writeln("Graph is not connected or empty.");
//     } else {
//         foreach (u, neighbors; mst) {
//             foreach (v, weight; neighbors) {
//                 writefln("%s-%s (%s)", u, v, weight);
//             }
//         }
//     }
// }
```

## Applications

### Application

`Prim's Algorithm` is widely used in various fields where finding the most economical way to connect a set of points is required:
- **Network Design:** Designing telecommunication networks, computer networks, or road networks with minimum cabling or construction costs.
- **Clustering Algorithms:** In data analysis, `Prim's Algorithm` can be adapted to form clusters based on the shortest distances between data points.
- **Circuit Design:** Finding the most efficient way to lay out connections on a circuit board.
- **Image Segmentation:** Used in image processing to group pixels into regions based on intensity differences.
- **Geographic Information Systems (GIS):** Optimizing routes for delivery services, emergency services, or public transport.

