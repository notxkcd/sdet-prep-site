---
title: "Expleo-4"
date: 2026-01-30
draft: false
---

---

## Original Questions

Expleo L1
----------
1.Introduce yourself 
2.Explain your project in detail
3.Regression testing vs sanity
4.what you will do in a splint 
5.java program - 100/8 need to print all the dividend of 8 in the console.
6.Selenium - how will you handle windows, alert, get, navigate,wait concept 
7.complete explanation of cucumber framework 
8.more about previous project 
9.making domain question ( how will you validate the range of age limit and how will you validate the account balance)
10. Basic about sql

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. Introduce yourself
Standard opener. Keep it concise, professional, and focus on your automation experience, tech stack, and achievements.

### 2. Explain your project in detail
Standard. Focus on the application's domain, your role, the architecture of your automation framework, the challenges you faced, and your specific contributions and achievements. Be ready to deep-dive into any aspect.

### 3. Regression testing vs sanity
-   **Regression Testing:** A broad, comprehensive test suite run after any code changes to ensure existing functionality remains unbroken.
-   **Sanity Testing:** A narrow, quick test on a small functional area after a change or fix to verify the change works and hasn't introduced immediate issues.

### 4. what you will do in a splint
This refers to a **Sprint** in Agile.
"During a sprint, my main activities as a QA automation engineer include:
-   **Daily Stand-ups:** Reporting progress and blockers.
-   **Test Analysis and Design:** Reviewing user stories, clarifying requirements, and designing test cases (manual and automated).
-   **Automation Scripting:** Writing new automated tests for the features in the current sprint.
-   **Test Execution:** Running automated test suites against new builds and performing exploratory testing on completed features.
-   **Defect Management:** Identifying, reporting, and tracking bugs.
-   **Collaboration:** Working closely with developers and product owners.
-   **Retrospectives:** Participating in discussions to improve our processes."

### 5. java program - 100/8 need to print all the dividend of 8 in the console.
This means printing multiples of 8 up to 100.

```java
public class MultiplesOfEight {
    public static void main(String[] args) {
        for (int i = 8; i <= 100; i += 8) {
            System.out.println(i);
        }
    }
}
```

### 6. Selenium - how will you handle windows, alert, get, navigate,wait concept
-   **Windows:** Use `driver.getWindowHandles()` to get all window IDs and `driver.switchTo().window(handle)` to switch focus.
-   **Alert:** Use `driver.switchTo().alert()` to interact with native JavaScript alerts (`accept()`, `dismiss()`, `getText()`).
-   **`get(url)`:** Navigates to a URL and waits for the page to load. `driver.get("https://example.com");`
-   **`navigate()`:** Provides methods to go back, forward, refresh, and `to()` a URL. `driver.navigate().back();`
-   **Wait Concept:** Essential for synchronization. Use **Explicit Waits** (`WebDriverWait` with `ExpectedConditions`) to wait for specific conditions to be met before interacting with elements.

### 7. complete explanation of cucumber framework
Cucumber is a BDD framework.
-   **Purpose:** To improve collaboration by defining application behavior in human-readable Gherkin (`Given/When/Then`) in `.feature` files.
-   **Components:** Feature Files, Step Definitions (Java methods implementing Gherkin steps), Runner Class (to execute tests), and Hooks (for setup/teardown).
-   **Workflow:** Runner reads features, maps steps to Java code, executes code, generates reports.

### 8. more about previous project
Standard. Be ready to discuss the project in depth, including specific test scenarios, challenges, and your contributions.

### 9. making domain question ( how will you validate the range of age limit and how will you validate the account balance)
-   **Validate Age Limit Range (e.g., 18-65):**
    -   **UI:** Enter values like 17, 18, 19, 65, 66 into the age field. Verify error messages for out-of-range values and acceptance for in-range values.
    -   **API:** Send requests with age values at the boundaries and just outside them. Verify the API returns correct validation errors or processes valid ages.
    -   **DB:** Check that only valid ages are stored in the database.
-   **Validate Account Balance:**
    -   **UI:** Display the balance on screen.
    -   **API:** Make an API call to retrieve the account balance.
    -   **DB:** Query the database directly to get the actual balance.
    -   **Assertion:** Compare the UI/API displayed balance with the database value. Crucial for financial applications. Test positive, negative, and zero balances.

### 10. Basic about sql
SQL (Structured Query Language) is the standard language for managing and querying relational databases. Key commands:
-   `SELECT`: Retrieve data.
-   `INSERT`: Add new data.
-   `UPDATE`: Modify existing data.
-   `DELETE`: Remove data.
-   `JOIN`: Combine data from multiple tables.
In QA, used for test data setup/cleanup and backend verification.
