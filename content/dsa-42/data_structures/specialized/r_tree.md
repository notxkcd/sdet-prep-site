---
title: "R-Tree"
---

An R-Tree is a tree data structure used for spatial access methods, i.e., for organizing spatial data (e.g., rectangles, polygons) in dynamic applications where the objects change frequently. It's particularly well-suited for two-dimensional data, such as geographical coordinates or bounding boxes of objects in an image.

R-Trees are used in geographical information systems (GIS), computer-aided design (CAD), and database systems for efficient spatial queries like "find all restaurants within this map area."

## How it Works

### How it Works (Expanded)

Unlike K-D trees or Quadtrees which subdivide space based on fixed rules, R-Trees group nearby objects into minimum bounding rectangles (MBRs). MBRs for child nodes are then grouped into larger MBRs for parent nodes, and so on, up to the root.

---

Key Concept: Minimum Bounding Rectangles (MBRs)

[    MBR for Node A    ]
[  +---------------+   ]
[  | MBR for NWA |   ]
[  | +---+ +---+ |   ]
[  | |obj| |obj| |   ]
[  | +---+ +---+ |   ]
[  | +---+ +---+ |   ]
[  | |obj| |obj| |   ]
[  | +---+ +---+ |   ]
[  +---------------+   ]
[    MBR for Node B    ]

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
# Simplified R-Tree concept - full implementation is complex and extensive.
# This demonstrates the idea of MBR and hierarchical structure.

class Rect:
    def __init__(self, x_min, y_min, x_max, y_max):
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max

    def intersects(self, other_rect):
        return not (self.x_max < other_rect.x_min or
                    self.x_min > other_rect.x_max or
                    self.y_max < other_rect.y_min or
                    self.y_min > other_rect.y_max)

    def contains(self, other_rect):
        return (self.x_min <= other_rect.x_min and
                self.y_min <= other_rect.y_min and
                self.x_max >= other_rect.x_max and
                self.y_max >= other_rect.y_max)

    def enlarge(self, other_rect):
        self.x_min = min(self.x_min, other_rect.x_min)
        self.y_min = min(self.y_min, other_rect.y_min)
        self.x_max = max(self.x_max, other_rect.x_max)
        self.y_max = max(self.y_max, other_rect.y_max)

# In a real R-Tree, nodes would have multiple entries (MBRs and pointers)
# and complex split algorithms. This is highly simplified for conceptual understanding.
class RTreeNode:
    def __init__(self, mbr, is_leaf=True):
        self.mbr = mbr # Minimum Bounding Rectangle
        self.is_leaf = is_leaf
        self.children = [] # List of child RTreeNodes or actual data objects (Rects)
        self.capacity = 4 # Max entries per node (simplified)

    def insert(self, rect):
        # Very simplified insert logic
        if self.is_leaf:
            self.children.append(rect)
            # In a real R-Tree, if capacity is exceeded, node splits.
        else:
            # Choose best child for insertion (least enlargement or overlap)
            # This is complex in full R-Tree, simplified to just first child.
            self.children[0].insert(rect)
            self.mbr.enlarge(rect) # Enlarge parent MBR


    def query(self, query_rect, found_items=None):
        if found_items is None:
            found_items = []

        if not self.mbr.intersects(query_rect):
            return found_items

        if self.is_leaf:
            for item_rect in self.children:
                if query_rect.intersects(item_rect): # Assuming item_rects are also Rect objects
                    found_items.append(item_rect)
        else:
            for child_node in self.children:
                child_node.query(query_rect, found_items)
        return found_items

# Example Usage (highly simplified):
# data_rects = [
#     Rect(0,0,1,1), Rect(1,1,2,2), Rect(5,5,6,6), Rect(6,6,7,7)
# ]
# root_mbr = Rect(0,0,10,10)
# r_tree = RTreeNode(root_mbr, is_leaf=False) # Root is usually not a leaf
# # For conceptual demo, manually create a child
# child1_mbr = Rect(0,0,3,3)
# child1 = RTreeNode(child1_mbr, is_leaf=True)
# child1.insert(data_rects[0])
# child1.insert(data_rects[1])
# r_tree.children.append(child1)
# r_tree.mbr.enlarge(child1_mbr) # Update root MBR

