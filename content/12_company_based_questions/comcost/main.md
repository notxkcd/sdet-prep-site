---
title: "ComCost"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

ComCost L1 and L2 rounds interview questions:
--------------------------------------------
1)How you will select the stories
2)explain epic and feature
3)explain CI and CD
4)Write testcase f creating password 
5)explain static 
6)Explain Git
7)explain Get method
8)difference beween post and put
9)How you will use the authendication in postman? 
10)Dependence on method
11)write end to end script for passing values in selenium
12)Reverse the string
13)Explain about project

---

## Answers (No-BS Java QA / SDET Explanations)

### 1) How you will select the stories
This refers to the **Sprint Planning** meeting in Scrum.
"The Product Owner presents the highest priority user stories from the product backlog. The development team (including QA) then discusses each story to understand the requirements and the effort involved. We collectively 'select' the stories by committing to a set of them that we are confident we can complete within the sprint, based on our team's velocity and the story point estimates."

### 2) explain epic and feature
-   **Epic:** A very large user story that is too big to be completed in a single sprint. It's a high-level placeholder for a major piece of functionality. Example: "Implement Online Payment System".
-   **Feature:** A distinct piece of functionality that delivers value to the user. Epics are broken down into multiple features or user stories. Example: "Pay with Credit Card" and "Pay with PayPal" would be two features/stories within the "Implement Online Payment System" epic.

### 3) explain CI and CD
-   **CI (Continuous Integration):** A development practice where developers merge their code changes into a central repository frequently. Each merge triggers an automated build and an automated test run (unit, integration). The goal is to find integration bugs early and provide rapid feedback.
-   **CD (Continuous Delivery/Deployment):** The practice of automatically deploying every change that passes the automated tests to a production-like environment (Continuous Delivery) or directly to production (Continuous Deployment). This ensures that the software can be released reliably at any time.

### 4) Write testcase f creating password
**Feature:** Password Creation
**Test Case ID:** TC_PWD_01
**Title:** Verify password creation meets all validation criteria.

**Scenarios:**
-   **Positive:**
    -   Create a password that meets all criteria (e.g., 10 characters, 1 uppercase, 1 number, 1 special character). **Expected:** Success message.
-   **Negative (Equivalence Partitioning & Boundary Value Analysis):**
    -   Test a password with 7 characters (below min length). **Expected:** "Password must be at least 8 characters long."
    -   Test a password with no uppercase letter. **Expected:** "Password must contain an uppercase letter."
    -   Test a password with no number. **Expected:** "Password must contain a number."
    -   Test a password with no special character. **Expected:** "Password must contain a special character."
    -   Test a password that is identical to the username. **Expected:** "Password cannot be the same as the username."

### 5) explain static
`static` is a Java keyword that means the member (variable or method) belongs to the **class itself**, not to an instance of the class.
-   **`static` variable:** A single copy is shared among all objects of the class.
-   **`static` method:** Can be called directly on the class (`MyClass.myMethod()`) without creating an object.

### 6) Explain Git
Git is a **distributed version control system**. It's a tool used to track changes in source code. It allows multiple developers to work on the same project simultaneously without overwriting each other's work. It keeps a history of every change, so you can revert to previous versions if needed.

### 7) explain Get method
The `GET` method is an HTTP verb used to **request and retrieve** data from a specified resource on a server. It should be safe (no side-effects on the server) and idempotent (calling it multiple times produces the same result).

### 8) difference beween post and put
-   **`POST`:** Creates a new resource. Not idempotent. (e.g., creating a new user).
-   **`PUT`:** Replaces an existing resource entirely. Is idempotent. (e.g., updating a user's entire profile).

### 9) How you will use the authendication in postman?
The interviewer probably means "authentication".
"In Postman, I use the **Authorization** tab to handle authentication.
-   For **Basic Auth**, I enter the username and password directly in the fields provided.
-   For token-based authentication, like **Bearer Token**, I first make a login request to get the token. I then store this token in an environment variable (e.g., `{{accessToken}}`). For all subsequent requests, I set the authorization type to 'Bearer Token' and use `{{accessToken}}` as the token value. This makes it easy to reuse the token across many requests."

### 10) Dependence on method
This likely refers to TestNG's `dependsOnMethods` attribute. It's a way to specify that a test method should only be run if another specific test method has successfully completed.

```java
@Test
public void login() {
    // ... login logic ...
}

@Test(dependsOnMethods = { "login" })
public void verifyDashboard() {
    // This test will only run if the 'login' test passes.
    // If 'login' fails, this test will be skipped.
}
```
> **Side Note:** While useful, overusing `dependsOnMethods` can make your test suite brittle and hard to maintain. Tests should be as independent as possible.

### 11) write end to end script for passing values in selenium
This is a request for a complete, simple test script.

```java
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class EndToEndScript {
    public static void main(String[] args) {
        WebDriver driver = new ChromeDriver();
        try {
            // 1. Navigate
            driver.get("http://example-login-page.com");

            // 2. Find elements and pass values
            WebElement usernameInput = driver.findElement(By.id("username"));
            usernameInput.sendKeys("testuser");

            WebElement passwordInput = driver.findElement(By.id("password"));
            passwordInput.sendKeys("password123");

            // 3. Perform action
            WebElement loginButton = driver.findElement(By.id("login-button"));
            loginButton.click();

            // 4. Validate outcome
            WebElement welcomeMessage = driver.findElement(By.id("welcome-message"));
            String message = welcomeMessage.getText();
            if (message.contains("Welcome, testuser")) {
                System.out.println("Test Passed!");
            } else {
                System.out.println("Test Failed!");
            }
        } finally {
            // 5. Cleanup
            driver.quit();
        }
    }
}
```

### 12) Reverse the string
The standard answer: `new StringBuilder(str).reverse().toString();`

### 13) Explain about project
Standard.
