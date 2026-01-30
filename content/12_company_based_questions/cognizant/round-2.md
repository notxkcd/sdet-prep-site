---
title: "Cognizant-2"
date: 2026-01-30
draft: false
---

---

## Original Questions

Cognizant:
-------------
1.Self introduction
2.Why did you leave your previous job?
3.Framework explanation
4.Swap two variable without using 3rd variable
5.Write a code for Palindrome
6.How to takesscreenshot?
7.What is chaining in rest assured?
8.What is an api header?
9.How you cover end to end api testing?
10.How to handle switch windows in selenium

---

## Answers

### 1. Self introduction
Standard opener. Keep it concise, professional, and highlight your most relevant skills and experiences for the role.

### 2. Why did you leave your previous job?
This is a culture-fit question. Be positive and forward-looking. **Do not** badmouth your previous employer.
-   **Good Answer:** "I'm looking for new challenges and opportunities for growth. I'm particularly interested in this role because it offers a chance to work on [mention something specific about the role/company, e.g., large-scale distributed systems, a new technology stack], which aligns with my career goals."
-   **Bad Answer:** "My manager was terrible, the pay was low, and I was bored."

### 3. Framework explanation
Describe the architecture of your test automation framework, not just a list of tools.
-   **Core:** "Our framework is a Java-based hybrid framework using TestNG as the test runner, Selenium for UI automation, and REST-assured for API testing."
-   **Design:** "It's built on the Page Object Model (POM) to separate UI logic from our test cases, making them clean and maintainable. We use a `BaseTest` class for common setup/teardown."
-   **Data:** "It's data-driven, using TestNG's `@DataProvider` to read test data from external JSON files."
-   **Integration:** "The entire framework is built with Maven and integrated into a Jenkins CI/CD pipeline for automated execution."

### 4. Swap two variable without using 3rd variable
A classic interview riddle. The arithmetic way is the most common.

```java
public class Swapper {
    public static void main(String[] args) {
        int a = 10;
        int b = 20;

        System.out.println("Before: a=" + a + ", b=" + b);

        // Arithmetic approach
        a = a + b; // a = 30
        b = a - b; // b = 30 - 20 = 10 (original value of a)
        a = a - b; // a = 30 - 10 = 20 (original value of b)

        System.out.println("After: a=" + a + ", b=" + b);
    }
}
```
You can also mention the XOR method (`a = a ^ b; ...`) to show deeper knowledge, but state that the arithmetic way is more readable.

### 5. Write a code for Palindrome
A palindrome is a word or number that reads the same forwards and backward. The simplest way to check is to reverse the string and see if it equals the original.

```java
public class PalindromeChecker {
    public static boolean isPalindrome(String str) {
        if (str == null) {
            return false;
        }
        // Clean the string: remove non-alphanumeric characters and convert to lower case
        String cleanedStr = str.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        
        // Reverse it
        String reversedStr = new StringBuilder(cleanedStr).reverse().toString();
        
        // Compare
        return cleanedStr.equals(reversedStr);
    }

    public static void main(String[] args) {
        System.out.println(isPalindrome("A man, a plan, a canal: Panama")); // true
        System.out.println(isPalindrome("racecar")); // true
        System.out.println(isPalindrome("hello")); // false
    }
}
```

### 6. How to takesscreenshot?
In Selenium, you use the `TakesScreenshot` interface. This is a critical capability for debugging failed UI tests.

```java
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import java.io.File;
import org.apache.commons.io.FileUtils; // From Apache Commons IO library

public void captureScreenshot(WebDriver driver, String filePath) {
    try {
        File screenshotFile = ((TakesScreenshot) driver).getScreenshotAs(OutputType.FILE);
        FileUtils.copyFile(screenshotFile, new File(filePath));
    } catch (Exception e) {
        System.err.println("Failed to take screenshot: " + e.getMessage());
    }
}
```
> **Side note:** In a real framework, this logic is placed in a TestNG/JUnit listener's `onTestFailure` method to automatically capture a screenshot whenever a test fails.

### 7. What is chaining in rest assured?
Chaining in REST-assured refers to its fluent API design, where you chain method calls together to build a request and validate the response in a single, readable statement. It follows the BDD syntax of `given/when/then`.

```java
import static io.restassured.RestAssured.*;
import static org.hamcrest.Matchers.*;

// Example of chaining
given()
    .baseUri("https://api.example.com")
    .header("Content-Type", "application/json")
    .param("userId", "123")
.when()
    .get("/users")
.then()
    .statusCode(200)
    .body("data.name", equalTo("John Doe"));
```
This is a single Java statement where each method call returns an object that allows the next method to be called.

### 8. What is an api header?
An API header (specifically, an HTTP header) is a piece of metadata sent along with an API request or response. It provides additional information about the request or the response itself.
**Common Request Headers:**
-   `Content-Type`: Specifies the format of the data in the request body (e.g., `application/json`).
-   `Authorization`: Carries credentials to authenticate the client (e.g., `Bearer <token>`).
-   `Accept`: Tells the server what media types the client can understand in the response.

**Common Response Headers:**
-   `Content-Type`: Specifies the format of the data in the response body.
-   `Date`: The date and time the response was generated.
-   `Server`: Information about the server software.

### 9. How you cover end to end api testing?
End-to-end API testing involves validating a complete business workflow by chaining multiple API calls together, simulating a real user journey.
"I design E2E tests that follow a business process. For example, for an e-commerce API:
1.  **POST `/register`:** Create a new user. Extract the `userId` from the response.
2.  **POST `/login`:** Log in as that user. Extract the `authToken` from the response.
3.  **GET `/products?q=laptop`:** Search for a product using the `authToken` for authentication. Extract a `productId`.
4.  **POST `/cart`:** Add the product to the cart using the `productId` and `authToken`.
5.  **POST `/orders`:** Create an order from the cart. Verify the response.
6.  **GET `/orders/{orderId}`:** Fetch the order details to confirm it was created correctly.
7.  **DELETE `/users/{userId}` (Cleanup):** Delete the test user to ensure the test is isolated and repeatable.
This verifies that the services not only work in isolation but also integrate correctly to fulfill a business workflow."

### 10. How to handle switch windows in selenium
This refers to handling multiple browser windows or tabs.
1.  Get the handle of the original window: `String originalWindow = driver.getWindowHandle();`
2.  Perform the action that opens the new window (e.g., click a link).
3.  Get all handles: `Set<String> allWindows = driver.getWindowHandles();`
4.  Loop through the set to find the handle of the new window.
5.  Switch focus to the new window: `driver.switchTo().window(newWindowHandle);`
6.  Perform actions in the new window.
7.  When done, close the new window (`driver.close()`) and switch back to the original (`driver.switchTo().window(originalWindow)`).
