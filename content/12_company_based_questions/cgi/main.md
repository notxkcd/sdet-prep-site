---
title: "CGI"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

- CGI Interview Questions:- 45 Minutes
-----------------------
1. Tell me Yourself and projects 
2. Reverse string program
3. Oops concept - Full explanation 
4. Cucumber architecture and file structure 
5. Scenario writing for login page and explain it
6. TestNG annotation
7. Selenium version your are using

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. Tell me Yourself and projects
Standard opener. Give a concise summary of your professional background, focusing on your automation experience, the types of projects you've worked on (e.g., e-commerce, fintech), and the technologies you're proficient in (Java, Selenium, REST-assured, etc.).

### 2. Reverse string program
The standard and most efficient way is to use the `StringBuilder` class.

```java
public class StringReverser {
    public static String reverseString(String str) {
        if (str == null) {
            return null;
        }
        return new StringBuilder(str).reverse().toString();
    }
}
```
This demonstrates knowledge of the core Java library and an preference for clean, built-in solutions over manual loops for solved problems.

### 3. Oops concept - Full explanation
The four pillars of Object-Oriented Programming:
1.  **Encapsulation:** The practice of bundling data (fields) and the methods that operate on that data into a single unit (a class). It hides the internal state of an object from the outside. In test automation, the **Page Object Model** is a perfect example, where locators are kept private and access is provided through public methods.
2.  **Abstraction:** Hiding complex implementation details and showing only the necessary features. The `WebDriver` interface is the canonical example; you write your code against the `WebDriver` type, and it works for `ChromeDriver`, `FirefoxDriver`, etc., without you needing to know the internal details of each.
3.  **Inheritance:** A mechanism where a new class (subclass) inherits properties and methods from an existing class (superclass). Used for code reuse. For example, having a `BaseTest` class with common setup/teardown logic that all your test classes `extend`.
4.  **Polymorphism:** Literally "many forms." This is the ability of an object to take on many forms, most commonly seen through **method overriding**. A `BasePage` might have a `verifyPageIsLoaded()` method, which is then overridden by `HomePage` and `ProductPage` to add their own specific verifications.

### 4. Cucumber architecture and file structure
A typical Cucumber project architecture is designed to separate concerns:
-   **File Structure:**
    ```
    src/
    ├── test/
    │   ├── java/
    │   │   └── com/your/package/
    │   │       ├── stepdefinitions/  <- The glue code
    │   │       └── runners/          <- The test execution entry point
    │   └── resources/
    │       └── features/             <- The human-readable test cases
    └── pom.xml                       <- Maven dependencies and build config
    ```
-   **Architecture Components:**
    1.  **Feature Files:** `.feature` files containing scenarios written in Gherkin. These describe *what* the system should do.
    2.  **Step Definitions:** Java classes that "glue" the Gherkin steps to automation code. They define *how* each step is executed.
    3.  **Test Runner:** A JUnit or TestNG class that uses `@CucumberOptions` to configure and run the tests. It tells Cucumber where to find the feature files and step definitions.

### 5. Scenario writing for login page and explain it
This is asking for a Gherkin example.

**Feature File: `login.feature`**
```gherkin
Feature: User Login Functionality

  Scenario: Successful login with valid credentials
    Given I am on the application login page
    When I enter my valid username and password
    And I click the 'Login' button
    Then I should be successfully logged in and see the dashboard

  Scenario Outline: Unsuccessful login with invalid credentials
    Given I am on the application login page
    When I attempt to log in with "<username>" and "<password>"
    Then I should see an error message stating "<error_message>"

    Examples:
      | username        | password      | error_message          |
      | "invalid_user"  | "wrong_pass"  | "Invalid credentials." |
      | "valid_user"    | ""            | "Password is required."|
```
**Explanation:**
-   The `Feature` keyword describes the overall functionality.
-   `Scenario` describes a single, specific test case (the happy path).
-   `Scenario Outline` is a template used for data-driven testing. It runs once for each row in the `Examples` table, substituting the values in `<placeholders>`. This is efficient for testing multiple negative cases.

### 6. TestNG annotation
TestNG uses annotations to control test execution flow. The most important ones are:
-   `@Test`: Marks a method as a test case.
-   `@BeforeMethod` / `@AfterMethod`: Run before and after *each* `@Test` method. Perfect for driver setup and teardown.
-   `@BeforeClass` / `@AfterClass`: Run once before/after all tests in a class.
-   `@BeforeSuite` / `@AfterSuite`: Run once before/after all tests in the entire XML suite.
-   `@DataProvider`: Marks a method that supplies test data to a `@Test` method.

### 7. Selenium version your are using
"I am using **Selenium 4**. We upgraded to leverage its full W3C WebDriver protocol compliance, which offers more stable and consistent cross-browser testing. I've also made use of some of the new features like `RelativeLocators` for handling complex UI layouts." (Knowing the *why* is more important than just the number).
