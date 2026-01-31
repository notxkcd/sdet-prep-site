---
title: "Matrix Chain Multiplication"
---

The `Matrix Chain Multiplication` problem is a classic optimization problem that can be efficiently solved using `dynamic programming`. Given a sequence of matrices, the goal is to find the most efficient way to multiply these matrices. The problem is not about performing the actual multiplications, but merely determining the order of parenthesization that minimizes the total number of scalar multiplications.

Matrix multiplication is associative, meaning that the order in which matrices are multiplied does not affect the final product. However, the number of scalar multiplications required can vary dramatically depending on the order of parenthesization.

## How it Works

### How it Works (Expanded)

To multiply a `p x q` matrix `A` by a `q x r` matrix `B`, the resulting matrix `C` will be `p x r`, and it will require `p * q * r` scalar multiplications. The key insight is that for a chain of matrices `A1 * A2 * ... * An`, a final multiplication splits the chain into two sub-chains: `(A1 * ... * Ak) * (Ak+1 * ... * An)`. The optimal solution for the whole chain contains optimal solutions for its sub-chains.

---

Example: Chain of matrices A1, A2, A3, A4
Dimensions: A1(10x100), A2(100x5), A3(5x50), A4(50x1)

Possible parenthesizations:
- ((A1A2)A3)A4:
- (A1A2) costs 10*100*5 = 5000 (result 10x5)
- ((A1A2)A3) costs 5000 + 10*5*50 = 7500 (result 10x50)
- (((A1A2)A3)A4) costs 7500 + 10*50*1 = 8000
- (A1(A2A3))A4:
- (A2A3) costs 100*5*50 = 25000 (result 100x50)
- (A1(A2A3)) costs 25000 + 10*100*50 = 75000 (result 10x50)
- ((A1(A2A3))A4) costs 75000 + 10*50*1 = 75500
- ... and so on.

The goal is to find the minimum.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
import sys

def matrix_chain_order(dims):
    n = len(dims) - 1 # Number of matrices
    
    # m[i][j] stores the minimum number of scalar multiplications
    # needed to compute the matrix A[i]...A[j]
    m = [[0 for _ in range(n)] for _ in range(n)]
    
    # s[i][j] stores the index k where the optimal split occurs
    s = [[0 for _ in range(n)] for _ in range(n)]

    # chain length L from 2 to n
    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            m[i][j] = sys.maxsize # Initialize with a very large value

            # Try all possible split points k
            for k in range(i, j):
                # cost = cost of (A[i]...A[k]) + cost of (A[k+1]...A[j]) + cost of multiplying results
                cost = m[i][k] + m[k + 1][j] + dims[i] <em> dims[k + 1] </em> dims[j + 1]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k # Store the split point

    return m[0][n-1], s # Return min multiplications and split points

def print_optimal_parenthesization(s, i, j, names):
    if i == j:
        return names[i]
    else:
        return "(" + print_optimal_parenthesization(s, i, s[i][j], names) + \
               print_optimal_parenthesization(s, s[i][j] + 1, j, names) + ")"

# Example
# A1: 10x100, A2: 100x5, A3: 5x50, A4: 50x1
# Dimensions array: p = [p0, p1, p2, p3, p4] => A1(p0xp1), A2(p1xp2), ...
# So, dims = [10, 100, 5, 50, 1]
# min_mults, splits = matrix_chain_order(dims)
# print("Minimum scalar multiplications:", min_mults) # Expected: 1550
# # To reconstruct parenthesization:
# matrix_names = ["A1", "A2", "A3", "A4"]
# print("Optimal Parenthesization:", print_optimal_parenthesization(splits, 0, len(dims) - 2, matrix_names)) # Expected: ((A1(A2A3))A4)
```

### Javascript

```javascript
function matrixChainOrder(dims) {
    const n = dims.length - 1; // Number of matrices
    
    // m[i][j] stores the minimum number of scalar multiplications
    // needed to compute the matrix A[i]...A[j]
    const m = Array(n).fill(0).map(() => Array(n).fill(0));
    
    // s[i][j] stores the index k where the optimal split occurs
    const s = Array(n).fill(0).map(() => Array(n).fill(0));

    // chain length L from 2 to n
    for (let L = 2; L <= n; L++) {
        for (let i = 0; i <= n - L; i++) {
            const j = i + L - 1;
            m[i][j] = Infinity; // Initialize with a very large value

            // Try all possible split points k
            for (let k = i; k < j; k++) {
                // cost = cost of (A[i]...A[k]) + cost of (A[k+1]...A[j]) + cost of multiplying results
                const cost = m[i][k] + m[k + 1][j] + dims[i] <em> dims[k + 1] </em> dims[j + 1];
                if (cost < m[i][j]) {
                    m[i][j] = cost;
                    s[i][j] = k; // Store the split point
                }
            }
        }
    }

    return { minMults: m[0][n-1], splits: s };
}

