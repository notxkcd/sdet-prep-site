---
title: "Capgemini"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

First round:
Self intro
wap String reverse and swap
wap even and odd nos in given array
stateelement exception'
Four exception and explanation
Garbage collector
Cucumber explain
Hooks 
diff bw hooks and background
Jira tool
RTM
diff bw smoke sanity and regression
diff bw adhoc and explaoratory test
collection list and set
why xml interact with html
iframe
dropdown
action Class
example for abstract and interface encapsulation
inheritance


---

## Answers (No-BS Java QA / SDET Explanations)

### Self intro

This is a filter. They're checking if you can communicate. Structure your answer like this:
1.  **Who you are:** "I'm a QA Engineer specializing in Java test automation."
2.  **What you do:** "I build and maintain automated test suites for enterprise web applications, focusing on API and UI testing."
3.  **Your core skills:** "My main tools are Java, Selenium, and REST-assured. I'm responsible for designing frameworks, writing tests, and integrating them into the CI/CD pipeline."
4.  **Your recent achievement:** "Recently, I reduced our regression suite's runtime by 30% by parallelizing tests and refactoring our wait strategy."

Don't tell your life story. Keep it to 60-90 seconds.

### wap String reverse and swap

They're testing basic coding fluency. "Swap" is ambiguous here, it could mean swapping characters or words. Let's assume character-level operations. A competent engineer provides a clean, readable solution.

**String Reverse:**

```java
public class StringManipulation {
    // The simple, correct way. Don't write a for loop unless they force you.
    public static String reverseString(String str) {
        if (str == null) {
            return null;
        }
        return new StringBuilder(str).reverse().toString();
    }
}
```

> **What this shows:** You know the standard library. You're not going to reinvent the wheel for a solved problem. This is a good thing. Only a junior developer thinks writing a C-style for-loop here is impressive.

**String "Swap":** This is a weird question. It probably means swapping the first and last characters, or pairs of characters. Let's assume swapping the first and last.

```java
public static String swapFirstAndLast(String str) {
    if (str == null || str.length() <= 1) {
        return str;
    }
    char[] chars = str.toCharArray();
    char first = chars[0];
    chars[0] = chars[chars.length - 1];
    chars[chars.length - 1] = first;
    return new String(chars);
}
```

> **Side note:** Clarify the ambiguity. Ask: "When you say 'swap,' do you mean swapping adjacent characters, the first and last, or something else?" This shows you think before you code.

### wap even and odd nos in given array

Another basic filter. Can you loop and use the modulo operator?

```java
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.Arrays;

public class ArraySorters {

    // The classic for-loop. It's fine.
    public static void printEvenAndOdd(int[] arr) {
        List<Integer> even = new ArrayList<>();
        List<Integer> odd = new ArrayList<>();
        for (int num : arr) {
            if (num % 2 == 0) {
                even.add(num);
            } else {
                odd.add(num);
            }
        }
        System.out.println("Even: " + even);
        System.out.println("Odd: " + odd);
    }

    // The Java 8+ way. Shows you're modern.
    public static void printEvenAndOddStreams(int[] arr) {
        Map<Boolean, List<Integer>> parts = Arrays.stream(arr)
                                                   .boxed()
                                                   .collect(Collectors.partitioningBy(i -> i % 2 == 0));
        System.out.println("Even: " + parts.get(true));
        System.out.println("Odd: " + parts.get(false));
    }
}
```
> **What they're testing:** The stream-based solution is better. It's declarative. You're saying *what* you want ("partition by even/odd"), not *how* to do it (manual loop and `if` statement). In test automation, declarative code is easier to maintain.

### stateelement exception`

It's `StaleElementReferenceException`. You get this when you locate a web element, the DOM changes (e.g., due to an AJAX call or navigation), and you try to interact with the element you *used* to have a reference to. The reference is now "stale" because the element it pointed to is gone or has been replaced.

**The QA mindset answer:** This isn't just an exception; it's a symptom of a race condition between your test script and the application's frontend. The root cause is almost always an issue with waiting.

**How to fix it:**
1.  **Don't use `Thread.sleep()`:** It's a guarantee of flaky tests.
2.  **Use explicit waits:** Use `WebDriverWait` to wait for a specific condition (e.g., `ExpectedConditions.elementToBeClickable`) before interacting.
3.  **Re-find the element:** If you perform an action that you know refreshes a part of the page, find the element again before the next interaction. This is the most robust solution.

```java
// Bad: Prone to StaleElementReferenceException
WebElement button = driver.findElement(By.id("submit"));
// some action that refreshes the button
button.click(); // BOOM! Stale

// Good: Re-finding the element
driver.findElement(By.id("submit")).click(); // Action 1
// some action that refreshes the button
driver.findElement(By.id("submit")).click(); // Action 2, element is re-found
```

### Four exception and explanation

They want to see if you've actually written code and seen it fail. Don't give them textbook definitions. Give them QA scenarios.

1.  **`NullPointerException`:** The classic. You called a method on an object reference that was `null`. In testing, this often happens when a `findElement` call fails to find an element and returns `null` (though modern Selenium throws `NoSuchElementException` instead), or when you're handling test data and an expected object isn't there.
2.  **`NoSuchElementException` (Selenium):** You tried to find an element with a locator (`By.id`, `By.xpath`, etc.) but it wasn't in the DOM when Selenium looked. This is a timing issue 99% of the time. The fix is an explicit wait.
3.  **`TimeoutException` (Selenium):** Your `WebDriverWait` gave up. You told it to wait for a condition for X seconds, and the condition never became true. This tells you the application is slower than your test expects, or something is broken. It's a test failure, and a good one. It caught a real issue.
4.  **`InvalidSelectorException` (Selenium):** Your XPath or CSS selector is garbage. The syntax is wrong. This is a coding error in your test itself. It should be caught and fixed immediately.

