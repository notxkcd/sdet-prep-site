---
title: "Photon"
date: 2026-01-30
draft: false
---

---

## Original Questions

- Photon Interview Questions

- Tell about yourself
- Diff between Junit and TestNG
- what are TestNG annotations?
- Find Duplicate Characters in string.
- Find reversal of string word by word.
- Selenium - Given this url "https://www.geico.com/" and asked to pass numbers to zipcode textbox and click go and validate the result "thanks message"
- diff between assert and verify
- Explain about locators in selenium.
- diff between explicit and implicit wait.
- what are types of testing?
- what is method overloading and overriding?
- How do you upload a file in selenium?
- How do you create a defect in jira tool?
- Experience on Rest API
- Explain about API response codes

---

## Answers

### Tell about yourself
Standard opener. Keep it concise, technical, and focused on your skills, and accomplishments.

### Diff between Junit and TestNG
Both are Java testing frameworks, but TestNG is generally considered more powerful and suitable for large-scale test automation, which is why it's more common in Selenium projects.

| Feature               | JUnit (4/5)                                                                | TestNG                                                                      | 
| :-------------------- | :------------------------------------------------------------------------- | :-------------------------------------------------------------------------- | 
| **Annotations**       | Has a good set (`@Test`, `@BeforeEach`, `@AfterEach`).                      | Has a more extensive and powerful set (`@BeforeSuite`, `@BeforeTest`, etc.). | 
| **Grouping**          | Supported via `@Tag` annotation (JUnit 5).                                 | First-class citizen with `@Test(groups = "...")` and XML configuration. Very flexible. | 
| **Parallel Execution**| Possible in JUnit 5, but more complex to configure.                        | Simple and powerful to configure via the `testng.xml` file.                 | 
| **Data-Driven Tests** | Supported via `@ParameterizedTest` (JUnit 5).                               | Supported via the very intuitive `@DataProvider` annotation.                | 
| **Dependencies**      | Does not support test dependencies. Tests should be independent.           | Allows you to make tests dependent on each other with `dependsOnMethods`.   | 
| **Configuration**     | Primarily through annotations.                                             | Highly configurable through the `testng.xml` suite file.                    | 

**Conclusion:** For a complex test automation suite, TestNG's advanced features for grouping, parallelization, and configuration give it a significant edge.

### what are TestNG annotations?
They are markers that control how TestNG executes your test methods.
-   **Suite/Test/Class Level:** `@BeforeSuite`, `@AfterSuite`, `@BeforeTest`, `@AfterTest`, `@BeforeClass`, `@AfterClass`. Used for setup/teardown that happens once per suite, test block, or class.
-   **Method Level:** `@BeforeMethod`, `@AfterMethod`. Run before and after *each* `@Test` method. Ideal for `WebDriver` initialization and cleanup.
-   **Test Method:** `@Test`. Marks the method as a test case.
-   **Data Provider:** `@DataProvider`. Marks a method that supplies data to a test.

### Find Duplicate Characters in string.
Use a `Map` to store character frequencies.

```java
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;

public class DuplicateFinder {
    public static void findDuplicates(String str) {
        if (str == null || str.isEmpty()) return;

        Map<Character, Long> freq = str.chars()
            .mapToObj(c -> (char) c)
            .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
        
        System.out.println("Duplicate characters in '" + str + "':");
        freq.entrySet().stream()
            .filter(entry -> entry.getValue() > 1)
            .forEach(entry -> System.out.println("'" + entry.getKey() + "' appears " + entry.getValue() + " times."));
    }
}
```

### Find reversal of string word by word.
Split the string by spaces, then build a new string by iterating through the words in reverse order.

```java
public class WordReverser {
    public static String reverseWords(String sentence) {
        if (sentence == null || sentence.trim().isEmpty()) {
            return sentence;
        }
        
        String[] words = sentence.trim().split("\\s+");
        StringBuilder reversed = new StringBuilder();
        
        for (int i = words.length - 1; i >= 0; i--) {
            reversed.append(words[i]).append(" ");
        }
        
        return reversed.toString().trim();
    }

    public static void main(String[] args) {
        System.out.println(reverseWords("Hello World from Java")); 
        // Output: Java from World Hello
    }
}
```

