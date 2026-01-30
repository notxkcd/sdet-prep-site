---
title: "Cognizant"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

Cognizant
Round 1:
1) tell me about yourself
2) find max and min numbers in array
3) get key value from hasmap
4) inspect an element from Flipkart and write xpath
5) method overloading and method overriding
6) super and this keyword
7) Select a link from drop-down, navigate to new tab, enter username and password in new tab, click on submit button. The page will navigate to the base window again. Write scripting for this
8) explain about cucumber project
9) difference between scenario and scenario outline
10) annotations order in testNG
11) how will u rerun a failed test case again and again in testNg
12) how will execution be performed in cucumber framework
13) write syntax for runner class
14) what is monochrome
15) How will u handle stale element exception
16) how will u handle element not interactable exception

Round 2:
1) explain severity and priority with an example
2) explain low priority high severity and high priority low severity example
3) find the duplicate characters count
4) explain about your project
5) explain about your day to day activities
6) what are the oops concepts in Java. And what are the areas it is implemented in selenium
7) explain about sprint activities
8) explain about cucumber framework
9) what are the Maven life cycles. Explain
10) about actions class.

---

## Answers (No-BS Java QA / SDET Explanations)

### Round 1

#### 1) tell me about yourself
Standard. Role, responsibilities, tech stack, achievement. Keep it under 90 seconds.

#### 2) find max and min numbers in array
Classic coding filter.

```java
import java.util.Arrays;

public class ArrayMinMax {
    public static void findMinAndMax(int[] arr) {
        if (arr == null || arr.length == 0) {
            System.out.println("Array is empty or null.");
            return;
        }

        // The Java 8 Streams way. It's clean and declarative.
        int min = Arrays.stream(arr).min().getAsInt();
        int max = Arrays.stream(arr).max().getAsInt();

        System.out.println("Min: " + min + ", Max: " + max);

        // The old-school loop way. Also fine, but shows less modern knowledge.
        int minLoop = arr[0];
        int maxLoop = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < minLoop) {
                minLoop = arr[i];
            }
            if (arr[i] > maxLoop) {
                maxLoop = arr[i];
            }
        }
        System.out.println("Min (loop): " + minLoop + ", Max (loop): " + maxLoop);
    }
}
```

#### 3) get key value from hasmap
This is poorly phrased. You use a key to get a value.

```java
import java.util.HashMap;
import java.util.Map;

public class HashMapRetrieve {
    public static void main(String[] args) {
        Map<String, String> config = new HashMap<>();
        config.put("browser", "chrome");
        config.put("baseUrl", "http://example.com");

        // Use the key "browser" to get the value "chrome"
        String browserValue = config.get("browser");

        System.out.println("The value for key 'browser' is: " + browserValue);
    }
}
```

#### 4) inspect an element from Flipkart and write xpath
This is a practical test of your core skill. They want to see if you can write a robust, non-brittle XPath. Let's say we want to find the main search input bar on Flipkart.

1.  **Inspect:** Right-click the search bar, choose "Inspect".
2.  **Analyze:** You see something like `<input type="text" class="_3704LK" title="Search for products, brands and more" name="q" ...>`
3.  **Formulate XPath:**
    *   **Bad XPath:** `/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input`. This is absolute and will break instantly.
    *   **Okay XPath:** `//input[@name='q']`. Uses the `name` attribute. Pretty good.
    *   **Better XPath:** `//input[@title='Search for products, brands and more']`. Using the `title` is also good as it's descriptive.
    *   **Robust XPath:** `//form//input[@name='q' and @type='text']`. This is more specific. It finds an input with `name='q'` inside a form.

The answer isn't just the XPath; it's explaining *why* you chose it: "I'd use `//input[@name='q']` because the `name` attribute is likely to be stable and is directly related to the element's function on the form."

#### 5) method overloading and method overriding
-   **Overloading:** Same method name, different parameters (number or type). Happens in the same class. It's resolved at compile-time.
-   **Overriding:** Same method name, same parameters. Happens in a parent-child class relationship. The child class provides a specific implementation. It's resolved at runtime. The `@Override` annotation should be used.

#### 6) super and this keyword
-   `this`: Refers to the **current object instance**. Used to call other constructors or to differentiate instance variables from local variables.
-   `super`: Refers to the **parent class object**. Used to call the parent's constructor (`super()`) or methods (`super.myMethod()`).

#### 7) Select a link from drop-down, navigate to new tab...
This combines three skills: `Select` class, window handling, and basic navigation.

```java
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.ui.Select;
import java.util.Set;

public void dropdownAndNewTabWorkflow(WebDriver driver) {
    String originalTab = driver.getWindowHandle();

    // 1. Select from dropdown (assuming the value is the URL)
    Select dropdown = new Select(driver.findElement(By.id("my-dropdown")));
    dropdown.selectByValue("http://some-new-tab-url.com"); // Let's assume this action opens a new tab

    // A more realistic scenario is clicking a link that opens a new tab
    // driver.findElement(By.id("link-that-opens-new-tab")).click();

    // 2. Wait for and switch to the new tab
    Set<String> allTabs = driver.getWindowHandles();
    allTabs.remove(originalTab);
    String newTab = allTabs.iterator().next();
    driver.switchTo().window(newTab);

    // 3. Interact with the new tab
    driver.findElement(By.id("username")).sendKeys("user");
    driver.findElement(By.id("password")).sendKeys("pass");
    driver.findElement(By.id("submit")).click();

    // 4. The scenario says the page navigates back to the base window.
    // This is weird. A child tab can't force the focus back to the parent.
    // It more likely means the test logic should switch back.
    driver.switchTo().window(originalTab);
    
    // Now you are back in the context of the original tab.
    System.out.println("Back on the original tab: " + driver.getTitle());
}

```

#### 8) explain about cucumber project
A Cucumber project is structured to separate behavior from implementation.
-   **`src/test/resources/features`**: This directory holds the `.feature` files written in Gherkin (`Given/When/Then`). This is the human-readable part.
-   **`src/test/java/com/myapp/stepdefinitions`**: This package holds the "glue code" – Java classes with methods annotated with `@Given`, `@When`, `@Then` that implement the steps from the feature files.
-   **`src/test/java/com/myapp/runners`**: This package holds the test runner class. This class is annotated with `@RunWith(Cucumber.class)` and `@CucumberOptions`, which configure where to find feature files, step definitions (glue), plugins for reporting, and which tags to run.