### Garbage collector

The GC's job is to free up memory by deleting objects that are no longer reachable. In Java, you don't `free()` memory yourself. The JVM does it for you.

**Why a QA engineer should care:**
*   **Memory Leaks:** If your application (or your test suite) has a memory leak, performance will degrade over time until it crashes with an `OutOfMemoryError`. Long-running regression suites can expose these leaks.
*   **Test Performance:** GC pauses can affect test execution time. If you're creating millions of objects in a tight loop in a performance test, the GC will be working overtime, and its pauses will skew your measurements. You need to be aware of this.
*   **Object Scope:** Understanding when an object becomes eligible for garbage collection is key to writing clean code. In a test, if you create a `WebDriver` instance, you must call `driver.quit()` in a `finally` block or using a `@After` hook. If you don't, the browser process might hang around, and the resources won't be cleaned up properly.

### Cucumber explain

Cucumber is a tool that runs automated tests written in a human-readable language called Gherkin. It's supposed to enable BDD (Behavior-Driven Development).

**The No-BS take:**
*   **The Good:** Gherkin (`Given`/`When`/`Then`) can, in theory, let non-technical people (like product owners) understand what tests do. It provides a layer of abstraction over your Java code.
*   **The Bad:** In 90% of teams, this abstraction becomes a liability. The Gherkin files get out of sync with the step definitions (the Java code). Only the developers write the Gherkin anyway, so the "non-technical person" benefit is lost. It adds another layer of indirection that makes debugging harder.

**A typical Gherkin scenario:**
```gherkin
Scenario: User logs in with valid credentials
  Given the user is on the login page
  When the user enters "testuser" and "password123"
  Then the user should be redirected to the dashboard
```
Each of those lines maps to a Java method in a "Step Definition" file. The real work happens in the Java. Cucumber just parses the text and calls the right methods.

### Hooks

In Cucumber, hooks are blocks of code that run at specific points in the test cycle. They are for setup and teardown.

*   `@Before`: Runs before each scenario. Good for setting up a `WebDriver` instance, clearing cookies, or seeding a database.
*   `@After`: Runs after each scenario, even if it fails. **CRITICAL** for cleanup. This is where you put `driver.quit()` and screenshot logic for failures.

```java
public class Hooks {

    private WebDriver driver;

    @Before
    public void setup() {
        this.driver = new ChromeDriver();
        driver.manage().window().maximize();
    }

    @After
    public void teardown(Scenario scenario) {
        if (scenario.isFailed()) {
            // Take a screenshot
            final byte[] screenshot = ((TakesScreenshot) driver).getScreenshotAs(OutputType.BYTES);
            scenario.attach(screenshot, "image/png", "failure-screenshot");
        }
        if (driver != null) {
            driver.quit();
        }
    }
}
```
> **What this shows:** You understand test lifecycle management. Unmanaged resources (like leftover browser windows) are a sign of an amateur.

### diff bw hooks and background

*   **`Background`:** It's Gherkin syntax. It's a set of `Given` steps that run before *every single scenario* in a feature file. It's for setting up a common state that all scenarios in that file need. It's part of the test's narrative.
*   **`@Before` Hook:** It's Java code. It also runs before every scenario, but it's invisible in the Gherkin feature file. It's for technical setup (starting a browser, setting up a mock server) that the business-facing Gherkin doesn't need to know about.

**Rule of thumb:**
*   If a product owner would understand and care about the step, put it in `Background`. (e.g., `Given the user is logged in as an administrator`)
*   If it's a purely technical setup step, use a `@Before` hook. (e.g., `startWebDriver()`)

### Jira tool

Jira is a project management tool. For a QA engineer, it's the source of truth.

*   **Bug Tracking:** This is our bread and butter. You find a bug, you write a Jira ticket. A good bug report is not a complaint; it's a technical document. It must include:
    *   A clear, concise title.
    *   Steps to reproduce (unambiguous and minimal).
    *   Expected result vs. Actual result.
    *   Environment details (browser, OS, app version).
    *   Logs, screenshots, video recordings.
*   **Test Case Management:** Jira can be used for this (with plugins like Zephyr or Xray), linking test cases to user stories and bugs. This creates traceability.
*   **Traceability:** You should be able to link a user story to the test cases that validate it, and to the bugs that were found while testing it. RTM is about this.

### RTM

Requirements Traceability Matrix. It's a table that maps requirements (user stories) to test cases.

| Requirement ID | Requirement Description | Test Case ID(s) |
| :------------- | :---------------------- | :-------------- |
| PROJ-123       | User can log in         | TC-001, TC-002  |
| PROJ-124       | User can log out        | TC-003          |

**Why it matters (sometimes):**
*   **Coverage:** It shows you have tests for every requirement. No gaps.
*   **Impact Analysis:** If a requirement changes, you can instantly see which tests need to be updated.
*   **Regulated Industries:** In finance or healthcare, you are often *required* by auditors to prove this traceability.

**The modern take:** In many Agile teams, the direct link inside Jira between a story and its associated tests (and the CI/CD build results) has replaced the formal RTM document. The principle is the same; the implementation is just more dynamic.

### diff bw smoke sanity and regression

