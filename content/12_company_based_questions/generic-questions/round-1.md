---
title: "Generic Questions 1"
date: 2026-01-30
draft: false
---

---

## Original Questions

- Tell me about yourself
- Explain the projects you have done
- What are the types of locators?
- Which locator you have used most?
- What is super head of class?
Explain OOPS
- Explain Inheritance
- Explain Method Overloading
- Explain static and dynamic polymorphism
- How to handle notification popup
- Difference between quite and close
- Selenium components
- Black box testing
- Agile methodology -  daily activities
- What is the defect rejection ratio and defect leakage ratio?
Response code
- Variables in postman
- Do we use authentication token for all variables in postman
- Difference between SQL and MySQL
- Explain Epic, task and story point
- Difference between TestNG and Junit
- What are the types to navigate
- Scenario question: you have started working in Agile method, in between you need some requirements what will you do ?

---

## Answers

### Tell me about yourself
Standard opening. Provide a concise, professional summary:
-   Your current role and 2-3 key responsibilities.
-   Your tech stack (Java, Selenium, REST-assured, TestNG).
-   A quantifiable achievement or impact.
-   What you're looking for in the next role.
Keep it under 90 seconds.

### Explain the projects you have done
Focus on 1-2 most relevant projects. For each, describe:
-   The application/product you worked on (domain).
-   Your specific role and contributions (e.g., "I led the automation of the checkout flow").
-   The technologies you used.
-   Any challenges you faced and how you overcame them.
-   The impact of your work (e.g., improved test coverage, reduced test execution time).

### What are the types of locators?
Locators are how Selenium finds elements on a web page.
1.  `id`: Most preferred, if unique and stable.
2.  `name`: Good for form elements.
3.  `className`: Use with caution, often not unique.
4.  `tagName`: For finding elements by HTML tag (e.g., `<a>`, `<div>`).
5.  `linkText`: For links (`<a>`) by their exact visible text.
6.  `partialLinkText`: For links by partial visible text.
7.  `cssSelector`: Fast and powerful, especially for complex selections.
8.  `xpath`: Most flexible, can traverse DOM in any direction, essential for elements without stable attributes.

### Which locator you have used most?
"I prioritize `id` first for its reliability and speed. If `id` is not available or dynamic, I prefer `cssSelector` for its performance and robustness. I use `xpath` when `cssSelector` is not sufficient, especially for navigating by text or using axes relative to a stable parent element."

### What is super head of class?
This sounds like a misheard or custom term. There is no standard Java concept called "super head of class."
They might be referring to:
-   **`super` keyword:** Refers to the parent class.
-   **Superclass:** The parent class in an inheritance hierarchy.
-   **`Object` class:** The ultimate superclass of all classes in Java.

If you encounter such a term, clarify: "I haven't encountered that specific term before. Could you please clarify what you mean by 'super head of class'?"

### Explain OOPS
The four fundamental principles of Object-Oriented Programming:
1.  **Encapsulation:** Bundling data and methods into a single unit (class), hiding implementation details.
2.  **Abstraction:** Showing only essential information, hiding complexity.
3.  **Inheritance:** Reusing code by creating new classes that derive properties/behavior from existing ones.
4.  **Polymorphism:** "Many forms." Allowing objects of different classes to be treated as objects of a common type (e.g., method overloading and overriding).

### Explain Inheritance
Inheritance is a mechanism where one class (subclass/child class) acquires the properties and behaviors (fields and methods) of another class (superclass/parent class).
-   **Keyword:** `extends`.
-   **Purpose:** Promotes code reuse and establishes an "is-a" relationship (e.g., `Dog is an Animal`).
-   **Example in Framework:** A `BaseTest` class with common `@BeforeMethod` and `@AfterMethod` logic for WebDriver setup/teardown. All specific test classes (`LoginTest`, `SearchTest`) `extend BaseTest` to inherit this common functionality.

