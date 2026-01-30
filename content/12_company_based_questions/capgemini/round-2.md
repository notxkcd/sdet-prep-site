---
title: "Capgemini-2"
date: 2026-01-30
draft: false
---

---

## Original Questions

Capgemini interview questions :
------------------------------
Tell about yourself 
Oops concept 
Palindrom program
Axes xpath in flipkart
Constant variable in java
Constructor, defaults constructor execution and usage in your project
explain POM
How to use excel data
Crossbrowser test in testng
Testng annotation with detail
Challenges in your project 
Gherkins in cucumber 
Example in feature file
Smoke regression performance testing
Execution of Environmental details
UAT testing
Agile methodology 
Run the particular test multiple times 
Explain jenkin pipeline

---

## Answers

### Tell about yourself
Standard. Role, responsibilities, tech stack, key achievement.

### Oops concept
The four pillars: Encapsulation (POM), Abstraction (`WebDriver`), Inheritance (`BaseTest`), Polymorphism (method overriding).

### Palindrom program
A palindrome reads the same forwards and backward.
```java
public boolean isPalindrome(String str) {
    if (str == null) return false;
    String cleaned = str.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
    String reversed = new StringBuilder(cleaned).reverse().toString();
    return cleaned.equals(reversed);
}
```

### Axes xpath in flipkart
XPath Axes are used to navigate the DOM tree in ways that standard locators cannot, like finding parents or siblings.
**Scenario on Flipkart:** Find the price of a product, given the product's name.
Assuming the HTML is something like:
```html
<div class="_2kHMtA">
  <div class="_4rR01T">Flippy Knife</div>
  <div class="_30jeq3 _1_WHN1">₹1,299</div>
</div>
```
**XPath using axes:**
`//div[text()='Flippy Knife']/ancestor::div[@class='_2kHMtA']//div[contains(@class, '_30jeq3')]`

**Explanation:**
1.  `//div[text()='Flippy Knife']`: Find the div with the product name.
2.  `/ancestor::div[@class='_2kHMtA']`: Find the common parent container for the name and price.
3.  `//div[contains(@class, '_30jeq3')]`: From that container, find the descendant div that contains the price.

### Constant variable in java
A constant variable is a variable whose value cannot be changed after it is initialized. In Java, you create one using the `final` keyword. By convention, constant names are in `UPPER_SNAKE_CASE`.

```java
public static final String BROWSER_NAME = "chrome";
public static final int DEFAULT_TIMEOUT_SECONDS = 10;
```
Using `static final` makes it a true constant that belongs to the class and is shared by all instances.

### Constructor, defaults constructor execution and usage in your project
-   **Constructor:** A special method used to initialize an object when it's created.
-   **Default Constructor:** If you do not define any constructor in a class, the Java compiler provides a default, no-argument constructor for you. If you define *any* constructor (e.g., one that takes parameters), the compiler does **not** provide the default one anymore.
-   **Execution:** A constructor is executed when you use the `new` keyword.
-   **Usage in Project:** "In our framework, every Page Object class has a constructor that accepts the `WebDriver` instance as a parameter. This is essential for dependency injection, ensuring the page object is initialized with a valid driver to interact with the browser. Example: `public LoginPage(WebDriver driver) { this.driver = driver; }`."

### explain POM
Page Object Model. A design pattern in test automation that creates an object repository for web UI elements. The main principle is to create one class per web page (or component), which encapsulates all the locators and interaction methods for that page. This separates test logic from UI interaction logic, making tests cleaner and more maintainable.

### How to use excel data
You use a third-party Java library like **Apache POI**.
1.  Add the Apache POI dependency to your `pom.xml`.
2.  Create a utility class that contains methods to open an Excel workbook (`.xlsx`), get a specific sheet, and read data from rows and columns.
3.  In your TestNG `@DataProvider` method, call this utility to read data from the Excel file and return it as a 2D `Object[][]` array for your test methods to consume.

### Crossbrowser test in testng
Cross-browser testing is running the same test suite against different browsers. In TestNG, this is achieved using parameters in the `testng.xml` suite file.

