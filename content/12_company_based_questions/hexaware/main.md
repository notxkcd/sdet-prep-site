---
title: "Hexaware"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

Hexaware:


1) Explain your project
2) Write a TestCase for your Project.
3) Write a program to convert array to list and explain the program.
4) Write a program to find a duplicate word from the string s="Hexaware" and explain the program.
5) What is break? why it is used?
6) What is the difference between List and Map?
7) What is collections?
8) What is window handling and its methods
9) What is the difference between Array and ArrayList?
10) Write a syntax for moveToElement?
11) What is Action class?
12) What is perform() method why it is used.
13) Write a sql to find the Employee name from the table
14) Write a code to read the text file.
15) How to handle dynamic web elements?
16) What is polymorphism?
17) Explain STLC
18) in which phase, we will detect the defect in STLC?
19) What is Maven?
20) What is grooming session?
21) What is day to day activity?
22) What is your roles and responsiblity?
23) what is API?
24) if the url is password protected, where will you give the password in postman tool.
25) Status code
26) TestNg Annotation

---

## Answers (No-BS Java QA / SDET Explanations)

### 1) Explain your project

Standard opener. Be concise and technical. Mention the application domain, your specific responsibilities, the tech stack, and the scale. Example: "I was the lead QA automation engineer for a B2B logistics platform. I was responsible for designing and maintaining the end-to-end test framework for the shipment tracking and invoicing modules. The stack was Java, Selenium, REST-assured, and Jenkins."

### 2) Write a TestCase for your Project.

They want to see if you can think in a structured way. Pick a simple, core feature of your project. Don't write a novel. Use a standard format.

**Feature:** User Login
**Test Case ID:** TC_LOGIN_001
**Title:** Verify successful login with valid credentials
**Preconditions:**
1.  User exists in the system with username "testuser" and password "password123".
2.  Browser is open at the login page.
**Steps:**
1.  Enter "testuser" into the username field.
2.  Enter "password123" into the password field.
3.  Click the "Login" button.
**Expected Result:**
-   User is redirected to the account dashboard page (`/dashboard`).
-   A "Welcome, testuser" message is visible.

### 3) Write a program to convert array to list and explain the program.

The modern, correct way uses `Arrays.asList()` or streams.

```java
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class ArrayConverter {

    public static void main(String[] args) {
        String[] carArray = {"BMW", "Audi", "Mercedes"};

        // Method 1: Arrays.asList()
        // Quick and easy, but creates a fixed-size list backed by the original array.
        // You can't add or remove elements from this list.
        List<String> carListFixed = Arrays.asList(carArray);
        System.out.println("Fixed-size list: " + carListFixed);

        // Method 2: Streams (The better, more flexible way)
        // This creates a new, fully functional ArrayList.
        List<String> carListMutable = Arrays.stream(carArray).collect(Collectors.toList());
        carListMutable.add("Tesla"); // This works
        System.out.println("Mutable list: " + carListMutable);
    }
}
```
**Explanation:**
-   `Arrays.asList(carArray)` is a factory method that returns a `List` wrapper around the original array. It's fast but inflexible. Changes to the array will reflect in the list and vice versa. You cannot change its size.
-   `Arrays.stream(carArray).collect(Collectors.toList())` creates a stream from the array, then collects the elements into a brand new `ArrayList`. This is the one you want for a general-purpose, mutable list.

### 4) Write a program to find a duplicate word from the string s="Hexaware" and explain the program.

"Word" is a typo, they mean character. The question is to find duplicate *characters*. Using a `Set` is the classic approach to check for duplicates.

```java
import java.util.HashSet;
import java.util.Set;

public class DuplicateFinder {

    public static void findDuplicateChars(String str) {
        if (str == null || str.length() < 2) {
            System.out.println("No duplicates possible.");
            return;
        }

        Set<Character> uniqueChars = new HashSet<>();
        Set<Character> duplicateChars = new HashSet<>();

        for (char c : str.toCharArray()) {
            // The add() method returns false if the element is already in the set.
            if (!uniqueChars.add(c)) {
                duplicateChars.add(c);
            }
        }

        System.out.println("Duplicate characters are: " + duplicateChars); // Output: [e]
    }

    public static void main(String[] args) {
        findDuplicateChars("Hexaware");
    }
}
```
**Explanation:**
1.  We iterate through the string's characters.
2.  We use a `HashSet` called `uniqueChars` to keep track of the characters we've seen.
3.  The `add()` method of a `Set` returns `true` if the element was successfully added (i.e., it was new), and `false` if the element was already present.
4.  If `add()` returns `false`, we know we've found a duplicate, so we add it to our `duplicateChars` set.

