batch = """
<a name="q241"></a>
### 241) Thread group of main thread?
[Back to TOC](#q241-toc)

**Answer:**
**"main"**.

---

<a name="q242"></a>
### 242) activeCount() and activeGroupCount()?
[Back to TOC](#q242-toc)

**Answer:**
- **`activeCount()`**: Returns an estimate of the number of active threads in the current thread's group and its subgroups.
- **`activeGroupCount()`**: Returns an estimate of the number of active groups in the current thread's group and its subgroups.

---

<a name="q243"></a>
### 243) Java 8-21: Object Oriented or Functional?
[Back to TOC](#q243-toc)

**Answer:**
**Both.** Java remains a strongly typed, Object-Oriented language, but since Java 8, it has adopted **Functional Programming** features (Lambdas, Streams, Optional) to make code more concise and readable.
*Modern Context:* In Java 21, features like **Record Patterns** and **Pattern Matching for Switch** further bridge the gap between OO and Functional styles.

---

<a name="q244"></a>
### 244) Three main features of Functional Programming in Java?
[Back to TOC](#q244-toc)

**Answer:**
1.  **Lambda Expressions.**
2.  **Functional Interfaces.**
3.  **Stream API.**

---

<a name="q245"></a>
### 245) What are Lambda Expressions?
[Back to TOC](#q245-toc)

**Answer:**
An anonymous function (a function without a name). It allows you to treat functionality as a method argument, or code as data.
```java
// Before Java 8
Runnable r1 = new Runnable() {
    @Override
    public void run() { System.out.println("Hello"); }
};

// With Lambda
Runnable r2 = () -> System.out.println("Hello");
```

---

<a name="q246"></a>
### 246) How is the signature of a Lambda determined?
[Back to TOC](#q246-toc)

**Answer:**
By the **Target Type**. The compiler looks at the single abstract method of the Functional Interface that the Lambda is being assigned to.

---

<a name="q247"></a>
### 247) How is the return type of a Lambda determined?
[Back to TOC](#q247-toc)

**Answer:**
From the context and the body of the Lambda. If the body has a single expression, its return type is used. If it's a block, the `return` statement's type is used.

---

<a name="q248"></a>
### 248) Use non-final local variables in a Lambda?
[Back to TOC](#q248-toc)

**Answer:**
**No.** Local variables must be **final** or **effectively final**. This is because Lambdas "capture" variables, and allowing them to change would lead to thread-safety issues.

---

<a name="q249"></a>
### 249) Advantages of Lambdas?
[Back to TOC](#q249-toc)

**Answer:**
1.  Reduced boilerplate code.
2.  Improved readability.
3.  Enables parallel processing (via Streams).
4.  Easier API usage (e.g., `forEach`, `removeIf`).

---

<a name="q250"></a>
### 250) What are Functional Interfaces?
[Back to TOC](#q250-toc)

**Answer:**
An interface with **exactly one abstract method**.
*Examples:* `Runnable`, `Callable`, `Comparator`.
*Modern Context:* Use the **`@FunctionalInterface`** annotation to let the compiler enforce this rule.

---

<a name="q251"></a>
### 251) New Functional Interfaces in Java 8+?
[Back to TOC](#q251-toc)

**Answer:**
Located in **`java.util.function`**:
1.  **`Predicate<T>`**: Takes T, returns boolean (`test()`).
2.  **`Function<T, R>`**: Takes T, returns R (`apply()`).
3.  **`Consumer<T>`**: Takes T, returns nothing (`accept()`).
4.  **`Supplier<T>`**: Takes nothing, returns T (`get()`).

---

<a name="q252"></a>
### 252) Predicate vs BiPredicate?
[Back to TOC](#q252-toc)

**Answer:**
- `Predicate<T>`: One argument.
- `BiPredicate<T, U>`: Two arguments.

---

<a name="q253"></a>
### 253) Function vs BiFunction?
[Back to TOC](#q253-toc)

**Answer:**
- `Function<T, R>`: One input, one output.
- `BiFunction<T, U, R>`: Two inputs, one output.

---

<a name="q254"></a>
### 254) Interface for operation on object that returns nothing?
[Back to TOC](#q254-toc)

**Answer:**
**`Consumer<T>`**.

---

<a name="q255"></a>
### 255) Interface for creating new objects?
[Back to TOC](#q255-toc)

**Answer:**
**`Supplier<T>`**.

---

<a name="q256"></a>
### 256) UnaryOperator and BinaryOperator?
[Back to TOC](#q256-toc)

**Answer:**
Special cases of Function where the input and output types are the **same**.
- `UnaryOperator<T>`: One input T, returns T.
- `BinaryOperator<T>`: Two inputs T, returns T.

---

<a name="q257"></a>
### 257) Primitive Functional Interfaces?
[Back to TOC](#q257-toc)

**Answer:**
Yes, like **`IntPredicate`**, **`LongConsumer`**, **`DoubleFunction`**. They exist to **avoid the performance cost of Auto-boxing/Unboxing**.

---

<a name="q258"></a>
### 258) Lambdas and Functional Interfaces relationship?
[Back to TOC](#q258-toc)

**Answer:**
A Lambda expression provides the **implementation** for the single abstract method of a Functional Interface.

---

<a name="q259"></a>
### 259) What are Method References?
[Back to TOC](#q259-toc)

**Answer:**
A shorthand for Lambdas that only call an existing method.
```java
// Lambda
list.forEach(s -> System.out.println(s));

// Method Reference
list.forEach(System.out::println);
```

---

<a name="q260"></a>
### 260) Method Reference syntax types?
[Back to TOC](#q260-toc)

**Answer:**
1.  `StaticMethod`: `ClassName::staticMethodName`
2.  `InstanceMethod`: `instance::methodName`
3.  `ArbitraryObject`: `ClassName::methodName`
4.  `Constructor`: `ClassName::new`

---

<a name="q261"></a>
### 261) Major changes to interfaces in Java 8+?
[Back to TOC](#q261-toc)

**Answer:**
1.  **Default methods.**
2.  **Static methods.**
3.  **Private methods (Java 9+).**

---

<a name="q262"></a>
### 262) What are Default Methods?
[Back to TOC](#q262-toc)

**Answer:**
Methods in an interface that have a body. They allow you to add new functionality to interfaces without breaking existing implementations.

---

<a name="q263"></a>
### 263) Solving the Diamond Problem with default methods?
[Back to TOC](#q263-toc)

**Answer:**
If a class inherits two default methods with the same signature, the compiler forces you to **override** the method and manually specify which one to use.
```java
@Override
public void myMethod() {
    InterfaceA.super.myMethod();
}
```

---

<a name="q264"></a>
### 264) Static methods in interfaces?
[Back to TOC](#q264-toc)

**Answer:**
They are used for utility methods related to the interface. They are not inherited by implementing classes.

---

<a name="q265"></a>
### 265) What are Streams?
[Back to TOC](#q265-toc)

**Answer:**
A sequence of elements supporting functional-style operations. It is **not** a data structure; it processes data from a source (Collection, Array, I/O).
```java
// Modern Stream Example (Java 16+)
List<String> result = list.stream()
    .filter(s -> s.startsWith("A"))
    .map(String::toUpperCase)
    .toList(); // Shorthand for collect(Collectors.toList())
```

---

<a name="q266"></a>
### 266) Is Stream a data structure?
[Back to TOC](#q266-toc)

**Answer:**
**No.** Streams do not store data. They only convey data from a source through a pipeline of computational steps.

---

<a name="q267"></a>
### 267) Intermediate vs Terminal operations?
[Back to TOC](#q267-toc)

**Answer:**
- **Intermediate:** Returns a new Stream (Lazy). E.g., `filter()`, `map()`, `sorted()`.
- **Terminal:** Produces a result or side-effect. E.g., `collect()`, `forEach()`, `count()`.

---

<a name="q268"></a>
### 268) What is a Pipeline of operations?
[Back to TOC](#q268-toc)

**Answer:**
A sequence of one source, zero or more intermediate operations, and one terminal operation.

---

<a name="q269"></a>
### 269) "Implicit iteration" in Streams?
[Back to TOC](#q269-toc)

**Answer:**
In a `for` loop, you manage the iteration (External). In a Stream, the API manages the iteration for you (Internal), allowing for optimizations like parallel processing.

---

<a name="q270"></a>
### 270) Lazy Loading in Streams?
[Back to TOC](#q270-toc)

**Answer:**
Intermediate operations are not performed until the **terminal operation** is invoked. This allows for "short-circuiting" (e.g., finding the first element without checking the whole list).

---

<a name="q271"></a>
### 271) Short-circuiting operations?
[Back to TOC](#q271-toc)

**Answer:**
Operations that don't need to process the whole stream to produce a result.
- **Intermediate:** `limit()`.
- **Terminal:** `findFirst()`, `anyMatch()`.

---

<a name="q272"></a>
### 272) Selection operations?
[Back to TOC](#q272-toc)

**Answer:**
`filter()`, `distinct()`, `limit()`, `skip()`.

---

<a name="q273"></a>
### 273) Sorting operations?
[Back to TOC](#q273-toc)

**Answer:**
`sorted()` (natural order) or `sorted(Comparator)`.

---

<a name="q274"></a>
### 274) Reducing operations?
[Back to TOC](#q274-toc)

**Answer:**
Operations that combine elements into a single value.
`reduce()`, `collect()`, `count()`, `sum()`, `max()`, `min()`.

---

<a name="q275"></a>
### 275) Matching operations?
[Back to TOC](#q275-toc)

**Answer:**
`anyMatch()`, `allMatch()`, `noneMatch()`.

---

<a name="q276"></a>
### 276) Finding operations?
[Back to TOC](#q276-toc)

**Answer:**
`findFirst()`, `findAny()`.

---

<a name="q277"></a>
### 277) Mapping operations?
[Back to TOC](#q277-toc)

**Answer:**
`map()`, `flatMap()`, `mapToInt()`, `mapToLong()`, `mapToDouble()`.

---

<a name="q278"></a>
### 278) map() vs flatMap()?
[Back to TOC](#q278-toc)

**Answer:**
- **`map()`**: Transforms one element into another (One-to-One).
- **`flatMap()`**: Transforms one element into a stream and flattens it (One-to-Many). Used to handle "nested" collections.

---

<a name="q279"></a>
### 279) limit() vs skip()?
[Back to TOC](#q279-toc)

**Answer:**
- `limit(n)`: Takes the first `n` elements.
- `skip(n)`: Discards the first `n` elements.

---

<a name="q280"></a>
### 280) findFirst() vs findAny()?
[Back to TOC](#280-toc)

**Answer:**
- `findFirst()`: Always returns the first element in the source order.
- `findAny()`: Returns any element (more efficient in parallel streams).

---
"""
with open('ultimate-questions-cheatsheet/Java-Ultimate-Cheat-Sheet.md', 'a') as f:
    f.write(batch)
