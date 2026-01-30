---
title: "CTS-2"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

CTS L1 and L2 interview Questions:
-----------------------------------
1) different ways to open url 
2) different keywords under list and set
3) explain about framework 
4) Background 
5) dryrun
6) write xpath and tell about xpath types briefly 
7)write the code for going back current  browser to previous browser.
8)how will u handle windows handle
9) actions and methods
10) r u using take screenshot in ur project 
11)explain Maven tool  and pom xmal 
12)from dialog box ,you need to import the file how u will handle this
13) what's class and interface
14 what's js abstract class
15)Webtable 
16) Move to element 
17)cucumber frame work
17) int [] = [1,0,0,2,0,0,0,3]. Output [1,2,3,0,0,0]
18;how will u handle frames incide frames 
19) cucumber with data table 
20 ) using scenario outline how will you pass the data 
21) where will you pass the testdata .
22)will you pass test data in excel in  your project?
23)will you configure jenkins
24)for click how many ways u ll use in selenium
25) POM

---

## Answers (No-BS Java QA / SDET Explanations)

### 1) different ways to open url
In Selenium, there are two primary ways:
1.  `driver.get("https://www.example.com");`
2.  `driver.navigate().to("https://www.example.com");`

Both achieve the same goal. `navigate()` is part of a larger interface that also allows you to move back, forward, and refresh the page. `get()` is more direct for just loading a URL.

### 2) different keywords under list and set
This likely refers to the **methods** available on `List` and `Set` objects.
-   **`List` Methods:**
    -   `add(element)`: Appends an element.
    -   `get(index)`: Retrieves an element by its index.
    -   `set(index, element)`: Replaces an element at a specific index.
    -   `remove(index)`: Removes an element by its index.
    -   `size()`: Returns the number of elements.
-   **`Set` Methods:**
    -   `add(element)`: Adds an element. Returns `false` if the element is already present.
    -   `remove(element)`: Removes a specific element.
    -   `contains(element)`: Returns `true` if the set contains the element.
    -   `size()`: Returns the number of elements.
    -   `isEmpty()`: Returns `true` if the set is empty.

### 3) explain about framework
Standard question. Describe your automation framework's architecture: its core tools (Java, Selenium, TestNG), design patterns (Page Object Model), data management strategy (JSON/Excel files with `@DataProvider`), reporting tools (ExtentReports), and CI/CD integration (Maven, Jenkins).

### 4) Background
In Cucumber, the `Background` keyword is used to define a series of `Given` steps that run **before every single scenario** in a feature file. It's used to set up a common state or precondition, reducing repetition and making the scenarios cleaner.

### 5) dryrun
`dryRun` is an option in Cucumber's `@CucumberOptions`.
-   `dryRun = true`: When you run the tests, Cucumber will **not** execute the actual step definition code. It will only check that every Gherkin step in your feature files has a corresponding step definition (glue code). This is a quick way to find any undefined steps without running the slow browser tests.
-   `dryRun = false` (default): Cucumber will execute the tests normally.

### 6) write xpath and tell about xpath types briefly
-   **Absolute XPath:**
    -   Starts from the root of the document (`/html`).
    -   Example: `/html/body/div[1]/div/input`
    -   **Bad:** Extremely brittle. Breaks with any UI change. Avoid it.
-   **Relative XPath:**
    -   Starts from anywhere in the document (`//`).
    -   Example: `//input[@id='username']`
    -   **Good:** Flexible and robust. It locates an element based on its own attributes or its relationship to other elements, not its absolute position.

### 7) write the code for going back current browser to previous browser.
You use the `navigate().back()` method.

```java
// Navigate to the first page
driver.get("https://www.google.com");
// Navigate to a second page
driver.get("https://www.bing.com");
// Go back to the previous page (Google)
driver.navigate().back();
```

### 8) how will u handle windows handle
This is about handling multiple browser windows or tabs. You use `driver.getWindowHandle()` for the current window ID, `driver.getWindowHandles()` for all window IDs, and `driver.switchTo().window(handleId)` to switch focus between them.

### 9) actions and methods
The `Actions` class in Selenium is used to build and perform complex user gestures.
-   **Methods:**
    -   `moveToElement(element)`: Simulates a mouse hover.
    -   `click()`: Simulates a click.
    -   `doubleClick()`: Simulates a double click.
    -   `contextClick()`: Simulates a right-click.
    -   `dragAndDrop(source, target)`: Drags an element and drops it on another.
-   **Execution:** You chain these methods to build a sequence and then call `.perform()` to execute it.

### 10) r u using take screenshot in ur project
"Yes, absolutely. We have a custom TestNG listener that implements `onTestFailure`. Whenever a test fails, this listener automatically calls our screenshot utility to capture an image of the browser at the moment of failure. The screenshot is then embedded directly into our ExtentReport for easy debugging."

