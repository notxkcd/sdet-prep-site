---
title: "Metric Tree"
---

A `Metric Tree` (specifically an `M-Tree`) is a tree data structure used for indexing `objects` in a `metric space`. Unlike traditional `tree structures` that rely on spatial coordinates (like `K-D Trees` or `R-Trees`) or sorted keys (like `BSTs`), `Metric Trees` organize `objects` based solely on their pairwise `distances`, defined by a `metric function`.

This allows it to handle data where coordinate geometry might not be applicable, but a meaningful `distance` between any two `objects` can be calculated (e.g., image similarity, document plagiarism, protein structures). It's particularly useful for `similarity searches` (finding `objects` "similar" to a given query `object`) in high-dimensional or non-Euclidean spaces.

## How it Works

### How it Works (Expanded)

In an `M-Tree`, each `node` stores a set of "`routing objects`" and for each `routing object`, it keeps a pointer to a child `node` or a `leaf node`, along with a "`covering radius`."

---

Key Concepts:

1.  **`Metric Space`**: A set of elements and a distance function `d(x,y)` that satisfies:
- `d(x,y) >= 0` (non-negativity)
- `d(x,y) == 0` iff `x == y` (identity of indiscernibles)
- `d(x,y) == d(y,x)` (symmetry)
- `d(x,z) <= d(x,y) + d(y,z)` (triangle inequality)

2.  **`Routing Objects`**: In each internal node, these are representative objects from the subtree.

3.  **`Covering Radius`**: For each routing object, this is the maximum distance from the routing object to any object in its corresponding child subtree.

Conceptual M-Tree (m=3, max 2 routing objects per node, max 3 children)

                  Root (Routing: R1, R2)
                 /      |      \
                /       |       \
          Child1 (R3, R4)  Child2 (R5, R6)  Child3 (R7, R8)
          (Covering Radii for R3,R4)
                 / | \
                /  |  \
            Leaves with Actual Data Objects

## Implementation {#implementation}

### Python

```python
# Conceptual M-Tree in Python (highly simplified)
# A full M-Tree implementation is very complex, typically managing disk pages.
# This focuses on the conceptual structure and distance-based logic.

# Assume we have a generic Item that has a 'distance' method
# class Item:
#     def distance(self, other_item):
#         # Must implement a metric distance function
#         pass

class MTreeNode:
    def __init__(self, is_leaf=True):
        self.is_leaf = is_leaf
        self.routing_objects = [] # List of (Item, covering_radius, child_node/payload)
        self.capacity = 4 # Max entries per node (simplified)

class MTree:
    def __init__(self, distance_func):
        self.root = MTreeNode()
        self.distance_func = distance_func # The metric distance function

    def _choose_subtree(self, node, item):
        # In a real M-Tree, this involves finding the routing object
        # that minimizes radius enlargement or is closest to the item.
        # Here, simplified to just returning the first routing object's child.
        if node.routing_objects:
            # Simulate choosing the "best" child
            return node.routing_objects[0][2] # return the child_node
        return None

    def insert(self, root_node, item):
        # Simplified insert - does not handle node splitting or complex routing
        if root_node.is_leaf:
            # Assume item itself is the payload for leaves
            root_node.routing_objects.append((item, 0, None)) # (item, radius, payload_or_child)
        else:
            child_to_insert_into = self._choose_subtree(root_node, item)
            if child_to_insert_into:
                self.insert(child_to_insert_into, item)
            else: # No children, make it a leaf for now (very simplified)
                root_node.is_leaf = True
                root_node.routing_objects.append((item, 0, None))

    def range_query(self, root_node, query_item, radius, results=None):
        if results is None:
            results = []

        if root_node.is_leaf:
            for ro, _, _ in root_node.routing_objects:
                if self.distance_func(query_item, ro) <= radius:
                    results.append(ro)
        else:
            for ro, covering_radius, child_node in root_node.routing_objects:
                # Pruning condition: if the query range can intersect the child's covering radius
                if self.distance_func(query_item, ro) <= radius + covering_radius:
                    self.range_query(child_node, query_item, radius, results)
        return results

# Example Usage (highly conceptual):
# def euclidean_distance_1d(a, b): # Simple 1D distance for conceptual demo
#     return abs(a - b)

# mt = MTree(euclidean_distance_1d)
# items = [10, 20, 5, 15, 25, 30]
# root = MTreeNode(is_leaf=False) # Start with a non-leaf root
# # Manually create a child node for the root to simplify initial setup
# child1 = MTreeNode(is_leaf=True)
# root.routing_objects.append((10, 5, child1)) # (routing_obj, covering_radius, child_node)
# mt.root = root

# mt.insert(mt.root, 12) # Conceptual insert
# query_item = 11
# query_radius = 2
# found = mt.range_query(mt.root, query_item, query_radius)
# print(f"Items within distance {query_radius} of {query_item}: {found}")
```

