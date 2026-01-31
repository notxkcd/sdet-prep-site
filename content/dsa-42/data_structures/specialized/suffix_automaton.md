---
title: "Suffix Automaton"
---

A `Suffix Automaton` (also known as a `Directed Acyclic Word Graph` or `DAWG`) is a powerful data structure that represents all substrings of a given string. It is the smallest possible `deterministic finite automaton (DFA)` that accepts all suffixes of the string, and by extension, all its substrings.

While being extremely space-efficient (requiring `O(N)` space for a string of length `N`), it can answer complex string queries in linear time. It is a more powerful and often more efficient alternative to both `Suffix Trees` and `Suffix Arrays` for many problems.

## How it Works

### How it Works (Expanded)

A `Suffix Automaton` is a directed acyclic graph where each path from the `initial state` to any other `state` corresponds to a unique substring of the string. Each `state` represents a set of substrings that end at the same positions in the original string.

---

Conceptual Suffix Automaton for "abacaba":

Initial State -> a -> b -> a -> c -> a -> b -> a
     \         / |  ...
      \       /  |
       `-----` (transitions for other substrings)

Key Components:
- States: Each state represents a set of substrings.
- Transitions: Edges labeled with characters.
- Suffix Links: Special links from a state to another state representing the longest proper suffix of the strings in the current state.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
# Conceptual Suffix Automaton in Python (simplified, full implementation is very complex)
# This focuses on the structure and online construction concept.

class SuffixAutomatonNode:
    def __init__(self, length):
        self.length = length # Length of the longest substring for this state
        self.link = -1 # Suffix link, -1 indicates no link initially
        self.transitions = {} # map of char to state index

class SuffixAutomaton:
    def __init__(self):
        self.states = [SuffixAutomatonNode(0)] # Initial state
        self.last = 0 # Index of the state corresponding to the whole string

    def extend(self, char):
        new_state_idx = len(self.states)
        self.states.append(SuffixAutomatonNode(self.states[self.last].length + 1))
        
        p = self.last
        while p != -1 and char not in self.states[p].transitions:
            self.states[p].transitions[char] = new_state_idx
            p = self.states[p].link
        
        if p == -1:
            self.states[new_state_idx].link = 0 # Link to initial state
        else:
            q = self.states[p].transitions[char]
            if self.states[q].length == self.states[p].length + 1:
                self.states[new_state_idx].link = q
            else:
                clone_idx = len(self.states)
                clone_node = SuffixAutomatonNode(self.states[p].length + 1)
                clone_node.transitions = self.states[q].transitions.copy()
                clone_node.link = self.states[q].link
                self.states.append(clone_node)

                while p != -1 and self.states[p].transitions.get(char) == q:
                    self.states[p].transitions[char] = clone_idx
                    p = self.states[p].link
                
                self.states[q].link = clone_idx
                self.states[new_state_idx].link = clone_idx
        
        self.last = new_state_idx

    def build(self, text):
        for char in text:
            self.extend(char)

    def contains(self, pattern):
        current_state_idx = 0
        for char in pattern:
            if char in self.states[current_state_idx].transitions:
                current_state_idx = self.states[current_state_idx].transitions[char]
            else:
                return False
        return True

# sa = SuffixAutomaton()
# sa.build("abacaba")
# print("Contains 'aba':", sa.contains("aba")) # Expected: True
# print("Contains 'baba':", sa.contains("baba")) # Expected: False
```

### Javascript

```javascript
// Conceptual Suffix Automaton in JavaScript (simplified)

class SuffixAutomatonNode {
    constructor(length) {
        this.length = length;
        this.link = -1;
        this.transitions = new Map();
    }
}

class SuffixAutomaton {
    constructor() {
        this.states = [new SuffixAutomatonNode(0)];
        this.last = 0;
    }

