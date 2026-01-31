---
title: "Dancing Links (DLX)"
---

`Dancing Links`, also known as `DLX`, is not a data structure in the traditional sense but rather a technique developed by Donald Knuth to efficiently implement his `Algorithm X`. It is used to solve the `exact cover problem`, a type of combinatorial problem that aims to find all possible ways to cover a set with a collection of subsets.

The "`dancing`" aspect refers to the way pointers are cleverly manipulated (linked and unlinked) during the backtracking process, making the algorithm surprisingly efficient. It uses a circular, doubly-linked list of lists to represent a sparse matrix, where each 1 in the matrix indicates that a subset contains a particular element.

## How it Works

### How it Works (Expanded)

`DLX` uses a grid of `nodes` to represent the `exact cover matrix`. Each `node` is part of two circular, doubly-linked lists: one for its `column` and one for its `row`.

---

Conceptual DLX Structure:
- A special `header node` H links to all column header nodes.
- Each `column header` C links to all `nodes` in its column.
- Each `node` in a row links to the next `node` in its row.

       H <-> C1 <-> C2 <-> C3 <-> H
             ^     ^     ^
             |     |     |
            N11 <- N12   |
             ^     ^     |
             |     |     |
            N21    |    N23
                   ^
                   |
                  N32 <- N33

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
# Conceptual Dancing Links (DLX) in Python (highly simplified)
# This focuses on the node structure and the basic cover/uncover idea.
# A full implementation is extensive and highly detailed.

class DLXNode:
    def __init__(self):
        self.left = self
        self.right = self
        self.up = self
        self.down = self
        self.column = self # Points to the column header node

class DLX:
    def __init__(self, num_columns):
        self.header = DLXNode() # Special header for the column list
        self.columns = []
        for _ in range(num_columns):
            new_col = DLXNode()
            self.columns.append(new_col)
            # Link into header list
            new_col.right = self.header
            new_col.left = self.header.left
            self.header.left.right = new_col
            self.header.left = new_col

    def add_row(self, row_indices):
        # Link nodes for each 1 in a row of the matrix
        first_node = None
        for col_idx in row_indices:
            new_node = DLXNode()
            new_node.column = self.columns[col_idx]
            
            # Link into column
            new_node.down = self.columns[col_idx]
            new_node.up = self.columns[col_idx].up
            self.columns[col_idx].up.down = new_node
            self.columns[col_idx].up = new_node
            
            # Link into row
            if first_node:
                new_node.right = first_node
                new_node.left = first_node.left
                first_node.left.right = new_node
                first_node.left = new_node
            else:
                first_node = new_node

    def _cover(self, column_header):
        # "Unlink" a column and all rows it intersects
        column_header.right.left = column_header.left
        column_header.left.right = column_header.right
        
        # Iterate down the column
        i = column_header.down
        while i != column_header:
            j = i.right
            while j != i:
                j.down.up = j.up
                j.up.down = j.down
                j = j.right
            i = i.down

    def _uncover(self, column_header):
        # "Relink" a column and all rows it intersects (reverse of cover)
        i = column_header.up
        while i != column_header:
            j = i.left
            while j != i:
                j.down.up = j
                j.up.down = j
                j = j.left
            i = i.up

        column_header.right.left = column_header
        column_header.left.right = column_header

    def solve(self):
        # The main recursive search function (Algorithm X)
        if self.header.right == self.header: # Matrix is empty, solution found
            # Process solution
            return True
        
        # Choose a column (e.g., one with fewest nodes)
        col_to_cover = self.header.right
        self._cover(col_to_cover)
        
        # For each row in the chosen column...
        r = col_to_cover.down
        while r != col_to_cover:
            # ... add row to partial solution ...
            
            # ... cover other columns in this row ...
            j = r.right
            while j != r:
                self._cover(j.column)
                j = j.right
            
            # Recurse
            if self.solve():
                return True # Found a solution
            
            # Backtrack (uncover columns)
            j = r.left
            while j != r:
                self._uncover(j.column)
                j = j.left
            
            r = r.down
            
        self._uncover(col_to_cover)
        return False # No solution found from this path