### Javascript

```javascript
// Conceptual M-Tree in JavaScript (highly simplified)
// A full M-Tree implementation is very complex.

class Item {
    constructor(id, value) {
        this.id = id;
        this.value = value;
    }

    // Must implement a metric distance function externally or here
    distance(otherItem) {
        // Example 1D Euclidean distance
        return Math.abs(this.value - otherItem.value);
    }
}

class MTreeNode {
    constructor(isLeaf = true) {
        this.isLeaf = isLeaf;
        this.routingObjects = []; // List of {item: Item, coveringRadius: number, childNode: MTreeNode}
        this.capacity = 4; // Simplified max entries per node
    }
}

class MTree {
    constructor(distanceFunc) {
        this.root = new MTreeNode();
        this.distanceFunc = distanceFunc; // The metric distance function
    }

    _chooseSubtree(node, item) {
        // Simplified: just returns the first valid child or null
        if (node.routingObjects.length > 0) {
            // In a real M-Tree, logic to find best child (e.g., min enlargement of radius)
            return node.routingObjects[0].childNode;
        }
        return null;
    }

    insert(rootNode, item) {
        // Simplified insert - no splitting, just adds to leaf or first child
        if (rootNode.isLeaf) {
            rootNode.routingObjects.push({ item: item, coveringRadius: 0, childNode: null });
        } else {
            let childToInsertInto = this._chooseSubtree(rootNode, item);
            if (childToInsertInto) {
                this.insert(childToInsertInto, item);
                // Update covering radius of routing object if needed
            } else {
                rootNode.isLeaf = true; // Make current node a leaf if no children yet
                rootNode.routingObjects.push({ item: item, coveringRadius: 0, childNode: null });
            }
        }
    }

    rangeQuery(rootNode, queryItem, radius, results = []) {
        if (!rootNode) {
            return results;
        }

        if (rootNode.isLeaf) {
            for (const entry of rootNode.routingObjects) {
                if (this.distanceFunc(queryItem, entry.item) <= radius) {
                    results.push(entry.item);
                }
            }
        } else {
            for (const entry of rootNode.routingObjects) {
                // Pruning condition (conceptual): if query range can intersect child's covering radius
                if (this.distanceFunc(queryItem, entry.item) <= radius + entry.coveringRadius) {
                    this.rangeQuery(entry.childNode, queryItem, radius, results);
                }
            }
        }
        return results;
    }
}

// const euclideanDistance1D = (a, b) => Math.abs(a.value - b.value);
// const mt = new MTree(euclideanDistance1D);
// const items = [new Item(1, 10), new Item(2, 20), new Item(3, 5), new Item(4, 15)];

// // Simplified: manually building a root and child for demo
// const root = new MTreeNode(false);
// const child1 = new MTreeNode(true); // Leaf child
// root.routingObjects.push({ item: new Item('R1', 12), coveringRadius: 5, childNode: child1 });
// mt.root = root;

// mt.insert(mt.root, new Item(5, 12)); // Conceptual insert
// const queryItem = new Item('Q', 11);
// const queryRadius = 2;
// const found = mt.rangeQuery(mt.root, queryItem, queryRadius);
// console.log(<code>Items within distance ${queryRadius} of ${queryItem.value}:</code>, found.map(i => i.value));
```

### Typescript

