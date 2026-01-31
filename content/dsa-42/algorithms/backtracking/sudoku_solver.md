---
title: "Sudoku Solver"
---

The `Sudoku Solver` is a classic problem that can be efficiently solved using a `backtracking algorithm`. The goal is to fill a 9x9 grid with `digits` from 1 to 9 such that each `column`, each `row`, and each of the nine 3x3 `subgrids` (also called "boxes" or "blocks") contains all of the `digits` from 1 to 9.

Given a partially filled `Sudoku grid`, the solver finds a valid solution by systematically trying to place numbers and backtracking when a conflict arises.

## How it Works

### How it Works (Expanded)

A `Sudoku Solver` uses a `backtracking algorithm` that tries to place a number in an empty cell. If the number is valid according to Sudoku rules, it proceeds to the next empty cell. If it reaches a point where no valid number can be placed, it backtracks to the previous decision and tries a different number.

---

Example: Solve a 9x9 Sudoku (simplified fragment)

Given Board:
5 3 . | . 7 . | . . .
6 . . | 1 9 5 | . . .
. 9 8 | . . . | . 6 .
---------------------
8 . . | . 6 . | . . 3
4 . . | 8 . 3 | . . 1
7 . . | . 2 . | . . 6
---------------------
. 6 . | . . . | 2 8 .
. . . | 4 1 9 | . . 5
. . . | . 8 . | . 7 9

1. Find the first empty cell (0,2).
2. Try numbers 1-9 for (0,2):
- Is 1 safe? Yes. Place 1. Recurse for next empty cell.
- If that fails, remove 1. Try 2. Is 2 safe? ...
3. If no number is safe for (0,2), backtrack to previous cell.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
def is_valid_placement(board, num, row, col):
    # Check row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check 3x3 box
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

def find_empty_location(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0: # 0 represents empty cell
                return r, c
    return -1, -1 # No empty cell found

def solve_sudoku(board):
    row, col = find_empty_location(board)

    # Base case: If no empty location, puzzle solved
    if row == -1:
        return True
    
    # Try numbers 1 to 9
    for num in range(1, 10):
        if is_valid_placement(board, num, row, col):
            board[row][col] = num # Place number
            if solve_sudoku(board): # Recur for next empty cell
                return True
            board[row][col] = 0 # Backtrack: remove number
            
    return False # No number found for this cell

# Example Sudoku (0 for empty cells)
# board = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# ]
# if solve_sudoku(board):
#     for r in board:
#         print(r)
# else:
#     print("No solution exists")
```

### Javascript

```javascript
function isValidPlacement(board, num, row, col) {
    // Check row
    for (let x = 0; x < 9; x++) {
        if (board[row][x] === num) {
            return false;
        }
    }

    // Check column
    for (let x = 0; x < 9; x++) {
        if (board[x][col] === num) {
            return false;
        }
    }

    // Check 3x3 box
    const startRow = row - (row % 3);
    const startCol = col - (col % 3);
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            if (board[i + startRow][j + startCol] === num) {
                return false;
            }
        }
    }
    return true;
}

function findEmptyLocation(board) {
    for (let r = 0; r < 9; r++) {
        for (let c = 0; c < 9; c++) {
            if (board[r][c] === 0) { // 0 represents empty cell
                return { row: r, col: c };
            }
        }
    }
    return null; // No empty cell found
}

function solveSudoku(board) {
    const emptyLoc = findEmptyLocation(board);

    // Base case: If no empty location, puzzle solved
    if (emptyLoc === null) {
        return true;
    }
    
    const { row, col } = emptyLoc;

    // Try numbers 1 to 9
    for (let num = 1; num <= 9; num++) {
        if (isValidPlacement(board, num, row, col)) {
            board[row][col] = num; // Place number
            if (solveSudoku(board)) { // Recur for next empty cell
                return true;
            }
            board[row][col] = 0; // Backtrack: remove number
        }
    }
            
    return false; // No number found for this cell
}