#### 9) difference between scenario and scenario outline
-   **`Scenario`:** A single, concrete test case. It runs once.
    ```gherkin
    Scenario: Successful login
      Given I am on the login page
      When I enter "valid_user" and "valid_pass"
      Then I should be on the dashboard
    ```
-   **`Scenario Outline`:** A template for running the same scenario multiple times with different data. It uses `<placeholders>` and an `Examples` table. It's Cucumber's way of doing data-driven testing.
    ```gherkin
    Scenario Outline: Invalid login attempts
      Given I am on the login page
      When I enter "<username>" and "<password>"
      Then I should see an "<error_message>"
    
    Examples:
      | username      | password      | error_message          |
      | "invalid_user"| "wrong_pass"  | "Invalid credentials." |
      | "valid_user"  | ""            | "Password is required."|
    ```

#### 10) annotations order in testNG
TestNG annotations have a strict execution order.
1.  `@BeforeSuite`
2.  `@BeforeTest`
3.  `@BeforeClass`
4.  `@BeforeMethod`
5.  `@Test`
6.  `@AfterMethod`
7.  `@AfterClass`
8.  `@AfterTest`
9.  `@AfterSuite`

`@DataProvider` methods are run before the tests that depend on them.

#### 11) how will u rerun a failed test case again and again in testNg
There are two main ways:

1.  **Automatically via a Listener (Best approach):** You create a class that implements the `IRetryAnalyzer` interface. In its `retry` method, you define the logic (e.g., "retry up to 2 times"). Then, you create another class that implements `IAnnotationTransformer` and in its `transform` method, you tell TestNG to use your retry analyzer for all tests. You register this transformer in your `testng.xml`. This automatically applies the retry logic to all tests without changing the test code.

2.  **Manually after a run:** After a TestNG run, it creates a file called `testng-failed.xml` in the output directory. This XML file contains only the tests that failed. You can then run this file directly (`mvn test -Dsurefire.suiteXmlFiles=target/surefire-reports/testng-failed.xml`) to re-run only the failures.

#### 12) how will execution be performed in cucumber framework
1.  The **Test Runner** (`@RunWith(Cucumber.class)`) is executed by JUnit or TestNG.
2.  The runner reads the `@CucumberOptions`.
3.  It finds the `.feature` files specified.
4.  For each scenario, it parses the Gherkin steps (`Given`, `When`, `Then`).
5.  For each step, it looks in the `glue` path for a Java method with a matching annotation (e.g., `@When("I enter {string}")`).
6.  It executes the Java method, passing in any parameters from the step.
7.  After the run, it generates reports based on the `plugin` options.

#### 13) write syntax for runner class
```java
import io.cucumber.junit.Cucumber;
import io.cucumber.junit.CucumberOptions;
import org.junit.runner.RunWith;

@RunWith(Cucumber.class)
@CucumberOptions(
    features = "src/test/resources/features",
    glue = "com.myapp.stepdefinitions",
    plugin = {"pretty", "html:target/cucumber-reports.html"},
    tags = "@smoke and not @wip"
)
public class TestRunner {
    // This class body is usually empty.
    // The configuration is all in the annotations.
}
```

#### 14) what is monochrome
In `@CucumberOptions`, `monochrome = true` tells Cucumber to make the console output more readable, especially on Windows systems where colored console output might not display correctly. It prints the output in a clean, black-and-white format.

#### 15) How will u handle stale element exception
`StaleElementReferenceException` means your reference to a `WebElement` is no longer valid because the DOM has changed.

**The only real solution is to re-find the element.**

-   **Bad:** Using a `try-catch` block to retry the interaction. This is a band-aid that hides the real problem.
-   **Good:** Structure your code (especially in Page Objects) so that `driver.findElement()` is called right before the interaction. Don't store `WebElement`s in instance variables for long periods.
-   **Best:** Use explicit waits. A well-written explicit wait for an element to be `clickable` or `visible` will naturally handle staleness because it re-fetches the element on each polling attempt.

#### 16) how will u handle element not interactable exception
`ElementNotInteractableException` means the element is in the DOM, but a user couldn't interact with it.
1.  **Wait for it to be interactable:** The most common cause is a timing issue. The element is present but disabled or covered by an overlay. The fix is an explicit wait: `wait.until(ExpectedConditions.elementToBeClickable(locator));`
2.  **Scroll to it:** The element might be off-screen. Use `JavascriptExecutor` to scroll it into view before clicking. `js.executeScript("arguments[0].scrollIntoView(true);", element);`
3.  **Use JavaScript click:** If another element is covering it (like a cookie banner), and you can't get rid of the overlay, you can bypass the Selenium interaction check and force a click with JavaScript. This is a last resort. `js.executeScript("arguments[0].click();", element);`

### Round 2

#### 1) explain severity and priority with an example
-   **Severity:** The technical impact of the bug on the system. (Set by QA)
-   **Priority:** The business urgency of fixing the bug. (Set by Product Owner/Manager)

**Example:** A typo of the company's name in the footer of the website.
-   **Severity:** Trivial. It doesn't break any functionality.
-   **Priority:** High. It's a major embarrassment to the brand and must be fixed immediately.

#### 2) explain low priority high severity and high priority low severity example
-   **High Priority, Low Severity:** The typo example from above. A spelling mistake on the homepage. Doesn't break anything (low severity), but needs to be fixed NOW (high priority).
-   **Low Priority, High Severity:** A crash that happens under very rare and obscure conditions. For example, if a user with a 1000-character-long name goes to a specific settings page and clicks three buttons in a specific order, the server crashes. It's a critical crash (high severity), but it affects almost no one and is hard to reproduce, so it's not urgent to fix (low priority).

#### 3) find the duplicate characters count
This means finding the frequency of each character, and then identifying which ones appear more than once. A `Map` is perfect for this.

```java
import java.util.HashMap;
import java.util.Map;

public class DuplicateCharCounter {
    public static void countDuplicateChars(String str) {
        Map<Character, Integer> charCountMap = new HashMap<>();
        for (char c : str.toCharArray()) {
            charCountMap.put(c, charCountMap.getOrDefault(c, 0) + 1);
        }

        System.out.println("Duplicate character counts:");
        for (Map.Entry<Character, Integer> entry : charCountMap.entrySet()) {
            if (entry.getValue() > 1) {
                System.out.println("'" + entry.getKey() + "': " + entry.getValue());
            }
        }
    }
}
```