### 5) What is break? why it is used?

`break` is a control flow statement. It has two main uses:
1.  **Exiting a loop:** Immediately terminates the innermost `for`, `while`, or `do-while` loop.
2.  **Exiting a `switch` statement:** Stops execution from "falling through" to the next `case`. This is the most common use.

```java
// Use 1: Exiting a loop
int[] numbers = {1, 5, -3, 10, 2};
for (int num : numbers) {
    if (num < 0) {
        System.out.println("Negative number found. Stopping.");
        break; // Exit the for loop immediately
    }
    System.out.println(num);
}

// Use 2: In a switch
int day = 3;
String dayName;
switch (day) {
    case 1: dayName = "Monday"; break;
    case 2: dayName = "Tuesday"; break;
    case 3: dayName = "Wednesday"; break; // without break, it would fall through to Thursday
    case 4: dayName = "Thursday"; break;
    default: dayName = "Unknown"; break;
}
```

### 6) What is the difference between List and Map?

They are both core collection interfaces, but they model different things.

-   **`List`**: An ordered collection of elements. Think of it as an array that can grow.
    -   **Key feature:** Access by integer index (`list.get(0)`).
    -   **Allows duplicates.**
    -   **Example:** A list of `WebElement`s returned by `driver.findElements()`. The order matters.

-   **`Map`**: A collection of key-value pairs. Think of it as a dictionary or a lookup table.
    -   **Key feature:** Access by key (`map.get("myKey")`).
    -   **Keys must be unique.** Values can be duplicates.
    -   **Example:** Storing test configuration where the key is the property name (e.g., "browser") and the value is the setting (e.g., "chrome").

| Feature      | `List`                         | `Map`                          |
| :----------- | :----------------------------- | :----------------------------- |
| Structure    | Ordered sequence of elements   | Unordered set of key-value pairs |
| Access       | By integer index (`get(index)`) | By key (`get(key)`)            |
| Duplicates   | Allows duplicate elements      | Keys must be unique            |
| Implementation | `ArrayList`, `LinkedList`      | `HashMap`, `LinkedHashMap`     |

### 7) What is collections?

"Collections" usually refers to the **Java Collections Framework**. It's a set of interfaces and classes in the `java.util` package for storing and manipulating groups of objects.

**The core interfaces are:**
-   **`Collection`**: The root interface.
    -   **`List`**: Ordered, indexed, allows duplicates.
    -   **`Set`**: Unordered, does not allow duplicates.
    -   **`Queue`**: A collection for holding elements prior to processing (e.g., FIFO - First-In, First-Out).
-   **`Map`**: A separate interface for key-value pairs. It does not extend `Collection`.

The framework also provides concrete implementations (`ArrayList`, `HashSet`, `HashMap`) and utility classes (`Collections` with an 's') with static methods for sorting, searching, etc.

### 8) What is window handling and its methods

This is for dealing with multiple browser windows or tabs. Selenium's driver has one focus at a time. If a new window opens, you must switch the driver's focus to it.

**Methods:**
-   `driver.getWindowHandle()`: Returns the unique string ID of the **current** window.
-   `driver.getWindowHandles()`: Returns a `Set<String>` of the IDs of **all** open windows.
-   `driver.switchTo().window(String windowHandleId)`: Switches the driver's focus to the window with the given ID.

> **Side note:** The process is always: get original handle, trigger new window, get all handles, loop to find the new one, switch to it.

### 9) What is the difference between Array and ArrayList?

-   **Array:**
    -   Fixed size. You declare the size when you create it, and it can never change.
    -   A basic language feature, not part of the Collections Framework.
    -   Can hold primitives (`int[]`) or objects (`String[]`).
    -   Access elements with `array[i]`.
    -   Length is a property: `array.length`.