// const board = [
//     [5, 3, 0, 0, 7, 0, 0, 0, 0],
//     [6, 0, 0, 1, 9, 5, 0, 0, 0],
//     [0, 9, 8, 0, 0, 0, 0, 6, 0],
//     [8, 0, 0, 0, 6, 0, 0, 0, 3],
//     [4, 0, 0, 8, 0, 3, 0, 0, 1],
//     [7, 0, 0, 0, 2, 0, 0, 0, 6],
//     [0, 6, 0, 0, 0, 0, 2, 8, 0],
//     [0, 0, 0, 4, 1, 9, 0, 0, 5],
//     [0, 0, 0, 0, 8, 0, 0, 7, 9]
// ];
// if (solveSudoku(board)) {
//     board.forEach(row => console.log(row));
// } else {
//     console.log("No solution exists");
// }
```

### Typescript

```typescript
function isValidPlacementTS(board: number[][], num: number, row: number, col: number): boolean {
    // Check row
    for (let x = 0; x < 9; x++) {
        if (board[row][x] === num) {
            return false;
        }
    }

    // Check column
    for (let x = 0; x < 9; x++) {
        if (board[x][col] === num) {
            return false;
        }
    }

    // Check 3x3 box
    const startRow = row - (row % 3);
    const startCol = col - (col % 3);
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            if (board[i + startRow][j + startCol] === num) {
                return false;
            }
        }
    }
    return true;
}

interface EmptyLocation {
    row: number;
    col: number;
}

function findEmptyLocationTS(board: number[][]): EmptyLocation | null {
    for (let r = 0; r < 9; r++) {
        for (let c = 0; c < 9; c++) {
            if (board[r][c] === 0) { // 0 represents empty cell
                return { row: r, col: c };
            }
        }
    }
    return null; // No empty cell found
}

function solveSudokuTS(board: number[][]): boolean {
    const emptyLoc = findEmptyLocationTS(board);

    // Base case: If no empty location, puzzle solved
    if (emptyLoc === null) {
        return true;
    }
    
    const { row, col } = emptyLoc;

    // Try numbers 1 to 9
    for (let num = 1; num <= 9; num++) {
        if (isValidPlacementTS(board, num, row, col)) {
            board[row][col] = num; // Place number
            if (solveSudokuTS(board)) { // Recur for next empty cell
                return true;
            }
            board[row][col] = 0; // Backtrack: remove number
        }
    }
            
    return false; // No number found for this cell
}

// const boardTS = [
//     [5, 3, 0, 0, 7, 0, 0, 0, 0],
//     [6, 0, 0, 1, 9, 5, 0, 0, 0],
//     [0, 9, 8, 0, 0, 0, 0, 6, 0],
//     [8, 0, 0, 0, 6, 0, 0, 0, 3],
//     [4, 0, 0, 8, 0, 3, 0, 0, 1],
//     [7, 0, 0, 0, 2, 0, 0, 0, 6],
//     [0, 6, 0, 0, 0, 0, 2, 8, 0],
//     [0, 0, 0, 4, 1, 9, 0, 0, 5],
//     [0, 0, 0, 0, 8, 0, 0, 7, 9]
// ];
// if (solveSudokuTS(boardTS)) {
//     boardTS.forEach(row => console.log(row));
// } else {
//     console.log("No solution exists");
// }
```

### Cpp

```cpp
#include <vector>
#include <iostream>
#include <numeric> // For std::iota

bool isValidPlacement(const std::vector<std::vector<int>>& board, int num, int row, int col) {
    // Check row
    for (int x = 0; x < 9; x++) {
        if (board[row][x] == num) {
            return false;
        }
    }

    // Check column
    for (int x = 0; x < 9; x++) {
        if (board[x][col] == num) {
            return false;
        }
    }

    // Check 3x3 box
    int start_row = row - row % 3;
    int start_col = col - col % 3;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (board[i + start_row][j + start_col] == num) {
                return false;
            }
        }
    }
    return true;
}

std::pair<int, int> findEmptyLocation(const std::vector<std::vector<int>>& board) {
    for (int r = 0; r < 9; r++) {
        for (int c = 0; c < 9; c++) {
            if (board[r][c] == 0) { // 0 represents empty cell
                return {r, c};
            }
        }
    }
    return {-1, -1}; // No empty cell found
}

bool solveSudoku(std::vector<std::vector<int>>& board) {
    std::pair<int, int> empty_loc = findEmptyLocation(board);
    int row = empty_loc.first;
    int col = empty_loc.second;

    // Base case: If no empty location, puzzle solved
    if (row == -1) {
        return true;
    }
    
    // Try numbers 1 to 9
    for (int num = 1; num <= 9; num++) {
        if (isValidPlacement(board, num, row, col)) {
            board[row][col] = num; // Place number
            if (solveSudoku(board)) { // Recur for next empty cell
                return true;
            }
            board[row][col] = 0; // Backtrack: remove number
        }
    }
            
    return false; // No number found for this cell
}

