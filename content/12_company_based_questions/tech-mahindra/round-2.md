---
title: "Tech_Mahindra-2"
date: 2026-01-30
draft: false
---

---

## Original Questions

- Tech Mahindra level 1 interview
-------------------------------
1) tell about yourself 
2) framework structure 
3)final and finally
4)interface and abstract
5) write a query for second maximum 
6) did u use offset method
7lwhat is rest assured
8) what isnthe code for forbidden
9) post status code 
10)how vl u maintain the testdata
11) collection and types explain 
12)oops concept with framework 
13) what is defect tracking tool u r using 
14)explain cucumber reports

---

## Answers (No-BS Java QA / SDET Explanations)

### 1) tell about yourself
Standard opener. Keep it concise, professional, and highlight your automation experience, tech stack, and achievements.

### 2) framework structure
Describe the layered architecture of your test automation framework:
1.  **Test Layer:** TestNG test classes (contain test logic and assertions).
2.  **Page Object Layer:** Java classes representing web pages/components (locators, interaction methods).
3.  **API Layer:** Classes for API endpoints, containing methods for making API calls.
4.  **Utility Layer:** Helper classes (e.g., config reader, screenshot utility, Excel/JSON data reader).
5.  **Data Layer:** External data files (JSON, Excel, properties) for test data and configuration.
6.  **Build/Execution Layer:** Maven for dependencies, TestNG for test execution, Jenkins for CI/CD.

### 3) final and finally
-   **`final`:** A keyword. Makes a variable constant, a method non-overridable, or a class non-extendable.
-   **`finally`:** A block of code in a `try-catch` statement that **always executes**, regardless of whether an exception occurred. Used for resource cleanup (`driver.quit()`).

### 4) interface and abstract
-   **Interface:** A blueprint defining a contract. Contains abstract methods (and default/static methods from Java 8). A class `implements` multiple interfaces.
-   **Abstract Class:** A class that cannot be instantiated directly. Can have abstract and concrete methods, fields, and constructors. A class `extends` only one abstract class.

### 5) write a query for second maximum
Assuming a table `Employees` with a `Salary` column.

```sql
-- Method 1: Using Subquery
SELECT Salary
FROM Employees
WHERE Salary < (SELECT MAX(Salary) FROM Employees)
ORDER BY Salary DESC
LIMIT 1;

-- Method 2: Using LIMIT and OFFSET (MySQL/PostgreSQL)
SELECT DISTINCT Salary
FROM Employees
ORDER BY Salary DESC
LIMIT 1 OFFSET 1;

-- Method 3: Using DENSE_RANK (SQL Server, Oracle)
SELECT Salary
FROM (
    SELECT Salary, DENSE_RANK() OVER (ORDER BY Salary DESC) as rnk
    FROM Employees
) AS RankedSalaries
WHERE rnk = 2;
```

### 6) did u use offset method
This is ambiguous.
-   **SQL `OFFSET`:** Used with `LIMIT` to skip a number of rows. (Example in previous question for second max salary).
-   **Java String `indexOf(char ch, int fromIndex)`:** Can search from an offset index.
-   **Selenium `read_file` tool:** Has an `offset` parameter for reading specific lines.
Clarify which "offset" is being referred to.

### 7)lwhat is rest assured
REST-assured is a Java DSL (Domain Specific Language) for testing RESTful web services. It provides a fluent, BDD-style API (`given().when().then()`) that simplifies writing robust and readable API tests.

### 8) what isnthe code for forbidden
This likely refers to the HTTP status code for "Forbidden".
It is **`403 Forbidden`**.

### 9) post status code
The status code returned for a successful `POST` request is typically **`201 Created`**. This indicates that the request has been fulfilled and has resulted in one or more new resources being created.

### 10)how vl u maintain the testdata
"We maintain test data externally, separate from the test code.
-   **Configuration:** For environment-specific settings (URLs, API keys), we use `.properties` files.
-   **Test Case Data:** For scenario-specific inputs and expected outputs, we use **JSON files**. Our framework has a utility that reads this JSON, and TestNG's `@DataProvider` supplies it to our tests.
-   **Database:** For complex scenarios, we sometimes use JDBC to set up specific test data directly in the database before a test and clean it up afterward."

### 11) collection and types explain
The Java Collections Framework provides interfaces and classes to represent collections of objects.
-   **`Collection` interface:** Base interface.
-   **`List`:** Ordered collection, allows duplicates (e.g., `ArrayList`, `LinkedList`).
-   **`Set`:** Unordered collection, does not allow duplicates (e.g., `HashSet`, `LinkedHashSet`).
-   **`Map`:** Stores key-value pairs, keys must be unique (e.g., `HashMap`, `TreeMap`).

### 12)oops concept with framework
(Repeated).
-   **Encapsulation:** Page Object Model (`private` locators, `public` methods).
-   **Abstraction:** `WebDriver` interface.
-   **Inheritance:** `BaseTest` and `BasePage` classes.
-   **Polymorphism:** Method overriding in page objects (`verifyPageLoaded()`).

### 13) what is defect tracking tool u r using
"We use **Jira** for defect tracking and management. It allows us to log bugs with detailed information, track their lifecycle, and collaborate with developers on resolution."

### 14)explain cucumber reports
Cucumber can generate several types of reports via its `plugin` option in `@CucumberOptions`:
-   **`pretty`:** Human-readable console output.
-   **`html`:** Basic HTML report.
-   **`json`:** A JSON file containing raw test results, which can be processed by other reporting tools.
-   **`junit`:** An XML report in JUnit format.
For richer, more interactive reports, tools like **ExtentReports** or **Allure Reports** are typically integrated by processing Cucumber's JSON output.