```typescript
// Conceptual M-Tree in TypeScript (highly simplified)

interface MetricItem {
    id: any;
    value: any;
    distance(other: MetricItem): number;
}

class MTreeNodeTS {
    public isLeaf: boolean;
    // item: routing object, coveringRadius, childNode: points to child subtree or actual data
    public routingObjects: {item: MetricItem, coveringRadius: number, childNode: MTreeNodeTS | null}[];
    public capacity: number;

    constructor(isLeaf: boolean = true) {
        this.isLeaf = isLeaf;
        this.routingObjects = [];
        this.capacity = 4;
    }
}

class MTreeTS {
    public root: MTreeNodeTS;
    private distanceFunc: (a: MetricItem, b: MetricItem) => number;

    constructor(distanceFunc: (a: MetricItem, b: MetricItem) => number) {
        this.root = new MTreeNodeTS();
        this.distanceFunc = distanceFunc;
    }

    private _chooseSubtree(node: MTreeNodeTS, item: MetricItem): MTreeNodeTS | null {
        // Simplified: in a real M-Tree, complex logic to select the best child
        if (node.routingObjects.length > 0) {
            return node.routingObjects[0].childNode;
        }
        return null;
    }

    public insert(rootNode: MTreeNodeTS, item: MetricItem): void {
        if (rootNode.isLeaf) {
            rootNode.routingObjects.push({ item: item, coveringRadius: 0, childNode: null });
        } else {
            let childToInsertInto = this._chooseSubtree(rootNode, item);
            if (childToInsertInto) {
                this.insert(childToInsertInto, item);
                // Update covering radius of routing object if needed
            } else {
                rootNode.isLeaf = true; // Very simplified: make current node a leaf
                rootNode.routingObjects.push({ item: item, coveringRadius: 0, childNode: null });
            }
        }
    }

    public rangeQuery(rootNode: MTreeNodeTS | null, queryItem: MetricItem, radius: number, results: MetricItem[] = []): MetricItem[] {
        if (!rootNode) {
            return results;
        }

        if (rootNode.isLeaf) {
            for (const entry of rootNode.routingObjects) {
                if (this.distanceFunc(queryItem, entry.item) <= radius) {
                    results.push(entry.item);
                }
            }
        } else {
            for (const entry of rootNode.routingObjects) {
                // Pruning condition (conceptual)
                if (this.distanceFunc(queryItem, entry.item) <= radius + entry.coveringRadius) {
                    this.rangeQuery(entry.childNode, queryItem, radius, results);
                }
            }
        }
        return results;
    }
}

// const euclideanDistance1D = (a: MetricItem, b: MetricItem): number => Math.abs(a.value - b.value);
// // Example Item for conceptual demo
// class MyItem implements MetricItem {
//     constructor(public id: any, public value: number) {}
//     distance(other: MetricItem): number {
//         return Math.abs(this.value - (other as MyItem).value);
//     }
// }

// const mtTS = new MTreeTS(euclideanDistance1D);
// const itemsTS: MyItem[] = [new MyItem(1, 10), new MyItem(2, 20), new MyItem(3, 5), new MyItem(4, 15)];

// // Simplified: manually building a root and child for demo
// const rootTS = new MTreeNodeTS(false);
// const child1TS = new MTreeNodeTS(true);
// rootTS.routingObjects.push({ item: new MyItem('R1', 12), coveringRadius: 5, childNode: child1TS });
// mtTS.root = rootTS;

// mtTS.insert(mtTS.root, new MyItem(5, 12));
// const queryItemTS = new MyItem('Q', 11);
// const queryRadiusTS = 2;
// const foundTS = mtTS.rangeQuery(mtTS.root, queryItemTS, queryRadiusTS);
// console.log(<code>Items within distance ${queryRadiusTS} of ${queryItemTS.value}:</code>, foundTS.map(i => i.value));
```

### Cpp

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <functional> // For std::function
#include <algorithm>  // For std::min, std::max

// Forward declaration for distance function
class MetricItem;

// Define a metric distance function type
using DistanceFunc = std::function<double(const MetricItem&, const MetricItem&)>;

// Generic item with some value and an ID
class MetricItem {
public:
    int id;
    double value; // For simple conceptual demo
    // In real scenarios, this could be complex data, an image hash, etc.

    MetricItem(int i, double v) : id(i), value(v) {}

    // Implement distance method or pass a distance function to MTree
    // For this conceptual example, we assume external distance_func.
};

// Example 1D Euclidean distance function
double euclideanDistance1D(const MetricItem& a, const MetricItem& b) {
    return std::abs(a.value - b.value);
}

class MTreeNode {
public:
    bool is_leaf;
    // Stores: {routing_object, covering_radius, pointer_to_child_node_or_payload}
    std::vector<std::tuple<MetricItem, double, MTreeNode<em>>> routing_objects;
    int capacity;

