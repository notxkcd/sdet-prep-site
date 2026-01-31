---
title: "Fisher-Yates Shuffle"
---

The `Fisher-Yates Shuffle` is an algorithm for generating a random permutation of a finite sequence. In simple terms, it shuffles an array in an unbiased way, meaning every possible permutation is equally likely. The modern version of the algorithm, often attributed to Richard Durstenfeld and popularized by Donald Knuth, is an in-place shuffle that is both efficient and easy to implement.

The algorithm iterates through the array from the end to the beginning. In each step, it swaps the current element with a randomly chosen element from the unshuffled part of the array (including itself).

## How it Works

### How it Works (Expanded)

The `Fisher-Yates Shuffle` works by building up a random permutation one element at a time. It ensures that at each step `i`, the element placed at index `i` has an equal chance of being any of the elements from the original array that have not yet been placed.

---

Example: Shuffle Array = [1, 2, 3, 4]

1. Start at last element (index 3).
- i = 3. Pick a random index j from [0, 1, 2, 3]. Say j=1.
- Swap arr[3] and arr[1]. Array becomes: [1, 4, 3, 2].
- Element at index 3 is now fixed.

2. Move to next element (index 2).
- i = 2. Pick a random index j from [0, 1, 2]. Say j=2.
- Swap arr[2] and arr[2]. Array remains: [1, 4, 3, 2].
- Element at index 2 is now fixed.

3. Move to next element (index 1).
- i = 1. Pick a random index j from [0, 1]. Say j=0.
- Swap arr[1] and arr[0]. Array becomes: [4, 1, 3, 2].
- Element at index 1 is now fixed.

4. Loop finishes. Array is shuffled.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
import random

def fisher_yates_shuffle(arr):
    """
    Shuffles an array in-place using the Fisher-Yates shuffle algorithm.
    """
    n = len(arr)
    for i in range(n - 1, 0, -1):
        # Pick a random index from 0 to i
        j = random.randint(0, i)
        
        # Swap arr[i] with the element at random index
        arr[i], arr[j] = arr[j], arr[i]
    return arr

