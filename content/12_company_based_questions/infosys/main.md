---
title: "Infosys"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

- Infosys Interview Questions

1. Self Introduction
2. Explain oops concepts?
3. What is Interface?
4. What is the key word to implement child classes in Inheritance?
5. Screen share:
*Reverse the String?
* Print the Vowels?
* Screenshot?
*Find the duplicate elements of
- array?
6. How to handle window handles?
7. How to handle the popup or alerts?
8. Exception handling?
9. How to troubleshoot the exception?
10. What is BDD?
11. How do you handle version issues, what approach you will handle to resolve?
12. What is Constructor?
- Why do we need a constructor for our project?
Give example.
13. What is Ortho Response?
14. 505, 200, 404, ?
15. Diff bet final, finally and finalize in Java?
16. Can we change the variable once it declare final?
17. Is Final can be overridden?
18. Multiple Inheritance?
19. Collections ?
- Diff between list, set and map?
20. What is 429 response code?
21. How you validate the request methods in API?
22. POM ?
- Page Factory?

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. Self Introduction

Standard opener. Keep it brief, technical, and relevant. 60-90 seconds. Structure: Role, Responsibilities, Tech Stack, Key Achievement.

### 2. Explain oops concepts?

The four pillars. Use QA-centric examples.
-   **Encapsulation:** Page Object Model. Hiding locators and implementation logic within a page class. Tests only call public methods like `loginPage.login()`.
-   **Abstraction:** The `WebDriver` interface. You code against `WebDriver`, and you don't care about the specific implementation (`ChromeDriver`, `FirefoxDriver`).
-   **Inheritance:** A `BaseTest` class with common setup (`@BeforeMethod`) and teardown (`@AfterMethod`) logic that all your test classes extend.
-   **Polymorphism:** Method overriding. A `BasePage` has a `verifyPageLoad()` method. `HomePage` and `ProductPage` both override it to add their own specific verification steps.

### 3. What is Interface?

An interface is a pure abstraction. It's a contract that defines a set of method signatures that a class *must* implement if it `implements` that interface.
-   It contains only `public static final` variables and `public abstract` methods (by default).
-   A class can implement multiple interfaces.
-   It enforces a standard structure. In test automation, you could have an interface `Reporting` with methods like `logPass()` and `logFail()`, and have different classes implement it for ExtentReports or Allure.

### 4. What is the key word to implement child classes in Inheritance?

The keyword is `extends`.
`public class LoginPage extends BasePage { ... }`

### 5. Screen share

This is a live coding check. They want to see how you think and write code, not just if you know the answer.

#### *Reverse the String?

The `StringBuilder` approach is the clean, correct one.

```java
public String reverseString(String str) {
    if (str == null) return null;
    return new StringBuilder(str).reverse().toString();
}
```

#### * Print the Vowels?

Loop and check against a set of vowel characters.

```java
public void printVowels(String str) {
    if (str == null) return;
    String vowels = "aeiou";
    for (char c : str.toLowerCase().toCharArray()) {
        if (vowels.indexOf(c) != -1) {
            System.out.print(c);
        }
    }
}
```

#### * Screenshot?

This is a Selenium question. You use the `TakesScreenshot` interface.

```java
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import java.io.File;
import org.apache.commons.io.FileUtils; // From Apache Commons IO library

public void takeScreenshot(WebDriver driver, String filePath) {
    try {
        // 1. Cast the driver to TakesScreenshot
        TakesScreenshot ts = (TakesScreenshot) driver;

        // 2. Get the screenshot as a file
        File source = ts.getScreenshotAs(OutputType.FILE);

        // 3. Copy the file to the desired destination
        FileUtils.copyFile(source, new File(filePath));
    } catch (Exception e) {
        System.out.println("Exception while taking screenshot: " + e.getMessage());
    }
}
```
> **Side note:** In a real framework, this logic is in a listener (`onTestFailure`) or a utility class.

#### *Find the duplicate elements of array?

