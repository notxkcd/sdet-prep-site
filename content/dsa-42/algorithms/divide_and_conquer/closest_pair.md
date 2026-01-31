---
title: "Closest Pair of Points"
---

The `Closest Pair of Points Problem` is a classic problem in computational geometry that asks to find the pair of points in a set that have the smallest distance between them. A naive brute-force approach would compare every pair of points, resulting in an `O(N^2)` time complexity. However, a more efficient solution can be achieved using a `divide and conquer` approach.

The `divide and conquer` algorithm for this problem achieves an `O(N log N)` time complexity, which is a significant improvement over the brute-force method, especially for large sets of points.

## How it Works

### How it Works (Expanded)

The `divide and conquer` strategy for the `Closest Pair of Points Problem` involves recursively splitting the set of points into two halves, finding the closest pair in each half, and then handling a crucial "merge" step where the closest pair might span the two halves.

---

Example: Find closest pair in a set of 2D points.

1.  **Divide:** Sort the points by their x-coordinate. Split the sorted array into two halves at the median x-coordinate.
2.  **Conquer:** Recursively find the closest pair in the left half (let the min distance be `d_L`) and the right half (min distance `d_R`).
3.  **Combine:** The minimum distance `d` so far is `min(d_L, d_R)`.
4.  **Merge Step (Crucial):** A closer pair might exist where one point is in the left half and the other in the right half.
- Create a "strip" of points that are within distance `d` of the median line.
- For each point in the strip, we only need to check for closer points within a small, constant number of its neighbors in a sub-array sorted by y-coordinate. It can be proven that for any point `p`, we only need to check a constant number of points in the strip that are sorted by y-coordinate.

This merge step, if implemented correctly, takes `O(N)` time.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])<strong>2 + (p1[1] - p2[1])</strong>2)

def brute_force_closest_pair(points):
    min_dist = float('inf')
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
    return min_dist

def closest_pair_recursive(points_sorted_x):
    n = len(points_sorted_x)
    if n <= 3:
        return brute_force_closest_pair(points_sorted_x)

    mid = n // 2
    mid_point = points_sorted_x[mid]

    left_half = points_sorted_x[:mid]
    right_half = points_sorted_x[mid:]

    d_left = closest_pair_recursive(left_half)
    d_right = closest_pair_recursive(right_half)
    d = min(d_left, d_right)

    # Build a strip of points close to the median line
    strip = [p for p in points_sorted_x if abs(p[0] - mid_point[0]) < d]

    # Sort the strip by y-coordinate
    strip.sort(key=lambda p: p[1])
    
    # Check for closer pairs in the strip
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            # Break if y-distance is greater than d
            if (strip[j][1] - strip[i][1]) >= d:
                break
            dist = distance(strip[i], strip[j])
            if dist < d:
                d = dist

    return d

def closest_pair_of_points(points):
    """
    Finds the closest pair of points in a set using a divide and conquer approach.
    <code>points</code>: a list of (x, y) tuples.
    """
    if len(points) < 2:
        return float('inf')
    
    # Initial sort by x-coordinate
    points_sorted_x = sorted(points, key=lambda p: p[0])
    
    return closest_pair_recursive(points_sorted_x)

# Example
# points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
# print(closest_pair_of_points(points)) # Expected: 1.414... (from (2,3) and (3,4))
```

### Javascript

```javascript
function distance(p1, p2) {
    return Math.sqrt(Math.pow(p1.x - p2.x, 2) + Math.pow(p1.y - p2.y, 2));
}

function bruteForceClosestPair(points) {
    let min_dist = Infinity;
    for (let i = 0; i < points.length; i++) {
        for (let j = i + 1; j < points.length; j++) {
            const dist = distance(points[i], points[j]);
            if (dist < min_dist) {
                min_dist = dist;
            }
        }
    }
    return min_dist;
}

function closestPairRecursive(pointsSortedX) {
    const n = pointsSortedX.length;
    if (n <= 3) {
        return bruteForceClosestPair(pointsSortedX);
    }

    const mid = Math.floor(n / 2);
    const midPoint = pointsSortedX[mid];

    const leftHalf = pointsSortedX.slice(0, mid);
    const rightHalf = pointsSortedX.slice(mid);

    const dLeft = closestPairRecursive(leftHalf);
    const dRight = closestPairRecursive(rightHalf);
    let d = Math.min(dLeft, dRight);

    // Build a strip of points close to the median line
    const strip = pointsSortedX.filter(p => Math.abs(p.x - midPoint.x) < d);

    // Sort the strip by y-coordinate
    strip.sort((a, b) => a.y - b.y);
    
    // Check for closer pairs in the strip
    for (let i = 0; i < strip.length; i++) {
        for (let j = i + 1; j < strip.length; j++) {
            // Break if y-distance is greater than d
            if ((strip[j].y - strip[i].y) >= d) {
                break;
            }
            const dist = distance(strip[i], strip[j]);
            if (dist < d) {
                d = dist;
            }
        }
    }

    return d;
}

