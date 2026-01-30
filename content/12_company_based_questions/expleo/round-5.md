---
title: "Expleo-5"
date: 2026-01-30
draft: false
---

---

## Original Questions

- Expleo interview questions
---------------------------
1.Cucumber framework explanation
2.Day to day activities
3.Agile methodologies
4.How will you run the failed testcases in cucumber
5.Regression testing
6.scenario  : you have a some missing information in recquirement you got only the heading and basic information but you didn't get the exact recquirement what you will do
7. Developer is not accepting the issue has a  bug that you had raised what you will do
8. You are not able to complete within the sprint what you will do
9.on TestNG how will you handle the failed test cases
10. Who will be conducting the sprint plan meeting what you will do on the meeting
11. When you will run your automation scripts
12. How will handle the dynamic webelement
13. There are 7 submit button  are available on the webpage. So what I want to click on the 7the click button what I want to do on this
14. What I need to do to scroll the webpage
15. Explain the POM
16. In your project where you had applied the OOP's Concept in java
17. Write the code to find the highest value in the array
18. The testcases that we had written for manual testing and the testcases that we write  on feature file will they both will show  duplicate
19. How will you confirm the checkbox is selected  or not in the webpage
20. Explain the HTTP methods in API and status codes
21. How will you validate the response in rest assured

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. Cucumber framework explanation
Cucumber is a BDD (Behavior-Driven Development) framework that enables collaboration between technical and non-technical stakeholders. It uses Gherkin (`Given/When/Then`) to describe application behavior in `.feature` files, which are then linked to executable code (step definitions) written in Java. This makes tests readable, serves as living documentation, and drives development based on shared understanding.

### 2. Day to day activities
Standard. Daily stand-up, test analysis/design, automation scripting, test execution, bug reporting/verification, team collaboration, framework maintenance.

### 3. Agile methodologies
Agile is an iterative, incremental approach to software development emphasizing flexibility, continuous delivery of value, and customer collaboration. It works in short cycles called sprints, promoting adaptability over rigid planning.

### 4. How will you run the failed testcases in cucumber
Cucumber tests are typically run via JUnit or TestNG.
-   **JUnit:** After a test run, JUnit can generate a list of failed tests.
-   **TestNG:** TestNG generates a `testng-failed.xml` file containing only the failed test cases. You can then execute this XML file to re-run only the failures.

### 5. Regression testing
Regression testing is the process of re-executing existing tests to ensure that recent code changes (new features, bug fixes) have not negatively impacted previously working functionality. It acts as a safety net to prevent new bugs from being introduced into stable parts of the application.

### 6. scenario : you have a some missing information in recquirement you got only the heading and basic information but you didn't get the exact recquirement what you will do
"My first action would be to **escalate this immediately** to the Product Owner and my Test Lead. It's crucial not to make assumptions or proceed with incomplete information, as this is a primary source of defects. I would:
1.  **Document the Gap:** Clearly identify and document what specific information is missing.
2.  **Seek Clarification:** Schedule a meeting with the Product Owner, Business Analyst, and potentially the developer to get the exact requirements.
3.  **Risk Assessment:** Discuss the impact of this missing information. If it's critical, the story might need to be re-estimated or even pulled from the current sprint until clarity is achieved."

### 7. Developer is not accepting the issue has a bug that you had raised what you will do
This is a test of collaboration and communication.
1.  **Understand their perspective:** Ask the developer to explain why they don't consider it a bug. There might be a misunderstanding of the requirements or application behavior.
2.  **Reproduce together:** The most effective step is to show them the bug live, ideally by reproducing it on their machine or a shared environment.
3.  **Refer to requirements:** Point to the specific acceptance criteria or requirement document that indicates the current behavior is incorrect.
4.  **Involve the Product Owner:** If there is still a disagreement on whether the behavior is expected or a defect, the Product Owner (who owns the requirements) is the ultimate arbiter.

### 8. You are not able to complete within the sprint what you will do
"If I realize I won't be able to complete my tasks within the sprint:
1.  **Communicate Early:** I would immediately communicate this to my Scrum Master and the rest of the team during the daily stand-up. Transparency is key.
2.  **Explain Why:** I would explain the reasons (e.g., unexpected complexity, blockers, higher priority work emerging).
3.  **Propose Solutions:** I would propose solutions or ask for help, such as:
    -   Pairing with another QA.
    -   Requesting help from a developer if it's a technical blocker.
    -   Discussing with the Product Owner about de-scoping the story or moving it to the next sprint if it's not a critical path.
The goal is to be proactive, not wait until the last day of the sprint."

### 9. on TestNG how will you handle the failed test cases
1.  **`testng-failed.xml`:** After a TestNG run, if there are failures, TestNG automatically generates a `testng-failed.xml` file. This XML file contains only the failed test cases, which can be run again separately.
2.  **`IRetryAnalyzer`:** For flakiness, TestNG provides the `IRetryAnalyzer` interface. You can implement a custom retry logic that automatically re-executes failed tests a specified number of times (e.g., 2 or 3 times) before marking them as a definitive failure. This is often applied globally via an `IAnnotationTransformer`.