**`testng.xml` configuration:**
```xml
<suite name="CrossBrowserSuite" parallel="tests" thread-count="2">

  <test name="ChromeTest">
    <parameter name="browser" value="chrome"/>
    <classes>
      <class name="com.mytests.LoginTest"/>
    </classes>
  </test>
  
  <test name="FirefoxTest">
    <parameter name="browser" value="firefox"/>
    <classes>
      <class name="com.mytests.LoginTest"/>
    </classes>
  </test>

</suite>
```
**In your `BaseTest`:**
```java
@BeforeMethod
@Parameters("browser")
public void setup(String browser) {
    if (browser.equalsIgnoreCase("chrome")) {
        driver = new ChromeDriver();
    } else if (browser.equalsIgnoreCase("firefox")) {
        driver = new FirefoxDriver();
    }
    // ...
}
```
When you run this suite, TestNG will run `LoginTest` twice in parallel: once with the `browser` parameter as "chrome" and once as "firefox".

### Testng annotation with detail
-   `@BeforeSuite`/`@AfterSuite`: Run once before/after all tests in a suite. For global setup/teardown.
-   `@BeforeTest`/`@AfterTest`: Run once before/after all tests within a `<test>` tag in `testng.xml`.
-   `@BeforeClass`/`@AfterClass`: Run once before/after all tests in the current class.
-   `@BeforeMethod`/`@AfterMethod`: Run before/after **every `@Test` method**. This is the most common place for WebDriver setup and teardown.
-   `@Test`: Marks a method as a test case. Can have attributes like `priority`, `dependsOnMethods`, `groups`.
-   `@DataProvider`: Marks a method that supplies data to a test method.

### Challenges in your project
Have specific, technical examples ready.
-   **Flaky Tests:** Due to timing issues. Solved by implementing robust explicit waits.
-   **Test Data Management:** Ensuring unique data for parallel runs. Solved by creating a test data factory or using a database cleanup strategy.
-   **Dynamic UI Elements:** Locators breaking frequently. Solved by developing better XPath/CSS strategies and working with developers to add stable `data-testid` attributes.

### Gherkins in cucumber
Gherkin is the language used to write test scenarios in Cucumber `.feature` files. It's a simple, human-readable syntax designed to be understood by non-technical stakeholders. Its main keywords are:
-   `Feature`: Describes the feature being tested.
-   `Scenario` / `Scenario Outline`: A specific test case or template.
-   `Given`: Sets up a precondition.
-   `When`: Describes an action performed by the user.
-   `Then`: Describes the expected outcome or result.
-   `And`, `But`: Used to chain multiple steps of the same type.
-   `Background`: Defines steps that run before every scenario in the feature.

### Example in feature file
```gherkin
Feature: User Login

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter valid credentials
    And I click the "Login" button
    Then I should be redirected to the user dashboard
```

### Smoke regression performance testing
-   **Smoke Testing:** A quick, shallow test of the most critical functionalities to ensure a new build is stable enough for further testing.
-   **Regression Testing:** A comprehensive test suite run to ensure that new code changes haven't broken existing functionality.
-   **Performance Testing:** A non-functional test to evaluate how a system performs in terms of responsiveness and stability under a particular workload (e.g., using tools like JMeter or k6).

### Execution of Environmental details
This likely means "How do you manage environment-specific details for test execution?".
"We manage environment details through external **configuration files** (e.g., `qa.properties`, `staging.properties`). Our framework has a `ConfigReader` utility that loads the appropriate file based on a parameter we pass at runtime (e.g., via a Maven profile: `mvn test -P staging`). This file contains environment-specific details like the base URL, database connection strings, and API keys. This way, the same test code can be run against any environment without modification."

### UAT testing
User Acceptance Testing. This is one of the final phases of testing, where the software is tested by the **end-users or the client** to verify that it meets their business requirements and is "acceptable" for release. It focuses on validating the business flow, not on finding technical bugs (which should have been found already).

### Agile methodology
An iterative approach to software development focused on delivering value in small increments (sprints), customer collaboration, and adapting to change. Scrum and Kanban are popular frameworks for implementing Agile.

### Run the particular test multiple times
In TestNG, you can use the `invocationCount` attribute in the `@Test` annotation.

```java
@Test(invocationCount = 5)
public void testThisMultipleTimes() {
    // This test method will be executed 5 times.
}
```
If you want to run it in parallel, you can add `threadPoolSize`: `@Test(invocationCount = 5, threadPoolSize = 5)`.

### Explain jenkin pipeline
A Jenkins pipeline defines your entire build, test, and deploy process as code, typically in a file called a `Jenkinsfile`.
-   It's composed of **stages** (e.g., "Build", "Test", "Deploy").
-   Each stage contains **steps** (e.g., run `mvn clean install`, run `sh './run-tests.sh'`).
-   This "pipeline as code" approach makes the build process version-controlled, repeatable, and resilient.
-   It provides great visibility into the delivery process.
