---
title: "TestNG Interview Questions"
date: 2026-01-30
draft: false
categories: ["TestNG"]
---

## Beginner (Annotations & Basics)
1. [What is TestNG and explain why and where it is required?](#1-what-is-testng-and-explain-why-and-where-it-is-required)
2. [What are the advantages of TestNG?](#2-what-are-the-advantages-of-testng)
3. [What are the common annotations you handle in your project?](#3-what-are-the-common-annotations-you-handle-in-your-project)
4. [Explain the TestNG annotations in detail?](#4-explain-the-testng-annotations-in-detail)
5. [What is the execution order of TestNG annotations?](#5-what-is-the-execution-order-of-testng-annotations)
6. [Write the hierarchy of annotations in TestNG?](#6-write-the-hierarchy-of-annotations-in-testng)
7. [What is the purpose of the `@Test` annotation?](#7-what-is-the-purpose-of-the-test-annotation)
8. [Do you know TestNG?](#8-do-you-know-testng)

## Intermediate (Configuration & Data)
1. [What is the use of the `testng.xml` file?](#testng-xml-use)
2. [What is the sequence used in `testng.xml`?](#testng-xml-sequence)
3. [What is a Data Provider in TestNG?](#dataprovider-concept)
4. [How do you perform parameterization in TestNG?](#parameterization)
5. [How do you pass test data in TestNG?](#pass-test-data)
6. [Difference between `@Parameters` and `@DataProvider`?](#parameters-vs-dataprovider)
7. [What are listeners in TestNG and how do you use them?](#listeners-testng)
8. [What types of reports can be generated in TestNG?](#testng-reports)
9. [How do you generate reports in TestNG?](#generate-reports)
10. [How do you run a single test case multiple times in TestNG?](#run-test-multiple-times)
11. [How do you skip or ignore a particular test case in TestNG?](#ignore-skip-test)
12. [Difference between TestNG and Cucumber?](#testng-vs-cucumber)
13. [Difference between TestNG and JUnit?](#testng-vs-junit)

## Advanced (Logic & Execution)
1. [How do you set priority in TestNG?](#set-priority)
2. [If there is no priority set, how will the tests run?](#no-priority-logic)
3. [How do you handle failed test cases in TestNG?](#handle-failed-tests)
4. [How do you rerun failed test cases in TestNG?](#rerun-failed-tests)
5. [Explain the difference between `dependsOnMethods` and `dependsOnGroups`?](#depends-on-methods-groups)
6. [How do you perform parallel execution in TestNG?](#parallel-execution)
7. [Explain soft assertions and hard assertions?](#soft-vs-hard-assertions)
8. [Scenario: You have two `@Test` methods, which one will run first?](#two-test-order)
9. [How do you group tests in TestNG?](#grouping-tests)
10. [What logic is used in the `@BeforeTest` annotation?](#beforetest-logic)

---

## Questions with Answers

### Beginner (Annotations & Basics) - Answers

### 1. What is TestNG and explain why and where it is required? {#1-what-is-testng-and-explain-why-and-where-it-is-required}
**Answer**: TestNG (Test Next Generation) is a testing framework for Java inspired by JUnit. It is required for advanced test automation, providing features like grouping, sequencing, and data-driven testing.

### 2. What are the advantages of TestNG? {#2-what-are-the-advantages-of-testng}
**Answer**:
- Flexible test configuration.
- Support for Data-Driven Testing (via `@DataProvider`).
- Parallel test execution.
- Powerful reporting.
- Easy grouping and prioritization.

### 3. What are the common annotations you handle in your project? {#3-what-are-the-common-annotations-you-handle-in-your-project}
**Answer**: I frequently use `@Test`, `@BeforeMethod`, `@AfterMethod`, `@BeforeClass`, and `@DataProvider`.

### 4. Explain the TestNG annotations in detail? {#4-explain-the-testng-annotations-in-detail}
**Answer**: Annotations guide the execution flow. Examples: `@BeforeSuite` runs once per suite; `@BeforeMethod` runs before every single `@Test` case.

### 5. What is the execution order of TestNG annotations? {#5-what-is-the-execution-order-of-testng-annotations}
**Answer**:
1. `@BeforeSuite`
2. `@BeforeTest`
3. `@BeforeClass`
4. `@BeforeMethod`
5. **`@Test`**
6. `@AfterMethod`
7. `@AfterClass`
8. `@AfterTest`
9. `@AfterSuite`

### 6. Write the hierarchy of annotations in TestNG? {#6-write-the-hierarchy-of-annotations-in-testng}
**Answer**: (Same as the execution order listed above).

### 7. What is the purpose of the `@Test` annotation? {#7-what-is-the-purpose-of-the-test-annotation}
**Answer**: It marks a Java method as a **test case**. It is the primary building block of a TestNG suite.

### 8. Do you know TestNG? {#8-do-you-know-testng}
**Answer**: Yes, I have used TestNG for the past 3 years to build and execute automated test suites.

### Intermediate (Configuration & Data) - Answers

### 1. What is the use of the `testng.xml` file? {#testng-xml-use}
**Answer**: It is used to define and execute test suites. It allows you to group classes, include/exclude methods, set execution priority, and enable parallel testing.

### 2. What is the sequence used in `testng.xml`? {#testng-xml-sequence}
**Answer**: `<suite>` -> `<test>` -> `<classes>` -> `<class>` -> `<methods>` -> `<include/exclude>`.

### 3. What is a Data Provider in TestNG? {#dataprovider-concept}
**Answer**: A method annotated with `@DataProvider` that returns a 2D array of objects. It allows you to run the same test method multiple times with different data sets.

### 4. How do you perform parameterization in TestNG? {#parameterization}
**Answer**:
1. Using the `@Parameters` annotation (values provided in `testng.xml`).
2. Using the `@DataProvider` annotation (values provided in code).

### 5. How do you pass test data in TestNG? {#pass-test-data}
**Answer**: Primarily through the `@DataProvider` method or by reading values from the `testng.xml` file.

### 6. Difference between `@Parameters` and `@DataProvider`? {#parameters-vs-dataprovider}
**Answer**:
- **`@Parameters`**: Best for simple, static data (like browser name) provided in XML.
- **`@DataProvider`**: Best for complex, dynamic data sets (like multiple user logins).

### 7. What are listeners in TestNG? {#listeners-testng}
**Answer**: Listeners are interfaces (like `ITestListener`) that allow you to modify TestNG behavior. I use them to take screenshots on test failure.

### 8. What types of reports can be generated in TestNG? {#testng-reports}
**Answer**: Default HTML reports, Emailable reports, and XML reports. I also integrate **Extent Reports** for better visuals.

### 9. How do you generate reports in TestNG? {#generate-reports}
**Answer**: Reports are automatically generated in the `test-output` folder after execution.

### 10. How do you run a single test case multiple times in TestNG? {#run-test-multiple-times}
**Answer**: By using the `invocationCount` attribute in the `@Test` annotation: `@Test(invocationCount = 5)`.

### 11. How do you skip or ignore a particular test case in TestNG? {#ignore-skip-test}
**Answer**:
- **Skip**: Use `throw new SkipException("reason");` in the code.
- **Ignore**: Set `enabled = false` in the `@Test` annotation.

### 12. Difference between TestNG and Cucumber? {#testng-vs-cucumber}
**Answer**:
- **TestNG**: A testing framework focused on technical logic and annotations.
- **Cucumber**: A BDD tool focused on collaboration and human-readable English scenarios.

### 13. Difference between TestNG and JUnit? {#testng-vs-junit}
**Answer**: TestNG is more advanced, offering grouping, prioritization, dependency testing, and built-in parallel execution, which were missing in older JUnit versions.

### Advanced (Logic & Execution) - Answers

### 1. How do you set priority in TestNG? {#set-priority}
**Answer**: By using the `priority` attribute: `@Test(priority = 1)`. Lower values (including negative) run first.

### 2. If there is no priority set, how will the tests run? {#no-priority-logic}
**Answer**: Tests will run in **alphabetical order** by their method name.

### 3. How do you handle failed test cases in TestNG? {#handle-failed-tests}
**Answer**: By using **Listeners** to capture screenshots and logs, and **Assertions** to provide clear failure messages.

### 4. How do you rerun failed test cases in TestNG? {#rerun-failed-tests}
**Answer**: Run the `testng-failed.xml` file generated in the `test-output` folder, or implement the `IRetryAnalyzer` interface.

### 5. Difference between `dependsOnMethods` and `dependsOnGroups`? {#depends-on-methods-groups}
**Answer**:
- **`dependsOnMethods`**: A test method waits for a specific method to pass.
- **`dependsOnGroups`**: A test method waits for an entire group of tests to pass.

### 6. How do you perform parallel execution in TestNG? {#parallel-execution}
**Answer**: In `testng.xml`, set the `parallel` attribute in the `<suite>` tag (e.g., `parallel="methods"`) and define the `thread-count`.

### 7. Explain soft assertions and hard assertions? {#soft-vs-hard-assertions}
**Answer**:
- **Hard Assert**: Stops the test immediately on failure.
- **Soft Assert**: Continues the test execution even if an assertion fails, reporting all failures at the end using `assertAll()`.

### 8. Scenario: You have two `@Test` methods, which one will run first? {#two-test-order}
**Answer**: If priorities are the same or not set, they will run in alphabetical order. Otherwise, the one with the lower priority value runs first.

### 9. How do you group tests in TestNG? {#grouping-tests}
**Answer**: Using the `groups` attribute: `@Test(groups = {"smoke", "regression"})`. You can then run specific groups via `testng.xml`.

### 10. What logic is used in the `@BeforeTest` annotation? {#beforetest-logic}
**Answer**: It is used for configuration that needs to run before any test method belonging to the `<test>` tag in `testng.xml`, such as opening a database connection.