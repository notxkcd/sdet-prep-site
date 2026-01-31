---
title: "K-D Tree"
---

A K-D Tree (k-dimensional tree) is a space-partitioning data structure for organizing points in a k-dimensional space. It's a binary tree in which every node is a k-dimensional point. Every non-leaf node implicitly generates a splitting hyperplane that divides the space into two half-spaces.

K-D trees are particularly useful for range searches and nearest neighbor searches in multi-dimensional datasets, commonly found in applications like computer graphics, robotics, and geographical information systems (GIS).

## How it Works

### How it Works (Expanded)

The core idea behind a K-D tree is to create a binary tree where each level of the tree splits the data points along a different dimension. For a 2D dataset, it might alternate splitting along the X-axis, then the Y-axis, then X again, and so on.

---

Example K-D Tree (2D): Points (P1, P2, P3, ...)
Split along X-axis at Root (e.g., P5)
    /  \
   /    \
  Left   Right (points with X < P5.x and X > P5.x)
        Split along Y-axis at next level

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
class Node:
    def __init__(self, point, axis, left=None, right=None):
        self.point = point
        self.axis = axis
        self.left = left
        self.right = right

def build_kdtree(points, depth=0):
    if not points:
        return None

    k = len(points[0]) # dimensionality
    axis = depth % k

    points.sort(key=lambda x: x[axis])
    median_idx = len(points) // 2

    return Node(
        point=points[median_idx],
        axis=axis,
        left=build_kdtree(points[:median_idx], depth + 1),
        right=build_kdtree(points[median_idx + 1:], depth + 1)
    )

def kdtree_search_nearest(root, query_point, depth=0, best=None):
    if root is None:
        return best

    k = len(query_point)
    axis = depth % k

    # Update best if current node is closer
    if best is None or distance(root.point, query_point) < distance(best.point, query_point):
        best = root

    # Decide which branch to go down
    if query_point[axis] < root.point[axis]:
        next_branch = root.left
        other_branch = root.right
    else:
        next_branch = root.right
        other_branch = root.left

    best = kdtree_search_nearest(next_branch, query_point, depth + 1, best)

    # Check if the other branch could contain a closer point
    # i.e., if the distance to the splitting plane is less than current best distance
    if best is None or abs(query_point[axis] - root.point[axis]) < distance(best.point, query_point):
        best = kdtree_search_nearest(other_branch, query_point, depth + 1, best)

    return best

def distance(p1, p2):
    # Euclidean distance for 2D points (x, y)
    return ((p1[0] - p2[0])<strong>2 + (p1[1] - p2[1])</strong>2)*<em>0.5

# Example Usage:
# points = [(2,3), (5,4), (9,6), (4,7), (8,1), (7,2)]
# kdtree_root = build_kdtree(points)
# query = (9, 2)
# nearest_node = kdtree_search_nearest(kdtree_root, query)
# print(f"Nearest point to {query} is {nearest_node.point}") # Expected: (8,1) or (7,2) depending on median choice. 
```

### Javascript

```javascript
class Node {
    constructor(point, axis, left = null, right = null) {
        this.point = point;
        this.axis = axis;
        this.left = left;
        this.right = right;
    }
}

function buildKDTree(points, depth = 0) {
    if (!points || points.length === 0) {
        return null;
    }

    const k = points[0].length; // dimensionality
    const axis = depth % k;

    points.sort((a, b) => a[axis] - b[axis]);
    const medianIdx = Math.floor(points.length / 2);

    return new Node(
        points[medianIdx],
        axis,
        buildKDTree(points.slice(0, medianIdx), depth + 1),
        buildKDTree(points.slice(medianIdx + 1), depth + 1)
    );
}

function distance(p1, p2) {
    // Euclidean distance for 2D points (x, y)
    return Math.sqrt(Math.pow(p1[0] - p2[0], 2) + Math.pow(p1[1] - p2[1], 2));
}

function searchNearest(root, queryPoint, depth = 0, best = null) {
    if (root === null) {
        return best;
    }

    const k = queryPoint.length;
    const axis = depth % k;

    // Update best if current node is closer
    if (best === null || distance(root.point, queryPoint) < distance(best.point, queryPoint)) {
        best = root;
    }

    let nextBranch, otherBranch;
    if (queryPoint[axis] < root.point[axis]) {
        nextBranch = root.left;
        otherBranch = root.right;
    } else {
        nextBranch = root.right;
        otherBranch = root.left;
    }

    best = searchNearest(nextBranch, queryPoint, depth + 1, best);

    // Check if the other branch could contain a closer point
    // i.e., if the distance to the splitting hyperplane is less than current best distance
    if (best === null || Math.abs(queryPoint[axis] - root.point[axis]) < distance(best.point, queryPoint)) {
        best = searchNearest(otherBranch, queryPoint, depth + 1, best);
    }

    return best;
}