    MTreeNode(bool leaf = true) : is_leaf(leaf), capacity(4) {}

    ~MTreeNode() {
        // Proper deletion of child nodes
        if (!is_leaf) {
            for (auto& entry : routing_objects) {
                delete std::get<2>(entry); // Delete child MTreeNode</em>
            }
        }
    }
};

class MTree {
public:
    MTreeNode<em> root;
    DistanceFunc distance_func;

    MTree(DistanceFunc df) : distance_func(df) {
        root = new MTreeNode(true); // Initially, root is a leaf
    }

    ~MTree() {
        delete root;
    }

private:
    // Simplified: in a real M-Tree, complex logic to select the best child
    MTreeNode</em> chooseSubtree(MTreeNode<em> node, const MetricItem& item) {
        if (node->routing_objects.empty()) {
            return nullptr;
        }
        // Simplified to just return the first child
        return std::get<2>(node->routing_objects[0]);
    }

    void insert(MTreeNode</em>& root_node, const MetricItem& item) {
        if (root_node->is_leaf) {
            root_node->routing_objects.emplace_back(item, 0.0, nullptr);
            // In a real M-Tree, check capacity and split if full
        } else {
            MTreeNode<em> child_to_insert_into = chooseSubtree(root_node, item);
            if (child_to_insert_into) {
                insert(child_to_insert_into, item);
                // Update covering radius of routing object if needed
            } else {
                // If no children, create a new leaf child (very simplified)
                MTreeNode</em> new_leaf_child = new MTreeNode(true);
                new_leaf_child->routing_objects.emplace_back(item, 0.0, nullptr);
                root_node->routing_objects.emplace_back(MetricItem(-1, 0.0), 0.0, new_leaf_child); // Dummy routing for new child
            }
        }
    }

    void rangeQuery(MTreeNode<em> node, const MetricItem& query_item, double radius, std::vector<MetricItem>& results) {
        if (node == nullptr) {
            return;
        }

        if (node->is_leaf) {
            for (auto& entry : node->routing_objects) {
                const MetricItem& stored_item = std::get<0>(entry);
                if (distance_func(query_item, stored_item) <= radius) {
                    results.push_back(stored_item);
                }
            }
        } else {
            for (auto& entry : node->routing_objects) {
                const MetricItem& routing_obj = std::get<0>(entry);
                double covering_radius = std::get<1>(entry);
                MTreeNode</em> child_node = std::get<2>(entry);

                // Pruning condition (conceptual)
                if (distance_func(query_item, routing_obj) <= radius + covering_radius) {
                    rangeQuery(child_node, query_item, radius, results);
                }
            }
        }
    }

public:
    void insert(const MetricItem& item) {
        insert(root, item);
    }

    std::vector<MetricItem> rangeQuery(const MetricItem& query_item, double radius) {
        std::vector<MetricItem> results;
        rangeQuery(root, query_item, radius, results);
        return results;
    }
};

// int main() {
//     MTree mt(euclideanDistance1D);
//     std::vector<MetricItem> items_to_insert = {
//         MetricItem(1, 10), MetricItem(2, 20), MetricItem(3, 5), MetricItem(4, 15)
//     };

//     for (const auto& item : items_to_insert) {
//         mt.insert(item);
//     }

//     MetricItem query_item(99, 12); // Query for value 12
//     double query_radius = 3;
//     std::vector<MetricItem> found = mt.rangeQuery(query_item, query_radius);
//     std::cout << "Items within distance " << query_radius << " of " << query_item.value << ": ";
//     for (const auto& item : found) {
//         std::cout << item.value << " "; // Expected: 10, 15 (if initial insert logic simplified)
//     }
//     std::cout << std::endl;
//     
//     return 0;
// }
```

### D

```d
import std.stdio;
import std.string;
import std.algorithm;
import std.array;
import std.math;
import std.functional; // For delegate

// Generic item with some value and an ID
class MetricItem {
    int id;
    double value;

    this(int i, double v) {
        id = i; value = v;
    }
}

// Define a metric distance function type
alias DistanceFunc = double delegate(MetricItem, MetricItem);

// Example 1D Euclidean distance function
double euclideanDistance1D(MetricItem a, MetricItem b) {
    return abs(a.value - b.value);
}

