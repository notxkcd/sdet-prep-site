---
title: "Wipro-4"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

Wipro L1:
----------
How to integration testing perform in your project.what approach you used
2.explain your project and roles and responsibilities
3.in your project how to test regression testing,if any one monitor regression testing and where you check status.
4.which tool you using version control.and how it's run.local or cloud.
5.waits concepts
6.instead of using explicit wait and fluent wait,can we use for loop , can we give condition in this forloop
7.you need to scroll particular element and accept popup. You give some x and y axis values ,and you completed qa test and signoff done.but it's not working in UAT environment,they use different window size,they didn't get that popup, how to you handle this situation.
8.one table having 3 columns (name,product id,quantity).another table having 3 columns(item id,price,productname).
3rd table contains name and multiplication of product price and quantity.
Resultset  gives that 3rd table values. Write program for this.
9.what are all the object mappers used in your project.
10.Do we really need retrospective meeting.why
11.in that meeting did you receive comments like you need to improve anything from your scrum master .
12.what are all the components you handle in your project.
14.@after suit ,what you are mention

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. How to integration testing perform in your project.what approach you used
"We perform integration testing primarily at the **API layer**.
-   **Approach:** We use **REST-assured** to write automated tests that verify the communication and data flow between our microservices. For example, after an order creation API call, we might verify that the order service correctly invoked the inventory service to deduct stock.
-   **Database Integration:** We also integrate with the database using **JDBC**. After an API call that modifies data, we perform direct database queries to confirm that the data was correctly persisted."
-   **Mocking/Stubbing:** For external third-party services, we use **WireMock** to mock their responses, allowing us to test our internal service's integration logic in isolation.

### 2. explain your project and roles and responsibilities
Standard.

### 3. in your project how to test regression testing,if any one monitor regression testing and where you check status.
"Our regression testing is fully automated.
-   **Execution:** Our entire regression suite is triggered automatically by **Jenkins** on every code commit to the `develop` branch and nightly against our QA environment.
-   **Monitoring:** The status is monitored in two main places:
    1.  **Jenkins Dashboard:** We have a dedicated Jenkins view that shows the status of the regression build. If it fails, the team is notified immediately via Slack.
    2.  **ExtentReports:** After each run, Jenkins publishes a detailed **ExtentReport**, which provides a clear HTML dashboard of passed, failed, and skipped tests, along with screenshots for failures.
-   **Team Involvement:** Developers and product owners can also access these reports to see the quality status of the latest build."

### 4. which tool you using version control.and how it's run.local or cloud.
"We use **Git** as our version control system. Our remote repositories are hosted on **GitHub** (which is a cloud-based service). All development and testing code is version-controlled in Git, and we follow a feature-branching workflow with pull requests for code reviews."

### 5. waits concepts
-   **Implicit Wait (Bad):** A global setting that tells Selenium to poll the DOM for a certain amount of time. Hides timing issues, slows tests.
-   **Explicit Wait (Good):** (`WebDriverWait`) Waits for a *specific condition* to be true before proceeding. Reliable, precise.
-   **Fluent Wait (Advanced Explicit Wait):** Configurable polling interval and exceptions to ignore.

### 6. instead of using explicit wait and fluent wait,can we use for loop , can we give condition in this forloop
"You *could* theoretically implement a custom wait using a `for` loop combined with `Thread.sleep()` and a condition check. However, this would be reinventing the wheel and is a **bad practice**.
-   **Reasons:**
    -   **Less Readable:** It makes your code more verbose and harder to understand.
    -   **Error Prone:** You'd have to manage exceptions, timeouts, and polling logic manually.
    -   **Already Solved:** `WebDriverWait` and `FluentWait` already provide robust, tested, and optimized implementations for this exact problem.
    -   **Maintainability:** Any changes or improvements to the waiting strategy would require updating custom loops across the entire test suite, rather than in a single `WebDriverWait` configuration."

### 7. you need to scroll particular element and accept popup. You give some x and y axis values ,and you completed qa test and signoff done.but it's not working in UAT environment,they use different window size,they didn't get that popup, how to you handle this situation.
This is a real-world scenario testing your understanding of robust automation.
"Using fixed X and Y coordinates for scrolling or clicking is a **very brittle** approach and a common cause of flakiness. It breaks when the screen size, element position, or resolution changes.
**How to handle it:**
1.  **Scroll to Element:** Instead of coordinates, use `JavascriptExecutor` to scroll the *element itself* into view: `js.executeScript("arguments[0].scrollIntoView(true);", element);`. This is dynamic and works regardless of screen size.
2.  **Pop-up Handling:**
    -   **Explicit Wait:** For the popup, use an explicit wait: `wait.until(ExpectedConditions.alertIsPresent());` for JavaScript alerts, or `wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("popup-id")));` for HTML modals. This waits for the popup to *actually appear*.
    -   **Dynamic Locators:** For the "accept" button on the popup, use a reliable locator (ID, CSS, or dynamic XPath) rather than fixed coordinates.