### Selenium - Given this url "https://www.geico.com/" and asked to pass numbers to zipcode textbox and click go and validate the result "thanks message" 
This is a practical scripting task.

```java
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.time.Duration;

public class GeicoTest {
    public static void main(String[] args) {
        // Assume WebDriver is set up
        WebDriver driver = new ChromeDriver();
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));

        try {
            // 1. Navigate to the URL
            driver.get("https://www.geico.com/");

            // 2. Find the zipcode textbox and enter a value
            // Inspecting the site shows the input has an id 'zip'
            WebElement zipCodeInput = driver.findElement(By.id("zip"));
            zipCodeInput.sendKeys("20878");

            // 3. Find and click the 'Go' button
            // The button is an <input type="submit">
            WebElement goButton = driver.findElement(By.cssSelector("input[type='submit'][value='Go']"));
            goButton.click();

            // 4. Validate the result
            // Wait for the message to be visible and get its text
            // Inspecting shows the message might be in an element with id 'DummiesLanding_lblMessage' or similar.
            // THIS LOCATOR IS LIKELY TO CHANGE. It's for demonstration.
            WebElement thanksMessage = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("DummiesLanding_lblMessage")));
            
            String messageText = thanksMessage.getText();
            assert messageText.contains("Thanks for choosing GEICO"); // Or whatever the real message is

            System.out.println("Test Passed! Validation message found: " + messageText);

        } finally {
            driver.quit();
        }
    }
}
```
> **What they're testing:** Can you find locators? Can you use `sendKeys` and `click`? Most importantly, do you use an **explicit wait** before validating the result? The assertion will fail without a wait because the message doesn't appear instantly.

### diff between assert and verify
This is a classic distinction, especially in older testing tools.
-   **Assert (Hard Assert):** When an assertion fails, it throws an `AssertionError`, the test is immediately **stopped**, and marked as failed. You use this for critical checkpoints. If the login fails, there's no point in continuing the test. `Assert.assertEquals(...)` in TestNG/JUnit is a hard assert.

-   **Verify (Soft Assert):** When a verification fails, it does **not** stop the test. The failure is logged, and the test continues to execute. At the end of the test, all collected failures are reported. You use this when you want to check several non-critical things on a page and want to see all the failures at once, not just the first one.

**In modern TestNG, you implement this with the `SoftAssert` class:**
```java
import org.testng.asserts.SoftAssert;

@Test
public void testWithSoftAssert() {
    SoftAssert softAssert = new SoftAssert();
    
    softAssert.assertEquals(driver.getTitle(), "Expected Title"); // Fails, but continues
    softAssert.assertTrue(driver.findElement(By.id("logo")).isDisplayed()); // Continues
    softAssert.assertEquals(driver.findElement(By.id("header")).getText(), "Wrong Text"); // Fails, but continues
    
    // CRITICAL: This line gathers all failures and fails the test if any were found.
    softAssert.assertAll(); 
}
```

### Explain about locators in selenium.
Locators are the strategies Selenium uses to find elements on a web page. There are 8 types:
1.  `id`: Best choice. Should be unique and stable.
2.  `name`: Good choice. Often used for form elements.
3.  `className`: Can be useful, but often not unique. Be careful with compound classes (`class="btn btn-primary"`).
4.  `tagName`: For finding elements by their HTML tag (e.g., `<a>`, `<h1>`). Usually returns many elements.
5.  `linkText`: Finds a link (`<a>`) by its exact visible text.
6.  `partialLinkText`: Finds a link by a partial match of its visible text.
7.  `cssSelector`: Powerful and fast. Can select elements based on `id`, `class`, attributes, and relationships. Often preferred over XPath for performance.
8.  `xpath`: Most powerful and flexible, but can be slower. Can traverse the DOM in any direction (up, down, sideways), which CSS cannot. Essential for finding elements without stable attributes.