// int main() {
//     std::vector<std::vector<int>> board = {
//         {5, 3, 0, 0, 7, 0, 0, 0, 0},
//         {6, 0, 0, 1, 9, 5, 0, 0, 0},
//         {0, 9, 8, 0, 0, 0, 0, 6, 0},
//         {8, 0, 0, 0, 6, 0, 0, 0, 3},
//         {4, 0, 0, 8, 0, 3, 0, 0, 1},
//         {7, 0, 0, 0, 2, 0, 0, 0, 6},
//         {0, 6, 0, 0, 0, 0, 2, 8, 0},
//         {0, 0, 0, 4, 1, 9, 0, 0, 5},
//         {0, 0, 0, 0, 8, 0, 0, 7, 9}
//     };
//     if (solveSudoku(board)) {
//         for (const auto& row : board) {
//             for (int val : row) {
//                 std::cout << val << " ";
//             }
//             std::cout << std::endl;
//         }
//     } else {
//         std::cout << "No solution exists" << std::endl;
//     }
//     return 0;
// }
```

### Go

```go
package main

import "fmt"

func isValidPlacement(board [][]int, num, row, col int) bool {
    // Check row
    for x := 0; x < 9; x++ {
        if board[row][x] == num {
            return false
        }
    }

    // Check column
    for x := 0; x < 9; x++ {
        if board[x][col] == num {
            return false
        }
    }

    // Check 3x3 box
    startRow := row - row%3
    startCol := col - col%3
    for i := 0; i < 3; i++ {
        for j := 0; j < 3; j++ {
            if board[i+startRow][j+startCol] == num {
                return false
            }
        }
    }
    return true
}

func findEmptyLocation(board [][]int) (int, int) {
    for r := 0; r < 9; r++ {
        for c := 0; c < 9; c++ {
            if board[r][c] == 0 { // 0 represents empty cell
                return r, c
            }
        }
    }
    return -1, -1 // No empty cell found
}

func solveSudoku(board [][]int) bool {
    row, col := findEmptyLocation(board)

    // Base case: If no empty location, puzzle solved
    if row == -1 {
        return true
    }
    
    // Try numbers 1 to 9
    for num := 1; num <= 9; num++ {
        if isValidPlacement(board, num, row, col) {
            board[row][col] = num // Place number
            if solveSudoku(board) { // Recur for next empty cell
                return true
            }
            board[row][col] = 0 // Backtrack: remove number
        }
    }
            
    return false // No number found for this cell
}

// func main() {
//     board := [][]int{
//         {5, 3, 0, 0, 7, 0, 0, 0, 0},
//         {6, 0, 0, 1, 9, 5, 0, 0, 0},
//         {0, 9, 8, 0, 0, 0, 0, 6, 0},
//         {8, 0, 0, 0, 6, 0, 0, 0, 3},
//         {4, 0, 0, 8, 0, 3, 0, 0, 1},
//         {7, 0, 0, 0, 2, 0, 0, 0, 6},
//         {0, 6, 0, 0, 0, 0, 2, 8, 0},
//         {0, 0, 0, 4, 1, 9, 0, 0, 5},
//         {0, 0, 0, 0, 8, 0, 0, 7, 9},
//     }
//     if solveSudoku(board) {
//         for r := 0; r < 9; r++ {
//             for c := 0; c < 9; c++ {
//                 fmt.Printf("%d ", board[r][c])
//             }
//             fmt.Println()
//         }
//     } else {
//         fmt.Println("No solution exists")
//     }
// }
```

### D

```d
import std.stdio;
import std.array;
import std.algorithm;

bool isValidPlacement(int[][] board, int num, int row, int col) {
    // Check row
    foreach (x; 0 .. 9) {
        if (board[row][x] == num) {
            return false;
        }
    }

    // Check column
    foreach (x; 0 .. 9) {
        if (board[x][col] == num) {
            return false;
        }
    }

    // Check 3x3 box
    int startRow = row - row % 3;
    int startCol = col - col % 3;
    foreach (i; 0 .. 3) {
        foreach (j; 0 .. 3) {
            if (board[i + startRow][j + startCol] == num) {
                return false;
            }
        }
    }
    return true;
}

Tuple!(int, "row", int, "col") findEmptyLocation(int[][] board) {
    foreach (r; 0 .. 9) {
        foreach (c; 0 .. 9) {
            if (board[r][c] == 0) { // 0 represents empty cell
                return typeof(return)(r, c);
            }
        }
    }
    return typeof(return)(-1, -1); // No empty cell found
}

