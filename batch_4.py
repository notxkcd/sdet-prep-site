batch = """
<a name="q121"></a>
### 121) What is the use of final class?
[Back to TOC](#q121-toc)

**Answer:**
To prevent inheritance. 
**Common Examples:** `String`, `Integer`, and all other wrapper classes are `final` for security and immutability reasons.
*Modern Context:* Use **`sealed` classes** (Java 17+) if you want to allow *some* classes to extend yours but not others.

---

<a name="q122"></a>
### 122) Can we change the value of an interface field?
[Back to TOC](#q122-toc)

**Answer:**
**No.** All fields in an interface are implicitly **`public static final`** (constants).

---

<a name="q123"></a>
### 123) Where can you initialize a final non-static global variable?
[Back to TOC](#q123-toc)

**Answer:**
1.  At the time of **declaration**.
2.  In an **Instance Initializer block**.
3.  In **every constructor** of the class.

---

<a name="q124"></a>
### 124) Definition of final class, method, and variable?
[Back to TOC](#q124-toc)

**Answer:**
- **Final Class:** Cannot be subclassed.
- **Final Method:** Cannot be overridden.
- **Final Variable:** Becomes a constant (value cannot be changed after initialization).

---

<a name="q125"></a>
### 125) Where can you initialize a final static global variable?
[Back to TOC](#q125-toc)

**Answer:**
1.  At the time of **declaration**.
2.  In a **Static Initializer block**.

---

<a name="q126"></a>
### 126) Can we declare constructors as final?
[Back to TOC](#q126-toc)

**Answer:**
**No.** Constructors are never inherited, so `final` would be meaningless.

---

<a name="q127"></a>
### 127) What is ArrayStoreException?
[Back to TOC](#q127-toc)

**Answer:**
A runtime exception thrown when you try to store an object of the wrong type in an array of objects.
```java
Object[] x = new String[3];
x[0] = 10; // Throws ArrayStoreException (trying to put Integer in String array)
```

---

<a name="q128"></a>
### 128) Can you pass a negative number as an array size?
[Back to TOC](#128-toc)

**Answer:**
**No.** It will compile, but throw a **`NegativeArraySizeException`** at runtime.

---

<a name="q129"></a>
### 129) Can you change the size of an array once created?
[Back to TOC](#129-toc)

**Answer:**
**No.** Arrays are fixed-size. If you need a dynamic size, use **`ArrayList`**.

---

<a name="q130"></a>
### 130) What is an anonymous array?
[Back to TOC](#130-toc)

**Answer:**
An array created without a name (reference). It's usually passed directly to a method.
```java
printArray(new int[]{1, 2, 3}); // Anonymous array
```

---

<a name="q131"></a>
### 131) Difference between int[] a and int a[]?
[Back to TOC](#131-toc)

**Answer:**
- `int[] a`: Preferred. Clearly shows that the type is "integer array".
- `int a[]`: Supported for C/C++ compatibility.

---

<a name="q132"></a>
### 132) Can you assign an array of 100 elements to an array of 10 elements?
[Back to TOC](#132-toc)

**Answer:**
**Yes.** You are just changing the reference. The array variable that held 10 elements will now point to the array with 100 elements.

---

<a name="q133"></a>
### 133) Is "int a[] = new int[3]{1, 2, 3}" legal?
[Back to TOC](#133-toc)

**Answer:**
**No.** If you provide the values `{1, 2, 3}`, you must NOT specify the size `[3]`.
Correct: `int a[] = new int[]{1, 2, 3};` or just `int a[] = {1, 2, 3};`

---

<a name="q134"></a>
### 134) Difference between Array and ArrayList?
[Back to TOC](#134-toc)

**Answer:**
| Feature | Array | ArrayList |
| :--- | :--- | :--- |
| **Size** | Fixed | Dynamic |
| **Type** | Primitives & Objects | Objects Only (uses Wrappers) |
| **Performance** | Faster | Slightly slower |
| **Methods** | `length` field | Rich API (`add`, `remove`, `sort`) |

---

<a name="q135"></a>
### 135) Ways to copy an array?
[Back to TOC](#135-toc)

**Answer:**
1.  `System.arraycopy()` (Fastest - native).
2.  `Arrays.copyOf()`.
3.  `clone()`.
4.  Manual loop.

---

<a name="q136"></a>
### 136) What are jagged arrays?
[Back to TOC](#136-toc)

**Answer:**
Multi-dimensional arrays where the sub-arrays have different lengths.
```java
int[][] jagged = new int[2][];
jagged[0] = new int[3];
jagged[1] = new int[5];
```

---

<a name="q137"></a>
### 137) How to check equality of two arrays?
[Back to TOC](#137-toc)

**Answer:**
Use **`Arrays.equals(a, b)`**. For multi-dimensional arrays, use **`Arrays.deepEquals(a, b)`**.
*Note:* `a.equals(b)` or `a == b` only checks if they are the same reference.

---

<a name="q138"></a>
### 138) What is ArrayIndexOutOfBoundsException?
[Back to TOC](#138-toc)

**Answer:**
Thrown when you try to access an index that doesn't exist (e.g., index -1 or index >= length).

---

<a name="q139"></a>
### 139) How to sort an array?
[Back to TOC](#139-toc)

**Answer:**
Use **`Arrays.sort(arr)`**.

---

<a name="q140"></a>
### 140) How to find intersection of two arrays?
[Back to TOC](#140-toc)

**Answer:**
Convert them to **`Sets`** and use `retainAll()`.
```java
Set<Integer> s1 = new HashSet<>(Arrays.asList(arr1));
Set<Integer> s2 = new HashSet<>(Arrays.asList(arr2));
s1.retainAll(s2); // s1 now contains only the intersection
```

---

<a name="q141"></a>
### 141) Ways to declare multidimensional arrays?
[Back to TOC](#141-toc)

**Answer:**
- `int[][] a;`
- `int a[][];`
- `int[] a[];`

---

<a name="q142"></a>
### 142) Can you specify dimension after an empty dimension? (e.g., new int[][5])
[Back to TOC](#142-toc)

**Answer:**
**No.** You must specify the high-level dimensions first. `new int[5][]` is valid; `new int[][5]` is not.

---

<a name="q143"></a>
### 143) How to search an element in an array?
[Back to TOC](#143-toc)

**Answer:**
1.  **Linear Search** (loop through all).
2.  **Binary Search** (`Arrays.binarySearch(arr, key)`) - *requires sorted array*.

---

<a name="q144"></a>
### 144) Default values of array elements?
[Back to TOC](#144-toc)

**Answer:**
- Numbers: 0 / 0.0
- Booleans: `false`
- Objects: `null`

---

<a name="q145"></a>
### 145) How to find duplicates in an array?
[Back to TOC](#145-toc)

**Answer:**
Use a **`HashSet`**. While adding elements, if `add()` returns `false`, it's a duplicate.
```java
Set<Integer> set = new HashSet<>();
for (int i : arr) {
    if (!set.add(i)) { System.out.println("Duplicate: " + i); }
}
```

---

<a name="q146"></a>
### 146) Ways to iterate over an array?
[Back to TOC](#146-toc)

**Answer:**
1.  For loop.
2.  Enhanced for loop (`for(int i : arr)`).
3.  **Streams (Java 8+):** `Arrays.stream(arr).forEach(...)`.

---

<a name="q147"></a>
### 147) How to find second largest element?
[Back to TOC](#147-toc)

**Answer:**
Iterate once while keeping track of `largest` and `secondLargest`.
*Modern Approach:* `Arrays.stream(arr).boxed().sorted(Comparator.reverseOrder()).skip(1).findFirst();`

---

<a name="q148"></a>
### 148) Find all pairs whose sum is equal to a given number?
[Back to TOC](#148-toc)

**Answer:**
Use a **`HashSet`** to store seen numbers and check if `(target - current)` exists in the set.
```java
for (int i : arr) {
    int complement = target - i;
    if (set.contains(complement)) {
        System.out.println(i + " + " + complement);
    }
    set.add(i);
}
```

---

<a name="q149"></a>
### 149) Separate zeros from non-zeros?
[Back to TOC](#149-toc)

**Answer:**
Iterate through the array and move all non-zero elements to the front, then fill the rest with zeros.

---

<a name="q150"></a>
### 150) Find continuous sub array whose sum is equal to a number?
[Back to TOC](#150-toc)

**Answer:**
Use the **Sliding Window** technique.

---

<a name="q151"></a>
### 151) Drawbacks of arrays?
[Back to TOC](#151-toc)

**Answer:**
1.  **Fixed Size.**
2.  **Homogeneous:** Only stores one type of data.
3.  **Memory:** Allocates contiguous memory, which can lead to allocation failures even if total free memory is enough.

---

<a name="q152"></a>
### 152) Is String a keyword?
[Back to TOC](#152-toc)

**Answer:**
**No.** It's a class in the `java.lang` package.

---

<a name="q153"></a>
### 153) Is String primitive or derived?
[Back to TOC](#153-toc)

**Answer:**
**Derived** (Object).

---

<a name="q154"></a>
### 154) Ways to create String objects?
[Back to TOC](#154-toc)

**Answer:**
1.  **Literal:** `String s = "Hello";` (Uses String Pool).
2.  **`new` keyword:** `String s = new String("Hello");` (Always creates a new object in the heap).

---

<a name="q155"></a>
### 155) What is String Constant Pool?
[Back to TOC](#155-toc)

**Answer:**
A special memory area in the Heap where unique strings are stored. If you create a literal that already exists in the pool, Java just gives you the reference to the existing one.

---

<a name="q156"></a>
### 156) What is special about String objects?
[Back to TOC](#156-toc)

**Answer:**
**Immutability.** Once created, a String object cannot be changed. Any modification results in a *new* String object.

---

<a name="q157"></a>
### 157) Mutable vs Immutable objects?
[Back to TOC](#157-toc)

**Answer:**
- **Immutable:** State cannot be changed after creation (`String`, `Integer`, `LocalDate`).
- **Mutable:** State can be changed (`StringBuilder`, `ArrayList`).

---

<a name="q158"></a>
### 158) Which classes are final: String, StringBuffer, StringBuilder?
[Back to TOC](#158-toc)

**Answer:**
**All three** are `final`.

---

<a name="q159"></a>
### 159) Difference between String, StringBuffer, and StringBuilder?
[Back to TOC](#159-toc)

**Answer:**
| Feature | String | StringBuffer | StringBuilder |
| :--- | :--- | :--- | :--- |
| **Mutability** | Immutable | Mutable | Mutable |
| **Thread-Safe** | Yes | **Yes** (Synchronized) | **No** |
| **Performance** | Slow (for updates) | Medium | **Fastest** |

---

<a name="q160"></a>
### 160) Why StringBuffer/StringBuilder exist?
[Back to TOC](#160-toc)

**Answer:**
Because concatenating Strings in a loop creates thousands of garbage objects. `StringBuilder` uses a single buffer, making it much more efficient for heavy string manipulation.

---
"""
with open('ultimate-questions-cheatsheet/Java-Ultimate-Cheat-Sheet.md', 'a') as f:
    f.write(batch)
