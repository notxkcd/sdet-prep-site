---
title: "WIPRO"
date: 2026-01-30
draft: false
---

---

## Original Questions

- WIPRO Interview Questions (Bangalore)
-------------------------------------
1. Self Inro
2. Framework Explanation?
3. About Project and Tools used?
4. Explain Oops? In detail?
5. How to Scroll the webpage to the particular element? Write Code for that.
6. Reporting tool?
7. Do we have multiple constructor in same class?
8. How to handle Dropdown in selenium? Write code for that.
9. Exception and its types?
10. String is Immutable, then how to change or update string value?
11. How to handle the webpage Which takes more time to load?
12. Explain waits? 
13. You have Many Link Test in webpage and if u click one it will open new webpage and you need to find the element in that new webpage, how you can achive that?
14. What are the status code will mostly get on APi testing? What is 429, 501, 500..etc?
15. In TestNG we have more tests like smoke and regression, How will you run only smoke test?
16. Explain HTTP methods?

---

## Answers

### 1. Self Inro

See previous answers. It's a communication filter. Be concise, technical, and confident. 60-90 seconds max.
- Who you are (Role).
- What you do (Responsibilities, tech stack).
- What you're good at (Key skills: Java, Selenium, API testing, CI/CD).
- A recent, quantifiable achievement.

### 2. Framework Explanation?

Don't just list tools. Describe the architecture and design patterns. A professional answer shows you understand *why* the framework is built the way it is.

**Example Structure:**
1.  **Core:** "Our framework is a hybrid, data-driven framework using Java, TestNG, and Selenium WebDriver."
2.  **Design:** "We use the Page Object Model (POM) to keep locators and element interactions separate from test logic. This makes tests readable and easy to maintain."
3.  **Data:** "Test data is externalized into Excel sheets or JSON files, and we use a custom data provider class to feed it into our TestNG tests."
4.  **Utilities:** "We have a central `WebDriverManager` for browser setup, explicit wait handlers, and screenshot utilities."
5.  **Reporting:** "Reporting is handled by ExtentReports, integrated via TestNG listeners to log steps and capture screenshots on failure."
6.  **Integration:** "The whole thing is built with Maven and run on a Jenkins pipeline, triggered by new code commits."

### 3. About Project and Tools used?

Be specific.
- **Project:** "I worked on the primary e-commerce platform for a major retailer. My team was responsible for the end-to-end testing of the checkout and payment processing modules."
- **Tools:**
    - **Programming:** Java
    - **Test Runner:** TestNG
    - **UI Automation:** Selenium WebDriver
    - **API Automation:** REST-assured
    - **Build Tool:** Maven
    - **CI/CD:** Jenkins
    - **Version Control:** Git (with GitHub)
    - **Project Management:** Jira
    - **Reporting:** ExtentReports

### 4. Explain Oops? In detail?

They want the four pillars. Give them QA-centric examples.

1.  **Encapsulation:** Bundling data (variables) and the methods that operate on that data into a single unit (a class). Hiding the implementation details.
    *   **QA Example:** The Page Object Model. A `LoginPage` class encapsulates the locators (`By.id("username")`) and the methods (`login()`). Your test script doesn't know *how* login works, it just calls `loginPage.login("user", "pass")`. The implementation is hidden.

2.  **Abstraction:** Hiding complex reality while exposing only the essential parts.
    *   **QA Example:** `WebDriver` is an interface. Your code uses `driver.get()` and `driver.findElement()`. You don't care if the implementation is `ChromeDriver`, `FirefoxDriver`, or `RemoteWebDriver`. The complexity of browser communication is abstracted away.

3.  **Inheritance:** A class acquiring the properties and methods of another class. Used for code reuse.
    *   **QA Example:** A `BaseTest` class contains `@BeforeMethod` and `@AfterMethod` logic for starting and stopping the `WebDriver`. All your test classes like `LoginTest` and `SearchTest` `extend BaseTest` to inherit this common setup/teardown behavior.

4.  **Polymorphism:** "Many forms." An object can take on many forms. The most common use is method overriding.
    *   **QA Example:** You have a `BasePage` with a method `verifyPageIsLoaded()`. For `HomePage`, this might just check the title. For `ProductDetailsPage`, you override this method to also check for the product image and price, because the title alone isn't enough. The same method name (`verifyPageIsLoaded`) does different things depending on the object (`HomePage` vs. `ProductDetailsPage`).

### 5. How to Scroll the webpage to the particular element? Write Code for that.

You use the `JavascriptExecutor`. Selenium itself doesn't have a robust scroll-to-element command, so you delegate this to the browser's own JavaScript engine.