#### 4) explain about your project
Standard.

#### 5) explain about your day to day activities
Standard. Mention daily standup, test design, automation, execution, bug reporting, and collaboration.

#### 6) what are the oops concepts in Java. And what are the areas it is implemented in selenium
The concepts are Encapsulation, Abstraction, Inheritance, and Polymorphism.

**Where they are implemented in Selenium:**
-   **Abstraction:** `WebDriver` is an interface. `SearchContext` is an interface. You code against these abstractions without needing to know the details of `ChromeDriver` or `RemoteWebElement`.
-   **Encapsulation:** The entire Page Object Model is an application of encapsulation. A `LoginPage` object hides its locators and the implementation of how it clicks buttons.
-   **Inheritance:** You use this in your framework. A `BaseTest` class is extended by all your test classes. A `BasePage` is extended by all page objects.
-   **Polymorphism:** `WebDriver driver = new ChromeDriver();` is an example of polymorphism. A parent class reference (`WebDriver`) is holding a child class object (`ChromeDriver`). Also, method overriding in your page objects (`verifyPageLoad()`).

#### 7) explain about sprint activities
A typical Scrum sprint involves several "ceremonies" or activities:
-   **Sprint Planning:** At the start, the team selects items from the backlog to work on during the sprint.
-   **Daily Stand-up:** A short daily meeting to sync on progress ("what I did yesterday, what I'll do today, any blockers").
-   **Backlog Grooming/Refinement:** A meeting during the sprint to review and clarify upcoming backlog items.
-   **Sprint Review:** At the end of the sprint, the team demonstrates the completed work to stakeholders. This is a demo.
-   **Sprint Retrospective:** Also at the end, the team privately discusses what went well, what went wrong, and what to improve in the next sprint.

#### 8) explain about cucumber framework
Answered in Round 1. It's a BDD framework that uses Gherkin (`.feature` files) to write human-readable tests, which are then linked to Java "glue code" (step definitions).

#### 9) what are the Maven life cycles. Explain
Maven has three built-in build lifecycles. Each lifecycle is made up of a sequence of phases.

1.  **`default` (The main one):** Handles project build and deployment. Its key phases are:
    -   `validate`: validate the project is correct and all necessary information is available.
    -   `compile`: compile the source code.
    -   `test`: run the tests using a suitable unit testing framework (like TestNG). **This is the phase automation engineers care about most.**
    -   `package`: take the compiled code and package it in its distributable format, such as a JAR.
    -   `install`: install the package into the local repository, for use as a dependency in other local projects.
    -   `deploy`: copies the final package to the remote repository for sharing with other developers and projects.
2.  **`clean`:** Cleans up artifacts created by prior builds. Its one phase is `clean` (deletes the `target` directory).
3.  **`site`:** Generates project site documentation. Its key phase is `site`.

When you run a command like `mvn install`, Maven runs all the phases in the `default` lifecycle up to and including `install`.

#### 10) about actions class.
It's the `Actions` class. It's used for emulating complex user gestures that aren't a simple click/type.
-   `moveToElement()` (hover)
-   `contextClick()` (right-click)
-   `doubleClick()`
-   `dragAndDrop()`
-   You build a chain of commands and then execute them with `.perform()`.

---

## Original Questions (UNTOUCHED)

- Cognizant round1

1. Tell about yourself and your roles and responsibities.
2. how will you validate the dropdown options in selenium. write code
3. Given a link https://www.countries-ofthe-world.com/capitals-of-the-world.html. In this write xpath for in such a way, If I give Afghanistan in xpath it should get its capital Kabul. if Albania is given, it should return Tirana and so on.
4. how will you find out second highest number in an array
5. explain bug life cycle
6. how will set up a pipeline in Jenkins
7. If a developer say the bug you raised is not actually a bug. what will you do?
8. write the order of output for below.
- @Test (priority= 0)
- public void test(){
- System.out.println("a")
}

- @Test (priority= 1)
- public void test1(){
- System.out.println("b")
}

@Test
- public void test2(){
- System.out.println("c")
}

@BeforeClass
- public void test2(){
- System.out.println("BeforeClass")
}

@BeforeTest
- public void test2(){
- System.out.println("BeforeTest")
}

9. Have you worked in API?
10. what is difference between POST and PUT methods?
11. What is 201 response code?
12. Have you worked in Agile?
13. What are Aglie Ceremonies?
14. What is been discussed in Retrospective meeting?
15. What is runner class?
16. what are the challenges you faced in automation project?
17. what are the selenium exceptions you faced in your project?
18. What is Scenario and Scenario outline in cucumber
19. What is background
20. In which area you want to improve yourself in next 1 year

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. Tell about yourself and your roles and responsibities.
Standard.

### 2. how will you validate the dropdown options in selenium. write code
You use the `Select` class and its `getOptions()` method.

```java
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.Select;
import java.util.List;
import java.util.stream.Collectors;

public void validateDropdownOptions(WebDriver driver) {
    Select dropdown = new Select(driver.findElement(By.id("country-dropdown")));
    
    // Get all <option> elements
    List<WebElement> allOptions = dropdown.getOptions();
    
    // Convert them to a list of strings
    List<String> allOptionTexts = allOptions.stream()
                                            .map(WebElement::getText)
                                            .collect(Collectors.toList());

    // Now you can perform assertions
    // For example, check if a specific country exists
    assert allOptionTexts.contains("France");
    
    // Or check the total number of options
    assert allOptionTexts.size() == 195; 
}
```

### 3. Given a link ... write xpath for in such a way, If I give Afghanistan in xpath it should get its capital Kabul.
This is a classic "find a related element" XPath question. You need to find an element based on its text, then navigate to another element relative to it.

Let's assume the HTML structure is something like this:
```html
<div class="row">
  <div class="country">Afghanistan</div>
  <div class="capital">Kabul</div>
</div>
<div class="row">
  <div class="country">Albania</div>
  <div class="capital">Tirana</div>
</div>
```

**The XPath:** You find the `div` with the country's text, then use the `following-sibling` axis to find the capital `div`.