### Explain Method Overloading
Method overloading allows a class to have multiple methods with the same name, as long as their parameter lists are different (either the number of parameters or their data types).
-   **Compile-time Polymorphism:** The compiler decides which overloaded method to call based on the arguments provided.
-   **Purpose:** To provide flexibility and a cleaner API for methods that perform similar operations on different types or amounts of input. Example: `add(int a, int b)` and `add(double a, double b)`.

### Explain static and dynamic polymorphism
-   **Static Polymorphism (Compile-time Polymorphism):** Achieved through **method overloading**. The compiler determines which method to call based on the method signature (name + parameters) at compile time.
-   **Dynamic Polymorphism (Run-time Polymorphism):** Achieved through **method overriding**. The JVM determines which overridden method to call based on the actual type of the object at runtime. This is the core of "coding to an interface" (e.g., `WebDriver driver = new ChromeDriver();`).

### How to handle notification popup
This can refer to a few things:
1.  **Browser Native Notifications:** The little pop-ups from the browser asking for permission to show notifications. You handle these by setting browser options (e.g., `ChromeOptions.addArguments("--disable-notifications")`) before launching the browser.
2.  **HTML Modals/Pop-ups:** These are `div` elements styled to look like pop-ups. They are part of the web page's DOM. You handle them by locating their close button or other interactive elements using standard Selenium locators and clicking them.
3.  **JavaScript Alerts/Confirm/Prompt:** These are native browser dialogs. You handle them using `driver.switchTo().alert()`.

Clarify with the interviewer what kind of "notification popup" they mean.

### Difference between quite and close
-   `driver.close()`: Closes the **current** browser window or tab that the driver has focus on. If it's the only window open, the browser process might still be running in the background.
-   `driver.quit()`: Closes **all** browser windows opened by the WebDriver session and safely terminates the WebDriver/browser process. This is the **critical** command to use in your `@AfterMethod` or `finally` block to prevent orphaned browser processes and memory leaks.

### Selenium components
The core components of Selenium are:
1.  **Selenium WebDriver:** The API that allows you to write automation scripts to interact with web browsers.
2.  **Selenium Grid:** A server that allows tests to be run on multiple machines across different browsers and operating systems in parallel.
3.  **Selenium IDE:** A browser extension for recording and replaying simple interactions. (Less relevant for professional automation).

### Black box testing
Black box testing is a software testing method in which the internal structure, design, and implementation of the item being tested are unknown to the tester.
-   **Focus:** The tester interacts with the application solely through its external interfaces (UI, API) and focuses on the inputs and outputs, based on requirements.
-   **Goal:** To verify functionality from an end-user perspective.
-   **Types:** Functional testing, system testing, acceptance testing, regression testing.

### Agile methodology - daily activities
In a Scrum Agile team, my daily activities include:
1.  **Daily Stand-up (Daily Scrum):** Report on what I did yesterday, what I'll do today, and any impediments.
2.  **Test Analysis and Design:** Analyzing new user stories, clarifying requirements with the Product Owner, and designing test cases (manual and automated).
3.  **Automation Scripting:** Writing and debugging automated tests (UI, API) for new features.
4.  **Test Execution:** Running automated regression suites and performing exploratory testing on new features.
5.  **Bug Reporting and Verification:** Finding and reporting bugs in Jira, then verifying bug fixes.
6.  **Collaboration:** Working closely with developers to understand features and debug issues.

### What is the defect rejection ratio and defect leakage ratio?
-   **Defect Rejection Ratio:** The percentage of reported defects that are deemed invalid (e.g., not a bug, duplicate, not reproducible) by the development team. A high rejection ratio indicates issues in the QA process (e.g., poor bug reporting, unclear requirements).
    -   `Formula: (Number of Rejected Defects / Total Number of Reported Defects) * 100`

-   **Defect Leakage Ratio:** The percentage of defects that "leak" from one phase of testing to a later phase, particularly into production. A high leakage ratio into production indicates gaps in the testing process.
    -   `Formula: (Number of Defects Found in Production / Total Number of Defects Found) * 100`

