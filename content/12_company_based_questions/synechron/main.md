---
title: "Synechron"
date: 2026-01-30
draft: false
---

---

## Original Questions

Synechron Interview Questions:- shared by azhar trainer:

1: Explain about your framework?
2: Have you used POM in your framework?
3: What is Page Factory?
4: Suppose you have 7 pages in your application then to achieve POM what will you do?
5: Have you used an interface in your framework other than selenium interfaces?
6: What are all the selenium interfaces?
7: Synchronization in selenium? syntax for implicit wait
8: How will you handle the popup window ?other then get window handle
9: What are Listeners?
10: How will you handle alerts?
11: How to get a system date and time?
12: How to connect to the database?
13: Exceptions in selenium?
14: Suppose u have class and abstract class in class there is a user defined constructor and main method which one will get executed first?
15: Primitives and Non Primitives data types in java?
- String is primitive or non primitive
16: What is Hashmap ?
- Can we store objects in a hash map and how to retrieve them?
17: What is Jenkins?
18: What is the use of Pom.xml?
19:what is the use of testng.xml?
20:Annotation used in page object model?

---

## Answers

### 1: Explain about your framework?

Describe the architecture, not just the tools. A good answer shows you think about design, maintainability, and scalability.
-   **Core:** "Java-based hybrid framework using TestNG, Selenium, and REST-assured."
-   **Design:** "Built on the Page Object Model. We have a `BaseTest` for common setup/teardown and a `BasePage` that all page objects extend for shared functionality like waits and custom click handlers."
-   **Data:** "Data-driven, with test data managed in JSON files loaded by a Jackson `ObjectMapper` and fed into tests via a custom `DataProvider`."
-   **Reporting & CI/CD:** "ExtentReports for reporting, integrated via TestNG listeners. The whole suite is built with Maven and executed in a Jenkins pipeline."

### 2: Have you used POM in your framework?

Yes. It's the industry standard design pattern for Selenium frameworks. The Page Object Model is fundamental to creating scalable and maintainable UI tests. Briefly restate what it is: "Yes, POM is the core design pattern of our framework. We create one Java class for each page or major component. This class encapsulates all the locators and interaction methods for that part of the UI, keeping our test scripts clean and free of Selenium code."

### 3: What is Page Factory?

Page Factory is a specific implementation of the POM pattern provided by Selenium's support library. It uses the `@FindBy` annotation to define locators for `WebElements`. The `PageFactory.initElements(driver, this)` method is used in the page object's constructor to initialize these `WebElement` fields.

> **The professional take:** "We used Page Factory initially, but we moved away from it. While it reduces some boilerplate, it can make debugging `StaleElementReferenceException`s harder because it hides them by re-finding the element on every access. We found that a plain POM with explicit `driver.findElement()` calls inside methods gave us more control and more transparent failure modes."

### 4: Suppose you have 7 pages in your application then to achieve POM what will you do?

"I would create 7 separate Java classes, one for each page. For example, `HomePage.java`, `LoginPage.java`, `ProductPage.java`, and so on. If there are common elements across all pages, like a header or footer, I'd create a `BasePage.java` abstract class with methods to handle those common elements, and all 7 page classes would `extend` `BasePage`."

### 5: Have you used an interface in your framework other than selenium interfaces?

This is a great question to separate senior from junior engineers. It tests if you think about abstraction in your own code.

**Good Answer:**
"Yes. We defined a custom `IConfigReader` interface. It had one method, `getProperty(String key)`. We then created two classes that implemented it: `PropertiesConfigReader` which read from a `.properties` file, and `JsonConfigReader` which read from a JSON file. In our `BaseTest`, we could switch between them easily. This allowed us to use different configuration sources for local runs versus CI runs without changing the test code, following the dependency inversion principle."

### 6: What are all the selenium interfaces?

The most important ones are:
1.  **`WebDriver`**: The core interface representing a browser. All driver classes (`ChromeDriver`, `FirefoxDriver`, etc.) implement this.
2.  **`WebElement`**: Represents an HTML element on the page.
3.  **`TakesScreenshot`**: An interface that `WebDriver` can be cast to, allowing you to take screenshots.
4.  **`JavascriptExecutor`**: An interface for executing JavaScript code in the browser context.
5.  **`Alert`**: For interacting with native browser JavaScript alerts.

### 7: Synchronization in selenium? syntax for implicit wait

Synchronization is waiting for the application under test to be in the right state before the test proceeds. This is the #1 challenge in UI automation.

There are three types of waits. The interviewer is asking for the syntax of the bad one. Give it to them, but explain why it's bad.