    extend(char) {
        const newStateIdx = this.states.length;
        this.states.push(new SuffixAutomatonNode(this.states[this.last].length + 1));
        
        let p = this.last;
        while (p !== -1 && !this.states[p].transitions.has(char)) {
            this.states[p].transitions.set(char, newStateIdx);
            p = this.states[p].link;
        }
        
        if (p === -1) {
            this.states[newStateIdx].link = 0; // Link to initial state
        } else {
            const qIdx = this.states[p].transitions.get(char);
            if (this.states[qIdx].length === this.states[p].length + 1) {
                this.states[newStateIdx].link = qIdx;
            } else {
                const cloneIdx = this.states.length;
                const cloneNode = new SuffixAutomatonNode(this.states[p].length + 1);
                cloneNode.transitions = new Map(this.states[qIdx].transitions);
                cloneNode.link = this.states[qIdx].link;
                this.states.push(cloneNode);

                while (p !== -1 && this.states[p].transitions.get(char) === qIdx) {
                    this.states[p].transitions.set(char, cloneIdx);
                    p = this.states[p].link;
                }
                
                this.states[qIdx].link = cloneIdx;
                this.states[newStateIdx].link = cloneIdx;
            }
        }
        
        this.last = newStateIdx;
    }

    build(text) {
        for (const char of text) {
            this.extend(char);
        }
    }

    contains(pattern) {
        let currentStateIdx = 0;
        for (const char of pattern) {
            if (this.states[currentStateIdx].transitions.has(char)) {
                currentStateIdx = this.states[currentStateIdx].transitions.get(char);
            } else {
                return false;
            }
        }
        return true;
    }
}

// const sa = new SuffixAutomaton();
// sa.build("abacaba");
// console.log("Contains 'aba':", sa.contains("aba")); // Expected: true
// console.log("Contains 'baba':", sa.contains("baba")); // Expected: false
```

### Typescript

```typescript
// Conceptual Suffix Automaton in TypeScript (simplified)

class SuffixAutomatonNodeTS {
    public length: number;
    public link: number;
    public transitions: Map<string, number>;

    constructor(length: number) {
        this.length = length;
        this.link = -1;
        this.transitions = new Map();
    }
}

class SuffixAutomatonTS {
    public states: SuffixAutomatonNodeTS[];
    public last: number;

    constructor() {
        this.states = [new SuffixAutomatonNodeTS(0)];
        this.last = 0;
    }

    public extend(char: string): void {
        const newStateIdx = this.states.length;
        this.states.push(new SuffixAutomatonNodeTS(this.states[this.last].length + 1));
        
        let p = this.last;
        while (p !== -1 && !this.states[p].transitions.has(char)) {
            this.states[p].transitions.set(char, newStateIdx);
            p = this.states[p].link;
        }
        
        if (p === -1) {
            this.states[newStateIdx].link = 0; // Link to initial state
        } else {
            const qIdx = this.states[p].transitions.get(char)!;
            if (this.states[qIdx].length === this.states[p].length + 1) {
                this.states[newStateIdx].link = qIdx;
            } else {
                const cloneIdx = this.states.length;
                const cloneNode = new SuffixAutomatonNodeTS(this.states[p].length + 1);
                cloneNode.transitions = new Map(this.states[qIdx].transitions);
                cloneNode.link = this.states[qIdx].link;
                this.states.push(cloneNode);

                while (p !== -1 && this.states[p].transitions.get(char) === qIdx) {
                    this.states[p].transitions.set(char, cloneIdx);
                    p = this.states[p].link;
                }
                
                this.states[qIdx].link = cloneIdx;
                this.states[newStateIdx].link = cloneIdx;
            }
        }
        
        this.last = newStateIdx;
    }

    public build(text: string): void {
        for (const char of text) {
            this.extend(char);
        }
    }

    public contains(pattern: string): boolean {
        let currentStateIdx = 0;
        for (const char of pattern) {
            if (this.states[currentStateIdx].transitions.has(char)) {
                currentStateIdx = this.states[currentStateIdx].transitions.get(char)!;
            } else {
                return false;
            }
        }
        return true;
    }
}