# query_area = Rect(0.5, 0.5, 1.5, 1.5)
# results = r_tree.query(query_area)
# for r in results:
#     print(f"Found: ({r.x_min},{r.y_min})-({r.x_max},{r.y_max})")
```

### Javascript

```javascript
// Simplified R-Tree concept - full implementation is complex and extensive.

class Rect {
    constructor(xMin, yMin, xMax, yMax) {
        this.xMin = xMin;
        this.yMin = yMin;
        this.xMax = xMax;
        this.yMax = yMax;
    }

    intersects(otherRect) {
        return !(
            this.xMax < otherRect.xMin ||
            this.xMin > otherRect.xMax ||
            this.yMax < otherRect.yMin ||
            this.yMin > otherRect.yMax
        );
    }

    contains(otherRect) {
        return (
            this.xMin <= otherRect.xMin &&
            this.yMin <= otherRect.yMin &&
            this.xMax >= otherRect.xMax &&
            this.yMax >= otherRect.yMax
        );
    }

    enlarge(otherRect) {
        this.xMin = Math.min(this.xMin, otherRect.xMin);
        this.yMin = Math.min(this.yMin, otherRect.yMin);
        this.xMax = Math.max(this.xMax, otherRect.xMax);
        this.yMax = Math.max(this.yMax, otherRect.yMax);
    }
}

class RTreeNode {
    constructor(mbr, isLeaf = true) {
        this.mbr = mbr; // Minimum Bounding Rectangle
        this.isLeaf = isLeaf;
        this.children = [];
        this.capacity = 4; // Simplified capacity
    }

    insert(rect) {
        // Very simplified insert logic
        if (this.isLeaf) {
            this.children.push(rect);
        } else {
            // In a real R-Tree, choose best child, potentially split nodes.
            // Simplified to just first child for concept.
            if (this.children.length > 0) {
                this.children[0].insert(rect);
            } else { // If no children, make it a leaf and add
                this.isLeaf = true;
                this.children.push(rect);
            }
            this.mbr.enlarge(rect);
        }
    }

    query(queryRect, foundItems = []) {
        if (!this.mbr.intersects(queryRect)) {
            return foundItems;
        }

        if (this.isLeaf) {
            for (let itemRect of this.children) {
                if (queryRect.intersects(itemRect)) {
                    foundItems.push(itemRect);
                }
            }
        } else {
            for (let childNode of this.children) {
                childNode.query(queryRect, foundItems);
            }
        }
        return foundItems;
    }
}
// Example Usage (highly simplified - for conceptual understanding only):
// const dataRects = [
//     new Rect(0,0,1,1), new Rect(1,1,2,2), new Rect(5,5,6,6), new Rect(6,6,7,7)
// ];
// const rootMbr = new Rect(0,0,10,10);
// const rTree = new RTreeNode(rootMbr, false); // Root is usually not a leaf

// // Manually creating a child node for demonstration
// const child1Mbr = new Rect(0,0,3,3);
// const child1 = new RTreeNode(child1Mbr, true);
// child1.insert(dataRects[0]);
// child1.insert(dataRects[1]);
// rTree.children.push(child1);
// rTree.mbr.enlarge(child1Mbr);

// const queryArea = new Rect(0.5, 0.5, 1.5, 1.5);
// const results = rTree.query(queryArea);
// results.forEach(r => console.log(<code>Found: (${r.xMin},${r.yMin})-(${r.xMax},${r.yMax})</code>));
```

### Cpp

```cpp
#include <iostream>
#include <vector>
#include <algorithm> // For std::min, std::max

class Rect {
public:
    double x_min, y_min, x_max, y_max;

    Rect(double x1, double y1, double x2, double y2) : x_min(x1), y_min(y1), x_max(x2), y_max(y2) {}

    bool intersects(const Rect& other_rect) const {
        return !(x_max < other_rect.x_min ||
                x_min > other_rect.x_max ||
                y_max < other_rect.y_min ||
                y_min > other_rect.y_max);
    }

    bool contains(const Rect& other_rect) const {
        return (x_min <= other_rect.x_min &&
                y_min <= other_rect.y_min &&
                x_max >= other_rect.x_max &&
                y_max >= other_rect.y_max);
    }