### 11) explain Maven tool and pom xmal
-   **Maven:** A powerful build automation and project management tool. It standardizes how Java projects are built.
-   **`pom.xml` (Project Object Model):** The central configuration file for a Maven project. Its key purposes are:
    -   **Dependency Management:** Declaring all external libraries (like Selenium, TestNG) the project needs. Maven automatically downloads and manages them.
    -   **Build Configuration:** Defining the build lifecycle and configuring plugins (e.g., the `maven-surefire-plugin` to run tests).

### 12) from dialog box ,you need to import the file how u will handle this
This refers to a file upload. You **do not** interact with the OS-native file dialog box. Instead, you find the hidden `<input type="file">` element on the page and use `sendKeys()` to pass the absolute path of the file to it.

```java
String filePath = "/Users/me/Documents/upload.txt";
WebElement fileInput = driver.findElement(By.cssSelector("input[type='file']"));
fileInput.sendKeys(filePath); // This "uploads" the file
```

### 13) what's class and interface
-   **Class:** A blueprint for creating objects. It can have fields (data) and methods (behavior).
-   **Interface:** A contract. It defines a set of methods that a class *must* implement. It's pure abstraction. A class can `implement` multiple interfaces but can only `extend` one class.

### 14 what's js abstract class
This is likely a typo for "Java abstract class".
-   **Abstract Class:** A class that cannot be instantiated on its own and must be subclassed. It can contain both abstract methods (with no implementation) and concrete methods (with implementation). It's a mix of abstraction and concrete behavior.

### 15) Webtable
A webtable is an HTML `<table>` element. Handling them in Selenium involves:
1.  Locating the table element.
2.  Finding all rows (`<tr>`) within the table: `table.findElements(By.tagName("tr"))`.
3.  Looping through the rows.
4.  For each row, finding all cells (`<td>`): `row.findElements(By.tagName("td"))`.
5.  Extracting text or interacting with elements within the cells.

### 16) Move to element
This refers to the `moveToElement()` method of the `Actions` class, used to simulate a mouse hover.

### 17) cucumber frame work
It's a BDD framework where you write tests in human-readable Gherkin (`.feature` files) that are then linked to Java automation code (step definitions).

### 17) int [] = [1,0,0,2,0,0,0,3]. Output [1,2,3,0,0,0]
This is a "move all zeros to the end" problem.

```java
import java.util.Arrays;

public class MoveZeros {
    public static int[] moveZerosToEnd(int[] arr) {
        if (arr == null) return null;
        int[] result = new int[arr.length];
        int nonZeroIndex = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] != 0) {
                result[nonZeroIndex++] = arr[i];
            }
        }
        return result;
    }
    public static void main(String[] args) {
        int[] input = {1, 0, 0, 2, 0, 0, 0, 3};
        System.out.println(Arrays.toString(moveZerosToEnd(input))); // [1, 2, 3, 0, 0, 0, 0, 0]
        // Note: The original question's output is missing some zeros. The code provides the correct result.
    }
}
```

### 18) how will u handle frames incide frames
You handle nested frames by switching into them one by one.
1.  `driver.switchTo().frame("outerFrame");`
2.  `driver.switchTo().frame("innerFrame");`
3.  Interact with elements in the inner frame.
4.  To get back to the outer frame: `driver.switchTo().parentFrame();`
5.  To get all the way back to the main page: `driver.switchTo().defaultContent();`

### 19) cucumber with data table
A `DataTable` is used to pass a collection of data to a single Gherkin step.
```gherkin
When I create a user with the following data:
  | username | testuser |
  | email    | test@ex.com |
```
In the step definition, you receive this as a `DataTable` object, which you can then convert to a `Map`.

### 20) using scenario outline how will you pass the data
A `Scenario Outline` uses an `Examples` table to pass data. The scenario runs once for each row in the table.

### 21) where will you pass the testdata .
In a well-designed framework, test data is stored externally, not hardcoded.
-   **Configuration data:** in `.properties` files.
-   **Test case data:** in **JSON** or **Excel** files. This data is then read by a `@DataProvider` (TestNG) or within the step definition (Cucumber).

### 22) will you pass test data in excel in your project?
"Yes, in a previous project, we used Excel for our test data. We used the **Apache POI** library to read the `.xlsx` files from within our TestNG `@DataProvider` methods. This allowed our manual testers and BAs to easily contribute to the test data pool."

### 23) will you configure jenkins
"Yes, I have experience configuring Jenkins jobs for our automation suite. I've created and managed pipeline jobs, configured them to pull from our Git repository, set up build triggers, and defined the build steps using a `Jenkinsfile` to execute our Maven test commands."

### 24) for click how many ways u ll use in selenium
1.  **`element.click()`:** The standard, most common way.
2.  **`actions.click(element).perform()`:** Using the `Actions` class.
3.  **`javascriptExecutor.executeScript("arguments[0].click();", element)`:** A forceful click using JavaScript, used when a standard click is intercepted or fails.
4.  **`element.sendKeys(Keys.ENTER)`:** For submit buttons or links, sending the Enter key can sometimes work as a click.

### 25) POM
Page Object Model. A design pattern that separates UI interaction logic from test script logic by creating a class for each page of the application.
