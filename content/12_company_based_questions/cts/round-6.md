---
title: "CTS-6"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

CTS L1 and L2 interview 
-----------------------
1Explain waits concepts
2)explain testng reports
3)Explain frames handling in ur project
4)Explain webtable comcept in ur project
5)Use scanner and collection and get unique values and print this
6)Write a program for reverse string with palindrome 
7) write a syntax for window handles 
8)without using drag and drop how u ll swap the values
9)write the 
Syntex for select class
10)write a program for getting maximum and minimum values
11)chaining concept
12)what will u use under abstract  and interface ,which is best
13)if I select u in my team wt is ur first approach
14) have u extend and work in the project 
15)Maven sure fire plugin used for?
16) CI CD?
17)difference between set and map
18) testng annotations
19)Iretry analyser used for?
20)selenium 3 and 4 difference?
21) how many times
 U will do regression per year 
22)In regression how many test cases  u will run and how long it will take to run using jenkins on daily basis

---

## Answers (No-BS Java QA / SDET Explanations)

### 1) Explain waits concepts
Waits are crucial for handling synchronization issues in Selenium due to the asynchronous nature of web applications.
-   **Implicit Wait (Bad):** A global setting that implicitly polls the DOM for elements. Avoid it as it masks timing issues and slows down tests.
-   **Explicit Wait (Good):** (`WebDriverWait` with `ExpectedConditions`) Waits for a *specific condition* to be met for an element (e.g., element is clickable). This is the recommended practice for stable tests.
-   **Fluent Wait (Advanced Explicit Wait):** A more configurable version of Explicit Wait, allowing custom polling intervals and exceptions to ignore.

### 2) explain testng reports
TestNG generates basic HTML and XML reports in the `test-output` folder by default. These provide a summary of pass/fail/skip and detailed logs. For more professional and visually rich reports, third-party libraries like **ExtentReports** or **Allure Reports** are integrated via TestNG listeners.

### 3) Explain frames handling in ur project
"In our project, when dealing with `iframe`s, we ensure that before interacting with any elements inside a frame, we explicitly switch Selenium's context into that frame using `driver.switchTo().frame("frameNameOrId")` or `driver.switchTo().frame(index)`. After completing interactions within the frame, we always switch back to the default content of the page using `driver.switchTo().defaultContent()` to avoid issues with subsequent element searches."

### 4) Explain webtable comcept in ur project
"In our project, we often encounter web tables. Our approach for handling them involves:
1.  **Locating the Table:** Finding the main `<table>` element.
2.  **Iterating Rows:** Getting all `<tr>` elements within the table (`table.findElements(By.tagName("tr"))`).
3.  **Iterating Cells:** For each row, getting all `<td>` (data cells) or `<th>` (header cells) (`row.findElements(By.tagName("td"))`).
4.  **Data Extraction/Verification:** Extracting text using `.getText()` from cells or interacting with elements located within specific cells.
5.  **Dynamic Access:** We often use dynamic XPath to locate specific rows based on content (e.g., `//tr[td[text()='ExpectedValue']]`) and then navigate to a specific cell within that row."

### 5) Use scanner and collection and get unique values and print this
```java
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

public class UniqueValuesScanner {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<String> inputValues = new ArrayList<>();
        System.out.println("Enter values (type 'done' to finish):");

        while (true) {
            String input = scanner.nextLine();
            if (input.equalsIgnoreCase("done")) {
                break;
            }
            inputValues.add(input);
        }
        scanner.close();

        Set<String> uniqueValues = new HashSet<>(inputValues); // Collections to get unique values
        
        System.out.println("\nUnique values entered:");
        uniqueValues.forEach(System.out::println);
    }
}
```

### 6) Write a program for reverse string with palindrome
```java
public class StringReversePalindrome {
    public static String reverseString(String str) {
        if (str == null) return null;
        return new StringBuilder(str).reverse().toString();
    }

    public static boolean isPalindrome(String str) {
        if (str == null || str.isEmpty()) return false;
        String cleanedStr = str.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        return cleanedStr.equals(reverseString(cleanedStr));
    }

    public static void main(String[] args) {
        String testStr = "madam";
        String reversed = reverseString(testStr);
        System.out.println("Original: " + testStr + ", Reversed: " + reversed);
        System.out.println("Is Palindrome? " + isPalindrome(testStr)); // true
        
        testStr = "hello";
        reversed = reverseString(testStr);
        System.out.println("Original: " + testStr + ", Reversed: " + reversed);
        System.out.println("Is Palindrome? " + isPalindrome(testStr)); // false
    }
}
```

