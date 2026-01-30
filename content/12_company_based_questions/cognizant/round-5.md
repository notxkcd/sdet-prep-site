---
title: "Cognizant-5"
date: 2026-01-30
draft: false
---

---

## Original Questions

- Congnizant Level 2
--------------------
1) take xpath
2) explain get text and get the attribute
3) explain data driven framework
4) CI CD pipeline
5) for new application and defect retest,how you handle the testcases?
6) program for 2nd maximum

---

## Answers (No-BS Java QA / SDET Explanations)

### 1) take xpath
This is a practical question. The interviewer wants you to demonstrate how to write a good XPath for a given element. It's often followed by them pointing to an element on a shared screen.
-   **Approach:** "I would inspect the element using browser developer tools. I'd look for a unique and stable attribute like `id`, `name`, or a custom `data-*` attribute. If not available, I'd identify a stable parent or sibling and use relative XPath with axes or functions like `text()` or `contains()`."
-   **Example:** For a login button: `//button[@id='loginButton']` or `//button[text()='Login']` if text is unique.

### 2) explain get text and get the attribute
-   **`element.getText()`:** Retrieves the visible (rendered) inner text of a `WebElement`. It ignores any hidden text or text within child elements that are not displayed.
    -   Example: If HTML is `<div id="greeting">Hello <span>World</span></div>`, `driver.findElement(By.id("greeting")).getText()` returns "Hello World".
-   **`element.getAttribute(String attributeName)`:** Retrieves the value of a specific HTML attribute of a `WebElement`.
    -   Example: If HTML is `<a href="/home" id="homeLink">Home</a>`, `driver.findElement(By.id("homeLink")).getAttribute("href")` returns "/home".

### 3) explain data driven framework
A data-driven framework is an automation testing framework where the test data (inputs and expected outputs) is stored separately from the test script logic. The same test script is executed multiple times with different sets of data.
-   **Purpose:** To test various combinations of data, cover more scenarios, and reduce test script duplication.
-   **Implementation:** In Java with TestNG, this is typically done using the `@DataProvider` annotation, which reads data from external sources like JSON files, Excel sheets (via Apache POI), or databases.

### 4) CI CD pipeline
-   **CI (Continuous Integration):** A development practice where developers frequently merge their code changes into a central repository. Each merge automatically triggers a build and a comprehensive set of automated tests (unit, integration, UI regression). Goal: Early detection of integration bugs.
-   **CD (Continuous Delivery/Deployment):** The practice of automating the release process.
    -   **Continuous Delivery:** Ensures that every code change, after passing all automated tests, is reliably released to a production-like staging environment, ready for manual deployment to production at any time.
    -   **Continuous Deployment:** Automates the entire process, deploying every change that passes tests directly to production without human intervention.
-   **Pipeline:** A series of automated steps (stages) that code goes through from development to production (e.g., Build -> Test -> Deploy). Tools like Jenkins, GitLab CI, GitHub Actions are used to implement pipelines.

### 5) for new application and defect retest,how you handle the testcases?
-   **New Application:**
    1.  **Understand Requirements:** Collaborate with BA/PO, developers to clarify acceptance criteria.
    2.  **Test Strategy:** Determine what layers to test (unit, API, UI), and the mix of manual/automated.
    3.  **Test Case Design:** Write comprehensive manual test cases in a Test Case Management tool.
    4.  **Automation:** Prioritize automating critical, repetitive, and stable test cases for the UI and API layers.
    5.  **Exploratory Testing:** Perform manual exploratory testing to uncover unknown unknowns.
-   **Defect Retest:**
    1.  **Verify Fix:** Re-execute the specific test case(s) that initially failed to confirm the bug is resolved.
    2.  **Targeted Regression:** Run a small, focused set of automated tests on the affected area to ensure the fix hasn't introduced any localized regressions.
    3.  **Documentation:** Update the bug status in Jira (e.g., 'Ready for QA' -> 'Closed').

### 6) program for 2nd maximum
```java
import java.util.Arrays;
import java.util.Comparator;

public class SecondMaximum {
    public static int findSecondMaximum(int[] arr) {
        if (arr == null || arr.length < 2) {
            throw new IllegalArgumentException("Array must contain at least two elements.");
        }
        return Arrays.stream(arr)
                     .distinct() // Remove duplicates
                     .boxed()    // Convert to Stream<Integer>
                     .sorted(Comparator.reverseOrder()) // Sort in descending order
                     .skip(1)    // Skip the largest element
                     .findFirst()// Get the next element
                     .orElseThrow(() -> new IllegalStateException("Array does not have a second distinct maximum value."));
    }
}
```
This is a standard interview question to check knowledge of streams and collections.
