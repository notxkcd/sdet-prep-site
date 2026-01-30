---
title: "INCEDOINC"
date: 2026-01-30
draft: false
---

---

## Original Questions

INCEDOINC:

1.Oops concepts fully.
2.findByElement and findByElements
3.How do we pass testdata?
4.where we maintain our Testcases?
5.wait types
6.syntax for explicit wait
7.multi threading concept
8.WAP to remove duplicates in array
9.different between navigate and get
10.difference between string and stringbuffer
11.polymorphism
12.Priority
12.severity
13.end to end testing
14.tell about your framework
15.dependency name for passing excel document..

---

## Answers

### 1. Oops concepts fully.
The four pillars, explained with a test automation focus.
-   **Encapsulation:** Hiding implementation details. The Page Object Model is the classic example. Your test calls `loginPage.login()` and doesn't know or care about the locators or the sequence of `sendKeys` and `click` calls within the method.
-   **Abstraction:** Hiding complexity. The `WebDriver` interface is the prime example. You code against the `WebDriver` interface (`driver.get()`, `driver.findElement()`), abstracting away the specific browser implementation (`ChromeDriver`, `FirefoxDriver`).
-   **Inheritance:** Reusing common code. A `BaseTest` class with `@BeforeMethod` and `@AfterMethod` to handle driver setup and teardown, which all your test classes `extend`.
-   **Polymorphism:** "Many forms." Primarily method overriding. A `BasePage` might have a `verifyPageLoaded()` method. The `HomePage` and `ProductPage` both override this method to add their own specific checks (e.g., checking for a banner vs. checking for a product price).

### 2. findByElement and findByElements
The method names are `findElement` and `findElements`.
-   **`findElement(By locator)`:**
    -   Finds the **first** matching element on the page.
    -   **Returns:** A single `WebElement` object.
    -   **If not found:** Throws a `NoSuchElementException`, which will typically fail your test.

-   **`findElements(By locator)`:**
    -   Finds **all** matching elements on the page.
    -   **Returns:** A `List<WebElement>`.
    -   **If not found:** Returns an **empty list**. It does **not** throw an exception. This is useful for verifying that an element *does not* exist (`driver.findElements(locator).isEmpty()`).

### 3. How do we pass testdata?
In a professional framework, you externalize test data.
1.  **TestNG's `@DataProvider`:** The best way for data-driven tests. A method annotated with `@DataProvider` returns an `Object[][]`. The test method runs once for each row of data.
2.  **External Files:** The `@DataProvider` method itself reads the data from an external source.
    -   **JSON files:** Clean, easy to read, and easy to parse with libraries like Jackson or Gson.
    -   **Excel files:** Common in enterprise, especially if business users need to provide data. You use a library like **Apache POI** to read `.xls` or `.xlsx` files.
    -   **Properties files:** Good for simple key-value configuration data (like URL, browser, timeouts).

### 4. where we maintain our Testcases?
-   **Test Case Management Tool:** The professional answer. Tools like **Jira** (with plugins like Xray or Zephyr), **TestRail**, or **qTest**. These tools allow you to write test cases, link them to requirements (user stories), track their execution status against different builds, and generate reports on coverage and pass rates.
-   **In the code (BDD):** If you're using a BDD framework like Cucumber, the `.feature` files themselves act as the test cases and living documentation. They are maintained directly in the Git repository alongside the code.

### 5. wait types
There are three types. One is good, one is bad, one is advanced.
-   **Implicit Wait:** **Bad.** A global setting on the driver to poll the DOM for a certain amount of time. It's a blunt instrument that hides timing problems and slows down tests. Avoid it.
-   **Explicit Wait:** **Good.** The correct way to handle synchronization. You use `WebDriverWait` to wait for a *specific condition* to be true before proceeding (e.g., element is clickable, element is visible). It's precise and reliable.
-   **Fluent Wait:** An advanced version of explicit wait. It allows you to configure the polling frequency and exceptions to ignore. `WebDriverWait` is just a pre-configured `FluentWait`.

### 6. syntax for explicit wait
```java
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.time.Duration;

public class WaitExample {
    public void demonstrateWait(WebDriver driver) {
        // 1. Create a WebDriverWait instance
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));

        // 2. Use the 'until()' method with an ExpectedCondition
        WebElement element = wait.until(ExpectedConditions.elementToBeClickable(By.id("submit-button")));

        // 3. Now you can safely interact with the element
        element.click();
    }
}
```

### 7. multi threading concept
Multithreading is a form of concurrency where you execute multiple threads (lightweight processes) simultaneously within a single program. Each thread has its own call stack, but they share the same memory (heap space).