-   **`ArrayList`:**
    -   Dynamic size. It grows automatically as you add elements.
    -   Part of the Collections Framework (`implements List`).
    -   Can only hold objects. For primitives, you must use wrapper classes (`ArrayList<Integer>`).
    -   Access elements with `list.get(i)`.
    -   Size is a method: `list.size()`.
    -   Provides many useful methods for manipulation (`add`, `remove`, `clear`, `contains`, etc.).

**Rule:** Use an `Array` if you know the exact size of your collection and it will never change. For everything else, use an `ArrayList`. In test automation, you almost always want `ArrayList`.

### 10) Write a syntax for moveToElement?

`moveToElement` is a method of the `Actions` class. It's used to simulate hovering the mouse over an element.

```java
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;

public class ActionsExample {
    public void hoverOverMenu(WebDriver driver) {
        // 1. Create an Actions object
        Actions actions = new Actions(driver);
        
        // 2. Find the element to hover over
        WebElement mainMenu = driver.findElement(By.id("main-menu"));

        // 3. Build the action and perform it
        actions.moveToElement(mainMenu).perform(); 
    }
}
```
The key is the chain: `actions.moveToElement(element).perform()`.

### 11) What is Action class?

It's the `Actions` class (plural). It's a utility in Selenium for building and executing sequences of complex user interactions that can't be done with a single `click()` or `sendKeys()`.

**Use it for:**
-   Mouse hovers (`moveToElement`)
-   Right-clicks (`contextClick`)
-   Double-clicks (`doubleClick`)
-   Drag and drop (`dragAndDrop`)
-   Keyboard actions like holding down SHIFT while clicking (`keyDown`, `keyUp`).

### 12) What is perform() method why it is used.

The `perform()` method is what actually **executes** the sequence of actions you've defined with the `Actions` class.

All the methods like `moveToElement()`, `click()`, `sendKeys()` are just steps in a builder pattern. They build up a composite action. Nothing happens until you call `perform()`.

```java
// This does NOTHING. It just defines the action.
actions.moveToElement(menu).click(submenu); 

// This executes the hover-and-click action in the browser.
actions.moveToElement(menu).click(submenu).perform(); 
```
> **Side note:** There's also a `.build()` method. `perform()` is just a shortcut for `build().perform()`. You'd use `.build()` if you wanted to store the compiled action in a variable to be executed later.

### 13) Write a sql to find the Employee name from the table

Assuming a table named `Employees` with columns `EmployeeID`, `FirstName`, `LastName`.

```sql
-- Find a specific employee by ID
SELECT FirstName, LastName
FROM Employees
WHERE EmployeeID = 123;

-- Find all employees
SELECT FirstName, LastName
FROM Employees;
```

### 14) Write a code to read the text file.

The modern way uses `java.nio.file.Files`. It's cleaner and more efficient than older `FileReader` or `Scanner` approaches.

```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Stream;

public class FileReader {
    
    public void readFile(String filePath) {
        try {
            // Method 1: Read all lines into a List<String>
            List<String> allLines = Files.readAllLines(Paths.get(filePath));
            allLines.forEach(System.out::println);

            System.out.println("---");

            // Method 2: Process lines as a Stream (more memory efficient for huge files)
            try (Stream<String> stream = Files.lines(Paths.get(filePath))) {
                stream.forEach(System.out::println);
            }

        } catch (IOException e) {
            System.err.println("Failed to read file: " + e.getMessage());
            // In a real test, you'd probably throw a custom runtime exception here
        }
    }
}
```

### 15) How to handle dynamic web elements?

"Dynamic element" usually means an element whose attributes (like `id` or `class`) change on every page load. `id="ember345"`, `id="ember357"`.

You can't use those dynamic attributes for your locators. The solution is to find a **stable locator** based on something that *doesn't* change.