function closestPairOfPoints(points) {
    if (points.length < 2) {
        return Infinity;
    }
    
    // Initial sort by x-coordinate
    const pointsSortedX = [...points].sort((a, b) => a.x - b.x);
    
    return closestPairRecursive(pointsSortedX);
}

// const points = [
//     {x: 2, y: 3}, {x: 12, y: 30}, {x: 40, y: 50}, 
//     {x: 5, y: 1}, {x: 12, y: 10}, {x: 3, y: 4}
// ];
// console.log(closestPairOfPoints(points)); // Expected: 1.414...
```

### Typescript

```typescript
interface Point {
    x: number;
    y: number;
}

function distanceTS(p1: Point, p2: Point): number {
    return Math.sqrt(Math.pow(p1.x - p2.x, 2) + Math.pow(p1.y - p2.y, 2));
}

function bruteForceClosestPairTS(points: Point[]): number {
    let min_dist = Infinity;
    for (let i = 0; i < points.length; i++) {
        for (let j = i + 1; j < points.length; j++) {
            const dist = distanceTS(points[i], points[j]);
            if (dist < min_dist) {
                min_dist = dist;
            }
        }
    }
    return min_dist;
}

function closestPairRecursiveTS(pointsSortedX: Point[]): number {
    const n = pointsSortedX.length;
    if (n <= 3) {
        return bruteForceClosestPairTS(pointsSortedX);
    }

    const mid = Math.floor(n / 2);
    const midPoint = pointsSortedX[mid];

    const leftHalf = pointsSortedX.slice(0, mid);
    const rightHalf = pointsSortedX.slice(mid);

    const dLeft = closestPairRecursiveTS(leftHalf);
    const dRight = closestPairRecursiveTS(rightHalf);
    let d = Math.min(dLeft, dRight);

    // Build a strip of points close to the median line
    const strip = pointsSortedX.filter(p => Math.abs(p.x - midPoint.x) < d);

    // Sort the strip by y-coordinate
    strip.sort((a, b) => a.y - b.y);
    
    // Check for closer pairs in the strip
    for (let i = 0; i < strip.length; i++) {
        for (let j = i + 1; j < strip.length; j++) {
            // Break if y-distance is greater than d
            if ((strip[j].y - strip[i].y) >= d) {
                break;
            }
            const dist = distanceTS(strip[i], strip[j]);
            if (dist < d) {
                d = dist;
            }
        }
    }

    return d;
}

function closestPairOfPointsTS(points: Point[]): number {
    if (points.length < 2) {
        return Infinity;
    }
    
    // Initial sort by x-coordinate
    const pointsSortedX = [...points].sort((a, b) => a.x - b.x);
    
    return closestPairRecursiveTS(pointsSortedX);
}

// const pointsTS: Point[] = [
//     {x: 2, y: 3}, {x: 12, y: 30}, {x: 40, y: 50}, 
//     {x: 5, y: 1}, {x: 12, y: 10}, {x: 3, y: 4}
// ];
// console.log(closestPairOfPointsTS(pointsTS)); // Expected: 1.414...
```

### Cpp

```cpp
#include <vector>
#include <cmath> // For sqrt, pow
#include <algorithm> // For std::sort, std::min
#include <iostream>
#include <limits> // For std::numeric_limits

struct Point {
    double x, y;
};

double distance(Point p1, Point p2) {
    return std::sqrt(std::pow(p1.x - p2.x, 2) + std::pow(p1.y - p2.y, 2));
}

double bruteForceClosestPair(const std::vector<Point>& points) {
    double min_dist = std::numeric_limits<double>::max();
    for (size_t i = 0; i < points.size(); ++i) {
        for (size_t j = i + 1; j < points.size(); ++j) {
            double dist = distance(points[i], points[j]);
            if (dist < min_dist) {
                min_dist = dist;
            }
        }
    }
    return min_dist;
}

