---
title: "Set"
---

Imagine a mathematical `set` – a collection of distinct elements, where the order doesn't matter and duplicates are not allowed. That's exactly what a `Set` data structure provides in computer science.

`Sets` are incredibly useful when you need to store unique items and quickly check for membership (if an item is in the `set`).

## How it Works

### How it Works (Expanded)

`Sets` are typically implemented using hash tables or balanced binary search trees internally, which allows for their efficient operations.

---

Properties of a `Set`:
- **Uniqueness:** All elements in a `set` must be unique. Adding a duplicate element has no effect.
- **Unordered:** Elements in a `set` do not have a specific order.
- **Membership Testing:** Very fast checking if an element exists in the `set`.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
# Python's built-in 'set' type.
my_set = {1, 2, 3, 4, 5}

# Add (O(1) on average)
my_set.add(6)
my_set.add(3) # No effect, 3 is already in the set
print("Set after adding:", my_set) # Order might vary: {1, 2, 3, 4, 5, 6}

# Remove (O(1) on average)
my_set.remove(2)
print("Set after removing 2:", my_set) # {1, 3, 4, 5, 6}

# Check membership (O(1) on average)
print("Is 4 in set?", 4 in my_set)   # Output: True
print("Is 7 in set?", 7 in my_set)   # Output: False

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Union:", set_a.union(set_b))         # {1, 2, 3, 4, 5, 6}
print("Intersection:", set_a.intersection(set_b)) # {3, 4}
print("Difference (A-B):", set_a.difference(set_b)) # {1, 2}
```

### Javascript

```javascript
// JavaScript's built-in 'Set' object.
let mySet = new Set([1, 2, 3, 4, 5]);

// Add (O(1) on average)
mySet.add(6);
mySet.add(3); // No effect, 3 is already in the Set
console.log("Set after adding:", mySet); // Output: Set(6) {1, 2, 3, 4, 5, 6}

// Delete (O(1) on average)
mySet.delete(2);
console.log("Set after deleting 2:", mySet); // Set(5) {1, 3, 4, 5, 6}

// Check membership (O(1) on average)
console.log("Is 4 in Set?", mySet.has(4));   // Output: true
console.log("Is 7 in Set?", mySet.has(7));   // Output: false

// Set operations (manual for now, but often libraries provide these)
let setA = new Set([1, 2, 3, 4]);
let setB = new Set([3, 4, 5, 6]);

function unionSets(set1, set2) {
    return new Set([...set1, ...set2]);
}

function intersectionSets(set1, set2) {
    return new Set([...set1].filter(x => set2.has(x)));
}

function differenceSets(set1, set2) {
    return new Set([...set1].filter(x => !set2.has(x)));
}

console.log("Union:", unionSets(setA, setB));         // Set(6) {1, 2, 3, 4, 5, 6}
console.log("Intersection:", intersectionSets(setA, setB)); // Set(2) {3, 4}
console.log("Difference (A-B):", differenceSets(setA, setB)); // Set(2) {1, 2}
```

### Cpp

```cpp
#include <iostream>
#include <set> // Standard Library Set (implemented using a Red-Black Tree)
#include <algorithm> // For std::set_union, std::set_intersection, etc.
#include <vector> // For temporary storage for set operations

int main() {
    std::set<int> mySet;

    // Add (O(log n))
    mySet.insert(1);
    mySet.insert(2);
    mySet.insert(3);
    mySet.insert(4);
    mySet.insert(5);
    mySet.insert(3); // No effect, 3 is already in the set
    
    std::cout << "Set elements:";
    for (int x : mySet) {
        std::cout << " " << x;
    }
    std::cout << std::endl; // Output: 1 2 3 4 5

    // Remove (O(log n))
    mySet.erase(2);
    std::cout << "Set after erasing 2:";
    for (int x : mySet) {
        std::cout << " " << x;
    }
    std::cout << std::endl; // Output: 1 3 4 5

    // Check membership (O(log n))
    std::cout << "Is 4 in set? " << (mySet.count(4) ? "True" : "False") << std::endl; // Output: True
    std::cout << "Is 7 in set? " << (mySet.count(7) ? "True" : "False") << std::endl; // Output: False

    // Set operations
    std::set<int> setA = {1, 2, 3, 4};
    std::set<int> setB = {3, 4, 5, 6};
    std::vector<int> result;

    // Union
    std::set_union(setA.begin(), setA.end(),
                   setB.begin(), setB.end(),
                   std::back_inserter(result));
    std::cout << "Union:";
    for (int x : result) std::cout << " " << x;
    std::cout << std::endl; // Output: 1 2 3 4 5 6
    result.clear();

    // Intersection
    std::set_intersection(setA.begin(), setA.end(),
                          setB.begin(), setB.end(),
                          std::back_inserter(result));
    std::cout << "Intersection:";
    for (int x : result) std::cout << " " << x;
    std::cout << std::endl; // Output: 3 4
    result.clear();

    // Difference (A-B)
    std::set_difference(setA.begin(), setA.end(),
                        setB.begin(), setB.end(),
                        std::back_inserter(result));
    std::cout << "Difference (A-B):";
    for (int x : result) std::cout << " " << x;
    std::cout << std::endl; // Output: 1 2

    return 0;
}
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

`Sets` are a core feature in many modern programming languages, often implemented with high efficiency.

---

**Python:** Has a built-in `set` type. Provides methods like `add()`, `remove()`, and operators/methods for `union` (`|` or `union()`), `intersection` (`&` or `intersection()`), and `difference` (`-` or `difference()`).

**JavaScript:** The `Set` object allows you to store unique values of any type. It has methods like `add()`, `delete()`, and `has()`. `Set` operations (`union`, `intersection`, `difference`) are typically implemented manually using `array spread` syntax and `filter()`, as shown in the example.

**C++:** The STL provides `std::set` (implemented as a balanced binary search tree, offering `O(log n)` operations) and `std::unordered_set` (implemented as a hash table, offering `O(1)` on average operations). `Set` operations like `union`, `intersection`, and `difference` are available as algorithms in `<algorithm>`.

[Back to Implementation](#implementation)

