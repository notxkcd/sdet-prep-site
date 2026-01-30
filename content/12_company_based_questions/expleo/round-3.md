---
title: "Expleo-3"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

Expleo interview questions
----------------------------
Tell me about yourself
Reusability and maintainability in agile 
Exception types 
How handle exception
Selenium exceptions
How will you handle this
Getters and setters How  do use 
Explain Functional testing and functional testing 
 explain Window handles 
explain How to handle mouse hover in selenium
Explain wait concept and types
Explain  types of xpath 
Explain cucumber framework
Reverse  the string program
Input=test automation
Output=automation test write the program
What is mobile testing
Which tool you use mobile testing
Explain agile methodology 
What is scrum ceremonies 
Can you parallam test in Selenium script it is possible And how to test
Explain pom
Why you pom in your project
What data driven
What is the purpose of reusable class

---

## Answers (No-BS Java QA / SDET Explanations)

### Tell me about yourself
Standard opener. Keep it concise, professional, and highlight your relevant experience and skills.

### Reusability and maintainability in agile
-   **Reusability:** In Agile, we aim to deliver small, working increments. Reusability means building components (code, test modules) that can be used across multiple tests or features without having to rewrite them. For example, a `LoginPage` class is reusable across all tests that need to log in.
-   **Maintainability:** Code (and tests) should be easy to understand, modify, and extend. Good design patterns (like POM) and clean coding practices directly contribute to maintainability. In Agile, frequent changes make maintainability paramount.

### Exception types
In Java, exceptions are primarily categorized into:
-   **Checked Exceptions:** Compiler forces you to handle them (e.g., `IOException`, `SQLException`).
-   **Unchecked Exceptions (Runtime Exceptions):** You are not required to handle them; they usually indicate programming errors (e.g., `NullPointerException`, `ArrayIndexOutOfBoundsException`).

### How handle exception
Using `try-catch-finally` blocks.
-   **`try`:** Contains code that might throw an exception.
-   **`catch`:** Catches and handles specific types of exceptions.
-   **`finally`:** Code that always executes, regardless of an exception, typically for cleanup.

### Selenium exceptions
Common exceptions: `NoSuchElementException`, `StaleElementReferenceException`, `TimeoutException`, `ElementNotInteractableException`, `InvalidSelectorException`.

### How will you handle this
This likely refers to handling the Selenium exceptions mentioned above. The key is to prevent them through robust framework design:
-   **`NoSuchElementException`:** Use accurate, stable locators and **explicit waits**.
-   **`StaleElementReferenceException`:** Re-find the element before interaction, or use explicit waits that re-locate.
-   **`TimeoutException`:** Adjust explicit wait timeouts if justified, or investigate application performance.
-   **`ElementNotInteractableException`:** Scroll to element, wait for it to be enabled/visible.

### Getters and setters How do use
Getters (`get...()`) are public methods to retrieve the value of a private field. Setters (`set...()`) are public methods to modify the value of a private field. They are used to implement **encapsulation**, providing controlled access to an object's internal state.

### Explain Functional testing and functional testing
This is a duplicate. Assuming it means Functional vs. Non-Functional Testing.
-   **Functional Testing:** Verifies that the system behaves according to its specifications and business requirements. It checks *what* the system does (e.g., unit, integration, system, acceptance testing).
-   **Non-Functional Testing:** Verifies *how well* the system performs. It checks non-functional requirements like performance, security, usability, and scalability.

### explain Window handles
`driver.getWindowHandle()` gets the ID of the current window. `driver.getWindowHandles()` gets all window IDs. `driver.switchTo().window(handle)` switches the driver's focus to a specific window. Used for managing multiple browser windows/tabs.

### explain How to handle mouse hover in selenium
You use the `Actions` class and its `moveToElement()` method.

```java
import org.openqa.selenium.interactions.Actions;
// ...
Actions actions = new Actions(driver);
WebElement elementToHover = driver.findElement(By.id("menuItem"));
actions.moveToElement(elementToHover).perform();
```

### Explain wait concept and types
(Duplicate of previous questions). Implicit, Explicit, Fluent waits. Explicit waits are recommended.

### Explain types of xpath
(Duplicate of previous questions). Absolute (bad) and Relative (good).

### Explain cucumber framework
(Duplicate of previous questions). BDD, Gherkin, Feature Files, Step Definitions, Runner Class, Hooks.

### Reverse the string program Input=test automation Output=automation test write the program
This means reversing the order of words in a sentence.

```java
public class SentenceReverser {
    public static String reverseWordOrder(String sentence) {
        if (sentence == null || sentence.trim().isEmpty()) {
            return sentence;
        }
        String[] words = sentence.trim().split("\\s+"); // Split by one or more spaces
        StringBuilder reversed = new StringBuilder();
        for (int i = words.length - 1; i >= 0; i--) {
            reversed.append(words[i]).append(" ");
        }
        return reversed.toString().trim(); // Remove trailing space
    }

    public static void main(String[] args) {
        System.out.println(reverseWordOrder("test automation")); // Output: automation test
    }
}
```

### What is mobile testing
Testing applications on mobile devices (native apps, mobile web apps, hybrid apps). Tools like Appium are commonly used.

### Which tool you use mobile testing
"I primarily use **Appium** for mobile test automation, leveraging its capabilities to test native, hybrid, and mobile web applications across Android and iOS platforms. For mobile web testing, I also use Selenium WebDriver with browser emulation."

### Explain agile methodology
(Duplicate of previous questions). Iterative, incremental, short sprints, customer collaboration, continuous feedback.

### What is scrum ceremonies
The key meetings in Scrum:
-   **Sprint Planning:** What work will be done.
-   **Daily Scrum (Stand-up):** Daily sync on progress, blockers.
-   **Sprint Review:** Demo of completed work to stakeholders.
-   **Sprint Retrospective:** Team inspects and adapts its process.

### Can you parallam test in Selenium script it is possible And how to test
"Yes, parallel testing is absolutely possible in Selenium using TestNG.
-   **How:** You configure your `testng.xml` file by setting the `parallel` attribute on the `<suite>` tag (e.g., `parallel="methods"` or `parallel="tests"`) and specifying `thread-count`.
-   **Tools:** For true parallel execution across different machines/browsers, you use **Selenium Grid** or a cloud-based testing platform like BrowserStack/Sauce Labs."

### Explain pom
(Duplicate of previous questions). Page Object Model: a design pattern for test automation.

### Why you pom in your project
"We use the Page Object Model because it significantly enhances the **maintainability, readability, and reusability** of our test automation code. When UI elements change, we only need to update the locator in one Page Object class, rather than in every test script that uses that element."

### What data driven
Data-driven testing is an automation approach where test data is separated from the test logic. The same test script is executed multiple times with different sets of input data and expected results. This allows for more efficient testing of various scenarios without modifying the test code itself.

### What is the purpose of reusable class
A reusable class contains generic helper methods or common functionalities that can be used across multiple tests or page objects.
-   **Purpose:** To avoid code duplication, improve maintainability (change once, affect everywhere), and make tests more concise.
-   **Examples:** A `WebDriverFactory` to manage browser instantiation, a `ScreenshotUtil` class, an `ExcelReader` class.
