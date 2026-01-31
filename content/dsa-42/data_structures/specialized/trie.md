---
title: "Trie"
---

A `Trie` (pronounced "try" or "tree", from retrieval) is a tree-like data structure used to store a dynamic set or associative array where the `keys` are usually strings. Unlike a `binary search tree`, `nodes` in a `Trie` do not store the `key`s themselves. Instead, their position in the `Trie` defines the `key` with which they are associated.

`Tries` are particularly useful for problems involving strings, such as autocomplete features, spell checkers, and IP routing.

## How it Works

### How it Works (Expanded)

Each `node` in a `Trie` represents a prefix of a `key`. The `root node` represents the empty string. Each child `node` represents an additional character in the `key`. Paths from the `root` to other `nodes` represent `keys`. A special flag (e.g., a boolean `is_end_of_word`) in a `node` marks the end of a complete `word`.

---

Example Trie for words: "apple", "app", "apricot", "banana"

       (root)
       /    \
      a      b
     /|\     |
    p l e    a
   /  |      |
  p   r      n
 /    |      |
l     i      a
|     |
 e     c      n
      |      |
      o      a
      |
      t

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def _collect_all_words(self, node, prefix, words):
        if node.is_end_of_word:
            words.append(prefix)
        for char, child_node in node.children.items():
            self._collect_all_words(child_node, prefix + char, words)

    def autocomplete(self, prefix: str) -> list[str]:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        words = []
        self._collect_all_words(node, prefix, words)
        return words

# Example Usage:
# trie = Trie()
# trie.insert("apple")
# trie.insert("app")
# trie.insert("apricot")
# trie.insert("banana")

# print(trie.search("apple"))      # True
# print(trie.search("app"))        # True
# print(trie.search("ap"))         # False (not a complete word)
# print(trie.starts_with("app"))   # True
# print(trie.autocomplete("ap"))   # ['apple', 'app', 'apricot']
# print(trie.autocomplete("ban"))  # ['banana']
# print(trie.autocomplete("bat"))  # []
```

### Javascript

```javascript
class TrieNode {
    constructor() {
        this.children = new Map();
        this.isEndOfWord = false;
    }
}

class Trie {
    constructor() {
        this.root = new TrieNode();
    }

    insert(word) {
        let node = this.root;
        for (const char of word) {
            if (!node.children.has(char)) {
                node.children.set(char, new TrieNode());
            }
            node = node.children.get(char);
        }
        node.isEndOfWord = true;
    }

    search(word) {
        let node = this.root;
        for (const char of word) {
            if (!node.children.has(char)) {
                return false;
            }
            node = node.children.get(char);
        }
        return node.isEndOfWord;
    }

    startsWith(prefix) {
        let node = this.root;
        for (const char of prefix) {
            if (!node.children.has(char)) {
                return false;
            }
            node = node.children.get(char);
        }
        return true;
    }

    _collectAllWords(node, prefix, words) {
        if (node.isEndOfWord) {
            words.push(prefix);
        }
        for (const [char, childNode] of node.children) {
            this._collectAllWords(childNode, prefix + char, words);
        }
    }

    autocomplete(prefix) {
        let node = this.root;
        for (const char of prefix) {
            if (!node.children.has(char)) {
                return [];
            }
            node = node.children.get(char);
        }
        
        const words = [];
        this._collectAllWords(node, prefix, words);
        return words;
    }
}

// Example Usage:
// const trie = new Trie();
// trie.insert("apple");
// trie.insert("app");
// trie.insert("apricot");
// trie.insert("banana");

