---
title: "Generic Questions-3"
date: 2026-01-30
draft: false
---

---

## Original Questions

- How you will be using the constructor in selenium
- What are the locators that is available in selenium
- Reverse the string
- Api status code
- What is the use of patch code in api
- What is the purpose of get in api
- What  post method will do  in api
- How you will handle the windows in selenium
- Explain the step defination in cucumber
- Write a code on selenium to launch the browser
- Explain this keyword
- Have you done estimatation on your project
- On cucumber where you will store the xpath
- On where you will be adding the dependencies in cucumber
- Navigations in TestNG
- How you will handle the dropdown in selenium
- Have you developed any frameworks

---

## Answers (No-BS Java QA / SDET Explanations)

### How you will be using the constructor in selenium
Constructors are fundamental to the Page Object Model (POM).
"In my Selenium framework, I use constructors in every Page Object class. The primary purpose is **dependency injection**—specifically, to pass the `WebDriver` instance from the test class to the page object. This ensures that the page object has the necessary driver to find elements and perform actions.

```java
public class LoginPage {
    private WebDriver driver;

    // Constructor to initialize the driver for this page object
    public LoginPage(WebDriver driver) {
        this.driver = driver;
        // If using PageFactory, you'd call PageFactory.initElements(driver, this); here.
    }

    public void enterUsername(String username) {
        // Now the 'driver' field can be used safely
        driver.findElement(By.id("username")).sendKeys(username);
    }
}
```
Without the constructor, the page object would have no way to interact with the browser."

### What are the locators that is available in selenium
There are 8 standard locators: `id`, `name`, `className`, `tagName`, `linkText`, `partialLinkText`, `cssSelector`, and `xpath`.

### Reverse the string
The standard, efficient way: `new StringBuilder(str).reverse().toString();`

### Api status code
HTTP Status Codes are grouped into 5 classes:
-   **1xx (Informational):** Request received, continuing process.
-   **2xx (Success):** The action was successfully received, understood, and accepted. (`200 OK`, `201 Created`, `204 No Content`).
-   **3xx (Redirection):** Further action needs to be taken to complete the request. (`301 Moved Permanently`).
-   **4xx (Client Error):** The client has made an error. (`400 Bad Request`, `401 Unauthorized`, `404 Not Found`).
-   **5xx (Server Error):** The server failed to fulfill an apparently valid request. (`500 Internal Server Error`, `503 Service Unavailable`).

### What is the use of patch code in api
The question means the `PATCH` HTTP method.
`PATCH` is used to apply a **partial update** to a resource. Unlike `PUT`, where you must send the entire resource object to replace the existing one, with `PATCH` you only send the fields that you want to change.

### What is the purpose of get in api
The `GET` HTTP method is used to **retrieve** or read a representation of a resource. It should be safe (no side effects) and idempotent (calling it multiple times has the same effect as calling it once).

### What post method will do in api
The `POST` HTTP method is used to **create** a new resource on the server. It is typically not idempotent; calling the same `POST` request twice will create two new resources. The data for the new resource is carried in the request body.

### How you will handle the windows in selenium
Using window handles.
1.  `driver.getWindowHandle()` gets the ID of the current window.
2.  `driver.getWindowHandles()` gets the IDs of all open windows.
3.  `driver.switchTo().window(windowId)` switches focus to the specified window.
The process is to get the original handle, trigger the new window, get all handles, find the new one by comparing sets, and then switch to it.

### Explain the step defination in cucumber
A step definition is a Java method that is "glued" to a Gherkin step in a `.feature` file.
-   It's annotated with `@Given`, `@When`, or `@Then`.
-   The annotation contains a regular expression that matches the text of the Gherkin step.
-   This method contains the actual automation code (e.g., Selenium calls) that executes the step.
It is the bridge between the human-readable feature file and the code that makes the test run.

### Write a code on selenium to launch the browser
```java
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class BrowserLaunch {
    public static void main(String[] args) {
        // This assumes chromedriver is on the system PATH or
        // you've used System.setProperty("webdriver.chrome.driver", "/path/to/driver");
        // A better approach is using WebDriverManager library.
        
        WebDriver driver = new ChromeDriver();
        driver.get("https://www.google.com");
        System.out.println("Page title is: " + driver.getTitle());
        driver.quit();
    }
}
```

### Explain this keyword
`this` is a reference to the **current object instance**.
Its main uses are:
1.  **Disambiguation:** To distinguish between an instance variable and a local variable (or parameter) with the same name. `this.name = name;`
2.  **Calling another constructor:** To call another constructor from within the same class (`this(defaultName);`). This is called constructor chaining.

### Have you done estimatation on your project
"Yes. As part of our sprint planning process, I am responsible for providing effort estimates for the testing and automation tasks associated with each user story. We use a relative estimation technique with story points, where I assess the complexity, uncertainty, and amount of work required for testing a given feature."

### On cucumber where you will store the xpath
XPath locators, like all locators, should **not** be stored in the Cucumber `.feature` file. The feature file should be purely descriptive and non-technical.

XPath locators belong in the implementation layer, specifically within **Page Object Model (POM) classes**. The step definition method would call a method on a page object (e.g., `loginPage.clickLoginButton()`), and inside that `clickLoginButton()` method is where the `driver.findElement(By.xpath(...))` call would be, using a locator defined as a `private` field within that page object class.

### On where you will be adding the dependencies in cucumber
In a Maven project, all dependencies for Cucumber, Selenium, TestNG, etc., are added in the **`pom.xml`** file, inside the `<dependencies>` section.

### Navigations in TestNG
TestNG itself does not have "navigation". This question is likely confusing TestNG with Selenium. **Selenium** provides the navigation commands:
-   `driver.get(url)`
-   `driver.navigate().to(url)`
-   `driver.navigate().back()`
-   `driver.navigate().forward()`
-   `driver.navigate().refresh()`

TestNG is the framework that *runs* the tests that *use* these Selenium commands.

### How you will handle the dropdown in selenium
For a standard `<select>` dropdown, use Selenium's `Select` class:
1.  Locate the `<select>` element.
2.  Create a `Select` object: `Select dropdown = new Select(element);`
3.  Use one of its selection methods: `selectByVisibleText()`, `selectByValue()`, or `selectByIndex()`.

For custom dropdowns (made with `div`s), you automate it manually: click to open, wait for the option to be visible, then click the option.

### Have you developed any frameworks
"Yes, I have been heavily involved in developing our team's test automation framework from the ground up. I designed the initial structure based on the Page Object Model, implemented the WebDriver management and configuration handling, created the data-driven testing approach using JSON files, and integrated our ExtentReports reporting. I was responsible for making key architectural decisions to ensure it was scalable and maintainable."
Even if you didn't build it from scratch, you can say: "I haven't built one from zero, but I have significantly enhanced and maintained our existing framework by adding new core functionalities like..."
