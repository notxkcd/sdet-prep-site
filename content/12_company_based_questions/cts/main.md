---
title: "CTS"
date: 2026-01-30
draft: false
---

---

## Original Questions

- CTS interview questions:-
1. You have test scenarios in the feature file already now you are going to write new additional scenarios,how do you generate snippets alone for new?
2. Exception handling in Java
3. Actions class
4. Java executor for disabled elements
5. SQL query - existing table retrieves the one column and  creates a temporary column but the folder has only one column
6.testng - annotation

1. What is your roles and responsibilties
2. what is feature file in Cucumber
3. what is step definition in cucumber
4. How many scenarios in the feature file
5. How many ways to define webdriver
6. TestNg annotations
7. TestNg annotations execution order
8. Dataprovider in TestNg
9. What are important files in the cucumber
10. Overall experience in IT
11. Previous experience apart from IT
12. In automation will you do manual testing anywhere
13. which tool used for CI/CD
14. Explain about the jenkins and how do  you integrate your project in jenkins
15. Which report you will get from jenkins
16. Which format or how will you share the reports to your client
17. Selenium Exceptions
18. difference between find elements and find element
19. if you have not find any element in findelement and find elements what will get return
20. How to you write test cases and have you used any tools?
21. Have you work on waterfall model or Agile methodology?
22. In agile, what are meetings have you attended?
23. What is the purpose of restrospective meeting?
24. If you get user stories how will you start your work?
25. what is nosuch driver exception

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. You have test scenarios in the feature file already now you are going to write new additional scenarios, how do you generate snippets alone for new?
When you add new Gherkin steps to a `.feature` file that don't have corresponding step definitions (Java methods), Cucumber will tell you.
1.  **Run the test:** Execute your Cucumber test runner.
2.  **Look for "Undefined steps":** Cucumber will identify the new, undefined steps and print "snippets" to the console output. These snippets are Java method stubs with the correct regular expressions to match your Gherkin steps.
3.  **Copy and paste:** Copy these generated snippets and paste them into your step definition file.
4.  **Implement:** Fill in the method body with your automation code (Selenium, REST-assured, etc.).

This is how Cucumber helps you bridge the gap between human-readable scenarios and executable code.

### 2. Exception handling in Java
Using `try-catch-finally` blocks.
-   `try`: Code that might throw an exception.
-   `catch`: Code to execute if a specific exception occurs.
-   `finally`: Code that *always* executes, regardless of whether an exception was thrown. Used for cleanup (`driver.quit()`).

### 3. Actions class
Selenium's `Actions` class is used to perform complex user interactions like mouse hovers (`moveToElement`), right-clicks (`contextClick`), double-clicks (`doubleClick`), and drag-and-drop actions. You build a sequence of actions and then execute them with `.perform()`.

### 4. Java executor for disabled elements
You use `JavascriptExecutor` to interact with disabled elements, but it's generally a **bad practice** for testing. A user cannot interact with a disabled element, so your test shouldn't either.
If you *must* interact (e.g., to confirm the element exists but is disabled), you can use `JavascriptExecutor` to read its value or even force a click, but this bypasses the actual user experience.

```java
JavascriptExecutor js = (JavascriptExecutor) driver;
// To click a disabled element (use with extreme caution)
js.executeScript("arguments[0].click();", disabledElement);
// To get the value of a disabled input
String value = (String) js.executeScript("return arguments[0].value;", disabledElement);
```

### 5. SQL query - existing table retrieves the one column and creates a temporary column but the folder has only one column
This question is poorly phrased, especially the "folder has only one column" part. Assuming they mean: "Retrieve one column from an existing table and add a calculated or constant temporary column to the result."

```sql
-- Retrieve a column and add a constant temporary column
SELECT ProductName, 'In Stock' AS Status 
FROM Products;

-- Retrieve a column and add a calculated temporary column (e.g., based on other columns)
SELECT FirstName, LastName, (Salary * 0.10) AS Bonus
FROM Employees;
```
This is a basic `SELECT` statement with an aliased calculated column.

