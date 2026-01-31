---
title: "Interval Tree"
---

An `Interval Tree` is a tree data structure that efficiently stores intervals and allows for quick querying of all intervals that overlap with a given point or another interval. It is particularly useful when dealing with datasets that have many overlapping intervals, such as in scheduling applications, genomic data analysis, or event management.

It is typically built upon a balanced `binary search tree`, where each `node` is augmented with additional information about the `intervals` in its subtree to speed up queries.

## How it Works

### How it Works (Expanded)

An `Interval Tree` augments a balanced `BST` structure. Each `node` in the `tree` stores:
- A "center" point: The midpoint or endpoint of some interval.
- A `list` of `intervals` that "stab" (contain) the center point.
- A `left subtree` containing `intervals` completely to the `left` of the center point.
- A `right subtree` containing `intervals` completely to the `right` of the center point.

---

Example: Interval Tree for intervals [1,5], [2,6], [4,8], [9,12]

Center 7: (for entire range [1,12])
 Intervals: None stab 7
 Left subtree (for [1,6]):
  Center 4:
   Intervals: [1,5], [2,6], [4,8] (all stab 4)
   Left subtree (for [1,3]): ...
   Right subtree (for [5,6]): ...
 Right subtree (for [8,12]):
  Center 10:
   Intervals: [9,12] (stabs 10)
   Left subtree (for [8,9]): ...
   Right subtree (for [11,12]): ...

## Implementation {#implementation}

### Python

```python
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def overlaps(self, other_interval):
        return self.start <= other_interval.end and self.end >= other_interval.start

class IntervalTreeNode:
    def __init__(self, center):
        self.center = center
        self.intervals_left = []  # Intervals that start left of center and end right of center
        self.intervals_right = [] # Intervals that start left of center and end right of center
                                  # Sorted by start point for intervals_left, by end point for intervals_right
        self.left_child = None
        self.right_child = None
        # Max end point in this subtree, useful for optimizing queries
        self.max_end = -float('inf') 

class IntervalTree:
    def __init__(self):
        self.root = None

    def insert(self, root, interval):
        if not root:
            # Pick the midpoint of the interval as the center for the root node
            # For simplicity, we'll pick the start of the interval being inserted as the center
            # A more robust approach would use a global median or a balanced BST
            new_node = IntervalTreeNode(interval.start) 
            new_node.max_end = interval.end
            new_node.intervals_left.append(interval)
            return new_node
        
        root.max_end = max(root.max_end, interval.end)

        if interval.end < root.center:
            root.left_child = self.insert(root.left_child, interval)
        elif interval.start > root.center:
            root.right_child = self.insert(root.right_child, interval)
        else: # Interval overlaps the center
            root.intervals_left.append(interval)
            root.intervals_right.append(interval)
            # Sorting these lists helps with query speed
            root.intervals_left.sort(key=lambda i: i.start)
            root.intervals_right.sort(key=lambda i: i.end, reverse=True)
        return root

    def query(self, root, query_interval):
        if not root or query_interval.start > root.max_end: # Pruning optimization
            return []
        
        results = []

        # Query intervals_left (overlapping to the right of query_interval.start)
        for interval in root.intervals_left:
            if interval.overlaps(query_interval):
                results.append(interval)
            elif interval.start > query_interval.end: # Optimization: intervals_left sorted by start
                break # No more overlaps possible in this direction
        
        if query_interval.start < root.center:
            results.extend(self.query(root.left_child, query_interval))
        
        if query_interval.end > root.center:
            results.extend(self.query(root.right_child, query_interval))
            
        return results

# Example Usage:
# tree = IntervalTree()
# root_node = None
# intervals = [
#     Interval(1, 5), Interval(2, 6), Interval(4, 8),
#     Interval(9, 12), Interval(10, 14), Interval(0, 3)
# ]
# for i in intervals:
#     root_node = tree.insert(root_node, i)

# query_int = Interval(3, 7)
# overlaps = tree.query(root_node, query_int)
# print(f"Intervals overlapping with [{query_int.start}, {query_int.end}]:")
# for o in overlaps:
#     print(f"[{o.start}, {o.end}]") # Expected: [1,5], [2,6], [4,8]
```

### Javascript

