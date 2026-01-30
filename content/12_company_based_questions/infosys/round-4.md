---
title: "Infosys-4"
date: 2026-01-30
draft: false
---

---

## Original Questions

- Infosys virtual interview
--------------------------
1) Tell me something about yourself.
2) What are your Role and Responsibilities in the current project?
3)How will you drag and drop in selenium?
4) What is the scenario outline?
5) What is the page factory Why do we use it?
6) What are the new features in Selenium 4?
7)cucumber hook class
8) What is fluent wait?
9) HTTP methods explain CRUD operations with example
10) JWT explains?
11) Different status codes and he asked me about 429
12) What do you mean by Bearer tokens

---

## Answers (No-BS Java QA / SDET Explanations)

### 1) Tell me something about yourself.
Standard opener. Keep it concise, professional, and focus on your relevant experience (automation skills, tech stack, achievements).

### 2) What are your Role and Responsibilities in the current project?
"My role is an SDET (Software Development Engineer in Test). My core responsibilities include:
-   **Automation Framework Development:** Designing, developing, and maintaining our Java-based test automation framework.
-   **Test Scripting:** Writing automated UI tests using Selenium and API tests using REST-assured.
-   **CI/CD Integration:** Integrating test suites into Jenkins pipelines for continuous testing.
-   **Defect Management:** Identifying, reporting, and tracking bugs in Jira.
-   **Collaboration:** Working closely with developers and product owners to ensure testability and quality throughout the SDLC."

### 3) How will you drag and drop in selenium?
You use the `Actions` class in Selenium.

```java
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;

public class DragAndDropExample {
    public void performDragAndDrop(WebDriver driver) {
        // Locate the source and target elements
        WebElement sourceElement = driver.findElement(By.id("draggable"));
        WebElement targetElement = driver.findElement(By.id("droppable"));

        // Create an Actions object
        Actions actions = new Actions(driver);

        // Perform the drag and drop
        actions.dragAndDrop(sourceElement, targetElement).perform();
    }
}
```

### 4) What is the scenario outline?
In Cucumber, a `Scenario Outline` is used for **data-driven testing**. It defines a template for a test scenario that will be executed multiple times with different sets of input data. The data is provided in an `Examples` table, and `<placeholders>` are used in the scenario steps to represent the data values.

### 5) What is the page factory Why do we use it?
-   **Page Factory:** A specific implementation of the Page Object Model (POM) provided by Selenium. It uses the `@FindBy` annotation to locate WebElements and the `PageFactory.initElements()` method to initialize them.
-   **Why use it?** It simplifies the creation of Page Objects by automatically initializing WebElements. It also potentially reduces boilerplate code.

> **Note:** Many experienced engineers now advise caution or avoiding Page Factory, as its lazy loading can mask `StaleElementReferenceException` issues and its performance can be less predictable than explicit `driver.findElement()` calls.

### 6) What are the new features in Selenium 4?
1.  **W3C WebDriver Protocol Compliance:** Fully compliant with the W3C standard, leading to more consistent cross-browser behavior.
2.  **Relative Locators (Friendly Locators):** New API to find elements relative to other elements (`toLeftOf`, `above`, `below`, `near`).
3.  **Improved Selenium Grid:** Easier setup, better Docker support, and automatic test distribution.
4.  **Native Chrome DevTools Protocol (CDP) Integration:** Allows direct interaction with browser features like network mocking, performance metrics, and geolocation simulation.

### 7) cucumber hook class
A class containing methods annotated with Cucumber's `@Before`, `@After`, `@BeforeStep`, `@AfterStep`. These "hooks" are used to set up preconditions and clean up resources before/after scenarios or steps.

### 8) What is fluent wait?
A `FluentWait` is a highly configurable explicit wait in Selenium. It allows you to define:
-   The maximum timeout.
-   The polling interval (how often to check the condition).
-   Which exceptions to ignore while polling.
`WebDriverWait` is actually a subclass of `FluentWait` with predefined defaults. You use `FluentWait` when `WebDriverWait`'s defaults are not sufficient for your specific waiting needs.

### 9) HTTP methods explain CRUD operations with example
**CRUD** stands for Create, Read, Update, Delete – the four basic functions of persistent storage. These map directly to HTTP methods in RESTful APIs:
-   **Create (POST):** `POST /users` with a request body to create a new user.
-   **Read (GET):** `GET /users/{id}` to retrieve a specific user, or `GET /users` to retrieve all users.
-   **Update (PUT/PATCH):** `PUT /users/{id}` to replace a user's entire data, or `PATCH /users/{id}` to partially update a user's data.
-   **Delete (DELETE):** `DELETE /users/{id}` to remove a specific user.

### 10) JWT explains?
**JWT** stands for **JSON Web Token**. It's a compact, URL-safe means of representing claims (information) between two parties.
-   **Structure:** Consists of three parts separated by dots: `Header.Payload.Signature`.
-   **Purpose:** Commonly used for **authentication** and **authorization** in APIs. After a user logs in, the server issues a JWT. This token is then sent with every subsequent request in the `Authorization` header to verify the user's identity and permissions.
-   **Stateless:** JWTs are stateless, meaning the server doesn't need to store session information. The token itself contains all the necessary claims.

### 11) Different status codes and he asked me about 429
-   **`429 Too Many Requests`:** The client has sent too many requests in a given amount of time ("rate limiting"). The server is telling the client to slow down.
-   Other common status codes: `200 OK`, `201 Created`, `204 No Content`, `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`, `500 Internal Server Error`.

### 12) What do you mean by Bearer tokens
A **Bearer Token** is a type of access token. In the context of OAuth 2.0 and JWTs, a "bearer token" is a security token that grants the bearer (whoever possesses the token) access to a protected resource.
-   **Usage:** It's usually sent in the `Authorization` header of an HTTP request, prefixed with the word "Bearer": `Authorization: Bearer <your-jwt-token-here>`.
-   **Concept:** Anyone in possession of the token can use it, so it must be protected (e.g., sent over HTTPS).
-   **QA Relevance:** In API automation, you typically automate a login flow to obtain a bearer token, then include it in the headers of all subsequent API requests.
