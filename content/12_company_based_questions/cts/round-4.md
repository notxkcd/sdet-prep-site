---
title: "CTS-4"
date: 2026-01-30
draft: false
---

---

## Original Questions

CTS L1 and L2:
--------------
Tell abt ur self
Draw your Framework architecture and explain
Select class methods 
Select particular window from multiple windows
Two boxes present click the second box, xpath and js executor not working
How to pass data from excel
How to pass data from pdf
Which version selenium using in your project
Fullpage screenshot
Write a code to find a  previous element  and nxt element using Xpath axes
Explain feature file
Cucumber options
DryRun true false difference
Explain Restassured  framework
Explain Put get post patch 
How to generate token
How to validate response 
How to link automation screenshots in to jira tool
Git conflict
Can you write sql query 
Explain jenkins
What is webdriver
Write a program go to google search testing automation and click the link and find broken link and use implicit and explicit wait 
Have you work any other languages other than English
How many ways to remove special characters in a string

---

## Answers (No-BS Java QA / SDET Explanations)

### Tell abt ur self
Standard opener. Keep it concise, professional, and focused on your automation experience.

### Draw your Framework architecture and explain
Be prepared to describe this on a whiteboard or conceptually.
"Our framework is layered:
1.  **Test Layer:** TestNG test classes. They contain test logic and assertions only.
2.  **Page Object Layer:** Java classes representing pages of the application. They contain element locators and interaction methods. This layer uses Selenium.
3.  **Utility Layer:** Helper classes for things like reading config files, reading Excel data (Apache POI), database connections (JDBC), and reporting (ExtentReports).
4.  **Data Layer:** External files (`.properties`, JSON, or Excel) that store our test data and configuration.
5.  **Build/Execution Layer:** Maven (`pom.xml`) manages dependencies and the build lifecycle. TestNG (`testng.xml`) manages test execution. Jenkins orchestrates the entire process for CI/CD."

### Select class methods
The `Select` class in Selenium is used for `<select>` dropdowns. Key methods:
-   `selectByVisibleText("Text of the option")`
-   `selectByValue("value_attribute_of_option")`
-   `selectByIndex(int index)`
-   `getOptions()`: Returns a `List<WebElement>` of all options.
-   `getFirstSelectedOption()`: Returns the currently selected option.

### Select particular window from multiple windows
1.  Get all window handles: `Set<String> allHandles = driver.getWindowHandles();`
2.  You need a way to identify the window you want (e.g., by its title or URL).
3.  Loop through the handles, switch to each window, and check its title/URL.
    ```java
    for (String handle : allHandles) {
        driver.switchTo().window(handle);
        if (driver.getTitle().equals("Target Window Title")) {
            break; // Found the right window, stop looping
        }
    }
    ```

### Two boxes present click the second box, xpath and js executor not working
This is a problem-solving question. If standard methods fail, you have to get creative.
1.  **`Actions` class:** Sometimes the `Actions` class can succeed where a direct click fails. `new Actions(driver).moveToElement(secondBox).click().perform();`
2.  **Send Keys (Enter/Space):** If the box can receive focus, you can try to `TAB` to it or use `sendKeys(Keys.ENTER)` or `sendKeys(Keys.SPACE)` which can trigger a click event.
3.  **Re-evaluate the problem:** Is the element actually a checkbox? Is it inside an `iframe`? Is there an overlay covering it? The problem is likely not the click itself, but a misunderstanding of the element's state or context. Go back to DevTools and re-inspect everything.

### How to pass data from excel
Using the **Apache POI** library. You create a utility class to read the `.xlsx` file, then use a TestNG `@DataProvider` to feed that data into your `@Test` methods.

### How to pass data from pdf
This is much harder than Excel. Selenium has no built-in way to do this. You need a third-party Java library like **Apache PDFBox**.
-   **Process:**
    1.  Add the `pdfbox` dependency to your `pom.xml`.
    2.  Write a utility class that uses PDFBox to load a PDF file and parse its text content.
    3.  Your test would then call this utility to get the text and perform assertions or extract data.
-   This is an uncommon requirement, but knowing that Apache PDFBox is the tool for the job is the key part of the answer.

### Which version selenium using in your project
"We are on **Selenium 4**. We upgraded to take advantage of the W3C protocol compliance and new features like relative locators."

### Fullpage screenshot
Standard Selenium `TakesScreenshot` only captures the visible viewport. To take a full-page screenshot that includes the scrolled content, you need a different approach.
-   **Third-party libraries:** The most common solution is to use a library like **AShot**. You add its dependency and then use its API:
    ```java
    Screenshot fpScreenshot = new AShot()
        .shootingStrategy(ShootingStrategies.viewportPasting(1000))
        .takeScreenshot(driver);
    ImageIO.write(fpScreenshot.getImage(), "PNG", new File("fullpage.png"));
    ```
-   **Firefox Native:** Firefox's WebDriver has a built-in capability for this: `((FirefoxDriver)driver).getFullPageScreenshotAs(OutputType.FILE);`

### Write a code to find a previous element and nxt element using Xpath axes
-   **`following-sibling`:** Finds the next sibling.
-   **`preceding-sibling`:** Finds the previous sibling.

