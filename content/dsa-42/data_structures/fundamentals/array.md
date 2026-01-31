---
title: "Array / Dynamic Array"
---

An array is the most fundamental data structure. Think of it as a numbered row of boxes, where each box can hold one piece of information. You can instantly access any box if you know its number (its `index`).

A `static array` has a fixed size. A `dynamic array` (like Python's `list` or C++'s `std::vector`) can automatically grow when it gets full, making it much more flexible.

## How it Works

### How it Works (Expanded)

Arrays store elements in a contiguous block of memory. This is their superpower and their main limitation.

---

Memory: | Box 0 | Box 1 | Box 2 | Box 3 | ...
Index:      0       1       2       3
Value:     'A'     'B'     'C'     'D'

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
# Python's list is a dynamic array by default.
my_array = [10, 20, 30, 40]

# Access (O(1))
print(my_array[2])  # Output: 30

# Append (Amortized O(1))
my_array.append(50)
print(my_array) # Output: [10, 20, 30, 40, 50]

# Insert (O(n))
my_array.insert(1, 15)
print(my_array) # Output: [10, 15, 20, 30, 40, 50]

# Delete (O(n))
del my_array[3]
print(my_array) # Output: [10, 15, 20, 40, 50]
```

### Javascript

```javascript
// JavaScript's Array is a dynamic array.
let myArray = [10, 20, 30, 40];

// Access (O(1))
console.log(myArray[2]); // Output: 30

// Append (Amortized O(1))
myArray.push(50);
console.log(myArray); // Output: [10, 20, 30, 40, 50]

// Insert at start (O(n))
myArray.unshift(5);
console.log(myArray); // Output: [5, 10, 20, 30, 40, 50]

// Delete from middle (O(n))
myArray.splice(3, 1); // Removes 1 element at index 3
console.log(myArray); // Output: [5, 10, 20, 40, 50]
```

### Cpp

```cpp
#include <iostream>
#include <vector> // std::vector is C++'s dynamic array

int main() {
    std::vector<int> myArray = {10, 20, 30, 40};

    // Access (O(1))
    std::cout << "Element at index 2: " << myArray[2] << std::endl;

    // Append (Amortized O(1))
    myArray.push_back(50);

    // Insert (O(n))
    myArray.insert(myArray.begin() + 1, 15);

    // Delete (O(n))
    myArray.erase(myArray.begin() + 3);

    // Print all elements
    for (int i : myArray) {
        std::cout << i << " ";
    }
    std::cout << std::endl;
    // Expected output: 10 15 20 40 50 
    return 0;
}
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

Most modern languages provide a built-in dynamic array.

---

**Access:** Using bracket notation `array[index]` is a direct memory offset calculation, making it incredibly fast.

**Append:** Adding to the end (`push_back`, `append`, `push`) is usually fast. The array keeps extra capacity. Only when that capacity is used up does it need to resize, which is a slow `O(n)` operation. This is called "amortized `O(1)`" time.

<strong>Insert/Delete:</b> Adding or removing from the middle or beginning is slow because it requires shifting all subsequent elements (`O(n)`).

[Back to Implementation](#implementation)