bool solveSudoku(int[][] board) {
    auto emptyLoc = findEmptyLocation(board);
    int row = emptyLoc.row;
    int col = emptyLoc.col;

    // Base case: If no empty location, puzzle solved
    if (row == -1) {
        return true;
    }
    
    // Try numbers 1 to 9
    foreach (num; 1 .. 10) {
        if (isValidPlacement(board, num, row, col)) {
            board[row][col] = num; // Place number
            if (solveSudoku(board)) { // Recur for next empty cell
                return true;
            }
            board[row][col] = 0; // Backtrack: remove number
        }
    }
            
    return false; // No number found for this cell
}

// void main() {
//     int[][] board = [
//         [5, 3, 0, 0, 7, 0, 0, 0, 0],
//         [6, 0, 0, 1, 9, 5, 0, 0, 0],
//         [0, 9, 8, 0, 0, 0, 0, 6, 0],
//         [8, 0, 0, 0, 6, 0, 0, 0, 3],
//         [4, 0, 0, 8, 0, 3, 0, 0, 1],
//         [7, 0, 0, 0, 2, 0, 0, 0, 6],
//         [0, 6, 0, 0, 0, 0, 2, 8, 0],
//         [0, 0, 0, 4, 1, 9, 0, 0, 5],
//         [0, 0, 0, 0, 8, 0, 0, 7, 9]
//     ];
//     if (solveSudoku(board)) {
//         foreach (row; board) {
//             foreach (val; row) {
//                 writef("%d ", val);
//             }
//             writeln();
//         }
//     } else {
//         writeln("No solution exists");
//     }
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

The `Sudoku Solver` is a classic application of `backtracking`, where the algorithm tries to place a number in an empty cell and explores further. If a path leads to a dead end, it backtracks.

---

**`is_valid_placement(board, num, row, col)` Function:**
- This helper function checks if placing `num` at `(row, col)` is valid according to Sudoku rules.
- **Checks:**
- `Row`: Ensures `num` is not already present in the given `row`.
- `Column`: Ensures `num` is not already present in the given `col`.
- `3x3 Box`: Determines which 3x3 `subgrid` `(row, col)` belongs to and checks if `num` is already present in that `subgrid`.

    </li>
- Returns `True` if placement is valid, `False` otherwise.

**`find_empty_location(board)` Function:**
- Scans the `board` from `(0,0)` to `(8,8)` to find the next empty cell (represented by 0).
- Returns the `(row, col)` of the empty cell, or `(-1, -1)` if no empty cells are found.

**`solve_sudoku(board)` Function (Main Backtracking Logic):**
- `board`: The 9x9 Sudoku grid, with 0s representing empty cells.

**Algorithm Steps:**
- **Base Case:** Calls `find_empty_location`. If it returns `(-1, -1)` (meaning no empty cells are left), the `board` is solved, so it returns `true`.
- **Recursive Step:** If an empty cell `(row, col)` is found:
- Iterate `num` from 1 to 9:
- **Validity Check:** If `is_valid_placement(board, num, row, col)` returns `true` (placing `num` at `(row, col)` is valid):
- **Place Number:** Place `num` at `board[row][col]`.
- **Recur:** Recursively call `solve_sudoku(board)` to attempt to solve the rest of the `board`.
- If the recursive call returns `true` (a solution was found down this path), then this `num` was correct, and we propagate `true` back up.
- **Backtrack:** If the recursive call returns `false` (this `num` did not lead to a solution), remove `num` from `board[row][col]` (reset to 0). This "undoes" the choice, allowing the loop to try the next `num`.

                    </li>

            </li>
- If the loop finishes (all numbers 1-9 have been tried for `(row, col)` and none led to a solution), return `false`. This signifies a dead end from the current `board` state, and the previous recursive call will backtrack.

    </li>

[Back to Implementation](#implementation)

## Applications

### Application

Solving `Sudoku` puzzles using `backtracking` is a direct application of `constraint satisfaction problems` and illustrates fundamental algorithmic principles applicable to a broader range of challenges:
- **Constraint Satisfaction Problems (CSPs):** Sudoku is a classic example of a CSP. The `backtracking` approach is generalizable to other CSPs like coloring graphs, scheduling tasks, and solving logic puzzles.
- **Game Development:** Developing AI for puzzle games or generating puzzles (e.g., generating solvable Sudoku grids).
- **Resource Allocation:** Similar to N-Queens, but for specific grid-based allocations, where resources (numbers) must be placed without violating rules (constraints).
- **Automated Reasoning:** In artificial intelligence, `backtracking` forms the basis for search algorithms used in expert systems and automated planning.
- **Combinatorial Optimization:** Finding one or all solutions from a finite set of possibilities that satisfy certain criteria.