These are scopes of testing. People argue about the definitions, but here's the practical breakdown.

*   **Smoke Test:** A shallow, wide test of the most critical functionality. Does the app start? Can you log in? Can you get to the main page? It's the first thing you run on a new build. If the smoke test fails, the build is rejected immediately. Don't waste time on further testing. It's a "build verification test."
*   **Sanity Test:** A narrow, deep test of a specific area of functionality, usually after a small change or bug fix. Did the fix I just made work, and did it not break anything obviously related? It's a quick check to see if the change is "sane."
*   **Regression Test:** The big one. A broad and deep set of tests designed to ensure that new code hasn't broken *any* existing functionality. This suite grows with the application and is usually automated. This is what you run before a release.

| Type       | Goal                               | Scope         | When to Run                        |
| :--------- | :--------------------------------- | :------------ | :--------------------------------- |
| **Smoke**  | Is the build stable enough to test?| Wide, Shallow | On every new build                 |
| **Sanity** | Did my recent change work?         | Narrow, Deep  | After a small code change or fix   |
| **Regression** | Did the new changes break old features? | Wide, Deep    | Before a release / on a schedule |

### diff bw adhoc and exploratory test

*   **Ad-hoc Testing:** Completely informal. You're just clicking around with no plan, hoping to find a bug. It's random and depends entirely on the tester's luck and mood. It's not structured and it's not repeatable.
*   **Exploratory Testing:** It's structured and systematic, but not scripted. It's a "thinking" activity. You have a mission or a charter (e.g., "Explore the user profile update functionality for security vulnerabilities"). You design and execute tests on the fly, and you document what you do and what you find. It's about learning the application while you test it.

Exploratory testing is a formal discipline. Ad-hoc testing is what your cousin does when you show them your new app.

### collection list and set

Both are interfaces in the Java Collections Framework that extend `Collection`.

*   **`List`:** An **ordered** collection. Elements have an index. You can access elements by their integer position. It **allows duplicates**.
    *   Common implementations: `ArrayList` (fast for random access), `LinkedList` (fast for adding/removing from the middle).
    *   **QA Use Case:** When you get a list of web elements from `findElements`, it's a `List`. The order is the order they appear in the DOM. You might assert that the first element has a specific text.

*   **`Set`:** An **unordered** collection. It **does not allow duplicates**. If you try to add an element that's already in the set, the add operation does nothing.
    *   Common implementations: `HashSet` (fast, uses `hashCode`), `LinkedHashSet` (maintains insertion order), `TreeSet` (maintains natural sorting order).
    *   **QA Use Case:** You need to verify that all the links on a page are unique. Scrape them all into a `List`, then add them all to a `HashSet`. If `list.size() != set.size()`, you have duplicate links.

```java
// List example
List<String> names = new ArrayList<>();
names.add("Alice");
names.add("Bob");
names.add("Alice"); // Duplicate is allowed
System.out.println(names.get(0)); // "Alice"
System.out.println(names.size()); // 3

// Set example
Set<String> uniqueNames = new HashSet<>();
uniqueNames.add("Alice");
uniqueNames.add("Bob");
uniqueNames.add("Alice"); // Duplicate is ignored
System.out.println(uniqueNames.size()); // 2
```

### why xml interact with html

This question is poorly phrased. "Interact" is the wrong word. The real connection is `XPath`, and historically, `XML` was the predecessor to many web technologies.

*   **XPath:** XPath (XML Path Language) is a query language for selecting nodes from an XML document. Since HTML (especially older XHTML) is structured like an XML document (with tags, attributes, and a tree structure), you can use XPath to navigate the HTML DOM.
*   **Selenium:** Selenium uses XPath as one of its primary locator strategies to find elements on a web page. `driver.findElement(By.xpath("//div[@id='login']"))` is using an XPath expression.

So, it's not that XML "interacts with" HTML. It's that a technology designed for XML (XPath) is also extremely useful for navigating HTML.

### iframe

An `iframe` (inline frame) is an HTML element that loads another HTML document within the current one. It's like a window into another webpage.

**From a QA perspective:**
*   **The Problem:** Selenium's context is, by default, the main page. If an element you want to interact with is inside an `iframe`, `driver.findElement()` will fail with `NoSuchElementException` because it's not looking in the right document.
*   **The Solution:** You must explicitly switch Selenium's context into the `iframe` before you can find elements inside it, and then switch back out when you're done.

```java
// 1. Switch into the iframe (by name, id, or as a WebElement)
driver.switchTo().frame("my-iframe");

// 2. Now you can find elements inside the iframe
WebElement buttonInFrame = driver.findElement(By.id("button-inside"));
buttonInFrame.click();

// 3. CRITICAL: Switch back to the main document context
driver.switchTo().defaultContent();
```

### dropdown

A dropdown is a UI element that lets you select one or more options from a list. In HTML, this is usually a `<select>` tag with `<option>` tags inside.

**How to handle it in Selenium:**
Selenium has a dedicated `Select` class to make this easy. Don't try to just click the options manually unless you have to (e.g., if it's a custom-built dropdown made of `div`s and `span`s).

```java
import org.openqa.selenium.support.ui.Select;

WebElement dropdownElement = driver.findElement(By.id("my-dropdown"));
Select dropdown = new Select(dropdownElement);

// 3 ways to select an option:
dropdown.selectByVisibleText("Option 3");
dropdown.selectByValue("value_3"); // based on the 'value' attribute of <option>
dropdown.selectByIndex(2); // 0-indexed
```
> **Side note:** If the dropdown is not a `<select>` element, you can't use the `Select` class. You have to treat it like any other custom UI component: click the main element to open the options, then wait for the desired option to be visible, then click it.