1.  **Use static text:** Find the element based on its visible text. This is often brittle if the text changes. `//button[text()='Submit']`
2.  **Use a stable attribute:** Look for `data-testid`, `name`, or another attribute that developers have put there for testing purposes. `//button[@data-testid='submit-button']`
3.  **Find a stable parent:** Locate a stable parent element, then find your dynamic element relative to it. This is what XPath axes are for.
    ```xpath
    // Find a div with a stable ID, then find the button inside it.
    //div[@id='stable-parent-id']//button
    ```
4.  **Use partial matches (`contains`, `starts-with`):** If part of the attribute is stable, use that.
    ```xpath
    // ID is 'user-12345', 'user-67890'. The 'user-' part is stable.
    //input[starts-with(@id, 'user-')]
    ```

### 16) What is polymorphism?

Answered in WIPRO section. It means "many forms." In OOP, it's the ability of an object to be treated as an instance of its parent class. The most practical application is **method overriding**, where a subclass provides its own implementation of a method from its superclass.

### 17) Explain STLC

Software Testing Life Cycle. It's a sequence of specific activities conducted during the testing process.

1.  **Requirement Analysis:** QA team understands the requirements. Identifies testable requirements.
2.  **Test Planning:** The Test Lead/Manager defines the test strategy, objectives, resources, and schedule.
3.  **Test Case Design:** Test cases are created, reviewed, and approved. Test data is prepared.
4.  **Test Environment Setup:** The environment (servers, devices, browsers) where testing will be done is prepared and validated.
5.  **Test Execution:** The prepared test cases are run. Bugs are found and reported.
6.  **Test Cycle Closure:** The testing process is formally concluded. A test closure report is prepared with final metrics.

### 18) in which phase, we will detect the defect in STLC?

Defects are primarily **detected** during the **Test Execution** phase.

However, a good QA process finds issues much earlier:
-   During **Requirement Analysis**, you can find defects in the requirements themselves (ambiguity, contradictions).
-   During **Test Case Design**, you can find logic flaws or uncover edge cases that weren't considered.

The mantra is "shift left." The earlier you find a defect, the cheaper it is to fix.

### 19) What is Maven?

Maven is a build automation and project management tool. It's the backbone of most professional Java projects.

**For a QA engineer, it does three critical things:**
1.  **Dependency Management:** It automatically downloads and manages all the libraries your project needs (Selenium, TestNG, REST-assured, etc.). You declare them in the `pom.xml` file, and Maven handles the rest. This solves "jar hell."
2.  **Build Lifecycle:** It defines a standard lifecycle for building your project: `compile`, `test`, `package`, `install`, `deploy`. You can run your entire test suite from the command line with a single command: `mvn test`. This is how CI/CD servers like Jenkins run your tests.
3.  **Project Object Model (POM):** The `pom.xml` file is the heart of a Maven project. It describes the project, its dependencies, and how to build it.

### 20) What is grooming session?

Also called "backlog refinement." It's a meeting in Agile/Scrum where the product owner and the development team (including QA) review items on the product backlog.

**The goals are:**
-   To ensure the backlog items are well-understood.
-   To add details and requirements.
-   To break down large items (epics) into smaller user stories.
-   To estimate the effort required for each story (story points).

**QA's role here is critical:** You ask questions to uncover ambiguities, identify edge cases, and determine the testability of a feature *before* any code is written.

### 21) What is day to day activity?

"My day is usually structured around the current sprint:"
1.  **Stand-up:** "Start the day with the daily stand-up meeting to sync with the team on progress and blockers."
2.  **Test Design/Automation:** "If we're at the beginning of a sprint, I'm analyzing new user stories, writing test cases in Jira, and starting to write the automation scripts for them."
3.  **Test Execution & Reporting:** "If a new build has been deployed to the QA environment, I'm running the regression suite, performing exploratory testing on new features, and reporting any bugs found."
4.  **Collaboration:** "I work closely with developers to reproduce and debug issues, and with the product owner to clarify requirements."
5.  **Framework Maintenance:** "I might also spend time maintaining or improving our test framework, for example, by adding a new utility or refactoring a page object."

### 22) What is your roles and responsiblity?