```javascript
class Interval {
    constructor(start, end) {
        this.start = start;
        this.end = end;
    }

    overlaps(otherInterval) {
        return this.start <= otherInterval.end && this.end >= otherInterval.start;
    }
}

class IntervalTreeNode {
    constructor(center) {
        this.center = center;
        this.intervalsLeft = []; // Intervals that start left of center and end right of center
        this.intervalsRight = []; // Intervals that start left of center and end right of center
        this.leftChild = null;
        this.rightChild = null;
        this.maxEnd = -Infinity; // Max end point in this subtree, useful for optimizing queries
    }
}

class IntervalTree {
    constructor() {
        this.root = null;
    }

    insert(root, interval) {
        if (!root) {
            const newNode = new IntervalTreeNode(interval.start);
            newNode.maxEnd = interval.end;
            newNode.intervalsLeft.push(interval);
            return newNode;
        }
        
        root.maxEnd = Math.max(root.maxEnd, interval.end);

        if (interval.end < root.center) {
            root.leftChild = this.insert(root.leftChild, interval);
        } else if (interval.start > root.center) {
            root.rightChild = this.insert(root.rightChild, interval);
        } else { // Interval overlaps the center
            root.intervalsLeft.push(interval);
            root.intervalsRight.push(interval);
            root.intervalsLeft.sort((a, b) => a.start - b.start);
            root.intervalsRight.sort((a, b) => b.end - a.end); // Descending for faster overlap checks
        }
        return root;
    }

    query(root, queryInterval) {
        if (!root || queryInterval.start > root.maxEnd) { // Pruning optimization
            return [];
        }
        
        let results = [];

        // Query intervalsLeft
        for (const interval of root.intervalsLeft) {
            if (interval.overlaps(queryInterval)) {
                results.push(interval);
            } else if (interval.start > queryInterval.end) {
                break; // Optimization: intervalsLeft sorted by start
            }
        }
        
        if (queryInterval.start < root.center) {
            results = results.concat(this.query(root.leftChild, queryInterval));
        }
        
        if (queryInterval.end > root.center) {
            results = results.concat(this.query(root.rightChild, queryInterval));
        }
        
        return results;
    }
}

// const tree = new IntervalTree();
// let rootNode = null;
// const intervals = [
//     new Interval(1, 5), new Interval(2, 6), new Interval(4, 8),
//     new Interval(9, 12), new Interval(10, 14), new Interval(0, 3)
// ];
// for (const i of intervals) {
//     rootNode = tree.insert(rootNode, i);
// }

// const queryInt = new Interval(3, 7);
// const overlaps = tree.query(rootNode, queryInt);
// console.log(<code>Intervals overlapping with [${queryInt.start}, ${queryInt.end}]:</code>);
// for (const o of overlaps) {
//     console.log(<code>[${o.start}, ${o.end}]</code>); // Expected: [1,5], [2,6], [4,8]
// }
```

### Typescript

```typescript
class IntervalTS {
    constructor(public start: number, public end: number) {}

    overlaps(otherInterval: IntervalTS): boolean {
        return this.start <= otherInterval.end && this.end >= otherInterval.start;
    }
}

class IntervalTreeNodeTS {
    public center: number;
    public intervalsLeft: IntervalTS[];
    public intervalsRight: IntervalTS[];
    public leftChild: IntervalTreeNodeTS | null = null;
    public rightChild: IntervalTreeNodeTS | null = null;
    public maxEnd: number;

    constructor(center: number) {
        this.center = center;
        this.intervalsLeft = [];
        this.intervalsRight = [];
        this.maxEnd = -Infinity;
    }
}

class IntervalTreeTS {
    public root: IntervalTreeNodeTS | null = null;

    public insert(rootNode: IntervalTreeNodeTS | null, interval: IntervalTS): IntervalTreeNodeTS {
        if (!rootNode) {
            const newNode = new IntervalTreeNodeTS(interval.start);
            newNode.maxEnd = interval.end;
            newNode.intervalsLeft.push(interval);
            return newNode;
        }
        
        rootNode.maxEnd = Math.max(rootNode.maxEnd, interval.end);

        if (interval.end < rootNode.center) {
            rootNode.leftChild = this.insert(rootNode.leftChild, interval);
        } else if (interval.start > rootNode.center) {
            rootNode.rightChild = this.insert(rootNode.rightChild, interval);
        } else {
            rootNode.intervalsLeft.push(interval);
            rootNode.intervalsRight.push(interval);
            rootNode.intervalsLeft.sort((a, b) => a.start - b.start);
            rootNode.intervalsRight.sort((a, b) => b.end - a.end);
        }
        return rootNode;
    }

    public query(rootNode: IntervalTreeNodeTS | null, queryInterval: IntervalTS): IntervalTS[] {
        if (!rootNode || queryInterval.start > rootNode.maxEnd) {
            return [];
        }
        
        let results: IntervalTS[] = [];

        for (const interval of rootNode.intervalsLeft) {
            if (interval.overlaps(queryInterval)) {
                results.push(interval);
            } else if (interval.start > queryInterval.end) {
                break;
            }
        }
        
        if (queryInterval.start < rootNode.center) {
            results = results.concat(this.query(rootNode.leftChild, queryInterval));
        }
        
        if (queryInterval.end > rootNode.center) {
            results = results.concat(this.query(rootNode.rightChild, queryInterval));
        }
        
        return results;
    }
}

// const treeTS = new IntervalTreeTS();
// let rootNodeTS: IntervalTreeNodeTS | null = null;
// const intervalsTS: IntervalTS[] = [
//     new IntervalTS(1, 5), new IntervalTS(2, 6), new IntervalTS(4, 8),
//     new IntervalTS(9, 12), new IntervalTS(10, 14), new IntervalTS(0, 3)
// ];
// for (const i of intervalsTS) {
//     rootNodeTS = treeTS.insert(rootNodeTS, i);
// }

// const queryIntTS = new IntervalTS(3, 7);
// const overlapsTS = treeTS.query(rootNodeTS, queryIntTS);
// console.log(<code>Intervals overlapping with [${queryIntTS.start}, ${queryIntTS.end}]:</code>);
// for (const o of overlapsTS) {
//     console.log(<code>[${o.start}, ${o.end}]</code>); // Expected: [1,5], [2,6], [4,8]
// }
```