### action Class

It's `Actions` class in Selenium. You use it for complex user gestures that a simple `.click()` or `.sendKeys()` can't handle.

**What it's for:**
*   **Mouse Hover:** `moveToElement()` (e.g., to make a hidden menu appear).
*   **Right-Click:** `contextClick()`.
*   **Double-Click:** `doubleClick()`.
*   **Drag and Drop:** `dragAndDrop()`.

**How it works:** You build a sequence of actions and then call `.perform()` to execute them.

```java
import org.openqa.selenium.interactions.Actions;

Actions actions = new Actions(driver);

WebElement menu = driver.findElement(By.id("main-menu"));
WebElement subMenuItem = driver.findElement(By.id("sub-menu-item"));

// Build the action sequence: hover over menu, then click submenu item
actions.moveToElement(menu).click(subMenuItem).build().perform();
```
> **What they're testing:** Do you know how to handle interactive, modern web UIs? Not every element is just a simple click away.

### example for abstract and interface encapsulation inheritance

This is four concepts in one. Let's break them down from a QA framework design perspective.

*   **Encapsulation:** Hiding the implementation details of an object and only exposing a public interface. A Page Object Model (POM) is a perfect example.
    ```java
    // The details of the locators and the click logic are hidden.
    // The test only knows it can "login".
    public class LoginPage {
        private By usernameField = By.id("username");
        private By passwordField = By.id("password");
        private By loginButton = By.id("login");
        private WebDriver driver;

        public LoginPage(WebDriver driver) { this.driver = driver; }

        public void login(String username, String password) {
            driver.findElement(usernameField).sendKeys(username);
            driver.findElement(passwordField).sendKeys(password);
            driver.findElement(loginButton).click();
        }
    }
    ```

*   **Inheritance:** Creating a new class that is a type of an existing class. You use it for code reuse. In a test framework, you might have a `BasePage` that all your other page objects extend.
    ```java
    // BasePage has common functionality (header, footer, waits)
    public abstract class BasePage {
        protected WebDriver driver;
        public BasePage(WebDriver driver) { this.driver = driver; }
        public void clickLogo() { driver.findElement(By.id("logo")).click(); }
    }

    // LoginPage inherits from BasePage
    public class LoginPage extends BasePage {
        public LoginPage(WebDriver driver) { super(driver); }
        // ... login-specific methods
    }
    ```

*   **Abstract Class:** A class that cannot be instantiated. It's a blueprint. `BasePage` above is a good candidate to be `abstract`. It exists only to be extended. It can have both abstract methods (that subclasses *must* implement) and concrete methods (that subclasses inherit).

*   **Interface:** A contract. It defines what methods a class *must* implement, but provides no implementation. For example, you could define a `Searchable` interface for pages that have a search bar.
    ```java
    public interface Searchable {
        void searchFor(String query);
    }

    public class HomePage extends BasePage implements Searchable {
        public void searchFor(String query) {
            // implementation for searching from the home page
        }
    }

    public class SearchResultsPage extends BasePage implements Searchable {
        public void searchFor(String query) {
            // implementation for searching from the results page
        }
    }
    ```
> **What this shows:** Can you think about software architecture? A test suite isn't just a pile of scripts. It's a software project. These concepts are how you keep it from turning into an unmaintainable mess.

---

## Original Questions (UNTOUCHED)

Second round:
Self intro
Framework
Abstract use on my project
Interface use in my project
Method overload and override in my project
Waits
Which wait used in my project and syntex
Iframe and method syntax
Window handle
Diff between list and set
Final, finally, finalize
Access modifiers 
Wap for a count in given string
Wap for word count in gvn sentence
Swap the nos
Remove duplicate in array
Updates for current and previous project
Test case for ATM
Priority and severity
Synyax for oops and array and literal and non literal string
Report generation
cucumber plugins
xpath related ancestor, following, siblings, parent


---

## Answers (No-BS Java QA / SDET Explanations)

### Framework

"Tell me about your framework" is not about listing tools. It's about explaining the architecture you used to make testing scalable and maintainable.

A good answer has layers:
1.  **Core Tools:** "We used a Java-based stack with Selenium WebDriver for UI automation and REST-assured for API testing. TestNG was our test runner."
2.  **Design Pattern:** "We built it around the Page Object Model (POM) to separate UI interaction logic from our test logic. This keeps our tests clean and readable."
3.  **Data Management:** "Test data was managed using property files for static data and a TestDataFactory class for generating dynamic data like unique usernames."
4.  **Reporting:** "For reporting, we used ExtentReports, integrated with TestNG listeners to automatically capture screenshots on failure."
5.  **CI/CD Integration:** "The entire suite was run via Maven from a Jenkins pipeline. Tests were triggered on every commit to the dev branch and run in parallel on a Selenium Grid."

This answer shows you didn't just write scripts; you built a system.

### Abstract use on my project

See the answer in the first round. The canonical example is a `BasePage` or `BaseTest` class.

`BaseTest`:
*   **What it does:** Holds setup and teardown logic common to all tests.
*   **Why abstract?** You never want to create an instance of `BaseTest` itself. It's not a real test. It's a template for other tests.
*   **Example methods:** `@BeforeMethod` to initialize `WebDriver`, `@AfterMethod` to quit the driver.

