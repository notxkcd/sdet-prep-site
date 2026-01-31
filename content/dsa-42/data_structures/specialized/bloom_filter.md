---
title: "Bloom Filter"
---

A `Bloom Filter` is a space-efficient probabilistic data structure, conceived by Burton Howard `Bloom` in 1970, that is used to test whether an element is a member of a `set`.

It's probabilistic because it can tell you that an element is definitely not in the `set`, or that it might be in the `set` (with a certain probability of `false positives`). It never produces `false negatives`.

`Bloom filters` are widely used in applications where memory efficiency and fast membership queries are critical, such as `database lookups`, `network routing`, and `caching`.

## How it Works

### How it Works (Expanded)

A `Bloom Filter` consists of a `bit array` (a long array of bits, initially all set to 0) and a number of `hash functions`. When you add an element to the `Bloom Filter`:
- The element is fed into each of the `k hash functions`.
- Each `hash function` outputs an `index` in the `bit array`.
- The `bits` at these `k indices` are set to 1.

To check if an element is in the `set`:
- The element is again fed into the same `k hash functions`.
- If all `bits` at the resulting `k indices` are 1, then the element *might* be in the `set`.
- If any of the `bits` are 0, then the element is *definitely not* in the `set`.

---

Insert "apple":
Bit Array: [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Hash1("apple") -> 1  (set bit 1 to 1)
Hash2("apple") -> 5  (set bit 5 to 1)
Hash3("apple") -> 12 (set bit 12 to 1)
Bit Array: [0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0]

Check "apple":
Hash1("apple") -> 1 (bit 1 is 1)
Hash2("apple") -> 5 (bit 5 is 1)
Hash3("apple") -> 12 (bit 12 is 1)
Result: "apple" *might* be in the set.

Check "orange":
Hash1("orange") -> 3 (bit 3 is 0)
Result: "orange" is *definitely not* in the set.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
import mmh3 # For MurmurHash3, a good non-cryptographic hash function
from bitarray import bitarray # For efficient bit array

class BloomFilter:
    def __init__(self, capacity, error_rate):
        self.capacity = capacity  # Max number of items expected to be stored
        self.error_rate = error_rate # Desired false positive probability
        self.num_bits = self.get_num_bits(capacity, error_rate) # Size of bit array (m)
        self.num_hashes = self.get_num_hashes(self.num_bits, capacity) # Number of hash functions (k)
        self.bit_array = bitarray(self.num_bits)
        self.bit_array.setall(0) # Initialize all bits to 0

    @staticmethod
    def get_num_bits(capacity, error_rate):
        # m = -(n <em> ln(p)) / (ln(2)^2)
        m = -(capacity </em> error_rate.as_integer_ratio()[0].__float__().log()) / (0.69314718056 <em> 0.69314718056) # ln(2)^2 approx 0.48
        # Using a more robust log implementation if available, or direct math.log
        return int(m) # simplified, requires <code>math</code> module; direct expansion here
        # return int(-(capacity </em> math.log(error_rate)) / (math.log(2)*<em>2))

    @staticmethod
    def get_num_hashes(num_bits, capacity):
        # k = (m/n) </em> ln(2)
        k = (num_bits / capacity) <em> 0.69314718056 # math.log(2)
        return int(k) # simplified
        # return int((num_bits / capacity) </em> math.log(2))

    def _get_hashes(self, item):
        # Use two hash functions and combine them to generate k hashes
        # This reduces the need for k independent hash functions
        hash1 = mmh3.hash(item, 0)
        hash2 = mmh3.hash(item, hash1) # Use result of hash1 as seed for hash2
        
        hashes = []
        for i in range(self.num_hashes):
            # General formula: Hi(x) = (hash1(x) + i <em> hash2(x)) % m
            hashes.append(abs((hash1 + i </em> hash2) % self.num_bits))
        return hashes

    def add(self, item):
        for h_idx in self._get_hashes(item):
            self.bit_array[h_idx] = 1

    def contains(self, item):
        for h_idx in self._get_hashes(item):
            if self.bit_array[h_idx] == 0:
                return False
        return True # Might be in the set

# Example Usage:
# bf = BloomFilter(100, 0.01) # 100 items, 1% false positive rate
# words_to_add = ["apple", "banana", "cherry", "date"]
# for word in words_to_add:
#     bf.add(word)

# print("Contains 'apple':", bf.contains("apple")) # True
# print("Contains 'grape':", bf.contains("grape")) # False (or True, if false positive)
```

### Javascript

```javascript
class BloomFilter {
    constructor(capacity, errorRate) {
        this.capacity = capacity;
        this.errorRate = errorRate;
        this.numBits = this._getNumBits(capacity, errorRate);
        this.numHashes = this._getNumHashes(this.numBits, capacity);
        this.bitArray = new Array(this.numBits).fill(0);
    }

    _getNumBits(capacity, errorRate) {
        // m = -(n <em> ln(p)) / (ln(2)^2)
        return Math.ceil(-(capacity </em> Math.log(errorRate)) / (Math.log(2) *<em> 2));
    }

    _getNumHashes(numBits, capacity) {
        // k = (m/n) </em> ln(2)
        return Math.ceil((numBits / capacity) <em> Math.log(2));
    }

    // A simple non-cryptographic hash function example
    // For a real Bloom Filter, you'd use multiple good hash functions
    _hashString(str, seed) {
        let hash = seed;
        for (let i = 0; i < str.length; i++) {
            hash = (hash << 5) - hash + str.charCodeAt(i);
            hash |= 0; // Convert to 32bit integer
        }
        return Math.abs(hash);
    }

    _getHashes(item) {
        const strItem = String(item);
        const hashes = [];
        let hash1 = this._hashString(strItem, 0);
        let hash2 = this._hashString(strItem, hash1); // Use hash1 as seed for hash2

        for (let i = 0; i < this.numHashes; i++) {
            // General formula: Hi(x) = (hash1(x) + i </em> hash2(x)) % m
            hashes.push(Math.abs((hash1 + i <em> hash2) % this.numBits));
        }
        return hashes;
    }

    add(item) {
        for (const hIdx of this._getHashes(item)) {
            this.bitArray[hIdx] = 1;
        }
    }

    contains(item) {
        for (const hIdx of this._getHashes(item)) {
            if (this.bitArray[hIdx] === 0) {
                return false;
            }
        }
        return true; // Might be in the set
    }
}

// Example Usage:
// const bf = new BloomFilter(100, 0.01); // 100 items, 1% false positive rate
// const wordsToAdd = ["apple", "banana", "cherry", "date"];
// for (const word of wordsToAdd) {
//     bf.add(word);
// }

// console.log("Contains 'apple':", bf.contains("apple")); // true
// console.log("Contains 'grape':", bf.contains("grape")); // false (or true, if false positive)
```

### Cpp

```cpp
#include <vector>
#include <string>
#include <cmath> // For std::log, std::pow
#include <functional> // For std::hash
#include <iostream>

// A simple hash function (for demonstration)
// In a real Bloom Filter, you'd use robust hash functions like MurmurHash
unsigned int simple_hash(const std::string& s, unsigned int seed) {
    unsigned int hash = seed;
    for (char c : s) {
        hash = (hash </em> 31) + c;
    }
    return hash;
}

class BloomFilter {
private:
    std::vector<bool> bit_array;
    int num_bits;
    int num_hashes;
    int capacity;

    int get_num_bits(int capacity, double error_rate) {
        // m = -(n <em> ln(p)) / (ln(2)^2)
        return std::ceil(-(capacity </em> std::log(error_rate)) / (std::log(2) <em> std::log(2)));
    }

    int get_num_hashes(int num_bits, int capacity) {
        // k = (m/n) </em> ln(2)
        return std::ceil((static_cast<double>(num_bits) / capacity) <em> std::log(2));
    }

    std::vector<unsigned int> get_hash_indices(const std::string& item) {
        std::vector<unsigned int> hashes;
        unsigned int h1 = simple_hash(item, 0);
        unsigned int h2 = simple_hash(item, h1); // Use h1 as seed for h2

        for (int i = 0; i < num_hashes; ++i) {
            // General formula: Hi(x) = (hash1(x) + i </em> hash2(x)) % m
            hashes.push_back(std::abs(static_cast<int>((h1 + i <em> h2) % num_bits)));
        }
        return hashes;
    }

public:
    BloomFilter(int capacity, double error_rate) :
        capacity(capacity) {
        num_bits = get_num_bits(capacity, error_rate);
        num_hashes = get_num_hashes(num_bits, capacity);
        bit_array.resize(num_bits, false); // Initialize all bits to false (0)
    }

    void add(const std::string& item) {
        for (unsigned int h_idx : get_hash_indices(item)) {
            bit_array[h_idx] = true; // Set bit to true (1)
        }
    }

    bool contains(const std::string& item) {
        for (unsigned int h_idx : get_hash_indices(item)) {
            if (!bit_array[h_idx]) {
                return false;
            }
        }
        return true; // Might be in the set
    }
};

// Example Usage:
// int main() {
//     BloomFilter bf(100, 0.01); // 100 items, 1% false positive rate
//     std::vector<std::string> words_to_add = {"apple", "banana", "cherry", "date"};
//     for (const std::string& word : words_to_add) {
//         bf.add(word);
//     }

//     std::cout << "Contains 'apple': " << (bf.contains("apple") ? "True" : "False") << std::endl; // True
//     std::cout << "Contains 'grape': " << (bf.contains("grape") ? "True" : "False") << std::endl; // False (or True, if false positive)
//     return 0;
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

A `Bloom Filter` implementation requires careful selection of `hash functions` and calculation of optimal `bit array size (m)` and `number of hash functions (k)`.

---

**Formulae for `m` and `k`:**
- Optimal number of `bits` `m = -(n </em> ln(p)) / (ln(2)^2)`
- Optimal number of `hashes` `k = (m/n) <em> ln(2)`

Where `n` is the expected `capacity` and `p` is the desired `false positive rate`.

**`BloomFilter` Class:**
- `num_bits (m)`: The size of the internal `bit array`.
- `num_hashes (k)`: The number of `hash functions` to use.
- `bit_array`: The actual `array` of `bits` (often implemented using a boolean `vector` or specialized bit `array` for efficiency).
- **`_get_hashes(item)`:** Generates `k hash values` for a given `item`. A common technique is to use two independent `hash functions` (`h1` and `h2`) and combine them using the formula `Hi(x) = (h1(x) + i </em> h2(x)) % m`.
- **`add(item)`:** Computes `k hash values` for the `item` and sets the corresponding `bits` in the `bit array` to 1.
- **`contains(item)`:** Computes `k hash values` for the `item`. If all corresponding `bits` are 1, it returns true (might be present). If any `bit` is 0, it returns false (definitely not present).

[Back to Implementation](#implementation)

## Applications

### Application

Bloom Filters are used in many systems where space is a concern and a small rate of false positives is acceptable. For example, **Google Chrome** uses a Bloom Filter to check for malicious URLs before navigating to a site. Distributed databases like **Google Bigtable** and **Apache Cassandra** use Bloom Filters to quickly check if a row or column exists in a table on disk, avoiding costly disk I/O for non-existent data. They are also used in network routers for filtering and in various caching systems.