### Cpp

```cpp
#include <iostream>
#include <vector>
#include <algorithm> // For std::max, std::sort
#include <limits>    // For std::numeric_limits

class Interval {
public:
    int start;
    int end;

    Interval(int s, int e) : start(s), end(e) {}

    bool overlaps(const Interval& other_interval) const {
        return start <= other_interval.end && end >= other_interval.start;
    }
};

class IntervalTreeNode {
public:
    int center;
    std::vector<Interval> intervals_left; // Intervals that start left of center and end right of center
    std::vector<Interval> intervals_right; // Intervals that start left of center and end right of center
    IntervalTreeNode<em> left_child;
    IntervalTreeNode</em> right_child;
    int max_end; // Max end point in this subtree, useful for optimizing queries

    IntervalTreeNode(int c) : center(c), left_child(nullptr), right_child(nullptr), max_end(std::numeric_limits<int>::min()) {}

    ~IntervalTreeNode() {
        delete left_child;
        delete right_child;
    }
};

class IntervalTree {
public:
    IntervalTreeNode<em> root;

    IntervalTree() : root(nullptr) {}
    ~IntervalTree() {
        delete root;
    }

    IntervalTreeNode</em> insert(IntervalTreeNode<em> node, const Interval& interval) {
        if (node == nullptr) {
            // For simplicity, pick the interval's start as center if node is null
            // A more robust approach would dynamically pick a center
            IntervalTreeNode</em> new_node = new IntervalTreeNode(interval.start);
            new_node->max_end = interval.end;
            new_node->intervals_left.push_back(interval);
            return new_node;
        }
        
        node->max_end = std::max(node->max_end, interval.end);

        if (interval.end < node->center) {
            node->left_child = insert(node->left_child, interval);
        } else if (interval.start > node->center) {
            node->right_child = insert(node->right_child, interval);
        } else { // Interval overlaps the center
            node->intervals_left.push_back(interval);
            node->intervals_right.push_back(interval);
            // Sorting these lists helps with query speed
            std::sort(node->intervals_left.begin(), node->intervals_left.end(), 
                      [](const Interval& a, const Interval& b){ return a.start < b.start; });
            std::sort(node->intervals_right.begin(), node->intervals_right.end(), 
                      [](const Interval& a, const Interval& b){ return a.end > b.end; }); // Descending
        }
        return node;
    }

    std::vector<Interval> query(IntervalTreeNode<em> node, const Interval& query_interval) {
        std::vector<Interval> results;
        if (node == nullptr || query_interval.start > node->max_end) { // Pruning optimization
            return results;
        }
        
        // Query intervals_left (overlapping to the right of query_interval.start)
        for (const auto& interval : node->intervals_left) {
            if (interval.overlaps(query_interval)) {
                results.push_back(interval);
            } else if (interval.start > query_interval.end) { // Optimization: intervals_left sorted by start
                break; 
            }
        }
        
        if (query_interval.start < node->center) {
            std::vector<Interval> left_results = query(node->left_child, query_interval);
            results.insert(results.end(), left_results.begin(), left_results.end());
        }
        
        if (query_interval.end > node->center) {
            std::vector<Interval> right_results = query(node->right_child, query_interval);
            results.insert(results.end(), right_results.begin(), right_results.end());
        }
        
        return results;
    }
};

// int main() {
//     IntervalTree tree;
//     std::vector<Interval> intervals_to_insert = {
//         Interval(1, 5), Interval(2, 6), Interval(4, 8),
//         Interval(9, 12), Interval(10, 14), Interval(0, 3)
//     };
//     for (const auto& i : intervals_to_insert) {
//         tree.root = tree.insert(tree.root, i);
//     }

//     Interval query_int(3, 7);
//     std::vector<Interval> overlaps = tree.query(tree.root, query_int);
//     std::cout << "Intervals overlapping with [" << query_int.start << ", " << query_int.end << "]:
";
//     for (const auto& o : overlaps) {
//         std::cout << "[" << o.start << ", " << o.end << "]" << std::endl; // Expected: [1,5], [2,6], [4,8]
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
    "sort"
)

type Interval struct {
    Start int
    End   int
}

func (i Interval) Overlaps(otherInterval Interval) bool {
    return i.Start <= otherInterval.End && i.End >= otherInterval.Start
}

type IntervalTreeNode struct {
    Center        int
    IntervalsLeft []Interval // Intervals that start left of center and end right of center
    IntervalsRight []Interval // Intervals that start left of center and end right of center
    LeftChild     </em>IntervalTreeNode
    RightChild    <em>IntervalTreeNode
    MaxEnd        int // Max end point in this subtree, useful for optimizing queries
}

func NewIntervalTreeNode(center int) </em>IntervalTreeNode {
    return &IntervalTreeNode{
        Center:        center,
        IntervalsLeft:  []Interval{},
        IntervalsRight: []Interval{},
        MaxEnd:        math.MinInt32,
    }
}

type IntervalTree struct {
    Root <em>IntervalTreeNode
}

func (t </em>IntervalTree) Insert(node <em>IntervalTreeNode, interval Interval) </em>IntervalTreeNode {
    if node == nil {
        newNode := NewIntervalTreeNode(interval.Start)
        newNode.MaxEnd = interval.End
        newNode.IntervalsLeft = append(newNode.IntervalsLeft, interval)
        return newNode
    }

    node.MaxEnd = int(math.Max(float64(node.MaxEnd), float64(interval.End)))

    if interval.End < node.Center {
        node.LeftChild = t.Insert(node.LeftChild, interval)
    } else if interval.Start > node.Center {
        node.RightChild = t.Insert(node.RightChild, interval)
    } else { // Interval overlaps the center
        node.IntervalsLeft = append(node.IntervalsLeft, interval)
        node.IntervalsRight = append(node.IntervalsRight, interval)
        sort.Slice(node.IntervalsLeft, func(i, j int) bool {
            return node.IntervalsLeft[i].Start < node.IntervalsLeft[j].Start
        })
        sort.Slice(node.IntervalsRight, func(i, j int) bool {
            return node.IntervalsRight[i].End > node.IntervalsRight[j].End
        }) // Descending
    }
    return node
}

func (t <em>IntervalTree) Query(node </em>IntervalTreeNode, queryInterval Interval) []Interval {
    var results []Interval
    if node == nil || queryInterval.Start > node.MaxEnd {
        return results
    }

    // Query IntervalsLeft
    for _, interval := range node.IntervalsLeft {
        if interval.Overlaps(queryInterval) {
            results = append(results, interval)
        } else if interval.Start > queryInterval.End {
            break // Optimization: IntervalsLeft sorted by Start
        }
    }

    if queryInterval.Start < node.Center {
        results = append(results, t.Query(node.LeftChild, queryInterval)...)
    }

    if queryInterval.End > node.Center {
        results = append(results, t.Query(node.RightChild, queryInterval)...)
    }

    return results
}

// func main() {
//     tree := &IntervalTree{}
//     intervals := []Interval{
//         {1, 5}, {2, 6}, {4, 8},
//         {9, 12}, {10, 14}, {0, 3},
//     }
//     for _, i := range intervals {
//         tree.Root = tree.Insert(tree.Root, i)
//     }

//     queryInt := Interval{3, 7}
//     overlaps := tree.Query(tree.Root, queryInt)
//     fmt.Printf("Intervals overlapping with [%d, %d]:\n", queryInt.Start, queryInt.End)
//     for _, o := range overlaps {
//         fmt.Printf("[%d, %d]\n", o.Start, o.End) // Expected: [1,5], [2,6], [4,8]
//     }
// }
```