# Example Setup (for a small exact cover problem):
# dlx = DLX(num_columns=7)
# dlx.add_row([2, 4, 5])
# dlx.add_row([0, 3, 6])
# # ... add more rows
# dlx.solve()
```

### Javascript

```javascript
class DLXNode {
    constructor() {
        this.left = this;
        this.right = this;
        this.up = this;
        this.down = this;
        this.column = this; // Points to the column header node
    }
}

class DLX {
    constructor(numColumns) {
        this.header = new DLXNode(); // Special header for the column list
        this.columns = [];
        for (let i = 0; i < numColumns; i++) {
            const newCol = new DLXNode();
            this.columns.push(newCol);
            newCol.right = this.header;
            newCol.left = this.header.left;
            this.header.left.right = newCol;
            this.header.left = newCol;
        }
    }

    addRow(rowIndices) {
        let firstNode = null;
        for (const colIdx of rowIndices) {
            const newNode = new DLXNode();
            newNode.column = this.columns[colIdx];
            
            // Link into column
            newNode.down = this.columns[colIdx];
            newNode.up = this.columns[colIdx].up;
            this.columns[colIdx].up.down = newNode;
            this.columns[colIdx].up = newNode;
            
            // Link into row
            if (firstNode) {
                newNode.right = firstNode;
                newNode.left = firstNode.left;
                firstNode.left.right = newNode;
                firstNode.left = newNode;
            } else {
                firstNode = newNode;
            }
        }
    }

    _cover(columnHeader) {
        columnHeader.right.left = columnHeader.left;
        columnHeader.left.right = columnHeader.right;
        
        for (let i = columnHeader.down; i !== columnHeader; i = i.down) {
            for (let j = i.right; j !== i; j = j.right) {
                j.down.up = j.up;
                j.up.down = j.down;
            }
        }
    }

    _uncover(columnHeader) {
        for (let i = columnHeader.up; i !== columnHeader; i = i.up) {
            for (let j = i.left; j !== i; j = j.left) {
                j.down.up = j;
                j.up.down = j;
            }
        }
        columnHeader.right.left = columnHeader;
        columnHeader.left.right = columnHeader;
    }

    solve() {
        if (this.header.right === this.header) {
            // Solution found
            return true;
        }
        
        // Choose a column
        let colToCover = this.header.right;
        this._cover(colToCover);
        
        for (let r = colToCover.down; r !== colToCover; r = r.down) {
            // Add row to partial solution

            for (let j = r.right; j !== r; j = j.right) {
                this._cover(j.column);
            }
            
            if (this.solve()) {
                return true;
            }
            
            // Backtrack
            for (let j = r.left; j !== r; j = j.left) {
                this._uncover(j.column);
            }
        }
        
        this._uncover(colToCover);
        return false;
    }
}

// const dlx = new DLX(7);
// dlx.addRow([2, 4, 5]);
// dlx.addRow([0, 3, 6]);
// // ... add more rows for a specific problem
// dlx.solve();
```

### Typescript

```typescript
class DLXNodeTS {
    public left: DLXNodeTS;
    public right: DLXNodeTS;
    public up: DLXNodeTS;
    public down: DLXNodeTS;
    public column: DLXNodeTS;

    constructor() {
        this.left = this;
        this.right = this;
        this.up = this;
        this.down = this;
        this.column = this;
    }
}

class DLXTS {
    public header: DLXNodeTS;
    public columns: DLXNodeTS[];

    constructor(numColumns: number) {
        this.header = new DLXNodeTS();
        this.columns = [];
        for (let i = 0; i < numColumns; i++) {
            const newCol = new DLXNodeTS();
            this.columns.push(newCol);
            newCol.right = this.header;
            newCol.left = this.header.left;
            this.header.left.right = newCol;
            this.header.left = newCol;
        }
    }

    public addRow(rowIndices: number[]): void {
        let firstNode: DLXNodeTS | null = null;
        for (const colIdx of rowIndices) {
            const newNode = new DLXNodeTS();
            newNode.column = this.columns[colIdx];
            
            // Link into column
            newNode.down = this.columns[colIdx];
            newNode.up = this.columns[colIdx].up;
            this.columns[colIdx].up.down = newNode;
            this.columns[colIdx].up = newNode;
            
            // Link into row
            if (firstNode) {
                newNode.right = firstNode;
                newNode.left = firstNode.left;
                firstNode.left.right = newNode;
                firstNode.left = newNode;
            } else {
                firstNode = newNode;
            }
        }
    }