function printOptimalParenthesization(s, i, j, names) {
    if (i === j) {
        return names[i];
    } else {
        return "(" + printOptimalParenthesization(s, i, s[i][j], names) +
               printOptimalParenthesization(s, s[i][j] + 1, j, names) + ")";
    }
}

// const dims = [10, 100, 5, 50, 1]; // A1(10x100), A2(100x5), A3(5x50), A4(50x1)
// const { minMults, splits } = matrixChainOrder(dims);
// console.log("Minimum scalar multiplications:", minMults); // Expected: 1550
// const matrixNames = ["A1", "A2", "A3", "A4"];
// console.log("Optimal Parenthesization:", printOptimalParenthesization(splits, 0, dims.length - 2, matrixNames)); // Expected: ((A1(A2A3))A4)
```

### Typescript

```typescript
function matrixChainOrderTS(dims: number[]): { minMults: number; splits: number[][] } {
    const n = dims.length - 1; // Number of matrices
    
    // m[i][j] stores the minimum number of scalar multiplications
    // needed to compute the matrix A[i]...A[j]
    const m: number[][] = Array(n).fill(0).map(() => Array(n).fill(0));
    
    // s[i][j] stores the index k where the optimal split occurs
    const s: number[][] = Array(n).fill(0).map(() => Array(n).fill(0));

    // chain length L from 2 to n
    for (let L = 2; L <= n; L++) {
        for (let i = 0; i <= n - L; i++) {
            const j = i + L - 1;
            m[i][j] = Infinity; // Initialize with a very large value

            // Try all possible split points k
            for (let k = i; k < j; k++) {
                // cost = cost of (A[i]...A[k]) + cost of (A[k+1]...A[j]) + cost of multiplying results
                const cost = m[i][k] + m[k + 1][j] + dims[i] <em> dims[k + 1] </em> dims[j + 1];
                if (cost < m[i][j]) {
                    m[i][j] = cost;
                    s[i][j] = k; // Store the split point
                }
            }
        }
    }

    return { minMults: m[0][n-1], splits: s };
}

function printOptimalParenthesizationTS(s: number[][], i: number, j: number, names: string[]): string {
    if (i === j) {
        return names[i];
    } else {
        return "(" + printOptimalParenthesizationTS(s, i, s[i][j], names) +
               printOptimalParenthesizationTS(s, s[i][j] + 1, j, names) + ")";
    }
}

// const dimsTS = [10, 100, 5, 50, 1]; // A1(10x100), A2(100x5), A3(5x50), A4(50x1)
// const { minMults: minMultsTS, splits: splitsTS } = matrixChainOrderTS(dimsTS);
// console.log("Minimum scalar multiplications:", minMultsTS); // Expected: 1550
// const matrixNamesTS = ["A1", "A2", "A3", "A4"];
// console.log("Optimal Parenthesization:", printOptimalParenthesizationTS(splitsTS, 0, dimsTS.length - 2, matrixNamesTS)); // Expected: ((A1(A2A3))A4)
```

### Cpp

```cpp
#include <vector>
#include <iostream>
#include <algorithm> // For std::min
#include <limits>    // For std::numeric_limits

std::pair<int, std::vector<std::vector<int>>> matrixChainOrder(const std::vector<int>& dims) {
    int n = dims.size() - 1; // Number of matrices
    
    // m[i][j] stores the minimum number of scalar multiplications
    // needed to compute the matrix A[i]...A[j]
    std::vector<std::vector<int>> m(n, std::vector<int>(n, 0));
    
    // s[i][j] stores the index k where the optimal split occurs
    std::vector<std::vector<int>> s(n, std::vector<int>(n, 0));

    // chain length L from 2 to n
    for (int L = 2; L <= n; L++) {
        for (int i = 0; i <= n - L; i++) {
            int j = i + L - 1;
            m[i][j] = std::numeric_limits<int>::max(); // Initialize with a very large value

            // Try all possible split points k
            for (int k = i; k < j; k++) {
                // cost = cost of (A[i]...A[k]) + cost of (A[k+1]...A[j]) + cost of multiplying results
                int cost = m[i][k] + m[k + 1][j] + dims[i] <em> dims[k + 1] </em> dims[j + 1];
                if (cost < m[i][j]) {
                    m[i][j] = cost;
                    s[i][j] = k; // Store the split point
                }
            }
        }
    }

    return {m[0][n-1], s};
}