This is a higher-level version of the previous question.
-   "My primary responsibility is to ensure the quality of the product."
-   "This involves designing and implementing the test automation strategy for our web application."
-   "I am responsible for writing and maintaining automated UI and API tests using Selenium and REST-assured."
-   "I integrate these tests into our Jenkins CI/CD pipeline to provide fast feedback to the development team."
-   "I also perform manual exploratory testing to find bugs that automation might miss and am responsible for bug advocacy, from reporting in Jira to verification of the fix."

### 23) what is API?

Application Programming Interface. It's a contract that allows two pieces of software to talk to each other. In web development, this usually means a **web API** that allows a frontend (like a React web app) to get data from a backend server over HTTP.

Instead of returning HTML like a traditional website, a web API returns data, usually in JSON format.

### 24) if the url is password protected, where will you give the password in postman tool.

You use the **Authorization** tab in Postman. You don't put credentials directly in the URL.

The specific type of authorization depends on the API:
-   **Basic Auth:** You select "Basic Auth" and enter a username and password. Postman will encode this and add it to the request headers.
-   **Bearer Token:** You select "Bearer Token" and paste in an API token (like a JWT) that you've received from a login endpoint.
-   **API Key:** You select "API Key" and provide the key and value, specifying whether it goes in the Header or Query Params.

### 25) Status code

Answered in the WIPRO section. Know your 2xx, 4xx, and 5xx codes.
-   `200 OK`
-   `201 Created`
-   `204 No Content`
-   `400 Bad Request`
-   `401 Unauthorized`
-   `403 Forbidden`
-   `404 Not Found`
-   `500 Internal Server Error`

### 26) TestNg Annotation

These are markers that tell TestNG how to treat a Java method.

**Execution Order Annotations:**
-   `@BeforeSuite` / `@AfterSuite`: Runs once before/after all tests in the suite.
-   `@BeforeTest` / `@AfterTest`: Runs once before/after all tests in a `<test>` tag in `testng.xml`.
-   `@BeforeClass` / `@AfterClass`: Runs once before/after all tests in the current class.
-   `@BeforeMethod` / `@AfterMethod`: Runs before/after **each** test method (`@Test`). This is where you put `WebDriver` setup and teardown.

**Test Method Annotation:**
-   `@Test`: Marks a method as a test case.

**Data Annotation:**
-   `@DataProvider`: Marks a method that supplies data to a test method.

---

## Original Questions (UNTOUCHED)

- Hexaware technology
Round 1:
1) tell me about yourself
2) explain about project
3) difference b/w class and object
4) equals and '=='
5) find vowels in the string 'welcome'
6) what is static and dynamic testing
7) explain about keyword driven and data driven framework
8) Test driven development

ROUND 2:
1) why looking for job change
2) what is your salary
3) which framework is best in the current market
4) difference b/w set and hashmap explain where u use in project
5) Why bdd is considered best.

---

## Answers (No-BS Java QA / SDET Explanations)

### Round 1

#### 1) tell me about yourself

Standard opener. See previous answers.

#### 2) explain about project

Standard opener. See previous answers.

#### 3) difference b/w class and object

-   **Class:** A blueprint or template for creating objects. It defines properties (variables) and behaviors (methods). A `class` is a concept in your source code. `public class Car { ... }`
-   **Object:** A specific instance of a class. It's a concrete thing that exists in memory at runtime. You create an object using the `new` keyword. `Car myBmw = new Car();`

Analogy: A `class` is the blueprint for a house. An `object` is the actual house built from that blueprint. You can build many houses (objects) from one blueprint (class).

#### 4) equals and '=='

This is a fundamental Java question.
-   **`==` (Operator):** For primitive types (`int`, `char`, etc.), it compares **values**. For objects, it compares **memory addresses**. It checks if two references point to the exact same object in memory.

-   **`.equals()` (Method):** This method is defined in the `Object` class. By default, it behaves exactly like `==` (compares memory addresses). However, classes like `String`, `Integer`, etc., **override** this method to compare the actual **content** or value of the objects.

```java
String s1 = new String("hello");
String s2 = new String("hello");
String s3 = s1;

System.out.println(s1 == s2);      // false (different objects in memory)
System.out.println(s1.equals(s2)); // true (content is the same)
System.out.println(s1 == s3);      // true (both references point to the same object)
```
> **Rule of thumb:** For comparing objects, you almost always want to use `.equals()`. Use `==` for primitives.

