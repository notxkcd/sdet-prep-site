---
title: "Cognizant_2025-02"
date: 2026-01-30
draft: false
---

---

## Original Questions

Cognizant (Java Selenium) Interview Questions conducted on 15/02/25 (1Hour):
--------------------------------------------------------------------------
1. Introduce yourself and current project handling
2. What is String Buffer and String Builder
3. Difference between Final, Finally and Finalize
4. What are the listeners in cucumber Framework
5. OOPS concept (Encapsulation and Inheritance)
6. Is two main class is possible? If yes or no. Why?
7. Difference between static block and Mail class (PSVM).. Which one will run first?
8. Feature file writing (Go to Flipkart, Login, Search Laptop, Click the Lenova Brand and Take the First one with name and Price)
9. What are Tags are available and where it is used in your framework?
10. How did you select the values which were the WebElement updated Dynamically?
11. Explain the concept Extent report creation?
12. Where did you use Group (Include and Exclude) - Exactly with real time scenarios in your framework?
13. Java Program - String is Anagram or not (Str 1 = Bored and Str 2 = Robed).

---

## Answers

### 1. Introduce yourself and current project handling
Standard intro. Briefly describe your role (SDET), your experience with Java/Selenium/etc., and then give a concise overview of your current project: what the application does (domain), your specific responsibilities (e.g., "I handle the end-to-end automation for the payment and checkout modules"), and the tech stack you use.

### 2. What is String Buffer and String Builder
Both are mutable classes for string manipulation, unlike the immutable `String` class.
-   **`StringBuilder`:** **Not thread-safe** (not synchronized). This makes it faster. This is the default choice for any single-threaded scenario, like building a string inside a method.
-   **`StringBuffer`:** **Thread-safe** (its methods are synchronized). This makes it slower due to locking overhead. You should only use it if you need to share and modify a string across multiple threads, which is a rare use case.

### 3. Difference between Final, Finally and Finalize
A classic Java trip-up question.
-   **`final`:** A keyword. When applied to a variable, it becomes a constant. When applied to a method, it cannot be overridden. When applied to a class, it cannot be extended.
-   **`finally`:** A code block. It's part of a `try-catch` statement. The `finally` block is **always executed**, regardless of whether an exception was thrown or not. It's critical for resource cleanup, like `driver.quit()`.
-   **`finalize()`:** A method. It's a method from the `Object` class that the garbage collector calls before an object is destroyed. It's deprecated, unreliable, and **should not be used** for resource cleanup.

### 4. What are the listeners in cucumber Framework
This is a trick question. **Cucumber itself does not have a "listener" concept in the same way TestNG or JUnit does.**

Cucumber's equivalent is **Hooks** (`@Before`, `@After`, `@BeforeStep`, `@AfterStep`).

The "listeners" (`ITestListener`, etc.) come from the test runner you use to execute Cucumber, which is typically **TestNG** or **JUnit**. So the correct answer is: "Cucumber uses hooks like `@Before` and `@After` for setup and teardown. The listener functionality, like taking a screenshot on failure with `onTestFailure`, is provided by the TestNG (or JUnit) runner that executes our Cucumber tests. We register a TestNG `ITestListener` in our suite to handle these events."

### 5. OOPS concept (Encapsulation and Inheritance)
-   **Encapsulation:** The bundling of data (fields) and the methods that operate on that data into a single unit (a class), and hiding the internal state from the outside. The **Page Object Model** is a perfect example where locators are `private` and interactions are exposed via `public` methods.
-   **Inheritance:** A mechanism where a child class acquires the properties and methods of a parent class (`extends` keyword). This is used for code reuse. A common example is having all test classes extend a `BaseTest` to inherit common `WebDriver` setup and teardown logic.

### 6. Is two main class is possible? If yes or no. Why?
A single Java application can have **only one entry point**. This means only one `public static void main(String[] args)` method will be executed by the JVM when you run the application.

However, you can have **multiple classes with a `main` method** in your project. Each of them can be run individually as a separate application. But within the context of a single run, only one `main` method serves as the starting point.

### 7. Difference between static block and Mail class (PSVM).. Which one will run first?
The interviewer means `main` method, not "Mail class".
A `static` block is executed when the class is first loaded into the JVM. The `main` method is the entry point for the program execution.

**The `static` block runs first.**

```java
public class ExecutionOrder {
    static {
        System.out.println("Static block runs first.");
    }

    public static void main(String[] args) {
        System.out.println("Main method runs second.");
    }
}
// Output:
// Static block runs first.
// Main method runs second.
```