-   **Implicit Wait:** A global setting on the driver. If an element is not immediately found, it polls the DOM for the specified duration.
    -   **Syntax:** `driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));`
    -   **Why it's bad:** It's a blunt instrument. It slows down tests because it always waits the full timeout for elements that *don't* exist. It can't handle conditions other than presence (e.g., waiting for an element to be clickable). It hides timing issues. Don't use it.

-   **Explicit Wait:** The correct way. Wait for a *specific* condition.
    -   **Syntax:** `WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10)); wait.until(ExpectedConditions.elementToBeClickable(By.id("myButton")));`

### 8: How will you handle the popup window ?other then get window handle

This is a trick question. For a true browser popup window (or tab), you **must** use window handles (`getWindowHandle`, `getWindowHandles`, `switchTo().window()`). There is no other way.

If the interviewer pushes, they are probably confusing a "popup window" with something else:
-   **JavaScript `alert`**: Handled with `driver.switchTo().alert()`.
-   **HTML Modal Dialog**: This is not a real window. It's just a `div` styled to look like one. You handle it like any other `WebElement` on the page—find its locator and click the close button.

### 9: What are Listeners?

In the context of TestNG or JUnit, listeners are interfaces that allow you to "listen" for events during a test run and execute custom code when those events occur. They are the key to building advanced framework features.

**The most important one in TestNG is `ITestListener`.** It has methods like:
-   `onTestStart()`: Runs when a test method starts.
-   `onTestSuccess()`: Runs when a test method passes.
-   `onTestFailure()`: Runs when a test method fails. **This is where you put your screenshot logic.**
-   `onFinish()`: Runs after all tests are complete.

You connect your listener class to TestNG via the `testng.xml` file or using the `@Listeners` annotation on your test class.

### 10: How will you handle alerts?

You use the `Alert` interface.
1.  Switch the driver's context to the alert: `Alert alert = driver.switchTo().alert();`
2.  Interact with it:
    -   `alert.getText()`: Get the text from the alert.
    -   `alert.accept()`: Click "OK".
    -   `alert.dismiss()`: Click "Cancel" or press Escape.
    -   `alert.sendKeys("some text")`: Type into a `prompt` alert.

### 11: How to get a system date and time?

Use the `java.time` package, introduced in Java 8. It is immutable and thread-safe.

```java
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class DateTimeExample {
    public static void main(String[] args) {
        // Get the current date and time
        LocalDateTime now = LocalDateTime.now();
        System.out.println("Current DateTime: " + now);

        // Format it into a specific string format for file names or logs
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd_HH-mm-ss");
        String formattedNow = now.format(formatter);
        System.out.println("Formatted DateTime: " + formattedNow);
    }
}
```

### 12: How to connect to the database?

You use **JDBC** (Java Database Connectivity) API.
**The process:**
1.  **Add Dependency:** Make sure you have the JDBC driver dependency for your specific database (e.g., `mysql-connector-java` for MySQL) in your `pom.xml`.
2.  **Load the Driver:** `Class.forName("com.mysql.cj.jdbc.Driver");` (often not needed with modern JDBC drivers).
3.  **Establish Connection:** Use `DriverManager.getConnection()` with the database URL, username, and password.
4.  **Create a Statement:** Create a `Statement` or `PreparedStatement` object.
5.  **Execute Query:** Run the SQL query using `executeQuery()` (for `SELECT`) or `executeUpdate()` (for `INSERT`, `UPDATE`, `DELETE`).
6.  **Process ResultSet:** If it was a `SELECT`, iterate through the `ResultSet` object to get your data.
7.  **Close Everything:** CRITICAL: Close the `ResultSet`, `Statement`, and `Connection` in a `finally` block to prevent resource leaks.

### 13: Exceptions in selenium?

The most common ones an automation engineer deals with:
-   **`NoSuchElementException`**: `findElement()` couldn't find the element. Your locator is wrong or it's a timing issue.
-   **`StaleElementReferenceException`**: You had a reference to an element, but the page's DOM changed (e.g., via an AJAX call) and that element is now gone. You need to re-find the element.
-   **`TimeoutException`**: Your `WebDriverWait` gave up waiting for a condition to become true. The application is slow or broken.
-   **`ElementNotInteractableException`**: The element was found in the DOM, but you can't interact with it (e.g., it's hidden, covered by another element, or disabled).
-   **`InvalidSelectorException`**: The syntax of your XPath or CSS selector is wrong.

### 14: Suppose u have class and abstract class...

The question is a bit confusingly worded. Let's assume it means: "If a class has a user-defined constructor and a main method, which is executed first?"