### diff between explicit and implicit wait.
-   **Implicit Wait:** A global setting on the `WebDriver` instance. Tells the driver to poll the DOM for a set amount of time if an element is not immediately available. **It's a bad practice** because it's imprecise and hides timing issues.
-   **Explicit Wait:** The correct approach. You use the `WebDriverWait` class to wait for a *specific, expected condition* to be true before proceeding. It's targeted, reliable, and makes test failures easier to diagnose.

### what are types of testing?
This is a broad question. Structure the answer from high-level to low-level.
-   **Functional Testing:** Verifying what the system does.
    -   `Unit Testing`: Testing individual methods or classes in isolation.
    -   `Integration Testing`: Testing how multiple components or services work together.
    -   `System Testing`: Testing the complete, integrated system against its requirements.
    -   `Acceptance Testing (UAT)`: Formal testing to determine if the system satisfies its business requirements.
-   **Non-Functional Testing:** Verifying *how well* the system works.
    -   `Performance Testing`: Testing for speed, scalability, and stability under load (Load, Stress, Soak testing).
    -   `Security Testing`: Testing for vulnerabilities.
    -   `Usability Testing`: Testing how user-friendly the application is.
    -   `Compatibility Testing`: Testing across different browsers, OSes, and devices.

### what is method overloading and overriding?
-   **Overloading:** Same method name, different parameter list (type or number of arguments). Resolved at compile time.
-   **Overriding:** A subclass provides a specific implementation for a method that is already defined in its parent class. Same method signature. Resolved at runtime using dynamic polymorphism.

### How do you upload a file in selenium?
You do **not** click the "Upload" or "Browse" button. That opens an OS-native file dialog, which Selenium cannot control.

Instead, you use `sendKeys()` on the file input element itself. The element is usually an `<input type="file">`.

```java
import java.io.File;

public void uploadFile(WebDriver driver) {
    // 1. Find the <input type="file"> element. It might be hidden.
    WebElement fileInput = driver.findElement(By.cssSelector("input[type='file']"));
    
    // 2. Get the absolute path to your file.
    String filePath = new File("src/test/resources/my-file-to-upload.txt").getAbsolutePath();
    
    // 3. Use sendKeys() to "type" the file path into the input element.
    fileInput.sendKeys(filePath);
    
    // 4. Click the submit button for the form.
    driver.findElement(By.id("submit-upload")).click();
}
```

### How do you create a defect in jira tool?
This is a process question.
1.  Log in to Jira.
2.  Navigate to the correct project.
3.  Click the "Create" button.
4.  In the "Create Issue" dialog, select the Issue Type as "Bug".
5.  Fill out the fields with high-quality information:
    -   **Summary/Title:** A clear, concise title (e.g., "Login fails with 500 error for users with special characters in password").
    -   **Component/s:** The part of the application that is affected.
    -   **Description:** Provide detailed, unambiguous steps to reproduce the bug. Include the **Expected Result** vs. the **Actual Result**.
    -   **Environment:** Specify the browser, OS, and application version.
    -   **Attachments:** Add screenshots, video recordings, and relevant log files.
    -   **Priority/Severity:** Assign a severity and suggest a priority.
6.  Click "Create".

### Experience on Rest API
"Yes, I have strong experience testing REST APIs. I use REST-assured in Java to build automated test suites that cover our API's functionality. My tests validate status codes, response times, headers, and JSON response bodies using JSONPath assertions. I also work with Postman for manual and exploratory API testing."

### Explain about API response codes
-   **`1xx` Informational:** Request received, continuing process. (Rarely seen).
-   **`2xx` Success:** The action was successfully received, understood, and accepted. (`200 OK`, `201 Created`).
-   **`3xx` Redirection:** Further action needs to be taken to complete the request. (`301 Moved Permanently`).
-   **`4xx` Client Error:** The request contains bad syntax or cannot be fulfilled. The client messed up. (`400 Bad Request`, `401 Unauthorized`, `404 Not Found`).
-   **`5xx` Server Error:** The server failed to fulfill an apparently valid request. The server messed up. (`500 Internal Server Error`, `503 Service Unavailable`).