    private _cover(columnHeader: DLXNodeTS): void {
        columnHeader.right.left = columnHeader.left;
        columnHeader.left.right = columnHeader.right;
        
        for (let i = columnHeader.down; i !== columnHeader; i = i.down) {
            for (let j = i.right; j !== i; j = j.right) {
                j.down.up = j.up;
                j.up.down = j.down;
            }
        }
    }

    private _uncover(columnHeader: DLXNodeTS): void {
        for (let i = columnHeader.up; i !== columnHeader; i = i.up) {
            for (let j = i.left; j !== i; j = j.left) {
                j.down.up = j;
                j.up.down = j;
            }
        }
        columnHeader.right.left = columnHeader;
        columnHeader.left.right = columnHeader;
    }

    public solve(): boolean {
        if (this.header.right === this.header) {
            // Solution found
            return true;
        }
        
        let colToCover = this.header.right;
        this._cover(colToCover);
        
        for (let r = colToCover.down; r !== colToCover; r = r.down) {
            // Add row to partial solution

            for (let j = r.right; j !== r; j = j.right) {
                this._cover(j.column);
            }
            
            if (this.solve()) {
                return true;
            }
            
            // Backtrack
            for (let j = r.left; j !== r; j = j.left) {
                this._uncover(j.column);
            }
        }
        
        this._uncover(colToCover);
        return false;
    }
}

// const dlxTS = new DLXTS(7);
// dlxTS.addRow([2, 4, 5]);
// dlxTS.addRow([0, 3, 6]);
// // ... add more rows for a specific problem
// dlxTS.solve();
```

### Cpp

```cpp
#include <iostream>
#include <vector>

class DLXNode {
public:
    DLXNode<em> left;
    DLXNode</em> right;
    DLXNode<em> up;
    DLXNode</em> down;
    DLXNode<em> column; // Points to the column header node

    DLXNode() {
        left = right = up = down = column = this;
    }
};

class DLX {
public:
    DLXNode</em> header;
    std::vector<DLXNode<em>> columns;

    DLX(int num_columns) {
        header = new DLXNode();
        columns.resize(num_columns);
        for (int i = 0; i < num_columns; ++i) {
            DLXNode</em> new_col = new DLXNode();
            columns[i] = new_col;
            new_col->right = header;
            new_col->left = header->left;
            header->left->right = new_col;
            header->left = new_col;
        }
    }

    void addRow(const std::vector<int>& row_indices) {
        DLXNode<em> first_node = nullptr;
        for (int col_idx : row_indices) {
            DLXNode</em> new_node = new DLXNode();
            new_node->column = columns[col_idx];
            
            // Link into column
            new_node->down = columns[col_idx];
            new_node->up = columns[col_idx]->up;
            columns[col_idx]->up->down = new_node;
            columns[col_idx]->up = new_node;
            
            // Link into row
            if (first_node) {
                new_node->right = first_node;
                new_node->left = first_node->left;
                first_node->left->right = new_node;
                first_node->left = new_node;
            } else {
                first_node = new_node;
            }
        }
    }

    void cover(DLXNode<em> column_header) {
        column_header->right->left = column_header->left;
        column_header->left->right = column_header->right;
        
        for (DLXNode</em> i = column_header->down; i != column_header; i = i->down) {
            for (DLXNode<em> j = i->right; j != i; j = j->right) {
                j->down->up = j->up;
                j->up->down = j->down;
            }
        }
    }

    void uncover(DLXNode</em> column_header) {
        for (DLXNode<em> i = column_header->up; i != column_header; i = i->up) {
            for (DLXNode</em> j = i->left; j != i; j = j.left) {
                j->down->up = j;
                j->up->down = j;
            }
        }
        column_header->right->left = column_header;
        column_header->left->right = column_header;
    }

    bool solve() {
        if (header->right == header) {
            // Solution found
            return true;
        }
        
        DLXNode<em> col_to_cover = header->right;
        cover(col_to_cover);
        
        for (DLXNode</em> r = col_to_cover->down; r != col_to_cover; r = r->down) {
            // Add row to partial solution

            for (DLXNode<em> j = r->right; j != r; j = j->right) {
                cover(j->column);
            }
            
            if (solve()) {
                return true;
            }
            
            // Backtrack
            for (DLXNode</em> j = r->left; j != r; j = j->left) {
                uncover(j->column);
            }
        }
        
        uncover(col_to_cover);
        return false;
    }
};