Using a `Set` is the standard, efficient way.

```java
import java.util.HashSet;
import java.util.Set;

public void findDuplicates(int[] arr) {
    Set<Integer> uniqueElements = new HashSet<>();
    Set<Integer> duplicateElements = new HashSet<>();
    for (int i : arr) {
        if (!uniqueElements.add(i)) {
            duplicateElements.add(i);
        }
    }
    System.out.println("Duplicates: " + duplicateElements);
}
```

### 6. How to handle window handles?

Selenium's focus is on one window/tab at a time. To handle a new one, you must switch context.
1.  Get the handle of the original window: `String originalHandle = driver.getWindowHandle();`
2.  Trigger the action that opens the new window.
3.  Get all handles: `Set<String> allHandles = driver.getWindowHandles();`
4.  Loop through `allHandles` and find the one that is not `originalHandle`.
5.  Switch to it: `driver.switchTo().window(newHandle);`
6.  When done, `driver.close()` the new window and `driver.switchTo().window(originalHandle);` back to the original.

### 7. How to handle the popup or alerts?

There are two kinds of "popups".
1.  **JavaScript Alerts:** These are native browser popups created by `alert()`, `confirm()`, or `prompt()`. They block the UI. You must handle them using Selenium's `Alert` interface.
    ```java
    // Switch to the alert
    Alert alert = driver.switchTo().alert();
    
    // Get its text
    String alertText = alert.getText();
    
    // Accept it (click OK) or dismiss it (click Cancel/Escape)
    alert.accept();
    // or
    alert.dismiss();
    ```

2.  **HTML "Popups" (Modals):** These are just `div` elements styled to look like popups. They are part of the page's HTML. You handle them just like any other web element: find their locators and click the close button or whatever other element you need to interact with.

### 8. Exception handling?

In Java, it's done with a `try-catch-finally` block.
-   `try`: The block of code that might throw an exception.
-   `catch`: The block that executes if an exception of a specific type is thrown in the `try` block. You handle the error here (log it, report it).
-   `finally`: This block **always** executes, whether an exception occurred or not. It's critical for cleanup code, like `driver.quit()`.

```java
WebDriver driver = null;
try {
    driver = new ChromeDriver();
    // Do some test stuff...
} catch (Exception e) {
    // Log the error, maybe take a screenshot
    System.out.println("Test failed: " + e.getMessage());
    throw e; // Re-throw the exception to fail the test
} finally {
    if (driver != null) {
        driver.quit(); // This MUST run to prevent hanging browser processes.
    }
}
```

### 9. How to troubleshoot the exception?

A systematic approach:
1.  **Read the Stack Trace:** Don't just read the exception name (`NullPointerException`). Read the whole trace. The most important lines are usually the first few and the ones that mention your own code (`com.myproject...`). This tells you *where* the error happened.
2.  **Identify the Exception Type:** What kind of exception is it?
    -   `NoSuchElementException`: Your locator is wrong or you have a timing issue.
    -   `NullPointerException`: An object was `null` when you tried to use it. Why was it null? Did a previous method fail to initialize it?
    -   `StaleElementReferenceException`: The DOM changed. You need to re-find the element.
3.  **Analyze the Context:** What was the test trying to do right before it failed? Look at the application state.
4.  **Reproduce It:** Try to run the test again. If it fails consistently, it's a solid bug. If it's flaky, it's almost certainly a timing issue.
5.  **Use Debugging Tools:** Set a breakpoint just before the line that throws the exception and inspect the state of all variables. Check if the element is actually present and visible in the browser at that exact moment.

### 10. What is BDD?

Behavior-Driven Development. It's an extension of TDD that focuses on defining application behavior in plain, human-readable language from a user's perspective.
-   **Tool:** Cucumber is the most common BDD tool in the Java world.
-   **Language:** Gherkin (`Given-When-Then` syntax) is used to write "feature files."
-   **Goal:** To improve communication between developers, QAs, and business stakeholders. The feature files act as living documentation and acceptance criteria.