The `main` method is the entry point of the program. It gets executed first. The constructor is only executed when you create an instance of the class using the `new` keyword *inside* the `main` method (or another method called by `main`).

```java
public class ExecutionOrder {

    // Constructor
    public ExecutionOrder() {
        System.out.println("Constructor is executed.");
    }

    // Main method - the entry point
    public static void main(String[] args) {
        System.out.println("Main method starts.");
        new ExecutionOrder(); // Now the constructor is called.
        System.out.println("Main method ends.");
    }
}
// Output:
// Main method starts.
// Constructor is executed.
// Main method ends.
```

### 15: Primitives and Non Primitives data types in java? String is primitive or non primitive

-   **Primitives:** The 8 fundamental data types built into the language. They are not objects. They hold values directly.
    -   `byte`, `short`, `int`, `long`, `float`, `double`, `char`, `boolean`.
-   **Non-Primitives (Reference Types):** Everything else. These are objects. They hold a reference (a memory address) to where the object's data is stored.
    -   Includes all classes you create, and all built-in Java classes like `String`, `Array`, `ArrayList`, `Object`.

**`String` is a non-primitive reference type.** It's a class (`java.lang.String`). It gets special treatment from the compiler (like literal assignment `String s = "hi";`), but it is an object.

### 16: What is Hashmap ? Can we store objects in a hash map and how to retrieve them?

A `HashMap` is a data structure that stores key-value pairs. It uses the `hashCode()` of the key to find the "bucket" where the value is stored, making lookups very fast (close to O(1) on average).

**Yes, you can store objects** as both keys and values.

```java
import java.util.HashMap;
import java.util.Map;

// Assume a simple User POJO class exists
class User {
    String id;
    String name;
    public User(String id, String name) { this.id = id; this.name = name; }
    // Important: For custom objects as keys, you MUST override equals() and hashCode()
    @Override public String toString() { return name; }
}

public class HashMapObjectExample {
    public static void main(String[] args) {
        Map<String, User> userMap = new HashMap<>();
        
        User user1 = new User("u123", "Alice");
        User user2 = new User("u456", "Bob");

        // Store objects as values
        userMap.put(user1.id, user1);
        userMap.put(user2.id, user2);

        // Retrieve an object using its key
        User retrievedUser = userMap.get("u123");
        
        System.out.println("Retrieved user: " + retrievedUser); // Alice
    }
}
```

### 17: What is Jenkins?

Jenkins is an open-source automation server. It's the most popular tool for building **CI/CD pipelines**.
-   **CI (Continuous Integration):** Automatically builds and tests your code every time a developer commits a change to version control (Git). This gives fast feedback.
-   **CD (Continuous Delivery/Deployment):** Automatically deploys your application to staging or production environments after it passes all the tests.

For a QA engineer, Jenkins is the tool that **runs your automated test suite** automatically, on a schedule, or triggered by a code change.

### 18: What is the use of Pom.xml?

The `pom.xml` (Project Object Model) is the core configuration file for a **Maven** project.

**Its primary uses are:**
1.  **Dependency Management:** Declaring all the external libraries (dependencies) your project needs, like Selenium, TestNG, etc. Maven then automatically downloads them.
2.  **Build Configuration:** Configuring plugins and defining how to build the project. For example, you configure the `maven-surefire-plugin` to specify which TestNG suite file to run (`mvn test`).
3.  **Project Metadata:** Contains basic information about the project like its `groupId`, `artifactId`, and `version`.

### 19:what is the use of testng.xml?

`testng.xml` is the primary configuration file for a **TestNG** test suite.

**It lets you control:**
1.  **Which tests to run:** You can specify which classes or packages to include or exclude.
2.  **Grouping:** You can choose to run only specific groups of tests (e.g., `smoke` or `regression`).
3.  **Parallel Execution:** You can configure tests to run in parallel by methods, classes, or tests to speed up execution.
4.  **Parameters:** You can pass parameters from the XML file into your test methods (e.g., the browser name or base URL).
5.  **Listeners:** You can register your custom listeners.

It gives you fine-grained control over the test execution, which you can't get by just running a test class directly.

### 20:Annotation used in page object model?

The most common annotation used in the Page Object Model is **`@FindBy`**.

This annotation is part of Selenium's **Page Factory** implementation. You use it to declare locators for your WebElements directly as class fields.

```java
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class LoginPage {

    @FindBy(id = "username")
    private WebElement usernameInput;

    @FindBy(how = How.NAME, using = "password")
    private WebElement passwordInput;
    
    @FindBy(xpath = "//button[text()='Login']")
    private WebElement loginButton;
}
```
Then, in the constructor, you call `PageFactory.initElements(driver, this);` to initialize these fields.