#### 5) find vowels in the string 'welcome'

A simple loop and check.

```java
public class VowelFinder {
    public static void findVowels(String str) {
        String vowels = "aeiou";
        System.out.print("Vowels in '" + str + "': ");
        for (char c : str.toLowerCase().toCharArray()) {
            if (vowels.indexOf(c) != -1) {
                System.out.print(c + " "); // e o e
            }
        }
        System.out.println();
    }

    public static void main(String[] args) {
        findVowels("welcome");
    }
}
```

#### 6) what is static and dynamic testing

-   **Static Testing:** Testing the code without actually running it. It's about prevention, not detection.
    -   **Examples:** Code reviews, static analysis tools (like SonarQube or Checkstyle) that check for style violations or potential bugs, reviewing requirements and design documents.

-   **Dynamic Testing:** Testing the code by executing it. This is what most people think of as "testing."
    -   **Examples:** Unit tests, integration tests, end-to-end UI tests, API tests. You are running the application and verifying its behavior.

#### 7) explain about keyword driven and data driven framework

These are two strategies for designing test automation frameworks, often used together.

-   **Data-Driven Framework:** The test data (inputs and expected outputs) is separated from the test script logic. The data is stored externally (e.g., in Excel, JSON, or a database). The same test script is run multiple times with different sets of data. TestNG's `@DataProvider` is a perfect example of this.
    -   **Benefit:** Easily add new test cases by just adding a new row of data. No code changes needed.

-   **Keyword-Driven Framework:** This is another layer of abstraction. You create a high-level "keyword" for each common action (e.g., `login`, `createOrder`, `verifyText`). The test case is then written as a sequence of these keywords, often in a spreadsheet. A test interpreter reads the spreadsheet and calls the corresponding Java methods.
    -   **Benefit:** Can allow non-programmers to write test cases (in theory).
    -   **Drawback:** Can become very complex to maintain. The layer of indirection makes debugging harder.

A **Hybrid Framework** combines elements of both, which is what most modern frameworks are. They are data-driven using external files, but also have keyword-like reusable methods in Page Objects.

#### 8) Test driven development

TDD is a software development process where you write the **test before** you write the application code.

**The cycle (Red-Green-Refactor):**
1.  **Red:** Write a failing test for a small piece of functionality that doesn't exist yet. The test will fail because the code hasn't been written.
2.  **Green:** Write the absolute minimum amount of application code required to make the test pass. Don't add extra features. Just make the bar go green.
3.  **Refactor:** Clean up the code you just wrote (both the test code and the application code) while keeping the test passing. Remove duplication, improve readability.
4.  Repeat the cycle for the next piece of functionality.

> **Side Note:** BDD (Behavior-Driven Development) is an evolution of TDD that emphasizes writing the tests in a human-readable format (like Gherkin) that describes the *behavior* of the system from the user's perspective.

### Round 2

#### 1) why looking for job change

Be positive. Don't badmouth your current company.
-   "I'm looking for a new challenge and an opportunity to grow my skills in a different environment."
-   "I'm particularly interested in [Company Name]'s work in [specific area, e.g., fintech, cloud services], and I want to apply my automation skills to more complex systems."
-   "I'm seeking a role with more responsibility where I can contribute to test strategy at a higher level."

#### 2) what is your salary

Do your research. Know the market rate for your experience level and location. Give a range.
-   "Based on my experience and the market rate for this role, I'm expecting a salary in the range of [X] to [Y]."
-   You can also deflect: "I'm open to discussing compensation, but first I'd like to ensure this role is a great fit for both of us. Could you tell me the approved salary range for this position?"

#### 3) which framework is best in the current market

This is a trick question. There is no single "best" framework. The best one is the one that fits the project's needs.

A good answer shows you understand this trade-off:
"There isn't one 'best' framework, it depends on the context.
-   For a team of Java experts doing complex web UI testing, a custom-built framework with **Selenium, TestNG, and Maven** is powerful and flexible.
-   For a team with mixed technical skills or a need for strong BDD collaboration, a framework built on **Cucumber** might be better.
-   For modern JavaScript-based applications, frameworks like **Cypress** or **Playwright** are gaining huge popularity because they are faster and less flaky for certain tasks, as they operate differently from Selenium."