`//div[text()='Afghanistan']/following-sibling::div`

If the structure is a table:
```html
<tr>
  <td>Afghanistan</td>
  <td>Kabul</td>
</tr>
```
**The XPath:**
`//td[text()='Afghanistan']/following-sibling::td`

The key is to use `text()` to find the known element and then use an axis (`following-sibling`, `parent`, `ancestor`) to navigate to the unknown element.

### 4. how will you find out second highest number in an array
A common coding question.
1.  Remove duplicates.
2.  Sort the array.
3.  The second-to-last element is your answer.

```java
import java.util.Arrays;
import java.util.Comparator;

public class SecondHighest {
    public static int findSecondHighest(int[] arr) {
        return Arrays.stream(arr)
                     .distinct() // Remove duplicates
                     .boxed()    // Convert from IntStream to Stream<Integer>
                     .sorted(Comparator.reverseOrder()) // Sort in descending order
                     .skip(1)    // Skip the highest element
                     .findFirst()// Get the next one (which is the second highest)
                     .orElseThrow(() -> new IllegalStateException("Array has fewer than 2 unique elements"));
    }
}
```

### 5. explain bug life cycle
A bug goes through a series of states from creation to closure.
1.  **New:** A bug is reported for the first time.
2.  **Open/Assigned:** The bug is reviewed and assigned to a developer.
3.  **In Progress/Fixed:** The developer is actively working on a fix. When done, they mark it as "Fixed."
4.  **Ready for QA/Verification:** The fix has been deployed to a test environment, and it's ready for the QA team to verify.
5.  **Reopened:** If the QA team finds that the fix doesn't work, they reopen the bug and assign it back to the developer.
6.  **Closed:** If the QA team confirms the fix works, they close the bug.
7.  **Rejected/Deferred:** A bug might be rejected if it's not a real bug, or deferred if it's low priority and will be fixed in a later release.

### 6. how will set up a pipeline in Jenkins
You use a `Jenkinsfile`.
1.  Create a `Jenkinsfile` in the root of your Git repository.
2.  Inside the `Jenkinsfile`, define your pipeline using declarative syntax (`pipeline { ... }`).
3.  Define **stages** for your pipeline (e.g., "Build", "Test", "Deploy").
4.  In the "Test" stage, you'd have a step to run your test suite, e.g., `sh 'mvn clean test'`.
5.  In Jenkins, create a "Pipeline" or "Multibranch Pipeline" job and point it to your Git repository. Jenkins will automatically find and execute the `Jenkinsfile`.

### 7. If a developer say the bug you raised is not actually a bug. what will you do?
This is a test of your communication and collaboration skills.
1.  **Don't argue.** First, understand their perspective.
2.  **Review the requirement:** Go back to the user story or requirement document. Is the expected behavior clearly defined? Maybe there's a misunderstanding of the requirement on either your side or the developer's.
3.  **Reproduce together:** Ask the developer to join you for a quick call. Reproduce the issue on your screen so they can see exactly what you're doing. Often, the issue is related to environment, data, or specific steps that the developer didn't follow.
4.  **Involve the Product Owner:** If there's still disagreement and it's about how the feature *should* work, then the Product Owner is the tie-breaker. They own the requirements.
5.  **If it's a UX issue:** Sometimes a feature works as coded but provides a terrible user experience. Frame your argument from the user's point of view.

### 8. write the order of output for below.
This tests knowledge of TestNG annotation order and default priority.
- There are two methods named `test2`, which is a compile error. Assuming they have different names (e.g., `beforeClass`, `beforeTest`, `testC`).
- `@Test` methods without a priority run after priority 0, and by default have `priority=0`. When priorities are the same, they run in alphabetical order. So `test2()` (c) runs after `test()` (a) because 't' comes after 't' but 'e' comes after 'e' but 's' comes after 's' but 't' comes after 't' - alphabetical order of method names. NO, that's not how it works. Let's assume default priority is 0, so test() and test2() are both priority 0. `test1()` is priority 1. Order between same-priority tests is not guaranteed, but often alphabetical. `test2()` would likely run after `test()`. `test1()` runs last.

Correcting the broken code:
```java
@Test(priority=0) public void testA(){ System.out.println("a"); }
@Test(priority=1) public void testB(){ System.out.println("b"); }
@Test public void testC(){ System.out.println("c"); } // Default priority = 0
@BeforeClass public void beforeClass(){ System.out.println("BeforeClass"); }
@BeforeTest public void beforeTest(){ System.out.println("BeforeTest"); }
```

**Correct Execution Order:**
1.  `@BeforeTest`
2.  `@BeforeClass`
3.  `@Test` with priority 0 (`testA`) and default priority 0 (`testC`). The order between these two is not guaranteed, but often alphabetical by method name. So `testA` then `testC`.
4.  `@Test` with priority 1 (`testB`).

**Output:**
```
BeforeTest
BeforeClass
a
c
b
```

### 9. Have you worked in API?
Yes. "I have experience testing REST APIs using REST-assured with Java. I'm responsible for writing automated tests to verify CRUD operations, status codes, response bodies, and schema validation."

### 10. what is difference between POST and PUT methods?
-   **POST:** Creates a new subordinate resource. It is **not idempotent**. Calling it twice creates two resources.
-   **PUT:** Replaces a resource at a known URL. It **is idempotent**. Calling it twice with the same data has the same effect as calling it once. You must send the *entire* resource representation.

### 11. What is 201 response code?
`201 Created`. A new resource has been successfully created as a result of a `POST` request. The response usually includes a `Location` header pointing to the URL of the new resource.

### 12. Have you worked in Agile?
Yes. "My team follows the Scrum methodology, with two-week sprints."

### 13. What are Aglie Ceremonies?
Sprint Planning, Daily Stand-up, Sprint Review, Sprint Retrospective.

### 14. What is been discussed in Retrospective meeting?
It's a process improvement meeting for the team. You discuss three things:
1.  What went well? (Things to continue doing)
2.  What went wrong? (Things to stop doing)
3.  What should we try to improve? (Action items for the next sprint)

### 15. What is runner class?
The test runner class is the entry point for executing Cucumber tests. It's a JUnit or TestNG class that is annotated with `@CucumberOptions` to configure the test run.

### 16. what are the challenges you faced in automation project?
Have examples ready: flaky tests due to timing issues, unstable locators from dynamic UI, and test data management.

