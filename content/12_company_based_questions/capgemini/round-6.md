---
title: "Capgemini-6"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

Capgemini virtual
-----------------
1. Tell about yourself
2. Explain oops concept 
3. Explain implicit wait and explicit wait
4. Difference between list and array
5. Reverse the string
6. Http methods
7. Explain about your frame work 
8. What is method overload and method override
9. Explain https codes
10. Cucumber components 
11. Where parallel test we run.
12. We have six tabs open and in one tab your name appear ...write a code for to find a name in selenium 
13. Go to Amazon...you entered the watch section find all the links appear
14. Explain your project.

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. Tell about yourself
Standard opening. Concise, professional, focusing on relevant skills and experience.

### 2. Explain oops concept
The four pillars of Object-Oriented Programming:
-   **Encapsulation:** Bundling data and methods into a single unit and hiding implementation details.
-   **Abstraction:** Showing only essential features, hiding complexity.
-   **Inheritance:** Reusing code by creating new classes from existing ones.
-   **Polymorphism:** "Many forms," allowing objects of different classes to be treated as objects of a common type (e.g., method overloading and overriding).

### 3. Explain implicit wait and explicit wait
-   **Implicit Wait (Bad Practice):** A global setting that tells WebDriver to poll the DOM for a certain amount of time when trying to find an element. It masks timing issues and makes tests slower and less predictable.
-   **Explicit Wait (Good Practice):** Uses `WebDriverWait` with `ExpectedConditions` to wait for a *specific condition* to be true for a maximum amount of time. It's precise, reliable, and crucial for stable UI automation.

### 4. Difference between list and array
-   **Array:**
    -   Fixed size (size defined at creation, cannot change).
    -   Can store primitives or objects.
    -   Part of Java language basics.
-   **`List` (e.g., `ArrayList`):**
    -   Dynamic size (can grow or shrink).
    -   Can store only objects (uses wrapper classes for primitives).
    -   Part of the Java Collections Framework. Provides many utility methods.

### 5. Reverse the string
`new StringBuilder(str).reverse().toString();`

### 6. Http methods
The verbs used in HTTP requests: `GET` (retrieve), `POST` (create), `PUT` (replace/update), `PATCH` (partial update), `DELETE` (delete).

### 7. Explain about your frame work
Describe your automation framework's architecture: its core tools (Java, Selenium, TestNG), design patterns (Page Object Model), data management strategy (JSON/Excel files with `@DataProvider`), reporting tools (ExtentReports), and CI/CD integration (Maven, Jenkins).

### 8. What is method overload and method override
-   **Overloading:** Same method name, different parameters (number or type), within the same class. (Compile-time polymorphism).
-   **Overriding:** Same method signature, in a child class providing its own implementation of a parent's method. (Run-time polymorphism).

### 9. Explain https codes
This is likely a typo for **HTTP status codes**.
-   **1xx:** Informational.
-   **2xx (Success):** `200 OK`, `201 Created`, `204 No Content`.
-   **3xx (Redirection):** `301 Moved Permanently`.
-   **4xx (Client Error):** `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`.
-   **5xx (Server Error):** `500 Internal Server Error`, `503 Service Unavailable`.

### 10. Cucumber components
-   **Feature Files:** `.feature` files containing Gherkin scenarios.
-   **Step Definitions:** Java classes with methods implementing the Gherkin steps.
-   **Test Runner:** A JUnit/TestNG class to execute the tests.
-   **Hooks:** (`@Before`, `@After`) for setup/teardown.

### 11. Where parallel test we run.
Parallel tests are typically run:
-   **On a local machine:** Configured via `testng.xml` for local execution (e.g., `parallel="methods"`).
-   **On a Selenium Grid:** A distributed test environment where tests run simultaneously across multiple browser instances on different machines.
-   **In a CI/CD pipeline (Jenkins):** Jenkins jobs can be configured to execute tests in parallel on a Grid or multiple agents.

### 12. We have six tabs open and in one tab your name appear ...write a code for to find a name in selenium
This requires iterating through all window handles and switching focus.

```java
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import java.util.Set;

public class FindNameInTab {
    public static void findNameInTabs(WebDriver driver, String nameToFind) {
        String originalHandle = driver.getWindowHandle();
        Set<String> allHandles = driver.getWindowHandles();

        for (String handle : allHandles) {
            driver.switchTo().window(handle);
            // Check if the current tab's page source contains the name
            if (driver.getPageSource().contains(nameToFind)) {
                System.out.println("Name '" + nameToFind + "' found in tab with title: " + driver.getTitle());
                // Optionally, break or interact with this tab
                // driver.findElement(By.id("someElement")).click();
                break; // Exit loop once found
            }
        }
        driver.switchTo().window(originalHandle); // Always switch back to original
    }
}
```

### 13. Go to Amazon...you entered the watch section find all the links appear
```java
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import java.util.List;

public class FindAllLinks {
    public static void findAllLinks(WebDriver driver) {
        // Assume you are already on the Amazon watch section page
        // driver.get("https://www.amazon.com/watches"); 
        
        List<WebElement> links = driver.findElements(By.tagName("a"));
        System.out.println("Total links found: " + links.size());

        for (WebElement link : links) {
            String href = link.getAttribute("href");
            String text = link.getText();
            if (href != null && !href.isEmpty()) {
                System.out.println("Link Text: " + text + ", Href: " + href);
            }
        }
    }
}
```

### 14. Explain your project.
Standard.