### 11. How do you handle version issues, what approach you will handle to resolve?

This usually means dependency management issues. The only correct answer is **Maven** (or Gradle).

-   **The Problem:** Manually managing JAR files is a nightmare. You get conflicts (e.g., Library A needs `guava-18.0` but Library B needs `guava-23.0`). This is "JAR Hell."
-   **The Solution:** Maven's `pom.xml` centralizes all dependency declarations.
    -   **Dependency Declaration:** You specify the libraries and versions you need in the `<dependencies>` section.
    -   **Transitive Dependencies:** Maven automatically downloads the dependencies *of your dependencies*.
    -   **Dependency Mediation:** If there's a version conflict, Maven has a "nearest definition" strategy: it chooses the version closest to your project in the dependency tree.
    -   **Troubleshooting:** You can use the `mvn dependency:tree` command to visualize the entire dependency tree and identify where conflicting versions are coming from. You can then use the `<dependencyManagement>` section in your POM to explicitly force a specific version of a library to be used everywhere.

### 12. What is Constructor? Why do we need a constructor for our project? Give example.

A constructor is a special method that is called when an object is created (`new`). Its job is to initialize the state of the object. It has the same name as the class and has no return type.

**Why we need it:** To ensure an object is created in a valid and usable state.

**Example in a test framework (Page Object Model):**

```java
public class LoginPage {
    private WebDriver driver;
    private By usernameField = By.id("username");

    // Constructor: ensures that LoginPage always has a WebDriver instance to work with.
    public LoginPage(WebDriver driver) {
        if (driver == null) {
            throw new IllegalArgumentException("Driver cannot be null");
        }
        this.driver = driver;
    }

    public void enterUsername(String username) {
        // The 'driver' object is guaranteed to be non-null here because of the constructor.
        driver.findElement(usernameField).sendKeys(username);
    }
}
```
Without the constructor, the `driver` would be `null`, and `enterUsername()` would throw a `NullPointerException`.

### 13. What is Ortho Response?

This is likely a misinterpretation or a niche term. The interviewer probably meant **Idempotent** or something related to API responses. If you hear a term you don't know, ask for clarification: "I haven't heard that specific term before, could you spell it out or describe what it means?"

If they mean **idempotent response**, it's an operation that can be applied multiple times without changing the result beyond the initial application. `GET`, `PUT`, and `DELETE` requests should be idempotent. `POST` is not.

### 14. 505, 200, 404, ?

Standard HTTP status codes.
-   `200 OK`: Success.
-   `404 Not Found`: The requested resource does not exist.
-   `505 HTTP Version Not Supported`: The server does not support the HTTP protocol version used in the request. This is very rare to see.

### 15. Diff bet final, finally and finalize in Java?

A classic Java question to trip people up.
-   **`final` (keyword):** A modifier to make something unchangeable.
    -   `final` variable: A constant.
    -   `final` method: Cannot be overridden.
    -   `final` class: Cannot be extended (`String` is a final class).
-   **`finally` (block):** Part of a `try-catch` statement. This block of code is **always** executed, regardless of whether an exception was thrown. It's used for resource cleanup (`driver.quit()`).
-   **`finalize()` (method):** A method from the `Object` class that the garbage collector calls before destroying an object. **You should never use this.** It's deprecated and unreliable. Using a `finally` block is the correct way to manage resources.

### 16. Can we change the variable once it declare final?

No. That's the entire point of `final`.

### 17. Is Final can be overridden?

A `final` **method** cannot be overridden.
A `final` **class** cannot be extended, so the concept of overriding doesn't even apply.

### 18. Multiple Inheritance?

Java classes do **not** support multiple inheritance (a class cannot `extend` more than one other class). This is to avoid the "Diamond Problem" where a class inherits two different implementations of the same method.

Java **does** support a form of multiple inheritance through **interfaces**. A class can `implement` multiple interfaces, inheriting their abstract methods and default method implementations.

