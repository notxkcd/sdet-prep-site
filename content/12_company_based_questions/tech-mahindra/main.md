---
title: "Tech Mahindra"
date: 2026-01-30
draft: false
---

---

## Original Questions

- Tech Mahindra Questions
-----------------------
Tell about yourself
Explain about the cucumber framework
Write feature file for login page
what is TestNG and its advantages?
Annotations used in testng?
How will you pass test data in testng?
what is maven and its purpose?
what is POM?
Have you used Gitlab ?
write the dependency which you add in pom.xml for Selenium in notepad 
Coding - sum of two integer arrays. 
Eg:
int arr1 [] = {2,3,4,5,6}
int arr2 [] = {7,8,9,10,11}
Exception - how will you handle exceptions.
what is SDLC and which sdlc methodology you are following? 
Experience in API & RestAssured 
Tool used for API Testing
Explain about http methods.
Explain Response codes.

---

## Answers

> Many of these questions are standard framework and process questions. See previous files for more detailed answers on some topics.

### Tell about yourself
Standard opener. Role, responsibilities, tech stack, achievements. Keep it concise.

### Explain about the cucumber framework
Cucumber is a tool that supports Behavior-Driven Development (BDD). It lets you write test cases in a human-readable language called Gherkin.
-   **`.feature` files:** Contain the Gherkin scenarios (`Given/When/Then`). They describe the behavior of the application from a user's perspective.
-   **Step Definitions:** Java methods that are "glued" to each Gherkin step. This is where the actual automation code (like Selenium calls) lives.
-   **Runner Class:** A JUnit or TestNG class that configures and runs the tests, specifying where to find feature files and step definitions.
Its main purpose is to improve communication between technical and non-technical team members.

### Write feature file for login page

```gherkin
# features/login.feature
Feature: User Authentication

  Background:
    Given the user is on the login page

  Scenario: Successful login with valid credentials
    When the user enters valid username and password
    Then the user should be redirected to the dashboard

  Scenario Outline: Unsuccessful login with invalid credentials
    When the user enters "<username>" and "<password>"
    Then an error message "<message>" should be displayed

    Examples:
      | username      | password      | message                |
      | "invalid_user"| "wrong_pass"  | "Invalid credentials." |
      | "valid_user"  | ""            | "Password is required."|
      | ""            | "valid_pass"  | "Username is required."|
```

### what is TestNG and its advantages?
TestNG is a testing framework for Java, inspired by JUnit but with more powerful features. It's the de-facto standard for Selenium test automation in Java.

**Advantages:**
1.  **Powerful Annotations:** Provides a rich set of annotations (`@BeforeSuite`, `@BeforeClass`, `@BeforeMethod`, etc.) for fine-grained control over test setup and teardown.
2.  **Data-Driven Testing:** Excellent built-in support for data-driven tests via the `@DataProvider` annotation.
3.  **Grouping:** Allows you to group tests (e.g., `@Test(groups="smoke")`) and then run specific groups.
4.  **Parallel Execution:** Simple to configure parallel test execution in `testng.xml` to significantly speed up your test suite.
5.  **Parameterization:** Easy to pass parameters to tests from the `testng.xml` file.
6.  **Dependent Tests:** You can make tests dependent on one another (e.g., a test runs only if another one passes).

### Annotations used in testng?
-   **Setup/Teardown:** `@BeforeSuite`, `@AfterSuite`, `@BeforeTest`, `@AfterTest`, `@BeforeClass`, `@AfterClass`, `@BeforeMethod`, `@AfterMethod`.
-   **Test:** `@Test`.
-   **Data:** `@DataProvider`, `@Parameters`.
-   **Listeners:** `@Listeners`.

### How will you pass test data in testng?
1.  **`@DataProvider` (Best way):** A method annotated with `@DataProvider` returns a 2D array of objects (`Object[][]`). A test method can then consume this data, running once for each row in the array. This is the most flexible approach for data-driven testing.

    ```java
    @DataProvider(name = "loginData")
    public Object[][] provideLoginData() {
        return new Object[][] {
            { "user1", "pass1" },
            { "user2", "pass2" }
        };
    }

    @Test(dataProvider = "loginData")
    public void testLogin(String username, String password) {
        // ... test logic
    }
    ```

