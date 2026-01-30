---
title: "Wipro-5"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

Wipro Interview - First Round -F2F - 40 to 45 mins:
--------------------------------------------------
1. Introduce yourself 
2. Roles and Responsibilities 
3. What are the tools you are using for API Testing 
4. Explain the concept about Rest Assured 
5. How will you using the OOPS concept in your framework. Explain it individually each one
6. How will you generate report in your testing 
7. Are you involved in scrum and sprint meeting. What is your contribution in that meeting
8. When will conducting retrospective meeting 
9. How will you handle the drag and drop using selenium
10. Tell me the interfaces you are using and explain it with real time scenarios with your project 
11. How many projects you are handling so far 
12. Explain about the agile methodologies in your project 
13. What are the tools you are using test case creation and defect management 
14. Java program string = Interview for Java and Selenium (Reverse each word in the given string without changing the caps and small letters) Eg: Interview= wievrenI

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. Introduce yourself
Standard opener. Focus on professional experience, automation skills, tech stack, and a key achievement.

### 2. Roles and Responsibilities
Be specific about what you do day-to-day as an SDET/QA Automation Engineer. This includes designing frameworks, writing tests (UI/API), integrating into CI/CD, bug reporting, and collaborating with the team.

### 3. What are the tools you are using for API Testing
-   **Automated Testing:** **REST-assured** (Java library).
-   **Manual/Exploratory Testing:** **Postman**.

### 4. Explain the concept about Rest Assured
REST-assured is a Java DSL (Domain Specific Language) for testing RESTful Web Services.
-   **Fluent API:** It provides a fluent, BDD-style syntax (`given().when().then()`) that makes writing API tests readable and concise.
-   **Simplifies HTTP:** It abstracts away the complexities of sending HTTP requests and parsing responses, letting you focus on testing the API's behavior.
-   **Features:** Supports various HTTP methods, authentication schemes, header/body validation, JSONPath/XMLPath for response parsing, and Hamcrest matchers for assertions.

### 5. How will you using the OOPS concept in your framework. Explain it individually each one
-   **Encapsulation:** "Our Page Object Model (POM) is a prime example. Locators and interaction methods for a web page are encapsulated within a single page class. `private By` locators are hidden, and `public` methods expose functionality (`loginPage.login()`)."
-   **Abstraction:** "We code against the `WebDriver` interface (`WebDriver driver = new ChromeDriver();`), abstracting away browser-specific implementation details. Also, our API endpoint classes abstract the details of HTTP requests."
-   **Inheritance:** "All our UI test classes `extend` a `BaseTest` class, inheriting common setup (`@BeforeMethod` for browser launch) and teardown (`@AfterMethod` for browser close) logic. Our Page Objects `extend` a `BasePage` for common page-level methods."
-   **Polymorphism:** "We use method overriding. For instance, a `BasePage` might have a `verifyPageLoaded()` method, which child Page Objects (like `DashboardPage`) override to add specific checks relevant to their page."

### 6. How will you generate report in your testing
"We use **ExtentReports** to generate comprehensive and visually rich HTML test reports.
-   **Integration:** It's integrated into our TestNG framework via a custom `ITestListener`.
-   **Features:** The listener automatically logs test start/end, pass/fail status, and crucially, captures screenshots on failure, embedding them directly into the report.
-   **Publishing:** The generated HTML reports are published as artifacts in Jenkins, making them easily accessible to the team and stakeholders."

### 7. Are you involved in scrum and sprint meeting. What is your contribution in that meeting
"Yes, I am actively involved in all Scrum meetings:
-   **Sprint Planning:** I provide estimates for testing effort (story points) and clarify requirements to ensure testability.
-   **Daily Scrum (Stand-up):** I update the team on my progress, any blockers, and my plans for the day.
-   **Sprint Review:** I demonstrate the features I've tested and automated to stakeholders.
-   **Sprint Retrospective:** I contribute feedback on team processes and help identify areas for improvement."

### 8. When will conducting retrospective meeting
A **Sprint Retrospective** is conducted at the **end of each sprint**, after the Sprint Review and before the next Sprint Planning meeting.

### 9. How will you handle the drag and drop using selenium
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

        // Perform the drag and drop action
        actions.dragAndDrop(sourceElement, targetElement).perform();
    }
}
```

### 10. Tell me the interfaces you are using and explain it with real time scenarios with your project
-   **`WebDriver`:** The primary interface for browser automation. Used for `driver = new ChromeDriver();`. Real scenario: `driver.get("url")`.
-   **`WebElement`:** Represents an HTML element. Real scenario: `driver.findElement(By.id("username")).sendKeys("user")`.
-   **`TakesScreenshot`:** For capturing screenshots. Real scenario: In an `@AfterMethod` listener, `((TakesScreenshot)driver).getScreenshotAs(OutputType.FILE)` on test failure.
-   **`JavascriptExecutor`:** For executing JavaScript in the browser context. Real scenario: `((JavascriptExecutor)driver).executeScript("arguments[0].scrollIntoView(true);", element)`.
-   **`List` and `Set` (Java Collections):** For handling collections of elements. Real scenario: `driver.findElements(By.tagName("a"))` returns a `List<WebElement>`. Using a `Set` to check for unique values.

### 11. How many projects you are handling so far
Be accurate and concise. "In my X years, I've primarily worked on Y projects, with my most recent project being..."

### 12. Explain about the agile methodologies in your project
"We follow the Scrum framework. This involves working in two-week sprints, holding daily stand-ups, conducting sprint planning at the start, and sprint reviews/retrospectives at the end. As QA, I'm involved in all phases, providing continuous feedback and ensuring quality throughout the sprint."

### 13. What are the tools you are using test case creation and defect management
-   **Test Case Creation:** We use **Jira** integrated with **Xray** (or Zephyr) for formal test case documentation, linking them to user stories. For automated tests, the Cucumber `.feature` files serve as our living documentation/test cases.
-   **Defect Management:** **Jira** is used for logging, tracking, and managing all defects throughout their lifecycle.

### 14. Java program string = Interview for Java and Selenium (Reverse each word in the given string without changing the caps and small letters) Eg: Interview= wievrenI
This is "reverse words in sentence, but keep word order".

```java
public class ReverseWordsInSentence {
    public static String reverseEachWord(String sentence) {
        if (sentence == null || sentence.isEmpty()) {
            return sentence;
        }

        String[] words = sentence.split(" "); // Split by space
        StringBuilder result = new StringBuilder();

        for (String word : words) {
            StringBuilder reversedWord = new StringBuilder(word).reverse();
            result.append(reversedWord).append(" ");
        }
        return result.toString().trim(); // Remove trailing space
    }

    public static void main(String[] args) {
        String input = "Interview for Java and Selenium";
        System.out.println("Original: " + input);
        System.out.println("Reversed: " + reverseEachWord(input));
        // Output: wievretnI rof avaJ dna muineleS
    }
}
```
The example `Interview= wievrenI` implies individual word reversal, not sentence reversal. The code above does individual word reversal.
If the example `Interview= wievrenI` means "reverse each word, keeping the first letter capitalized", that is a much harder problem. But it's usually just "reverse characters within each word".
The current code reverses characters within each word while preserving whitespace separation and original casing (because `StringBuilder.reverse()` operates on chars).
The output `wievrenI rof avaJ dna muineleS` matches the example's interpretation.