### 19. Collections ? Diff between list, set and map?

-   **`List`:** An ordered collection of elements, allows duplicates. Access by index. `ArrayList`, `LinkedList`.
-   **`Set`:** An unordered collection of unique elements. No duplicates. `HashSet`, `LinkedHashSet`.
-   **`Map`:** A collection of key-value pairs. Keys must be unique. `HashMap`, `LinkedHashMap`.

`List` and `Set` implement the `Collection` interface. `Map` does not.

### 20. What is 429 response code?

`429 Too Many Requests`. The client is being rate-limited. You have sent too many requests in a given period, and the server is telling you to slow down. The response headers often include a `Retry-After` header indicating how long to wait before trying again.

### 21. How you validate the request methods in API?

This question is a bit ambiguous. It could mean:
1.  **How do you test the behavior of different HTTP methods?**
    -   **GET:** Assert the status code is `200 OK` and the response body contains the expected data.
    -   **POST:** Assert the status code is `201 Created`, and optionally hit the returned `Location` URL to verify the new resource exists.
    -   **PUT:** Assert status code is `200 OK`. Then, do a `GET` request for that resource and assert the entire object was updated.
    -   **DELETE:** Assert status code is `204 No Content`. Then, do a `GET` request for that resource and assert you get a `404 Not Found`.

2.  **How do you validate that an endpoint only allows certain methods?**
    -   Send a non-supported method and assert the right error code. For example, if an endpoint `GET /users` should not support `POST`, send a `POST` request to it and assert that the status code is `405 Method Not Allowed`.

### 22. POM ? Page Factory?

-   **POM (Page Object Model):** A design pattern, not a tool. It's the concept of creating one class per page (or component) of your application. This class is responsible for encapsulating the locators and interaction methods for that page. It makes tests cleaner and more maintainable.

-   **Page Factory:** A specific implementation of the POM concept provided by Selenium. It uses annotations (`@FindBy`) to define locators and a static `initElements` method to initialize the `WebElement` fields in your page object class.

    ```java
    public class LoginPage {
        @FindBy(id = "username")
        private WebElement usernameField;

        @FindBy(id = "password")
        private WebElement passwordField;

        public LoginPage(WebDriver driver) {
            // PageFactory initializes the @FindBy elements
            PageFactory.initElements(driver, this);
        }
    }
    ```
