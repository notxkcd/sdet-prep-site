---
title: "Infosys-7"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

L1 in Infosys(virtual) one of the interviewer Asha
-------------------------------------------------
1. Tell me about yourself , Roles and Responsibilities and overall experience
2. go to google.com and in search box type "infosys technologies" out of  the options everytime we need to choose Nth option, write a code for this 
3. what is super keyword in java
4. what is inheritance
5. what is getters and setters in java
6. what are all the exceptions you have faced in your project
7. what are collections in java
8. what is the difference between List and ArrayList?
9. how to handle no stale element exception
10. what do we use pom.xml
11. why should we give dependencies , what does it do
12. what is action class
13. suppose if i have 2 tabs, and i have to go to second tab and do actions , how to do it ?
14. how do you handle multiple windows, write code for it and explain
15. you said you worked in ajile methodologies, what is velocity
16. how many manual testcases you write in a week
17. how many testcases you will automate 
18. what is the industry standard for test cases and its automation ?

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. Tell me about yourself , Roles and Responsibilities and overall experience
Standard opener. Focus on professional experience, specific years in automation, and outline your roles and responsibilities.

### 2. go to google.com and in search box type "infosys technologies" out of the options everytime we need to choose Nth option, write a code for this
This requires handling search suggestions.

```java
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.time.Duration;
import java.util.List;

public class GoogleSearchNthOption {
    public static void selectNthSuggestion(WebDriver driver, String searchTerm, int n) {
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        
        driver.get("https://www.google.com");
        
        // Find the search box and type the search term
        WebElement searchBox = driver.findElement(By.name("q"));
        searchBox.sendKeys(searchTerm);
        
        // Wait for search suggestions to appear
        By suggestionsLocator = By.xpath("//ul[@role='listbox']//li[@role='presentation']//div[@role='option']//div[1]//span");
        wait.until(ExpectedConditions.visibilityOfElementLocated(suggestionsLocator));
        
        // Get all suggestions
        List<WebElement> suggestions = driver.findElements(suggestionsLocator);
        
        // Check if the Nth option exists
        if (n > 0 && n <= suggestions.size()) {
            WebElement nthOption = suggestions.get(n - 1); // Nth option is at index n-1
            System.out.println("Selecting: " + nthOption.getText());
            nthOption.click();
        } else {
            System.out.println("Nth option not found or out of bounds. Number of suggestions: " + suggestions.size());
        }
    }

    public static void main(String[] args) {
        WebDriver driver = new ChromeDriver();
        try {
            selectNthSuggestion(driver, "infosys technologies", 3); // Select the 3rd option
        } finally {
            driver.quit();
        }
    }
}
```

### 3. what is super keyword in java
The `super` keyword in Java is used to refer to the **parent class (superclass) object**.
-   **Calling parent constructor:** `super()` can be used to invoke the immediate parent class's constructor from a subclass constructor. This must be the first statement.
-   **Accessing parent members:** `super.methodName()` or `super.variableName` can be used to call a method or access a field of the parent class, especially if it's been overridden or shadowed in the child class.

### 4. what is inheritance
Inheritance is an OOP concept where one class (the child/subclass) acquires the properties (fields) and behaviors (methods) of another class (the parent/superclass). It promotes code reuse and establishes an "is-a" relationship. Keyword: `extends`.

### 5. what is getters and setters in java
-   **Getters (Accessor Methods):** `public` methods used to retrieve the value of a `private` instance variable. (e.g., `public String getName() { return name; }`).
-   **Setters (Mutator Methods):** `public` methods used to update or set the value of a `private` instance variable. (e.g., `public void setName(String newName) { this.name = newName; }`).
They are a core part of **encapsulation**, providing controlled access to an object's internal state.

### 6. what are all the exceptions you have faced in your project
-   **Selenium Exceptions:** `NoSuchElementException`, `StaleElementReferenceException`, `TimeoutException`, `ElementNotInteractableException`.
-   **Java Exceptions:** `NullPointerException`, `IOException` (during file operations), `IllegalArgumentException`.