### 7) write a syntax for window handles
-   `String currentWindowHandle = driver.getWindowHandle();` (gets the unique ID of the current window/tab).
-   `Set<String> allWindowHandles = driver.getWindowHandles();` (gets a set of all unique IDs of currently open windows/tabs).
-   `driver.switchTo().window(targetWindowHandle);` (switches the driver's focus to the window identified by `targetWindowHandle`).

### 8) without using drag and drop how u ll swap the values
This question is ambiguous.
-   **Swapping numbers without a third variable:** This is a coding riddle. (e.g., `a = a + b; b = a - b; a = a - b;`)
-   **Swapping elements on a UI without `Actions.dragAndDrop()`:** This would require using `JavascriptExecutor` to manipulate the DOM directly, which is generally not recommended for testing as it bypasses user interaction. A typical approach would be to simulate a `mousedown`, `mousemove`, and `mouseup` sequence if `Actions` is explicitly disallowed and `JavascriptExecutor` is allowed.

### 9)write the Syntex for select class
```java
import org.openqa.selenium.support.ui.Select;
// ...
WebElement dropdownElement = driver.findElement(By.id("mySelectDropdown"));
Select select = new Select(dropdownElement);
select.selectByVisibleText("Option Text"); // Or selectByValue("value") or selectByIndex(index)
```

### 10)write a program for getting maximum and minimum values
```java
import java.util.Arrays;

public class MaxMinArray {
    public static void findMaxMin(int[] arr) {
        if (arr == null || arr.length == 0) {
            System.out.println("Array is empty or null.");
            return;
        }
        int min = Arrays.stream(arr).min().getAsInt();
        int max = Arrays.stream(arr).max().getAsInt();
        System.out.println("Min: " + min + ", Max: " + max);
    }
}
```

### 11)chaining concept
"Chaining" refers to the practice of calling multiple methods on the same object in a single statement, where each method returns the object itself (or a related builder object). This creates a fluent, readable API.
-   **Example in REST-assured:** `given().when().get("/users").then().statusCode(200);`
-   **Example in Selenium Actions:** `new Actions(driver).moveToElement(el1).click(el2).perform();`

### 12)what will u use under abstract and interface ,which is best
Neither is inherently "best"; they serve different purposes.
-   **Abstract Class:** Use when you want to provide a common base for subclasses, including some default implementations, but also want to enforce that certain methods must be implemented by subclasses. A class can extend only one abstract class.
-   **Interface:** Use when you want to define a contract for behavior. A class can implement multiple interfaces. Ideal for defining capabilities.
-   **In my project:** "I use **abstract classes** (e.g., `BaseTest`, `BasePage`) to provide common setup, teardown, and utility methods that are inherited by all my test classes and page objects. I use **interfaces** when I need to define a contract for a specific capability, like a `ConfigReader` interface that can be implemented by `ExcelConfigReader` or `JsonConfigReader`."

### 13)if I select u in my team wt is ur first approach
"My first approach would be to:
1.  **Understand the Product:** Gain a deep understanding of the application under test, its business domain, and key user flows.
2.  **Familiarize with the Team and Process:** Understand the team's agile process, communication channels, and current sprint goals.
3.  **Review the Existing Test Automation Framework:** Dive into the existing framework code, architecture, tools, and test suites. Identify areas for potential improvement or any immediate gaps.
4.  **Start Contributing:** Begin by automating or maintaining existing test cases, familiarizing myself with the codebase, and actively participating in team meetings."

### 14) have u extend and work in the project
This question is a bit unclear, possibly "have you extended and worked in the project" or "have you extended the framework and worked on the project".
Assuming "extended the framework": "Yes, I have significantly extended and enhanced our test automation framework. For instance, I added a custom reporting module to integrate ExtentReports, implemented a more robust explicit wait utility, and developed a test data management system to read data from external JSON files."

### 15)Maven sure fire plugin used for?
The `maven-surefire-plugin` is used to **run unit tests** (and typically integration tests if they are configured as unit tests) during the `test` phase of the Maven build lifecycle. It supports JUnit and TestNG. It generates XML and HTML test reports.

### 16) CI CD?
-   **CI (Continuous Integration):** Developers frequently merge code into a central repository, triggering automated builds and tests to find integration issues early.
-   **CD (Continuous Delivery/Deployment):** Automating the release process, either to staging environments (Delivery) or directly to production (Deployment), after successful CI.

### 17)difference between set and map
-   **`Set`:** A collection of unique elements. Unordered.
-   **`Map`:** A collection of key-value pairs. Keys must be unique. Values can be duplicates.

### 18) testng annotations
`@Test`, `@BeforeSuite`, `@AfterSuite`, `@BeforeTest`, `@AfterTest`, `@BeforeClass`, `@AfterClass`, `@BeforeMethod`, `@AfterMethod`, `@DataProvider`, `@Parameters`.

### 19)Iretry analyser used for?
The `IRetryAnalyzer` interface in TestNG is used to **automatically re-run failed test cases** a specified number of times. It helps reduce test flakiness caused by transient issues (e.g., network glitches, UI rendering delays).

### 20)selenium 3 and 4 difference?
-   **W3C WebDriver Protocol:** Selenium 4 is fully W3C compliant; Selenium 3 used JSON Wire Protocol.
-   **Relative Locators:** New in Selenium 4 (`toLeftOf`, `above`, etc.).
-   **Improved Grid:** Easier setup, better Docker support in Selenium 4.
-   **Chrome DevTools Protocol:** Native integration in Selenium 4 for advanced browser interactions.

### 21) how many times U will do regression per year
"We run our full automated regression suite at least **once per sprint** (every two weeks) and as part of every major release cycle. For critical code changes, a targeted regression suite might be run more frequently."
(Provide your actual numbers if different).

### 22)In regression how many test cases U will run and how long it will take to run using jenkins on daily basis
"Our full regression suite contains approximately **500-600 automated test cases**. When run in parallel on our Selenium Grid via Jenkins, it takes about **45-60 minutes** to complete. This allows us to get quick feedback on the health of our application."
(Provide your actual numbers if different).