```java
public abstract class BaseTest {
    protected WebDriver driver;

    @BeforeMethod
    public void setup() {
        // Driver initialization logic here
        driver = new ChromeDriver();
    }

    @AfterMethod
    public void teardown() {
        if (driver != null) {
            driver.quit();
        }
    }
}

public class LoginTest extends BaseTest {
    @Test
    public void testSuccessfulLogin() {
        // 'driver' is inherited from BaseTest
        LoginPage loginPage = new LoginPage(driver);
        loginPage.login("user", "pass");
        // ... assertions
    }
}
```

### Interface use in my project

See the answer in the first round. Interfaces define a contract.

A sharper example for test automation: Different third-party integrations.

Imagine your application can get user data from a database, a REST API, or a CSV file. You can abstract this away.

```java
// The contract: any user data source MUST be able to get a user by ID.
public interface UserDataSource {
    User getUserById(String id);
}

// Implementations
public class ApiUserSource implements UserDataSource {
    public User getUserById(String id) {
        // ... logic to call a REST API
    }
}

public class DbUserSource implements UserDataSource {
    public User getUserById(String id) {
        // ... logic to query a database
    }
}

// Your test uses the interface, so it doesn't care about the implementation.
// This allows you to easily swap out the data source for different test environments.
public class UserProfileTest {
    private UserDataSource dataSource;

    public UserProfileTest(UserDataSource source) {
        this.dataSource = source;
    }

    @Test
    public void testUserProfileData() {
        User user = dataSource.getUserById("123");
        // ... now test the UI against this user object
    }
}
```
This is dependency injection. It's a hallmark of a well-designed system, including a test framework.

### Method overload and override in my project

*   **Overriding:** This is runtime polymorphism. A subclass provides a specific implementation for a method that is already defined in its superclass. The `@Override` annotation is used.
    *   **Project Example:** You have a `BasePage` with a `verifyPageLoad()` method that just checks the title. A specific `DashboardPage` might override it to also check for the presence of a specific chart element, because just the title isn't enough to prove the page loaded correctly.

*   **Overloading:** This is compile-time polymorphism. You have multiple methods with the same name but different parameters (different type, different number, or both).
    *   **Project Example:** A common one is a custom `click()` method in a utility class.
    ```java
    public class ClickUtils {
        // Simple click
        public void click(WebElement element) {
            element.click();
        }

        // Click using JavaScript, as a fallback
        public void click(WebElement element, JavascriptExecutor js) {
            js.executeScript("arguments[0].click();", element);
        }

        // Click and wait for an element to disappear
        public void click(WebElement elementToClick, WebElement elementToDisappear, WebDriverWait wait) {
            elementToClick.click();
            wait.until(ExpectedConditions.invisibilityOf(elementToDisappear));
        }
    }
    ```

### Waits

There are three types. One of them is garbage.

1.  **Implicit Wait:** Garbage. Don't use it. It's a global setting on the `WebDriver` instance that tells it to wait a certain amount of time when trying to find an element. It sounds good, but it slows down your tests (it always waits for the full duration if an element is *not* present) and it can't handle conditions other than presence. It hides timing issues instead of fixing them.
2.  **Explicit Wait:** The correct choice. You use `WebDriverWait` and `ExpectedConditions` to wait for a *specific* condition to be true before proceeding. It's precise and deals with the actual state of the application.
3.  **Fluent Wait:** A more configurable version of `WebDriverWait`. You can specify the polling interval and exceptions to ignore. `WebDriverWait` is actually a subclass of `FluentWait`. You'd use it if you need fine-grained control, like checking for an element every 200ms instead of the default 500ms.

### Which wait used in my project and syntex

"I exclusively use explicit waits because they are deterministic and target specific application states, which is the only reliable way to write non-flaky UI tests."

**Syntax:**

```java
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.support.ui.ExpectedConditions;
import java.time.Duration;

// Setup the wait object, typically once per page or test
WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));

// Use it before an interaction
WebElement myElement = wait.until(ExpectedConditions.elementToBeClickable(By.id("my-button")));
myElement.click();
```
The key is `.until()`. It polls the condition until it returns true or the timeout is reached. If it times out, it throws a `TimeoutException`.

### Iframe and method syntax

Answered in the first round. The key methods are:
*   `driver.switchTo().frame(String nameOrId)`
*   `driver.switchTo().frame(int index)`
*   `driver.switchTo().frame(WebElement frameElement)`
*   `driver.switchTo().defaultContent()`
*   `driver.switchTo().parentFrame()` (to go up one level if you have nested iframes)

### Window handle

This is for when your application opens a new browser window or tab (e.g., by clicking a link with `target="_blank"`). Selenium's context remains on the original window. You have to explicitly switch to the new one.

Each window/tab has a unique ID, called a "window handle."

**The process:**
1.  Get the handle of the current window.
2.  Perform the action that opens a new window.
3.  Get all current window handles.
4.  Loop through the handles to find the one that is not the original handle.
5.  Switch to the new window.

```java
String originalWindow = driver.getWindowHandle();
assert driver.getWindowHandles().size() == 1;

driver.findElement(By.linkText("open new window")).click();

// Wait for the new window to open
wait.until(ExpectedConditions.numberOfWindowsToBe(2));

for (String windowHandle : driver.getWindowHandles()) {
    if(!originalWindow.contentEquals(windowHandle)) {
        driver.switchTo().window(windowHandle);
        break;
    }
}

// Now you are in the new window/tab
System.out.println("New window title: " + driver.getTitle());

// Close the new window and switch back
driver.close();
driver.switchTo().window(originalWindow);
```