### 17. what are the selenium exceptions you faced in your project?
`NoSuchElementException`, `StaleElementReferenceException`, `TimeoutException`, `ElementNotInteractableException`.

### 18. What is Scenario and Scenario outline in cucumber
-   `Scenario`: A single test case.
-   `Scenario Outline`: A data-driven test case template that runs multiple times using data from an `Examples` table.

### 19. What is background
In a Cucumber `.feature` file, the `Background` keyword is used to define a set of `Given` steps that run before **every scenario** in that feature file. It's used for setting up a common precondition.

### 20. In which area you want to improve yourself in next 1 year
Shows you have a career plan.
-   "I want to get deeper into performance testing with tools like JMeter or k6."
-   "I'm looking to expand my skills into security testing and learn about common vulnerabilities."
-   "I want to improve my DevOps skills by learning more about Docker and Kubernetes to better manage test environments."

---

## Original Questions (UNTOUCHED)

- Cognizant Interview Questions
- Tell About yourself ?
- What is Abstraction ?
- Can abstract method be final?
- Can abstract class contains final method ?
- What is immutable in java?
- Write program to find repeated characters present in a word "ASSASINATION";
- Write program to print if these two strings patterns are same - program should return "CAT" and "ACT" as same pattern as both contains same letters.
- Write program to find 3rd maximum element in given array.
- What is serialization in java?
- Explain about collection framework?
- Does map allows null values?
- how do you initialize HashMap ?
- Difference between explicit & fluent wait?
- when do you use explicit wait?
- what kind of exceptions you have faced in your project?
- what is stale element exception and how do you handle stale element exception?
- what is absolute and relative xpath?
- disadvantages of selenium?
- Write code to read data from table of specific row in a given webpage
- Explain about the cucumber framework?
- how do you pass data in cucumber?
- what are tags used in runner class?
- Write a feature file and step definition to login ecommerce website and add 5 products to cart & validate checkout page -
- pass values of five products using datatable and add to cart ?

---

## Answers (No-BS Java QA / SDET Explanations)

### Tell About yourself ?
Standard.

### What is Abstraction ?
Hiding implementation details and showing only functionality. In Java, it's achieved with `abstract` classes and `interfaces`. The `WebDriver` interface is the canonical example in test automation.

### Can abstract method be final?
No. An `abstract` method has no implementation and *must* be overridden by a subclass. A `final` method *cannot* be overridden. The two keywords are mutually exclusive. This would be a compiler error.

### Can abstract class contains final method ?
Yes. An abstract class can contain concrete (`final` or non-final) methods. If a method in an abstract class is marked `final`, it means that any concrete subclass can use that method as-is, but cannot override it.

### What is immutable in java?
An object is immutable if its state cannot be changed after it is created. `String` is the classic example. Any "modification" to a `String` object creates a new `String` object in memory. This makes them inherently thread-safe.

### Write program to find repeated characters present in a word "ASSASINATION"
This is a character frequency count. Use a `Map`.

```java
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;

public class CharacterFrequency {
    public static void findRepeatedChars(String str) {
        Map<Character, Long> freq = str.chars()
                                       .mapToObj(c -> (char) c)
                                       .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
        
        freq.forEach((character, count) -> {
            if (count > 1) {
                System.out.println("Character '" + character + "' repeats " + count + " times.");
            }
        });
    }
    public static void main(String[] args) {
        findRepeatedChars("ASSASINATION");
    }
}
```

### Write program to print if these two strings patterns are same - program should return "CAT" and "ACT" as same pattern as both contains same letters.
This means, "check if two strings are anagrams." The simplest way is to sort the character arrays of both strings and see if they are equal.

```java
import java.util.Arrays;

public class AnagramChecker {
    public static boolean areAnagrams(String s1, String s2) {
        if (s1 == null || s2 == null || s1.length() != s2.length()) {
            return false;
        }
        char[] arr1 = s1.toCharArray();
        char[] arr2 = s2.toCharArray();
        Arrays.sort(arr1);
        Arrays.sort(arr2);
        return Arrays.equals(arr1, arr2);
    }

    public static void main(String[] args) {
        System.out.println(areAnagrams("CAT", "ACT")); // true
        System.out.println(areAnagrams("DOG", "GOD")); // true
        System.out.println(areAnagrams("HELLO", "JELLO")); // false
    }
}
```

### Write program to find 3rd maximum element in given array.
Similar to finding the second highest. Sort, remove duplicates, and pick the third element.

```java
import java.util.Arrays;
import java.util.Comparator;

public class NthMaximum {
    public static int findNthMax(int[] arr, int n) {
        if (n <= 0) throw new IllegalArgumentException("N must be positive.");
        return Arrays.stream(arr)
                     .distinct()
                     .boxed()
                     .sorted(Comparator.reverseOrder())
                     .skip(n - 1)
                     .findFirst()
                     .orElseThrow(() -> new IllegalStateException("Array has fewer than " + n + " unique elements"));
    }
    
    public static void main(String[] args) {
        int[] nums = { 1, 5, 2, 8, 8, 3, 10, 10 };
        System.out.println("3rd max: " + findNthMax(nums, 3)); // 5
    }
}
```

### What is serialization in java?
Serialization is the process of converting a Java object's state into a byte stream. Deserialization is the reverse. It's used for:
-   **Persistence:** Saving an object to a file or database.
-   **Communication:** Sending an object over a network (e.g., in Remote Method Invocation - RMI).

A class must implement the `java.io.Serializable` marker interface to be serializable.

### Explain about collection framework?
The Java Collections Framework is a set of interfaces and classes for storing and manipulating groups of objects. Key interfaces are `List` (ordered, allows duplicates), `Set` (unordered, unique), `Queue` (for processing), and `Map` (key-value pairs).

### Does map allows null values?
-   `HashMap`: Allows **one `null` key** and **multiple `null` values**.
-   `TreeMap`: Does **not** allow `null` keys (it needs to call `compareTo` on them), but allows `null` values.
-   `Hashtable`: A legacy, synchronized version of HashMap. Does **not** allow `null` keys or `null` values.