### 6. testng - annotation
`@Test` marks a method as a test case. Other common annotations: `@BeforeMethod`, `@AfterMethod`, `@BeforeClass`, `@AfterClass`, `@DataProvider`.

### 1. What is your roles and responsibilties
Standard. Focus on test automation, framework development, CI/CD integration, bug reporting, and collaboration with dev/product.

### 2. what is feature file in Cucumber
A `.feature` file is a plain-text file written in Gherkin syntax (`Given/When/Then`) that describes a feature or behavior of the software from a user's perspective. It contains scenarios that detail specific test cases.

### 3. what is step definition in cucumber
A step definition is a Java method (in our context) annotated with `@Given`, `@When`, or `@Then` (from the Cucumber library) that provides the actual automation code to execute a corresponding Gherkin step from a feature file. It's the "glue code" between the human-readable scenario and the technical automation.

### 4. How many scenarios in the feature file
A feature file can contain one or many scenarios. There's no fixed limit, but for readability and maintainability, it's usually best to keep the number of scenarios focused on a single feature or logical set of behaviors. If a file gets too long, it might be split into multiple feature files.

### 5. How many ways to define webdriver
There aren't "ways to define WebDriver" as much as there are different implementations of the `WebDriver` interface and different ways to instantiate them.
1.  **Direct instantiation:** `WebDriver driver = new ChromeDriver();`
2.  **Remote WebDriver:** `WebDriver driver = new RemoteWebDriver(new URL("http://localhost:4444/wd/hub"), capabilities);` (for Selenium Grid).
3.  **Third-party (e.g., Appium):** `WebDriver driver = new AppiumDriver(new URL("..."), capabilities);` (though Appium has its own driver type).
4.  **`EventFiringWebDriver`:** A wrapper around a standard WebDriver to listen to events.

### 6. TestNg annotations
Refer to previous answers. `@Test`, `@BeforeSuite`, `@AfterSuite`, `@BeforeTest`, `@AfterTest`, `@BeforeClass`, `@AfterClass`, `@BeforeMethod`, `@AfterMethod`, `@DataProvider`.

### 7. TestNg annotations execution order
`@BeforeSuite -> @BeforeTest -> @BeforeClass -> @BeforeMethod -> @Test -> @AfterMethod -> @AfterClass -> @AfterTest -> @AfterSuite`.

### 8. Dataprovider in TestNg
`@DataProvider` is an annotation that marks a method that provides test data to a TestNG `@Test` method. The DataProvider method must return `Object[][]` or `Iterator<Object[]>`. The `@Test` method specifies the DataProvider by name.

### 9. What are important files in the cucumber
1.  **`.feature` files:** Contain the Gherkin scenarios.
2.  **Step definition files:** Java classes containing the automation code for the Gherkin steps.
3.  **Test Runner class:** A Java class that orchestrates the Cucumber test execution (using `@RunWith(Cucumber.class)` and `@CucumberOptions`).
4.  **`pom.xml` (Maven):** Manages dependencies (Cucumber, Selenium, TestNG) and the build process.

### 10. Overall experience in IT
State your total years of experience, and possibly a breakdown of roles (e.g., "5 years in IT, with the last 3 focused on QA Automation and SDET roles").

### 11. Previous experience apart from IT
If applicable, briefly mention it if it taught you transferrable skills (e.g., "I worked in customer service, which taught me strong communication skills and user empathy, valuable for understanding user pain points in testing."). If not relevant, keep it short or just state "No, my career has always been in IT."

### 12. In automation will you do manual testing anywhere
"Absolutely. A good automation engineer understands that not everything should be automated. I regularly perform:
-   **Exploratory Testing:** For new features, to find bugs that automated scripts might miss.
-   **Usability Testing:** To provide feedback on the user experience.
-   **Ad-hoc Testing:** Quick checks.
-   **Bug Verification:** To confirm that a reported bug has been fixed."

### 13. which tool used for CI/CD
"We use **Jenkins** for our CI/CD pipelines. It automatically builds our project, runs the test suites, and deploys to various environments." (Other options: GitLab CI, GitHub Actions, Azure DevOps Pipelines).

