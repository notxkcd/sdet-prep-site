---
title: "Intech_hud-2"
date: 2026-01-30
draft: false
---

---

## Original Questions

- Intech hud Virtual Interview:-
-----------------------------
1.Tell About Your Self 
2.Difference Manual testcase and Test Scenario 
3.What is Entry and Exit Criteria in testing 
4.Difference between Functional and non functional testing
5.Write Testcase for facebook login page
6.Explain OOPS concept in java
7.Explain Abstraction
8.What are the annotations in TestNG

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. Tell About Your Self
Standard opener. Keep it concise, professional, and highlight your relevant experience and skills.

### 2. Difference Manual testcase and Test Scenario
-   **Test Case:** A detailed, step-by-step set of instructions for verifying a specific functionality. It includes preconditions, a sequence of actions, and expected results. Test cases are precise and granular.
-   **Test Scenario:** A high-level description of a particular user interaction or a functionality to be tested. It focuses on *what* to test, not *how*. A single test scenario can often be broken down into multiple test cases. In BDD, Cucumber's `Scenario` keyword represents a test scenario.

### 3. What is Entry and Exit Criteria in testing
-   **Entry Criteria:** Conditions that must be met before starting a specific testing phase. Failing to meet these can lead to inefficient testing.
    -   **Examples:** Test plan approved, test environment ready, test data available, build deployed and smoke tested successfully.
-   **Exit Criteria:** Conditions that must be met before completing a specific testing phase or ending testing altogether.
    -   **Examples:** All critical/high priority test cases executed, X% of test cases passed, no high-priority bugs open, test coverage achieved, test summary report approved.

### 4. Difference between Functional and non functional testing
-   **Functional Testing:** Verifies that the system performs its specified functions according to the requirements. It checks *what* the system does.
    -   Examples: Unit testing, integration testing, system testing, acceptance testing, regression testing.
-   **Non-Functional Testing:** Verifies *how well* the system performs. It checks non-functional requirements.
    -   Examples: Performance testing (load, stress), security testing, usability testing, compatibility testing, reliability testing.

### 5. Write Testcase for facebook login page
**Test Case ID:** TC_FB_LOGIN_001
**Title:** Verify successful login to Facebook with valid credentials.

**Preconditions:**
1.  User has a valid Facebook account (username: `testuser@example.com`, password: `Password123!`).
2.  Browser is open and navigated to `https://www.facebook.com/`.

**Steps:**
1.  Enter `testuser@example.com` into the "Email or phone" field.
2.  Enter `Password123!` into the "Password" field.
3.  Click the "Log in" button.

**Expected Results:**
-   User is successfully redirected to their Facebook news feed or home page.
-   The user's profile picture/name is visible in the top navigation bar.
-   No error messages are displayed.

### 6. Explain OOPS concept in java
The four pillars of Object-Oriented Programming:
-   **Encapsulation:** Bundling data and methods into a single unit (class), controlling access to data.
-   **Abstraction:** Hiding complex implementation details, showing only essential features.
-   **Inheritance:** Creating new classes based on existing ones, promoting code reuse.
-   **Polymorphism:** Allowing objects to take on many forms, enabling methods to behave differently based on the object type.

### 7. Explain Abstraction
Abstraction is the concept of simplifying a complex system by hiding its complex implementation details and exposing only the necessary functionalities. In Java, this is primarily achieved through **abstract classes** and **interfaces**. The `WebDriver` interface in Selenium is a prime example: you interact with its methods (`get()`, `findElement()`) without needing to know how `ChromeDriver` or `FirefoxDriver` implements them internally.

### 8. What are the annotations in TestNG
TestNG annotations are special markers that provide metadata about methods and classes, controlling how TestNG executes tests.
-   **`@Test`:** Marks a method as a test case.
-   **Configuration Annotations:** `@BeforeSuite`, `@AfterSuite`, `@BeforeTest`, `@AfterTest`, `@BeforeClass`, `@AfterClass`, `@BeforeMethod`, `@AfterMethod`. These define setup and teardown logic at different levels.
-   **Data Annotations:** `@DataProvider` (to supply test data), `@Parameters` (to receive data from `testng.xml`).
-   **Utility Annotations:** `@Listeners` (to register event listeners).
