---
title: "Zopsmart"
date: 2026-01-30
draft: false
---

---

## Original Questions

- Company Name : Zopsmart
- Mode of Interview : Virtual
Questions:
-----------
1.Difference between smoke and Integration Test
2.How Often will you do smoke test in your project
3.Drawbacks of Manual Testing
4.Difference between priority and severity
5.What is Testcases,TestPlan,Scenario
6.All OOps Concept
7.How to create an object for abstract class
8.can we create an object for interface
9.Why String is immutable
10.methods used to compare string and their differences
11.Program to find second largest number in an array
12.RestAssured code to validate the response(List of all Users) of Get Request
13.qn about agile

---

## Answers

### 1. Difference between smoke and Integration Test
-   **Smoke Test:** A quick, high-level test of the most critical functionalities to ensure the build is stable enough for further testing. It's a "go/no-go" decision.
-   **Integration Test:** Verifies the interactions and data flow between different modules or components of a software system. Ensures they work correctly when combined.

### 2. How Often will you do smoke test in your project
"We run our automated smoke test suite **on every code commit** to the `develop` or `main` branch, as part of our CI pipeline. This provides immediate feedback on the health of the latest build. We also run it before any major deployment to a new environment."

### 3. Drawbacks of Manual Testing
1.  **Time-Consuming:** Manual execution is slow and requires significant human effort.
2.  **Prone to Human Error:** Testers can miss details, make mistakes, or become fatigued, leading to inconsistent results.
3.  **Not Scalable:** Difficult to execute large test suites for regression testing or complex data-driven scenarios.
4.  **Repetitive and Boring:** Performing the same tests repeatedly can lead to demotivation.
5.  **Costly:** High human resource costs for long-term regression testing.

### 4. Difference between priority and severity
-   **Priority:** Business urgency of a defect (High, Medium, Low). Decided by Product Owner/Management.
-   **Severity:** Technical impact of a defect on the system (Critical, Major, Minor, Trivial). Decided by QA.

### 5. What is Testcases,TestPlan,Scenario
-   **Test Case:** A set of actions executed to verify a specific functionality, including preconditions, steps, and expected results.
-   **Test Plan:** A formal document outlining the strategy, scope, resources, schedule, and environment for testing a project.
-   **Scenario:** In BDD (Cucumber), a specific example of how a feature behaves, written in Gherkin (`Given/When/Then`).

### 6. All OOps Concept
The four pillars of Object-Oriented Programming:
1.  **Encapsulation:** Bundling data and methods into a single unit, hiding implementation.
2.  **Abstraction:** Showing essential features, hiding complexity.
3.  **Inheritance:** Reusing code by creating new classes from existing ones.
4.  **Polymorphism:** "Many forms," allowing objects of different classes to be treated as objects of a common type.

### 7. How to create an object for abstract class
You cannot directly create an object of an abstract class using `new`.
To use an abstract class, you must:
1.  Create a **concrete subclass** that `extends` the abstract class.
2.  Implement all the abstract methods from the abstract class in the concrete subclass.
3.  Then, create an object of the **concrete subclass**. This object can then be referenced by the abstract class type (polymorphism).

### 8. can we create an object for interface
No, you cannot directly create an object of an interface using `new`. An interface only defines a contract; it doesn't provide implementation.
To use an interface, you must:
1.  Create a **concrete class** that `implements` the interface.
2.  Implement all methods declared in the interface.
3.  Then, create an object of the **concrete class**. This object can then be referenced by the interface type (polymorphism).

### 9. Why String is immutable
`String` objects in Java are immutable because once created, their value cannot be changed.
-   **Thread Safety:** Immutable objects are inherently thread-safe, making them safe to share across multiple threads without external synchronization.
-   **Security:** Important for parameters in network connections, database URLs, and file paths. If a string could be modified after security checks, it would be a vulnerability.
-   **Caching:** String literals are stored in the String Constant Pool, saving memory.

### 10. methods used to compare string and their differences
-   **`==` operator:** Compares memory addresses (references). Returns `true` only if both string variables refer to the *exact same object* in memory. Not recommended for content comparison.
-   **`.equals(Object other)` method:** Compares the actual content (character sequence) of two string objects. This is the correct method for checking if two strings have the same value. Case-sensitive.
-   **`.equalsIgnoreCase(String anotherString)` method:** Compares the content of two strings, ignoring case differences.

### 11. Program to find second largest number in an array
```java
import java.util.Arrays;
import java.util.Comparator;

public class SecondLargest {
    public static int findSecondLargest(int[] arr) {
        if (arr == null || arr.length < 2) {
            throw new IllegalArgumentException("Array must contain at least two elements.");
        }
        return Arrays.stream(arr)
                     .distinct() // Remove duplicates
                     .boxed()    // Convert to Stream<Integer>
                     .sorted(Comparator.reverseOrder()) // Sort in descending order
                     .skip(1)    // Skip the largest element
                     .findFirst()// Get the next (second largest)
                     .orElseThrow(() -> new IllegalStateException("Array does not have a second distinct largest element."));
    }
}
```

### 12. RestAssured code to validate the response(List of all Users) of Get Request
```java
import static io.restassured.RestAssured.*;
import static org.hamcrest.Matchers.*;

public void validateUsersList() {
    given()
        .baseUri("https://api.example.com")
    .when()
        .get("/users") // Assuming this returns a list of users
    .then()
        .statusCode(200) // Validate status code
        .body("$", hasSize(greaterThan(0))) // Validate that the root is a list and not empty
        .body("[0].id", notNullValue()) // Validate first user has an ID
        .body("[0].name", isA(String.class)); // Validate first user has a name (string)
        // You can add more specific assertions for each user's properties.
}
```

### 13. qn about agile
(Question about Agile). Explain Agile principles (iterative, incremental, customer collaboration, flexibility) and mention a framework like Scrum (sprints, stand-ups, etc.).