# Example
# my_arr = [1, 2, 3, 4, 5, 6, 7, 8]
# print("Original:", my_arr)
# print("Shuffled:", fisher_yates_shuffle(my_arr))
```

### Javascript

```javascript
function fisherYatesShuffle(arr) {
    /*<em>
     </em> Shuffles an array in-place using the Fisher-Yates shuffle algorithm.
     <em>/
    let n = arr.length;
    for (let i = n - 1; i > 0; i--) {
        // Pick a random index from 0 to i
        const j = Math.floor(Math.random() </em> (i + 1));
        
        // Swap arr[i] with the element at random index
        [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
}

// const myArr = [1, 2, 3, 4, 5, 6, 7, 8];
// console.log("Original:", myArr);
// console.log("Shuffled:", fisherYatesShuffle([...myArr])); // Use spread to avoid modifying original array for demo
```

### Typescript

```typescript
function fisherYatesShuffleTS(arr: any[]): any[] {
    /*<em>
     </em> Shuffles an array in-place using the Fisher-Yates shuffle algorithm.
     <em>/
    let n = arr.length;
    for (let i = n - 1; i > 0; i--) {
        // Pick a random index from 0 to i
        const j = Math.floor(Math.random() </em> (i + 1));
        
        // Swap arr[i] with the element at random index
        [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
}

// const myArrTS: number[] = [1, 2, 3, 4, 5, 6, 7, 8];
// console.log("Original:", myArrTS);
// console.log("Shuffled:", fisherYatesShuffleTS([...myArrTS])); // Use spread to avoid modifying original array for demo
```

### Cpp

```cpp
#include <vector>
#include <iostream>
#include <random>    // For std::mt19937 and std::uniform_int_distribution
#include <algorithm> // For std::swap

void fisherYatesShuffle(std::vector<int>& arr) {
    int n = arr.size();
    
    // Create a random number generator
    std::random_device rd;
    std::mt19937 g(rd());

    for (int i = n - 1; i > 0; i--) {
        // Pick a random index from 0 to i
        std::uniform_int_distribution<int> dist(0, i);
        int j = dist(g);
        
        // Swap arr[i] with the element at random index
        std::swap(arr[i], arr[j]);
    }
}

// int main() {
//     std::vector<int> myArr = {1, 2, 3, 4, 5, 6, 7, 8};
//     std::cout << "Original: ";
//     for (int val : myArr) std::cout << val << " ";
//     std::cout << std::endl;
//     
//     fisherYatesShuffle(myArr);
//     
//     std::cout << "Shuffled: ";
//     for (int val : myArr) std::cout << val << " ";
//     std::cout << std::endl;
//     return 0;
// }
```

### Go

```go
package main

import (
    "fmt"
    "math/rand"
    "time"
)

func fisherYatesShuffle(arr []interface{}) {
    n := len(arr)
    rand.Seed(time.Now().UnixNano())

    for i := n - 1; i > 0; i-- {
        // Pick a random index from 0 to i
        j := rand.Intn(i + 1)
        
        // Swap arr[i] with the element at random index
        arr[i], arr[j] = arr[j], arr[i]
    }
}

// func main() {
//     myArr := []interface{}{1, 2, 3, 4, 5, 6, 7, 8}
//     fmt.Println("Original:", myArr)
//     fisherYatesShuffle(myArr)
//     fmt.Println("Shuffled:", myArr)
// }
```

### D

```d
import std.stdio;
import std.random;
import std.array;
import std.algorithm; // For std.algorithm.swap

void fisherYatesShuffle(T)(T[] arr) {
    auto n = arr.length;
    auto rnd = Random(unpredictableSeed);

    for (int i = n - 1; i > 0; i--) {
        // Pick a random index from 0 to i
        int j = uniform(0, i + 1, rnd);
        
        // Swap arr[i] with the element at random index
        swap(arr[i], arr[j]);
    }
}

// void main() {
//     auto myArr = [1, 2, 3, 4, 5, 6, 7, 8];
//     writeln("Original: ", myArr);
//     fisherYatesShuffle(myArr);
//     writeln("Shuffled: ", myArr);
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

The `Fisher-Yates Shuffle` is an in-place algorithm that iterates backwards through an array, swapping each element with a randomly chosen one from the unshuffled portion.

---

**`fisher_yates_shuffle(arr)` Function:**
- `n`: The number of elements in the array `arr`.

**Algorithm Steps:**
- **Loop Backwards:** The algorithm starts a loop from the last element of the array (`i = n - 1`) and goes down to the second element (`i = 1`). The element at `i=0` does not need to be processed because when `i=1`, `arr[1]` will be swapped with either `arr[0]` or `arr[1]`, effectively randomizing the first element's position.
- **Pick Random Index `j`:** Inside the loop, a random index `j` is chosen from the range `[0, i]` (inclusive). This `j` points to a random element in the part of the array that has not yet been "fixed" or shuffled.
- **Swap:** The element at the current position `i` is swapped with the element at the randomly chosen position `j`. This places a randomly selected element from the unshuffled part of the array into the `i`-th position.
- After the swap, the element at `arr[i]` is considered "fixed" in its final shuffled position. The loop continues by decrementing `i`, reducing the range of unshuffled elements.

**Result:**
- After the loop completes, the entire array is shuffled in-place.

[Back to Implementation](#implementation)

## Applications

### Application

The `Fisher-Yates Shuffle` is the standard and most robust algorithm for shuffling a list or array, with many practical applications:
- **Gaming and Gambling:** Shuffling a deck of cards, randomizing a sequence of events (e.g., enemy spawns), or generating random game boards.
- **Statistics and Machine Learning:** Randomly shuffling a dataset before splitting it into training and testing sets to ensure unbiased sampling.
- **Cryptography:** Used in some cryptographic algorithms as part of the process for generating random permutations or keys.
- **Simulations:** In Monte Carlo simulations or other probabilistic models, for randomizing the order of events or samples.
- **Music Players:** Implementing a "shuffle" feature for a playlist to ensure a random and non-repeating (until all songs are played) order.