2.  **`@Parameters` / `testng.xml` (For simple parameters):** You can define simple string parameters in your `testng.xml` file and have TestNG pass them to your `@Test` or `@Before` methods. This is good for environment-level configuration like browser name or base URL.

    ```xml
    <!-- in testng.xml -->
    <test name="MyTest">
      <parameter name="browser" value="chrome"/>
      <classes>
        <class name="com.mytests.LoginTest"/>
      </classes>
    </test>
    ```
    ```java
    // in LoginTest.java
    @BeforeMethod
    public void setup(@Parameters("browser") String browserName) {
        // ... setup logic using browserName
    }
    ```

### what is maven and its purpose?
Maven is a build automation and project management tool. Its purpose is to standardize and simplify the process of building Java projects.
1.  **Dependency Management:** Its most important feature. It automatically downloads and manages all third-party libraries (dependencies) from a central repository. You just declare them in `pom.xml`.
2.  **Standard Build Lifecycle:** Provides a standard set of phases (`compile`, `test`, `package`, etc.) to build the project. `mvn test` runs your entire test suite.

### what is POM?
This can mean two things.
1.  **Project Object Model (Maven):** The `pom.xml` file. It's the core configuration file for a Maven project, defining its dependencies, build process, and metadata.
2.  **Page Object Model (Selenium):** A design pattern for test automation where you create a Java class for each page of your web application. This class encapsulates the locators and interaction logic for that page, separating it from the test scripts.

Given the context, they likely mean the Maven POM, but it's good to clarify or mention both.

### Have you used Gitlab ?
"Yes. GitLab is a complete DevOps platform built around Git. While I've used GitHub more frequently, I've used GitLab for version control, CI/CD pipelines (using `.gitlab-ci.yml`), and its integrated container registry."

### write the dependency which you add in pom.xml for Selenium in notepad
```xml
<dependency>
    <groupId>org.seleniumhq.selenium</groupId>
    <artifactId>selenium-java</artifactId>
    <version>4.1.2</version> <!-- Or whatever the latest stable version is -->
</dependency>
```

### Coding - sum of two integer arrays.
This is ambiguous. It could mean concatenating them, or summing them element-wise. Assuming element-wise sum into a new array.

```java
public class ArraySummer {
    public static int[] sumArrays(int[] arr1, int[] arr2) {
        // Assuming arrays are of the same length, as in the example.
        // A robust solution would handle different lengths.
        if (arr1.length != arr2.length) {
            throw new IllegalArgumentException("Arrays must have the same length.");
        }
        
        int[] result = new int[arr1.length];
        for (int i = 0; i < arr1.length; i++) {
            result[i] = arr1[i] + arr2[i];
        }
        return result;
    }
}
```

### Exception - how will you handle exceptions.
-   For **checked exceptions** (like `IOException`), which are predictable, you use a `try-catch` block to handle the error gracefully.
-   For **runtime exceptions** (like `NullPointerException`), they usually indicate a bug in the code. The best "handling" is to let the exception be thrown and fail the test, so the bug is visible and can be fixed.
-   In test automation, a **`finally`** block is critical for resource cleanup, especially `driver.quit()`, to ensure it runs even if the test fails with an exception.
-   In Selenium, the best way to "handle" exceptions like `NoSuchElementException` is to **prevent** them by using robust explicit waits.

### what is SDLC and which sdlc methodology you are following?
SDLC is the Software Development Life Cycle, a process for planning, creating, testing, and deploying an information system.

"I am following the **Agile** methodology, specifically **Scrum**. We work in two-week sprints, with a focus on delivering small, incremental pieces of working software and adapting to changing requirements."

### Experience in API & RestAssured
"Yes, I have extensive experience in API testing. I use **REST-assured** with Java and TestNG to automate our API tests. My tests cover status code validation, response body assertions using JSONPath, contract testing against a Swagger/OpenAPI spec, and end-to-end scenarios where I chain multiple API calls together."

### Tool used for API Testing
-   **Automation:** REST-assured (for Java).
-   **Manual/Exploratory Testing:** Postman. It's excellent for quickly sending requests, inspecting responses, and trying out new endpoints.

### Explain about http methods.
-   `GET`: Retrieve data.
-   `POST`: Create new data.
-   `PUT`: Completely replace existing data.
-   `PATCH`: Partially update existing data.
-   `DELETE`: Remove data.

### Explain Response codes.
-   `2xx` (Success): `200 OK`, `201 Created`, `204 No Content`.
-   `3xx` (Redirection): `301 Moved Permanently`, `302 Found`.
-   `4xx` (Client Error): `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`. Your request is wrong.
-   `5xx` (Server Error): `500 Internal Server Error`, `503 Service Unavailable`. The server is broken. This is a bug.
