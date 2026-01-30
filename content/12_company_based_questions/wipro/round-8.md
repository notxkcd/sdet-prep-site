---
title: "Wipro-8"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

Wipro level 1
-------------- 
coding Test

1)Write a program for Word occurance 
2)  remove duplicates using arrays functions

Level 2
1) write a feature file for login page validation 
2) write the step definition 
3) difference between strict and dry run
4) difference between scenario and  scenario outline 
5)data table concept in cucumber framework
6) a (1,2,3,a,b,c)
  Remove (a b c) and sum (1 2 3) this numbers
7)Write syntex for  handling the dropdowns 
8) how will you do mouse operations and write a syntex 
9) Web table 
10) oops concepts in real project
11) difference between interface and abstract
12) what are the jnfaces used in the project
13) final and finally -explain
14)rest assured explain
15) how you will validate the status code write the code

---

## Answers (No-BS Java QA / SDET Explanations)

### Coding Test

#### 1)Write a program for Word occurance
Use a `HashMap` to store word counts.

```java
import java.util.HashMap;
import java.util.Map;

public class WordCounter {
    public static Map<String, Integer> countWordOccurrences(String sentence) {
        Map<String, Integer> wordCounts = new HashMap<>();
        if (sentence == null || sentence.trim().isEmpty()) {
            return wordCounts;
        }

        // Split the sentence into words, convert to lowercase for case-insensitivity
        String[] words = sentence.toLowerCase().split("\\s+|\\\p{Punct}"); // Split by space or punctuation

        for (String word : words) {
            if (!word.isEmpty()) { // Avoid empty strings from multiple delimiters
                wordCounts.put(word, wordCounts.getOrDefault(word, 0) + 1);
            }
        }
        return wordCounts;
    }

    public static void main(String[] args) {
        String text = "Hello world, hello Java. Java is great!";
        Map<String, Integer> occurrences = countWordOccurrences(text);
        occurrences.forEach((word, count) -> System.out.println(word + ": " + count));
    }
}
```

#### 2) remove duplicates using arrays functions
To remove duplicates from an array of integers, you can use Java 8 Streams `distinct()` method or convert to a `Set`.

```java
import java.util.Arrays;
import java.util.LinkedHashSet;
import java.util.Set;

public class DuplicateRemover {
    public static int[] removeDuplicates(int[] arr) {
        return Arrays.stream(arr).distinct().toArray();
    }

    public static Integer[] removeDuplicatesUsingSet(int[] arr) {
        Set<Integer> uniqueSet = new LinkedHashSet<>(); // Keeps order
        for (int num : arr) {
            uniqueSet.add(num);
        }
        return uniqueSet.toArray(new Integer[0]);
    }
}
```

### Level 2

#### 1) write a feature file for login page validation
```gherkin
Feature: User Login Functionality

  Scenario: Successful login with valid credentials
    Given a user is on the login page
    When the user enters a valid username and password
    And clicks the "Login" button
    Then the user should be redirected to the dashboard

  Scenario Outline: Unsuccessful login with invalid credentials
    Given a user is on the login page
    When the user attempts to log in with "<username>" and "<password>"
    And clicks the "Login" button
    Then an error message "<error_message>" should be displayed

    Examples:
      | username       | password     | error_message               |
      | "invalid_user" | "wrong_pass" | "Invalid username or password" |
      | "valid_user"   | ""           | "Password cannot be empty"  |
```

#### 2) write the step definition
For the "Successful login" scenario:
```java
import io.cucumber.java.en.Given;
import io.cucumber.java.en.When;
import io.cucumber.java.en.And;
import io.cucumber.java.en.Then;
// Assuming LoginPage and DashboardPage are Page Objects
// import com.myproject.pages.LoginPage;
// import com.myproject.pages.DashboardPage;

public class LoginSteps {
    // private WebDriver driver; // Assuming driver is managed by hooks
    // private LoginPage loginPage;
    // private DashboardPage dashboardPage;

    @Given("a user is on the login page")
    public void aUserIsOnTheLoginPage() {
        // driver.get("http://your-app/login");
        // loginPage = new LoginPage(driver);
    }

    @When("the user enters a valid username and password")
    public void theUserEntersValidCredentials() {
        // loginPage.enterUsername("testuser");
        // loginPage.enterPassword("password123");
    }

    @And("clicks the {string} button")
    public void clicksTheButton(String buttonName) {
        // if (buttonName.equals("Login")) loginPage.clickLoginButton();
    }

    @Then("the user should be redirected to the dashboard")
    public void theUserShouldBeRedirectedToTheDashboard() {
        // Assert.assertTrue(dashboardPage.isDashboardDisplayed(), "Dashboard not displayed");
    }
}
```