> **Modern View:** Many experienced engineers now advise **against** using Page Factory. It can be less efficient (elements are located every time they're used) and can hide `StaleElementReferenceException`s by re-finding the element, which can mask underlying timing issues in your tests. A plain POM class where you use `driver.findElement()` inside your methods is often more robust and easier to debug.

---

## Original Questions (UNTOUCHED)

- Infosys Interview Questions - (Round 1)
-------------------------------------------

1. Self Intro
2. Project Explanation and Frameworks and Tools Used in ur Previous Project?
3. How do you validate the Broken Links Rest Assured using Automation?
4. What are all the methods in Rest Assured?
5. What is GET method does?
6. What is Diff between Put and Post?
7. What are the dependencies you use for Rest Assured?
8. Write Get Request by using payload? In Which dependency .given().when() is coming?
9. Diff between findElement() and findElements() ?
10. Write Program 
String str = " java is &%#@!GoodABCD1234";
Print How many character, Numbers and Special Character.
11. Diff between StringBuffer and StringBuilder?
12. Is it possible to change the string Variable once it assigned?
13. Where did you execute the Script in Your Project?
14. How do you configure Jenkins with Github?
15. Diff between Abstraction and Encapsulation? Tell me the major/Common diff especially for users.
16. How do we get data from POJO classes?
17. Write pojo class for Username and password?
18. Diff between This and Super ?
19. How to Click a Button in the Child window from parent window?
20. Scenario Based Question"
     1. There is 5 Test Boxes, Which have same Properties, values, Names, ancor tag, everything is same. How do find the Odd one?
     2. Explain Dynamic Xpath? what is its aspects?
21. Diff Between Relative and Absolute Xpath?

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. Self Intro

Standard.

### 2. Project Explanation and Frameworks and Tools Used in ur Previous Project?

Standard. Be specific about tools and your role.

### 3. How do you validate the Broken Links Rest Assured using Automation?

You don't use REST-assured for this. REST-assured is for testing APIs. You find broken links on a web page using Selenium.

**The process:**
1.  Use Selenium to find all `<a>` tags on the page: `driver.findElements(By.tagName("a"))`.
2.  Iterate through the list of `WebElement`s.
3.  For each element, get the `href` attribute.
4.  If the `href` is not null and not empty, use a standard Java HTTP client (like `HttpURLConnection` or Apache `HttpClient`) to send a `HEAD` or `GET` request to that URL. **Do not use Selenium to `navigate()` to each link**, that would be incredibly slow.
5.  Check the HTTP response code. Anything `400` or greater is a broken link.

```java
// Simplified example
List<WebElement> links = driver.findElements(By.tagName("a"));
for (WebElement link : links) {
    String url = link.getAttribute("href");
    if (url != null && !url.isEmpty()) {
        try {
            HttpURLConnection connection = (HttpURLConnection) new URL(url).openConnection();
            connection.setRequestMethod("HEAD");
            connection.connect();
            int responseCode = connection.getResponseCode();
            if (responseCode >= 400) {
                System.out.println("Broken link: " + url + " - Response code: " + responseCode);
            }
        } catch (IOException e) {
            System.out.println("Error checking link: " + url + " - " + e.getMessage());
        }
    }
}
```

### 4. What are all the methods in Rest Assured?

REST-assured uses a fluent, BDD-style syntax. The main "methods" are chained parts of this syntax.
-   `given()`: Where you set up the request (headers, cookies, body, auth).
-   `when()`: Where you specify the HTTP method (`get()`, `post()`, `put()`, `delete()`) and the endpoint URL.
-   `then()`: Where you perform assertions on the response (status code, body content, headers).
-   `log()`: For logging details of the request or response.
-   `extract()`: To extract values from the response for further use.

### 5. What is GET method does?

Retrieves a resource from the server. It's safe and idempotent.

### 6. What is Diff between Put and Post?

-   **POST:** Creates a new resource. Not idempotent.
-   **PUT:** Updates an existing resource *completely*. Is idempotent. You send the full representation of the resource.

### 7. What are the dependencies you use for Rest Assured?

You need at least these in your `pom.xml`:

1.  **`rest-assured`**: The core library.
2.  **`json-path`**: For parsing JSON responses using JSONPath expressions.
3.  **`xml-path`**: For parsing XML responses.
4.  **`gson` or `jackson-databind`**: A JSON serialization/deserialization library. REST-assured uses one of these to automatically convert your POJOs to/from JSON. Jackson is more common.
5.  **A testing framework**: `testng` or `junit`.

### 8. Write Get Request by using payload? In Which dependency .given().when() is coming?

`GET` requests should **not** have a payload (body). This is a trick question. The HTTP spec says a body on a GET has no defined semantics and some servers will reject it. If you need to send parameters, you use query parameters in the URL.

The `.given().when()` syntax comes from the main **`rest-assured`** dependency.

```java
import static io.restassured.RestAssured.*;

// Correct GET with query parameters, NO payload
given()
    .baseUri("https://api.example.com")
    .param("userId", "123")
.when()
    .get("/user")
.then()
    .statusCode(200);
```

### 9. Diff between findElement() and findElements() ?

-   **`findElement(By locator)`:**
    -   Finds the **first** matching element on the page.
    -   **Return type:** `WebElement`.
    -   **If no element is found:** Throws a `NoSuchElementException`.

-   **`findElements(By locator)`:**
    -   Finds **all** matching elements on the page.
    -   **Return type:** `List<WebElement>`.
    -   **If no elements are found:** Returns an **empty list**. It does **not** throw an exception. This is useful for checking if an element exists without using a `try-catch` block (`driver.findElements(locator).isEmpty()`).

### 10. Write Program String str = " java is &%#@!GoodABCD1234"; Print How many character, Numbers and Special Character.

Iterate through the string and use `Character` class helper methods.

```java
public void countCharTypes(String str) {
    int letters = 0;
    int numbers = 0;
    int spaces = 0;
    int specials = 0;

    for (char c : str.toCharArray()) {
        if (Character.isLetter(c)) {
            letters++;
        } else if (Character.isDigit(c)) {
            numbers++;
        } else if (Character.isWhitespace(c)) {
            spaces++;
        } else {
            specials++;
        }
    }
    System.out.println("Letters: " + letters);
    System.out.println("Numbers: " + numbers);
    System.out.println("Spaces: " + spaces);
    System.out.println("Specials: " + specials);
}
```

### 11. Diff between StringBuffer and StringBuilder?

Both are mutable string classes.
-   **`StringBuilder`:** Not thread-safe (not synchronized). It's faster. This is the one you should use by default for any single-threaded string manipulation.
-   **`StringBuffer`:** Thread-safe (its methods are synchronized). This makes it slower due to the overhead of locking. You should only use it if you are sharing and modifying a string across multiple threads, which is a very rare scenario.

### 12. Is it possible to change the string Variable once it assigned?

You can change what a `String` reference variable points to, but you cannot change the `String` object itself. Strings are immutable.

```java
String s = "hello"; // s points to "hello"
s = "world";        // s now points to a *new* string object "world".
                    // The original "hello" object is unchanged.
```

### 13. Where did you execute the Script in Your Project?

This is a CI/CD question.
"We executed our scripts in multiple environments:
1.  **Locally:** On our own machines during development and debugging of new tests.
2.  **CI/CD Pipeline (Jenkins):** This was the main execution environment. On every code commit, Jenkins would pull the latest code, build the project with Maven, and run the entire regression suite (`mvn test`) on a Selenium Grid.
3.  **Staging Environment:** We had a dedicated nightly run against the staging environment to catch issues before a release.
4.  **Production (Smoke Tests):** A small subset of critical smoke tests were run against the production environment immediately after a deployment to ensure the core functionality was up."

### 14. How do you configure Jenkins with Github?

You use a **webhook**.
1.  **In GitHub:** Go to your repository settings -> Webhooks. Add a new webhook. The "Payload URL" will be `http://<your-jenkins-server>/github-webhook/`. Set the content type to `application/json`. Choose which events should trigger the webhook (e.g., "Just the `push` event").
2.  **In Jenkins:**
    -   Create a new pipeline job.
    -   In the "Build Triggers" section, check "GitHub hook trigger for GITScm polling".
    -   In the "Pipeline" section, configure the source to be "Pipeline script from SCM".
    -   Set the SCM to "Git" and provide your repository URL.
    -   This tells Jenkins to look for a `Jenkinsfile` in your repository.
3.  **`Jenkinsfile`:** You create a file named `Jenkinsfile` in the root of your Git repository. This file defines your build pipeline in code.

Now, when you `git push` to your repository, GitHub sends a notification to the webhook URL, which tells Jenkins to wake up, pull the code, and run the pipeline defined in your `Jenkinsfile`.

### 15. Diff between Abstraction and Encapsulation? Tell me the major/Common diff especially for users.

-   **Encapsulation:** About **hiding complexity**. It bundles data and methods together and protects the internal state from outside interference. The "user" of the class only sees the public methods. **Think:** A car's dashboard. You see the speedometer and steering wheel, you don't see the engine wiring.
-   **Abstraction:** About **hiding implementation**. It shows *what* an object does, but not *how* it does it. **Think:** The steering wheel itself. You know turning it left turns the car left, you don't need to know if it's rack-and-pinion or power steering. The `WebDriver` interface is the perfect example.

**The simplest difference:** Encapsulation hides data and internal workings. Abstraction hides the "how".

### 16. How do we get data from POJO classes?

You use **getter** methods. A POJO (Plain Old Java Object) encapsulates its fields by making them `private` and provides `public` getter and setter methods to access them.

```java
User user = new User("test", "pass");
String username = user.getUsername(); // Using the getter
```

### 17. Write pojo class for Username and password?

```java
public class User {
    // Private fields to encapsulate data
    private String username;
    private String password;

    // A no-arg constructor is often needed for libraries like Jackson
    public User() {
    }

    // A constructor to initialize the object
    public User(String username, String password) {
        this.username = username;
        this.password = password;
    }

    // Public getter for username
    public String getUsername() {
        return username;
    }

    // Public setter for username
    public void setUsername(String username) {
        this.username = username;
    }

    // Public getter for password
    public String getPassword() {
        return password;
    }

    // Public setter for password
    public void setPassword(String password) {
        this.password = password;
    }
}
```

### 18. Diff between This and Super ?

Both are keywords used within a class.
-   **`this`:** Refers to the **current instance** of the class.
    -   Used to disambiguate between instance variables and local variables: `this.username = username;`.
    -   Used to call another constructor from within a constructor: `this("defaultUser");`.

-   **`super`:** Refers to the **parent class** (superclass).
    -   Used to call the parent class's constructor: `super(driver);`. This must be the first line in a child class's constructor.
    -   Used to call a parent class's method if you've overridden it: `super.verifyPageLoad();`.

### 19. How to Click a Button in the Child window from parent window?

You can't. Selenium's context is tied to a single window at a time. You must first **switch the driver's context** to the child window, and *then* you can find and click the button. See the answer to question 6 on window handling.

### 20. Scenario Based Question

#### 1. There is 5 Test Boxes, Which have same Properties, values, Names, ancor tag, everything is same. How do find the Odd one?

If all attributes are identical, you cannot distinguish them with a static locator. There must be something different.
-   **Position:** The most likely answer. You can get all of them with `findElements` and then select one by its index. `driver.findElements(By.xpath("//input[@class='same']")).get(2)` would get the third one.
-   **Surrounding Text:** Is there a unique label next to one of them? You could use XPath axes: `//label[text()='Unique Label']/following-sibling::input`.
-   **Hidden Attribute:** Use the browser's developer tools to inspect everything. There might be a hidden attribute or a difference in the computed CSS properties that you can't see on the surface.

If they are truly, 100% identical in every way, then from a user's perspective, they are indistinguishable. This would be a UI design bug.

#### 2. Explain Dynamic Xpath? what is its aspects?

A dynamic XPath is a locator strategy you use when element attributes (like `id`) are not static. Instead of relying on an exact match, you use XPath functions and axes to build a locator based on stable relationships.

**The "aspects" or techniques are:**
-   **Functions:** `contains()`, `starts-with()`, `text()`.
    -   `//button[contains(@id, 'submit-btn-')]`
-   **Axes:** `ancestor`, `parent`, `following-sibling`, `preceding-sibling`.
    -   `//h2[text()='Login']/parent::div//button` (Find the button that is a descendant of the div that is the parent of the h2 with the text 'Login').
-   **Logical Operators:** `and`, `or`.
    -   `//input[@type='text' and @name='username']`

### 21. Diff Between Relative and Absolute Xpath?

-   **Absolute XPath:** Starts from the root of the HTML document (`/html`). It's a full path to the element.
    -   Example: `/html/body/div[1]/section/div[2]/form/input[1]`
    -   **Why it's bad:** Extremely brittle. If any element in that long path changes (e.g., a developer adds a new `div`), the XPath breaks. **You should never use absolute XPaths.**

-   **Relative XPath:** Starts from a known, stable element, or anywhere in the document using `//`. It's relative to the current context.
    -   Example: `//input[@id='username']`
    -   **Why it's good:** It's shorter, more readable, and much more resilient to changes in the page structure. It only depends on the element itself or a nearby stable element, not the entire DOM tree.
