batch = """
<a name="q321"></a>
### 321) Clean up operations in finally block?
[Back to TOC](#q321-toc)

**Answer:**
Because the `finally` block is guaranteed to execute, it's the perfect place to close database connections, files, or network sockets to prevent resource leaks.
*Modern Context:* Use **Try-with-resources** for classes that implement `AutoCloseable`.

---

<a name="q322"></a>
### 322) final vs finally vs finalize?
[Back to TOC](#q322-toc)

**Answer:**
- **`final`**: Modifier (constant variable, non-overridable method, non-inheritable class).
- **`finally`**: Block in exception handling (guaranteed execution).
- **`finalize()`**: Method called by Garbage Collector before destroying an object (Deprecated since Java 9, **Do not use!**).

---

<a name="q323"></a>
### 323) Create customized exceptions?
[Back to TOC](#q323-toc)

**Answer:**
Extend the `Exception` class (for checked) or `RuntimeException` class (for unchecked).
```java
public class MyException extends Exception {
    public MyException(String message) { super(message); }
}
```

---

<a name="q324"></a>
### 324) ClassCastException?
[Back to TOC](#324-toc)

**Answer:**
Thrown when you try to cast an object to a subclass of which it is not an instance.

---

<a name="q325"></a>
### 325) throw vs throws vs throwable?
[Back to TOC](#325-toc)

**Answer:**
- **`throw`**: Keyword used to manually throw an exception.
- **`throws`**: Keyword used in method signature to declare potential exceptions.
- **`Throwable`**: The root class for all Errors and Exceptions.

---

<a name="q326"></a>
### 326) StackOverflowError?
[Back to TOC](#326-toc)

**Answer:**
Thrown when the stack memory is full, usually due to **infinite recursion**.

---

<a name="q327"></a>
### 327) Override method with broader checked exception?
[Back to TOC](#327-toc)

**Answer:**
**No.** Subclasses cannot throw broader checked exceptions than their parents.

---

<a name="q328"></a>
### 328) Chained Exceptions?
[Back to TOC](#328-toc)

**Answer:**
Relating one exception to another. E.g., catching a low-level exception and throwing a high-level one while preserving the original "cause".
```java
try {
    // some code
} catch (IOException e) {
    throw new MyException("High level error", e); // 'e' is the cause
}
```

---

<a name="q329"></a>
### 329) Superclass for all Errors and Exceptions?
[Back to TOC](#329-toc)

**Answer:**
**`java.lang.Throwable`**.

---

<a name="q330"></a>
### 330) Legal combinations of try-catch-finally?
[Back to TOC](#330-toc)

**Answer:**
1.  `try-catch`
2.  `try-catch-finally`
3.  `try-finally`

---

<a name="q331"></a>
### 331) Use of printStackTrace()?
[Back to TOC](#331-toc)

**Answer:**
Prints the exception name, description, and the sequence of method calls (stack trace) that led to the exception. Extremely useful for debugging.

---

<a name="q332"></a>
### 332) Checked Exceptions examples?
[Back to TOC](#332-toc)

**Answer:**
`IOException`, `SQLException`, `ClassNotFoundException`, `FileNotFoundException`.

---

<a name="q333"></a>
### 333) Unchecked Exceptions examples?
[Back to TOC](#333-toc)

**Answer:**
`NullPointerException`, `ArithmeticException`, `NumberFormatException`, `ArrayIndexOutOfBoundsException`.

---

<a name="q334"></a>
### 334) Try-with-resources?
[Back to TOC](#334-toc)

**Answer:**
Introduced in Java 7, it's a `try` block that automatically closes resources at the end. The resources must implement **`AutoCloseable`**.
```java
try (BufferedReader br = new BufferedReader(new FileReader("file.txt"))) {
    System.out.println(br.readLine());
} catch (IOException e) {
    e.printStackTrace();
} // br is automatically closed here!
```

---

<a name="q335"></a>
### 335) Benefits of try-with-resources?
[Back to TOC](#335-toc)

**Answer:**
1.  Cleaner code (no explicit `close()` in `finally`).
2.  Prevents memory leaks.
3.  Handles "suppressed" exceptions correctly.

---

<a name="q336"></a>
### 336) Changes to exception handling in Java 7?
[Back to TOC](#336-toc)

**Answer:**
1.  **Try-with-resources**.
2.  **Multi-catch block** (`catch (IOException | SQLException e)`).

---

<a name="q337"></a>
### 337) Java 9 improvements to try-with-resources?
[Back to TOC](#337-toc)

**Answer:**
You can use **effectively final** variables in the try-with-resources statement without re-declaring them.
```java
BufferedReader br = new BufferedReader(...);
try (br) { // Valid in Java 9+
    // use br
}
```

---

<a name="q338"></a>
### 338) Java Collection Framework?
[Back to TOC](#338-toc)

**Answer:**
A set of classes and interfaces that implement commonly used data structures (Lists, Sets, Maps) to store and manipulate groups of objects efficiently.

---

<a name="q339"></a>
### 339) Root interface of Collection Framework?
[Back to TOC](#339-toc)

**Answer:**
**`java.util.Collection`**. (Note: `Iterable` is the super-interface of `Collection`).

---

<a name="q340"></a>
### 340) Four main core interfaces of Collection Framework?
[Back to TOC](#340-toc)

**Answer:**
1.  **List**
2.  **Set**
3.  **Queue**
4.  **Map** (Map doesn't extend Collection, but is part of the framework).

---

<a name="q341"></a>
### 341) Collection Framework Hierarchy?
[Back to TOC](#341-toc)

**Answer:**
- `Collection`
  - `List` (ArrayList, LinkedList, Vector, Stack)
  - `Set` (HashSet, LinkedHashSet, TreeSet)
  - `Queue` (PriorityQueue, Deque -> ArrayDeque)
- `Map` (HashMap, LinkedHashMap, TreeMap, Hashtable)

---

<a name="q342"></a>
### 342) Why Map doesn't extend Collection?
[Back to TOC](#342-toc)

**Answer:**
Because they are fundamentally different. `Collection` stores single elements, while `Map` stores **Key-Value pairs**.

---

<a name="q343"></a>
### 343) What is Iterable interface?
[Back to TOC](#343-toc)

**Answer:**
The root interface of the whole hierarchy. Any class implementing `Iterable` can be used in an **enhanced for-loop**.

---

<a name="q344"></a>
### 344) Characteristics of List?
[Back to TOC](#344-toc)

**Answer:**
1.  **Ordered** (maintains insertion order).
2.  **Allows Duplicates**.
3.  **Index-based** access.

---

<a name="q345"></a>
### 345) Major implementations of List?
[Back to TOC](#345-toc)

**Answer:**
`ArrayList`, `LinkedList`, `Vector`.

---

<a name="q346"></a>
### 346) Characteristics of ArrayList?
[Back to TOC](#346-toc)

**Answer:**
1.  Resizable array.
2.  Fast random access ($O(1)$).
3.  Slow insertion/deletion in the middle ($O(n)$) because of element shifting.

---

<a name="q347"></a>
### 347) Three marker interfaces in ArrayList?
[Back to TOC](#347-toc)

**Answer:**
1.  `RandomAccess`
2.  `Serializable`
3.  `Cloneable`

---

<a name="q348"></a>
### 348) Default initial capacity of ArrayList?
[Back to TOC](#348-toc)

**Answer:**
**10**.

---

<a name="q349"></a>
### 349) Main drawback of ArrayList?
[Back to TOC](#349-toc)

**Answer:**
**Shifting.** Adding or removing an element from the middle requires shifting all subsequent elements, which is slow for large lists.

---

<a name="q350"></a>
### 350) Array vs ArrayList?
[Back to TOC](#350-toc)

**Answer:**
| Feature | Array | ArrayList |
| :--- | :--- | :--- |
| **Size** | Fixed | Dynamic |
| **Type** | Primitive & Object | Object only |
| **Methods** | `length` field | Rich API (`add`, `remove`, `sort`) |

---

<a name="q351"></a>
### 351) Vector vs ArrayList?
[Back to TOC](#351-toc)

**Answer:**
- **Vector:** Synchronized (Thread-safe, but slower).
- **ArrayList:** Not synchronized (Faster).

---

<a name="q352"></a>
### 352) Why avoid Vector?
[Back to TOC](#352-toc)

**Answer:**
Because it synchronizes every operation even if only one thread is using it, leading to poor performance.

---

<a name="q353"></a>
### 353) Growth of Vector vs ArrayList?
[Back to TOC](#353-toc)

**Answer:**
- **Vector:** Doubles its size (100% growth).
- **ArrayList:** Increases by 50%.

---

<a name="q354"></a>
### 354) Characteristics of Queue?
[Back to TOC](#354-toc)

**Answer:**
**FIFO** (First-In, First-Out). Elements are added at the tail and removed from the head.

---

<a name="q355"></a>
### 355) Important methods of Queue?
[Back to TOC](#355-toc)

**Answer:**
- **Insert:** `add()`, `offer()`
- **Remove:** `remove()`, `poll()`
- **Examine:** `element()`, `peek()`

---

<a name="q356"></a>
### 356) Queue vs List?
[Back to TOC](#356-toc)

**Answer:**
Lists allow random access. Queues typically only allow access to the head/tail elements.

---

<a name="q357"></a>
### 357) Popular type implementing both List and Queue?
[Back to TOC](#357-toc)

**Answer:**
**`LinkedList`**.

---

<a name="q358"></a>
### 358) Characteristics of LinkedList?
[Back to TOC](#358-toc)

**Answer:**
1.  Doubly-linked list.
2.  Fast insertion/deletion ($O(1)$) as no shifting is needed.
3.  Slow random access ($O(n)$) because you must traverse from the start/end.

---

<a name="q359"></a>
### 359) ArrayList vs LinkedList?
[Back to TOC](#359-toc)

**Answer:**
- **Search:** ArrayList is faster ($O(1)$ vs $O(n)$).
- **Update/Delete:** LinkedList is faster ($O(1)$ vs $O(n)$) once the position is found.

---

<a name="q360"></a>
### 360) What is PriorityQueue?
[Back to TOC](#360-toc)

**Answer:**
A queue where elements are ordered by their **priority** (either natural order or a custom `Comparator`), not their insertion time.

---
"""
with open('ultimate-questions-cheatsheet/Java-Ultimate-Cheat-Sheet.md', 'a') as f:
    f.write(batch)