### how do you initialize HashMap ?
```java
// Standard way
Map<String, Integer> map1 = new HashMap<>();
map1.put("one", 1);
map1.put("two", 2);

// Using Map.of() (Java 9+) for an immutable map
Map<String, Integer> map2 = Map.of("one", 1, "two", 2);

// Using double-brace initialization (an anti-pattern, avoid it)
Map<String, Integer> map3 = new HashMap<>() {{
    put("one", 1);
    put("two", 2);
}};
```

### Difference between explicit & fluent wait?
A `FluentWait` is a more configurable `ExplicitWait`.
-   **`ExplicitWait` (`WebDriverWait`):** A pre-configured `FluentWait`. It polls for a condition with a default polling interval (500ms) and ignores `NoSuchElementException` by default.
-   **`FluentWait`:** Gives you full control. You can configure:
    -   The maximum timeout.
    -   The polling interval (`pollingEvery()`).
    -   Specific exceptions to ignore (`ignoring()`).

You use `FluentWait` when you need more fine-grained control than `WebDriverWait` provides.

### when do you use explicit wait?
**Always.** You use it whenever you need to wait for a specific condition in the application before proceeding. It is the only reliable way to handle synchronization in Selenium. Examples:
-   Waiting for an element to be visible: `visibilityOfElementLocated()`
-   Waiting for an element to be clickable: `elementToBeClickable()`
-   Waiting for an alert to be present: `alertIsPresent()`
-   Waiting for a page title to change: `titleContains()`

### what is stale element exception and how do you handle stale element exception?
`StaleElementReferenceException` occurs when your code has a reference to a `WebElement`, but that element has been removed from the DOM or replaced by a new one.

**Handling:**
The only real solution is to **re-find the element** just before you interact with it. Do not store `WebElement`s as instance variables in your page objects if they will be used across multiple actions that can refresh the DOM. A well-designed explicit wait often handles this implicitly because it re-fetches the element on each polling attempt.

### what is absolute and relative xpath?
-   **Absolute XPath:** Starts from the root (`/html`) and provides the full path. Brittle. Don't use it.
-   **Relative XPath:** Starts with `//` and finds an element anywhere based on its attributes or relationship to other elements. Robust and maintainable. This is the correct choice.

### disadvantages of selenium?
1.  **Only supports web browsers:** Can't automate desktop applications.
2.  **No built-in reporting:** You must integrate third-party tools like TestNG, ExtentReports, or Allure.
3.  **Complex setup:** Setting up a robust framework with a Selenium Grid can be complex.
4.  **Flakiness/Synchronization:** Handling waits and timing issues is the biggest challenge and requires skill to do well. Newer tools like Cypress and Playwright have tried to improve on this.
5.  **No image comparison:** Can't validate images or visual layout without integrating other libraries like AShot or Sikuli.

### Write code to read data from table of specific row in a given webpage
You use XPath to construct a locator for the specific row and cells. Let's say you want the 3rd cell (td[3]) from the row that contains the text "John Smith".

```html
<table>
  <tr><td>Jane Doe</td><td>Manager</td><td>50000</td></tr>
  <tr><td>John Smith</td><td>Developer</td><td>80000</td></tr>
</table>
```

```java
public String getTableCellData(WebDriver driver, String rowIdentifierText, int cellIndex) {
    // Construct a dynamic XPath
    // Find the <tr> that contains a <td> with the identifier text, then find the nth <td> within that row.
    String xpath = String.format("//tr[td[contains(text(), '%s')]]/td[%d]", rowIdentifierText, cellIndex);
    
    WebElement cell = driver.findElement(By.xpath(xpath));
    return cell.getText();
}

// Usage:
// String salary = getTableCellData(driver, "John Smith", 3); // "80000"
```

### how do you pass data in cucumber?
1.  **Parameters in the step:**
    `When I enter "testuser" in the username field` -> Maps to `(String username)`.
2.  **Scenario Outline `Examples` table:** For running the same scenario with multiple data sets.
3.  **Data Tables:** To pass a collection of data to a single step.
    ```gherkin
    When I register with the following details:
      | firstname | lastname | email         |
      | John      | Smith    | john@test.com |
    ```
    In the step definition, you receive this as a `DataTable` object.

### what are tags used in runner class?
The `tags` option in `@CucumberOptions` is used to filter which scenarios to run.
-   `tags = "@smoke"`: Runs only scenarios tagged with `@smoke`.
-   `tags = "@smoke and @regression"`: Runs scenarios that have *both* tags.
-   `tags = "@smoke or @regression"`: Runs scenarios that have *either* tag.
-   `tags = "not @wip"`: Runs all scenarios *except* those tagged with `@wip` (work in progress).

### Write a feature file and step definition to login ecommerce website...
**Feature File (`login_and_add.feature`):**
```gherkin
Feature: Cart Functionality

  Scenario: Add multiple products to cart after login
    Given I am logged in as a valid user
    When I add the following products to the cart:
      | product_name |
      | "Laptop"     |
      | "Mouse"      |
      | "Keyboard"   |
      | "Monitor"    |
      | "Webcam"     |
    And I navigate to the checkout page
    Then I should see 5 items in my cart summary
```

**Step Definitions (`CartSteps.java`):**
```java
import io.cucumber.datatable.DataTable;
import java.util.List;

public class CartSteps {

    // Assuming LoginPage and ProductPage objects exist
    
    @Given("I am logged in as a valid user")
    public void i_am_logged_in() {
        // Code to navigate to login page and log in
        loginPage.login("valid_user", "valid_pass");
    }

    @When("I add the following products to the cart:")
    public void i_add_the_following_products(DataTable dataTable) {
        List<String> products = dataTable.asList(String.class);
        // Skip header row if present, or just get the first column
        for (int i = 1; i < products.size(); i++) {
             productPage.searchFor(products.get(i));
             productPage.clickAddToCart();
        }
    }
    
    @When("I navigate to the checkout page")
    public void i_navigate_to_checkout() {
        header.clickCartIcon();
        header.clickCheckoutButton();
    }

    @Then("I should see {int} items in my cart summary")
    public void i_should_see_items_in_my_cart(Integer expectedCount) {
        int actualCount = checkoutPage.getCartItemCount();
        Assert.assertEquals(expectedCount, actualCount);
    }
}
```

---

## Original Questions (UNTOUCHED)