// const saTS = new SuffixAutomatonTS();
// saTS.build("abacaba");
// console.log("Contains 'aba':", saTS.contains("aba")); // Expected: true
// console.log("Contains 'baba':", saTS.contains("baba")); // Expected: false
```

### Cpp

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <map>

struct SuffixAutomatonNode {
    int length;
    int link;
    std::map<char, int> transitions;

    SuffixAutomatonNode(int len) : length(len), link(-1) {}
};

class SuffixAutomaton {
public:
    std::vector<SuffixAutomatonNode> states;
    int last;

    SuffixAutomaton() {
        states.emplace_back(0); // Initial state
        last = 0;
    }

    void extend(char c) {
        int new_state_idx = states.size();
        states.emplace_back(states[last].length + 1);
        
        int p = last;
        while (p != -1 && states[p].transitions.find(c) == states[p].transitions.end()) {
            states[p].transitions[c] = new_state_idx;
            p = states[p].link;
        }
        
        if (p == -1) {
            states[new_state_idx].link = 0; // Link to initial state
        } else {
            int q_idx = states[p].transitions[c];
            if (states[q_idx].length == states[p].length + 1) {
                states[new_state_idx].link = q_idx;
            } else {
                int clone_idx = states.size();
                SuffixAutomatonNode clone_node(states[p].length + 1);
                clone_node.transitions = states[q_idx].transitions;
                clone_node.link = states[q_idx].link;
                states.push_back(clone_node);

                while (p != -1 && states[p].transitions[c] == q_idx) {
                    states[p].transitions[c] = clone_idx;
                    p = states[p].link;
                }
                
                states[q_idx].link = clone_idx;
                states[new_state_idx].link = clone_idx;
            }
        }
        
        last = new_state_idx;
    }

    void build(const std::string& text) {
        for (char c : text) {
            extend(c);
        }
    }

    bool contains(const std::string& pattern) {
        int current_state_idx = 0;
        for (char c : pattern) {
            auto it = states[current_state_idx].transitions.find(c);
            if (it != states[current_state_idx].transitions.end()) {
                current_state_idx = it->second;
            } else {
                return false;
            }
        }
        return true;
    }
};

// int main() {
//     SuffixAutomaton sa;
//     sa.build("abacaba");
//     std::cout << "Contains 'aba': " << (sa.contains("aba") ? "True" : "False") << std::endl;
//     std::cout << "Contains 'baba': " << (sa.contains("baba") ? "True" : "False") << std::endl;
//     return 0;
// }
```

### Go

```go
package main

import "fmt"

type SuffixAutomatonNode struct {
    Length      int
    Link        int
    Transitions map[rune]int
}

func NewSuffixAutomatonNode(length int) <em>SuffixAutomatonNode {
    return &SuffixAutomatonNode{
        Length:      length,
        Link:        -1,
        Transitions: make(map[rune]int),
    }
}

type SuffixAutomaton struct {
    States []</em>SuffixAutomatonNode
    Last   int
}

func NewSuffixAutomaton() <em>SuffixAutomaton {
    return &SuffixAutomaton{
        States: []</em>SuffixAutomatonNode{NewSuffixAutomatonNode(0)},
        Last:   0,
    }
}

func (sa <em>SuffixAutomaton) Extend(char rune) {
    newStateIdx := len(sa.States)
    sa.States = append(sa.States, NewSuffixAutomatonNode(sa.States[sa.Last].Length+1))
    
    p := sa.Last
    for p != -1 {
        if _, ok := sa.States[p].Transitions[char]; !ok {
            sa.States[p].Transitions[char] = newStateIdx
            p = sa.States[p].Link
        } else {
            break
        }
    }
    
    if p == -1 {
        sa.States[newStateIdx].Link = 0
    } else {
        qIdx := sa.States[p].Transitions[char]
        if sa.States[qIdx].Length == sa.States[p].Length+1 {
            sa.States[newStateIdx].Link = qIdx
        } else {
            cloneIdx := len(sa.States)
            cloneNode := NewSuffixAutomatonNode(sa.States[p].Length + 1)
            cloneNode.Transitions = make(map[rune]int)
            for k, v := range sa.States[qIdx].Transitions {
                cloneNode.Transitions[k] = v
            }
            cloneNode.Link = sa.States[qIdx].Link
            sa.States = append(sa.States, cloneNode)

            for p != -1 && sa.States[p].Transitions[char] == qIdx {
                sa.States[p].Transitions[char] = cloneIdx
                p = sa.States[p].Link
            }
            
            sa.States[qIdx].Link = cloneIdx
            sa.States[newStateIdx].Link = cloneIdx
        }
    }
    
    sa.Last = newStateIdx
}

func (sa </em>SuffixAutomaton) Build(text string) {
    for _, char := range text {
        sa.Extend(char)
    }
}

func (sa <em>SuffixAutomaton) Contains(pattern string) bool {
    currentStateIdx := 0
    for _, char := range pattern {
        if nextState, ok := sa.States[currentStateIdx].Transitions[char]; ok {
            currentStateIdx = nextState
        } else {
            return false
        }
    }
    return true
}

// func main() {
//     sa := NewSuffixAutomaton()
//     sa.Build("abacaba")
//     fmt.Println("Contains 'aba':", sa.Contains("aba"))
//     fmt.Println("Contains 'baba':", sa.Contains("baba"))
// }
```

