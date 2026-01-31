---
title: "N-Queens Problem"
---

The `N-Queens Problem` is a classic problem in computer science and a perfect example for illustrating `backtracking algorithms`. The goal is to place `N` non-attacking `queens` on an `N x N` chessboard. A `queen` can attack any piece located on the same row, column, or diagonal.

The problem is to find all distinct configurations (or just one configuration) where no two `queens` threaten each other. For `N=1`, there is 1 solution. For `N=2` and `N=3`, there are no solutions. For `N=4`, there are 2 solutions.

## How it Works

### How it Works (Expanded)

The `N-Queens Problem` is typically solved using a `backtracking algorithm`. We try to place `queens` one by one, row by row. If placing a `queen` in a certain `position` leads to a conflict (i.e., it's attacked by another `queen`), we backtrack and try a different `position`.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
def solve_n_queens(n):
    """
    Solves the N-Queens problem using backtracking.
    Returns a list of all distinct solutions. Each solution is a list of strings
    representing the chessboard.
    """
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []

    # Helper function to check if a queen can be placed at board[row][col]
    def is_safe(current_board, r, c):
        # Check this row on left side
        # Not needed as we place queen row by row
        
        # Check upper diagonal on left side
        for i, j in zip(range(r, -1, -1), range(c, -1, -1)):
            if current_board[i][j] == 'Q':
                return False
        
        # Check lower diagonal on left side
        for i, j in zip(range(r, n, 1), range(c, -1, -1)):
            if current_board[i][j] == 'Q':
                return False
        
        # Check this column upwards
        for i in range(r):
            if current_board[i][c] == 'Q':
                return False

        return True

    # Main backtracking function
    def backtrack(r):
        if r == n: # All queens placed
            solutions.append(["".join(row) for row in board])
            return
        
        for c in range(n): # Try placing queen in each column of current row
            if is_safe(board, r, c):
                board[r][c] = 'Q' # Place queen
                backtrack(r + 1)  # Recur for next row
                board[r][c] = '.' # Backtrack: remove queen
    
    backtrack(0) # Start from first row
    return solutions

# Example
# n_val = 4
# solutions_4_queens = solve_n_queens(n_val)
# for sol in solutions_4_queens:
#     for row in sol:
#         print(row)
#     print()
# # Expected: 2 solutions
```

### Javascript

```javascript
function solveNQueens(n) {
    const solutions = [];
    // Initialize an empty board
    const board = Array(n).fill(0).map(() => Array(n).fill('.'));

    // Helper function to check if a queen can be placed at board[row][col]
    function isSafe(r, c) {
        // Check column upwards
        for (let i = 0; i < r; i++) {
            if (board[i][c] === 'Q') {
                return false;
            }
        }

        // Check upper-left diagonal
        for (let i = r - 1, j = c - 1; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] === 'Q') {
                return false;
            }
        }

        // Check upper-right diagonal
        for (let i = r - 1, j = c + 1; i >= 0 && j < n; i--, j++) {
            if (board[i][j] === 'Q') {
                return false;
            }
        }

        return true;
    }

    // Main backtracking function
    function backtrack(r) {
        if (r === n) { // All queens placed
            solutions.push(board.map(row => row.join('')));
            return;
        }
        
        for (let c = 0; c < n; c++) { // Try placing queen in each column of current row
            if (isSafe(r, c)) {
                board[r][c] = 'Q'; // Place queen
                backtrack(r + 1);  // Recur for next row
                board[r][c] = '.'; // Backtrack: remove queen
            }
        }
    }

    backtrack(0); // Start from first row
    return solutions;
}