// console.log(trie.search("apple"));      // true
// console.log(trie.search("app"));        // true
// console.log(trie.search("ap"));         // false
// console.log(trie.startsWith("app"));   // true
// console.log(trie.autocomplete("ap"));   // ['apple', 'app', 'apricot']
// console.log(trie.autocomplete("ban"));  // ['banana']
// console.log(trie.autocomplete("bat"));  // []
```

### Cpp

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <map> // For std::map to store children

class TrieNode {
public:
    std::map<char, TrieNode<em>> children;
    bool isEndOfWord;

    TrieNode() : isEndOfWord(false) {}

    ~TrieNode() {
        for (auto const& [key, val] : children) {
            delete val;
        }
    }
};

class Trie {
public:
    TrieNode</em> root;

    Trie() {
        root = new TrieNode();
    }

    ~Trie() {
        delete root;
    }

    void insert(const std::string& word) {
        TrieNode<em> node = root;
        for (char ch : word) {
            if (node->children.find(ch) == node->children.end()) {
                node->children[ch] = new TrieNode();
            }
            node = node->children[ch];
        }
        node->isEndOfWord = true;
    }

    bool search(const std::string& word) {
        TrieNode</em> node = root;
        for (char ch : word) {
            if (node->children.find(ch) == node->children.end()) {
                return false;
            }
            node = node->children[ch];
        }
        return node->isEndOfWord;
    }

    bool startsWith(const std::string& prefix) {
        TrieNode<em> node = root;
        for (char ch : prefix) {
            if (node->children.find(ch) == node->children.end()) {
                return false;
            }
            node = node->children[ch];
        }
        return true;
    }

private:
    void _collectAllWords(TrieNode</em> node, std::string currentPrefix, std::vector<std::string>& words) {
        if (node->isEndOfWord) {
            words.push_back(currentPrefix);
        }
        for (auto const& [ch, childNode] : node->children) {
            _collectAllWords(childNode, currentPrefix + ch, words);
        }
    }

public:
    std::vector<std::string> autocomplete(const std::string& prefix) {
        TrieNode* node = root;
        for (char ch : prefix) {
            if (node->children.find(ch) == node->children.end()) {
                return {};
            }
            node = node->children[ch];
        }
        
        std::vector<std::string> words;
        _collectAllWords(node, prefix, words);
        return words;
    }
};

// Example Usage:
// int main() {
//     Trie trie;
//     trie.insert("apple");
//     trie.insert("app");
//     trie.insert("apricot");
//     trie.insert("banana");

//     std::cout << "Search 'apple': " << (trie.search("apple") ? "True" : "False") << std::endl; // True
//     std::cout << "Search 'app': " << (trie.search("app") ? "True" : "False") << std::endl;     // True
//     std::cout << "Search 'ap': " << (trie.search("ap") ? "True" : "False") << std::endl;       // False
//     std::cout << "Starts with 'app': " << (trie.startsWith("app") ? "True" : "False") << std::endl; // True

//     std::vector<std::string> words_ap = trie.autocomplete("ap");
//     std::cout << "Autocomplete 'ap': ";
//     for (const std::string& word : words_ap) {
//         std::cout << word << " ";
//     }
//     std::cout << std::endl; // apple app apricot

//     std::vector<std::string> words_ban = trie.autocomplete("ban");
//     std::cout << "Autocomplete 'ban': ";
//     for (const std::string& word : words_ban) {
//         std::cout << word << " ";
//     }
//     std::cout << std::endl; // banana

//     return 0;
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

A Trie is typically implemented using nested hash maps (or arrays) to represent the `children` of each `TrieNode`.

---

**`TrieNode` Class:**
- `children`: A dictionary/map where `keys` are characters and `values` are pointers to child `TrieNode`s.
- `is_end_of_word`: A boolean flag, true if this `node` marks the end of a valid `word`.

**`Trie` Class:**
- `root`: A pointer to the `root TrieNode`.
- **`insert(word)`:**
- Starts from the `root`.
- For each `character` in the `word`, it checks if a child `node` for that `character` exists. If not, it creates a new `TrieNode`.
- Moves to the child `node`.
- Once all `characters` are processed, it sets the `is_end_of_word` flag of the final `node` to true.

    </li>
- **`search(word)`:**
- Traverses the `Trie` similar to `insert`.
- If any `character` path doesn't exist, returns false.
- If the end of the `word` is reached, returns the `is_end_of_word` flag of the current `node`.

    </li>
- **`startsWith(prefix)`:** Similar to `search`, but only checks if the `prefix` path exists, without checking the `is_end_of_word` flag.
- **`autocomplete(prefix)`:**
- Finds the `node` corresponding to the given `prefix`.
- Performs a recursive helper function (`_collectAllWords`) starting from that `node` to gather all `words` that extend the `prefix`. This is essentially a `DFS` traversal from the `prefix node`.

    </li>

[Back to Implementation](#implementation)

## Applications

### Application

Tries are the standard data structure for any application that involves processing prefixes of strings. Their most common use case is in implementing **autocomplete** features in search engines, code editors, and mobile keyboards. They are also used in **spell checkers** to efficiently suggest corrections for misspelled words. In networking, Tries are used to store **IP routing tables**, where the longest prefix match algorithm can be implemented efficiently to find the best route for a given IP address.

