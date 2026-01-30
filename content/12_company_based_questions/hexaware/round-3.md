---
title: "Hexaware-3"
date: 2026-01-30
draft: false
---

---

## Original Questions

- Hexaware L1 interview questions
-------------------------------
1. How to handle dynamic element which is changing for each page?
2. How to handle multiple browser in selenium?
3. Write code for take screenshot?
4. Tell about yourself?
5. What is string builder and string buffer?

---

## Answers

### 1. How to handle dynamic element which is changing for each page?
"Dynamic elements are a common challenge in UI automation. You handle them by using locators that rely on attributes or relationships that are **stable**, rather than those that change.
-   **Stable Attributes:** Prioritize `name` or `data-testid` attributes if developers have added them.
-   **Partial Matches:** Use XPath functions like `contains()` or `starts-with()` if only part of an attribute is dynamic (e.g., `//input[contains(@id, 'product-')]`).
-   **XPath Axes:** Navigate from a nearby stable element using axes like `following-sibling::` or `ancestor::` to locate the dynamic element relative to it."

### 2. How to handle multiple browser in selenium?
This refers to **cross-browser testing**.
-   **TestNG XML:** Configure your `testng.xml` to define multiple `<test>` blocks, each passing a different browser name (e.g., "chrome", "firefox") as a parameter.
-   **Setup Method:** In your TestNG `@BeforeMethod` (or `@BeforeTest`), accept this browser parameter and use a `switch` statement or a factory to instantiate the corresponding `WebDriver` (e.g., `ChromeDriver`, `FirefoxDriver`).
-   **Selenium Grid:** To run these tests simultaneously, use a Selenium Grid, which allows you to distribute tests across different browser instances running on various machines.

### 3. Write code for take screenshot?
```java
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import java.io.File;
import java.io.IOException;
import org.apache.commons.io.FileUtils; // Requires Apache Commons IO library

public class ScreenshotUtil {
    public static void captureScreenshot(WebDriver driver, String screenshotPath) {
        try {
            TakesScreenshot ts = (TakesScreenshot) driver; // Cast driver to TakesScreenshot
            File source = ts.getScreenshotAs(OutputType.FILE); // Get screenshot as a file
            FileUtils.copyFile(source, new File(screenshotPath)); // Copy to desired location
            System.out.println("Screenshot captured at: " + screenshotPath);
        } catch (IOException e) {
            System.err.println("Failed to capture screenshot: " + e.getMessage());
        }
    }
}
```
This method is typically called within an `@AfterMethod` in a TestNG listener when a test fails.

### 4. Tell about yourself?
Standard opener. Keep it concise, professional, and focus on your relevant experience (automation skills, tech stack, achievements).

### 5. What is string builder and string buffer?
Both are mutable classes used for creating and manipulating strings (unlike the immutable `String` class).
-   **`StringBuilder`:**
    -   **Not thread-safe** (not synchronized).
    -   **Faster** than `StringBuffer`.
    -   Best choice for single-threaded string manipulation (most common scenario).
-   **`StringBuffer`:**
    -   **Thread-safe** (its methods are synchronized).
    -   **Slower** than `StringBuilder` due to synchronization overhead.
    -   Use only if the string is being modified concurrently by multiple threads.
