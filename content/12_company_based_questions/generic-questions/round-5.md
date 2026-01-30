---
title: "Generic Questions-5"
date: 2026-01-30
draft: false
---

---

## Original Questions

1.Explain your frame work
2.Write a test case for one component that you had used in your project
3.How will you pass data to webelements
4.Explain webelement methods
5.write the syntax for the extent report
6. How many locators that you had used in your project
7. Write a syntax for css selector
8. How will you get the background colour of the webelement
9. Explain the TestNG annotations
10.How will you run the runner class in cucumber
11.How will you handle alerts
12.How will you handle the dropdown

---

## Answers

### 1. Explain your frame work
"I developed and maintained a hybrid, data-driven automation framework using Java.
-   **Core Stack:** TestNG for test execution, Selenium WebDriver for UI automation, and REST-assured for API testing.
-   **Design:** It's built on the Page Object Model (POM) to ensure maintainability. We have a `BaseTest` class for common setup/teardown and a `BasePage` for shared page functionalities.
-   **Data Management:** Test data is externalized into JSON files and fed into tests via TestNG's `@DataProvider`.
-   **Reporting:** We use ExtentReports, integrated with TestNG listeners, to generate detailed HTML reports with screenshots on failure.
-   **CI/CD:** The entire framework is managed with Maven and executed through Jenkins pipelines."

### 2. Write a test case for one component that you had used in your project
**Component:** Search Filter Component on an E-commerce Site
**Test Case ID:** TC_FILTER_01
**Title:** Verify that filtering by "Brand" correctly updates the search results.
**Preconditions:**
1.  User is on the search results page for "laptops".
2.  Multiple products from different brands (e.g., "Dell", "HP") are displayed.
**Steps:**
1.  Locate the "Brand" filter section.
2.  Click the checkbox for the brand "Dell".
3.  Wait for the product grid to refresh.
**Expected Result:**
-   All products now displayed in the grid should have "Dell" in their title or description.
-   No products from other brands (e.g., "HP") should be visible.
-   The "Dell" brand checkbox should remain checked.

### 3. How will you pass data to webelements
You use the `sendKeys()` method. This method simulates typing into an element.

```java
// Find the username input field
WebElement usernameInput = driver.findElement(By.id("username"));

// Clear any existing text (good practice)
usernameInput.clear();

// Pass the data "testuser" to the input field
usernameInput.sendKeys("testuser");
```

### 4. Explain webelement methods
`WebElement` is an interface in Selenium that represents an HTML element. Some of its most common methods are:
-   `.click()`: Clicks the element.
-   `.sendKeys(CharSequence... keysToSend)`: Types text into the element.
-   `.getText()`: Gets the visible inner text of the element.
-   `.getAttribute(String name)`: Gets the value of a given attribute (e.g., `href`, `class`, `value`).
-   `.isDisplayed()`: Returns `true` if the element is visible on the page.
-   `.isEnabled()`: Returns `true` if the element is enabled (e.g., a button that is not grayed out).
-   `.isSelected()`: Returns `true` if the element (like a checkbox or radio button) is selected.
-   `.clear()`: Clears the text from an input field.
-   `.submit()`: If the element is within a form, this will submit the form.

### 5. write the syntax for the extent report
You don't write "syntax for the report". You write code to configure and use the ExtentReports library. This is typically done in a TestNG listener.

**Basic Setup (in a helper class or `@BeforeSuite`):**
```java
import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.reporter.ExtentSparkReporter;

public class ExtentManager {
    public static ExtentReports createInstance(String reportPath) {
        ExtentSparkReporter sparkReporter = new ExtentSparkReporter(reportPath);
        sparkReporter.config().setReportName("Automation Test Results");
        
        ExtentReports extent = new ExtentReports();
        extent.attachReporter(sparkReporter);
        return extent;
    }
}
```

**Usage in a TestNG Listener:**
```java
import com.aventstack.extentreports.ExtentTest;
import org.testng.ITestListener;
import org.testng.ITestResult;

public class TestListener implements ITestListener {
    private ExtentReports extent = ExtentManager.createInstance("target/extent-report.html");
    private ThreadLocal<ExtentTest> test = new ThreadLocal<>();

    @Override
    public void onTestStart(ITestResult result) {
        ExtentTest extentTest = extent.createTest(result.getMethod().getMethodName());
        test.set(extentTest);
    }

    @Override
    public void onTestFailure(ITestResult result) {
        test.get().fail(result.getThrowable());
        // Add screenshot logic here
    }
    
    // ... other listener methods ...

    @Override
    public void onFinish(ITestContext context) {
        extent.flush(); // This writes everything to the report file
    }
}
```

### 6. How many locators that you had used in your project
"I use all 8 standard Selenium locators, choosing the best one for the situation. In our project, the most frequently used locators are `id`, `cssSelector`, and `xpath`, as they provide the most reliable and flexible ways to find elements."

### 7. Write a syntax for css selector
CSS Selectors have a rich syntax.
-   **By ID:** `div#uniqueId` or just `#uniqueId`
-   **By Class:** `button.primary-button`
-   **By Attribute:** `input[name='username']` or `a[href*='example.com']` (contains)
-   **By Tag:** `h1`
-   **Child/Descendant:** `div > h2` (direct child) or `div h2` (any descendant)

**Example:**
`driver.findElement(By.cssSelector("form#login-form input[name='password']"));`
This finds an `<input>` element with `name='password'` that is a descendant of a `<form>` with `id='login-form'`.

### 8. How will you get the background colour of the webelement
You use the `.getCssValue()` method. It retrieves the computed value of a given CSS property.

```java
WebElement button = driver.findElement(By.id("myButton"));
String backgroundColor = button.getCssValue("background-color");

// The returned value is typically in rgba format, e.g., "rgba(255, 0, 0, 1)" for red
System.out.println(backgroundColor); 
```

### 9. Explain the TestNG annotations
`@Test` marks a test method. The other key annotations control setup and teardown at different scopes:
-   `@BeforeSuite` / `@AfterSuite`: Run once for the entire suite.
-   `@BeforeTest` / `@AfterTest`: Run once for a `<test>` tag in `testng.xml`.
-   `@BeforeClass` / `@AfterClass`: Run once for a test class.
-   `@BeforeMethod` / `@AfterMethod`: Run before/after every single `@Test` method.

### 10. How will you run the runner class in cucumber
1.  **From an IDE (like Eclipse/IntelliJ):** You can simply right-click the Runner class and choose "Run As -> JUnit Test".
2.  **From Maven:** You configure the `maven-surefire-plugin` in your `pom.xml` to include your runner class. Then, running `mvn test` from the command line will automatically find and execute the runner.

### 11. How will you handle alerts
Using `driver.switchTo().alert()`. This returns an `Alert` object that you can then `.accept()`, `.dismiss()`, or get text from (`.getText()`).

### 12. How will you handle the dropdown
-   **For standard `<select>` tags:** Use the `Select` class.
    `Select dropdown = new Select(element); dropdown.selectByVisibleText("My Option");`
-   **For custom dropdowns (made of `div`s):** Automate it manually. Click to open it, then wait for and click the desired option element.
