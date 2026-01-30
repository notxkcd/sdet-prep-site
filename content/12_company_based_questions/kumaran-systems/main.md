---
title: "Kumaran_Systems"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

Kumaran Systems
---------------
1.Roles and Responsibilities
2.cucmber framework
3.TestNg annotation
4.amazon xpath for simcards in mobile(not use directly text method)
5.Java program:Reverse the string
6.Any Java program using hashmap
7.SQL Left join 
8.In a table fetch only headers using SQL query.9. API Http codes.
10. xpath methods
11.StringBuilder and StringBuffer

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. Roles and Responsibilities
Standard. Describe your day-to-day as an SDET/QA Automation Engineer, including framework development, test scripting (UI/API), CI/CD integration, bug reporting, and team collaboration.

### 2. cucmber framework
(Typo for Cucumber framework). A BDD framework that uses Gherkin (`Given/When/Then`) to describe application behavior in `.feature` files, which are then linked to executable code (step definitions) written in Java. Promotes collaboration and living documentation.

### 3. TestNg annotation
TestNG annotations define how test methods and configuration methods should be executed.
-   `@Test`: Marks a method as a test.
-   `@BeforeMethod`, `@AfterMethod`: Run before/after each test method. Ideal for browser setup/teardown.
-   `@BeforeClass`, `@AfterClass` (etc.): For class-level setup/teardown.
-   `@DataProvider`: Supplies data to a test method.

### 4. amazon xpath for simcards in mobile(not use directly text method)
This is a practical XPath question, implying you need to find an element without relying on its direct text content, likely because text can change or is not unique. You'd typically use attributes.
(Requires inspecting Amazon.com after searching for "simcards").

Example if a simcard listing has a data attribute for its product type:
`//div[@data-product-type='simcard']`
Or an input field for quantity related to simcards:
`//input[contains(@id, 'quantity') and contains(@name, 'simcard')]`

The key is to identify unique and stable attributes from the HTML.

### 5. Java program:Reverse the string
`new StringBuilder(str).reverse().toString();`

### 6. Any Java program using hashmap
A common use case is counting the frequency of elements (like words or characters) in a string.

```java
import java.util.HashMap;
import java.util.Map;

public class WordFrequency {
    public static Map<String, Integer> countWordOccurrences(String sentence) {
        Map<String, Integer> wordCounts = new HashMap<>();
        if (sentence == null || sentence.isEmpty()) {
            return wordCounts;
        }
        String[] words = sentence.toLowerCase().split("\\s+"); // Split by whitespace
        for (String word : words) {
            wordCounts.put(word, wordCounts.getOrDefault(word, 0) + 1);
        }
        return wordCounts;
    }

    public static void main(String[] args) {
        Map<String, Integer> freq = countWordOccurrences("hello world hello");
        System.out.println(freq); // Output: {world=1, hello=2}
    }
}
```

### 7. SQL Left join
A `LEFT JOIN` (or `LEFT OUTER JOIN`) in SQL returns all rows from the left table, and the matching rows from the right table. If there is no match, the right side will have `NULL` values.

```sql
SELECT
    Customers.CustomerName,
    Orders.OrderID
FROM
    Customers
LEFT JOIN
    Orders ON Customers.CustomerID = Orders.CustomerID;
```
This will return all customers, and their orders if they have any. Customers without orders will still be listed, but with `NULL` in the `OrderID` column.

### 8. In a table fetch only headers using SQL query.
If you have access to the database's metadata (information schema), you can query that.
-   **MySQL:**
    `SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'your_database' AND TABLE_NAME = 'your_table';`
-   **PostgreSQL:**
    `SELECT column_name FROM information_schema.columns WHERE table_schema = 'public' AND table_name = 'your_table';`
-   **Generic:** In many SQL clients, `DESCRIBE your_table;` or `SHOW COLUMNS FROM your_table;` will also give column information.

### 9. API Http codes.
Standard HTTP status codes (`200 OK`, `201 Created`, `400 Bad Request`, `404 Not Found`, `500 Internal Server Error`, etc.).

### 10. xpath methods
XPath functions are often called "methods". Examples:
-   `text()`: `//a[text()='Login']`
-   `contains()`: `//div[contains(@id, 'product-')]`
-   `starts-with()`: `//input[starts-with(@name, 'user')]`
-   `ends-with()` (XPath 2.0+): `//div[ends-with(@id, '-button')]`
-   `normalize-space()`: `//button[normalize-space()='Submit']` (handles leading/trailing/multiple spaces)
These are used within the `[]` predicate of an XPath expression.

### 11. StringBuilder and StringBuffer
Both are mutable classes for string manipulation.
-   **`StringBuilder`:** Not thread-safe, faster. Use in single-threaded contexts.
-   **`StringBuffer`:** Thread-safe (synchronized), slower. Use only if multiple threads modify the string concurrently.
