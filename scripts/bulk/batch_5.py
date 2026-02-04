batch = """
<a name="q161"></a>
### 161) How many objects will be created? (String s1 = "abc"; String s2 = "abc";)
[Back to TOC](#q161-toc)

**Answer:**
**Only one object.** Both `s1` and `s2` will point to the same "abc" object in the **String Constant Pool**.

---

<a name="q162"></a>
### 162) How to create mutable string objects?
[Back to TOC](#q162-toc)

**Answer:**
Use **`StringBuilder`** (preferred) or **`StringBuffer`** (if thread-safety is required).
```java
StringBuilder sb = new StringBuilder("Java");
sb.append(" 21");
System.out.println(sb.toString()); // Java 21
```

---

<a name="q163"></a>
### 163) "==" vs equals() for Strings?
[Back to TOC](#q163-toc)

**Answer:**
- **`==`**: Compares the **reference** (memory address).
- **`equals()`**: Compares the **content** (actual text).
*Always use `equals()` for string comparison.*

---

<a name="q164"></a>
### 164) Which class for mutable and thread-safe string objects?
[Back to TOC](#q164-toc)

**Answer:**
**`StringBuffer`**. Its methods are synchronized, making it thread-safe.

---

<a name="q165"></a>
### 165) Convert String to char array?
[Back to TOC](#q165-toc)

**Answer:**
Use **`str.toCharArray()`**.

---

<a name="q166"></a>
### 166) How many objects created? (String s1 = new String("abc"); String s2 = "abc";)
[Back to TOC](#q166-toc)

**Answer:**
**Two objects.**
1.  The string literal "abc" is created in the **String Pool**.
2.  The `new String("abc")` creates a separate object in the **Heap**.
*Note:* `s1 == s2` would be `false`.

---

<a name="q167"></a>
### 167) Where is the String Constant Pool located?
[Back to TOC](#q167-toc)

**Answer:**
Inside the **Heap** memory (since Java 7).

---

<a name="q168"></a>
### 168) Best class for high-performance, thread-safe string manipulation?
[Back to TOC](#q168-toc)

**Answer:**
**`StringBuffer`**. While `StringBuilder` is faster, it's not thread-safe. If you need thread-safety, `StringBuffer` is the standard choice.

---

<a name="q169"></a>
### 169) What is String intern?
[Back to TOC](#q169-toc)

**Answer:**
The **`intern()`** method checks the String Pool. If the string already exists, it returns the pooled reference. If not, it adds the string to the pool and returns that reference.
```java
String s1 = new String("abc").intern();
String s2 = "abc";
System.out.println(s1 == s2); // true!
```

---

<a name="q170"></a>
### 170) Java Strings vs C/C++ Strings?
[Back to TOC](#q170-toc)

**Answer:**
- **Java:** Strings are **Objects**, not null-terminated, and are immutable.
- **C/C++:** Strings are **Character Arrays** ending with a null character (`\\0`).

---

<a name="q171"></a>
### 171) How many objects created? (String s1 = new String("abc"); String s2 = new String("abc");)
[Back to TOC](#q171-toc)

**Answer:**
**Three objects.** One in the Pool ("abc") and two separate objects in the Heap.

---

<a name="q172"></a>
### 172) Can we call String methods on literals?
[Back to TOC](#q172-toc)

**Answer:**
**Yes.** Literals are objects. E.g., `"hello".toUpperCase()`.

---

<a name="q173"></a>
### 173) Why are Strings immutable in Java?
[Back to TOC](#q173-toc)

**Answer:**
1.  **String Pool:** Makes memory optimization possible.
2.  **Security:** Strings are used for passwords, network connections, etc. If they were mutable, they could be changed maliciously.
3.  **Thread Safety:** Immutable objects are inherently thread-safe.
4.  **Hashing:** Hashcode can be cached safely (critical for `HashMap` performance).

---

<a name="q174"></a>
### 174) Why use a String Pool?
[Back to TOC](#q174-toc)

**Answer:**
**Memory Efficiency.** Most programs use many duplicate strings. Storing them only once saves a significant amount of RAM.

---

<a name="q175"></a>
### 175) Similarity and difference between String and StringBuffer?
[Back to TOC](#q175-toc)

**Answer:**
- **Similarity:** Both represent character sequences and are final classes.
- **Difference:** String is immutable; StringBuffer is mutable and thread-safe.

---

<a name="q176"></a>
### 176) Similarity and difference between StringBuffer and StringBuilder?
[Back to TOC](#q176-toc)

**Answer:**
- **Similarity:** Both are mutable and have the same API.
- **Difference:** StringBuffer is synchronized (thread-safe); StringBuilder is not (faster).

---

<a name="q177"></a>
### 177) How to count occurrences of each character in a string?
[Back to TOC](#q177-toc)

**Answer:**
Use a **`HashMap<Character, Integer>`**.
```java
Map<Character, Integer> counts = new HashMap<>();
for (char c : str.toCharArray()) {
    counts.put(c, counts.getOrDefault(c, 0) + 1);
}
```

---

<a name="q178"></a>
### 178) How to remove all white spaces?
[Back to TOC](#q178-toc)

**Answer:**
Use **`str.replaceAll("\\\\s", "")`**.

---

<a name="q179"></a>
### 179) Find duplicate characters?
[Back to TOC](#q179-toc)

**Answer:**
Similar to counting occurrences, but only print characters with a count > 1.

---

<a name="q180"></a>
### 180) Java program to reverse a string?
[Back to TOC](#q180-toc)

**Answer:**
```java
String reversed = new StringBuilder(str).reverse().toString();
```

---

<a name="q181"></a>
### 181) Check if two strings are anagrams?
[Back to TOC](#q181-toc)

**Answer:**
Convert to `char[]`, sort them, and check `Arrays.equals()`.
```java
char[] a1 = s1.toCharArray();
char[] a2 = s2.toCharArray();
Arrays.sort(a1);
Arrays.sort(a2);
boolean isAnagram = Arrays.equals(a1, a2);
```

---

<a name="q182"></a>
### 182) Reverse string while preserving space positions?
[Back to TOC](#q182-toc)

**Answer:**
1.  Mark space positions.
2.  Reverse the rest of the characters.
3.  Insert spaces back at original positions.

---

<a name="q183"></a>
### 183) String to Integer and Integer to String?
[Back to TOC](#q183-toc)

**Answer:**
- **String to Int:** `Integer.parseInt(str)`
- **Int to String:** `String.valueOf(num)` or `Integer.toString(num)`

---

<a name="q184"></a>
### 184) Prove that Strings are immutable?
[Back to TOC](#q184-toc)

**Answer:**
```java
String s1 = "Java";
s1.concat(" 21");
System.out.println(s1); // Still prints "Java"
```

---

<a name="q185"></a>
### 185) Check if one string is a rotation of another?
[Back to TOC](#q185-toc)

**Answer:**
If lengths are equal, check if `(s1 + s1).contains(s2)`.
```java
String s1 = "ABCD";
String s2 = "CDAB";
boolean isRotation = (s1.length() == s2.length()) && (s1 + s1).contains(s2);
```

---

<a name="q186"></a>
### 186) Reverse each word of a string?
[Back to TOC](#q186-toc)

**Answer:**
Split by spaces, reverse each word, and join them back.
*Modern Context:* Use **`Collectors.joining(" ")`** with Streams.

---

<a name="q187"></a>
### 187) Print all substrings?
[Back to TOC](#q187-toc)

**Answer:**
Use nested loops: outer for start index, inner for end index.

---

<a name="q188"></a>
### 188) Common characters in alphabetical order?
[Back to TOC](#188-toc)

**Answer:**
Use two `Sets` of characters, find the intersection, and sort.

---

<a name="q189"></a>
### 189) Maximum occurring character?
[Back to TOC](#189-toc)

**Answer:**
Use a frequency map (HashMap) and find the entry with the max value.

---

<a name="q190"></a>
### 190) StringJoiner vs String.join() vs Collectors.joining()?
[Back to TOC](#190-toc)

**Answer:**
- **`StringJoiner`**: A low-level utility class for joining strings with delimiters.
- **`String.join()`**: A static helper method for simple joining.
- **`Collectors.joining()`**: The standard way to join elements in a **Stream**.

---

<a name="q191"></a>
### 191) Reverse a sentence word by word?
[Back to TOC](#191-toc)

**Answer:**
Split by space, reverse the array, and join back.

---

<a name="q192"></a>
### 192) What is multithreaded programming?
[Back to TOC](#192-toc)

**Answer:**
Running multiple parts of a program (threads) concurrently to maximize CPU usage.
*Modern Context:* In **Java 21**, we can run millions of **Virtual Threads** on a single machine!
```java
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    executor.submit(() -> System.out.println("Modern Concurrency!"));
}
```

---

<a name="q193"></a>
### 193) Ways to create threads in Java?
[Back to TOC](#193-toc)

**Answer:**
1.  **Extend `Thread` class.**
2.  **Implement `Runnable` interface.**
3.  **Implement `Callable` interface** (for results).
4.  **Use `Thread.ofVirtual()` (Java 21).**

---

<a name="q194"></a>
### 194) User Threads vs Daemon Threads?
[Back to TOC](#194-toc)

**Answer:**
- **User Threads:** JVM waits for them to finish before exiting.
- **Daemon Threads:** Background tasks (e.g., GC). JVM exits even if they are still running.

---

<a name="q195"></a>
### 195) Default daemon status?
[Back to TOC](#195-toc)

**Answer:**
**False** (User thread).

---

<a name="q196"></a>
### 196) Convert user thread to daemon?
[Back to TOC](#196-toc)

**Answer:**
Use `t.setDaemon(true)` **before** calling `t.start()`.

---

<a name="q197"></a>
### 197) Give name to a thread?
[Back to TOC](#197-toc)

**Answer:**
Use `t.setName("MyThread")`. Default names are `Thread-0`, `Thread-1`, etc.

---

<a name="q198"></a>
### 198) Change name of main thread?
[Back to TOC](#198-toc)

**Answer:**
**Yes.** `Thread.currentThread().setName("NewName")`.

---

<a name="q199"></a>
### 199) Can two threads have the same name?
[Back to TOC](#199-toc)

**Answer:**
**Yes**, but it's not recommended as it makes debugging harder. Use **Thread ID** (`t.threadId()`) to identify them uniquely.

---

<a name="q200"></a>
### 200) MIN_PRIORITY, NORM_PRIORITY, MAX_PRIORITY?
[Back to TOC](#200-toc)

**Answer:**
- `MIN_PRIORITY`: 1
- `NORM_PRIORITY`: 5 (Default)
- `MAX_PRIORITY`: 10

---
"""
with open('ultimate-questions-cheatsheet/Java-Ultimate-Cheat-Sheet.md', 'a') as f:
    f.write(batch)