### Diff between list and set

Answered in first round. List is ordered and allows duplicates. Set is unordered and requires uniqueness.

### Final, finally, finalize

They're testing if you know the difference between a language keyword, an exception handling block, and an object lifecycle method.

*   **`final`:** A keyword.
    *   **Variable:** You can't change its value. A constant.
    *   **Method:** You can't override it in a subclass.
    *   **Class:** You can't extend it (e.g., `String` is a final class).

*   **`finally`:** A block in a `try-catch` statement. The code inside `finally` is **always executed**, whether an exception was thrown or not. This is absolutely critical for cleanup.
    ```java
    WebDriver driver = null;
    try {
        driver = new ChromeDriver();
        // do test stuff... might throw an exception
    } finally {
        if (driver != null) {
            driver.quit(); // CRITICAL: This must always run to close the browser.
        }
    }
    ```

*   **`finalize()`:** A method from the `Object` class. The garbage collector calls this method on an object just before it's about to be destroyed. **You should almost never use this.** It's unpredictable when (or even if) it will be called. It's a deprecated concept for resource cleanup. Use `finally` blocks or `try-with-resources` instead. If you say you use `finalize()` in an interview, you've failed the question.

### Access modifiers

They control visibility.
*   **`public`:** Accessible from anywhere.
*   **`protected`:** Accessible within the same package, and by subclasses in other packages.
*   **Default (no modifier):** Accessible only within the same package.
*   **`private`:** Accessible only within the same class.

**In a test framework:**
*   Test methods (`@Test`) must be `public`.
*   Page Object methods that tests call (like `login()`) should be `public`.
*   Locators and internal helper methods within a page object should be `private`. This is encapsulation.
*   `BaseTest` fields like `WebDriver driver` are often `protected` so that subclass tests can access them.

### Wap for a count in given string

Assuming they mean character count. A `HashMap` is the classic way.

```java
import java.util.HashMap;
import java.util.Map;

public class CharCounter {
    public static Map<Character, Integer> countChars(String str) {
        if (str == null) {
            return new HashMap<>();
        }
        Map<Character, Integer> charCount = new HashMap<>();
        for (char c : str.toCharArray()) {
            // getOrDefault is cleaner than checking if the key exists
            charCount.put(c, charCount.getOrDefault(c, 0) + 1);
        }
        return charCount;
    }
}
```

### Wap for word count in gvn sentence

Split by whitespace. Be careful about punctuation and multiple spaces.

```java
import java.util.Arrays;
import java.util.Map;
import java.util.stream.Collectors;

public class WordCounter {
    public static long countWords(String sentence) {
        if (sentence == null || sentence.trim().isEmpty()) {
            return 0;
        }
        // A simple regex to split by one or more whitespace characters
        return sentence.trim().split("\\s+").length;
    }

    // If they want frequency of each word
    public static Map<String, Long> getWordFrequency(String sentence) {
         if (sentence == null || sentence.trim().isEmpty()) {
            return Map.of();
        }
        return Arrays.stream(sentence.trim().toLowerCase().split("\\s+"))
                     .collect(Collectors.groupingBy(word -> word, Collectors.counting()));
    }
}
```

### Swap the nos

This is a classic trick question. They want to see if you know the XOR swap or if you just use a temporary variable.

```java
public class Swapper {
    public static void swapWithTemp(int a, int b) {
        System.out.println("Before: a=" + a + ", b=" + b);
        int temp = a;
        a = b;
        b = temp;
        System.out.println("After: a=" + a + ", b=" + b);
    }

    // The "clever" way. Don't do this in production code. It's less readable.
    // But it's good to know for an interview.
    public static void swapWithoutTemp(int a, int b) {
        System.out.println("Before: a=" + a + ", b=" + b);
        a = a + b;
        b = a - b; // b is now original a
        a = a - b; // a is now original b
        System.out.println("After: a=" + a + ", b=" + b);
    }
}
```
> **Side note:** The temporary variable solution is better. It's clearer and expresses intent perfectly. The no-temp-var swap is a party trick. Show you know it, but also state that you'd use the clearer version in real code.

### Remove duplicate in array

The cleanest way is to use a `Set`.

```java
import java.util.Arrays;
import java.util.LinkedHashSet;
import java.util.Set;

public class DuplicateRemover {
    public static Integer[] removeDuplicates(int[] arr) {
        // Use a LinkedHashSet to preserve insertion order.
        Set<Integer> set = new LinkedHashSet<>();
        for (int i : arr) {
            set.add(i);
        }
        return set.toArray(new Integer[0]);
    }

    // Java 8+ one-liner
    public static int[] removeDuplicatesStream(int[] arr) {
        return Arrays.stream(arr).distinct().toArray();
    }
}
```
The stream version is superior. It's declarative and concise.

### Test case for ATM

This is a classic system design question for testers. They want to see how you think about a system's requirements, edge cases, and failure modes. Don't just list "test login." Structure your thinking.

*   **Functional / Positive Scenarios:**
    *   Valid card, valid PIN -> Display main menu.
    *   Check balance.
    *   Withdraw cash (within balance, within daily limit).
    *   Deposit cash/check.
    *   Transfer funds.
*   **Negative Scenarios:**
    *   Invalid card (expired, stolen, from another bank).
    *   Valid card, incorrect PIN (1st try, 2nd try, 3rd try -> lock card).
    *   Withdraw amount > current balance.
    *   Withdraw amount > daily limit.
    *   Withdraw amount that is not a multiple of the available notes (e.g., withdraw $25 when only $20 bills are available).
