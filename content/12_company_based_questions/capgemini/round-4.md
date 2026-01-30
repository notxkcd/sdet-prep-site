---
title: "Capgemini-4"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

Capgemini L1
------------
Tell about your self
Find the character count and duplicate characters in the string array
Go to amazon Take xpath for  mobile’s offer prize
Difference b/w abstract class and interface
Code for Window handlings
Framework explanation 
Difference between hook class and background 
Parallel and cross browser testing

---

## Answers (No-BS Java QA / SDET Explanations)

### Tell about your self
Standard opener. Focus on your professional experience, automation skills, tech stack, and a key achievement.

### Find the character count and duplicate characters in the string array
This seems to mean "in a given string".
To find the character count (frequency) and identify duplicates:
```java
import java.util.HashMap;
import java.util.Map;

public class CharAnalyzer {
    public static void analyzeString(String str) {
        if (str == null || str.isEmpty()) {
            System.out.println("String is empty or null.");
            return;
        }

        Map<Character, Integer> charCounts = new HashMap<>();
        for (char c : str.toCharArray()) {
            charCounts.put(c, charCounts.getOrDefault(c, 0) + 1);
        }

        System.out.println("Character Counts:");
        charCounts.forEach((character, count) -> System.out.println("'" + character + "': " + count));

        System.out.println("\nDuplicate Characters:");
        charCounts.forEach((character, count) -> {
            if (count > 1) {
                System.out.println("'" + character + "' appears " + count + " times.");
            }
        });
    }

    public static void main(String[] args) {
        analyzeString("Mississippi");
    }
}
```

### Go to amazon Take xpath for mobile’s offer prize
This is a practical XPath question. It requires inspecting the Amazon page.
Assuming a typical product listing structure, you'd look for an element with an offer price, likely indicated by a `span` or `div` with a specific class or data attribute.

Example (conceptual, may vary based on current Amazon HTML):
`//span[contains(@class, 'a-price-whole') and text() = '12,999']` - Find a specific offer price.
`//span[contains(@class, 'a-price') and contains(., '₹')]/span[@class='a-price-whole']` - Find any whole offer price that has a rupee symbol (conceptually).
A more robust XPath would likely involve navigating from a stable product container element.

`//div[@data-cel-widget='search_result_0']//span[contains(@class, 'a-price-whole')]` - Get the offer price of the first search result.

### Difference b/w abstract class and interface
| Feature             | Abstract Class                                 | Interface                                         |
| :------------------ | :--------------------------------------------- | :------------------------------------------------ |
| **Methods**         | Can have `abstract` and concrete methods.      | Can have `abstract`, `default`, `static` methods. (Pre-Java 8, only abstract). |
| **Variables**       | Can have instance, static, and final variables.| Only `public static final` variables (constants). |
| **Constructors**    | Can have constructors.                         | Cannot have constructors.                         |
| **Inheritance**     | A class can `extend` only one abstract class.  | A class can `implement` multiple interfaces.      |
| **Purpose**         | Provides a common base for subclasses, with some default behavior and some required behavior. | Defines a contract for behavior.                   |

### Code for Window handlings
```java
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.time.Duration;
import java.util.Set;

public class WindowHandler {
    public void switchToNewWindow(WebDriver driver, int timeoutInSeconds) {
        String originalWindowHandle = driver.getWindowHandle();
        
        // Trigger action that opens a new window/tab (e.g., clicking a link)
        driver.findElement(By.id("linkToNewWindow")).click();

        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(timeoutInSeconds));
        wait.until(ExpectedConditions.numberOfWindowsToBe(2)); // Wait for 2 windows to be present

        Set<String> allWindowHandles = driver.getWindowHandles();
        
        for (String handle : allWindowHandles) {
            if (!handle.equals(originalWindowHandle)) {
                driver.switchTo().window(handle);
                break; // Switch to the new window and exit loop
            }
        }
        // Now driver is focused on the new window
    }

    public void switchBackToOriginalWindow(WebDriver driver, String originalWindowHandle) {
        driver.close(); // Close the current window (which is the new one)
        driver.switchTo().window(originalWindowHandle); // Switch back
    }
}
```

### Framework explanation
Standard. Describe your framework's architecture, key components (POM, data-driven), tools (Java, Selenium, TestNG), and CI/CD integration.

### Difference between hook class and background
-   **Hook Class (Cucumber):** A Java class (or methods within a step definition class) containing `@Before` or `@After` methods. These are **code-level** mechanisms for setup/teardown that run before/after scenarios or steps. They are purely technical.
-   **Background (Gherkin Keyword):** A section in a `.feature` file that contains `Given` steps. These steps run before **every scenario** in that feature file. It's a **feature-level** mechanism to define common preconditions for scenarios, making the scenarios more concise. The `Background` is part of the business-readable specification.

### Parallel and cross browser testing
-   **Parallel Testing:** Running multiple test cases simultaneously to reduce the total execution time of the test suite. In TestNG, configured with `parallel="methods|classes|tests"` and `thread-count` in `testng.xml`.
-   **Cross-Browser Testing:** Running the same test suite on different web browsers (e.g., Chrome, Firefox, Edge) to ensure the application functions correctly across all of them. In TestNG, this is achieved by passing a `browser` parameter to your test setup methods from `testng.xml`, where you define separate `<test>` blocks for each browser.
-   **Combined:** You typically run cross-browser tests in parallel using a **Selenium Grid** to get results quickly.
