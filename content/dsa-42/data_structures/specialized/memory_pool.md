---
title: "Memory Pool"
---

A `Memory Pool` (also known as an `Object Pool`) is a design pattern used to manage memory more efficiently in situations where a large number of objects are created and destroyed frequently. Instead of allocating and deallocating memory for each object individually, a `Memory Pool` pre-allocates a fixed block of memory and then manages it internally.

This approach significantly reduces the overhead associated with frequent system-level `memory allocation` and `deallocation` calls (like `malloc`/`free` in C/C++ or `new`/`delete`). It's particularly useful in performance-critical applications like game development, embedded systems, and high-performance computing.

## How it Works

### How it Works (Expanded)

A `Memory Pool` typically works by:
- **Pre-allocation:** At initialization, a large contiguous block of `memory` is allocated from the operating system (or standard heap). This block is then divided into smaller, uniform-sized chunks, each capable of holding one `object` of a specific type.
- **Internal Management:** The `pool` maintains a `list` of available (free) `memory chunks`. When an application requests an `object`, the `pool` simply returns a free `chunk` from its internal `list`. When an `object` is "destroyed" or no longer needed, its `memory chunk` is returned to the `pool`'s free `list`, rather than being returned to the operating system.

---

Initial State (Pool of 4 objects):
[Obj1_Free] -> [Obj2_Free] -> [Obj3_Free] -> [Obj4_Free] -> NULL

After requesting 2 objects:
[Obj1_Used] [Obj2_Used] [Obj3_Free] -> [Obj4_Free] -> NULL

After releasing Obj1:
[Obj1_Free] -> [Obj3_Free] -> [Obj4_Free] -> NULL
       (Obj2 is still Used)

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
# Conceptual Object Pool in Python (illustrates the idea, Python's GC handles memory)

class ReusableObject:
    def __init__(self, obj_id):
        self.obj_id = obj_id
        self.in_use = False
        print(f"Object {self.obj_id} created.")

    def reset(self):
        # Reset object state for reuse
        print(f"Object {self.obj_id} reset.")
        self.in_use = False

    def use(self):
        self.in_use = True
        print(f"Object {self.obj_id} is now in use.")


class ObjectPool:
    def __init__(self, pool_size):
        self._pool = []
        for i in range(pool_size):
            self._pool.append(ReusableObject(i))
        self._free_objects = list(self._pool) # All objects initially free

    def acquire_object(self):
        if not self._free_objects:
            print("Pool exhausted, cannot acquire object.")
            return None
        obj = self._free_objects.pop(0) # Get first free object
        obj.in_use = True
        print(f"Acquired object {obj.obj_id}.")
        return obj

    def release_object(self, obj):
        if obj is not None and obj.in_use:
            obj.reset()
            self._free_objects.append(obj) # Return to free list
            print(f"Released object {obj.obj_id}.")
        else:
            print("Cannot release object not in use or invalid.")

# Example Usage:
# pool = ObjectPool(3)

# obj_a = pool.acquire_object()
# obj_b = pool.acquire_object()
# obj_c = pool.acquire_object()
# obj_d = pool.acquire_object() # This will fail

# pool.release_object(obj_a)
# obj_e = pool.acquire_object() # Should get obj_a back
```

### Javascript

```javascript
// Conceptual Object Pool in JavaScript (illustrates the idea)

class ReusableObject {
    constructor(objId) {
        this.objId = objId;
        this.inUse = false;
        console.log(<code>Object ${this.objId} created.</code>);
    }

    reset() {
        // Reset object state for reuse
        console.log(<code>Object ${this.objId} reset.</code>);
        this.inUse = false;
    }

    use() {
        this.inUse = true;
        console.log(<code>Object ${this.objId} is now in use.</code>);
    }
}

class ObjectPool {
    constructor(poolSize) {
        this._pool = [];
        for (let i = 0; i < poolSize; i++) {
            this._pool.push(new ReusableObject(i));
        }
        this._freeObjects = [...this._pool]; // All objects initially free
    }

    acquireObject() {
        if (this._freeObjects.length === 0) {
            console.log("Pool exhausted, cannot acquire object.");
            return null;
        }
        const obj = this._freeObjects.shift(); // Get first free object
        obj.inUse = true;
        console.log(<code>Acquired object ${obj.objId}.</code>);
        return obj;
    }

    releaseObject(obj) {
        if (obj && obj.inUse) {
            obj.reset();
            this._freeObjects.push(obj); // Return to free list
            console.log(<code>Released object ${obj.objId}.</code>);
        } else {
            console.log("Cannot release object not in use or invalid.");
        }
    }
}

// Example Usage:
// const pool = new ObjectPool(3);

