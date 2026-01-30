---
title: "Wipro-2"
date: 2026-01-30
draft: false
---

---

## Original Questions

Wipro interview questions :
--------------------------
1.Tell me about your self
2.Frame work explain
3.Reverse the string program
4.Testng annotation
5.Cumber scenarios, cumber annotations
6.Http methods in API
7.What are the dependency you know?
8.what is inheritance ?
9.what is scenario outline
10.How will you pass the value in has-map set?
11. How good are u in java - 4/5

---

## Answers

### 1. Tell me about your self
Standard opener. Keep it concise, professional, and focus on your relevant experience (automation skills, tech stack, achievements).

### 2. Frame work explain
Describe your test automation framework's architecture:
-   **Core stack:** Java, Selenium WebDriver, TestNG, REST-assured.
-   **Design patterns:** Page Object Model for UI, custom API client for REST-assured.
-   **Data management:** Data-driven, using `@DataProvider` from TestNG to read data from JSON files.
-   **Reporting:** ExtentReports, integrated with TestNG listeners.
-   **CI/CD:** Maven for build, Jenkins for continuous integration.

### 3. Reverse the string program
The most efficient and readable way:
```java
public String reverseString(String str) {
    if (str == null) return null;
    return new StringBuilder(str).reverse().toString();
}
```

### 4. Testng annotation
TestNG annotations define how test methods and configuration methods should be executed.
-   **`@Test`:** Marks a method as a test.
-   **`@BeforeMethod`, `@AfterMethod`:** Run before/after each test method. Ideal for browser setup/teardown.
-   **`@BeforeClass`, `@AfterClass`:** Run once before/after all tests in a class.
-   **`@BeforeSuite`, `@AfterSuite`:** Run once before/after all tests in the entire XML suite.
-   **`@DataProvider`:** Supplies data to a test method.

### 5. Cumber scenarios, cumber annotations
This refers to **Cucumber** scenarios and annotations.
-   **Scenarios:** A description of a specific behavior, written in Gherkin (`Given/When/Then`) in a `.feature` file.
-   **Cucumber Annotations (in Java step definitions):** `@Given`, `@When`, `@Then`, `@And`, `@But`. These connect the Gherkin steps to their Java implementation.
-   **Cucumber Hooks:** `@Before`, `@After`, `@BeforeStep`, `@AfterStep`. These control setup and teardown for scenarios/steps.

### 6. Http methods in API
The standard verbs used in HTTP requests for APIs:
-   `GET`: Retrieve data.
-   `POST`: Create new data.
-   `PUT`: Completely update/replace existing data.
-   `PATCH`: Partially update existing data.
-   `DELETE`: Remove data.

### 7. What are the dependency you know?
This means software libraries or modules that your project relies on.
-   **Selenium WebDriver:** For browser automation.
-   **TestNG:** For testing framework functionalities.
-   **REST-assured:** For API automation.
-   **Apache POI:** For Excel file handling.
-   **ExtentReports:** For test reporting.
-   **Guava / Apache Commons Lang / IO:** General utility libraries.
All these are declared in your `pom.xml` (if using Maven).

### 8. what is inheritance ?
A core OOP concept where one class (`child`) acquires properties and methods from another class (`parent`). It promotes code reuse and establishes an "is-a" relationship. Example: a `Dog` `is-a` `Animal`. In test frameworks, `BaseTest` classes are inherited by test classes.

### 9. what is scenario outline
In Cucumber, a `Scenario Outline` is a template for a test case that is executed multiple times with different sets of data. It uses `<placeholders>` in the steps that are filled from an `Examples` table. It's Cucumber's way to achieve data-driven testing.

### 10. How will you pass the value in has-map set?
This is a mixed question, likely meaning "how do you add values to a `HashMap`?" or "how do you use a `Set` for values?"
-   **`HashMap`:** You pass key-value pairs using the `put()` method.
    ```java
    Map<String, String> config = new HashMap<>();
    config.put("browser", "chrome"); // key "browser", value "chrome"
    ```
-   You don't typically "pass values into a `HashMap Set`" as it's not a standard construct. If they mean "what if the values in a map are a Set?", then you'd do:
    ```java
    Map<String, Set<String>> userRoles = new HashMap<>();
    userRoles.put("admin", new HashSet<>(Arrays.asList("manage", "reports")));
    ```

### 11. How good are u in java - 4/5
Be honest and be prepared to back it up.
"I would rate myself a **4 out of 5**. I'm proficient in core Java concepts like OOPs, Collections, Exception Handling, and multithreading, and I write clean, performant, and maintainable Java code for our automation frameworks. I'm always looking to learn and apply new Java features like Streams and Optionals. I might not be a pure Java developer, but I apply Java development best practices in my SDET role."