Cognizant
1 Tell me about your self
2 What is oops and explain using your project
3 Diff between list and set
4 What is Jenkins
5 What is git.
6 Types of locators
7Dynamic xpath and Xpath axes
8 reverse the string
9 List syntax and  print all data from list
10 split letters and number from string
11 write map and retrieve all data from map
12 where you use map in your project
13 write dynamic xpath for ebay
14 write action class and methods
15 what are the exceptions you faced in java and selenium
16 how to handle exception in your project
17 diff between final and finall
18 how to call static block variable
19 diff between super and this
20 diff between abstract and interface
21 diff between method overloading and overriding
22 how you handle dropdown and write code for it
23what are the interface used in selenium
24 how you handle frames
25 what is API
26 Http methods
27 diff between put and post

---

## Answers (No-BS Java QA / SDET Explanations)

> Many of these are repeats. See previous answers for details.

1.  **Tell me about your self**: Standard.
2.  **What is oops and explain using your project**: Encapsulation (POM), Abstraction (`WebDriver`), Inheritance (`BaseTest`), Polymorphism (overriding methods).
3.  **Diff between list and set**: List is ordered and allows duplicates. Set is unordered and unique.
4.  **What is Jenkins**: The leading open-source automation server for CI/CD.
5.  **What is git**: A distributed version control system for tracking changes in source code.
6.  **Types of locators**: `id`, `name`, `className`, `tagName`, `linkText`, `partialLinkText`, `cssSelector`, `xpath`.
7.  **Dynamic xpath and Xpath axes**: Dynamic XPath uses functions (`contains`, `starts-with`) and axes (`following-sibling`, `ancestor`) to find elements with unstable attributes.
8.  **reverse the string**: `new StringBuilder(str).reverse().toString();`
9.  **List syntax and print all data from list**: `List<String> list = new ArrayList<>(); list.add("A"); list.forEach(System.out::println);`
10. **split letters and number from string**: Loop through `str.toCharArray()` and use `Character.isLetter()` and `Character.isDigit()`.
11. **write map and retrieve all data from map**: `Map<String, String> map = new HashMap<>(); map.put("k", "v"); for (Map.Entry<String, String> entry : map.entrySet()) { System.out.println(entry.getKey() + "=" + entry.getValue()); }`
12. **where you use map in your project**: Storing test configuration data; caching test data; character frequency counts.
13. **write dynamic xpath for ebay**: "I would inspect the element, find a stable parent or a partial attribute, and use functions like `contains()` or axes like `following-sibling` to build a robust locator."
14. **write action class and methods**: It's the `Actions` class. `moveToElement()`, `dragAndDrop()`, `contextClick()`. `Actions actions = new Actions(driver); actions.moveToElement(element).click().perform();`
15. **what are the exceptions you faced**: `NoSuchElementException`, `StaleElementReferenceException`, `TimeoutException`.
16. **how to handle exception in your project**: Use `try-catch-finally` for expected exceptions (like `IOException` when reading files). For Selenium exceptions, the best "handling" is prevention through robust explicit waits. Unhandled exceptions should fail the test.
17. **diff between final and finall**: The interviewer means `final` and `finally`. `final` is a keyword to make something unchangeable. `finally` is a block for cleanup code that always executes.
18. **how to call static block variable**: You mean a static variable? You call it using the class name: `MyClass.myStaticVariable`.
19. **diff between super and this**: `this` is the current object. `super` is the parent object.
20. **diff between abstract and interface**: An `abstract` class can have state (instance variables) and implemented methods. A class can only extend one abstract class. An `interface` is pure abstraction (traditionally), cannot have state. A class can implement many interfaces.
21. **diff between method overloading and overriding**: Overloading is same method name, different parameters, same class. Overriding is same method signature, parent-child classes.
22. **how you handle dropdown and write code**: Use the `Select` class for `<select>` tags. `Select s = new Select(element); s.selectByVisibleText("Option");`
23. **what are the interface used in selenium**: `WebDriver`, `WebElement`, `TakesScreenshot`, `JavascriptExecutor`.
24. **how you handle frames**: `driver.switchTo().frame("frameNameOrId");` and `driver.switchTo().defaultContent();`.
25. **what is API**: Application Programming Interface. A contract for software to talk to software, usually over HTTP with JSON data.
26. **Http methods**: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`.
27. **diff between put and post**: `POST` creates, not idempotent. `PUT` replaces, is idempotent.

---

## Original Questions (UNTOUCHED)

Capgemini
- Tell me about your project
- Explain feature file using in your current project
- Reverse 2 number without temporary variable
Int x = 10;
Int y = 20:
- Reverse 2 string without temporary variable
String a = "India":
String b = "uk":
- String str = "123456" Convert into integer.
- What is wrapper class and what are they?
- String is a class Or datatype?
- What will be the output of the following?System.out.println (2+3+"HELLO");
- Difference between array and arraylist?
- Difference between list and set?
- How to find duplicates in 2 arrays
- int [] a = [1, 2,3,4,5,6];
- int [] b = [8, 1,3,9,4];
- Difference between
- Webdriver driver = new ChromeDriver() ;
ChromeDriver driver = new ChromeDriver() :
- How to interact with hidden elements in Selenium Webdriver?
- What is action class and syntax?
- How to use private variable in another class
- What is API ?
- What is Mobile Testing?
- What to do if Two Objects have same Xpath?
- What is the alternative for "click" in Selenium?
- How many PR approval you'll get in your project?
- What will be the answer if we compare
s1==s2
s1==s3
- String s1 = "HELLO";
- String s2 = "HELLO";
String s3 =  new String("HELLO"):
- System.out.println(s1==s2) //true
- System.out.println(s1 == s3); // false

---

## Answers (No-BS Java QA / SDET Explanations)

> This section has some great, tricky questions mixed with repeats.

### Tell me about your project
Standard.

### Explain feature file using in your current project
"In our Cucumber framework, a feature file describes one feature, like 'User Login'. It contains one or more `Scenario`s or `Scenario Outline`s written in Gherkin. For example, a login feature file would have a scenario for successful login, and a scenario outline for multiple failed login attempts with different invalid data. It serves as both our test case and our documentation."

### Reverse 2 number without temporary variable
This is a classic bit-twiddling or arithmetic trick.

```java
int x = 10;
int y = 20;

// Arithmetic way
x = x + y; // x = 30
y = x - y; // y = 30 - 20 = 10 (original x)
x = x - y; // x = 30 - 10 = 20 (original y)