// const objA = pool.acquireObject();
// const objB = pool.acquireObject();
// const objC = pool.acquireObject();
// const objD = pool.acquireObject(); // This will fail

// pool.releaseObject(objA);
// const objE = pool.acquireObject(); // Should get objA back
```

### Cpp

```cpp
#include <iostream>
#include <vector>
#include <memory> // For std::shared_ptr or std::unique_ptr for real-world scenarios

// A simple reusable object
class ReusableObject {
private:
    int id;
    bool in_use;
public:
    ReusableObject(int obj_id) : id(obj_id), in_use(false) {
        std::cout << "Object " << id << " created." << std::endl;
    }

    void reset() {
        // Reset object state for reuse
        std::cout << "Object " << id << " reset." << std::endl;
        in_use = false;
    }

    void use() {
        in_use = true;
        std::cout << "Object " << id << " is now in use." << std::endl;
    }

    bool isInUse() const { return in_use; }
    int getId() const { return id; }
};

// A simple object pool
class ObjectPool {
private:
    std::vector<ReusableObject</em>> pool;
    std::vector<ReusableObject<em>> free_objects; // Store pointers to free objects
    int pool_size;

public:
    ObjectPool(int size) : pool_size(size) {
        for (int i = 0; i < pool_size; ++i) {
            ReusableObject</em> obj = new ReusableObject(i);
            pool.push_back(obj);
            free_objects.push_back(obj); // Initially all objects are free
        }
    }

    ~ObjectPool() {
        // Deallocate all objects created by the pool
        for (ReusableObject<em> obj : pool) {
            delete obj;
        }
        pool.clear();
        free_objects.clear();
    }

    ReusableObject</em> acquireObject() {
        if (free_objects.empty()) {
            std::cout << "Pool exhausted, cannot acquire object." << std::endl;
            return nullptr;
        }
        ReusableObject<em> obj = free_objects.back(); // Get last free object
        free_objects.pop_back();                   // Remove from free list
        obj->use();
        std::cout << "Acquired object " << obj->getId() << "." << std::endl;
        return obj;
    }

    void releaseObject(ReusableObject</em> obj) {
        if (obj != nullptr && obj->isInUse()) {
            obj->reset();
            free_objects.push_back(obj); // Return to free list
            std::cout << "Released object " << obj->getId() << "." << std::endl;
        } else {
            std::cout << "Cannot release object not in use or invalid." << std::endl;
        }
    }
};

// Example Usage:
// int main() {
//     ObjectPool pool(3);

//     ReusableObject<em> objA = pool.acquireObject();
//     ReusableObject</em> objB = pool.acquireObject();
//     ReusableObject<em> objC = pool.acquireObject();
//     ReusableObject</em> objD = pool.acquireObject(); // This will fail

//     pool.releaseObject(objA);
//     ReusableObject* objE = pool.acquireObject(); // Should get objA back
    
//     // Note: Objects are automatically deallocated when pool goes out of scope.
//     return 0;
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

A `Memory Pool` is typically implemented with a `class` that manages an `array` of pre-allocated `objects` or raw `memory` blocks.

---

**`ReusableObject` Class:** A simple `class` representing the type of `object` the `pool` will manage.
- `obj_id`: An identifier for the `object`.
- `in_use`: A boolean flag to track if the `object` is currently active.
- `reset()`: A method to reset the `object`'s state when it's returned to the `pool`.
- `use()`: A method to mark the `object` as in use.

**`ObjectPool` Class:** The core of the `Memory Pool`.
- `_pool`: A `list`/`vector` holding all the pre-allocated `ReusableObject` instances.
- `_free_objects`: A `list`/`vector` (often a `stack` or `queue` for `O(1)` access) of currently available (free) `ReusableObject`s.
- `pool_size`: The maximum number of `objects` the `pool` can manage.
- **`acquire_object()`:**
- Checks if there are any free `objects` in `_free_objects`.
- If available, it takes an `object` from `_free_objects`, marks it as `in use`, and returns it.
- If the `pool` is exhausted, it returns `None` or throws an error.

    </li>
- **`release_object(obj)`:**
- Takes a used `object`, calls its `reset()` method to clean its state.
- Adds the `object` back to the `_free_objects` `list`.

    </li>

[Back to Implementation](#implementation)

## Applications

### Application

Memory Pools (or Object Pools) are a critical performance optimization in many domains. In **game engines**, they are used to manage frequently created and destroyed objects like bullets, particles, and enemies, avoiding the performance hit of constant memory allocation. **High-performance network servers** use pools to manage connection objects, which are opened and closed at a high frequency. Similarly, in **real-time and embedded systems**, pools provide deterministic, constant-time memory allocation, which is essential for meeting strict timing deadlines and preventing system stalls caused by standard memory management.