```java
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class UiUtils {
    public void scrollToElement(WebDriver driver, WebElement element) {
        // Cast the driver to a JavascriptExecutor
        JavascriptExecutor js = (JavascriptExecutor) driver;
        
        // Execute the script. 'arguments[0]' refers to the first argument passed, which is our element.
        js.executeScript("arguments[0].scrollIntoView(true);", element);
    }
}
```
> **Side note:** `scrollIntoView(true)` aligns the top of the element with the top of the viewport. `scrollIntoView(false)` aligns the bottom. This is the only correct way to do this.

### 6. Reporting tool?

Don't just name one. Explain why it's used.
-   **ExtentReports:** The most common answer. It creates beautiful, interactive HTML reports with charts, step logs, and embedded screenshots. It's highly customizable.
-   **Allure:** Another powerful option. It provides great historical trend analysis and can integrate results from multiple test runs.
-   **TestNG/JUnit Default Reports:** Basic, but functional. They produce XML files that CI/CD tools like Jenkins can easily parse to determine pass/fail status. The HTML reports are ugly but work.

You integrate these tools using **listeners** (`ITestListener` in TestNG).

### 7. Do we have multiple constructor in same class?

Yes. This is called **constructor overloading**. You can have multiple constructors as long as they have different parameter lists (different number of parameters, or different types).

```java
public class User {
    private String username;
    private String password;
    private boolean isActive;

    // Constructor 1: for a new user with default active state
    public User(String username, String password) {
        this.username = username;
        this.password = password;
        this.isActive = true; // Default value
    }

    // Constructor 2: for creating a user from a database record
    public User(String username, String password, boolean isActive) {
        this.username = username;
        this.password = password;
        this.isActive = isActive;
    }
}
```

### 8. How to handle Dropdown in selenium? Write code for that.

Use the `Select` class for standard `<select>` HTML tags.

```java
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.Select;

public class DropdownHandler {
    public void selectFromDropdown(WebDriver driver) {
        // 1. Find the <select> element
        WebElement dropdownElement = driver.findElement(By.id("country-dropdown"));

        // 2. Create a Select object
        Select countryDropdown = new Select(dropdownElement);

        // 3. Select an option in one of three ways
        countryDropdown.selectByVisibleText("United States");
        // OR
        countryDropdown.selectByValue("USA"); // From the <option value="USA"> attribute
        // OR
        countryDropdown.selectByIndex(1); // 0-indexed
    }
}
```
> **Important:** If the dropdown is a custom-built one using `<div>`s and `<span>`s (common in modern frameworks like React), you can't use the `Select` class. You have to automate it like any other element: click the dropdown to open it, then wait for the desired option to be visible and click it.

### 9. Exception and its types?

An exception is an event that disrupts the normal flow of the program.

**Two main categories:**
1.  **Checked Exceptions:** The compiler forces you to handle them using `try-catch` or `throws`. They represent predictable problems.
    *   `IOException`: Error reading a file. Your test data reader needs to handle this.
    *   `SQLException`: Error connecting to a database.
    *   `FileNotFoundException`: The file you're trying to read isn't there.

2.  **Unchecked Exceptions (Runtime Exceptions):** You are not forced to handle them. They usually represent programming errors.
    *   `NullPointerException`: You called a method on a `null` object.
    *   `ArrayIndexOutOfBoundsException`: You tried to access an array index that doesn't exist.
    *   `StaleElementReferenceException` (Selenium): The element you're trying to use is no longer attached to the DOM.
    *   `NoSuchElementException` (Selenium): The locator you used didn't find anything.

### 10. String is Immutable, then how to change or update string value?

You don't. That's what "immutable" means. Every time you "change" a string, you are actually creating a **new** string object in memory.

```java
String s1 = "hello"; 
// s1 points to a "hello" object in the string pool.

s1 = s1.concat(" world"); 
// A *new* string "hello world" is created. 
// s1 now points to this new object. The original "hello" is still there, now unreferenced.
```
If you need to perform many modifications to a string, using `String` is inefficient because it creates a lot of garbage. For that, you use a mutable string class:

-   **`StringBuilder`:** Mutable. Faster. Not thread-safe. Use this for building strings in a single thread (99% of the time).
-   **`StringBuffer`:** Mutable. Slower because it's synchronized (thread-safe). Use this only if you are modifying the string from multiple threads, which is rare.

### 11. How to handle the webpage Which takes more time to load?

This is a core competency for an automation engineer. The answer is **explicit waits**.

You use `WebDriverWait` to poll for a specific condition before you declare the page loaded or throw an error. Never use `Thread.sleep()`.

```java
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.support.ui.ExpectedConditions;
import java.time.Duration;

public void waitForPageLoad(WebDriver driver) {
    WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(30)); // Max wait time
    
    // Wait for a known, stable element on the page to be visible.
    // This element should be one of the last things to load.
    wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("footer")));
    
    // You can also wait for the document's ready state
    wait.until(driver -> ((JavascriptExecutor) driver).executeScript("return document.readyState").equals("complete"));
}
```

