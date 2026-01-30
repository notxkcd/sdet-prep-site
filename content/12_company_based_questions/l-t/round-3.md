---
title: "L_T-3"
date: 2026-01-30
draft: false
---

---

## Original Questions

L & T
--------------------------------
1.If you are given an angular application create a framework?
2.Code in selenium grid for parallel execution ?
3.How to run chrome in headless mode in selenium-java?
4.Boundary Value Analysis (BVA)?
5.Difference between Oracle n Sql?
6. SQL command to get common in two tables?
7.What is Structure in SQL?
8.What will you do if you detect a defect?
9.Bug life Cycle?
10.What is Constructor?
11.What is interface and keyword used?
12.What is Inheritance and keyword used?
13.How is Inheritance used in your selenium project?
14.What does 302 Status code stands for?
15.What is deferred bug?

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. If you are given an angular application create a framework?
"For an Angular application, I would build a Java-based test automation framework, much like for any other web application, but with some specific considerations:
-   **Core Tools:** Selenium WebDriver for UI automation (Java), TestNG as the test runner, Maven for build management.
-   **Locators:** Angular applications often rely on dynamic IDs. I'd prioritize `cssSelector` over `xpath` where possible, and actively collaborate with developers to introduce stable `data-testid` attributes.
-   **Synchronization:** Angular apps are highly dynamic. Extensive use of **Explicit Waits** (`WebDriverWait` with `ExpectedConditions`) would be critical to handle AJAX calls and dynamic element loading.
-   **Page Object Model:** Absolutely essential to manage the complex UI components and keep locators centralized.
-   **Protractor/Cypress (alternative):** While Selenium can test Angular, if the team is already JavaScript-heavy, I might also consider suggesting a JavaScript-based tool like **Cypress** or **Playwright**, as they often provide better native synchronization and integration with modern JS frameworks."

### 2. Code in selenium grid for parallel execution ?
To use Selenium Grid, your `WebDriver` initialization code needs to connect to the Grid Hub. Parallel execution is configured in `testng.xml`.

```java
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Parameters;
import java.net.URL;

public class BaseTestGrid {
    protected WebDriver driver;

    @BeforeMethod
    @Parameters("browser") // Passed from testng.xml
    public void setup(String browser) throws Exception {
        DesiredCapabilities caps = new DesiredCapabilities();
        if (browser.equalsIgnoreCase("chrome")) {
            caps.setBrowserName("chrome");
        } else if (browser.equalsIgnoreCase("firefox")) {
            caps.setBrowserName("firefox");
        }
        // Connect to the Selenium Grid Hub
        driver = new RemoteWebDriver(new URL("http://localhost:4444/wd/hub"), caps);
        driver.manage().window().maximize();
    }

    @AfterMethod
    public void teardown() {
        if (driver != null) {
            driver.quit();
        }
    }
}
```

**`testng.xml` for parallel execution:**
```xml
<!DOCTYPE suite SYSTEM "https://testng.org/testng-1.0.dtd" >
<suite name="GridSuite" parallel="tests" thread-count="2">

  <test name="ChromeTest">
    <parameter name="browser" value="chrome"/>
    <classes>
      <class name="com.myproject.tests.LoginTest"/>
    </classes>
  </test>
  
  <test name="FirefoxTest">
    <parameter name="browser" value="firefox"/>
    <classes>
      <class name="com.myproject.tests.LoginTest"/>
    </classes>
  </test>

</suite>
```

### 3. How to run chrome in headless mode in selenium-java?
Headless mode means running the browser without a visible UI. It's often used in CI/CD environments for faster execution.

```java
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

public class HeadlessChrome {
    public static WebDriver getHeadlessChromeDriver() {
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--headless"); // The key argument
        options.addArguments("--disable-gpu"); // Recommended for Windows
        options.addArguments("--window-size=1920,1080"); // Set a large window size

        WebDriver driver = new ChromeDriver(options);
        return driver;
    }
}
```

