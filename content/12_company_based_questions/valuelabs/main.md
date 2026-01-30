---
title: "Valuelabs"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

- Valuelabs Interview Questions : SDET 4.5 to 6 years
------------------------------------------------
1. Please introduce yourself.
2. Please explain your Automation Framework, all the components.
3. What is a Page Object Model?
4. How do you run your test cases in parallel in Cucumber?
5. Explain the contents of the Runner File in Cucumber?
6. What is a Singleton Design Pattern?
7. What are the advantages and disadvantages of the Page Object Model?
8. What is Selenium Grid?
9. Explain the WebDriver create statement line?
11. Explain the Maven Lifecycle?
12. How do you run the failed test cases?
13. How do you generate Reports in Selenium?
14. How do you customise reports after your test execution?
15. What kind of waits are there in Selenium?
16. Write the Code Snippet for Explicit Wait?
17. Write the Code Snippet for Drag and Drop in Selenium?
18. How do you switch to different Windows in Selenium?
19. Why do we use SET in Window Handles?
20. Write the Code for taking screenshot in Selenium?
21. What is the difference between Scenario and Scenario Outline in Cucumber?
22. How do you pass data to your Selenium Scripts?
23. How do you decide the priorities of your Test Cases?
24. If you want to execute one test case again and again how do you do that?
25. What are the different annotations used in TestNG?
26. Write the hierarchy of annotations in TestNG?
27. What is the defect life cycle?
28. What is the difference between Agile and Waterfall Model?
29. What is the difference between 201 and 204 Status Code?
30. What is the difference between 401 and 403 Status Code?
31. What are the components of an API Request?
32. What is the difference between Query Parameters and Path Parameters?
33. How do you resolve Conflicts in Git?
34. What is the difference between git pull and git patch?
35. Explain the use of Jenkins in the Automation Framework?

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. Please introduce yourself.
Standard opener. Focus on professional experience, automation skills, tech stack, and achievements relevant to an SDET role.

### 2. Please explain your Automation Framework, all the components.
"Our automation framework is a Java-based, hybrid, data-driven framework.
-   **Core Tools:** TestNG for test execution, Selenium WebDriver for UI automation, REST-assured for API automation, Maven for build/dependency management.
-   **Design:** It follows the **Page Object Model (POM)** for UI and uses a custom API client for API tests. We have `BaseTest` classes for common setup/teardown.
-   **Data:** Test data is externalized in JSON files and supplied via TestNG `@DataProvider`.
-   **Reporting:** We use **ExtentReports** integrated via TestNG listeners for rich HTML reports with screenshots on failure.
-   **CI/CD:** Tests are executed via **Jenkins** pipelines."

### 3. What is a Page Object Model?
A design pattern for UI test automation where each page (or significant component) of a web application is represented as a class. This class encapsulates all the locators and interaction methods for that page, abstracting the UI details from the test scripts. It improves maintainability, reusability, and readability.

### 4. How do you run your test cases in parallel in Cucumber?
Cucumber itself doesn't directly handle parallel execution of scenarios. You rely on the test runner.
-   **TestNG:** If you use TestNG to run Cucumber, you can configure `testng.xml` with `parallel="methods"` and `thread-count`. Each scenario would typically be run in a separate thread.
-   **JUnit:** For JUnit, you can use `maven-failsafe-plugin` with forks, or specific JUnit 5 parallel execution strategies.
-   **JVM Arguments:** For Cucumber-JVM, you can configure `max-threads` in the `cucumber.properties` file or via JVM arguments to specify the maximum number of parallel threads.
-   **Selenium Grid:** The actual browsers are typically run in parallel on a Selenium Grid.

### 5. Explain the contents of the Runner File in Cucumber?
A Cucumber Runner file (a Java class) is the entry point for executing Cucumber tests.
-   **`@RunWith(Cucumber.class)`:** Tells JUnit how to run the class.
-   **`@CucumberOptions`:** Configures Cucumber:
    -   `features`: Path to `.feature` files.
    -   `glue`: Path to step definition packages.
    -   `plugin`: Reporting formats (e.g., `html`, `json`).
    -   `tags`: Filters scenarios to run (e.g., `@smoke`).
    -   `dryRun`: Checks for undefined steps without execution.

### 6. What is a Singleton Design Pattern?
A Singleton is a creational design pattern that restricts the instantiation of a class to a **single object**. It ensures that there's only one instance of the class and provides a global point of access to that instance.
-   **Use in Project:** "In our framework, we implemented the `WebDriverFactory` class using the Singleton pattern. This ensures that only one instance of the WebDriver (browser) is created and managed throughout the test run, which is crucial for controlling browser lifecycle and preventing multiple, unmanaged browser instances."

### 7. What are the advantages and disadvantages of the Page Object Model?
-   **Advantages:**
    -   **Maintainability:** Changes to the UI only require updates in the page object, not across multiple test scripts.
    -   **Reusability:** Page object methods can be reused across different test cases.
    -   **Readability:** Test scripts become cleaner, more business-readable, and free of UI implementation details.
    -   **Abstraction:** Abstracts the technical details of the UI from the test logic.
