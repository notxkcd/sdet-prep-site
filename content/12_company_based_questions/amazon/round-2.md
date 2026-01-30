---
title: "Amazon-2"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

Amazon level 1:
----------------
1.What are the status you will see in jira
2.Name some bug resolution that you see
3. How will you perform the click the action in selenium
4. How will you write the manual test case and automation
5. Agile methadoligies
6. Who will give you the recquirement
7. Locators in selenium 
8. Xpath axes
9. Java code Reverse the string 
10. Webdriver and webelement methods
Amazon Level 2:
---------------
1.project explanation 
2.palindrome java code
3.selenium locators
4. Explain Test cases
5.why we need a components
6.write the syntax for the axes xpath
7.Scenario and scenario outline
8.cucumber framework Explanation
9.what are the steps you will follow to automate

---

## Answers (No-BS Java QA / SDET Explanations)

### Amazon Level 1

#### 1. What are the status you will see in jira
Common Jira statuses for a bug or task:
-   **Open/New:** The issue has been created.
-   **In Progress:** Someone is actively working on the issue.
-   **Resolved/Fixed:** The issue has been addressed by a developer (for bugs) or the task is completed.
-   **Ready for QA/Verification:** The issue is ready for the QA team to verify the fix or completion.
-   **Closed:** The issue has been verified and is no longer active.
-   **Reopened:** A resolved bug has been re-verified and found to still exist.
-   **Deferred:** The issue is valid but will be addressed in a future release.

#### 2. Name some bug resolution that you see
Common Jira bug resolutions:
-   **Fixed:** The bug has been fixed.
-   **Won't Fix:** The bug is acknowledged but will not be fixed (e.g., low priority, not enough impact).
-   **Duplicate:** The bug report is a duplicate of an existing one.
-   **Cannot Reproduce:** The QA team or developer cannot reproduce the bug based on the steps provided.
-   **Works as Designed:** The reported behavior is actually the intended functionality.
-   **Deferred:** The bug is postponed to a future release.

#### 3. How will you perform the click the action in selenium
1.  **`element.click()`:** The most common and direct way.
2.  **`Actions` class:** For complex clicks, like right-click or double-click, or if a regular click is being intercepted. `new Actions(driver).click(element).perform();`
3.  **`JavascriptExecutor`:** As a last resort, if `element.click()` fails, you can force a click using JavaScript. `((JavascriptExecutor) driver).executeScript("arguments[0].click();", element);`

#### 4. How will you write the manual test case and automation
-   **Manual Test Case:** Documented in a Test Case Management tool (like Jira/Xray or TestRail). It includes ID, title, preconditions, step-by-step actions, and expected results. Focuses on human execution.
-   **Automation Test Case:** An executable script (e.g., a TestNG `@Test` method or a Cucumber scenario + step definition). It automates the steps of a manual test case.

#### 5. Agile methadoligies
Agile is an iterative approach to software development emphasizing flexibility, collaboration, and rapid delivery of working software. Key methodologies include Scrum, Kanban, XP. Scrum involves sprints, daily stand-ups, sprint planning, review, and retrospective.

#### 6. Who will give you the recquirement
The **Product Owner** (or Product Manager/Business Analyst) is typically responsible for providing and clarifying requirements. They act as the voice of the customer and prioritize the product backlog.

#### 7. Locators in selenium
The 8 standard strategies: `id`, `name`, `className`, `tagName`, `linkText`, `partialLinkText`, `cssSelector`, `xpath`.

#### 8. Xpath axes
XPath axes allow you to navigate the HTML DOM tree relative to a selected element. Examples: `parent::`, `ancestor::`, `following-sibling::`, `preceding-sibling::`, `child::`, `descendant::`.

#### 9. Java code Reverse the string
`new StringBuilder(str).reverse().toString();`

#### 10. Webdriver and webelement methods
-   **`WebDriver` Methods:** `get()`, `findElement()`, `getTitle()`, `getCurrentUrl()`, `quit()`, `switchTo().alert()`, `manage().timeouts()`.
-   **`WebElement` Methods:** `click()`, `sendKeys()`, `getText()`, `getAttribute()`, `isDisplayed()`, `isEnabled()`, `isSelected()`, `clear()`, `submit()`.

### Amazon Level 2

#### 1. project explanation
Standard.

#### 2. palindrome java code
A palindrome reads the same forwards and backwards.
```java
public boolean isPalindrome(String str) {
    if (str == null) return false;
    String cleaned = str.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
    String reversed = new StringBuilder(cleaned).reverse().toString();
    return cleaned.equals(reversed);
}
```

#### 3. selenium locators
(Repeated) `id`, `name`, `className`, `tagName`, `linkText`, `partialLinkText`, `cssSelector`, `xpath`.

#### 4. Explain Test cases
A test case is a set of actions and conditions executed to verify a specific functionality. It includes a unique ID, title, preconditions, steps to execute, expected results, and postconditions.

#### 5. why we need a components
This is ambiguous. If referring to "Page Objects" as components:
"We need components (like Page Objects) in our test framework to organize our code, make it reusable, and improve maintainability. Each component (page or reusable UI module) has its own class that encapsulates its locators and actions. This adheres to the DRY (Don't Repeat Yourself) principle and makes our test scripts cleaner and more resilient to UI changes."

#### 6. write the syntax for the axes xpath
Example: `//div[@id='parent-element']/child::input` or `//label[text()='Username']/following-sibling::input`.

#### 7. Scenario and scenario outline
-   **`Scenario`:** A single, concrete test case in Cucumber.
-   **`Scenario Outline`:** A data-driven template for a scenario, using an `Examples` table to run multiple times with different data.

#### 8. cucumber framework Explanation
(Repeated) BDD, Gherkin, Feature Files, Step Definitions, Runner Class, Hooks.

#### 9. what are the steps you will follow to automate
1.  **Understand the User Story/Requirements:** Clarify the acceptance criteria.
2.  **Identify Test Cases:** Convert requirements into specific test scenarios.
3.  **Prioritize for Automation:** Choose which test cases are most suitable for automation based on criticality, repetitiveness, and stability.
4.  **Test Data Preparation:** Prepare or generate necessary test data.
5.  **Develop Automation Script:**
    -   Identify locators for UI elements.
    -   Write Page Object methods for UI interactions or API client methods for API calls.
    -   Write the actual test script (e.g., TestNG `@Test` or Cucumber scenario).
    -   Implement assertions.
6.  **Review and Refactor:** Ensure code quality, reusability, and maintainability.
7.  **Integrate with CI/CD:** Add the new tests to the automated build/release pipeline.