3.  **Root Cause Analysis:** For the UAT issue, I'd investigate:
    -   Why the popup wasn't appearing (environment issue? A/B test? different user settings?).
    -   Why the scroll failed (responsive design issue? element not present?).
    -   Then I'd update the automation script to use dynamic, reliable methods for scrolling and element interaction."

### 8. one table having 3 columns (name,product id,quantity).another table having 3 columns(item id,price,productname). 3rd table contains name and multiplication of product price and quantity. Resultset gives that 3rd table values. Write program for this.
This is a SQL `JOIN` and aggregation problem, then processed in Java.

**SQL Query (assuming `product id` and `item id` are joinable):**
```sql
SELECT
    T1.name,
    T1.quantity * T2.price AS total_value
FROM
    Table1 T1
INNER JOIN
    Table2 T2 ON T1.product_id = T2.item_id;
```

**Java Program (JDBC):**
```java
import java.sql.*;
import java.util.HashMap;
import java.util.Map;

public class ProductValueCalculator {

    public Map<String, Double> calculateProductValues(Connection connection) throws SQLException {
        Map<String, Double> productValues = new HashMap<>();
        String sql = "SELECT T1.name, T1.quantity * T2.price AS total_value " +
                     "FROM Table1 T1 INNER JOIN Table2 T2 ON T1.product_id = T2.item_id";

        try (Statement statement = connection.createStatement();
             ResultSet resultSet = statement.executeQuery(sql)) {

            while (resultSet.next()) {
                String name = resultSet.getString("name");
                double totalValue = resultSet.getDouble("total_value");
                productValues.put(name, totalValue);
            }
        }
        return productValues;
    }

    public static void main(String[] args) {
        // Example usage (replace with actual connection details)
        String url = "jdbc:mysql://localhost:3306/mydatabase";
        String user = "user";
        String password = "password";

        try (Connection conn = DriverManager.getConnection(url, user, password)) {
            ProductValueCalculator calculator = new ProductValueCalculator();
            Map<String, Double> values = calculator.calculateProductValues(conn);
            values.forEach((name, value) -> System.out.println("Product: " + name + ", Total Value: " + value));
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
```

### 9. what are all the object mappers used in your project.
"We primarily use **Jackson** (`ObjectMapper`) for JSON serialization and deserialization. This is crucial for our API tests where we:
1.  **Serialize:** Convert Java POJOs (Plain Old Java Objects) into JSON request bodies before sending them via REST-assured.
2.  **Deserialize:** Convert JSON responses from API calls back into Java POJOs for easier data validation using standard Java assertions."

### 10. Do we really need retrospective meeting.why
"Yes, absolutely. The retrospective meeting is critical for the continuous improvement aspect of Agile.
-   **Purpose:** It's the dedicated time for the team to reflect on the past sprint. We discuss what went well, what could have gone better, and identify actionable improvements for the next sprint.
-   **Why it's needed:** Without it, teams risk repeating mistakes, missing opportunities for efficiency, and not addressing underlying process issues. It's how we adapt and evolve as a team."

### 11. in that meeting did you receive comments like you need to improve anything from your scrum master .
"Yes, I appreciate constructive feedback. For example, in one retrospective, my Scrum Master suggested that I could improve my early engagement with developers during story grooming, to identify testability concerns even sooner. I took that feedback and started attending more design discussions, which helped prevent issues before development even began."

### 12. what are all the components you handle in your project.
"In my project, I primarily handle:
-   **Test Automation Framework:** Design, development, and maintenance.
-   **Automated Test Suites:** Writing and debugging UI (Selenium) and API (REST-assured) tests.
-   **CI/CD Integration:** Managing Jenkins jobs for our test runs.
-   **Test Data Management:** Creating and managing test data for automation.
-   **Defect Management:** Reporting, tracking, and verifying bugs in Jira.
-   **Test Reporting:** Generating and analyzing test execution reports."

### 14. @after suit ,what you are mention
This should be `@AfterSuite`.
"In the `@AfterSuite` method, I typically perform global teardown operations that need to run only once after all tests in the entire suite have completed.
-   **Example:** Tearing down the Selenium Grid (if it was launched programmatically).
-   **Example:** Generating and publishing the final consolidated ExtentReport, as all test results would have been collected by then."