// int main() {
//     DLX dlx(7);
//     dlx.addRow({2, 4, 5});
//     dlx.addRow({0, 3, 6});
//     // ... add more rows
//     dlx.solve();
//     return 0;
// }
```

### Go

```go
package main

import "fmt"

type DLXNode struct {
    Left, Right, Up, Down <em>DLXNode
    Column                </em>DLXNode
}

func NewDLXNode() <em>DLXNode {
    node := &DLXNode{}
    node.Left = node
    node.Right = node
    node.Up = node
    node.Down = node
    node.Column = node
    return node
}

type DLX struct {
    Header  </em>DLXNode
    Columns []<em>DLXNode
}

func NewDLX(numColumns int) </em>DLX {
    header := NewDLXNode()
    columns := make([]<em>DLXNode, numColumns)
    for i := 0; i < numColumns; i++ {
        newCol := NewDLXNode()
        columns[i] = newCol
        newCol.Right = header
        newCol.Left = header.Left
        header.Left.Right = newCol
        header.Left = newCol
    }
    return &DLX{Header: header, Columns: columns}
}

func (dlx </em>DLX) AddRow(rowIndices []int) {
    var firstNode <em>DLXNode
    for _, colIdx := range rowIndices {
        newNode := NewDLXNode()
        newNode.Column = dlx.Columns[colIdx]
        
        // Link into column
        newNode.Down = dlx.Columns[colIdx]
        newNode.Up = dlx.Columns[colIdx].Up
        dlx.Columns[colIdx].Up.Down = newNode
        dlx.Columns[colIdx].Up = newNode
        
        // Link into row
        if firstNode != nil {
            newNode.Right = firstNode
            newNode.Left = firstNode.Left
            firstNode.Left.Right = newNode
            firstNode.Left = newNode
        } else {
            firstNode = newNode
        }
    }
}

func (dlx </em>DLX) cover(columnHeader <em>DLXNode) {
    columnHeader.Right.Left = columnHeader.Left
    columnHeader.Left.Right = columnHeader.Right
    
    for i := columnHeader.Down; i != columnHeader; i = i.Down {
        for j := i.Right; j != i; j = j.Right {
            j.Down.Up = j.Up
            j.Up.Down = j.Down
        }
    }
}

func (dlx </em>DLX) uncover(columnHeader <em>DLXNode) {
    for i := columnHeader.Up; i != columnHeader; i = i.Up {
        for j := i.Left; j != i; j = j.Left {
            j.Down.Up = j
            j.Up.Down = j
        }
    }
    columnHeader.Right.Left = columnHeader
    columnHeader.Left.Right = columnHeader
}

func (dlx </em>DLX) Solve() bool {
    if dlx.Header.Right == dlx.Header {
        // Solution found
        return true
    }
    
    colToCover := dlx.Header.Right
    dlx.cover(colToCover)
    
    for r := colToCover.Down; r != colToCover; r = r.Down {
        // Add row to partial solution

        for j := r.Right; j != r; j = j.Right {
            dlx.cover(j.Column)
        }
        
        if dlx.Solve() {
            return true
        }
        
        // Backtrack
        for j := r.Left; j != r; j = j.Left {
            dlx.uncover(j.Column)
        }
    }
    
    dlx.uncover(colToCover)
    return false
}

// func main() {
//     dlx := NewDLX(7)
//     dlx.AddRow([]int{2, 4, 5})
//     dlx.AddRow([]int{0, 3, 6})
//     // ... add more rows
//     dlx.Solve()
// }
```

### D

```d
import std.stdio;
import std.array;
import std.algorithm;

class DLXNode {
    DLXNode left, right, up, down, column;

    this() {
        left = this;
        right = this;
        up = this;
        down = this;
        column = this;
    }
}

class DLX {
    DLXNode header;
    DLXNode[] columns;

    this(int numColumns) {
        header = new DLXNode();
        columns = new DLXNode[numColumns];
        foreach (i; 0..numColumns) {
            auto newCol = new DLXNode();
            columns[i] = newCol;
            newCol.right = header;
            newCol.left = header.left;
            header.left.right = newCol;
            header.left = newCol;
        }
    }

