batch = """
<a name="q281"></a>
### 281) Stream.collect(), Collector interface, and Collectors class?
[Back to TOC](#q281-toc)

**Answer:**
- **`collect()`**: The terminal operation that triggers the reduction process.
- **`Collector`**: The interface that defines the logic for how to accumulate elements into a result container.
- **`Collectors`**: A utility class providing implementations for common collection tasks (like `toList`, `toSet`, `groupingBy`).

---

<a name="q282"></a>
### 282) Five methods of Collectors class?
[Back to TOC](#q282-toc)

**Answer:**
1.  **`toList()`**: Accumulates elements into a List.
2.  **`toSet()`**: Accumulates into a Set.
3.  **`joining()`**: Concatenates elements into a String.
4.  **`groupingBy()`**: Groups elements based on a classifier function (similar to SQL `GROUP BY`).
5.  **`partitioningBy()`**: Partitions elements into two groups based on a Predicate.

---

<a name="q283"></a>
### 283) Collections vs Streams?
[Back to TOC](#q283-toc)

**Answer:**
| Feature | Collections | Streams |
| :--- | :--- | :--- |
| **Data** | Stores data. | Processes data. |
| **Iteration** | External (you control). | Internal (API controls). |
| **Usage** | Reusable. | Consumable (one-time use). |
| **Lazy** | Eagerly evaluated. | Lazily evaluated. |

---

<a name="q284"></a>
### 284) Purpose of Optional class?
[Back to TOC](#q284-toc)

**Answer:**
To provide a type-level solution for representing "no value" instead of using `null`. It helps **avoid NullPointerException**.
```java
// Modern usage
Optional<String> name = Optional.ofNullable(getName());
name.ifPresentOrElse(
    System.out::println, 
    () -> System.out.println("No name found")
);
```

---

<a name="q285"></a>
### 285) Spliterator vs Iterator?
[Back to TOC](#q285-toc)

**Answer:**
**`Spliterator`** ("Splitable Iterator") is designed for **parallel processing**. It can split a source into smaller parts that can be processed by different threads simultaneously.

---

<a name="q286"></a>
### 286) StringJoiner vs String.join() vs Collectors.joining()?
[Back to TOC](#q286-toc)

**Answer:**
- **`StringJoiner`**: A class for building a sequence of characters separated by a delimiter (and optional prefix/suffix).
- **`String.join()`**: A static method for joining arrays or Iterables.
- **`Collectors.joining()`**: Specifically for joining elements of a Stream.

---

<a name="q287"></a>
### 287) Three important classes of Java 8+ Date and Time API?
[Back to TOC](#q287-toc)

**Answer:**
Located in `java.time`:
1.  **`LocalDate`**: Date only (no time).
2.  **`LocalTime`**: Time only (no date).
3.  **`LocalDateTime`**: Both date and time.
*Note:* These are all **Immutable** and **Thread-safe**.

---

<a name="q288"></a>
### 288) Current date and time in Java 21?
[Back to TOC](#q288-toc)

**Answer:**
```java
LocalDateTime now = LocalDateTime.now();
System.out.println(now);
```

---

<a name="q289"></a>
### 289) Partition students based on percentage (> 60%)?
[Back to TOC](#q289-toc)

**Answer:**
```java
Map<Boolean, List<Student>> partitioned = students.stream()
    .collect(Collectors.partitioningBy(s -> s.getPercentage() > 60));
```

---

<a name="q290"></a>
### 290) Get names of top 3 students?
[Back to TOC](#q290-toc)

**Answer:**
```java
List<String> top3 = students.stream()
    .sorted(Comparator.comparingDouble(Student::getPercentage).reversed())
    .limit(3)
    .map(Student::getName)
    .toList();
```

---

<a name="q291"></a>
### 291) Get name and percentage of each student?
[Back to TOC](#q291-toc)

**Answer:**
```java
students.stream()
    .forEach(s -> System.out.println(s.getName() + ": " + s.getPercentage()));
```

---

<a name="q292"></a>
### 292) Get subjects offered in college?
[Back to TOC](#q292-toc)

**Answer:**
```java
Set<String> subjects = students.stream()
    .map(Student::getSubject)
    .collect(Collectors.toSet());
```

---

<a name="q293"></a>
### 293) Highest, lowest, and average percentage?
[Back to TOC](#q293-toc)

**Answer:**
```java
DoubleSummaryStatistics stats = students.stream()
    .mapToDouble(Student::getPercentage)
    .summaryStatistics();

System.out.println("Max: " + stats.getMax());
System.out.println("Min: " + stats.getMin());
System.out.println("Avg: " + stats.getAverage());
```

---

<a name="q294"></a>
### 294) Total number of students?
[Back to TOC](#q294-toc)

**Answer:**
```java
long count = students.stream().count();
```

---

<a name="q295"></a>
### 295) Group students by subject?
[Back to TOC](#q295-toc)

**Answer:**
```java
Map<String, List<Student>> groupedBySubject = students.stream()
    .collect(Collectors.groupingBy(Student::getSubject));
```

---

<a name="q296"></a>
### 296) Count employees in each department?
[Back to TOC](#q296-toc)

**Answer:**
```java
Map<String, Long> deptCount = employees.stream()
    .collect(Collectors.groupingBy(Employee::getDepartment, Collectors.counting()));
```

---

<a name="q297"></a>
### 297) Average salary of male and female employees?
[Back to TOC](#q297-toc)

**Answer:**
```java
Map<String, Double> avgSalaryByGender = employees.stream()
    .collect(Collectors.groupingBy(
        Employee::getGender, 
        Collectors.averagingDouble(Employee::getSalary)
    ));
```

---

<a name="q298"></a>
### 298) Highest paid employee?
[Back to TOC](#q298-toc)

**Answer:**
```java
Optional<Employee> highestPaid = employees.stream()
    .collect(Collectors.maxBy(Comparator.comparingDouble(Employee::getSalary)));
```

---

<a name="q299"></a>
### 299) Average age of each department?
[Back to TOC](#q299-toc)

**Answer:**
```java
Map<String, Double> avgAgeByDept = employees.stream()
    .collect(Collectors.groupingBy(
        Employee::getDepartment, 
        Collectors.averagingInt(Employee::getAge)
    ));
```

---

<a name="q300"></a>
### 300) Senior most employee?
[Back to TOC](#q300-toc)

**Answer:**
```java
Optional<Employee> seniorMost = employees.stream()
    .min(Comparator.comparingInt(Employee::getYearOfJoining));
```

---

<a name="q301"></a>
### 301) Youngest employee in organization?
[Back to TOC](#q301-toc)

**Answer:**
```java
Optional<Employee> youngest = employees.stream()
    .min(Comparator.comparingInt(Employee::getAge));
```

---

<a name="q302"></a>
### 302) Number of employees in each department?
[Back to TOC](#q302-toc)

**Answer:**
```java
Map<String, Long> count = employees.stream()
    .collect(Collectors.groupingBy(Employee::getDepartment, Collectors.counting()));
```

---

<a name="q303"></a>
### 303) Male and female employees count?
[Back to TOC](#q303-toc)

**Answer:**
```java
Map<String, Long> genderCount = employees.stream()
    .collect(Collectors.groupingBy(Employee::getGender, Collectors.counting()));
```

---

<a name="q304"></a>
### 304) What is an Exception?
[Back to TOC](#q304-toc)

**Answer:**
An unwanted or unexpected event that occurs during the execution of a program (at runtime) that disrupts the normal flow of instructions.

---

<a name="q305"></a>
### 305) Exception Handling Mechanism in Java?
[Back to TOC](#q305-toc)

**Answer:**
Using five keywords:
1.  **`try`**: Block where an exception might occur.
2.  **`catch`**: Handles the exception.
3.  **`finally`**: Code that always executes (cleanup).
4.  **`throw`**: Used to manually throw an exception.
5.  **`throws`**: Declares that a method might throw an exception.

---

<a name="q306"></a>
### 306) Error vs Exception?
[Back to TOC](#q306-toc)

**Answer:**
- **Error:** Indicates serious problems that a reasonable application should not try to catch (e.g., `OutOfMemoryError`, `StackOverflowError`).
- **Exception:** Indicates conditions that a reasonable application might want to catch (e.g., `IOException`, `NullPointerException`).

---

<a name="q307"></a>
### 307) Statements between try, catch, and finally?
[Back to TOC](#q307-toc)

**Answer:**
**No.** They must form a contiguous block.

---

<a name="q308"></a>
### 308) try block without catch or finally?
[Back to TOC](#q308-toc)

**Answer:**
**No.** It must be followed by at least one `catch` block or a `finally` block. (Exception: **Try-with-resources** in Java 7+).

---

<a name="q309"></a>
### 309) Exception in statement2: Does statement3 execute?
[Back to TOC](#q309-toc)

**Answer:**
**No.** Once an exception is thrown, the rest of the `try` block is skipped and control transfers to the `catch` block.

---

<a name="q310"></a>
### 310) Unreachable catch block error?
[Back to TOC](#310-toc)

**Answer:**
Occurs if you put a parent exception class (like `Exception`) before a child exception class (like `IOException`) in multiple catch blocks. The parent will catch everything, making the child catch block "unreachable".

---

<a name="q311"></a>
### 311) Exception Hierarchy?
[Back to TOC](#311-toc)

**Answer:**
`Throwable` (Root)
├── `Error`
└── `Exception`
    ├── `RuntimeException` (Unchecked)
    └── Other Exceptions (Checked)

---

<a name="q312"></a>
### 312) Runtime Exceptions examples?
[Back to TOC](#312-toc)

**Answer:**
`NullPointerException`, `ArrayIndexOutOfBoundsException`, `ArithmeticException`, `NumberFormatException`. These are **Unchecked** exceptions.

---

<a name="q313"></a>
### 313) What is OutOfMemoryError?
[Back to TOC](#313-toc)

**Answer:**
Thrown when the JVM cannot allocate an object because it is out of memory, and no more memory could be made available by the garbage collector.

---

<a name="q314"></a>
### 314) Checked vs Unchecked Exceptions?
[Back to TOC](#314-toc)

**Answer:**
- **Checked:** Checked at compile-time. You must either handle them or declare them in `throws`. (E.g., `IOException`).
- **Unchecked:** Occur at runtime. Compiler does not force you to handle them. (E.g., `NullPointerException`).

---

<a name="q315"></a>
### 315) ClassNotFoundException vs NoClassDefFoundError?
[Back to TOC](#315-toc)

**Answer:**
- **`ClassNotFoundException`**: Thrown when you try to load a class by its name using `Class.forName()` but the class is not on the classpath.
- **`NoClassDefFoundError`**: The class was present at compile-time but is **missing at runtime**.

---

<a name="q316"></a>
### 316) Statements after finally block if finally returns control?
[Back to TOC](#316-toc)

**Answer:**
**No.** If the `finally` block has a `return` or `throw` statement, any code after it is unreachable.

---

<a name="q317"></a>
### 317) Does finally execute if try/catch has a return?
[Back to TOC](#317-toc)

**Answer:**
**Yes.** The `finally` block always executes even if there is a `return` statement in the `try` or `catch` blocks.

---

<a name="q318"></a>
### 318) Throw exception manually?
[Back to TOC](#318-toc)

**Answer:**
Yes, using the **`throw`** keyword.
```java
if (age < 18) {
    throw new ArithmeticException("Not eligible to vote");
}
```

---

<a name="q319"></a>
### 319) Re-throwing an exception?
[Back to TOC](#319-toc)

**Answer:**
Catching an exception and then throwing it again (perhaps after logging it).

---

<a name="q320"></a>
### 320) Use of throws keyword?
[Back to TOC](#320-toc)

**Answer:**
To declare that a method might throw certain exceptions, delegating the responsibility of handling them to the caller.

---
"""
with open('ultimate-questions-cheatsheet/Java-Ultimate-Cheat-Sheet.md', 'a') as f:
    f.write(batch)