class MTreeNode {
    bool is_leaf;
    // Stores: {routing_object, covering_radius, pointer_to_child_node_or_payload}
    // D does not have direct tuples like Python/C++ std::tuple, use struct/class
    struct RoutingEntry {
        MetricItem item;
        double coveringRadius;
        MTreeNode childNode; // Can be null for leaf payloads
    }
    RoutingEntry[] routing_objects;
    int capacity;

    this(bool leaf = true) {
        is_leaf = leaf;
        capacity = 4;
        routing_objects = [];
    }
    
    // Deallocating children in D is managed by GC, no explicit destructor needed for this example
}

class MTree {
    MTreeNode root;
    DistanceFunc distance_func;

    this(DistanceFunc df) {
        distance_func = df;
        root = new MTreeNode(true); // Initially, root is a leaf
    }

private:
    // Simplified: in a real M-Tree, complex logic to select the best child
    MTreeNode chooseSubtree(MTreeNode node, MetricItem item) {
        if (node.routing_objects.empty) {
            return null;
        }
        // Simplified to just return the first child
        return node.routing_objects[0].childNode;
    }

    void insert(MTreeNode root_node, MetricItem item) {
        // Simplified insert - does not handle node splitting or complex routing
        if (root_node.is_leaf) {
            root_node.routing_objects ~= MTreeNode.RoutingEntry(item, 0.0, null);
            // In a real M-Tree, check capacity and split if full
        } else {
            MTreeNode child_to_insert_into = chooseSubtree(root_node, item);
            if (child_to_insert_into !is null) {
                insert(child_to_insert_into, item);
                // Update covering radius of routing object if needed
            } else {
                root_node.is_leaf = true; // Very simplified: make current node a leaf
                root_node.routing_objects ~= MTreeNode.RoutingEntry(item, 0.0, null);
            }
        }
    }

    void rangeQuery(MTreeNode node, MetricItem query_item, double radius, ref MetricItem[] results) {
        if (node is null) {
            return;
        }

        if (node.is_leaf) {
            foreach (entry; node.routing_objects) {
                if (distance_func(query_item, entry.item) <= radius) {
                    results ~= entry.item;
                }
            }
        } else {
            foreach (entry; node.routing_objects) {
                // Pruning condition (conceptual)
                if (distance_func(query_item, entry.item) <= radius + entry.coveringRadius) {
                    rangeQuery(entry.childNode, query_item, radius, results);
                }
            }
        }
    }

public:
    void insert(MetricItem item) {
        insert(root, item);
    }

    MetricItem[] rangeQuery(MetricItem query_item, double radius) {
        MetricItem[] results = [];
        rangeQuery(root, query_item, radius, results);
        return results;
    }
}

// void main() {
//     auto mt = new MTree(&euclideanDistance1D);
//     MetricItem[] items_to_insert = [
//         new MetricItem(1, 10), new MetricItem(2, 20), new MetricItem(3, 5), new MetricItem(4, 15)
//     ];

//     foreach (item; items_to_insert) {
//         mt.insert(item);
//     }

//     auto query_item = new MetricItem(99, 12); // Query for value 12
//     double query_radius = 3;
//     auto found = mt.rangeQuery(query_item, query_radius);
//     writef("Items within distance %s of %s: ", query_radius, query_item.value);
//     foreach (item; found) {
//         writef("%s ", item.value); // Expected: 10, 15 (if initial insert logic simplified)
//     }
//     writeln();
// }
```

## Applications

### Application

Metric Trees (especially the `M-Tree` variant) are specialized indexing structures for efficiently performing similarity searches in metric spaces where data is not easily represented by traditional coordinates.
- **Image and Video Databases:** Finding images "similar" to a query image based on features (e.g., color histograms, texture descriptors) where "similarity" is defined by a metric distance.
- **Document and Text Retrieval:** Identifying documents with similar content (e.g., plagiarism detection) using distance metrics like `Levenshtein distance` or `cosine similarity`.
- **Content-Based Information Retrieval:** Any system where you search for items based on their intrinsic properties and a defined similarity measure, rather than exact matches.
- **Bioinformatics:** Searching for similar protein or DNA sequences in a large database using sequence alignment distances.
- **Recommendation Systems:** Finding users or items similar to a given profile for personalized recommendations.

