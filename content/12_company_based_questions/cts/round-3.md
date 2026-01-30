---
title: "CTS-3"
date: 2026-01-30
draft: false
---

---

## Original Questions

CTS round 1
------------
1.Tell about your self
2.Manual test cases which form they will send
3.write a Sorting program
4.diferernce between implicit wait and explicit wait
5.write syntax implicit wait and explicit wait
6.Without I'd,tag name,text,class name how will you locate that element
7.testng-you have a two @test which will be first run 
8.types of xpath
9.Types of locators

---

## Answers

### 1. Tell about your self
Standard opener. Focus on your professional experience, automation skills, tech stack (Java, Selenium, etc.), and a key achievement.

### 2. Manual test cases which form they will send
This question is a bit ambiguous. It could mean "what format are manual test cases in?"
"Typically, manual test cases are documented in a test case management tool like Jira (with Xray/Zephyr) or TestRail. The 'form' includes standard fields:
-   **Test Case ID:** A unique identifier.
-   **Title/Summary:** A clear, concise description of the test's purpose.
-   **Preconditions:** The state the system must be in before the test begins.
-   **Steps:** A numbered list of actions to perform.
-   **Expected Results:** What the outcome should be for each step.
If a formal tool isn't used, they might be sent in a spreadsheet (like Excel or Google Sheets) with columns for each of these fields."

### 3. write a Sorting program
This is a basic coding filter. Sorting an array of integers is a classic example.

```java
import java.util.Arrays;

public class Sorter {
    public static void main(String[] args) {
        int[] numbers = {5, 1, 4, 2, 8};
        
        // The simple, correct way using the standard library.
        // Don't implement your own bubble sort unless they force you to.
        Arrays.sort(numbers);
        
        System.out.println("Sorted array: " + Arrays.toString(numbers));
    }
}
```
If they insist on a manual implementation, Bubble Sort is the easiest to write on the spot, but acknowledge it's inefficient (O(n^2)).

### 4. diference between implicit wait and explicit wait
-   **Implicit Wait:** A global setting on the `WebDriver` instance. It tells the driver to poll the DOM for a specified duration if an element is not found immediately. This is a **bad practice** as it's a blunt instrument that slows down tests and can hide timing issues.
-   **Explicit Wait:** The **correct** approach. You use the `WebDriverWait` class to wait for a *specific condition* to be true before proceeding (e.g., waiting for an element to be clickable). It's precise, reliable, and makes tests less flaky.

### 5. write syntax implicit wait and explicit wait
**Implicit Wait (Don't use this in a real project):**
```java
// Set once after driver initialization
driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
```

**Explicit Wait (The right way):**
```java
// Create a wait object
WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));

// Use it to wait for a specific condition
WebElement element = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("myElement")));
```

### 6. Without I'd,tag name,text,class name how will you locate that element
This is a locator strategy question. If the standard, simple locators are unavailable, you must use more advanced ones.
1.  **CSS Selector:** Use attribute-based selectors. Example: `input[name='username']`, `a[data-testid='login-button']`.
2.  **XPath:** This is the most powerful tool for this situation.
    -   **Attribute:** You can use any attribute, not just the common ones. `//div[@custom-attribute='some-value']`
    -   **Partial Matches:** Use `contains()` or `starts-with()`. `//div[contains(@class, 'login-button')]`
    -   **Axes:** Find a nearby stable element (like a label) and navigate from there using axes like `following-sibling`, `preceding-sibling`, or `ancestor`. Example: `//label[text()='Username']/following-sibling::input`

### 7. testng-you have a two @test which will be first run
The execution order of TestNG `@Test` methods depends on several factors:
-   **`priority`:** If you set `priority` (e.g., `@Test(priority = 1)`), lower priorities run first.
-   **`dependsOnMethods`:** If one test depends on another, the dependency will run first.
-   **Alphabetical (Default):** If there are no priority or dependency settings, TestNG typically runs tests in alphabetical order of their method names, though this is not a guaranteed behavior you should rely on.

**Answer:** "If no priority or dependency is set, the order is not guaranteed by TestNG, though it often defaults to alphabetical. The correct way to control the order is to use the `priority` or `dependsOnMethods` attributes."

### 8. types of xpath
There are two main types:
-   **Absolute XPath:** Starts from the root of the document (`/html/...`). It's a full, rigid path to the element. This is extremely brittle and should be avoided.
-   **Relative XPath:** Starts from anywhere in the document (`//...`). It locates elements based on their attributes or their relationship to other elements. This is the flexible, robust, and correct way to write XPaths.

### 9. Types of locators
The 8 standard locator strategies in Selenium: `id`, `name`, `className`, `tagName`, `linkText`, `partialLinkText`, `cssSelector`, and `xpath`.