This shows you are aware of the industry landscape beyond just one tool.

#### 4) difference b/w set and hashmap explain where u use in project

-   **`Set`**: A collection of **unique elements**. It implements the `Collection` interface. `Set<String>`.
-   **`HashMap`**: A collection of **key-value pairs**. Keys must be unique. It implements the `Map` interface. `HashMap<String, String>`.

A `HashSet` is actually implemented using a `HashMap` internally. The set's elements are stored as the keys of the map, and a constant dummy object is used for the values.

**Where you use them in a project:**
-   **`Set` Use Case:** "I used a `HashSet` to verify that all the links on our sitemap page were unique. I scraped all the `href` attributes into a list, then added them to a set. I then asserted that `list.size() == set.size()` to confirm there were no duplicates."
-   **`HashMap` Use Case:** "I used a `HashMap` to store test environment configuration. The key was the property name like '`baseUrl`' or '`browser`', and the value was the corresponding URL or browser name. This allowed for easy lookup of configuration settings within the framework."

#### 5) Why bdd is considered best.

Again, "best" is a trap. BDD is a tool, and it's not always the right one.

**The argument for BDD being "best":**
-   **Collaboration:** It creates a "ubiquitous language" using Gherkin (`Given/When/Then`). Product owners, developers, and QAs can all read and understand the feature files, which act as living documentation and acceptance criteria.
-   **User Focus:** It forces you to think about and describe the *behavior* of the system from a user's perspective, rather than just testing implementation details.

**The pragmatic counter-argument:**
-   **Overhead:** It adds a layer of abstraction between the feature file and the step definition code. This can make debugging and maintenance more complex.
-   **The BDD Fallacy:** In many teams, only technical people write the Gherkin files anyway, completely defeating the purpose of collaboration with non-technical stakeholders. In these cases, it's just extra boilerplate.

**A good answer:** "BDD is considered powerful because it improves collaboration and aligns testing with business requirements. However, it's only 'best' if the team is disciplined about using it for that purpose. If it's just developers writing Gherkin for themselves, it can be an unnecessary complication compared to a straightforward TestNG/JUnit framework."

---

## Original Questions (UNTOUCHED)

Hexaware technologies interview questions:
1) Given date format: 03-06-1995 and output should be in this format: 03/06/1995. Write a java program for it.
2) X = "A", Y=" B". Retrieve these two values using hashmap.
3) what is epic?
4) what are all the challenges you faced in last automation project?
5) How to derive at story points?
6) what is glue in cucumber?

---

## Answers (No-BS Java QA / SDET Explanations)

### 1) Given date format: 03-06-1995 and output should be in this format: 03/06/1995. Write a java program for it.

This is a string manipulation question, but the *correct* way to handle dates is with Java's date/time APIs.

```java
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class DateConverter {

    public static void main(String[] args) {
        String inputDate = "03-06-1995";

        // The dumb, brittle way. Don't do this in an interview unless forced.
        String simpleReplace = inputDate.replace('-', '/');
        System.out.println("Simple replace: " + simpleReplace);

        // The correct, robust way using java.time
        // Define the format of the input string
        DateTimeFormatter inputFormatter = DateTimeFormatter.ofPattern("dd-MM-yyyy");
        // Define the format for the output string
        DateTimeFormatter outputFormatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        // Parse the input string into a LocalDate object
        LocalDate date = LocalDate.parse(inputDate, inputFormatter);
        
        // Format the LocalDate object into the desired output string
        String outputDate = date.format(outputFormatter);
        
        System.out.println("Correct conversion: " + outputDate);
    }
}
```
**Explanation:** Using `java.time` is better because it validates that the input is a real date. `replace()` would happily convert "99-99-9999". A professional engineer uses the right tool for the job, and for dates, that tool is the `java.time` package.

### 2) X = "A", Y=" B". Retrieve these two values using hashmap.

