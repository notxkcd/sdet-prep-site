---
title: "Infosys-3"
date: 2026-01-30
draft: false
---

---

## Original Questions

- Infosys virtual
---------------
1.Tell about yourself
2.How many years experience in automation
3.are you work within jira what will do in jira
4.cucumber hook class
5.experience in testng 6.explain testng annotations
7.what methodology  you use in your project
8.explain agile methodologies 
9.write a swap the numbers with using variable and explain that
10.which client in your project
11.which kind application you will be work

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. Tell about yourself
Standard opening. Concise, professional, focus on relevant experience.

### 2. How many years experience in automation
State your actual experience here. "I have X years of experience primarily focused on test automation, covering both UI and API testing using Java-based frameworks."

### 3. are you work within jira what will do in jira
"Yes, I work extensively with Jira. My activities in Jira include:
-   **Bug Reporting:** Creating detailed bug tickets, including steps to reproduce, expected/actual results, and attachments.
-   **Test Case Management:** (Using plugins like Xray or Zephyr) Creating and linking test cases to user stories, tracking test execution status.
-   **Story/Task Management:** Updating my progress on user stories and tasks within the sprint.
-   **Workflow Management:** Moving tickets through their defined workflow (e.g., from 'To Do' to 'In Progress' to 'Done').
-   **Reporting:** Monitoring dashboards for test progress and defect trends."

### 4. cucumber hook class
A Cucumber hook class contains methods annotated with `@Before` or `@After` (and `@BeforeStep`, `@AfterStep`). These methods run at specific points in the test execution lifecycle.
-   **Purpose:** To manage setup (e.g., initializing `WebDriver`, setting up test data) and teardown (e.g., quitting `WebDriver`, taking screenshots on failure, cleaning up test data) operations for scenarios.
-   **Example:** A `@Before` hook to launch a browser before each scenario, and an `@After` hook to close it.

### 5. experience in testng explain testng annotations
"I have extensive experience with TestNG. It's my primary test runner for Java automation. I use its powerful annotations to control the test lifecycle and execution flow.
-   **`@Test`:** Marks a method as a test case.
-   **`@BeforeSuite`, `@AfterSuite`:** For global setup/teardown once per test suite.
-   **`@BeforeClass`, `@AfterClass`:** For setup/teardown once per test class.
-   **`@BeforeMethod`, `@AfterMethod`:** For setup/teardown before/after each test method (critical for isolating tests and managing `WebDriver`).
-   **`@DataProvider`:** For data-driven testing.
-   **`@Parameters`:** For passing parameters from `testng.xml`."

### 7. what methodology you use in your project
"We follow the **Agile methodology**, specifically **Scrum**. We work in two-week sprints, focusing on continuous delivery of small, working increments of software."

### 8. explain agile methodologies
Agile is an iterative and incremental approach to software development. It values:
-   Individuals and interactions over processes and tools.
-   Working software over comprehensive documentation.
-   Customer collaboration over contract negotiation.
-   Responding to change over following a plan.
Common methodologies within Agile include Scrum, Kanban, and XP.

### 9. write a swap the numbers with using variable and explain that
This usually refers to swapping two numbers without using a *third* (temporary) variable.

```java
public class NumberSwapper {
    public static void swap(int a, int b) {
        System.out.println("Before swap: a = " + a + ", b = " + b);
        a = a + b; // a now holds the sum of original a and b
        b = a - b; // b now holds (original a + original b) - original b = original a
        a = a - b; // a now holds (original a + original b) - original a = original b
        System.out.println("After swap: a = " + a + ", b = " + b);
    }
}
```

### 10. which client in your project
Be specific about the client or industry if possible and if not under NDA. "My project was for a major client in the financial services sector, specifically a global investment bank."

### 11. which kind application you will be work
"I primarily work on **web-based enterprise applications**. This includes complex web UI applications and backend RESTful APIs. I also have some experience with mobile web testing."
(If you have mobile native app experience, mention that too).
