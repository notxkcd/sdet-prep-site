---
title: "Tenacitics India Pvt Ltd"
date: 2026-01-30
draft: false
---

---

## Original Questions

- Tenacitics India Pvt Ltd Technical Round -

-Self Intoduction
-About your Project
-currently you have use github?
-why github is version control?
-What is HashMap?
-What is Unit testing?
- Explain your example?
-What is smoke Testing?
- Explain your example?
-What is Regression Testing?
- Explain your example?
-What is adhoc testing?
-Difference between Scenario and Test Case?
-Write Cucumber Project Folder Structure in Notepad?
-Difference between method overloading and method overriding?
- Write Syntax in the Notepad.
-Postman API methods?
- Why PUT method is used?
-What is TestNG and What are the annotations in TestNG?
-Use of @BeforeSuite annotation?

-Scenerio Based Question : If you are copy from correct username and password from notepad and
-paste it into login fields and click submit it alerts "username or password is wrong" why?
-Any questions from your side?

---

## Answers (No-BS Java QA / SDET Explanations)

### -Self Intoduction
Standard. Keep it professional, concise, and focused on relevant experience and aspirations.

### -About your Project
Standard. Describe the project domain, your role, tech stack, and key responsibilities/achievements.

### -currently you have use github?
"Yes, I use GitHub daily for version control. Our team's entire codebase, including test automation frameworks, is hosted on GitHub. I use it to manage my feature branches, collaborate through pull requests, and track changes to our code."

### -why github is version control?
GitHub is a **hosting service for Git repositories**. Git is the actual **version control system**.
-   **Version Control:** It tracks every change made to your code, allowing you to revert to previous versions, see who made what changes, and collaborate with multiple developers without overwriting each other's work.
-   **Collaboration:** GitHub (the platform) adds features like pull requests (code review), issue tracking, and project management tools, making it a central hub for team collaboration.

### -What is HashMap?
A `HashMap` is a data structure in Java that stores key-value pairs. It provides very fast (average O(1) time complexity) retrieval of values based on their unique keys.
-   **Key Feature:** Uses hashing to store elements, so there's no inherent order.
-   **Duplicates:** Keys must be unique; values can be duplicated.
-   **Nulls:** Allows one `null` key and multiple `null` values.
-   **Use in QA:** Storing test configuration (key: "browser", value: "chrome"), mapping test data (key: "testId", value: `UserObject`), or counting occurrences of items (e.g., character frequency).

### -What is Unit testing? Explain your example?
Unit testing is the testing of the smallest testable parts of an application, in isolation.
-   **Example:** Testing a utility method in your framework like `StringUtils.reverseString(String input)`. You'd provide known inputs ("hello") and assert the expected output ("olleh"). You wouldn't launch a browser or connect to a database for a unit test.

### -What is smoke Testing? Explain your example?
A quick, high-level test of the most critical functionality of an application to ensure it's stable enough for more thorough testing.
-   **Example:** After a new build deployment, run an automated smoke test that:
    1.  Navigates to the login page.
    2.  Successfully logs in with valid credentials.
    3.  Navigates to the main dashboard.
    4.  Logs out.
    If any of these steps fail, the build is considered broken, and further testing is halted.

### -What is Regression Testing? Explain your example?
Re-testing the application after code changes (new features, bug fixes) to ensure that the new changes have not introduced new bugs or caused existing functionality to break.
-   **Example:** After a new payment gateway integration, run the entire suite of existing tests for user login, product search, add-to-cart, and all other payment methods to ensure they still work correctly.

### -What is adhoc testing?
Informal, unstructured testing without any predefined test cases or plan. You're just exploring the application randomly with the goal of finding bugs. It's highly dependent on the tester's intuition and experience. It's often compared to "monkey testing" but with a goal.

### -Difference between Scenario and Test Case?
-   **Test Case:** A formal set of steps, preconditions, and expected results designed to verify a specific functionality or requirement. Typically stored in a Test Case Management tool.
-   **Scenario (Cucumber):** A description of a specific behavior of the system, written in Gherkin syntax. It serves as a single executable test example within a feature file. Each scenario is essentially an automated test case from a user's perspective.