The question is poorly phrased. It likely means "store these two values in a HashMap and then retrieve them."

```java
import java.util.HashMap;
import java.util.Map;

public class HashMapExample {
    public static void main(String[] args) {
        // Create a HashMap
        Map<String, String> map = new HashMap<>();

        // Store the values. We need keys for them. Let's call them "keyForX" and "keyForY".
        String x = "A";
        String y = "B"; // The original had a space, let's trim it.
        
        map.put("keyForX", x);
        map.put("keyForY", y.trim());

        // Retrieve the values using their keys
        String retrievedX = map.get("keyForX");
        String retrievedY = map.get("keyForY");

        System.out.println("Retrieved X: " + retrievedX); // A
        System.out.println("Retrieved Y: " + retrievedY); // B
    }
}
```
> **Side Note:** If the interviewer insists "the key is X", then the code is `map.put("X", "A")` and `map.get("X")`. Clarify the intent.

### 3) what is epic?

In Agile/Scrum, an epic is a large body of work that can be broken down into a number of smaller tasks (called user stories).

-   **Epic:** "Implement Online Payment System"
-   **User Stories within the Epic:**
    -   "As a user, I want to pay with a Credit Card."
    -   "As a user, I want to pay with PayPal."
    -   "As a user, I want to receive an email confirmation after payment."

Epics are often used as placeholders for big ideas that haven't been fully fleshed out yet. They typically span multiple sprints.

### 4) what are all the challenges you faced in last automation project?

Have a few real-world examples ready. This shows you've actually done the job.

-   **Challenge 1: Flaky Tests due to Timing Issues.** "Our application used a lot of asynchronous JavaScript. Initially, the tests were full of `Thread.sleep()`, which made them unreliable. My biggest challenge was to refactor the entire suite to use explicit waits (`WebDriverWait`), waiting for specific conditions before proceeding. This made the suite much more stable."
-   **Challenge 2: Dynamic Elements.** "The front-end developers used a framework that generated dynamic IDs for many elements. I had to develop robust XPath and CSS selector strategies using axes (`following-sibling`, `ancestor`) and `data-testid` attributes to create stable locators."
-   **Challenge 3: Test Data Management.** "Our tests needed unique user data for each run. We initially hardcoded it, which caused failures when running tests in parallel. I implemented a `TestDataFactory` class that generated unique user data on-the-fly, ensuring test isolation."

### 5) How to derive at story points?

Story points are a relative measure of the effort required to implement a user story. It's not about hours or days. It's a combination of complexity, uncertainty, and volume of work.

**The process is called Planning Poker:**
1.  The product owner explains a user story.
2.  The team discusses the story and asks questions.
3.  Each team member (dev, QA, etc.) privately chooses a card from a Fibonacci-like sequence (1, 2, 3, 5, 8, 13...).
4.  Everyone reveals their card at the same time.
5.  If the estimates are similar, you agree on a number and move on.
6.  If the estimates are wildly different (e.g., one person says 2, another says 13), this triggers a discussion. The person with the high estimate explains what they think makes it complex. The person with the low estimate explains what they think makes it simple. This conversation is the most valuable part of the process, as it uncovers hidden assumptions.
7.  The team re-votes until a consensus is reached.

### 6) what is glue in cucumber?

**Glue code** is the code that connects a Gherkin step in a `.feature` file to the actual automation code that executes the step. It's your **step definition** files.

In the Cucumber runner class, you use the `glue` option to tell Cucumber where to find these step definition files.

```gherkin
# in login.feature
When the user enters "testuser" and "password123"
```

```java
// in TestRunner.java
@CucumberOptions(
    features = "src/test/resources/features",
    glue = "com/myapp/stepdefinitions" // This is the glue path
)
public class TestRunner {}

// in com/myapp/stepdefinitions/LoginSteps.java (The Glue Code)
public class LoginSteps {
    @When("the user enters {string} and {string}")
    public void userEntersCredentials(String username, String password) {
        // Selenium code to enter username and password goes here
    }
}
```
The `glue` property tells Cucumber to scan the `com.myapp.stepdefinitions` package to find the method annotated with `@When("the user enters {string} and {string}")`.