### 12. Explain waits?

Answered in detail previously. Recap:
-   **Implicit Wait:** A global setting. Bad practice. Avoid it. It makes debugging timing issues harder and slows down failure cases.
-   **Explicit Wait:** The correct way. Use `WebDriverWait` to wait for a specific `ExpectedConditions` before proceeding. It's precise and reliable.
-   **Fluent Wait:** An advanced explicit wait. Gives you control over polling interval and exceptions to ignore. `WebDriverWait` is a pre-configured `FluentWait`.

### 13. You have Many Link Test in webpage...

This is a **window handling** question. When you click a link that opens a new tab or window, Selenium's focus stays on the original tab. You must explicitly switch it.

```java
public void handleNewWindow(WebDriver driver) {
    String originalWindowHandle = driver.getWindowHandle();
    
    // Click the link that opens the new window
    driver.findElement(By.id("new-window-link")).click();

    // Loop through all available window handles
    for (String windowHandle : driver.getWindowHandles()) {
        // If it's not the original window, switch to it
        if (!originalWindowHandle.equals(windowHandle)) {
            driver.switchTo().window(windowHandle);
            break;
        }
    }
    
    // Now you are in the context of the new window
    // Find your element and perform actions
    WebElement elementInNewWindow = driver.findElement(By.id("some-element"));
    elementInNewWindow.click();
    
    // When done, you can close the new window and switch back
    driver.close();
    driver.switchTo().window(originalWindowHandle);
}
```

### 14. What are the status code will mostly get on APi testing?

You should know these cold.

-   **2xx (Success):**
    -   `200 OK`: Standard success for GET, PUT, PATCH.
    -   `201 Created`: Success after a POST request that created a new resource. The response body usually contains the new resource.
    -   `204 No Content`: Success, but there's no data to return. Common for DELETE requests.

-   **4xx (Client Error):** Your request is bad.
    -   `400 Bad Request`: Generic client-side error. Malformed syntax, invalid parameters.
    -   `401 Unauthorized`: You're not logged in. You need to provide valid credentials (e.g., an auth token).
    -   `403 Forbidden`: You are logged in, but you don't have permission to access this resource.
    -   `404 Not Found`: The endpoint or resource you're asking for doesn't exist.
    -   `429 Too Many Requests`: You're being rate-limited. You've sent too many requests in a given amount of time.

-   **5xx (Server Error):** The server screwed up. This is a bug.
    -   `500 Internal Server Error`: The generic "something went wrong on our end" error. The server had an unhandled exception. This is always a high-severity bug.
    -   `501 Not Implemented`: The server doesn't support the functionality required to fulfill the request. For example, you sent a `PATCH` request to an endpoint that only accepts `GET` and `POST`.
    -   `503 Service Unavailable`: The server is down or overloaded.

### 15. In TestNG we have more tests like smoke and regression, How will you run only smoke test?

You use **TestNG groups**.

1.  **Annotate your tests:**
    ```java
    public class LoginTests {
        @Test(groups = {"smoke", "regression"})
        public void testSuccessfulLogin() { /* ... */ }

        @Test(groups = {"regression"})
        public void testInvalidPassword() { /* ... */ }
    }
    ```

2.  **Configure your `testng.xml`:** Create a suite file that specifies which groups to run.

    ```xml
    <!DOCTYPE suite SYSTEM "https://testng.org/testng-1.0.dtd" >
    <suite name="MySuite" verbose="1">
      <test name="SmokeTests">
        <groups>
          <run>
            <include name="smoke"/>
          </run>
        </groups>
        <classes>
          <class name="com.mytests.LoginTests"/>
          <!-- more classes -->
        </classes>
      </test>
    </suite>
    ```
    When you run this suite, only the tests annotated with `@Test(groups = "smoke")` will execute.

### 16. Explain HTTP methods?

These are the verbs of the web.

-   **GET:** Retrieve data. Safe and idempotent (running it multiple times doesn't change the server state). Should not have a request body.
-   **POST:** Create a new resource. Not idempotent (running it twice creates two new resources). Data is sent in the request body.
-   **PUT:** Update an existing resource completely. You send the *entire* representation of the resource. Idempotent.
-   **PATCH:** Partially update an existing resource. You only send the fields you want to change. Not necessarily idempotent.
-   **DELETE:** Delete a resource. Idempotent (deleting something that's already gone is still a success, usually `204 No Content`).
-   **HEAD:** Same as GET, but only returns the headers, not the response body. Useful for checking if a resource exists without downloading it.
-   **OPTIONS:** Asks the server which HTTP methods and headers are allowed for a URL. Used for CORS (Cross-Origin Resource Sharing).