**Why a QA engineer cares:**
1.  **Test Execution Speed:** You can run your Selenium tests in parallel using TestNG's parallel execution features. TestNG assigns each test to a separate thread, allowing you to run, for example, 5 tests at once instead of one after the other, drastically reducing total execution time.
2.  **Testing Concurrent Applications:** If the application itself is multi-threaded, you need to write tests that check for concurrency issues like **race conditions** (where the outcome depends on the unpredictable timing of threads) and **deadlocks**. This is advanced but critical for robust backend services.
3.  **Thread Safety:** You need to ensure your own framework utilities are thread-safe if they are shared between parallel tests. For example, if you have a static reporting object, you must synchronize access to it to prevent threads from overwriting each other's report entries. This is why managing `WebDriver` instances in a `ThreadLocal` is a common pattern in parallel test frameworks.

### 8. WAP to remove duplicates in array
The cleanest and most common way is to use a `Set`, which by definition cannot contain duplicates.

```java
import java.util.Arrays;
import java.util.LinkedHashSet;
import java.util.Set;

public class DuplicateRemover {
    // The Java 8+ Streams way. It's concise and declarative.
    public int[] removeDuplicates(int[] arr) {
        return Arrays.stream(arr).distinct().toArray();
    }

    // The classic Set way, which preserves insertion order if you use LinkedHashSet.
    public Integer[] removeDuplicatesWithSet(int[] arr) {
        Set<Integer> set = new LinkedHashSet<>();
        for (int i : arr) {
            set.add(i);
        }
        return set.toArray(new Integer[0]);
    }
}
```

### 9. different between navigate and get
Both are methods on the `driver` object to open a URL, but `navigate()` is more powerful.

-   **`driver.get(String url)`:**
    -   The simpler method. It loads a new web page.
    -   It will wait for the page to fully load before returning control to your script.

-   **`driver.navigate()`:**
    -   Returns a `Navigation` object that provides more capabilities.
    -   `driver.navigate().to(String url)`: Does the same thing as `driver.get()`.
    -   **`driver.navigate().back()`:** Simulates clicking the browser's back button.
    -   **`driver.navigate().forward()`:** Simulates clicking the browser's forward button.
    -   **`driver.navigate().refresh()`:** Simulates clicking the browser's refresh button.

**In short:** `get()` just loads a page. `navigate()` lets you load a page *and* move through the browser's history.

### 10. difference between string and stringbuffer
-   **`String`:**
    -   **Immutable.** Its value cannot be changed after creation. Any "modification" creates a new `String` object.
    -   Thread-safe by nature of being immutable.
    -   Good for general use where the value doesn't change often.

-   **`StringBuffer`:**
    -   **Mutable.** Its value can be changed after creation using methods like `append()`, `insert()`, `delete()`.
    -   **Thread-safe.** Its methods are synchronized, which adds overhead and makes it slower than `StringBuilder`.
    -   Use it only when you need to modify a string from **multiple threads** simultaneously (which is very rare). For single-threaded string building, use `StringBuilder`.

### 11. polymorphism
"Many forms." In OOP, it's the ability for an object of a child class to be treated as an object of its parent class. The most practical use is **method overriding**, where a subclass provides its own specific implementation of a method defined in its parent.

Example: `WebDriver driver = new ChromeDriver();` The `driver` object is a `ChromeDriver`, but it's being treated as a `WebDriver`, demonstrating polymorphism.

### 12. Priority and severity
-   **Severity:** The technical impact of the bug. How badly does it break the system? (e.g., Critical, Major, Minor). Set by QA.
-   **Priority:** The business urgency to fix the bug. How quickly does it need to be fixed? (e.g., High, Medium, Low). Set by the Product Owner.

### 13. end to end testing
End-to-end (E2E) testing is a methodology used to test an application's flow from start to finish, simulating a real user scenario.
-   It validates the entire system, including its integration with external dependencies like databases, APIs, and other services.
-   In a web application, an E2E test might involve:
    1.  Opening the browser and logging in.
    2.  Searching for a product.
    3.  Adding the product to the cart.
    4.  Proceeding through checkout.
    5.  Verifying the order confirmation.
-   The goal is to ensure the complete user workflow functions as expected. These tests are typically automated with tools like Selenium or Cypress.

### 14. tell about your framework
Standard question. Describe the architecture.
-   Core tech stack (Java, TestNG, Selenium).
-   Design patterns (Page Object Model).
-   Data management (DataProvider, JSON/Excel files).
-   Utilities (Waits, Reporting).
-   CI/CD integration (Maven, Jenkins).

### 15. dependency name for passing excel document..
The standard Java library for working with Microsoft Office documents, including Excel, is **Apache POI**.

You would add the following dependencies to your `pom.xml`:

```xml
<!-- For .xls and .xlsx files -->
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi-ooxml</artifactId>
    <version>5.2.2</version>
</dependency>

<!-- You might also need the base poi dependency -->
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi</artifactId>
    <version>5.2.2</version>
</dependency>
```
The key name to remember is **Apache POI**.