*   **Edge Cases / Other:**
    *   Session timeout (user walks away after logging in).
    *   Cancel transaction at various points.
    *   ATM runs out of cash.
    *   ATM runs out of receipt paper.
    *   Network failure during a transaction (this is a big one - the system must be atomic).
    *   Concurrent access (two people try to access the same account from two ATMs).

### Priority and severity

Two different axes for classifying a bug. 
*   **Severity:** How bad is the bug? What is the technical impact on the system?
    *   **Critical:** Crashes the system, data loss, security breach.
    *   **Major:** A major piece of functionality is completely broken.
    *   **Minor:** A minor feature doesn't work, or a major one has a small issue.
    *   **Trivial:** Cosmetic issue, typo.
*   **Priority:** How urgently does it need to be fixed? This is a business decision.
    *   **High:** Must fix now. It's blocking a release or costing the company money.
    *   **Medium:** Should be fixed in the normal course of development.
    *   **Low:** Fix if we have time.

**The classic example:** A typo in the company name on the home page.
*   **Severity:** Trivial. It doesn't break anything.
*   **Priority:** High. It looks unprofessional and is embarrassing.

### Synyax for oops and array and literal and non literal string

This is a grab-bag question. They want to see if you know basic Java syntax and terminology.

*   **OOPS (Object-Oriented Programming Concepts):**
    *   **Class:** Blueprint for objects (e.g., `public class LoginPage { ... }`).
    *   **Object:** An instance of a class (e.g., `WebDriver driver = new ChromeDriver();`).
    *   **Method:** A function within a class (e.g., `public void login(String user, String pass) { ... }`).
    *   **Inheritance:** `extends` keyword (e.g., `public class LoginTest extends BaseTest`).
    *   **Polymorphism:** Overriding (`@Override`) and Overloading (same method name, different parameters).
    *   **Encapsulation:** `private` fields, `public` methods.

*   **Array:** Fixed-size, ordered collection of elements of the same type.
    *   Declaration: `int[] numbers;`
    *   Initialization: `numbers = new int[5];`
    *   Access: `numbers[0] = 10;`
    *   Literal: `int[] nums = {1, 2, 3};`

*   **String Literal:** A fixed string value written directly in the code.
    *   `String message = "Hello";`
    *   String literals are immutable and often pooled by the JVM for efficiency.

*   **String Non-Literal (Object):** A string created using the `new` keyword.
    *   `String greeting = new String("Hello");`
    *   This creates a new object in the heap every time, even if the value is the same. Generally, you should prefer string literals.

### Report generation

In a test framework, this isn't about printing to the console. It's about creating a useful artifact after a test run.
*   **What should be in it?**
    *   Summary: How many tests passed, failed, skipped.
    *   Execution time.
    *   Detailed view of each test.
    *   For failed tests: Stack trace, error message, and **a screenshot** at the point of failure.
    *   Environment details (browser, OS, etc.).
*   **Tools:**
    *   **ExtentReports:** Very popular, creates beautiful HTML reports.
    *   **Allure:** Another powerful tool that can build trend charts and has great integrations.
    *   **TestNG/JUnit reports:** Basic XML/HTML reports that are good enough for CI/CD tools like Jenkins to parse.

You integrate these using test runner listeners (`ITestListener` in TestNG). The listener's `onTestFailure()` method is where you trigger the screenshot capture and log the failure details.

### cucumber plugins

Plugins customize Cucumber's output. You define them in the `@CucumberOptions` annotation.
*   **`pretty`:** Prints the Gherkin steps to the console in a readable format. Good for local debugging.
*   **`html:target/cucumber-reports.html`:** Generates a basic HTML report.
*   **`json:target/cucumber-report.json`:** Generates a JSON file with the test results. This is the important one. Other tools (like reporting libraries or Jenkins plugins) consume this JSON to create much better-looking reports.
*   **`junit:target/cucumber.xml`:** Generates a JUnit-style XML report, which is a standard format that most CI/CD tools understand.

```java
@CucumberOptions(
    features = "src/test/resources/features",
    glue = "com.myapp.stepdefs",
    plugin = { 
        "pretty", 
        "json:target/cucumber-report.json",
        "html:target/cucumber-report.html"
    }
)
public class TestRunner {
}
```

### xpath related ancestor, following, siblings, parent

These are XPath axes. They let you navigate the DOM tree from a known element (a "context node"). They are powerful but can lead to brittle tests if overused.

Assume your context node is an `input` field: `<input id="username">`

*   **`parent::*` or `..`**
    *   Selects the immediate parent of the context node.
    *   Example: `//input[@id='username']/parent::div` (selects the `div` that contains the input field).

*   **`ancestor::*`**
    *   Selects all ancestors (parent, grandparent, etc.) up to the root.
    *   Example: `//input[@id='username']/ancestor::form` (finds the form that the input field belongs to).

*   **`following-sibling::*`**
    *   Selects all sibling nodes that come *after* the context node.
    *   Example: `//label[@for='username']/following-sibling::input` (finds the input field that comes right after its label).

*   **`preceding-sibling::*`**
    *   Selects all sibling nodes that come *before* the context node.

*   **`following::*`**
    *   Selects *all* nodes in the document that appear after the context node, not just siblings. Use with caution.

*   **`preceding::*`**
    *   Selects *all* nodes that appear before the context node. Use with caution.