double closestPairRecursive(std::vector<Point>& points_sorted_x) {
    size_t n = points_sorted_x.size();
    if (n <= 3) {
        return bruteForceClosestPair(points_sorted_x);
    }

    size_t mid = n / 2;
    Point mid_point = points_sorted_x[mid];

    std::vector<Point> left_half(points_sorted_x.begin(), points_sorted_x.begin() + mid);
    std::vector<Point> right_half(points_sorted_x.begin() + mid, points_sorted_x.end());

    double d_left = closestPairRecursive(left_half);
    double d_right = closestPairRecursive(right_half);
    double d = std::min(d_left, d_right);

    // Build a strip of points close to the median line
    std::vector<Point> strip;
    for (const auto& p : points_sorted_x) {
        if (std::abs(p.x - mid_point.x) < d) {
            strip.push_back(p);
        }
    }

    // Sort the strip by y-coordinate
    std::sort(strip.begin(), strip.end(), [](Point a, Point b) {
        return a.y < b.y;
    });
    
    // Check for closer pairs in the strip
    for (size_t i = 0; i < strip.size(); ++i) {
        for (size_t j = i + 1; j < strip.size(); ++j) {
            // Break if y-distance is greater than d
            if ((strip[j].y - strip[i].y) >= d) {
                break;
            }
            double dist = distance(strip[i], strip[j]);
            if (dist < d) {
                d = dist;
            }
        }
    }

    return d;
}

double closestPairOfPoints(std::vector<Point>& points) {
    if (points.size() < 2) {
        return std::numeric_limits<double>::max();
    }
    
    // Initial sort by x-coordinate
    std::sort(points.begin(), points.end(), [](Point a, Point b) {
        return a.x < b.x;
    });
    
    return closestPairRecursive(points);
}

// int main() {
//     std::vector<Point> points = {{2, 3}, {12, 30}, {40, 50}, {5, 1}, {12, 10}, {3, 4}};
//     std::cout << "Closest distance: " << closestPairOfPoints(points) << std::endl; // 1.41421...
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

type Point struct {
    X, Y float64
}

func distance(p1, p2 Point) float64 {
    return math.Sqrt(math.Pow(p1.X-p2.X, 2) + math.Pow(p1.Y-p2.Y, 2))
}

func bruteForceClosestPair(points []Point) float64 {
    minDist := math.Inf(1)
    for i := 0; i < len(points); i++ {
        for j := i + 1; j < len(points); j++ {
            dist := distance(points[i], points[j])
            if dist < minDist {
                minDist = dist
            }
        }
    }
    return minDist
}

func closestPairRecursive(pointsSortedX []Point) float64 {
    n := len(pointsSortedX)
    if n <= 3 {
        return bruteForceClosestPair(pointsSortedX)
    }

    mid := n / 2
    midPoint := pointsSortedX[mid]

    leftHalf := pointsSortedX[:mid]
    rightHalf := pointsSortedX[mid:]

    dLeft := closestPairRecursive(leftHalf)
    dRight := closestPairRecursive(rightHalf)
    d := math.Min(dLeft, dRight)

    // Build a strip of points close to the median line
    strip := []Point{}
    for _, p := range pointsSortedX {
        if math.Abs(p.X-midPoint.X) < d {
            strip = append(strip, p)
        }
    }

    // Sort the strip by y-coordinate
    sort.Slice(strip, func(i, j int) bool {
        return strip[i].Y < strip[j].Y
    })
    
    // Check for closer pairs in the strip
    for i := 0; i < len(strip); i++ {
        for j := i + 1; j < len(strip); j++ {
            // Break if y-distance is greater than d
            if (strip[j].Y - strip[i].Y) >= d {
                break
            }
            dist := distance(strip[i], strip[j])
            if dist < d {
                d = dist
            }
        }
    }

    return d
}

func closestPairOfPoints(points []Point) float64 {
    if len(points) < 2 {
        return math.Inf(1)
    }
    
    // Initial sort by x-coordinate
    sort.Slice(points, func(i, j int) bool {
        return points[i].X < points[j].X
    })
    
    return closestPairRecursive(points)
}

// func main() {
//     points := []Point{
//         {X: 2, Y: 3}, {X: 12, Y: 30}, {X: 40, Y: 50},
//         {X: 5, Y: 1}, {X: 12, Y: 10}, {X: 3, Y: 4},
//     }
//     fmt.Println("Closest distance:", closestPairOfPoints(points)) // 1.41421356...
// }
```

### D

```d
import std.stdio;
import std.array;
import std.algorithm; // For std.algorithm.sort, min
import std.math; // For sqrt, fabs

struct Point {
    double x, y;
}

double distance(Point p1, Point p2) {
    return sqrt(pow(p1.x - p2.x, 2) + pow(p1.y - p2.y, 2));
}