### -Write Cucumber Project Folder Structure in Notepad?
```
your-project-root/
├── src/
│   └── test/
│       ├── java/
│       │   └── com/
│       │       └── yourcompany/
│       │           ├── runners/        # TestNG/JUnit runner classes
│       │           │   └── TestRunner.java
│       │           ├── stepdefinitions/  # Java glue code for Gherkin steps
│       │           │   ├── LoginSteps.java
│       │           │   └── CommonSteps.java
│       │           └── pages/          # Page Object Model classes
│       │               ├── LoginPage.java
│       │               └── HomePage.java
│       └── resources/
│           └── features/       # Gherkin feature files
│               ├── login.feature
│               └── search.feature
├── pom.xml                   # Maven build file
├── testng.xml                # TestNG suite configuration (if used with TestNG runner)
└── README.md
```

### -Difference between method overloading and method overriding? Write Syntax in the Notepad.
-   **Overloading:** Same method name, different parameter list, in the same class. (Compile-time polymorphism).
    ```java
    public class Calculator {
        public int add(int a, int b) { return a + b; }
        public int add(int a, int b, int c) { return a + b + c; } // Overloaded
    }
    ```
-   **Overriding:** Same method name, same parameter list, in a child class providing a specific implementation for a parent's method. (`@Override` annotation). (Runtime polymorphism).
    ```java
    class Animal { public void makeSound() { System.out.println("Animal makes sound"); } }
    class Dog extends Animal { @Override public void makeSound() { System.out.println("Woof"); } } // Overridden
    ```

### -Postman API methods? Why PUT method is used?
Postman supports all standard HTTP methods (verbs): `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS`.
-   **`PUT` method:** Used to **completely replace** an existing resource on the server with the new data provided in the request body. It is **idempotent**, meaning performing the same PUT request multiple times will have the same effect as performing it once.

### -What is TestNG and What are the annotations in TestNG?
TestNG is a powerful testing framework for Java, used extensively for Selenium test automation.
**Annotations:**
-   **Configuration:** `@BeforeSuite`, `@AfterSuite`, `@BeforeTest`, `@AfterTest`, `@BeforeClass`, `@AfterClass`, `@BeforeMethod`, `@AfterMethod`.
-   **Test Method:** `@Test`.
-   **Data-Driven:** `@DataProvider`.

### -Use of @BeforeSuite annotation?
`@BeforeSuite` is a TestNG annotation that marks a method to be executed **once before all tests in the entire suite start**.
-   **Use Case:** Ideal for heavy, one-time setup that needs to happen before any tests begin. Examples:
    -   Initializing a Selenium Grid.
    -   Setting up global database connections or test data factories.
    -   Loading global configuration files.
    -   Generating a unique report file name for the entire test run.

### -Scenerio Based Question : If you are copy from correct username and password from notepad and -paste it into login fields and click submit it alerts "username or password is wrong" why?
This is a common real-world bug or issue.
1.  **Hidden Characters:** When copying from Notepad, you might accidentally copy invisible characters (like a non-breaking space, a tab, or a newline character) along with the username or password. The application trims these from visible input but might still process them internally, making the credentials invalid.
2.  **Input Field Stripping:** The application might have JavaScript that automatically trims whitespace from the input fields. However, if your copy-paste includes leading/trailing invisible characters, it might not be a perfect match.
3.  **Encoding Issues:** Less common, but could be an issue if the Notepad file's encoding differs from the application's expected encoding, leading to character misinterpretation.
4.  **Application Bug:** It's also possible there's a legitimate bug in the application's login form handling, where it incorrectly validates pasted input versus typed input.

**How to troubleshoot:**
-   Manually type the credentials to see if it works.
-   Use browser developer tools to inspect the actual value of the input field after pasting (check for extra characters).
-   Check application logs for more specific error messages.

### -Any questions from your side?
Always have questions. This shows engagement.
-   "What does a typical day look like for a QA Automation Engineer here?"
-   "What are the biggest technical challenges facing the QA team in the next 6-12 months?"
-   "What opportunities are there for learning and development within the team?"
-   "How does the QA team collaborate with developers and product owners in the sprint?"
