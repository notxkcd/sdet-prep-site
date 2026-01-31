---
title: "Quadtree"
---

A `Quadtree` is a `tree data structure` in which each internal `node` has exactly four children. `Quadtrees` are most often used to partition a `two-dimensional space` by recursively subdividing it into four `quadrants` or `regions`.

They are particularly useful in `computer graphics`, `game development`, and `image processing` for efficiently storing and querying `spatial data` (e.g., finding all objects within a certain area on a `2D map`).

## How it Works

### How it Works (Expanded)

A `Quadtree` works by recursively dividing a `2D space` into four `equal-sized child regions` (`quadrants`). This subdivision continues until each `region` contains at most a predefined number of `objects` or reaches a minimum size.

---

Initial Region (`Node A`)
+---------------+
|       |       |
|   B   |   C   |  <- Subdivided into 4 children
|-------+-------|
|   D   |   E   |
+---------------+

If `region B` contains too many `objects`, it's subdivided further:
+-------+-------+
| F | G |       |
|---+---|   C   |
| H | I |       |
+-------+-------|
|   D   |   E   |
+---------------+

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x  # Center x
        self.y = y  # Center y
        self.w = w  # Half width
        self.h = h  # Half height

    def contains(self, point):
        return (point.x >= self.x - self.w and
                point.x <= self.x + self.w and
                point.y >= self.y - self.h and
                point.y <= self.y + self.h)

    def intersects(self, range_rect):
        return not (range_rect.x - range_rect.w > self.x + self.w or
                    range_rect.x + range_rect.w < self.x - self.w or
                    range_rect.y - range_rect.h > self.y + self.h or
                    range_rect.y + range_rect.h < self.y - self.h)

class QuadTree:
    def __init__(self, boundary, capacity):
        self.boundary = boundary
        self.capacity = capacity
        self.points = []
        self.divided = False

    def subdivide(self):
        x = self.boundary.x
        y = self.boundary.y
        w = self.boundary.w / 2
        h = self.boundary.h / 2

        nw = Rectangle(x - w, y - h, w, h)
        self.northwest = QuadTree(nw, self.capacity)
        ne = Rectangle(x + w, y - h, w, h)
        self.northeast = QuadTree(ne, self.capacity)
        sw = Rectangle(x - w, y + h, w, h)
        self.southwest = QuadTree(sw, self.capacity)
        se = Rectangle(x + w, y + h, w, h)
        self.southeast = QuadTree(se, self.capacity)

        self.divided = True

    def insert(self, point):
        if not self.boundary.contains(point):
            return False

        if len(self.points) < self.capacity:
            self.points.append(point)
            return True
        else:
            if not self.divided:
                self.subdivide()

            if self.northeast.insert(point): return True
            if self.northwest.insert(point): return True
            if self.southeast.insert(point): return True
            if self.southwest.insert(point): return True
        return false

    def query(self, range_rect, found=[]):
        if not self.boundary.intersects(range_rect):
            return found

        for p in self.points:
            if range_rect.contains(p):
                found.append(p)

        if self.divided:
            self.northwest.query(range_rect, found)
            self.northeast.query(range_rect, found)
            self.southwest.query(range_rect, found)
            self.southeast.query(range_rect, found)
        return found
```

### Javascript

```javascript
class Point {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
}

class Rectangle {
    constructor(x, y, w, h) {
        this.x = x; // Center x
        this.y = y; // Center y
        this.w = w; // Half width
        this.h = h; // Half height
    }

    contains(point) {
        return (
            point.x >= this.x - this.w &&
            point.x <= this.x + this.w &&
            point.y >= this.y - this.h &&
            point.y <= this.y + this.h
        );
    }

    intersects(rangeRect) {
        return !(
            rangeRect.x - rangeRect.w > this.x + this.w ||
            rangeRect.x + rangeRect.w < this.x - this.w ||
            rangeRect.y - rangeRect.h > this.y + this.h ||
            rangeRect.y + rangeRect.h < this.y - this.h
        );
    }
}

class QuadTree {
    constructor(boundary, capacity) {
        this.boundary = boundary;
        this.capacity = capacity;
        this.points = [];
        this.divided = false;
    }

    subdivide() {
        let x = this.boundary.x;
        let y = this.boundary.y;
        let w = this.boundary.w / 2;
        let h = this.boundary.h / 2;

        let nw = new Rectangle(x - w, y - h, w, h);
        this.northwest = new QuadTree(nw, this.capacity);
        let ne = new Rectangle(x + w, y - h, w, h);
        this.northeast = new QuadTree(ne, this.capacity);
        let sw = new Rectangle(x - w, y + h, w, h);
        this.southwest = new QuadTree(sw, this.capacity);
        let se = new Rectangle(x + w, y + h, w, h);
        this.southeast = new QuadTree(se, this.capacity);

        this.divided = true;
    }

    insert(point) {
        if (!this.boundary.contains(point)) {
            return false;
        }

        if (this.points.length < this.capacity) {
            this.points.push(point);
            return true;
        } else {
            if (!this.divided) {
                this.subdivide();
            }

            if (this.northeast.insert(point)) return true;
            if (this.northwest.insert(point)) return true;
            if (this.southeast.insert(point)) return true;
            if (this.southwest.insert(point)) return true;
        }
        return false;
    }