### 14. Explain about the jenkins and how do you integrate your project in jenkins
Jenkins is an open-source automation server.
**Integration with Project:**
1.  **Source Code Management (SCM):** Configure the Jenkins job to pull code from a Git repository.
2.  **Build Trigger:** Set up a webhook (e.g., GitHub webhook) or polling interval to trigger a build when code changes are pushed.
3.  **Build Steps:** Define the steps Jenkins should execute (e.g., `mvn clean install` to build the project and `mvn test` to run the tests).
4.  **Post-Build Actions:** Configure Jenkins to publish test reports (e.g., Surefire reports, ExtentReports), archive artifacts, and send notifications.

### 15. Which report you will get from jenkins
Jenkins itself provides basic build status reports.
-   **Test Results:** It can parse **JUnit/TestNG XML reports** (generated by Maven Surefire/Failsafe plugins) to display test trends, individual test results, and failure messages directly in the Jenkins UI.
-   **Custom Reports:** If you integrate tools like ExtentReports or Allure, Jenkins can publish these more sophisticated HTML reports, making them accessible via a link in the build history.

### 16. Which format or how will you share the reports to your client
-   **Automated Email:** Jenkins can be configured to email a summary of the test run (pass/fail count, link to detailed report) to stakeholders upon completion.
-   **HTML Reports:** For detailed analysis, clients are often given access to the generated HTML reports (e.g., ExtentReports, Allure reports) which are published as build artifacts in Jenkins.
-   **Dashboard:** Some companies use dedicated dashboards (e.g., qTest, TestRail) that aggregate test results from various sources, providing a centralized view for clients.

### 17. Selenium Exceptions
`NoSuchElementException`, `StaleElementReferenceException`, `TimeoutException`, `ElementNotInteractableException`, `InvalidSelectorException`.

### 18. difference between find elements and find element
-   `findElement()`: Returns a single `WebElement`. Throws `NoSuchElementException` if not found.
-   `findElements()`: Returns a `List<WebElement>`. Returns an empty list if no elements are found.

### 19. if you have not find any element in findelement and find elements what will get return
-   `findElement()`: Throws a `NoSuchElementException`.
-   `findElements()`: Returns an empty `List<WebElement>`.

### 20. How to you write test cases and have you used any tools?
"We write our test cases in **Jira**, using a dedicated Test Case Management plugin like Xray. Each test case is linked to a user story, and follows a standard structure including a title, preconditions, steps (actions and expected results), and test data. For automated tests, we link the automated script directly to the test case in Jira."

### 21. Have you work on waterfall model or Agile methodology?
"I have primarily worked in Agile methodology, specifically Scrum."

### 22. In agile, what are meetings have you attended?
Sprint Planning, Daily Stand-up, Backlog Grooming, Sprint Review, Sprint Retrospective.

### 23. What is the purpose of restrospective meeting?
To reflect on the past sprint and identify opportunities for continuous improvement in the team's processes and collaboration.

### 24. If you get user stories how will you start your work?
1.  **Understand Requirements:** Read the user story and acceptance criteria.
2.  **Ask Questions:** During backlog grooming, ask clarifying questions to the Product Owner/BA. Identify edge cases, non-functional requirements, and potential ambiguities.
3.  **Test Case Design:** Based on the requirements, start designing test cases (manual or automated) that cover all positive, negative, and edge scenarios.
4.  **Identify Automation Candidates:** Determine which test cases are best suited for automation.
5.  **Test Data Preparation:** Identify and prepare necessary test data.
6.  **Automation Scripting:** Start writing the automation scripts.

### 25. what is nosuch driver exception
This is usually `NoSuchDriverException` (or similar). It typically means:
1.  **WebDriver executable not found:** Selenium cannot find the `chromedriver.exe`, `geckodriver.exe`, etc., in the specified path or on the system PATH.
2.  **Driver version mismatch:** The browser version and the WebDriver executable version are incompatible.
3.  **Driver not initialized:** You tried to use `driver` without initializing it first.
Solution: Ensure you have the correct WebDriver executable for your browser version and it's properly configured (e.g., using `WebDriverManager` or `System.setProperty`).