double bruteForceClosestPair(Point[] points) {
    double min_dist = double.infinity;
    for (size_t i = 0; i < points.length; ++i) {
        for (size_t j = i + 1; j < points.length; ++j) {
            double dist = distance(points[i], points[j]);
            if (dist < min_dist) {
                min_dist = dist;
            }
        }
    }
    return min_dist;
}

double closestPairRecursive(Point[] pointsSortedX) {
    auto n = pointsSortedX.length;
    if (n <= 3) {
        return bruteForceClosestPair(pointsSortedX);
    }

    auto mid = n / 2;
    auto midPoint = pointsSortedX[mid];

    auto leftHalf = pointsSortedX[0 .. mid];
    auto rightHalf = pointsSortedX[mid .. $];

    auto dLeft = closestPairRecursive(leftHalf.dup); // Use .dup to create copies
    auto dRight = closestPairRecursive(rightHalf.dup);
    double d = min(dLeft, dRight);

    // Build a strip of points close to the median line
    Point[] strip;
    foreach (p; pointsSortedX) {
        if (fabs(p.x - midPoint.x) < d) {
            strip ~= p;
        }
    }

    // Sort the strip by y-coordinate
    strip.sort!((a, b) => a.y < b.y);
    
    // Check for closer pairs in the strip
    for (size_t i = 0; i < strip.length; ++i) {
        for (size_t j = i + 1; j < strip.length; ++j) {
            // Break if y-distance is greater than d
            if ((strip[j].y - strip[i].y) >= d) {
                break;
            }
            double dist = distance(strip[i], strip[j]);
            if (dist < d) {
                d = dist;
            }
        }
    }

    return d;
}

double closestPairOfPoints(Point[] points) {
    if (points.length < 2) {
        return double.infinity;
    }
    
    // Initial sort by x-coordinate
    points.sort!((a, b) => a.x < b.x);
    
    return closestPairRecursive(points);
}

// void main() {
//     Point[] points = [
//         Point(2, 3), Point(12, 30), Point(40, 50),
//         Point(5, 1), Point(12, 10), Point(3, 4)
//     ];
//     writeln("Closest distance: ", closestPairOfPoints(points)); // 1.41421...
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

The `Closest Pair of Points` algorithm uses `divide and conquer` to recursively find the smallest distance, with a crucial merge step to handle pairs spanning the two halves.

---

**`closest_pair_of_points(points)` Function (Main function):**
- Handles the edge case of fewer than two points.
- Performs a one-time sort of all points by their x-coordinate. This is a key preprocessing step that enables efficient partitioning.
- Calls the recursive helper function `closest_pair_recursive`.

**`closest_pair_recursive(points_sorted_x)` Function:**
- **Base Case:** If the number of points `n` is small (e.g., <= 3), it uses a simple `brute-force` approach to find the closest pair, which is efficient for small inputs.
- **Divide:** The sorted array of points is divided into two halves, `leftHalf` and `rightHalf`, at the `median` point `midPoint`.
- **Conquer:** The function is called recursively on both `leftHalf` and `rightHalf` to find the minimum distance in each half (`d_left` and `d_right`).
- **Combine:** The minimum distance found so far, `d`, is `min(d_left, d_right)`.
- **Merge Step:**
- A "strip" is created containing all points from `points_sorted_x` that are within a horizontal distance `d` from the `midPoint`.
- The `strip` is then sorted by y-coordinate. This allows us to efficiently check for closer pairs across the divide.
- For each point `p` in the `strip`, the algorithm checks its distance to the next few points in the `strip`. The inner loop is optimized to break if the y-distance alone is already greater than `d`, avoiding unnecessary distance calculations.
- If a closer pair is found, `d` is updated.

    </li>
- The final minimum distance `d` is returned.

[Back to Implementation](#implementation)

## Applications

### Application

The `Closest Pair of Points Problem` is a fundamental problem in computational geometry with applications in various domains:
- **Air Traffic Control:** Detecting airplanes that are too close to each other to prevent collisions.
- **Computer Graphics and Vision:** Used in image processing, pattern recognition, and for optimizing rendering of objects in 3D scenes.
- **Geographic Information Systems (GIS):** Finding the closest pair of locations, such as the closest pair of cities or points of interest.
- **Molecular Modeling:** Finding the closest pair of atoms or molecules in a simulation, which can be important for understanding interactions.
- **Data Analysis and Clustering:** As a step in certain clustering algorithms where proximity of data points is a key factor.
- **Robotics:** For collision detection and path planning, where a robot needs to be aware of the closest obstacles.