-   **Disadvantages:**
    -   **Initial Setup Time:** Requires more time to set up initially.
    -   **Increased Codebase:** Can lead to a larger number of classes for complex applications.
    -   **Learning Curve:** Team members need to understand the pattern.

### 8. What is Selenium Grid?
Selenium Grid is a proxy server that allows you to run Selenium WebDriver tests in parallel on multiple machines, using different browsers and operating systems. It consists of a Hub (central server) and multiple Nodes (machines running browser instances).

### 9. Explain the WebDriver create statement line?
`WebDriver driver = new ChromeDriver();`
-   **`WebDriver`:** This is an **interface** in Selenium. It defines the contract for browser automation.
-   **`driver`:** This is a reference variable of type `WebDriver`.
-   **`new ChromeDriver()`:** This creates an actual object (an instance) of the `ChromeDriver` class, which is a concrete implementation of the `WebDriver` interface specific to Google Chrome.
-   **Polymorphism:** This line demonstrates polymorphism (coding to an interface), allowing the `driver` variable to control any browser that implements the `WebDriver` interface.

### 11. Explain the Maven Lifecycle?
Maven has three built-in build lifecycles, each composed of phases:
1.  **`default`:** Handles project deployment (e.g., `validate`, `compile`, `test`, `package`, `install`, `deploy`). `mvn test` runs up to the `test` phase.
2.  **`clean`:** Handles project cleaning (e.g., `clean` phase deletes `target` directory).
3.  **`site`:** Handles creation of project site documentation.

### 12. How do you run the failed test cases?
-   **TestNG:** `testng-failed.xml` is generated after a run. Execute this XML file.
-   **Cucumber:** You can specify `@CucumberOptions(tags = "@rerun")` if your framework supports it after a rerun file is generated, or run a dynamically created rerun file.
-   **`IRetryAnalyzer` (TestNG):** Implement this interface to automatically re-run failed tests a specified number of times.

### 13. How do you generate Reports in Selenium?
Selenium WebDriver itself doesn't generate reports. It's usually done via:
-   **TestNG/JUnit:** These test runners generate basic HTML/XML reports.
-   **Third-party Libraries:** Integrate tools like **ExtentReports** or **Allure Reports** with your test runner (e.g., via TestNG listeners) to produce rich, interactive HTML reports.

### 14. How do you customise reports after your test execution?
"We customize our reports using **ExtentReports**.
-   **Configuration:** We configure the `ExtentSparkReporter` to set the report name, theme, and title.
-   **Logging:** We use `ExtentTest` objects to log test steps, status (pass/fail/skip), and embed screenshots for failures.
-   **Listeners:** All this is automated via a custom TestNG `ITestListener` that manages the lifecycle of the ExtentReport and logs events."

### 15. What kind of waits are there in Selenium?
-   **Implicit Wait (Avoid):** Global setting.
-   **Explicit Wait (Recommended):** `WebDriverWait` for specific `ExpectedConditions`.
-   **Fluent Wait:** Highly configurable explicit wait.

### 16. Write the Code Snippet for Explicit Wait?
```java
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.time.Duration;

public void waitForElement(WebDriver driver, By locator) {
    WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(15)); // Max 15 seconds
    WebElement element = wait.until(ExpectedConditions.elementToBeClickable(locator));
    element.click(); // Now safe to click
}
```

### 17. Write the Code Snippet for Drag and Drop in Selenium?
```java
import org.openqa.selenium.interactions.Actions;

public void dragAndDropElement(WebDriver driver, WebElement source, WebElement target) {
    Actions actions = new Actions(driver);
    actions.dragAndDrop(source, target).perform();
}
```

### 18. How do you switch to different Windows in Selenium?
Using window handles.
1.  Get all handles: `Set<String> allHandles = driver.getWindowHandles();`
2.  Iterate to find the target window (e.g., by title): `for (String handle : allHandles) { driver.switchTo().window(handle); if (driver.getTitle().contains("Desired Title")) break; }`
3.  Switch back: `driver.switchTo().window(originalHandle);`

### 19. Why do we use SET in Window Handles?
`Set<String>` is used for window handles because each window handle is **unique**, and the order in which they appear is **not guaranteed** to be consistent across different test runs or browsers. A `Set` naturally handles unique, unordered collections.

### 20. Write the Code for taking screenshot in Selenium?
```java
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import java.io.File;
import org.apache.commons.io.FileUtils;

public void takeScreenshot(WebDriver driver, String filePath) {
    File src = ((TakesScreenshot) driver).getScreenshotAs(OutputType.FILE);
    FileUtils.copyFile(src, new File(filePath));
}
```