// XOR way (more "leet")
x = x ^ y;
y = x ^ y;
x = x ^ y;
```

### Reverse 2 string without temporary variable
This uses string concatenation and `substring`. It's less efficient than using a temp variable but answers the riddle.

```java
String a = "India";
String b = "uk";

a = a + b; // a = "Indiauk"
b = a.substring(0, a.length() - b.length()); // b = "India"
a = a.substring(b.length()); // a = "uk"
```

### String str = "123456" Convert into integer.
`Integer.parseInt(str);`

### What is wrapper class and what are they?
A wrapper class is a class that wraps a primitive data type into an object. They are needed for collections like `ArrayList`, which can only store objects.
- `int` -> `Integer`
- `char` -> `Character`
- `double` -> `Double`
- `boolean` -> `Boolean`
etc. The process of converting a primitive to a wrapper is called **autoboxing**. The reverse is **unboxing**.

### String is a class Or datatype?
`String` is a **class** (`java.lang.String`). It's a reference type (non-primitive), not a primitive data type.

### What will be the output of the following? System.out.println (2+3+"HELLO");
Execution goes from left to right.
1.  `2 + 3` is integer addition, which results in `5`.
2.  `5 + "HELLO"` is string concatenation, which results in `"5HELLO"`.
**Output: `5HELLO`**

If it were `System.out.println("HELLO"+2+3);`, the output would be `"HELLO23"`.

### Difference between array and arraylist?
Array is fixed-size and a basic language feature. `ArrayList` is dynamic-size and part of the Collections framework.

### Difference between list and set?
`List` is ordered and allows duplicates. `Set` is unordered and unique.

### How to find duplicates in 2 arrays
The most efficient way is to use a `Set`.
1.  Create a `Set` from the first array.
2.  Iterate through the second array. For each element, try to add it to the set.
3.  If `set.add(element)` returns `false`, it means the element was already in the set (from the first array), so it's a duplicate.

```java
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

public class ArrayDuplicates {
    public static void findDuplicates(int[] a, int[] b) {
        Set<Integer> setA = Arrays.stream(a).boxed().collect(Collectors.toSet());
        Set<Integer> duplicates = new HashSet<>();
        for (int num : b) {
            if (!setA.add(num)) {
                duplicates.add(num);
            }
        }
        System.out.println("Duplicates are: " + duplicates); // [1, 3, 4]
    }
}
```

### Difference between `Webdriver driver = new ChromeDriver()` and `ChromeDriver driver = new ChromeDriver()`
This is about coding to an interface vs. coding to an implementation.
-   **`WebDriver driver = new ChromeDriver();` (Correct way):** You are creating a `ChromeDriver` object but referencing it through the `WebDriver` interface. This is good practice. It means you can easily change the implementation later: `WebDriver driver = new FirefoxDriver();` without changing any of the rest of your code that uses the `driver` object (as long as it only uses methods defined in the `WebDriver` interface). This is abstraction.

-   **`ChromeDriver driver = new ChromeDriver();` (Bad way):** You are tying your code directly to the `ChromeDriver` implementation. If you do this, you can access Chrome-specific methods not present in the `WebDriver` interface, but your code is no longer portable to other browsers. You would have to rewrite it to run on Firefox.

### How to interact with hidden elements in Selenium Webdriver?
You can't, directly. Selenium is designed to replicate user behavior, and a user cannot interact with a hidden element. `ElementNotInteractableException` is the expected result.

If you absolutely must interact with it (which usually indicates a flaw in your test approach), the only way is to use **`JavascriptExecutor`**.
`((JavascriptExecutor) driver).executeScript("arguments[0].click();", hiddenElement);`
This bypasses Selenium's visibility checks and tells the browser to fire the event directly. It should be a last resort.

### What is action class and syntax?
It's the `Actions` class. `Actions actions = new Actions(driver); actions.moveToElement(el).perform();`

### How to use private variable in another class
You don't, directly. That's the point of `private`. You provide `public` getter and setter methods in the class that owns the variable. This is encapsulation.

### What is Mobile Testing?
Testing an application on a mobile device. This can be:
-   **Native App Testing:** Testing an app installed on iOS or Android.
-   **Mobile Web Testing:** Testing your website on a mobile browser.
-   **Tools:** Appium is the Selenium equivalent for mobile apps. It even uses the WebDriver protocol.

### What to do if Two Objects have same Xpath?
`driver.findElement(By.xpath(xpath))` will always return the **first** one it finds in the DOM. If you need the second or third one, you have two options:
1.  **Use `findElements`:** `List<WebElement> elements = driver.findElements(By.xpath(xpath));` and then access the one you want by its index: `elements.get(1)` for the second one.
2.  **Refine the XPath:** Wrap your XPath in parentheses and specify an index: `(your-xpath)[2]`. This tells XPath to get the second matching node from the result set. Example: `(//div[@class='product'])[2]`

### What is the alternative for "click" in Selenium?
1.  **`Actions` class:** `new Actions(driver).click(element).perform();` (This is more for complex chains but can be used).
2.  **JavaScript click:** `((JavascriptExecutor) driver).executeScript("arguments[0].click();", element);` (The "big hammer" for when a normal click doesn't work).
3.  **`sendKeys(Keys.ENTER)`:** If the element is a form submit button, you can sometimes type into a field and then send the ENTER key to that field.

### How many PR approval you'll get in your project?
This is a process question. "In my project, we had a policy that every pull request required at least **one** approval from another engineer on the team before it could be merged into the main branch. For critical framework changes, we required two approvals."

### What will be the answer if we compare `s1==s2` and `s1==s3`
This tests knowledge of the String Constant Pool.

```java
String s1 = "HELLO";
String s2 = "HELLO";
String s3 = new String("HELLO");
```
-   `s1` and `s2` are string literals. The JVM is smart and places them in the **String Constant Pool**. Both `s1` and `s2` will point to the *exact same object* in memory.
-   `s3` uses the `new` keyword. This explicitly forces the creation of a **new object** on the heap, outside the pool.

-   `System.out.println(s1 == s2);` -> **`true`**. They point to the same object in the pool.
-   `System.out.println(s1 == s3);` -> **`false`**. They point to different objects in different memory locations.
-   `System.out.println(s1.equals(s3));` -> **`true`**. Their content is the same.
