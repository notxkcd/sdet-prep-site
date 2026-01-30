---
title: "Mphasis"
date: 2026-01-30
draft: false
---

---

## Original Questions

Mphasis
--------
L1 Virtual Discussion, 30 mins

1. Introduce about yourself and your project
2. What are the automation tools / technologies that you currently worked?
3. Java program to create an array and find the second maximum value from array.
4. Have you worked in API? How will you validate the API responses?
5. Have you worked in Database Testing?
6. Explain primary key and foreign key?
7. About inner join
8. Scenario: Consider the code in local is correct and when you try to upload and run using jenkins there is a error. What are the possible outcomes for the error?
9. About git usage in your current project.

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. Introduce about yourself and your project
Standard opener. Give a concise summary of your professional experience, the project you worked on (domain, what it does), and your specific role and contributions as an automation engineer.

### 2. What are the automation tools / technologies that you currently worked?
List your tech stack clearly.
-   **Core Language:** Java
-   **UI Automation:** Selenium WebDriver
-   **API Automation:** REST-assured
-   **Test Runner:** TestNG
-   **Build & Dependency Management:** Maven
-   **CI/CD:** Jenkins
-   **Version Control:** Git, with GitHub
-   **Test Management:** Jira (with Xray/Zephyr)

### 3. Java program to create an array and find the second maximum value from array.
A common coding question. The streams approach is clean and modern.

```java
import java.util.Arrays;
import java.util.Comparator;

public class SecondMax {
    public static int findSecondMaximum(int[] arr) {
        // Handle edge cases
        if (arr == null || arr.length < 2) {
            throw new IllegalArgumentException("Array must contain at least two elements.");
        }

        return Arrays.stream(arr)
                     .distinct() // Remove duplicates to handle arrays like {10, 10, 5}
                     .boxed()    // Convert IntStream to Stream<Integer>
                     .sorted(Comparator.reverseOrder()) // Sort in descending order
                     .skip(1)    // Skip the first (largest) element
                     .findFirst()// Get the next element
                     .orElseThrow(() -> new IllegalStateException("Array does not have a second unique maximum value."));
    }

    public static void main(String[] args) {
        int[] numbers = {10, 5, 8, 20, 19, 20};
        System.out.println("Second Maximum: " + findSecondMaximum(numbers)); // Output: 19
    }
}
```

### 4. Have you worked in API? How will you validate the API responses?
"Yes, I have extensive experience in API automation using REST-assured. I validate API responses in several ways:
1.  **Status Code:** The first and most basic check. `response.then().statusCode(200);`
2.  **Response Body:**
    -   **JSONPath:** I use JSONPath expressions to extract and assert specific values from the JSON response body. For example, `response.then().body("user.name", equalTo("John Doe"));`
    -   **POJO Deserialization:** For complex responses, I deserialize the JSON response into a POJO (Plain Old Java Object) and then use standard Java assertions on the object's getter methods.
3.  **Response Headers:** I validate important headers, like `Content-Type` or caching headers. `response.then().header("Content-Type", "application/json");`
4.  **Schema Validation:** I validate the response structure against a predefined JSON Schema to ensure the API contract is not broken.
5.  **Response Time:** I check that the API responds within an acceptable time limit. `response.then().time(lessThan(2000L));`"

### 5. Have you worked in Database Testing?
"Yes. In my role, database testing is a key part of ensuring data integrity. I use **JDBC (Java Database Connectivity)** in my automation framework to:
1.  **Test Data Setup:** Insert or update records in the database to create a specific precondition for a test.
2.  **Verification:** After performing an action through the UI or an API, I query the database directly to verify that the data was created, updated, or deleted correctly. This is more reliable than just trusting what the UI shows.
3.  **Cleanup:** I run `DELETE` queries in my `@AfterMethod` to remove any test data I created, ensuring tests are isolated and repeatable."

### 6. Explain primary key and foreign key?
-   **Primary Key (PK):** A constraint that uniquely identifies each record in a table. A primary key must contain unique values and cannot contain NULL values. There can be only one primary key in a table.
-   **Foreign Key (FK):** A key used to link two tables together. It's a field (or collection of fields) in one table that refers to the PRIMARY KEY in another table. This is how you create relationships between tables (e.g., the `CustomerID` in an `Orders` table is a foreign key that points to the primary key in the `Customers` table).

### 7. About inner join
An `INNER JOIN` is a SQL clause used to combine rows from two or more tables based on a related column between them. It returns only the records that have matching values in both tables.

**Example:**
```sql
SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;
```
This query will return a list of order IDs and the corresponding customer names, but only for orders that have a matching customer in the `Customers` table.

### 8. Scenario: Consider the code in local is correct and when you try to upload and run using jenkins there is a error. What are the possible outcomes for the error?
This is a classic environment-difference problem. The possible causes are:
1.  **Environment Configuration Mismatch:** The Jenkins agent may be pointing to a different application URL (e.g., Staging vs. QA), a different database, or have different API keys. The configuration files used by Jenkins might be incorrect.
2.  **Dependency Issues:** The Jenkins agent might have a different version of Java, Maven, or a browser installed than what's on the local machine. Or, a dependency might be missing from the `pom.xml` but was present locally for some reason.
3.  **Pathing and File System:** The test might rely on a hardcoded file path (e.g., `C:\Users\MyUser\file.txt`) that doesn't exist on the Linux-based Jenkins agent. All file paths should be relative.
4.  **Timing and Performance:** The Jenkins agent or the test environment it runs against might be slower than the local machine, causing explicit waits to time out. The waits might need to be more robust or have longer timeouts.
5.  **Headless/Permissions Issues:** If Jenkins is running in a headless environment, tests that rely on UI rendering might behave differently. There could also be permissions issues where the Jenkins user cannot access certain files or directories.

### 9. About git usage in your current project.
"We use a **Git-flow-based branching strategy**.
1.  All new work starts by creating a **feature branch** from the main `develop` branch.
2.  I commit my automation code to my local feature branch throughout the day (`git commit`).
3.  At the end of the day, or when the feature is complete, I push my branch to the remote GitHub repository (`git push`).
4.  I then open a **Pull Request (PR)** to merge my feature branch into `develop`.
5.  Another team member reviews my code in the PR. Once it's approved and the Jenkins CI build (which runs our tests) passes, the code is merged. This ensures code quality and prevents breaking the main development branch."
