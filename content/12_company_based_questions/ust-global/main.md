---
title: "UST Global"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

UST Global Interview Questions

1)Self Intro
2)What is your current project & what domain you are currently working?
3)What is the difference between smoke & sanity testing?
4)What is the difference between regression testing & retesting
5)What is mean by boundary value analysis & equivalence partitioning
6)What is the difference between waterfall & agile module
7)What is agile testing
8)What is mean by sprint retrospective
9)What is burn down chart
10)For what purpose we are using JIRA
11)What is bug life cycle
12)What is meant by priority & severity
13)Once the Url is ready what is the basic validation you will do
14)What are the applications you tested in mobile
15)What is the android version of the mobile you have tested
16)What is mean by CRUD?
17)What are the methods used in postman
18)What is the purpose of post,put,delete?
19)What is the tool used for API?
20)Which tool have you used in Automation?
21)How do you identify suitable test case for Automation
22)Types of waits in selenium
23)What are the TestNG Annotations
24)What is meant by Before class Annotations
25)How to generate reports in TestNg
26) Difference between method overloading & method overriding
27) What is feature file in cucumber
28) How will you handle dropdown in selenium
29) How will you handle multiple windows in selenium
30) Difference between close & quit
31) Program:Swape the 2 numbers using 3rd variable
32) Difference between authorization & authentication
33) What is the Testplan contains?
34) Example for high priority & high severity bug
35) In Amazon, Flipkart tell about one high priority and one high severity bug
36) One example for low priority and low severity
37) What are the locators in xpath
38) Which locators can be used frequently

---

## Answers (No-BS Java QA / SDET Explanations)

### 1) Self Intro
Standard. Role, tech stack, achievements, what you're looking for.

### 2) What is your current project & what domain you are currently working?
Be specific about the application and industry. Example: "My current project is automating the regression suite for a FinTech application – a trading platform for commodities. The domain is financial services."

### 3) What is the difference between smoke & sanity testing?
-   **Smoke Test:** Broad and shallow. Performed on a new build to ensure the most critical functions work and the build is stable enough for further testing. If it fails, the build is rejected.
-   **Sanity Test:** Narrow and deep. Performed after a minor change or bug fix to ensure the change works and hasn't broken anything closely related.

### 4) What is the difference between regression testing & retesting
-   **Retesting:** Verifying a bug fix. Running the *same* test case that originally found the bug to confirm it's fixed.
-   **Regression Testing:** Verifying that new changes (features, fixes) haven't broken existing, previously working functionality. Running a *suite* of existing tests.

### 5) What is mean by boundary value analysis & equivalence partitioning
-   **Equivalence Partitioning:** Dividing input data into partitions (classes) where all values in a class are expected to behave the same. Test one value from each class.
-   **Boundary Value Analysis:** Testing the values at the boundaries of these partitions (min, max, just inside min, just outside max). Errors are most common at boundaries.

### 6) What is the difference between waterfall & agile module
-   **Waterfall:** Linear, sequential model. Each phase (requirements, design, implementation, testing) must be completed before the next begins. Inflexible, hard to adapt to changes.
-   **Agile:** Iterative, incremental. Focuses on small, frequent releases (sprints), customer collaboration, and adapting to change. Flexible, rapid feedback.

### 7) What is agile testing
Agile testing is a software testing practice that follows the principles of Agile software development. It means:
-   **Continuous:** Testing is done continuously, not just at the end.
-   **Collaborative:** Testers work closely with developers and product owners.
-   **Early:** Testing starts early in the development cycle (shift-left).
-   **Iterative:** Tests are part of each sprint, providing rapid feedback.
-   **Automated:** Heavy reliance on test automation (unit, API, UI) to support continuous feedback.

### 8) What is mean by sprint retrospective
A meeting held at the end of each sprint where the Scrum team discusses what went well, what could be improved, and creates actionable plans for the next sprint. It's about process improvement.

### 9) What is burn down chart
A burn-down chart is a graphical representation of the work remaining in a sprint (or project) against time.
-   **X-axis:** Time (days in a sprint).
-   **Y-axis:** Remaining work (e.g., story points, hours).
-   **Ideal line:** Shows the expected progress.
-   **Actual line:** Shows the actual progress.
It helps the team visualize their progress and identify if they are on track to complete the sprint goals.

