---
title: "Colan Infotech"
date: 2026-01-30
draft: false
---

---

## Original Questions

Colan Infotech Interview Questions:
Round 1:
- Reverse the string
- Browser launch code
- About Get and navigate
Git steps
- Bdd explaination
- Introduce urself
- Find element and find elements difference
- Explain Oops concept
Alert handle
Frame handle
- Get window handle
Select class
- Broken links handle
- Select class alternate
- Hard and soft assert
- Return type of find element and find elements.
Frames
- Difference between manual and automation responsibilities
- Critical bug identify in your project
- Reason for change

---

## Answers (No-BS Java QA / SDET Explanations)

### Reverse the string
The most efficient and readable way is using `StringBuilder`.

```java
public String reverseString(String str) {
    if (str == null) return null;
    return new StringBuilder(str).reverse().toString();
}
```

### Browser launch code
This typically involves setting up the WebDriver and initializing a browser instance.

```java
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
// import org.openqa.selenium.firefox.FirefoxDriver;
// import org.openqa.selenium.edge.EdgeDriver;

public class BrowserLauncher {
    public WebDriver launchChrome() {
        // Option 1: Using WebDriverManager (recommended for local execution)
        // WebDriverManager.chromedriver().setup();

        // Option 2: Manually setting system property (if driver is on PATH or specified)
        System.setProperty("webdriver.chrome.driver", "/path/to/chromedriver");

        WebDriver driver = new ChromeDriver();
        driver.manage().window().maximize(); // Maximise browser window
        return driver;
    }
}
```
> **Side note:** In a real framework, this would be handled in a `BaseTest` class's `@BeforeMethod` with proper configuration from `testng.xml` or properties files.

### About Get and navigate
-   `driver.get(url)`: Loads a new web page and waits for it to load.
-   `driver.navigate().to(url)`: Does the same as `get()`, but `driver.navigate()` also provides additional methods to move back, forward, and refresh the page (`back()`, `forward()`, `refresh()`).

### Git steps
These are the core Git workflow steps:
1.  `git add .` (or `git add <file>`): Stage changes.
2.  `git commit -m "Your commit message"`: Commit staged changes to local repository.
3.  `git push origin <branch_name>`: Push committed changes to the remote repository.
4.  `git pull origin <branch_name>`: Fetch and merge changes from the remote repository.

### Bdd explaination
Behavior-Driven Development (BDD) is an agile software development process that encourages collaboration among developers, QA, and business stakeholders. It uses a common, human-readable language (Gherkin, e.g., `Given/When/Then`) to describe application behavior from the user's perspective. Tools like Cucumber then execute these specifications as automated tests, making the tests themselves living documentation.

### Introduce urself
Standard opener. Keep it concise, professional, and highlight your relevant experience and skills.

### Find element and find elements difference
-   `findElement(By locator)`: Returns the **first** matching `WebElement`. Throws `NoSuchElementException` if no element is found.
-   `findElements(By locator)`: Returns a `List<WebElement>` containing **all** matching elements. Returns an **empty list** if no elements are found (does not throw an exception).

### Explain Oops concept
The four pillars:
-   **Encapsulation:** Hiding data and implementation details (e.g., Page Object Model).
-   **Abstraction:** Showing only essential features, hiding background details (e.g., `WebDriver` interface).
-   **Inheritance:** Creating new classes from existing ones to reuse code (e.g., `BaseTest`).
-   **Polymorphism:** "Many forms." Method overloading and overriding.

### Alert handle
For native browser JavaScript alerts (not HTML modals), you use `driver.switchTo().alert()`.
-   `alert.accept()`: Click "OK".
-   `alert.dismiss()`: Click "Cancel" or close.
-   `alert.getText()`: Get the text of the alert.
-   `alert.sendKeys("text")`: Type into a prompt alert.

### Frame handle
For HTML `iframe`s, you must switch Selenium's context.
1.  `driver.switchTo().frame("frameNameOrId")` (by name or ID).
2.  `driver.switchTo().frame(index)` (by 0-based index).
3.  `driver.switchTo().frame(webElement)` (by locating the frame element itself).
After interacting with elements inside the frame, switch back to the main content: `driver.switchTo().defaultContent()`.

### Get window handle
This is about `driver.getWindowHandle()` (current window) and `driver.getWindowHandles()` (all open windows). Used to switch between multiple browser windows or tabs.

### Select class
Selenium's `Select` class is used to interact with `<select>` HTML dropdown elements.
-   `new Select(WebElement dropdownElement)`
-   `selectByVisibleText("Option Text")`
-   `selectByValue("option_value")`
-   `selectByIndex(index)`

### Broken links handle
You find all `<a>` elements, extract their `href` attributes, and then use a Java HTTP client (`HttpURLConnection`) to send a `HEAD` request to each URL. Check for HTTP status codes `400` or higher to identify broken links.

### Select class alternate
If a dropdown is *not* a standard `<select>` HTML element (e.g., it's a custom-built dropdown using `div`s and `span`s), you cannot use the `Select` class.
-   You handle it like any other web element:
    1.  Click the dropdown's visible element to expand the options.
    2.  Use an explicit wait to wait for the desired option to become visible.
    3.  Click the desired option.

### Hard and soft assert
-   **Hard Assert:** (`org.testng.Assert`) Fails immediately and stops the test execution on the first assertion failure.
-   **Soft Assert:** (`org.testng.asserts.SoftAssert`) Records all failures during the test but continues execution. Only fails the test at the very end when `softAssert.assertAll()` is called.

### Return type of find element and find elements.
-   `findElement()`: Returns a `WebElement`.
-   `findElements()`: Returns `List<WebElement>`.

### Frames
Same as "Frame handle". It's about HTML `iframe`s.

### Difference between manual and automation responsibilities
-   **Manual Tester:** Focuses on exploratory testing, usability, ad-hoc testing, and scenarios where human intuition is crucial. Writes manual test cases.
-   **Automation Engineer/SDET:** Focuses on designing, building, and maintaining automated test suites (unit, API, UI). Integrates tests into CI/CD. Often performs framework development and contributes to test strategy.
A good QA team has both roles. Automation handles the repetitive, regression checks. Manual/exploratory testing finds the new and complex bugs.

### Critical bug identify in your project
Be prepared with a real example.
"In my last project, I identified a critical bug where, under specific conditions (e.g., using a non-standard browser and certain privacy settings), the 'Forgot Password' functionality would intermittently fail with an internal server error. This meant users could be locked out of their accounts. It was critical because it directly impacted user access and could lead to support ticket overflow."

### Reason for change
Standard interview question. Positive, forward-looking reasons.
"I'm looking for a new challenge in a dynamic environment where I can apply my automation skills to a more complex product/system. I'm also keen on opportunities for professional growth and contributing to test strategy at a higher level."