#### 3) difference between strict and dry run
-   **`strict = true` (Cucumber option):** Cucumber will fail the test run if it finds any undefined or pending steps. This ensures all your Gherkin steps have corresponding code.
-   **`dryRun = true` (Cucumber option):** Cucumber will only perform a step definition scan and generate snippets for any undefined steps. It will **not execute** any actual code or tests. It's used to quickly verify that all Gherkin steps have corresponding step definitions without running the actual (potentially slow) tests.

#### 4) difference between scenario and scenario outline
-   **`Scenario`:** A single, concrete test case that executes once.
-   **`Scenario Outline`:** A template for a scenario that runs multiple times with different sets of data, defined in an `Examples` table. Used for data-driven testing.

#### 5) data table concept in cucumber framework
A `DataTable` is used in Cucumber to pass multiple values to a step definition in a structured way (like a table).
```gherkin
When I add the following items to the cart:
  | product | quantity |
  | Laptop  | 1        |
  | Mouse   | 2        |
```
The step definition receives this as `io.cucumber.datatable.DataTable`, which can then be converted to `List<Map<String, String>>` or `List<List<String>>` for easy processing.

#### 6) a (1,2,3,a,b,c) Remove (a b c) and sum (1 2 3) this numbers
This requires iterating through a mixed-type list/array, separating numbers from letters, summing numbers, and then presenting the sum.

```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class NumberAndLetterProcessor {
    public static void process(Object[] mixedArray) {
        List<String> letters = new ArrayList<>();
        int sum = 0;

        for (Object item : mixedArray) {
            if (item instanceof Integer) {
                sum += (Integer) item;
            } else if (item instanceof String) {
                letters.add((String) item);
            }
        }
        System.out.println("Removed letters: " + letters);
        System.out.println("Sum of numbers: " + sum);
    }

    public static void main(String[] args) {
        Object[] data = {1, 2, 3, "a", "b", "c"};
        process(data); // Output: Removed letters: [a, b, c], Sum of numbers: 6
    }
}
```

#### 7)Write syntex for handling the dropdowns
For HTML `<select>` elements, use the `Select` class:
```java
import org.openqa.selenium.support.ui.Select;
// ...
WebElement dropdownElement = driver.findElement(By.id("myDropdown"));
Select select = new Select(dropdownElement);
select.selectByVisibleText("Option Text"); // Or selectByValue("value"), selectByIndex(index)
```

#### 8) how will you do mouse operations and write a syntex
You use the `Actions` class for complex mouse operations.
```java
import org.openqa.selenium.interactions.Actions;
// ...
Actions actions = new Actions(driver);
WebElement elementToHover = driver.findElement(By.id("menu"));
actions.moveToElement(elementToHover).perform(); // Mouse hover

WebElement targetElement = driver.findElement(By.id("item"));
actions.contextClick(targetElement).perform(); // Right-click

actions.doubleClick(targetElement).perform(); // Double-click
```

#### 9) Web table
Handling web tables usually involves:
1.  Locating the `<table>` element.
2.  Getting all `<tr>` (row) elements.
3.  Looping through `<tr>`s to get `<td>` (data cell) or `<th>` (header cell) elements.
4.  Extracting text or interacting with elements within cells.
Often requires dynamic XPath to locate specific cells based on content.

#### 10) oops concepts in real project
-   **Encapsulation:** Page Object Model (`private` locators, `public` methods).
-   **Abstraction:** `WebDriver` interface, custom interfaces for services.
-   **Inheritance:** `BaseTest` and `BasePage` classes.
-   **Polymorphism:** Method overriding in page objects, overloading in utility classes.

#### 11) difference between interface and abstract
-   **Interface:** Defines a contract. Can only have abstract methods (pre-Java 8), can't have instance variables (only static final). A class can implement multiple interfaces.
-   **Abstract Class:** Can have both abstract and concrete methods. Can have instance variables and constructors. A class can extend only one abstract class.

#### 12) what are the jnfaces used in the project
This is likely a typo for "interfaces".
"In our project, we use core Selenium interfaces like `WebDriver`, `WebElement`, `TakesScreenshot`, and `JavascriptExecutor`. We also define our own custom interfaces for certain services, like `IConfigReader` for reading configuration from different sources (e.g., JSON, properties file)."

#### 13) final and finally -explain
-   **`final` (keyword):** Makes a variable constant, a method non-overridable, or a class non-extendable.
-   **`finally` (block):** Part of a `try-catch` statement, always executes. Used for resource cleanup.

#### 14)rest assured explain
(Duplicate of previous questions). A Java DSL for testing RESTful web services, providing a fluent BDD-style API for building and validating requests.

#### 15) how you will validate the status code write the code
In REST-assured, using the `.then()` part of the fluent API:
```java
import static io.restassured.RestAssured.*;
import static org.hamcrest.Matchers.*;

public void validateStatusCode() {
    given()
        .when()
        .get("https://api.example.com/users")
        .then()
        .statusCode(200); // Assert HTTP 200 OK status code
        // .statusCode(equalTo(200)); // Using Hamcrest matcher
}
```