// const nVal = 4;
// const solutions4Queens = solveNQueens(nVal);
// solutions4Queens.forEach(sol => {
//     sol.forEach(row => console.log(row));
//     console.log();
// });
```

### Typescript

```typescript
function solveNQueensTS(n: number): string[][] {
    const solutions: string[][] = [];
    // Initialize an empty board
    const board: string[][] = Array(n).fill(0).map(() => Array(n).fill('.'));

    // Helper function to check if a queen can be placed at board[row][col]
    function isSafe(r: number, c: number): boolean {
        // Check column upwards
        for (let i = 0; i < r; i++) {
            if (board[i][c] === 'Q') {
                return false;
            }
        }

        // Check upper-left diagonal
        for (let i = r - 1, j = c - 1; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] === 'Q') {
                return false;
            }
        }

        // Check upper-right diagonal
        for (let i = r - 1, j = c + 1; i >= 0 && j < n; i--, j++) {
            if (board[i][j] === 'Q') {
                return false;
            }
        }

        return true;
    }

    // Main backtracking function
    function backtrack(r: number): void {
        if (r === n) { // All queens placed
            solutions.push(board.map(row => row.join('')));
            return;
        }
        
        for (let c = 0; c < n; c++) { // Try placing queen in each column of current row
            if (isSafe(r, c)) {
                board[r][c] = 'Q'; // Place queen
                backtrack(r + 1);  // Recur for next row
                board[r][c] = '.'; // Backtrack: remove queen
            }
        }
    }

    backtrack(0); // Start from first row
    return solutions;
}

// const nValTS = 4;
// const solutions4QueensTS = solveNQueensTS(nValTS);
// solutions4QueensTS.forEach(sol => {
//     sol.forEach(row => console.log(row));
//     console.log();
// });
```

### Cpp

```cpp
#include <vector>
#include <string>
#include <iostream>
#include <numeric> // For std::iota

class NQueens {
private:
    std::vector<std::vector<std::string>> solutions;
    std::vector<std::string> board;
    int N;

    // Helper function to check if a queen can be placed at board[row][col]
    bool isSafe(int r, int c) {
        // Check column upwards
        for (int i = 0; i < r; i++) {
            if (board[i][c] == 'Q') {
                return false;
            }
        }

        // Check upper-left diagonal
        for (int i = r - 1, j = c - 1; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 'Q') {
                return false;
            }
        }

        // Check upper-right diagonal
        for (int i = r - 1, j = c + 1; i >= 0 && j < N; i++, j++) {
            if (board[i][j] == 'Q') {
                return false;
            }
        }

        return true;
    }

    // Main backtracking function
    void backtrack(int r) {
        if (r == N) { // All queens placed
            solutions.push_back(board);
            return;
        }
        
        for (int c = 0; c < N; c++) { // Try placing queen in each column of current row
            if (isSafe(r, c)) {
                board[r][c] = 'Q'; // Place queen
                backtrack(r + 1);  // Recur for next row
                board[r][c] = '.'; // Backtrack: remove queen
            }
        }
    }

public:
    std::vector<std::vector<std::string>> solveNQueens(int n) {
        N = n;
        board.assign(N, std::string(N, '.')); // Initialize empty board
        solutions.clear();
        backtrack(0); // Start from first row
        return solutions;
    }
};

// int main() {
//     NQueens solver;
//     int n_val = 4;
//     std::vector<std::vector<std::string>> solutions_4_queens = solver.solveNQueens(n_val);
//     for (const auto& sol : solutions_4_queens) {
//         for (const auto& row : sol) {
//             std::cout << row << std::endl;
//         }
//         std::cout << std::endl;
//     }
//     return 0;
// }
```

### Go

```go
package main

import "fmt"
import "strings"