### 8. Feature file writing (Go to Flipkart, Login, Search Laptop, Click the Lenova Brand and Take the First one with name and Price)
```gherkin
Feature: Product Search and Selection

  Scenario: Find the first Lenovo laptop and get its details
    Given I am a logged-in user on Flipkart
    When I search for "Laptop"
    And I filter the results by brand "Lenovo"
    Then I should see a list of Lenovo laptops
    And I can retrieve the name and price of the first laptop in the list
```

### 9. What are Tags are available and where it is used in your framework?
In Cucumber, tags are annotations (e.g., `@smoke`, `@regression`, `@sprint-5`) that you place above a `Feature` or `Scenario`.
-   **Purpose:** To categorize and group your tests.
-   **Usage:** They are used in the **runner class** (`@CucumberOptions`) to selectively run tests.
    -   `tags = "@smoke"`: Runs only smoke tests.
    -   `tags = "@regression and not @wip"`: Runs all regression tests except those marked as "work in progress".
This is how we manage different test suites (smoke, regression, etc.) from the same set of feature files.

### 10. How did you select the values which were the WebElement updated Dynamically?
This is about handling dynamic locators.
"I write locators that don't depend on the dynamic part of the attributes.
1.  **Use stable attributes:** I look for attributes that don't change, like `name` or a custom `data-testid`.
2.  **Use XPath functions:** If an ID is something like `product-123-button`, I use `starts-with(@id, 'product-')` or `contains(@id, '-button')`.
3.  **Use relationships (XPath Axes):** I find a nearby stable element (like a label with static text) and navigate from there using `following-sibling`, `ancestor`, etc. For example: `//h2[text()='Product Name']/following-sibling::div[@class='price']`."

### 11. Explain the concept Extent report creation?
ExtentReports is a third-party reporting library.
-   **Concept:** You create an `ExtentReports` object, attach a "reporter" (like `ExtentSparkReporter` which creates the HTML file), and then create `ExtentTest` objects for each of your tests. You log events (`pass`, `fail`, `info`) to these test objects.
-   **Integration:** The best way to integrate it is with a **TestNG `ITestListener`**.
    -   In `@BeforeSuite`, you initialize the `ExtentReports` object.
    -   In `onTestStart`, you create a new `ExtentTest`.
    -   In `onTestSuccess`/`onTestFailure`, you log the pass/fail status. In `onTestFailure`, you also attach a screenshot.
    -   In `@AfterSuite`, you call `extent.flush()` to write everything to the HTML file.

### 12. Where did you use Group (Include and Exclude) - Exactly with real time scenarios in your framework?
This refers to TestNG groups, configured in the `testng.xml` file.
"We use TestNG groups extensively to manage our test suites.
-   **Real-time scenario:** We have a `@Test(groups = {"smoke", "regression"})` for critical login tests. We have less critical tests marked only as `regression`.
-   **CI/CD Pipeline:**
    -   For our 'commit build' pipeline, we run only the smoke tests to get fast feedback. Our `testng-smoke.xml` is configured like this:
        ```xml
        <groups>
          <run>
            <include name="smoke"/>
          </run>
        </groups>
        ```
    -   For our 'nightly build', we run the full regression suite. Our `testng-regression.xml` is configured to run all tests *except* those we are currently working on:
        ```xml
        <groups>
          <run>
            <include name="regression"/>
            <exclude name="wip"/> <!-- work-in-progress -->
          </run>
        </groups>
        ```
This gives us flexible control over which tests to run in different contexts."

### 13. Java Program - String is Anagram or not (Str 1 = Bored and Str 2 = Robed).
Anagrams are strings that contain the same characters in a different order. The simplest way to check is to sort their character arrays and compare.

```java
import java.util.Arrays;

public class AnagramCheck {
    public static boolean areAnagrams(String s1, String s2) {
        // Sanitize inputs
        String cleanS1 = s1.replaceAll("\\s", "").toLowerCase();
        String cleanS2 = s2.replaceAll("\\s", "").toLowerCase();

        if (cleanS1.length() != cleanS2.length()) {
            return false;
        }

        char[] arr1 = cleanS1.toCharArray();
        char[] arr2 = cleanS2.toCharArray();

        Arrays.sort(arr1);
        Arrays.sort(arr2);

        return Arrays.equals(arr1, arr2);
    }

    public static void main(String[] args) {
        System.out.println(areAnagrams("Bored", "Robed")); // true
        System.out.println(areAnagrams("Listen", "Silent")); // true
        System.out.println(areAnagrams("Hello", "World")); // false
    }
}
```