### 4. Boundary Value Analysis (BVA)?
BVA is a black-box test design technique that focuses on testing the "edges" or boundaries of input data ranges. Experience shows that defects are most likely to occur at these boundaries.
-   **Rule:** Test values *at* the boundary, *just below* the boundary, and *just above* the boundary.
-   **Example:** For an age input field accepting 18-60 years:
    -   Valid boundary: 18, 60
    -   Just below: 17
    -   Just above: 61
    -   Test values: 17, 18, 19, 59, 60, 61.

### 5. Difference between Oracle n Sql?
-   **SQL (Structured Query Language):** This is a **language**. It's the standard programming language for managing and querying relational databases.
-   **Oracle:** This is a **Relational Database Management System (RDBMS)**. It's a specific software product (a database system) that implements the SQL language. You use SQL to interact with an Oracle database.

### 6. SQL command to get common in two tables?
This refers to an `INNER JOIN`. An `INNER JOIN` returns only the rows that have matching values in both tables.

```sql
SELECT
    A.column1,
    B.column2
FROM
    TableA A
INNER JOIN
    TableB B ON A.common_column = B.common_column;
```

### 7. What is Structure in SQL?
This could refer to several things:
-   **Database Schema:** The overall design of the database, including tables, columns, data types, relationships, indexes, etc.
-   **Table Structure:** The definition of a table, including its name, columns, their data types, constraints (e.g., PRIMARY KEY, FOREIGN KEY, NOT NULL), and default values. You use `CREATE TABLE` to define structure.
-   **Query Structure:** The syntax of SQL queries (`SELECT ... FROM ... WHERE ...`).

### 8. What will you do if you detect a defect?
1.  **Reproduce:** Verify the defect is consistently reproducible.
2.  **Isolate:** Determine the scope of the defect (what's affected, what's not).
3.  **Document:** Create a detailed bug report in Jira (or similar tool), including:
    -   Clear title.
    -   Steps to reproduce.
    -   Expected vs. Actual results.
    -   Environment details.
    -   Screenshots/logs.
    -   Severity.
4.  **Communicate:** Notify the relevant developer/team.
5.  **Track:** Monitor the bug's lifecycle.

### 9. Bug life Cycle?
The journey of a bug from detection to closure: New -> Open/Assigned -> Fixed -> Ready for QA -> Closed (or Reopened if not fixed).

### 10. What is Constructor?
A special method in a class that is automatically called when an object of that class is created using the `new` keyword. Its main purpose is to initialize the object's state (its instance variables). It has the same name as the class and no return type.

### 11. What is interface and keyword used?
-   **Interface:** A blueprint of a class; a contract specifying methods that implementing classes must define.
-   **Keyword:** `interface` (to declare an interface) and `implements` (for a class to use an interface).

### 12. What is Inheritance and keyword used?
-   **Inheritance:** An OOP mechanism where one class (subclass) acquires properties and behaviors from another class (superclass).
-   **Keyword:** `extends`.

### 13. How is Inheritance used in your selenium project?
"Inheritance is crucial in our Selenium framework for code reuse and structure.
-   **`BaseTest` Class:** We have an `abstract BaseTest` class that all our test classes `extend`. It contains common setup (`@BeforeMethod` for WebDriver initialization) and teardown (`@AfterMethod` for WebDriver quit) logic.
-   **`BasePage` Class:** All our Page Object classes `extend` a `BasePage` class, which holds common methods applicable to all pages (e.g., `waitForPageLoad()`, `clickGlobalHeader()`)."

### 14. What does 302 Status code stands for?
`302 Found` (or `Moved Temporarily`). This HTTP status code indicates that the resource requested has been temporarily moved to a different URI. The client should continue to use the original URI for future requests, but should redirect to the new URI for the current request.

### 15. What is deferred bug?
A deferred bug is a legitimate defect that has been identified and acknowledged, but the decision has been made **not to fix it in the current release or sprint**. It's postponed to a later release, typically because it's low priority or has an acceptable workaround, and fixing it now would delay more critical features.
