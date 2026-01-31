---
title: "Hash Table"
---

A Hash Table (or `Hash Map`) is like a magical filing cabinet. Instead of searching for a folder manually, you give it a '`key`' (like a person's name), and it instantly gives you back the '`value`' (like their phone number).

They are one of the most useful data structures, providing incredibly fast lookups, insertions, and deletions.

## How it Works

### How it Works (Expanded)

A Hash Table uses a 'hash function' to compute an index into an array of 'buckets' or 'slots', from which the desired value can be found.
- **`Key`:** The identifier you want to look up (e.g., '`username`').
- **Hash Function:** A function that takes the `key` and turns it into an integer index. `hash('username') -> 123`
- **Array (Buckets):** An array where values are stored. The `index` from the hash function points to a location in this array.

---

Key -> | Hash Function | -> Index [Bucket] -> Value
'name' -> | f(x) = ...  | -> 3   [ | | |*| | ] -> 'Shahid'

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
# Python's dictionary is a highly optimized hash table.
my_hash_table = {}

# Insert/Update (O(1) on average)
my_hash_table['name'] = 'Shahid'
my_hash_table['age'] = 42
print("Hash Table:", my_hash_table)

# Lookup (O(1) on average)
print("Name:", my_hash_table['name'])

# Deletion (O(1) on average)
del my_hash_table['age']
print("After deletion:", my_hash_table)

# Check for key
if 'name' in my_hash_table:
    print("Key 'name' exists.")
```

### Javascript

```javascript
// JavaScript's Object and Map can be used as hash tables. Map is preferred.
let myHashTable = new Map();

// Insert/Update (O(1) on average)
myHashTable.set('name', 'Shahid');
myHashTable.set('age', 42);
console.log("Hash Table:", myHashTable);

// Lookup (O(1) on average)
console.log("Name:", myHashTable.get('name'));

// Deletion (O(1) on average)
myHashTable.delete('age');
console.log("After deletion:", myHashTable);

// Check for key
if (myHashTable.has('name')) {
    console.log("Key 'name' exists.");
}
```

### Cpp

```cpp
#include <iostream>
#include <unordered_map> // C++'s hash table
#include <string>

int main() {
    std::unordered_map<std::string, std::string> myHashTable;

    // Insert/Update (O(1) on average)
    myHashTable["name"] = "Shahid";
    myHashTable["project"] = "DSA-42";
    
    // Lookup (O(1) on average)
    std::cout << "Name: " << myHashTable["name"] << std::endl;

    // Deletion (O(1) on average)
    myHashTable.erase("project");

    // Check for key
    if (myHashTable.count("name")) {
        std::cout << "Key 'name' exists." << std::endl;
    }

    // Iterate and print
    for (const auto& pair : myHashTable) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }
    return 0;
}
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

Like arrays, hash tables are so fundamental that they are built into most standard libraries.

---

**Python:** The `dict` (`dictionary`) type is the built-in hash table. Syntax is clean and simple.

**JavaScript:** While plain `Object`s can work, the `Map` object, introduced in ES6, is the preferred way to create a hash table/map. It avoids prototype-related issues and provides clean methods like `.get()`, `.set()`, `.has()`, and `.delete()`.

**C++:** The STL provides `std::unordered_map`. It operates similarly to Python's dictionary, using bracket notation for access and insertion, and the `.erase()` method for deletion.

[Back to Implementation](#implementation)