### 10) For what purpose we are using JIRA
Jira is a project management and issue tracking tool.
-   **Bug Tracking:** Reporting, tracking, and managing defects.
-   **User Story Management:** Creating and tracking user stories and tasks.
-   **Test Case Management:** (With plugins like Xray/Zephyr) Linking test cases to stories and tracking test execution.
-   **Project Workflow:** Managing the workflow of tasks and issues through various statuses.

### 11) What is bug life cycle
The stages a bug goes through from discovery to resolution: New -> Open/Assigned -> Fixed -> Ready for QA -> Closed (or Reopened if fix fails).

### 12) What is meant by priority & severity
-   **Priority:** Business urgency (High, Medium, Low). Decided by Product Owner.
-   **Severity:** Technical impact on the system (Critical, Major, Minor, Trivial). Decided by QA.

### 13) Once the Url is ready what is the basic validation you will do
This is a smoke test on a new URL/build.
1.  **Accessibility:** Can I actually navigate to the URL? (No `404 Not Found`).
2.  **Basic Content:** Is the main title correct? Is the key content visible (e.g., logo, main navigation bar)?
3.  **Login (if applicable):** Can I log in successfully?
4.  **Overall Look & Feel:** Does it look like the correct application, not a broken page?
This is a quick, high-level check to ensure the environment is up and the application is minimally functional.

### 14) What are the applications you tested in mobile
Mention specific types of apps if you have, or general categories. "I've primarily tested mobile web applications, ensuring our responsive web design works correctly across various device sizes. I've also done some testing on a hybrid mobile application built with React Native."

### 15) What is the android version of the mobile you have tested
Be specific if you can. "I've tested on Android versions 10, 11, and 12, focusing on common devices like Samsung Galaxy and Google Pixel."

### 16) What is mean by CRUD?
CRUD stands for Create, Read, Update, Delete. These are the four basic functions that any persistent storage application (like a database or an API that manages resources) should be able to perform.
-   **Create:** Adding new data/resources. (e.g., `POST` request to an API)
-   **Read:** Retrieving data/resources. (e.g., `GET` request to an API)
-   **Update:** Modifying existing data/resources. (e.g., `PUT` or `PATCH` request to an API)
-   **Delete:** Removing data/resources. (e.g., `DELETE` request to an API)

### 17) What are the methods used in postman
Postman supports all standard HTTP methods, including:
-   `GET`
-   `POST`
-   `PUT`
-   `PATCH`
-   `DELETE`
-   `HEAD`
-   `OPTIONS`

### 18) What is the purpose of post,put,delete?
-   **POST:** To create a new resource on the server.
-   **PUT:** To completely update or replace an existing resource with new data.
-   **DELETE:** To remove a resource from the server.

### 19) What is the tool used for API?
-   **Automated Testing:** REST-assured (Java), Postman (with scripting), Karate.
-   **Manual/Exploratory Testing:** Postman, Insomnia.

### 20) Which tool have you used in Automation?
"I primarily use **Selenium WebDriver** for UI automation, **REST-assured** for API automation, **TestNG** as my test runner, and **Maven** for build automation and dependency management. For CI/CD, we integrate with **Jenkins**."

### 21) How do you identify suitable test case for Automation
Not everything should be automated.
-   **High Priority / Critical Functionality:** Core business flows (e.g., login, checkout).
-   **Repetitive Tasks:** Tests that need to be run frequently (e.g., regression suite, smoke tests).
-   **Stable Functionality:** Areas of the application that don't change often.
-   **Data-Driven Scenarios:** Tests that require running with many different data sets.
-   **Non-Functional (Performance/Load):** Automation is essential here.