    void addRow(int[] rowIndices) {
        DLXNode firstNode = null;
        foreach (colIdx; rowIndices) {
            auto newNode = new DLXNode();
            newNode.column = columns[colIdx];
            
            // Link into column
            newNode.down = columns[colIdx];
            newNode.up = columns[colIdx].up;
            columns[colIdx].up.down = newNode;
            columns[colIdx].up = newNode;
            
            // Link into row
            if (firstNode !is null) {
                newNode.right = firstNode;
                newNode.left = firstNode.left;
                firstNode.left.right = newNode;
                firstNode.left = newNode;
            } else {
                firstNode = newNode;
            }
        }
    }

    private void cover(DLXNode columnHeader) {
        columnHeader.right.left = columnHeader.left;
        columnHeader.left.right = columnHeader.right;
        
        for (auto i = columnHeader.down; i !is columnHeader; i = i.down) {
            for (auto j = i.right; j !is i; j = j.right) {
                j.down.up = j.up;
                j.up.down = j.down;
            }
        }
    }

    private void uncover(DLXNode columnHeader) {
        for (auto i = columnHeader.up; i !is columnHeader; i = i.up) {
            for (auto j = i.left; j !is i; j = j.left) {
                j.down.up = j;
                j.up.down = j;
            }
        }
        columnHeader.right.left = columnHeader;
        columnHeader.left.right = columnHeader;
    }

    bool solve() {
        if (header.right is header) {
            // Solution found
            return true;
        }
        
        DLXNode colToCover = header.right;
        cover(colToCover);
        
        for (auto r = colToCover.down; r !is colToCover; r = r.down) {
            // Add row to partial solution

            for (auto j = r.right; j !is r; j = j.right) {
                cover(j.column);
            }
            
            if (solve()) {
                return true;
            }
            
            // Backtrack
            for (auto j = r.left; j !is r; j = j.left) {
                uncover(j.column);
            }
        }
        
        uncover(colToCover);
        return false;
    }
}

// void main() {
//     auto dlx = new DLX(7);
//     dlx.addRow([2, 4, 5]);
//     dlx.addRow([0, 3, 6]);
//     // ... add more rows
//     dlx.solve();
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

A `Dancing Links (DLX)` implementation is conceptually focused on pointer manipulation within a `toroidal doubly-linked list` structure. The code illustrates the setup and the crucial `cover` and `uncover` operations.

---

**`DLXNode` Class:**
- `left`, `right`, `up`, `down`: Pointers that create the grid of linked lists.
- `column`: A pointer from any `node` back to its `column header`.

**`DLX` Class:**
- `header`: A special `node` that acts as the entry point to the list of `column headers`.
- `columns`: An `array` of pointers to each `column header`.
- **`addRow(row_indices)`:** For each '1' in a conceptual row, it creates a new `DLXNode` and links it into both its respective `column list` (vertically) and its `row list` (horizontally).
- **`_cover(column_header)`:** This is the core of the algorithm.
- It "removes" the specified `column_header` from the main `header list` by unlinking its `left` and `right` pointers.
- It then iterates down this `column`. For each `node` `i` in the `column`, it iterates through its row (`j` from `i.right`), unlinking each `node j` from its respective `column`. This effectively removes all rows that intersect with the chosen `column`.

    </li>
- **`_uncover(column_header)`:** This reverses the `cover` operation by re-linking all the pointers, making backtracking extremely efficient.
- **`solve()`:** The recursive backtracking function. It selects a `column`, `covers` it, and then recursively tries to solve the subproblem for each `row` in that `column`. If a recursive call fails, it backtracks by `uncovering` everything.

[Back to Implementation](#implementation)

## Applications

### Application

Dancing Links (DLX) is the premier method for solving **exact cover problems**. These are problems where you must choose a subset of given sets such that every element in the universe is contained in exactly one of the chosen sets. Applications include:
- **Solving Puzzles:** It is famously used to create extremely fast solvers for puzzles like Sudoku, Pentominoes, and N-Queens, which can all be framed as exact cover problems.
- **Combinatorial Problems:** Any problem that can be modeled as an exact cover matrix is a candidate for DLX. For example, finding all ways to tile a grid with given shapes.
- **Algorithm Design:** As a powerful backtracking tool for certain NP-complete problems where the search space can be pruned effectively.