void printOptimalParenthesization(const std::vector<std::vector<int>>& s, int i, int j, const std::vector<std::string>& names) {
    if (i == j) {
        std::cout << names[i];
    } else {
        std::cout << "(";
        printOptimalParenthesization(s, i, s[i][j], names);
        printOptimalParenthesization(s, s[i][j] + 1, j, names);
        std::cout << ")";
    }
}

// int main() {
//     // A1: 10x100, A2: 100x5, A3: 5x50, A4: 50x1
//     // Dimensions array: p = [p0, p1, p2, p3, p4] => A1(p0xp1), A2(p1xp2), ...
//     std::vector<int> dims = {10, 100, 5, 50, 1};
//     std::vector<std::string> matrix_names = {"A1", "A2", "A3", "A4"};

//     auto result = matrixChainOrder(dims);
//     int min_mults = result.first;
//     std::vector<std::vector<int>> splits = result.second;

//     std::cout << "Minimum scalar multiplications: " << min_mults << std::endl; // 1550
//     std::cout << "Optimal Parenthesization: ";
//     printOptimalParenthesization(splits, 0, dims.size() - 2, matrix_names); // ((A1(A2A3))A4)
//     std::cout << std::endl;
//     return 0;
// }
```

### Go

```go
package main

import (
    "fmt"
    "math"
    "strings"
)

func matrixChainOrder(dims []int) (int, [][]int) {
    n := len(dims) - 1 // Number of matrices
    
    // m[i][j] stores the minimum number of scalar multiplications
    // needed to compute the matrix A[i]...A[j]
    m := make([][]int, n)
    for i := range m {
        m[i] = make([]int, n)
    }
    
    // s[i][j] stores the index k where the optimal split occurs
    s := make([][]int, n)
    for i := range s {
        s[i] = make([]int, n)
    }

    // chain length L from 2 to n
    for L := 2; L <= n; L++ {
        for i := 0; i <= n - L; i++ {
            j := i + L - 1
            m[i][j] = math.MaxInt32 // Initialize with a very large value

            // Try all possible split points k
            for k := i; k < j; k++ {
                // cost = cost of (A[i]...A[k]) + cost of (A[k+1]...A[j]) + cost of multiplying results
                cost := m[i][k] + m[k+1][j] + dims[i]<em>dims[k+1]</em>dims[j+1]
                if cost < m[i][j] {
                    m[i][j] = cost
                    s[i][j] = k // Store the split point
                }
            }
        }
    }

    return m[0][n-1], s
}

func printOptimalParenthesization(s [][]int, i, j int, names []string) string {
    if i == j {
        return names[i]
    } else {
        var builder strings.Builder
        builder.WriteString("(")
        builder.WriteString(printOptimalParenthesization(s, i, s[i][j], names))
        builder.WriteString(printOptimalParenthesization(s, s[i][j]+1, j, names))
        builder.WriteString(")")
        return builder.String()
    }
}

// func main() {
//     // A1: 10x100, A2: 100x5, A3: 5x50, A4: 50x1
//     // Dimensions array: p = [p0, p1, p2, p3, p4] => A1(p0xp1), A2(p1xp2), ...
//     dims := []int{10, 100, 5, 50, 1}
//     matrixNames := []string{"A1", "A2", "A3", "A4"}

//     minMults, splits := matrixChainOrder(dims)
//     fmt.Println("Minimum scalar multiplications:", minMults) // 1550
//     fmt.Print("Optimal Parenthesization: ")
//     fmt.Println(printOptimalParenthesization(splits, 0, len(dims)-2, matrixNames)) // ((A1(A2A3))A4)
// }
```

### D

```d
import std.stdio;
import std.array;
import std.algorithm; // For std.algorithm.min
import std.string;
import std.conv;

Tuple!(int, "minMults", int[][], "splits") matrixChainOrder(int[] dims) {
    auto n = dims.length - 1; // Number of matrices
    
    // m[i][j] stores the minimum number of scalar multiplications
    // needed to compute the matrix A[i]...A[j]
    auto m = new int[n][n];
    
    // s[i][j] stores the index k where the optimal split occurs
    auto s = new int[n][n];

    // Initialize m[i][i] to 0 for single matrices
    foreach (i; 0 .. n) {
        m[i][i] = 0;
    }

    // chain length L from 2 to n
    foreach (L; 2 .. n + 1) {
        foreach (i; 0 .. n - L + 1) {
            auto j = i + L - 1;
            m[i][j] = int.max; // Initialize with a very large value

            // Try all possible split points k
            foreach (k; i .. j) {
                // cost = cost of (A[i]...A[k]) + cost of (A[k+1]...A[j]) + cost of multiplying results
                auto cost = m[i][k] + m[k + 1][j] + dims[i] <em> dims[k + 1] </em> dims[j + 1];
                if (cost < m[i][j]) {
                    m[i][j] = cost;
                    s[i][j] = k; // Store the split point
                }
            }
        }
    }

    return typeof(return)(m[0][n-1], s);
}