    void enlarge(const Rect& other_rect) {
        x_min = std::min(x_min, other_rect.x_min);
        y_min = std::min(y_min, other_rect.y_min);
        x_max = std::max(x_max, other_rect.x_max);
        y_max = std::max(y_max, other_rect.y_max);
    }
};

// Simplified R-Tree Node (a full R-Tree is very complex)
class RTreeNode {
public:
    Rect mbr;
    bool is_leaf;
    std::vector<RTreeNode<em>> children_nodes; // For internal nodes
    std::vector<Rect> children_data;     // For leaf nodes
    int capacity;

    RTreeNode(Rect bounding_rect, bool leaf = true, int cap = 4) :
        mbr(bounding_rect), is_leaf(leaf), capacity(cap) {}

    ~RTreeNode() {
        if (!is_leaf) {
            for (RTreeNode</em> child : children_nodes) {
                delete child;
            }
        }
    }

    // Very simplified insert logic
    void insert(const Rect& rect) {
        if (is_leaf) {
            children_data.push_back(rect);
            mbr.enlarge(rect); // Enlarge this leaf's MBR
        } else {
            // In a real R-Tree, choose best child to insert into
            // For this concept, just add as a new child or into first child
            if (children_nodes.empty()) {
                children_nodes.push_back(new RTreeNode(rect, true, capacity)); // Create a new leaf child
            } else {
                children_nodes[0]->insert(rect);
            }
            mbr.enlarge(rect); // Enlarge parent MBR
        }
    }

    std::vector<Rect> query(const Rect& query_rect, std::vector<Rect> found_items = {}) const {
        if (!mbr.intersects(query_rect)) {
            return found_items;
        }

        if (is_leaf) {
            for (const auto& item_rect : children_data) {
                if (query_rect.intersects(item_rect)) {
                    found_items.push_back(item_rect);
                }
            }
        } else {
            for (const auto& child_node : children_nodes) {
                found_items = child_node->query(query_rect, found_items);
            }
        }
        return found_items;
    }
};
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

A full R-Tree implementation is quite complex, involving intricate algorithms for node splitting and choosing insertion paths. The provided code is a highly simplified conceptual demonstration.

---

**`Rect` Class:** Represents a rectangular area, used for both data objects and Minimum Bounding Rectangles (MBRs) of nodes.
- `x_min, y_min, x_max, y_max`: Coordinates defining the rectangle.
- `intersects(other_rect)`: Checks if this rectangle overlaps with another.
- `contains(other_rect)`: Checks if this rectangle fully contains another.
- `enlarge(other_rect)`: Expands this rectangle to encompass another rectangle.

**`RTreeNode` Class (Simplified):** Represents a node in the R-Tree.
- `mbr`: The `Minimum Bounding Rectangle` for this node.
- `is_leaf`: A boolean indicating if this is a leaf `node` (stores actual data `objects`) or an internal `node` (stores child `nodes`).
- `children_nodes` (for internal `nodes`) or `children_data` (for leaf `nodes`): Stores either pointers to child `RTreeNode`s or the actual `Rect` data `objects`.
- `capacity`: The maximum number of entries (children or data `objects`) a `node` can hold.
- **`insert(rect)` (Simplified):**
- If it's a `leaf node`, it adds the `rect` to `children_data` and enlarges its `mbr`.
- If it's an internal `node`, it (conceptually) picks a child to insert into (simplified to just the first child) and enlarges its own `mbr` to cover the new `rect`. Real R-Trees have complex algorithms to select the best child.

    </li>
- **`query(query_rect, found_items)`:**
- Checks if this `node`'s `mbr` intersects the `query_rect`. If not, it prunes this branch.
- If it's a `leaf node`, it checks its `children_data` for direct intersections with `query_rect` and adds them to `found_items`.
- If it's an internal `node`, it recursively calls `query` on its child `nodes` whose `mbr`s intersect the `query_rect`.

    </li>

[Back to Implementation](#implementation)

## Applications

### Application

R-Trees are a cornerstone of spatial databases and geographical information systems (GIS). They are used by database systems like **PostGIS (for PostgreSQL)** and **MySQL Spatial** to provide efficient indexing of geospatial data. This allows for fast queries like "find all parks within 5 miles of this point." They are also used in computer-aided design (CAD) systems for storing the layout of objects on a blueprint and in real-time mapping services to quickly fetch map features within the user's viewport.