### Response code
Refers to HTTP status codes returned by web servers and APIs. Examples:
-   `200 OK`: Success.
-   `201 Created`: Resource created.
-   `400 Bad Request`: Client-side error.
-   `401 Unauthorized`: Authentication required.
-   `403 Forbidden`: Client not authorized.
-   `404 Not Found`: Resource doesn't exist.
-   `500 Internal Server Error`: Server-side error.

### Variables in postman
Postman allows you to define variables to store and reuse values in your requests. This makes your requests more dynamic and reusable.
-   **Environment Variables:** Specific to an environment (e.g., "Dev", "QA", "Prod"). Good for base URLs, API keys per environment.
-   **Global Variables:** Available across all collections and environments.
-   **Collection Variables:** Specific to a Postman Collection.
-   **Local Variables:** Temporary variables within a request or script.
-   **Data Variables:** Used with the Collection Runner to import data from a file (CSV, JSON).

### Do we use authentication token for all variables in postman
No. You use authentication tokens specifically for **authentication and authorization**. A token, once generated (e.g., by a login request), is typically stored in an environment or collection variable. Then, it's passed in the `Authorization` header of subsequent API requests (e.g., `Authorization: Bearer {{accessToken}}`). You don't use tokens for all variables; only for those related to security context.

### Difference between SQL and MySQL
-   **SQL (Structured Query Language):** This is a **language**. It's the standard language for managing and manipulating relational databases. It's used to define, query, and modify data.
-   **MySQL:** This is a **Relational Database Management System (RDBMS)**. It's a specific software product that implements the SQL language. You use SQL *to interact with* MySQL.
    -   Other RDBMS examples: PostgreSQL, Oracle, SQL Server.

### Explain Epic, task and story point
These are Agile concepts for managing work.
-   **Epic:** A large body of work that can be broken down into smaller, manageable pieces (user stories). It often spans multiple sprints.
-   **Task:** A technical activity required to complete a user story. Developers and QAs break down user stories into tasks (e.g., "Write UI for login," "Automate login test").
-   **Story Point:** A relative measure of the effort, complexity, and uncertainty required to implement a user story. It's not a measure of time. Teams typically use a Fibonacci-like sequence (1, 2, 3, 5, 8...).

### Difference between TestNG and Junit
Both are popular testing frameworks for Java.
-   **TestNG:** Generally considered more powerful for enterprise-level test automation due to its richer set of annotations (`@BeforeSuite`, `@DataProvider`), built-in support for parallel execution, test grouping, and flexible XML configuration (`testng.xml`).
-   **JUnit:** The original and widely adopted unit testing framework. JUnit 5 (Jupiter) has brought many modern features, making it more competitive, but TestNG still holds an edge for complex test orchestration.

### What are the types to navigate
This likely refers to Selenium's navigation methods:
1.  `driver.get(url)`: Loads a URL.
2.  `driver.navigate().to(url)`: Same as `get()`.
3.  `driver.navigate().back()`: Browser back button.
4.  `driver.navigate().forward()`: Browser forward button.
5.  `driver.navigate().refresh()`: Browser refresh button.

### Scenario question: you have started working in Agile method, in between you need some requirements what will you do?
This is a test of your Agile process understanding and communication skills.
1.  **Don't assume:** "First, I would clarify exactly what requirements are missing or unclear. Is it a minor detail, or a critical piece of functionality?"
2.  **Consult the Product Owner:** "My primary point of contact would be the Product Owner. They are the voice of the customer and own the requirements. I'd explain the gap and seek clarification."
3.  **Daily Stand-up:** "I would bring this up in the daily stand-up as an impediment or a discussion point. This ensures the entire team is aware."
4.  **Backlog Refinement:** "If it's a significant new requirement, it might need to go through the backlog refinement process with the team to be properly understood, sized, and prioritized for a future sprint."
5.  **Impact Assessment:** "We'd collectively assess the impact on the current sprint. If it's critical to the current story, we might need to adjust the sprint scope. If it can wait, it would be added to the product backlog."
The key is open communication and following established Agile processes.