Avoid automating:
-   One-time tests.
-   Rarely used functionality.
-   Functionality that changes very frequently.
-   Exploratory testing (it's inherently manual).

### 22) Types of waits in selenium
-   **Explicit Wait:** (`WebDriverWait`) - The recommended wait. Waits for a *specific condition* to be true.
-   **Implicit Wait:** (`driver.manage().timeouts().implicitlyWait()`) - A global wait. Bad practice, avoid.
-   **Fluent Wait:** A more configurable explicit wait (`WebDriverWait` is built on it).

### 23) What are the TestNG Annotations
`@Test`, `@BeforeSuite`, `@AfterSuite`, `@BeforeTest`, `@AfterTest`, `@BeforeClass`, `@AfterClass`, `@BeforeMethod`, `@AfterMethod`, `@DataProvider`, `@Parameters`.

### 24) What is meant by Before class Annotations
`@BeforeClass` in TestNG marks a method that will be executed **once** before any of the test methods in the current class are run. It's typically used for class-level setup, like initializing the `WebDriver` if you're going to reuse the same browser instance for all tests in that class.

### 25) How to generate reports in TestNg
TestNG generates basic HTML and XML reports by default. For more professional and detailed reports:
-   **ExtentReports:** Integrate using TestNG listeners. It generates rich HTML reports with dashboards, step details, and embedded screenshots.
-   **Allure Reports:** Integrate using TestNG listeners. Generates comprehensive, interactive reports with trend analysis.

### 26) Difference between method overloading & method overriding
-   **Overloading:** Same method name, different parameters, same class. Compile-time polymorphism.
-   **Overriding:** Same method name, same parameters, parent-child classes. Runtime polymorphism.

### 27) What is feature file in cucumber
A plain text file with a `.feature` extension that describes a software feature in Gherkin syntax (`Given/When/Then`). It serves as documentation and a test script.

### 28) How will you handle dropdown in selenium
Use the `Select` class for `<select>` HTML elements: `Select dropdown = new Select(driver.findElement(By.id("dropdownId"))); dropdown.selectByVisibleText("Option Text");`

### 29) How will you handle multiple windows in selenium
Use window handles: `driver.getWindowHandle()` for the current window, `driver.getWindowHandles()` for all windows, then `driver.switchTo().window(handle)` to switch focus.

### 30) Difference between close & quit
-   `driver.close()`: Closes the **current** window or tab that the driver is focused on. If it's the only window, the browser might remain open in the background (process not killed).
-   `driver.quit()`: Closes **all** windows/tabs opened by the WebDriver session and safely terminates the WebDriver/browser process. This is the **critical** method to call in your `@AfterMethod` or `finally` block to prevent memory leaks and orphaned browser processes.

### 31) Program:Swape the 2 numbers using 3rd variable
```java
public void swapNumbers(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
    System.out.println("a: " + a + ", b: " + b);
}
```

### 32) Difference between authorization & authentication
-   **Authentication:** Verifies *who* you are. ("Are you who you say you are?") This typically involves a username and password.
-   **Authorization:** Determines *what* you are allowed to do once authenticated. ("What are you allowed to access?") This involves permissions and roles (e.g., an admin can delete users, a guest cannot).

### 33) What is the Testplan contains?
A test plan defines the scope, strategy, resources, and schedule for testing. It includes:
-   Test objectives
-   Scope (in/out)
-   Test strategy/approach
-   Roles and responsibilities
-   Environment setup
-   Entry/Exit criteria
-   Schedule, resources, tools
-   Risks and mitigation.

### 34) Example for high priority & high severity bug
-   **High Priority, High Severity:** "The 'Place Order' button on the checkout page is completely broken, preventing all users from making purchases." (Impacts core business, no workaround).

### 35) In Amazon, Flipkart tell about one high priority and one high severity bug
-   **Amazon High Priority/High Severity:** "On Prime Day, the 'Add to Cart' button stops working for all products, preventing all sales."
-   **Amazon Low Priority/Low Severity:** "A minor typo in the 'About Us' section of a less visited page."

### 36) One example for low priority and low severity
-   **Low Priority, Low Severity:** "A minor cosmetic misalignment of an icon on a rarely used administrative page that doesn't affect functionality."

### 37) What are the locators in xpath
XPath allows using many attributes and relationships:
-   **Attributes:** `@id`, `@name`, `@class`, `starts-with(@id, 'prefix')`, `contains(@class, 'part')`.
-   **Text:** `text()='Some Text'`.
-   **Axes:** `parent::`, `ancestor::`, `following-sibling::`, `preceding-sibling::`.
-   **Logical operators:** `and`, `or`.

### 38) Which locators can be used frequently
-   **`By.id()`:** If available and stable, it's the fastest and most reliable.
-   **`By.cssSelector()`:** Generally preferred after ID for its speed and readability, especially for complex selections.
-   **`By.xpath()`:** Essential for complex scenarios, navigating by text, or using axes, but can be slower.
-   **`By.name()`:** Good for form elements.
-   `By.className()`: Use with caution as classes are often not unique.
