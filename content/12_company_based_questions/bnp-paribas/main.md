---
title: "BNP Paribas"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

BNP Paribas interview Questions:
1. Tell about yourself more about professional experience and more about exposure towards automation.
2. What are the hooks you are using in your framework.
3. What is for @before you used in your framework?
4. Were you using background feature and for what purpose in your framework?
5. How do you pass test data?
6. Scenario: assume we have given below data in feature file and write code in step definition to pass all the 4 test data in UI using data table.
jack	sparrow
tim	tom
7. Scenario: Given a table structure and asked to retrieve all the table data. write code to return only unique value ignoring the duplicates in the table data.
- <table id="table">
<tr>
<td>jack</td>
<td>jack</td>
</tr>
<tr>
<td>tim</td>
<td>tim</td>
</tr>
</table>

8. Given amazon link and asked to write xpath for a particular element which in under ul\li tag.
9. which version of selenium you use in your project?
10. what are the major changes from version 3 to version 4
11. How do you perform regression in your project?
12. Tell me roadmap of your career as software tester.

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. Tell about yourself more about professional experience and more about exposure towards automation.
This is a standard "self-intro" with an emphasis. Focus on your automation journey.
"I'm a QA Automation Engineer with X years of experience, primarily focused on building robust and scalable test automation frameworks in Java. My expertise lies in designing end-to-end solutions for both UI (Selenium WebDriver) and API (REST-assured) testing. I've been instrumental in migrating manual test suites to automated ones, reducing regression cycles by X% and integrating these into CI/CD pipelines using Jenkins. I particularly enjoy the challenge of designing reusable Page Object Models and implementing efficient test data management strategies to ensure test reliability and maintainability."

### 2. What are the hooks you are using in your framework.
"In our Cucumber framework, we use hooks for setup and teardown before and after each scenario.
-   **`@Before` hooks:** We use them to initialize the `WebDriver` instance, set up browser capabilities (e.g., headless mode), maximize the browser window, and delete cookies. For API tests, we might set up default request specifications.
-   **`@After` hooks:** These are critical for cleanup. We use them to quit the `WebDriver` (closing all browser windows), take screenshots on test failure (and embed them in the report), and perform any database cleanup if test data was created during the scenario."

### 3. What is for @before you used in your framework?
`@Before` in Cucumber is a hook that runs **before each scenario**.
Its main purpose is to set up the necessary preconditions for the scenario to run in isolation.
"In my framework, `@Before` hooks are used to initialize resources. For example, before each UI test scenario, we launch a new browser instance and navigate to the base URL. This ensures that every test starts from a clean, known state, which is crucial for deterministic and reliable test results."

### 4. Were you using background feature and for what purpose in your framework?
"Yes, we use the `Background` feature in Cucumber. It's used to define a common set of `Given` steps that apply to *all* scenarios within a feature file.
**Purpose:** Instead of repeating the same three 'Given' steps (e.g., 'User is logged in', 'User is on the dashboard') at the beginning of every scenario, we put them in a `Background` block. This makes the feature file cleaner, more readable, and highlights what's unique about each scenario. It establishes a baseline state for all tests in that feature."

### 5. How do you pass test data?
"We primarily use two methods:
1.  **Cucumber `Scenario Outline` with `Examples` table:** For data-driven UI tests, especially for negative test cases (e.g., invalid login attempts).
2.  **Cucumber `Data Tables`:** For passing collections of structured data within a single step (e.g., a list of items to add to a cart).
3.  **External JSON/Excel files (via Step Definitions):** For more complex or larger datasets, our step definitions read test data from external JSON or Excel files, which are then parsed and used by the automation code."

### 6. Scenario: assume we have given below data in feature file and write code in step definition to pass all the 4 test data in UI using data table.
**Feature File:**
```gherkin
Scenario: Verify user names
  Given I am on the user list page
  When I verify the following users are present:
    | first_name | last_name |
    | jack       | sparrow   |
    | tim        | tom       |
```

**Step Definition (`UserSteps.java`):**
```java
import io.cucumber.datatable.DataTable;
import java.util.List;
import java.util.Map;

public class UserSteps {

    // Assuming a UserListPage object
    private UserListPage userListPage; 

    @When("I verify the following users are present:")
    public void iVerifyTheFollowingUsersArePresent(DataTable dataTable) {
        List<Map<String, String>> users = dataTable.asMaps(String.class, String.class);
        for (Map<String, String> user : users) {
            String firstName = user.get("first_name");
            String lastName = user.get("last_name");
            // Assuming your page object has a method to verify user presence
            Assert.assertTrue(userListPage.isUserPresent(firstName, lastName), 
                              "User " + firstName + " " + lastName + " not found.");
        }
    }
}
```

