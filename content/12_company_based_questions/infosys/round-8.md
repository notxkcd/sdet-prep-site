---
title: "Infosys-8"
date: 2026-01-30
draft: false
---

---

## Original Questions

- Infosys - Virtual mode - interviewer Rajiv
----------------------
1. Self Introduction
2. Project - role
3. Java version, Selenium version
4. write Take Screenshot
5. what are the exception you have faced and how will you handle-  explain it?
6. Explain Our Framework? BBD -Explain
7. what is WebElement?
8. what is NoStale element exception and how will you handle it?
9. what is broken link?
10. Explain n-1 approach?
11. Difference between stateful and stateless?
12. How comfortable are you with different Stack?
13. Status code for Gateway Timeout and Request Timeout?
14. digest auth?
15. how will you get bearer token?
16. Security Testing?

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. Self Introduction
Standard. Keep it concise, professional, and focus on your relevant experience (automation skills, tech stack, achievements).

### 2. Project - role
Standard. Describe the project domain, your specific role and contributions as an automation engineer.

### 3. Java version, Selenium version
"I am currently using **Java 11 (or 17)** and **Selenium WebDriver 4.x** (e.g., 4.1.2). We upgraded to Selenium 4 to take advantage of its W3C WebDriver protocol compliance and new features like Relative Locators."

### 4. write Take Screenshot
```java
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import java.io.File;
import java.io.IOException;
import org.apache.commons.io.FileUtils; // Requires Apache Commons IO

public void captureScreenshot(WebDriver driver, String filePath) {
    try {
        File srcFile = ((TakesScreenshot) driver).getScreenshotAs(OutputType.FILE);
        FileUtils.copyFile(srcFile, new File(filePath));
    } catch (IOException e) {
        System.err.println("Failed to take screenshot: " + e.getMessage());
    }
}
```

### 5. what are the exception you have faced and how will you handle- explain it?
-   **`NoSuchElementException`:** Handled by using robust locators and, more importantly, **explicit waits** before interacting with elements.
-   **`StaleElementReferenceException`:** Handled by re-finding the element just before interaction or by making the explicit waits intelligent enough to re-locate.
-   **`TimeoutException`:** Indicates a genuine application performance issue or a too-short wait. Handled by investigating the application or adjusting the wait time if justified.
-   **Java Exceptions:** Use `try-catch` blocks for expected situations like `IOException` during file operations. Unhandled runtime exceptions should fail the test.

### 6. Explain Our Framework? BBD -Explain
This is likely a typo for "BDD - Explain".
"Our framework is a Java-based automation framework. It uses **Selenium WebDriver** for UI tests and **REST-assured** for API tests. The core design pattern is the **Page Object Model**. We leverage **TestNG** as our test runner for its advanced features like parallel execution and data providers. We primarily follow a **BDD (Behavior-Driven Development)** approach using **Cucumber**. This means our test scenarios are written in human-readable Gherkin in `.feature` files, which serve as living documentation and bridge the gap between technical and non-technical stakeholders."

### 7. what is WebElement?
In Selenium, a `WebElement` is an interface that represents an HTML element on a web page. It's the primary way to interact with elements like buttons, input fields, links, etc., using methods like `click()`, `sendKeys()`, `getText()`, `getAttribute()`.

### 8. what is NoStale element exception and how will you handle it?
This is a typo for **`StaleElementReferenceException`**.
-   **What it is:** Occurs when a `WebElement` reference you previously located becomes "stale" because the element is no longer attached to the DOM (e.g., due to an AJAX update or page navigation).
-   **How to handle:** The most reliable way is to **re-find the element** just before you interact with it. Avoid storing `WebElement` instances as class variables if they might become stale. Use explicit waits that re-locate elements (like `ExpectedConditions.elementToBeClickable()`).

### 9. what is broken link?
A broken link is a hyperlink that no longer works. When you try to access it, it returns an HTTP status code indicating an error (most commonly `404 Not Found`). In automated testing, you check for broken links by sending `HEAD` (or `GET`) requests to all `href` attributes on a page and verifying the HTTP response codes.

### 10. Explain n-1 approach?
The "n-1 approach" in testing typically refers to the strategy of supporting and testing against the **current major version (n)** of a software component (like a browser or operating system) and the **previous major version (n-1)**. This helps ensure compatibility with the most common user environments without excessively increasing the testing matrix.

### 11. Difference between stateful and stateless?
-   **Stateful:** A system or application is stateful if it retains information about past interactions or the current context between requests. The server remembers the client's state. (e.g., A traditional web session where the server stores user data).
-   **Stateless:** A system or application is stateless if each request from a client to the server contains all the information necessary to understand the request. The server does not store any client state between requests. (e.g., A RESTful API, where each request must include authentication tokens, data, etc.).

### 12. How comfortable are you with different Stack?
This asks about your versatility with different technology stacks.
"I am very comfortable working with **Java-based test automation stacks** (Selenium, TestNG, REST-assured). I have a foundational understanding of JavaScript and some exposure to Python for scripting. I am always keen to learn and adapt to new technologies required by the project."

### 13. Status code for Gateway Timeout and Request Timeout?
-   **`504 Gateway Timeout`:** The server, while acting as a gateway or proxy, did not receive a timely response from an upstream server it needed to access to complete the request.
-   **`408 Request Timeout`:** The server did not receive a complete request message within the time that it was prepared to wait.

### 14. digest auth?
**Digest Authentication** is a simple challenge-response authentication mechanism in HTTP. It's an improvement over Basic Authentication because it sends a hash of the username, password, and a server-generated nonce (number used once), rather than sending credentials in plain text. This makes it more secure against eavesdropping.

### 15. how will you get bearer token?
You typically obtain a bearer token by making a `POST` request to a specific authentication endpoint of the API, sending your username and password in the request body. The API then responds with the bearer token (usually a JWT) in its response body. This token is then used in the `Authorization: Bearer <token>` header for subsequent protected API calls.

### 16. Security Testing?
Security testing is a type of software testing that aims to uncover vulnerabilities in an application that could lead to data breaches, unauthorized access, or system compromise.
-   **Types:** Penetration testing, vulnerability scanning, ethical hacking, security auditing.
-   **QA's Role:** While specialized security testers do deep dives, QAs contribute by:
    -   Testing authentication and authorization controls.
    -   Validating input fields for common injection attacks (e.g., SQL injection, XSS).
    -   Ensuring sensitive data is handled securely (e.g., encrypted in transit).
    -   Verifying session management.
    -   Checking for secure default configurations.