### D

```d
import std.stdio;
import std.string;
import std.array;
import std.map;

class SuffixAutomatonNode {
    int length;
    int link;
    int[char] transitions;

    this(int len) {
        this.length = len;
        this.link = -1;
        this.transitions = null;
    }
}

class SuffixAutomaton {
    SuffixAutomatonNode[] states;
    int last;

    this() {
        states ~= new SuffixAutomatonNode(0);
        last = 0;
    }

    void extend(char c) {
        int newStateIdx = cast(int)states.length;
        states ~= new SuffixAutomatonNode(states[last].length + 1);
        
        int p = last;
        while (p != -1 && (c !in states[p].transitions)) {
            states[p].transitions[c] = newStateIdx;
            p = states[p].link;
        }
        
        if (p == -1) {
            states[newStateIdx].link = 0;
        } else {
            int qIdx = states[p].transitions[c];
            if (states[qIdx].length == states[p].length + 1) {
                states[newStateIdx].link = qIdx;
            } else {
                int cloneIdx = cast(int)states.length;
                auto cloneNode = new SuffixAutomatonNode(states[p].length + 1);
                cloneNode.transitions = states[qIdx].transitions.dup;
                cloneNode.link = states[qIdx].link;
                states ~= cloneNode;

                while (p != -1 && states[p].transitions[c] == qIdx) {
                    states[p].transitions[c] = cloneIdx;
                    p = states[p].link;
                }
                
                states[qIdx].link = cloneIdx;
                states[newStateIdx].link = cloneIdx;
            }
        }
        
        last = newStateIdx;
    }

    void build(string text) {
        foreach (char c; text) {
            extend(c);
        }
    }

    bool contains(string pattern) {
        int currentStateIdx = 0;
        foreach (char c; pattern) {
            if (auto pNextState = c in states[currentStateIdx].transitions) {
                currentStateIdx = </em>pNextState;
            } else {
                return false;
            }
        }
        return true;
    }
}

// void main() {
//     auto sa = new SuffixAutomaton();
//     sa.build("abacaba");
//     writefln("Contains 'aba': %s", sa.contains("aba"));
//     writefln("Contains 'baba': %s", sa.contains("baba"));
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

The provided code illustrates the conceptual `online construction` algorithm for a `Suffix Automaton`. This algorithm processes the string one character at a time and extends the automaton.

---

**`SuffixAutomatonNode` Class:** Represents a state in the automaton.
- `length`: The length of the longest string corresponding to this state.
- `link`: A pointer to another state. This "`suffix link`" points to the state corresponding to the longest proper suffix of the strings in the current state.
- `transitions`: A map from characters to other state indices.

**`SuffixAutomaton` Class:**
- `states`: An array or vector storing all the `nodes` (states) of the automaton.
- `last`: The index of the state corresponding to the entire string processed so far.
- **`extend(char)`:** This is the core of the construction algorithm.
- Create a new `state` for the new, longer string.
- Follow the `suffix links` from the previous `last` state, adding transitions to the new `state` for the current character.
- If a transition for the character already exists, one of two cases occurs:
- The transition is "continuous" (satisfies a length check), so the new `state`'s `suffix link` can point directly to it.
- The transition is "non-continuous", which requires creating a new "`clone`" state to split the transition and maintain the automaton's properties. This is the most complex part of the algorithm.

            </li>
- Update `last` to point to the new `state`.

    </li>
- **`build(text)`:** Iterates through the input string and calls `extend` for each character.
- **`contains(pattern)`:** Simply traverses the automaton from the initial state according to the characters in the pattern.

[Back to Implementation](#implementation)

## Applications

### Application

Suffix Automata are one of the most powerful and versatile data structures for string processing, often providing the most efficient solutions to complex problems.
- **Finding All Occurrences of a Pattern:** Can find all occurrences of a pattern P in a text T in `O(|P| + num_occurrences)` time after building the automaton in `O(|T|)` time.
- **Counting Distinct Substrings:** The number of distinct substrings is simply the number of unique paths from the initial state, which can be calculated in `O(|T|)`.
- **Longest Common Substring:** Can solve the longest common substring problem for two strings in linear time with respect to their lengths.
- **Bioinformatics:** Used for a wide variety of sequence alignment and pattern matching tasks in DNA and protein analysis.
- **Data Compression:** The structure of the automaton can be used to find and exploit redundancies in a string.