### 10. Who will be conducting the sprint plan meeting what you will do on the meeting
The **Scrum Master** facilitates the Sprint Planning meeting, but the **Product Owner** leads by presenting the prioritized product backlog items, and the **Development Team** (including QA) is responsible for deciding what work can be committed to.

**My role (as QA):**
-   **Clarify Requirements:** Ask questions to ensure user stories are clear, testable, and have well-defined acceptance criteria.
-   **Estimate Testing Effort:** Provide estimates (in story points) for the testing tasks.
-   **Identify Risks:** Highlight potential risks or dependencies.
-   **Define Test Strategy:** Discuss the testing approach for the stories being committed.

### 11. When you will run your automation scripts
"Our automation scripts are run continuously throughout the development lifecycle:
-   **Locally:** During development for quick feedback and debugging.
-   **CI/CD Pipeline (Jenkins):**
    -   **On every code commit:** A subset of fast-running tests (smoke tests, unit tests) are executed.
    -   **Nightly/Scheduled:** The full regression suite runs against the QA or Staging environment."

### 12. How will handle the dynamic webelement
By using stable locators:
1.  **Stable Attributes:** Look for `name`, `value`, or custom `data-testid` attributes.
2.  **Partial Matches:** Use XPath `contains()` or `starts-with()` if only part of an attribute is dynamic (e.g., `//input[contains(@id, 'product-')]`).
3.  **XPath Axes:** Navigate from a stable parent or sibling (`following-sibling`, `ancestor`).
4.  **Relative Locators (Selenium 4):** Use `toLeftOf()`, `below()`, etc.

### 13. There are 7 submit button are available on the webpage. So what I want to click on the 7the click button what I want to do on this
1.  **`findElements` and Indexing:**
    ```java
    List<WebElement> buttons = driver.findElements(By.xpath("//button[@type='submit']"));
    if (buttons.size() >= 7) {
        buttons.get(6).click(); // 7th element is at index 6
    }
    ```
2.  **XPath Indexing (More precise):** If all buttons are identical but you know its specific position.
    `driver.findElement(By.xpath("(//button[@type='submit'])[7]")).click();`
3.  **Refine Locator:** Ideally, there would be a more semantic way to identify the 7th button (e.g., `text()`, specific data, or position relative to a label).

### 14. What I need to do to scroll the webpage
You use `JavascriptExecutor`.
-   **Scroll to a specific element:**
    `((JavascriptExecutor) driver).executeScript("arguments[0].scrollIntoView(true);", element);`
-   **Scroll to the top/bottom of the page:**
    `((JavascriptExecutor) driver).executeScript("window.scrollTo(0, document.body.scrollHeight)");` (to bottom)
    `((JavascriptExecutor) driver).executeScript("window.scrollTo(0, 0)");` (to top)

### 15. Explain the POM
Page Object Model is a design pattern that structures test automation code by creating a class for each page (or significant component) of the application. This class encapsulates all locators and interaction methods for that page, making tests maintainable, readable, and reusable.

### 16. In your project where you had applied the OOP's Concept in java
-   **Encapsulation:** Page Object Model (`private` locators, `public` methods).
-   **Abstraction:** `WebDriver` interface.
-   **Inheritance:** `BaseTest` and `BasePage` classes.
-   **Polymorphism:** Method overriding in page objects, or method overloading in utility classes.

### 17. Write the code to find the highest value in the array
```java
import java.util.Arrays;

public class MaxValueFinder {
    public static int findMax(int[] arr) {
        if (arr == null || arr.length == 0) {
            throw new IllegalArgumentException("Array cannot be empty or null.");
        }
        // Using Java 8 Streams
        return Arrays.stream(arr).max().getAsInt();
    }
}
```

### 18. The testcases that we had written for manual testing and the testcases that we write on feature file will they both will show duplicate
"Ideally, no, they shouldn't be exact duplicates.
-   **Manual Test Cases (in Jira/TCM):** Tend to be more detailed, covering pre-conditions, step-by-step actions, and expected results for human execution, often exploring edge cases.
-   **Feature Files (Cucumber):** Are higher-level, describing *behavior* from a business perspective. They act as acceptance criteria. The step definitions (Java code) behind them *implement* the automation.
While the underlying *logic* might be the same, the *representation* is different. A good practice is to link the feature file scenarios to the manual test cases in the TCM tool to ensure traceability without duplicating effort."

### 19. How will you confirm the checkbox is selected or not in the webpage
You use the `isSelected()` method of the `WebElement` interface.
`WebElement checkbox = driver.findElement(By.id("myCheckbox"));`
`boolean isChecked = checkbox.isSelected();`
`Assert.assertTrue(isChecked, "Checkbox is not selected.");`

### 20. Explain the HTTP methods in API and status codes
HTTP Methods: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`.
Status Codes: `2xx` (Success), `4xx` (Client Error), `5xx` (Server Error).

### 21. How will you validate the response in rest assured
In REST-assured, you use the `.then()` part of the fluent API chain:
-   **Status Code:** `response.then().statusCode(200);`
-   **Headers:** `response.then().header("Content-Type", "application/json");`
-   **Body Content (JSONPath):** `response.then().body("data.name", equalTo("John Doe"));`
-   **Schema Validation:** `response.then().body(matchesJsonSchemaInClasspath("userSchema.json"));`
-   **Response Time:** `response.then().time(lessThan(2000L));`
