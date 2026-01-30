---
title: "IBM-2"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

- IBM interview questions
------------------------
Tell about your self
Api status code
Write a Bdd feature  file for train booking scenario
Tell Testng annotations and explain
Roles and responsibilities 
Tell about sprint retrospective 
What doing in sprnit planning
How do pass data excelsheet what method we use
Explain the bug cycle or defect cycle
Explain your project
Any bug in your project what you do

---

## Answers (No-BS Java QA / SDET Explanations)

### Tell about your self
Standard opener. Keep it concise, professional, and focus on your relevant experience (automation skills, tech stack, achievements).

### Api status code
HTTP status codes are returned by web servers to indicate the status of an API request.
-   **2xx (Success):** Request was successfully received and processed (`200 OK`, `201 Created`).
-   **4xx (Client Error):** The client made an error in the request (`400 Bad Request`, `401 Unauthorized`, `404 Not Found`).
-   **5xx (Server Error):** The server encountered an error while processing a valid request (`500 Internal Server Error`, `503 Service Unavailable`).

### Write a Bdd feature file for train booking scenario
```gherkin
Feature: Train Ticket Booking

  Scenario: User books a train ticket successfully
    Given a user is logged into the "RailBook" application
    And the user has searched for a train from "New York" to "Boston" on "tomorrow"
    When the user selects a train and class "Economy"
    And the user provides passenger details
    And the user completes the payment process
    Then a booking confirmation message should be displayed
    And the user should receive an email with ticket details
```

### Tell Testng annotations and explain
TestNG annotations control how tests are executed.
-   `@Test`: Marks a method as a test case.
-   `@BeforeMethod`, `@AfterMethod`: Run before/after each test method. Ideal for test setup/teardown.
-   `@BeforeClass`, `@AfterClass`: Run once before/after all tests in a class.
-   `@BeforeSuite`, `@AfterSuite`: Run once before/after all tests in the entire suite.
-   `@DataProvider`: Provides data to test methods for data-driven testing.

### Roles and responsibilities
Be specific about your daily tasks: framework development, test scripting (UI/API), CI/CD integration, bug reporting, and team collaboration.

### Tell about sprint retrospective
A meeting held at the end of each Agile sprint where the team discusses:
-   What went well in the sprint?
-   What could have gone better?
-   What specific actions can be taken to improve the process in the next sprint?
It's crucial for continuous improvement.

### What doing in sprnit planning
This refers to **Sprint Planning** meeting.
"In Sprint Planning, the team collaborates to select user stories from the product backlog to work on in the upcoming sprint. As QA, I contribute by:
-   **Clarifying Requirements:** Asking questions to ensure I fully understand the acceptance criteria.
-   **Identifying Dependencies:** Highlighting any external dependencies that could impact testing.
-   **Estimating Testing Effort:** Providing estimates (in story points) for the testing tasks related to each story.
-   **Defining Test Strategy:** Discussing the testing approach for each story within the sprint."

### How do pass data excelsheet what method we use
You use the **Apache POI** library in Java to read data from Excel files (`.xlsx` or `.xls`). The data is typically extracted into a 2D `Object[][]` array, which can then be returned by a TestNG `@DataProvider` method to feed data into your tests.

### Explain the bug cycle or defect cycle
The workflow a bug goes through from discovery to resolution:
1.  **New:** Bug reported by QA.
2.  **Open/Assigned:** Bug is reviewed and assigned to a developer.
3.  **Fixed:** Developer resolves the bug in code.
4.  **Ready for QA/Verify:** Fix is deployed to test environment, ready for QA to retest.
5.  **Closed:** QA verifies the fix and closes the bug.
6.  **Reopened:** If QA finds the bug is not fixed, it's sent back to the developer.

### Explain your project
Standard. Describe the project domain, your role, automation framework (tools, architecture), challenges, and achievements.

### Any bug in your project what you do
"If I find a bug in my project:
1.  **Reproduce:** I first try to reproduce it consistently and ensure it's not a known issue or a false positive.
2.  **Report:** I log a detailed bug report in Jira, including clear steps to reproduce, expected vs. actual results, environment details, and attach screenshots/logs.
3.  **Triage:** I assign a severity level to the bug.
4.  **Communicate:** I notify the development team and product owner about critical bugs.
5.  **Verify:** Once the bug is fixed, I retest it to confirm the fix and then perform a targeted regression to ensure no new issues were introduced."