### D

```d
import std.stdio;
import std.algorithm;
import std.array;
import std.container.array;
import std.math; // For real.max

class Interval {
    int start;
    int end;

    this(int s, int e) {
        start = s;
        end = e;
    }

    bool overlaps(Interval other_interval) {
        return this.start <= other_interval.end && this.end >= other_interval.start;
    }
}

class IntervalTreeNode {
    int center;
    Interval[] intervals_left;  // Intervals that start left of center and end right of center
    Interval[] intervals_right; // Intervals that start left of center and end right of center
    IntervalTreeNode left_child;
    IntervalTreeNode right_child;
    int max_end; // Max end point in this subtree, useful for optimizing queries

    this(int c) {
        center = c;
        intervals_left = [];
        intervals_right = [];
        left_child = null;
        right_child = null;
        max_end = int.min;
    }
}

class IntervalTree {
    IntervalTreeNode root;

    this() {
        root = null;
    }

    IntervalTreeNode insert(IntervalTreeNode node, Interval interval) {
        if (node is null) {
            // For simplicity, pick the interval's start as center if node is null
            IntervalTreeNode new_node = new IntervalTreeNode(interval.start);
            new_node.max_end = interval.end;
            new_node.intervals_left ~= interval;
            return new_node;
        }
        
        node.max_end = max(node.max_end, interval.end);

        if (interval.end < node.center) {
            node.left_child = insert(node.left_child, interval);
        } else if (interval.start > node.center) {
            node.right_child = insert(node.right_child, interval);
        } else { // Interval overlaps the center
            node.intervals_left ~= interval;
            node.intervals_right ~= interval;
            node.intervals_left.sort!((a, b) => a.start < b.start);
            node.intervals_right.sort!((a, b) => a.end > b.end); // Descending
        }
        return node;
    }

    Interval[] query(IntervalTreeNode node, Interval query_interval) {
        Interval[] results = [];
        if (node is null || query_interval.start > node.max_end) {
            return results;
        }
        
        // Query intervals_left (overlapping to the right of query_interval.start)
        foreach (interval; node.intervals_left) {
            if (interval.overlaps(query_interval)) {
                results ~= interval;
            } else if (interval.start > query_interval.end) {
                break; // Optimization: intervals_left sorted by start
            }
        }
        
        if (query_interval.start < node.center) {
            results ~= query(node.left_child, query_interval);
        }
        
        if (query_interval.end > node.center) {
            results ~= query(node.right_child, query_interval);
        }
        
        return results;
    }
}

// void main() {
//     auto tree = new IntervalTree();
//     Interval[] intervals_to_insert = [
//         new Interval(1, 5), new Interval(2, 6), new Interval(4, 8),
//         new Interval(9, 12), new Interval(10, 14), new Interval(0, 3)
//     ];
//     foreach (i; intervals_to_insert) {
//         tree.root = tree.insert(tree.root, i);
//     }

//     Interval query_int = new Interval(3, 7);
//     auto overlaps = tree.query(tree.root, query_int);
//     writeln("Intervals overlapping with [%s, %s]:", query_int.start, query_int.end);
//     foreach (o; overlaps) {
//         writeln("[%s, %s]", o.start, o.end); // Expected: [1,5], [2,6], [4,8]
//     }
// }
```

## Applications

### Application

Interval Trees are powerful tools for managing and querying sets of intervals. Their applications include:
- **Genomic Data Analysis:** Finding overlapping genes, mutations, or regions in DNA sequences.
- **Calendar and Scheduling Software:** Efficiently finding all events that overlap with a particular time slot.
- **Computational Geometry:** Various problems involving intersections of line segments or rectangles.
- **Event Management:** Managing event timelines and finding concurrent events.
- **Graphical User Interfaces (GUIs):** For hit-testing, where you need to find all UI elements that overlap with a mouse click (point query) or a selection box (interval query).
- **Database Systems:** For handling queries on temporal data or ranges.