### 21. What is the difference between Scenario and Scenario Outline in Cucumber?
-   **`Scenario`:** A single, concrete test case that runs once.
-   **`Scenario Outline`:** A template for a scenario that runs multiple times with different data provided in an `Examples` table. Used for data-driven testing.

### 22. How do you pass data to your Selenium Scripts?
-   **`@DataProvider` (TestNG):** Reads data from external sources (JSON, Excel) and supplies it to test methods.
-   **Cucumber `Scenario Outline` with `Examples` table:** For data-driven BDD.
-   **Configuration Files:** `.properties` or JSON files for environment-specific parameters.

### 23. How do you decide the priorities of your Test Cases?
Test case priorities are typically determined by:
-   **Business Criticality:** How important is the feature to the business? (e.g., Login, Checkout are high).
-   **Frequency of Use:** How often is the feature used by end-users?
-   **Risk Assessment:** What is the impact if this feature fails?
-   **Dependency:** Tests that are prerequisites for other tests might have higher priority.

### 24. If you want to execute one test case again and again how do you do that?
-   **TestNG `invocationCount`:** Use `@Test(invocationCount = X)` to run a test method X times.
-   **Loops (in code):** Wrap the test logic in a `for` loop, though generally less preferred for TestNG.

### 25. What are the different annotations used in TestNG?
-   `@Test`
-   `@BeforeSuite`, `@AfterSuite`
-   `@BeforeTest`, `@AfterTest`
-   `@BeforeClass`, `@AfterClass`
-   `@BeforeMethod`, `@AfterMethod`
-   `@DataProvider`, `@Parameters`
-   `@Listeners`

### 26. Write the hierarchy of annotations in TestNG?
`@BeforeSuite -> @BeforeTest -> @BeforeClass -> @BeforeMethod -> @Test -> @AfterMethod -> @AfterClass -> @AfterTest -> @AfterSuite`.

### 27. What is the defect life cycle?
(Bug life cycle). New -> Open/Assigned -> Fixed -> Ready for QA -> Closed (or Reopened).

### 28. What is the difference between Agile and Waterfall Model?
-   **Agile:** Iterative, incremental, flexible, customer collaboration, short sprints.
-   **Waterfall:** Linear, sequential, rigid, phases completed in order, less flexible to changes.

### 29. What is the difference between 201 and 204 Status Code?
-   **`201 Created`:** Indicates successful resource **creation** (typically after a `POST`). Response often contains the newly created resource or a link to it.
-   **`204 No Content`:** Indicates successful request processing, but there is **no content** to return in the response body (typically after a `DELETE` or `PUT` that doesn't need to send data back).

### 30. What is the difference between 401 and 403 Status Code?
-   **`401 Unauthorized`:** Client **lacks valid authentication credentials**. You are not logged in or your token is invalid.
-   **`403 Forbidden`:** Client is **authenticated, but does not have permission** to access the requested resource. You are logged in, but you're not allowed to do that.

### 31. What are the components of an API Request?
1.  **URL (Endpoint):** The address of the resource (e.g., `https://api.example.com/users`).
2.  **HTTP Method (Verb):** `GET`, `POST`, `PUT`, `DELETE`.
3.  **Headers:** Metadata about the request (e.g., `Content-Type`, `Authorization`).
4.  **Request Body (Payload):** Data sent with the request (for `POST`, `PUT`, `PATCH`), usually in JSON format.

### 32. What is the difference between Query Parameters and Path Parameters?
-   **Query Parameters:** Key-value pairs after `?` in URL, used for filtering, sorting (e.g., `/products?category=electronics`).
-   **Path Parameters:** Variables embedded directly in the URL path, used to identify a specific resource (e.g., `/users/{id}`).

### 33. How do you resolve Conflicts in Git?
1.  Pull latest changes from remote.
2.  Git will indicate conflicted files.
3.  Manually edit the conflicted files, choosing which changes to keep.
4.  `git add` the resolved files.
5.  `git commit` to finalize the merge.

### 34. What is the difference between git pull and git patch?
-   **`git pull`:** Fetches changes from a remote repository and automatically merges them into your current local branch. It's a combination of `git fetch` and `git merge`.
-   **`git patch`:** (`git format-patch` to create, `git apply` to apply) Creates a small file (a "patch") that represents the changes between two commits. This patch file can then be emailed or shared, and another developer can apply these changes to their repository. It's a way to transfer changes without a full merge, often used in open-source projects or when direct repository access isn't available.

### 35. Explain the use of Jenkins in the Automation Framework?
Jenkins serves as our **Continuous Integration (CI)** server. It automates the execution of our test automation framework.
-   **Triggers:** Configured to automatically run our tests (unit, API, UI regression) upon every code commit or on a schedule.
-   **Execution:** Pulls the latest code, builds the project (Maven), and executes the test suite.
-   **Reporting:** Publishes test reports and notifies the team of failures.
-   **Benefits:** Provides immediate feedback on code quality, helps catch bugs early, and ensures the test suite is always running against the latest code.