// Example Usage:
// const points = [[2,3], [5,4], [9,6], [4,7], [8,1], [7,2]];
// const kdtreeRoot = buildKDTree(points);
// const query = [9, 2];
// const nearestNode = searchNearest(kdtreeRoot, query);
// console.log(<code>Nearest point to ${query} is ${nearestNode.point}</code>); // Expected: [8,1] or [7,2]
```

### Cpp

```cpp
#include <iostream>
#include <vector>
#include <algorithm> // For std::sort
#include <cmath>     // For std::pow, std::sqrt

struct Point {
    std::vector<int> coords;
    Point(std::vector<int> c) : coords(std::move(c)) {}
};

struct Node {
    Point point;
    int axis;
    Node </em>left, <em>right;

    Node(Point p, int ax) : point(std::move(p)), axis(ax), left(nullptr), right(nullptr) {}

    // Destructor to free memory
    ~Node() {
        delete left;
        delete right;
    }
};

double euclideanDistance(const Point& p1, const Point& p2) {
    double dist = 0;
    for (size_t i = 0; i < p1.coords.size(); ++i) {
        dist += std::pow(p1.coords[i] - p2.coords[i], 2);
    }
    return std::sqrt(dist);
}

Node</em> buildKDTree(std::vector<Point>& points, int depth = 0) {
    if (points.empty()) {
        return nullptr;
    }

    int k = points[0].coords.size(); // dimensionality
    int axis = depth % k;

    std::sort(points.begin(), points.end(), [&](const Point& a, const Point& b) {
        return a.coords[axis] < b.coords[axis];
    });

    size_t median_idx = points.size() / 2;

    Node<em> root = new Node(points[median_idx], axis);
    
    std::vector<Point> left_points(points.begin(), points.begin() + median_idx);
    std::vector<Point> right_points(points.begin() + median_idx + 1, points.end());

    root->left = buildKDTree(left_points, depth + 1);
    root->right = buildKDTree(right_points, depth + 1);

    return root;
}

Node</em> searchNearest(Node<em> root, const Point& query_point, int depth = 0, Node</em> best = nullptr) {
    if (root == nullptr) {
        return best;
    }

    int k = query_point.coords.size();
    int axis = depth % k;

    // Update best if current node is closer
    if (best == nullptr || euclideanDistance(root->point, query_point) < euclideanDistance(best->point, query_point)) {
        best = root;
    }

    Node<em> next_branch;
    Node</em> other_branch;

    if (query_point.coords[axis] < root->point.coords[axis]) {
        next_branch = root->left;
        other_branch = root->right;
    } else {
        next_branch = root->right;
        other_branch = root->left;
    }

    best = searchNearest(next_branch, query_point, depth + 1, best);

    // Check if the other branch could contain a closer point
    if (best == nullptr || std::abs(query_point.coords[axis] - root->point.coords[axis]) < euclideanDistance(best->point, query_point)) {
        best = searchNearest(other_branch, query_point, depth + 1, best);
    }

    return best;
}
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

A K-D Tree implementation typically involves a `Node` structure and recursive functions for building and searching.

---

**`Point` Struct/Class:** A simple structure to hold the `k`-dimensional coordinates of a point.

**`Node` Struct/Class:** Represents a `node` in the K-D tree. It stores the `point` it represents, the `axis` (dimension) it splits along, and pointers to its `left` and `right` children.

**`buildKDTree(points, depth)`:**
- This is a recursive function to construct the tree.
- It determines the current `axis` to split on based on the `depth`.
- It sorts the `points` along this `axis` and selects the `median point` as the current `node`'s `point`.
- It then recursively calls itself to build the `left` and `right subtrees` with the remaining `points`.

**`searchNearest(root, query_point, depth, best)`:**
- This is a recursive function to find the `nearest neighbor`.
- It compares the `query_point` to the current `node`'s `point` and updates the `best` candidate found so far.
- It then decides which child branch is "more likely" to contain the `nearest neighbor` and recursively searches that branch.
- Crucially, it then checks if the other branch (the one not initially chosen) could potentially contain a closer `point`. This check is based on the `distance` from the `query_point` to the splitting `hyperplane`. If this `distance` is less than the current `best distance`, it also recursively searches the other branch. This backtracking is what makes `nearest neighbor search` efficient in K-D trees.

[Back to Implementation](#implementation)

## Applications

### Application

K-D Trees are highly effective for organizing points in multi-dimensional space. Their primary applications include fast **nearest neighbor searches**, which are fundamental to many algorithms in data science and machine learning (e.g., k-NN classification). In computer graphics, they are used for tasks like ray tracing to quickly find intersection points. In robotics, they help process point cloud data from 3D scanners to understand the robot's environment.

