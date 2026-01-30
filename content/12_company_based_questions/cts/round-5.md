---
title: "CTS-5"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

CTS L1 virtual:
===============
1. Tell me about yourself, previous projects and roles and responsibilities.
2. Tell me 5 Interface in Selenium
3. common exceptions you have faced in selenium
4. write an xpath syntax
5. how will you handle alert?
6. difference between / and //
7. write a java program to find the maximum salary of an individual

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. Tell me about yourself, previous projects and roles and responsibilities.
Standard opener. Structure your answer:
1.  **Yourself:** "I'm a QA Automation Engineer with X years of experience, specializing in Java-based test automation for web applications."
2.  **Previous Projects:** "I've worked on projects in the e-commerce and FinTech domains. My last project involved automating the end-to-end testing of a customer-facing financial dashboard."
3.  **Roles & Responsibilities:** "My core responsibilities included designing and maintaining the automation framework using Selenium and TestNG, writing UI and API tests, integrating our test suites into a Jenkins CI/CD pipeline, and collaborating with the development team to triage and resolve defects."

### 2. Tell me 5 Interface in Selenium
1.  **`WebDriver`:** The main interface for browser automation. (`driver = new ChromeDriver();`)
2.  **`WebElement`:** Represents an HTML element on the page.
3.  **`SearchContext`:** The super-interface for `WebDriver` and `WebElement` that defines the `findElement()` and `findElements()` methods.
4.  **`TakesScreenshot`:** An interface that allows the driver to capture screenshots.
5.  **`JavascriptExecutor`:** An interface for executing JavaScript code within the browser context.

### 3. common exceptions you have faced in selenium
-   **`NoSuchElementException`:** `findElement()` could not find the element. Caused by an incorrect locator or a timing issue.
-   **`StaleElementReferenceException`:** The element you are trying to interact with is no longer attached to the DOM. The page has been refreshed. You need to re-find the element.
-   **`TimeoutException`:** An explicit wait (`WebDriverWait`) failed because the condition was not met within the specified time.
-   **`ElementNotInteractableException`:** The element was found, but it cannot be interacted with (e.g., it's hidden, disabled, or covered by another element).
-   **`InvalidSelectorException`:** The syntax of your XPath or CSS selector is incorrect.

### 4. write an xpath syntax
The basic syntax is `//tagName[@attribute='value']`.
-   `//`: Selects nodes from anywhere in the document.
-   `tagName`: The HTML tag (e.g., `input`, `div`, `a`).
-   `[]`: A predicate to filter the nodes.
-   `@attribute`: The name of an attribute (e.g., `@id`, `@name`, `@class`).
-   `'value'`: The value of the attribute.

**Example:** `//button[@id='login-button']`

### 5. how will you handle alert?
You use Selenium's `Alert` interface.
1.  Switch the driver's focus to the alert: `Alert alert = driver.switchTo().alert();`
2.  Interact with it:
    -   `alert.accept();` (Click OK)
    -   `alert.dismiss();` (Click Cancel)
    -   `alert.getText();` (Get the text from the alert)

This only works for native browser JavaScript alerts, not for HTML modal dialogs.

### 6. difference between / and //
In XPath, both are used to traverse the DOM tree, but they have a key difference:
-   **`/` (Single Slash):** Selects from the root node and creates an **absolute path**. It selects only the immediate children of the current node. It's very rigid.
-   **`//` (Double Slash):** Selects nodes from **anywhere in the document**, regardless of their position. It creates a **relative path** and selects any matching descendant of the current node. This is the one you should almost always use to start your XPath because it's far more robust against UI changes.

### 7. write a java program to find the maximum salary of an individual
This is a "find max value in an array" problem. The "individual" part is just context.

```java
import java.util.Arrays;

public class MaxSalaryFinder {
    public static void main(String[] args) {
        int[] salaries = {50000, 95000, 60000, 110000, 80000};
        
        // The Java 8 Streams way (clean and declarative)
        int maxSalary = Arrays.stream(salaries)
                                .max()
                                .orElseThrow(() -> new IllegalStateException("Array is empty."));

        System.out.println("The maximum salary is: " + maxSalary);

        // The traditional loop way
        int max = salaries[0];
        for (int i = 1; i < salaries.length; i++) {
            if (salaries[i] > max) {
                max = salaries[i];
            }
        }
        System.out.println("The maximum salary (using loop) is: " + max);
    }
}
```
Showing the streams approach is generally more impressive as it's more modern and concise.