### 7. Scenario: Given a table structure and asked to retrieve all the table data. write code to return only unique value ignoring the duplicates in the table data.
**HTML Table:**
```html
<table id="table">
  <tr>
    <td>jack</td>
    <td>jack</td>
  </tr>
  <tr>
    <td>tim</td>
    <td>tim</td>
  </tr>
</table>
```

**Selenium Code:**
```java
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class TableDataReader {

    public Set<String> getUniqueTableData(WebDriver driver, String tableId) {
        Set<String> uniqueData = new HashSet<>();
        WebElement table = driver.findElement(By.id(tableId));
        
        List<WebElement> rows = table.findElements(By.tagName("tr"));
        for (WebElement row : rows) {
            List<WebElement> cells = row.findElements(By.tagName("td"));
            for (WebElement cell : cells) {
                uniqueData.add(cell.getText().trim());
            }
        }
        return uniqueData;
    }

    public static void main(String[] args) {
        // Assume driver is initialized and navigated to a page with the table
        // WebDriver driver = new ChromeDriver();
        // Set<String> data = new TableDataReader().getUniqueTableData(driver, "table");
        // System.out.println(data); // Expected: [jack, tim]
    }
}
```

### 8. Given amazon link and asked to write xpath for a particular element which in under ul\li tag.
This is a practical XPath question. Let's assume you're looking for an element (e.g., a specific menu item) within a navigation list.

**Example HTML:**
```html
<ul id="nav-main-menu">
  <li class="nav-item"><a href="/deals">Today's Deals</a></li>
  <li class="nav-item"><a href="/customer-service">Customer Service</a></li>
</ul>
```

**XPath to find "Today's Deals" link:**
1.  **By link text:** `//a[text()="Today's Deals"]` (Simplest if text is unique and stable).
2.  **Relative to parent `li` and `ul`:** `//ul[@id='nav-main-menu']/li/a[text()="Today's Deals"]`
3.  **Using `contains` for text:** `//a[contains(text(), "Deals")]`

The most robust XPath depends on the specific, real-world HTML structure. Always inspect the page first.

### 9. which version of selenium you use in your project?
"We are currently using **Selenium WebDriver 4.x** (specify the exact version if you know it, e.g., 4.1.2). We upgraded from Selenium 3.x to take advantage of the improved W3C WebDriver protocol compliance, native support for `RelativeLocators`, and enhanced Grid capabilities."

### 10. what are the major changes from version 3 to version 4
-   **W3C WebDriver Standard Compliance:** Selenium 4 is fully W3C compliant, which means better cross-browser compatibility and stability. Selenium 3 used the JSON Wire Protocol.
-   **`RelativeLocators` (Friendly Locators):** New API to find elements relative to other known elements (e.g., `toLeftOf`, `below`, `above`, `near`). Very useful for dynamic UIs.
-   **Improved Selenium Grid:** Simpler setup (single JAR for both Hub and Node), better Docker support, and automatic test distribution.
-   **Native Chrome DevTools Protocol (CDP) Support:** Allows direct interaction with browser features like network mocking, performance metrics, and geolocation simulation.
-   **Removed Desired Capabilities:** Replaced by `Options` classes (e.g., `ChromeOptions`, `FirefoxOptions`).

### 11. How do you perform regression in your project?
"Regression testing is a critical part of our CI/CD pipeline.
1.  **Automation:** Our entire regression suite is automated using Selenium and REST-assured.
2.  **CI Trigger:** This suite is automatically triggered by **Jenkins** on every code merge to the `main` branch, or nightly for a comprehensive run.
3.  **Environment:** It runs against our dedicated QA or Staging environment.
4.  **Reporting:** Results are pushed to **ExtentReports** and aggregated in Jenkins, providing immediate feedback on any regressions introduced.
5.  **Targeted Regression:** For smaller changes, we might also run a more targeted subset of the regression suite relevant to the specific area of change."

### 12. Tell me roadmap of your career as software tester.
This tests your ambition and self-awareness.
"My career roadmap as a software tester is focused on evolving from an effective automation engineer to a well-rounded SDET (Software Development Engineer in Test) and eventually to a Test Architect.
-   **Short-term (1-2 years):** Deepen my expertise in performance testing (e.g., JMeter, k6) and explore advanced security testing techniques. I also want to contribute more to infrastructure setup, potentially leveraging Docker for test environment consistency.
-   **Mid-term (3-5 years):** Transition into a Test Lead or SDET Lead role, where I can mentor junior engineers, define test strategies for complex projects, and contribute to overall software design from a testability perspective. I aim to be proficient in designing resilient test architectures that scale with the product.
-   **Long-term (5+ years):** Aspire to a Test Architect position, focusing on defining enterprise-wide testing strategies, evaluating new tools and technologies, and driving best practices for quality assurance across multiple teams."