### 7. what are collections in java
The Java Collections Framework is a set of interfaces and classes in `java.util` package for storing and manipulating groups of objects. Key interfaces include `List` (ordered, allows duplicates), `Set` (unordered, unique), `Queue`, and `Map` (key-value pairs).

### 8. what is the difference between List and ArrayList?
-   **`List`:** An **interface** in the Java Collections Framework. It defines the contract for an ordered collection that allows duplicates.
-   **`ArrayList`:** A concrete **class** that `implements` the `List` interface. It's a resizable array implementation of the `List` interface, providing fast random access.

### 9. how to handle no stale element exception
This is a typo for **`StaleElementReferenceException`**.
-   **Solution:** Re-find the element just before interaction. The most robust way is to make sure your Page Object methods (or utility methods) perform `driver.findElement()` (or an explicit wait that re-locates) immediately before interacting with the element.

### 10. what do we use pom.xml
The `pom.xml` (Project Object Model) is the core configuration file for **Maven** projects. It defines:
-   **Dependencies:** All external libraries (e.g., Selenium, TestNG) required by the project.
-   **Build Configuration:** How the project is built, including plugins and build phases.
-   **Project Metadata:** Basic information about the project.

### 11. why should we give dependencies , what does it do
"Dependencies are external libraries (JAR files) that our project needs to function. We 'give' them in `pom.xml` so that Maven can automatically download, manage, and add them to our project's classpath. This avoids manually downloading JARs, resolves version conflicts, and ensures that our project builds consistently."

### 12. what is action class
Selenium's `Actions` class is used to perform complex user gestures that cannot be done with simple `click()` or `sendKeys()`, such as mouse hovers (`moveToElement`), drag-and-drop (`dragAndDrop`), right-clicks (`contextClick`), and double-clicks (`doubleClick`).

### 13. suppose if i have 2 tabs, and i have to go to second tab and do actions , how to do it ?
You use window handles.
1.  Get all window handles: `Set<String> allHandles = driver.getWindowHandles();`
2.  Convert the `Set` to an `ArrayList` to access by index: `List<String> handlesList = new ArrayList<>(allHandles);`
3.  Switch to the second tab (index 1): `driver.switchTo().window(handlesList.get(1));`
4.  Perform actions.

### 14. how do you handle multiple windows, write code for it and explain
(Duplicate of previous question). Explained with `getWindowHandles()` and `switchTo().window()`.

### 15. you said you worked in ajile methodologies, what is velocity
**Velocity** is a metric used in Agile (Scrum) to measure the amount of work (typically in story points) a development team can complete in a single sprint. It's calculated by summing the story points of all completed (and accepted) user stories in a sprint.
-   **Purpose:** Helps the team forecast how much work they can take on in future sprints.
-   **Not a Performance Metric:** It's a planning tool for the team, not a way to compare teams or individuals.

### 16. how many manual testcases you write in a week
"It varies based on the sprint. If it's a new feature, I might write anywhere from 5-15 detailed manual test cases in a week. If we're focusing heavily on automation, the number might be lower. My priority is quality over quantity, ensuring each test case adds value."

### 17. how many testcases you will automate
"Again, it varies. My goal is to automate all high-priority, repetitive, and stable test cases that are part of our regression suite. For a typical sprint, I usually automate 5-10 new test cases. Our overall automation goal is to keep our automated regression suite around 80-90% coverage for critical business paths."

### 18. what is the industry standard for test cases and its automation ?
There's no single "industry standard" as it varies greatly by context. However, general best practices suggest:
-   **Test Case Design:** Prioritize well-defined, atomic test cases that are unambiguous.
-   **Automation First:** Automate as much as possible, especially for regression, unit, and API tests. Aim for a high percentage of automation (e.g., 70-90% for regression).
-   **Testing Pyramid:** Focus on a large number of fast, cheap unit tests, fewer integration tests, and even fewer, well-chosen UI end-to-end tests.
-   **Continuous Testing:** Integrate tests into CI/CD pipelines to get fast feedback.
-   **Risk-Based Automation:** Prioritize automation based on business criticality and risk.
-   **Manual Testing:** Retain manual/exploratory testing for new features, usability, and complex scenarios that are hard to automate effectively.
