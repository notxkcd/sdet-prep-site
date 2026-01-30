---
title: "Maltras business economics pvt ltd"
date: 2026-01-30
draft: false
---

---

## Original Questions

Maltras business economics pvt ltd Interview Questions:
Round 1:
1. What is databinding?
2. What is Regression testing?
3. What is Configuration management?
4. What is API timeout?
5. What is the difference between API and UI Testing?
6. What is test runner file?
7. What is the difference between Behaviour and Datadriven?
8. What is token generation?
9. What is SQL injection?

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. What is databinding?
Databinding is a technique that establishes a connection between the application UI (user interface) and the data it displays. When the data changes, the UI automatically updates, and vice-versa.
-   **Frontend:** In web frameworks like Angular, React (with state management), or Vue, databinding connects UI elements to data models.
-   **Java Context (less common for traditional desktop UI):** In Java, older frameworks like Swing/AWT might use custom binding. More common in newer Java FX or Spring applications for connecting data to UI forms.
-   **QA Relevance:** When testing, you need to verify that databinding works correctly. If you update a field in the UI, you check if the underlying data model is updated. If the data model changes (e.g., from an API call), you check if the UI reflects that change.

### 2. What is Regression testing?
Regression testing is the process of testing existing software to ensure that changes (like new features, bug fixes, or configuration changes) have not introduced new defects or re-introduced old ones into previously working functionality.
-   **Goal:** To ensure that the software still functions correctly after modifications.
-   **How:** Typically involves re-running a comprehensive suite of previously passed test cases.
-   **Automation:** Regression testing is a prime candidate for test automation because it's repetitive and critical. An automated regression suite can be run quickly and frequently.

### 3. What is Configuration management?
Configuration management (CM) is a process for systematically controlling, organizing, and tracking changes to the components of a system.
-   **Code:** Using version control systems like Git to track changes to source code, test scripts, and framework code.
-   **Environments:** Managing and consistently setting up test, staging, and production environments (e.g., using Infrastructure as Code tools like Terraform or Ansible).
-   **Test Data:** Ensuring test data is consistent and versioned, or generated reproducibly.
-   **Purpose:** To maintain consistency, prevent conflicts, ensure reproducibility, and support auditing throughout the software development lifecycle. For QA, it means knowing exactly what version of the code is running on what environment, and having confidence that test runs are repeatable.

### 4. What is API timeout?
An API timeout occurs when a client (e.g., your test script or a frontend application) sends a request to an API endpoint, but the API server does not respond within a predefined time limit.
-   **Client-side timeout:** Configured by the client. If the server doesn't respond in time, the client aborts the connection and reports an error. Your `REST-assured` tests should have configurable timeouts.
-   **Server-side timeout:** Configured by the server. If a request takes too long to process, the server might terminate the process and return a `504 Gateway Timeout` or `500 Internal Server Error`.
-   **QA Relevance:** Timeouts are a critical part of performance and stability testing. You test that the API responds within acceptable limits. You also test how the client handles timeouts from the API (e.g., does it retry, display a user-friendly error?).

### 5. What is the difference between API and UI Testing?
They test different layers of the application and have different strengths.
-   **UI (User Interface) Testing:**
    -   **What:** Tests the graphical user interface. Simulates user interactions (clicks, typing, scrolling).
    -   **Tools:** Selenium WebDriver, Playwright, Cypress.
    -   **Focus:** End-to-end user flows, visual correctness, usability.
    -   **Pros:** Closest to how a user experiences the application.
    -   **Cons:** Slower, more brittle (UI changes frequently), more expensive to maintain, harder to debug.
-   **API (Application Programming Interface) Testing:**
    -   **What:** Tests the business logic and data layer directly, bypassing the UI. Sends requests to API endpoints and validates responses.
    -   **Tools:** REST-assured, Postman, JMeter.
    -   **Focus:** Data integrity, business rules, security, performance of the backend services.
    -   **Pros:** Faster, more stable (API contracts change less often than UI), easier to debug, more cost-effective.
    -   **Cons:** Doesn't cover UI-specific bugs (layout, rendering).

**Best Practice:** Build your testing pyramid. More API tests, fewer UI tests. API tests should cover most of your business logic. UI tests should focus on critical user journeys.

### 6. What is test runner file?
In Java testing frameworks, a test runner is the component that orchestrates the execution of your tests.
-   **TestNG:** The `testng.xml` file serves as the configuration for the TestNG runner. It defines which tests, classes, or groups to run, and how to run them (e.g., in parallel).
-   **Cucumber:** The "runner class" (a Java class annotated with `@RunWith(Cucumber.class)`) is the entry point. It uses `@CucumberOptions` to specify where to find `.feature` files and step definitions (`glue`), and how to generate reports.

### 7. What is the difference between Behaviour and Datadriven?
These describe different *aspects* of how tests are designed and executed.

-   **Behavior-Driven Testing (BDD):** Focuses on testing the *behavior* of the system from a user's perspective.
    -   **Language:** Uses Gherkin (`Given/When/Then`) to describe test scenarios in a human-readable format.
    -   **Goal:** Improved communication, living documentation, shared understanding of requirements.
    -   **Example:** "Given the user is on the login page, When the user enters valid credentials, Then the user should be redirected to the dashboard."

-   **Data-Driven Testing:** Focuses on separating test data from test logic.
    -   **Execution:** Runs the same test logic multiple times with different sets of input data and expected outputs.
    -   **Goal:** Efficiently test a wide range of inputs, reduce code duplication.
    -   **Example:** A single login test script reads usernames and passwords from an Excel sheet, running once for each row (valid, invalid, locked accounts).

**Can they be combined? Yes, absolutely.** BDD frameworks like Cucumber provide mechanisms (like `Scenario Outline` and `Data Tables`) to make their behavior-driven scenarios data-driven.

### 8. What is token generation?
Token generation is the process of creating a unique, often encrypted or cryptographically signed, string of characters (a "token") that represents a user's identity or authorization to perform certain actions.
-   **Authentication:** After a user logs in, the server generates an access token (e.g., a JWT - JSON Web Token). This token is then sent with every subsequent request to prove the user's identity without sending the password repeatedly.
-   **Security:** Tokens are typically short-lived and cryptographically secured to prevent tampering.
-   **QA Relevance:** In API testing, you often need to automate the token generation process (i.e., perform a login API call to get a token) and then use that token in the `Authorization` header of subsequent API requests.

### 9. What is SQL injection?
SQL injection is a type of cyber attack where malicious SQL code is injected into input fields to manipulate or compromise a database.
-   **How it works:** If an application doesn't properly sanitize user input, an attacker can enter SQL commands into a textbox. When the application uses this input to build a SQL query, the malicious code becomes part of the query, allowing the attacker to bypass authentication, retrieve sensitive data, or even delete the database.
-   **Example:** If a login query is `SELECT * FROM Users WHERE username = 'input_username' AND password = 'input_password';`
    An attacker might enter `username = 'admin'--` and `password = 'any_password'`.
    The query becomes `SELECT * FROM Users WHERE username = 'admin'--' AND password = 'any_password';`
    The `--` comments out the rest of the query, allowing the attacker to log in as admin.
-   **QA Relevance:** As a QA, you should perform **security testing** that includes testing for SQL injection vulnerabilities. You would provide various malicious SQL snippets in input fields and verify that the application correctly sanitizes the input and doesn't execute the malicious code.