func solveNQueens(n int) [][]string {
    solutions := [][]string{}
    board := make([][]rune, n)
    for i := range board {
        board[i] = make([]rune, n)
        for j := range board[i] {
            board[i][j] = '.'
        }
    }

    // Helper function to check if a queen can be placed at board[row][col]
    // Checks only rows above the current row
    func isSafe(r, c int) bool {
        // Check column upwards
        for i := 0; i < r; i++ {
            if board[i][c] == 'Q' {
                return false
            }
        }

        // Check upper-left diagonal
        for i, j := r-1, c-1; i >= 0 && j >= 0; i, j = i-1, j-1 {
            if board[i][j] == 'Q' {
                return false
            }
        }

        // Check upper-right diagonal
        for i, j := r-1, c+1; i >= 0 && j < n; i, j = i-1, j+1 {
            if board[i][j] == 'Q' {
                return false
            }
        }

        return true
    }

    // Main backtracking function
    var backtrack func(r int)
    backtrack = func(r int) {
        if r == n { // All queens placed
            solution := make([]string, n)
            for i, row := range board {
                solution[i] = string(row)
            }
            solutions = append(solutions, solution)
            return
        }
        
        for c := 0; c < n; c++ { // Try placing queen in each column of current row
            if isSafe(r, c) {
                board[r][c] = 'Q' // Place queen
                backtrack(r + 1)  // Recur for next row
                board[r][c] = '.' // Backtrack: remove queen
            }
        }
    }

    backtrack(0) // Start from first row
    return solutions
}

// func main() {
//     nVal := 4
//     solutions4Queens := solveNQueens(nVal)
//     for _, sol := range solutions4Queens {
//         for _, row := range sol {
//             fmt.Println(row)
//         }
//         fmt.Println()
//     }
// }
```

### D

```d
import std.stdio;
import std.array;
import std.string;
import std.algorithm; // For std.algorithm.max, min

class NQueens {
private:
    string[][] solutions;
    char[][] board;
    int N;

    // Helper function to check if a queen can be placed at board[row][col]
    bool isSafe(int r, int c) {
        // Check column upwards
        foreach (i; 0 .. r) {
            if (board[i][c] == 'Q') {
                return false;
            }
        }

        // Check upper-left diagonal
        for (int i = r - 1, j = c - 1; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 'Q') {
                return false;
            }
        }

        // Check upper-right diagonal
        for (int i = r - 1, j = c + 1; i >= 0 && j < N; i++, j++) {
            if (board[i][j] == 'Q') {
                return false;
            }
        }

        return true;
    }

    // Main backtracking function
    void backtrack(int r) {
        if (r == N) { // All queens placed
            solutions ~= board.map!(row => new string(row)).array;
            return;
        }
        
        foreach (c; 0 .. N) { // Try placing queen in each column of current row
            if (isSafe(r, c)) {
                board[r][c] = 'Q'; // Place queen
                backtrack(r + 1);  // Recur for next row
                board[r][c] = '.'; // Backtrack: remove queen
            }
        }
    }

public:
    string[][] solveNQueens(int n) {
        N = n;
        board = new char[N][N];
        foreach (ref row; board) {
            row[] = '.'; // Initialize empty board
        }
        solutions.clear();
        backtrack(0); // Start from first row
        return solutions;
    }
}

// void main() {
//     auto solver = new NQueens();
//     int nVal = 4;
//     auto solutions4Queens = solver.solveNQueens(nVal);
//     foreach (sol; solutions4Queens) {
//         foreach (row; sol) {
//             writeln(row);
//         }
//         writeln();
//     }
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

The `N-Queens Problem` is a classic example of how `backtracking` systematically explores potential solutions, pruning branches that violate constraints.

[Back to Implementation](#implementation)

## Applications

### Application

The `N-Queens Problem` is a classical puzzle and a fundamental example of problems solved using the `backtracking paradigm`. While the problem itself is specific, its solution approach is broadly applicable:
- **Constraint Satisfaction Problems (CSPs):** Many real-world problems can be modeled as CSPs (e.g., scheduling, resource allocation), and backtracking is a common technique for solving them.
- **Game AI:** Used in developing AI for games like Chess, where finding optimal moves or checking for specific board states involves exploring a tree of possibilities.
- **Automated Theorem Proving:** In logic and mathematics, finding proofs often involves exploring a search space of logical deductions.
- **Combinatorial Optimization:** Finding all valid arrangements or subsets that satisfy certain conditions.
- **Sudoku Solvers:** A variant of backtracking can be used to solve Sudoku puzzles.
- **Route Finding in Restricted Environments:** For example, finding paths in a maze or a robot navigating an environment with specific placement constraints.

