batch = """
<a name="q361"></a>
### 361) What are Deque and ArrayDeque?
[Back to TOC](#q361-toc)

**Answer:**
- **`Deque`** (Double-Ended Queue): Allows insertion/removal from both ends (Stack & Queue combined).
- **`ArrayDeque`**: A resizable array implementation of `Deque`. It's faster than `Stack` (when used as a stack) and faster than `LinkedList` (when used as a queue).

---

<a name="q362"></a>
### 362) Characteristics of Sets?
[Back to TOC](#q362-toc)

**Answer:**
1.  **No Duplicates** allowed.
2.  **Unordered** (usually).
3.  Allows at most one `null` element (implementation-dependent).

---

<a name="q363"></a>
### 363) Major implementations of Set?
[Back to TOC](#q363-toc)

**Answer:**
`HashSet`, `LinkedHashSet`, `TreeSet`.

---

<a name="q364"></a>
### 364) List vs Set?
[Back to TOC](#q364-toc)

**Answer:**
| Feature | List | Set |
| :--- | :--- | :--- |
| **Duplicates** | Allowed. | Not allowed. |
| **Order** | Ordered (insertion order). | Unordered (usually). |
| **Indexing** | Index-based access. | No index-based access. |

---

<a name="q365"></a>
### 365) Characteristics of HashSet?
[Back to TOC](#q365-toc)

**Answer:**
1.  Backed by a **`HashMap`**.
2.  Unordered.
3.  Fastest Set implementation ($O(1)$ for add/contains).

---

<a name="q366"></a>
### 366) How HashSet works internally?
[Back to TOC](#q366-toc)

**Answer:**
It uses a `HashMap` where your elements are stored as **Keys**, and a constant dummy value (a private static `Object PRESENT`) is stored as the **Value**.

---

<a name="q367"></a>
### 367) Characteristics of LinkedHashSet?
[Back to TOC](#q367-toc)

**Answer:**
Maintains **Insertion Order** using a doubly-linked list running through the hash table.

---

<a name="q368"></a>
### 368) When to prefer LinkedHashSet?
[Back to TOC](#q368-toc)

**Answer:**
When you need unique elements but also need to preserve the order in which they were added.

---

<a name="q369"></a>
### 369) How LinkedHashSet works internally?
[Back to TOC](#q369-toc)

**Answer:**
It extends `HashSet` and uses a `LinkedHashMap` internally instead of a regular `HashMap`.

---

<a name="q370"></a>
### 370) What is SortedSet?
[Back to TOC](#q370-toc)

**Answer:**
A Set that maintains elements in sorted order (natural order or custom `Comparator`). Implementation: **`TreeSet`**.

---

<a name="q371"></a>
### 371) What is NavigableSet?
[Back to TOC](#q371-toc)

**Answer:**
An extension of `SortedSet` that provides navigation methods like `lower()`, `floor()`, `ceiling()`, and `higher()`. Implementation: **`TreeSet`**.

---

<a name="q372"></a>
### 372) Characteristics of TreeSet?
[Back to TOC](#372-toc)

**Answer:**
1.  Sorted order.
2.  Backed by a **Red-Black Tree**.
3.  Does not allow `null` (throws NPE).
4.  $O(log n)$ time for operations.

---

<a name="q373"></a>
### 373) HashSet vs LinkedHashSet vs TreeSet?
[Back to TOC](#373-toc)

**Answer:**
- **`HashSet`**: Fastest, no order.
- **`LinkedHashSet`**: Insertion order.
- **`TreeSet`**: Sorted order.

---

<a name="q374"></a>
### 374) Iterator vs ListIterator?
[Back to TOC](#374-toc)

**Answer:**
- **`Iterator`**: Forward traversal only. Works on any Collection.
- **`ListIterator`**: Bi-directional traversal. Works only on Lists. Allows modification during iteration.

---

<a name="q375"></a>
### 375) Map interface vs others?
[Back to TOC](#375-toc)

**Answer:**
Maps use **Key-Value pairs**. You access data via keys, not indexes. It does not extend the `Collection` interface.

---

<a name="q376"></a>
### 376) Popular implementations of Map?
[Back to TOC](#376-toc)

**Answer:**
`HashMap`, `LinkedHashMap`, `TreeMap`, `ConcurrentHashMap`, `Hashtable`.

---

<a name="q377"></a>
### 377) Characteristics of HashMap?
[Back to TOC](#377-toc)

**Answer:**
1.  Unordered.
2.  Allows one `null` key and multiple `null` values.
3.  Not synchronized (not thread-safe).
4.  $O(1)$ average time complexity.

---

<a name="q378"></a>
### 378) How HashMap works internally? (The "Million Dollar" Interview Question)
[Back to TOC](#378-toc)

**Answer:**
1.  **Array of Buckets:** Stores `Node<K,V>` objects.
2.  **`hashCode()`**: Finds the bucket index.
3.  **Collision Handling:** Multiple keys in one bucket form a **LinkedList**.
4.  **Treeification (Java 8+):** If a bucket exceeds 8 nodes, the LinkedList converts to a **Balanced Tree** (Red-Black Tree) for better performance ($O(log n)$ vs $O(n)$).
5.  **`equals()`**: Used to find the exact key within a bucket.

---

<a name="q379"></a>
### 379) What is Hashing?
[Back to TOC](#379-toc)

**Answer:**
The process of converting an object into an integer representation (hash code) using a formula. It's used to quickly locate objects in a collection.

---

<a name="q380"></a>
### 380) Initial capacity of HashMap?
[Back to TOC](#380-toc)

**Answer:**
**16**.

---

<a name="q381"></a>
### 381) Load factor of HashMap?
[Back to TOC](#381-toc)

**Answer:**
**0.75**. It means the map will resize (double) once it is 75% full.

---

<a name="q382"></a>
### 382) HashMap Threshold?
[Back to TOC](#382-toc)

**Answer:**
`Threshold = Capacity * Load Factor`. (e.g., $16 * 0.75 = 12$).

---

<a name="q383"></a>
### 383) What is rehashing?
[Back to TOC](#383-toc)

**Answer:**
When the map's size exceeds the threshold, it doubles the internal array size and recalculates the bucket index for all existing entries to redistribute them.

---

<a name="q384"></a>
### 384) Impact of capacity and load factor?
[Back to TOC](#384-toc)

**Answer:**
- **High capacity:** Reduces rehashing but wastes memory.
- **Low load factor:** Reduces collisions but increases rehashing.
- **Default (16, 0.75)**: Optimal balance for most use cases.

---

<a name="q385"></a>
### 385) HashSet vs HashMap?
[Back to TOC](#385-toc)

**Answer:**
- `HashSet`: Implements `Set`. Stores objects.
- `HashMap`: Implements `Map`. Stores Key-Value pairs. (HashSet uses HashMap internally).

---

<a name="q386"></a>
### 386) HashMap vs Hashtable?
[Back to TOC](#386-toc)

**Answer:**
| Feature | HashMap | Hashtable |
| :--- | :--- | :--- |
| **Sync** | Not synchronized. | Synchronized. |
| **Nulls** | Allows 1 null key. | No nulls allowed. |
| **Performance** | Faster. | Slower (legacy). |

---

<a name="q387"></a>
### 387) Remove duplicates from ArrayList?
[Back to TOC](#387-toc)

**Answer:**
Wrap it in a `LinkedHashSet` (to preserve order) and then back to a List.
```java
List<String> uniqueList = new ArrayList<>(new LinkedHashSet<>(originalList));
```

---

<a name="q388"></a>
### 388) Sorted collection with no duplicates?
[Back to TOC](#388-toc)

**Answer:**
**`TreeSet`**.

---

<a name="q389"></a>
### 389) Fail-fast vs Fail-safe Iterators?
[Back to TOC](#389-toc)

**Answer:**
- **Fail-fast:** Throws `ConcurrentModificationException` if collection is modified during iteration (e.g., `ArrayList`).
- **Fail-safe:** Operates on a **copy** of the collection, so modifications don't affect iteration (e.g., `CopyOnWriteArrayList`).

---

<a name="q390"></a>
### 390) Array to ArrayList and vice versa?
[Back to TOC](#390-toc)

**Answer:**
- **Array to List:** `Arrays.asList(arr)`
- **List to Array:** `list.toArray(new String[0])`

---

<a name="q391"></a>
### 391) Collection vs Collections?
[Back to TOC](#391-toc)

**Answer:**
- **`Collection`**: The root **interface**.
- **`Collections`**: A **utility class** with static methods (like `sort()`, `reverse()`).

---

<a name="q392"></a>
### 392) Collections vs Streams? (Repeated)
[Back to TOC](#392-toc)

**Answer:**
Storage vs. Processing. Collections are for managing data; Streams are for transforming data.

---

<a name="q393"></a>
### 393) HashMap to ArrayList?
[Back to TOC](#393-toc)

**Answer:**
```java
List<String> keys = new ArrayList<>(map.keySet());
List<String> values = new ArrayList<>(map.values());
```

---

<a name="q394"></a>
### 394) keySet(), values(), and entrySet()?
[Back to TOC](#394-toc)

**Answer:**
- `keySet()`: Returns all keys.
- `values()`: Returns all values.
- `entrySet()`: Returns a Set of Key-Value pairs (`Map.Entry`).

---

<a name="q395"></a>
### 395) Iterator vs Spliterator? (Repeated)
[Back to TOC](#395-toc)

**Answer:**
Sequential traversal vs. Parallel traversal.

---

<a name="q396"></a>
### 396) How to sort an ArrayList?
[Back to TOC](#396-toc)

**Answer:**
`Collections.sort(list)` or `list.sort(Comparator.naturalOrder())`.

---

<a name="q397"></a>
### 397) HashMap vs ConcurrentHashMap?
[Back to TOC](#397-toc)

**Answer:**
`ConcurrentHashMap` is thread-safe and highly performant because it uses **segment-level locking** (or bucket-level locking in modern versions) instead of locking the whole map.

---

<a name="q398"></a>
### 398) Make collections read-only?
[Back to TOC](#398-toc)

**Answer:**
`Collections.unmodifiableList(list)` or **`List.of(...)`** (Java 9+ immutable collection).

---

<a name="q399"></a>
### 399) Reverse an ArrayList?
[Back to TOC](#399-toc)

**Answer:**
`Collections.reverse(list)`.

---

<a name="q400"></a>
### 400) Synchronized HashMap vs Hashtable vs ConcurrentHashMap?
[Back to TOC](#400-toc)

**Answer:**
- **Hashtable**: Legacy, slow, locks whole map.
- **Sync Map**: Wrapper, slow, locks whole map.
- **ConcurrentHashMap**: Modern, fast, locks only parts of the map.

---

<a name="q401"></a>
### 401) Sort HashMap by keys?
[Back to TOC](#401-toc)

**Answer:**
Wrap it in a **`TreeMap`**.
`TreeMap<String, String> sortedMap = new TreeMap<>(unsortedMap);`

---

<a name="q402"></a>
### 402) Sort HashMap by values?
[Back to TOC](#402-toc)

**Answer:**
```java
List<Map.Entry<K, V>> list = new ArrayList<>(map.entrySet());
list.sort(Map.Entry.comparingByValue());
```

---

<a name="q403"></a>
### 403) Merge two maps?
[Back to TOC](#403-toc)

**Answer:**
`map1.putAll(map2)` or use **`map1.merge(...)`** for fine-grained control over collisions.

---

<a name="q404"></a>
### 404) Java 9 Immutable Collections?
[Back to TOC](#404-toc)

**Answer:**
`List.of()`, `Set.of()`, `Map.of()`. They are truly immutable (cannot be changed after creation) and more space-efficient than unmodifiable wrappers.

---

<a name="q405"></a>
### 405) Java 10 copyOf()?
[Back to TOC](#405-toc)

**Answer:**
`List.copyOf()`, `Set.copyOf()`, `Map.copyOf()`. They return an unmodifiable collection containing the elements of the original collection.

---

<a name="q406"></a>
### 406) Enumeration vs Iterator?
[Back to TOC](#406-toc)

**Answer:**
- **Enumeration**: Legacy (since 1.0), read-only.
- **Iterator**: Modern (since 1.2), allows element removal.

---

<a name="q407"></a>
### 407) RandomAccess implementations?
[Back to TOC](#407-toc)

**Answer:**
**`ArrayList`** and **`Vector`**. (LinkedList does NOT implement it).

---

<a name="q408"></a>
### Bonus: Sequenced Collections (Java 21 Feature)
[Back to TOC](#q1-toc)

**Answer:**
Java 21 finally added a common interface for collections with a defined order (List, Deque, SortedSet).
```java
var list = List.of("First", "Second", "Last");
System.out.println(list.getFirst()); // "First"
System.out.println(list.getLast());  // "Last"
```

---
"""
with open('ultimate-questions-cheatsheet/Java-Ultimate-Cheat-Sheet.md', 'a') as f:
    f.write(batch)