**Why use them?** They are essential for finding elements that don't have a good, stable ID or class of their own. You find a nearby stable element (like a label with text) and then navigate from there. This is a key skill for automating complex, legacy applications.

```java
// Example using XPath axes
// Find the input field that follows the label with text 'Username'
driver.findElement(By.xpath("//label[text()='Username']/following-sibling::input"));
```

---

## Original Questions (UNTOUCHED)

Capgemini L2:
Tell me about your project
Explain feature file using in your current project
Reverse 2 number without temporary variable
Int x = 10;
Int y = 20:
Reverse 2 string without temporary variable
String a = "India":
String b = "uk": 
String str = "123456" Convert into integer. 
What is wrapper class and what are they? 
String is a class Or datatype? 
What will be the output of the following?System.out.println (2+3+"HELLO");
Difference between array and arraylist?
Difference between list and set?
How to find duplicates in 2 arrays
int [] a = [1, 2,3,4,5,6];
int [] b = [8, 1,3,9,4];
Difference between
Webdriver driver = new ChromeDriver() ;
ChromeDriver driver = new ChromeDriver() :
How to interact with hidden elements in Selenium Webdriver?
What is action class and syntax?
How to use private variable in another class
What is API ? 
What is Mobile Testing? 
What to do if Two Objects have same Xpath?
What is the alternative for "click" in Selenium?
How many PR approval you'll get in your project?
What will be the answer if we compare 
s1==s2
s1==s3
  String s1 = "HELLO";
        String s2 = "HELLO";
        String s3 =  new String("HELLO"):
System.out.println(s1==s2) //true
        System.out.println(s1 == s3); // false

---

## Answers (No-BS Java QA / SDET Explanations)

> Many of these are repeats. See previous answers for details.

### Reverse 2 number without temporary variable
`x = x + y; y = x - y; x = x - y;`

### Reverse 2 string without temporary variable
`a = a + b; b = a.substring(0, a.length() - b.length()); a = a.substring(b.length());`

### String str = "123456" Convert into integer. 
`Integer.parseInt(str);`

### What is wrapper class and what are they? 
Classes that wrap primitives into objects (e.g., `Integer`). Necessary for collections.

### String is a class Or datatype? 
It's a **class** (`java.lang.String`), a reference type.

### What will be the output of the following? System.out.println (2+3+"HELLO");
**"5HELLO"**. The `2+3` addition happens first, then the result `5` is concatenated with the string.

### Difference between array and arraylist?
Array is fixed-size. `ArrayList` is dynamic and part of the Collections Framework.

### Difference between list and set?
`List` is ordered, allows duplicates. `Set` is unordered, unique elements only.

### How to find duplicates in 2 arrays
Use a `Set`. Iterate through the first array and add all elements to the set. Then, iterate through the second array and for each element, check if it's already in the set. If it is, you've found a duplicate between the two arrays. A more efficient way is to convert one to a Set and use `retainAll` on a Set made from the second array.

```java
Set<Integer> setA = new HashSet<>(Arrays.asList(a));
Set<Integer> setB = new HashSet<>(Arrays.asList(b));
setA.retainAll(setB); // setA now contains only the elements present in both
System.out.println("Duplicates: " + setA);
```

### Difference between
`Webdriver driver = new ChromeDriver()` and 
`ChromeDriver driver = new ChromeDriver()`
Coding to an interface (`WebDriver`) vs. an implementation (`ChromeDriver`). Coding to the interface is correct. It makes your code portable to other browsers.

### How to interact with hidden elements in Selenium Webdriver?
You can't with standard Selenium commands. You must use `JavascriptExecutor` as a last resort: `((JavascriptExecutor) driver).executeScript("arguments[0].click();", hiddenElement);`

### What is action class and syntax?
The `Actions` class, for complex user gestures. `Actions actions = new Actions(driver); actions.moveToElement(element).perform();`

### How to use private variable in another class
You don't. You provide `public` getter/setter methods. This is encapsulation.

### What is API ?
Application Programming Interface. A contract for software to talk to each other, typically via HTTP and JSON.

### What is Mobile Testing? 
Testing applications on mobile devices (native apps or mobile web). **Appium** is the key tool to mention here.

### What to do if Two Objects have same Xpath?
-   `findElements` will return a `List` of them. You can then pick one by its index: `driver.findElements(By.xpath(xpath)).get(1)` for the second one.
-   You can also add an index directly to the XPath: `(//div[@class='product'])[2]`

### What is the alternative for "click" in Selenium?
1.  **JavaScript Click:** `((JavascriptExecutor) driver).executeScript("arguments[0].click();", element);` (The "hammer").
2.  **Actions Class Click:** `new Actions(driver).click(element).perform();`
3.  **Send ENTER key:** `element.sendKeys(Keys.ENTER);` (Works for submit buttons).

### How many PR approval you'll get in your project?
A process question. "My team required at least one approval from another engineer before merging a pull request."

### What will be the answer if we compare 
s1==s2
s1==s3
  String s1 = "HELLO";
        String s2 = "HELLO";
        String s3 =  new String("HELLO"):
System.out.println(s1==s2) //true
        System.out.println(s1 == s3); // false

This tests knowledge of the String Constant Pool.
-   `String s1 = "HELLO";` and `String s2 = "HELLO";` both point to the *same object* in the pool.
-   `String s3 = new String("HELLO");` forces the creation of a *new object* on the heap.

-   `s1 == s2` -> **true** (references are identical).
-   `s1 == s3` -> **false** (references are different).
-   The code in the prompt is correct.

```java
```