string printOptimalParenthesization(int[][] s, int i, int j, string[] names) {
    if (i == j) {
        return names[i];
    } else {
        return "(" ~ printOptimalParenthesization(s, i, s[i][j], names) ~
               printOptimalParenthesization(s, s[i][j] + 1, j, names) ~ ")";
    }
}

// void main() {
//     // A1: 10x100, A2: 100x5, A3: 5x50, A4: 50x1
//     // Dimensions array: p = [p0, p1, p2, p3, p4] => A1(p0xp1), A2(p1xp2), ...
//     auto dims = [10, 100, 5, 50, 1];
//     string[] matrixNames = ["A1", "A2", "A3", "A4"];

//     auto result = matrixChainOrder(dims);
//     int minMults = result.minMults;
//     int[][] splits = result.splits;

//     writeln("Minimum scalar multiplications: ", minMults); // 1550
//     write("Optimal Parenthesization: ");
//     writeln(printOptimalParenthesization(splits, 0, dims.length - 2, matrixNames)); // ((A1(A2A3))A4)
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

The `Matrix Chain Multiplication` algorithm uses `dynamic programming` to compute the minimum scalar multiplications by breaking the problem into overlapping subproblems.

---

**Input (`dims` array):**
- The dimensions of `n` matrices `A1, ..., An` are represented by an `array p` of size `n+1`.
- `Matrix Ai` has dimensions `p[i-1] x p[i]`.
- For example, if `dims = [10, 100, 5, 50, 1]`, then `A1` is 10x100, `A2` is 100x5, `A3` is 5x50, `A4` is 50x1.

**Initialization:**
- `m[i][j]`: A 2D array (DP table) where `m[i][j]` stores the minimum scalar multiplications needed to multiply the chain of matrices from `A_i` to `A_j`.
- `s[i][j]`: An additional 2D array to store the optimal split point `k` for the chain `A_i...A_j`. This is used to reconstruct the optimal parenthesization.
- All `m[i][i]` are initialized to 0, as multiplying a single matrix requires no scalar multiplications.

**Filling the DP Table (`m` array):**
- The algorithm iterates through `L`, the chain `length`, from 2 to `n`.
- For each `length L`, it iterates through `i`, the starting `index` of the chain (from 0 to `n - L`).
- `j` is calculated as `i + L - 1`, the ending `index` of the current chain.
- For each `chain A_i...A_j`, `m[i][j]` is initially set to infinity.
- The inner loop iterates through `k`, all possible split points for the chain `A_i...A_j` (`i <= k < j`).
- The cost for a split at `k` is calculated as `m[i][k] + m[k+1][j] + dims[i]*dims[k+1]*dims[j+1]`.
- `m[i][k]` is the cost to multiply `A_i...A_k`.
- `m[k+1][j]` is the cost to multiply `A_k+1...A_j`.
- `dims[i]*dims[k+1]*dims[j+1]` is the cost to multiply the two resulting matrices (dimensions `dims[i] x dims[k+1]` and `dims[k+1] x dims[j+1]`).

    </li>
- If this `cost` is less than the current `m[i][j]`, `m[i][j]` is updated, and the split point `k` is stored in `s[i][j]`.

**Result:**
- The minimum scalar multiplications for the entire chain `A_0...A_n-1` is `m[0][n-1]`.
- The `print_optimal_parenthesization` function uses the `s` table to recursively reconstruct the optimal parenthesization.

[Back to Implementation](#implementation)

## Applications

### Application

The `Matrix Chain Multiplication` algorithm is a foundational problem in `dynamic programming` with applications in various fields:
- **Compiler Optimization:** Optimizing the order of matrix multiplications in mathematical expressions within programming languages. Compilers can use this to generate more efficient code.
- **Computer Graphics:** In 3D graphics, transformations (translation, rotation, scaling) are often represented as matrices. Optimizing the order of these matrix multiplications can significantly improve rendering performance.
- **Scientific Computing:** Any field involving extensive matrix algebra, such as physics, engineering, and data science, can benefit from optimizing matrix multiplication sequences for performance.
- **Bioinformatics:** Some algorithms, particularly in sequence alignment, might involve operations that can be modeled as matrix chain multiplications, where the goal is to reduce computational cost.