```java
// Assuming HTML: <label>Username</label><input .../><label>Password</label>

// Find the input field (next element) after the 'Username' label
WebElement usernameInput = driver.findElement(By.xpath("//label[text()='Username']/following-sibling::input[1]"));

// Find the 'Username' label (previous element) before the password label
WebElement usernameLabel = driver.findElement(By.xpath("//label[text()='Password']/preceding-sibling::label[1]"));
```

### Explain feature file
A `.feature` file is the heart of Cucumber. It's a plain-text file written in Gherkin syntax that describes a feature and its scenarios. It serves as both documentation and an executable test specification.

### Cucumber options
`@CucumberOptions` is an annotation on the runner class that configures the test execution. Key options:
-   `features`: Path to your feature files.
-   `glue`: Path to your step definition packages.
-   `tags`: Filters which scenarios to run.
-   `plugin`: Configures reporters (e.g., `pretty`, `html:target/report.html`, `json:target/report.json`).
-   `dryRun`: Checks for missing step definitions without running tests.

### DryRun true false difference
-   `dryRun = true`: Cucumber runs through the feature files and verifies that every step has a matching step definition. It **does not** execute the actual test code.
-   `dryRun = false` (default): Cucumber executes the tests normally.

### Explain Restassured framework
REST-assured is a Java library for testing REST APIs. It provides a fluent, BDD-style syntax (`given/when/then`) that makes it easy to write powerful and readable API tests. You can use it to make HTTP requests and validate status codes, headers, and response bodies.

### Explain Put get post patch
-   `GET`: Retrieve a resource.
-   `POST`: Create a new resource.
-   `PUT`: Completely replace/update an existing resource.
-   `PATCH`: Partially update an existing resource.

### How to generate token
In API testing, you automate this by making a `POST` request to the login/authentication endpoint with valid credentials. You then extract the token (e.g., a JWT) from the response body and store it in a variable to use in the `Authorization` header of subsequent requests.

### How to validate response
In REST-assured, you do this in the `.then()` block.
-   `.statusCode(200)`
-   `.header("Content-Type", "application/json")`
-   `.body("path.to.field", equalTo("expectedValue"))` (using Hamcrest matchers)
-   `.time(lessThan(2000L))`

### How to link automation screenshots in to jira tool
This requires a Jira plugin that supports this (like **Xray** or **Zephyr**) and some CI/CD configuration.
-   **Process:**
    1.  Your test listener saves the screenshot to a known location in your Jenkins workspace.
    2.  You use the Jira plugin's REST API to attach this file to the test execution record or a newly created bug ticket in Jira.
    3.  This is typically done via a `curl` command or a custom script in a post-build step in Jenkins.

### Git conflict
A Git conflict occurs when you try to merge two branches that have competing changes to the same lines in the same file. Git cannot automatically resolve it and marks the file as conflicted, requiring manual intervention. You must open the file, choose which changes to keep, save it, and then `git add` and `git commit` the resolved file.

### Can you write sql query
"Yes, I can write basic to intermediate SQL queries to `SELECT`, `INSERT`, `UPDATE`, and `DELETE` data, and use `JOIN`s to query across multiple tables."

### Explain jenkins
An open-source automation server used for building CI/CD pipelines. It automates the process of building, testing, and deploying software.

### What is webdriver
`WebDriver` is the central **interface** in Selenium. It defines the set of methods for interacting with a web browser. All browser-specific driver classes (`ChromeDriver`, `FirefoxDriver`, etc.) implement this interface.

### Write a program go to google search testing automation and click the link and find broken link and use implicit and explicit wait
This is a complex question combining multiple concepts.
```java
// ... imports ...
public class GoogleSearchAndLinkCheck {
    public static void main(String[] args) {
        WebDriver driver = new ChromeDriver();
        // DO NOT USE Implicit Wait in a real project with Explicit Waits.
        // driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(5)); // Bad practice shown for question.

        try {
            driver.get("https://www.google.com");
            WebElement searchBox = driver.findElement(By.name("q"));
            searchBox.sendKeys("testing automation");
            searchBox.submit();

            // USE Explicit Wait - this is the correct way.
            WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
            // Wait for search results to be visible
            wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("search")));

            List<WebElement> links = driver.findElements(By.tagName("a"));
            System.out.println("Found " + links.size() + " links. Checking for broken links...");

            for (WebElement link : links) {
                String url = link.getAttribute("href");
                if (url != null && !url.isEmpty() && url.startsWith("http")) {
                    try {
                        HttpURLConnection connection = (HttpURLConnection) new URL(url).openConnection();
                        connection.setRequestMethod("HEAD");
                        connection.connect();
                        if (connection.getResponseCode() >= 400) {
                            System.out.println("BROKEN LINK: " + url + " - " + connection.getResponseCode());
                        }
                    } catch (Exception e) {
                        // Ignore connection errors, etc.
                    }
                }
            }
        } finally {
            driver.quit();
        }
    }
}
```

### Have you work any other languages other than English
This is an HR question about spoken languages. Be honest.

### How many ways to remove special characters in a string
1.  **Regex with `replaceAll()`:** The most common and flexible way.
    `String clean = original.replaceAll("[^a-zA-Z0-9]", "");`
2.  **Looping and `Character.isLetterOrDigit()`:** Manually build a new string.
    ```java
    StringBuilder sb = new StringBuilder();
    for (char c : original.toCharArray()) {
        if (Character.isLetterOrDigit(c)) {
            sb.append(c);
        }
    }
    String clean = sb.toString();
    ```