    query(rangeRect, found = []) {
        if (!this.boundary.intersects(rangeRect)) {
            return found;
        }

        for (let p of this.points) {
            if (rangeRect.contains(p)) {
                found.push(p);
            }
        }

        if (this.divided) {
            this.northwest.query(rangeRect, found);
            this.northeast.query(rangeRect, found);
            this.southwest.query(rangeRect, found);
            this.southeast.query(rangeRect, found);
        }
        return found;
    }
}
```

### Cpp

```cpp
#include <vector>
#include <iostream>

class Point {
public:
    double x, y;
    Point(double x, double y) : x(x), y(y) {}
};

class Rectangle {
public:
    double x, y, w, h; // Center x, y, half width, half height

    Rectangle(double x, double y, double w, double h) : x(x), y(y), w(w), h(h) {}

    bool contains(Point p) {
        return (p.x >= x - w &&
                p.x <= x + w &&
                p.y >= y - h &&
                p.y <= y + h);
    }

    bool intersects(const Rectangle& range_rect) const {
        return !(range_rect.x - range_rect.w > x + w ||
                range_rect.x + range_rect.w < x - w ||
                range_rect.y - range_rect.h > y + h ||
                range_rect.y + range_rect.h < y - h);
    }
};

class QuadTree {
public:
    Rectangle boundary;
    int capacity;
    std::vector<Point> points;
    bool divided;

    QuadTree <em>northwest, </em>northeast, <em>southwest, </em>southeast;

    QuadTree(Rectangle boundary, int capacity) : boundary(boundary), capacity(capacity), divided(false) {
        northwest = northeast = southwest = southeast = nullptr;
    }

    // Destructor to free memory
    ~QuadTree() {
        delete northwest;
        delete northeast;
        delete southwest;
        delete southeast;
    }

    void subdivide() {
        double x = boundary.x;
        double y = boundary.y;
        double w = boundary.w / 2;
        double h = boundary.h / 2;

        Rectangle nw = Rectangle(x - w, y - h, w, h);
        northwest = new QuadTree(nw, capacity);
        Rectangle ne = Rectangle(x + w, y - h, w, h);
        northeast = new QuadTree(ne, capacity);
        Rectangle sw = Rectangle(x - w, y + h, w, h);
        southwest = new QuadTree(sw, capacity);
        Rectangle se = Rectangle(x + w, y + h, w, h);
        southeast = new QuadTree(se, capacity);

        divided = true;
    }

    bool insert(Point p) {
        if (!boundary.contains(p)) {
            return false;
        }

        if (points.size() < capacity) {
            points.push_back(p);
            return true;
        } else {
            if (!divided) {
                subdivide();
            }

            if (northwest->insert(p)) return true;
            if (northeast->insert(p)) return true;
            if (southwest->insert(p)) return true;
            if (southeast->insert(p)) return true;
        }
        return false;
    }

    std::vector<Point> query(const Rectangle& range_rect, std::vector<Point> found_points = {}) {
        if (!boundary.intersects(range_rect)) {
            return found_points;
        }

        for (const auto& p : points) {
            if (range_rect.contains(p)) {
                found_points.push_back(p);
            }
        }

        if (divided) {
            found_points = northwest->query(range_rect, found_points);
            found_points = northeast->query(range_rect, found_points);
            found_points = southwest->query(range_rect, found_points);
            found_points = southeast->query(range_rect, found_points);
        }
        return found_points;
    }
};
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

A Quadtree implementation involves defining helper classes for Points and Rectangles, and then the Quadtree itself, often recursively.

---

**Point Class:** Simple class to represent a point in 2D space with `x` and `y` coordinates.

**Rectangle Class:** Represents the spatial boundary of a Quadtree node. It typically stores its center `(x, y)` and its `half-width (w)` and `half-height (h)`. It includes helper methods like `contains(point)` to check if a point is within its bounds, and `intersects(range_rect)` to check if it overlaps with another rectangle (useful for querying).

**QuadTree Class:**
- `boundary`: A `Rectangle` object defining the area this Quadtree node covers.
- `capacity`: The maximum number of points this node can hold before it subdivides.
- `points`: A list of `Point` objects stored in this node (if it's not subdivided).
- `divided`: A boolean flag indicating if this node has been subdivided.
- `northwest, northeast, southwest, southeast`: Pointers to the four child Quadtree nodes.
- **`subdivide()`:** Creates four new `QuadTree` objects for the four sub-quadrants and sets `divided` to true.
- **`insert(point)`:**
- Checks if the point is within this Quadtree's boundary. If not, returns false.
- If the node has capacity, adds the point to its `points` list.
- If the node is at capacity, it subdivides (if not already), and then attempts to insert the point into one of its children recursively.

    </li>
- **`query(range_rect, found_points)`:**
- Checks if the query `range_rect` intersects this Quadtree's boundary. If not, returns the current `found_points`.
- Checks all points directly held by this node and adds those within `range_rect` to `found_points`.
- If the node is divided, it recursively calls `query` on its children.

    </li>

[Back to Implementation](#implementation)

## Applications

### Application

Quadtrees are widely used in 2D computer graphics and geographical information systems (GIS). In video games, they are used for collision detection, efficiently culling objects that are not in the current view (view frustum culling), and for managing objects in a large 2D world. In GIS, they are used for spatial indexing of geographical data like cities, roads, and lakes, allowing for fast queries of features within a specific geographical area.

