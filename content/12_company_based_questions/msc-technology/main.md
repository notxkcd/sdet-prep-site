---
title: "MSC technology"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

MSC technology interview questions
-----------------------------------
Explain implicit wait and explicit  wait
Exceptions that you have on explicit wait
Differentiate sanitiy testing and regression testing 
Explain the end to end testing
Write a code to find the smallest value in array
How will you handle the alerts
How will you confirm whether the alert is present 
As a QA how will you test the file upload options

---

## Answers (No-BS Java QA / SDET Explanations)

### Explain implicit wait and explicit wait
-   **Implicit Wait (Bad Practice):** A global setting on the `WebDriver` that tells it to poll the DOM for a certain amount of time when trying to find an element. It masks timing issues, slows tests, and can only wait for element presence.
-   **Explicit Wait (Good Practice):** (`WebDriverWait` with `ExpectedConditions`) Waits for a *specific condition* to be true (e.g., element is clickable, element is visible) before proceeding. It's precise, reliable, and makes tests less flaky.

### Exceptions that you have on explicit wait
The primary exception thrown when an `ExplicitWait` condition is not met within the specified timeout is **`TimeoutException`**.

### Differentiate sanitiy testing and regression testing
-   **Sanity Testing:** A narrow and deep test performed after a minor change or bug fix. It quickly verifies that the change works and hasn't broken anything closely related.
-   **Regression Testing:** A broad and deep test suite run after any code changes (new features, bug fixes) to ensure that the changes haven't introduced new bugs or re-introduced old ones into existing functionality.

### Explain the end to end testing
End-to-end (E2E) testing validates an application's entire workflow from start to finish, simulating a real user. It checks that all integrated components, from the UI to the backend services and databases, work together correctly to fulfill a business process. For example, logging in, adding an item to a cart, proceeding to checkout, and verifying order confirmation.

### Write a code to find the smallest value in array
```java
import java.util.Arrays;

public class MinValueFinder {
    public static int findMin(int[] arr) {
        if (arr == null || arr.length == 0) {
            throw new IllegalArgumentException("Array cannot be empty or null.");
        }
        
        // Java 8 Streams approach
        return Arrays.stream(arr).min().getAsInt();

        /* // Traditional loop approach
        int min = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < min) {
                min = arr[i];
            }
        }
        return min; */
    }
}
```

### How will you handle the alerts
You use the `Alert` interface from Selenium.
1.  Switch to the alert: `Alert alert = driver.switchTo().alert();`
2.  Interact with it:
    -   `alert.accept();` (Click OK)
    -   `alert.dismiss();` (Click Cancel)
    -   `alert.getText();` (Get the text from the alert)
    -   `alert.sendKeys("text");` (Type into a prompt alert)

### How will you confirm whether the alert is present
You use an `ExplicitWait` with the `ExpectedConditions.alertIsPresent()` condition.

```java
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.time.Duration;

public boolean isAlertPresent(WebDriver driver, int timeoutInSeconds) {
    try {
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(timeoutInSeconds));
        wait.until(ExpectedConditions.alertIsPresent());
        return true;
    } catch (TimeoutException e) {
        return false;
    }
}
```

### As a QA how will you test the file upload options
1.  **Positive Test Cases:**
    -   Upload a valid file type (`.pdf`, `.jpg`) within the size limits.
    -   Upload multiple valid files (if supported).
    -   Verify the uploaded file appears correctly (e.g., file name displayed, file content can be viewed/downloaded).
2.  **Negative Test Cases:**
    -   Upload an invalid file type (e.g., an `.exe` file). Verify an error message is displayed.
    -   Upload a file larger than the allowed size. Verify an error message.
    -   Upload an empty file.
    -   Upload a file with a very long filename or special characters in its name.
3.  **Security Testing:**
    -   Attempt to upload malicious files (e.g., files containing scripts).
4.  **Automation:** For automation, you use `element.sendKeys(absoluteFilePath)` on the `<input type="file">` element.
