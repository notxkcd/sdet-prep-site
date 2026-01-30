---
title: "Capgemini-12"
date: 2026-01-30
draft: false
---

---

## Original Questions

Capgemini interview questions:
---------------------------
Framework used in API 
Explain pom 
WebDriver driver equal =new web driver();
Explain Abstraction OOPSconcept?
Explain put patch 
Collection Vs collections 
Garbage collection 
Priority Severity? With example 
Difference between equal to dot equal to operator? 
String reversal program 
SQL query for to find second largest salary? 
Element click intercepted exception 
Expalin BDD framework

---

## Answers (No-BS Java QA / SDET Explanations)

### Framework used in API
"For API automation, we use **REST-assured** as our primary framework with Java. It provides a fluent, BDD-style API (`given().when().then()`) for making HTTP requests and validating responses. We integrate it with TestNG for test execution and reporting."

### Explain pom
POM can refer to:
1.  **Project Object Model (Maven):** The `pom.xml` file, which defines a Maven project's dependencies and build configuration.
2.  **Page Object Model (Selenium):** A design pattern for UI test automation, where each web page (or significant component) is represented as a class that encapsulates its locators and interaction methods.

### WebDriver driver equal =new web driver();
This syntax is **incorrect**. `WebDriver` is an interface, so you cannot instantiate it directly.
The correct way to instantiate a `WebDriver` is to use a concrete implementation of the interface, such as `ChromeDriver` or `FirefoxDriver`.
**Correct Syntax:** `WebDriver driver = new ChromeDriver();`

### Explain Abstraction OOPSconcept?
Abstraction is a core OOP concept of hiding complex implementation details and showing only the essential features of an object or system. It simplifies complexity. In Java, it's achieved through abstract classes and interfaces. For example, the `WebDriver` interface abstracts away the browser-specific complexities.

### Explain put patch
-   **`PUT` method:** Used to **completely replace** an existing resource on the server with the new data provided in the request body. It is **idempotent**.
-   **`PATCH` method:** Used to apply **partial modifications** to an existing resource. You only send the fields that need to be changed. It is generally **not idempotent**.

### Collection Vs collections
-   **`Collection` (interface):** The root interface in the Java Collections Framework. It defines common operations for groups of objects (e.g., `add()`, `remove()`, `size()`). `List`, `Set`, and `Queue` interfaces extend `Collection`.
-   **`Collections` (class):** A utility class in `java.util.Collections` that provides static helper methods for operating on or returning collections. Examples: `Collections.sort()`, `Collections.reverseOrder()`, `Collections.synchronizedList()`.

### Garbage collection
Garbage Collection (GC) is the automatic process in Java (and other languages) of reclaiming memory occupied by objects that are no longer referenced by the running program. This frees the programmer from manually managing memory allocation and deallocation, preventing memory leaks.

### Priority Severity? With example
-   **Priority:** The business urgency to fix a bug (e.g., High, Medium, Low). Decided by Product Owner.
-   **Severity:** The technical impact of a bug on the system (e.g., Critical, Major, Minor). Decided by QA.
-   **Example:** A typo on the company homepage is low severity (functional impact is minimal) but high priority (brand damage).

### Difference between equal to dot equal to operator?
This refers to `==` operator and `.equals()` method.
-   **`==` operator:**
    -   For primitive types (`int`, `char`, `boolean`), compares their values.
    -   For objects, compares their memory addresses (checks if two references point to the same object).
-   **`.equals()` method:**
    -   For objects, it compares their content or state. Classes like `String` override this method to provide content-based comparison.

### String reversal program
`new StringBuilder(str).reverse().toString();`

### SQL query for to find second largest salary?
Assuming an `Employees` table with a `Salary` column.

```sql
SELECT DISTINCT Salary
FROM Employees
ORDER BY Salary DESC
LIMIT 1 OFFSET 1;
```
This is for MySQL/PostgreSQL. For other databases, you might use window functions like `DENSE_RANK()`.

### Element click intercepted exception
This is **`ElementClickInterceptedException`**. It occurs when Selenium tries to click an element, but another element (like an overlay, popup, or loading spinner) is covering it, preventing the click from reaching the intended element.
-   **Handling:** Use `Explicit Waits` to wait for the overlay to disappear (`ExpectedConditions.invisibilityOfElementLocated()`) or for the target element to become clickable (`ExpectedConditions.elementToBeClickable()`). Sometimes, `JavascriptExecutor` can force a click as a last resort.

### Explain BDD framework
BDD (Behavior-Driven Development) is an agile software development approach that focuses on defining application behavior in a human-readable format. Frameworks like Cucumber implement BDD by allowing test scenarios to be written in Gherkin (`Given/When/Then`), linking them to automation code, and serving as living documentation understandable by both technical and non-technical team members.
