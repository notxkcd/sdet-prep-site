---
title: "Wipro-3"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

Wipro level 1
-------------
1. Write a program/explain me the concept on how to remove duplicate in a long list of integers 
2. How will you replace a letter from a string 
3.  How to replace multiple letters from string using the same replace method 
4. How good are you in sql queries 
5. Say if we have 2 tables one in regression and other is in sdet and date is common in both the tables how you print all data excluding date (think and response with java perspective)
6. How you handle the scenario(5th question) if there is multiple table and each has lakh of datas
7. Difference between list and set

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. Write a program/explain me the concept on how to remove duplicate in a long list of integers
The most efficient and idiomatic way in Java is to use a `Set`.
-   **Concept:** A `Set` (like `HashSet` or `LinkedHashSet`) by definition cannot contain duplicate elements. When you try to add an element that is already present, the `add()` method returns `false` and the set remains unchanged.
-   **Program:**

```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

public class DuplicateRemover {
    public static List<Integer> removeDuplicates(List<Integer> numbers) {
        // Use LinkedHashSet to preserve the insertion order
        Set<Integer> uniqueNumbers = new LinkedHashSet<>(numbers);
        return new ArrayList<>(uniqueNumbers); // Convert back to a List if needed
    }

    public static int[] removeDuplicatesFromArray(int[] numbers) {
        // Java 8 Stream API - very concise
        return Arrays.stream(numbers).distinct().toArray();
    }

    public static void main(String[] args) {
        List<Integer> longList = Arrays.asList(1, 2, 3, 2, 4, 1, 5, 3, 6);
        System.out.println("Original List: " + longList);
        System.out.println("List without duplicates: " + removeDuplicates(longList));
        
        int[] longArray = {1, 2, 3, 2, 4, 1, 5, 3, 6};
        System.out.println("Original Array: " + Arrays.toString(longArray));
        System.out.println("Array without duplicates: " + Arrays.toString(removeDuplicatesFromArray(longArray)));
    }
}
```

### 2. How will you replace a letter from a string
Use the `replace()` or `replaceFirst()` methods of the `String` class.

```java
String original = "hello world";
String replaced = original.replace('o', 'x'); // replaces all 'o's
System.out.println(replaced); // hxllx wxrld
```
If you want to replace only the first occurrence:
```java
String replacedFirst = original.replaceFirst("o", "x"); // Uses regex for first argument
System.out.println(replacedFirst); // hxllo world
```

### 3. How to replace multiple letters from string using the same replace method
The `replace(char oldChar, char newChar)` method replaces *all* occurrences of the `oldChar`.
The `replaceAll(String regex, String replacement)` method allows you to use regular expressions to match multiple characters.

```java
String original = "apple banana";
String replaced = original.replace('a', 'x'); // Replaces all 'a'
System.out.println(replaced); // xpplx bxnxnx

// Using replaceAll with a regex to replace multiple specific characters
String replacedMultiple = original.replaceAll("[ae]", "X"); // Replaces 'a' or 'e'
System.out.println(replacedMultiple); // XpplX bXnXnX
```

### 4. How good are you in sql queries
"I would rate myself as proficient in SQL (a 7 out of 10). I'm comfortable writing standard DML (Data Manipulation Language) queries (`SELECT`, `INSERT`, `UPDATE`, `DELETE`) with `JOIN`s, `WHERE` clauses, `GROUP BY`, and aggregate functions. In my test automation work, I frequently use JDBC to query the database for test data setup and verification, and I can analyze query plans to identify performance issues."

### 5. Say if we have 2 tables one in regression and other is in sdet and date is common in both the tables how you print all data excluding date (think and response with java perspective)
This scenario is unclear. "Regression" and "SDET" are not table names. Assuming they mean two tables, `Table1` and `Table2`, both have a `date` column, and you want to join them and select all columns *except* the `date` column.

**SQL Perspective:**
```sql
SELECT
    T1.col1, T1.col2, -- all columns from Table1 except date
    T2.colX, T2.colY  -- all columns from Table2 except date
FROM
    Table1 T1
INNER JOIN
    Table2 T2 ON T1.CommonKey = T2.CommonKey -- Assuming a join condition
WHERE
    T1.DateColumn = T2.DateColumn; -- If date is the common column for joining
```
If you mean "select all columns except the date column from *one* table":
```sql
SELECT col1, col2, col3 -- manually list all columns except date
FROM YourTable;
```
There's no `SELECT * EXCLUDE date` syntax in standard SQL. You have to explicitly list the columns.

**Java Perspective (JDBC):**
"From a Java perspective using JDBC, I would execute the appropriate SQL query (as above). After getting the `ResultSet`, I would iterate through it. For each row, I would use `resultSet.getString("columnName")` or `resultSet.getInt("columnName")` for each column I *want* to print, explicitly skipping the `date` column."

### 6. How you handle the scenario(5th question) if there is multiple table and each has lakh of datas
If dealing with multiple tables with millions of rows, performance is critical.
1.  **Optimize SQL Queries:**
    -   **Indexing:** Ensure the columns used in `WHERE` clauses and `JOIN` conditions are indexed.
    -   **Filtering Early:** Use `WHERE` clauses to filter rows as early as possible before `JOIN`ing large tables.
    -   **Select Only Needed Columns:** Never use `SELECT *`. Explicitly select only the columns you need to reduce data transfer.
    -   **Limit Results:** Use `LIMIT` or `TOP` to fetch only a subset of data for testing if possible.
2.  **Database Connection Pooling:** In Java, use connection pooling (`HikariCP`, `c3p0`) instead of opening/closing connections for each query.
3.  **Fetch Size:** Set an appropriate `setFetchSize()` on the `Statement` or `PreparedStatement` to control how many rows are fetched from the database at once.
4.  **Java Memory:** Be mindful of Java's heap memory when processing large result sets. Stream processing or batch processing might be necessary rather than loading everything into an `ArrayList` at once.

### 7. Difference between list and set
-   **`List`:** An ordered collection of elements. Elements have an index. Allows duplicates. Implementations: `ArrayList`, `LinkedList`.
-   **`Set`:** An unordered collection of unique elements. Does not allow duplicates. Implementations: `HashSet`, `LinkedHashSet`, `TreeSet`.
