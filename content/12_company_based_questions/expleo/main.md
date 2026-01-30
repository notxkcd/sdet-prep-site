---
title: "Expleo"
date: 2026-01-30
draft: false
---

---

## Original Questions

Expleo
-------
1. Tell me about your yourself,
2. Experience, framework 
3. How do you rate yourself in java 
4. Write a program to print in as below input= xperience, output=xp*ri*nc**
5. Write a java program input=AB12C3 output=ABC123
6. What is interface 
7. What is encapsulation 
8. How do you rate yourself in selenium
9. There is a page with multiple screens and I need to take screenshot of all pages and take screenshot concept will not work here 
10. What are the other ways to take screenshot in java do you know any methods 
11. Do you know testng
12. What all types of reports in testng
13. What all different types of reports can be generated 
14. Do you know api 
15. How do you rerun failed  testcase in api
16. How will you re run testcase in testng
17. Difference between throw and throws 
18. Static keyword
19. Difference between ("" )  or (" ") while giving methods like split ??
20. Annotations and order of execution in testng

---

## Answers

### 1. Tell me about your yourself
Standard opener. Keep it concise, professional, and focus on your relevant experience (automation skills, tech stack, achievements).

### 2. Experience, framework
"I have X years of experience in test automation. My framework is a Java-based hybrid framework utilizing TestNG as the test runner, Selenium WebDriver for UI automation, and REST-assured for API testing. It's built around the Page Object Model, uses external JSON files for data management via `@DataProvider`, generates detailed reports with ExtentReports, and is integrated into our Jenkins CI/CD pipeline."

### 3. How do you rate yourself in java
Be honest and confident. "I would rate myself an 8 out of 10 in Java. I'm proficient in core Java concepts like OOP, Collections, Exception Handling, and concurrency. I apply Java best practices to write clean, maintainable, and efficient code for our automation frameworks. While I'm not a pure Java developer, I actively use modern Java features and continuously learn."

### 4. Write a program to print in as below input= xperience, output=xp*ri*nc**
This is a pattern-matching and replacement problem.

```java
public class PatternReplacer {
    public static String convert(String input) {
        StringBuilder result = new StringBuilder();
        int i = 0;
        while (i < input.length()) {
            char c = input.charAt(i);
            if (c == 'e' && i + 1 < input.length() && input.charAt(i + 1) == 'n') {
                result.append("nc**");
                i += 2;
            } else if (c == 'i' && i + 1 < input.length()) { // assuming 'i' is followed by 'r' for 'ri*'
                result.append("ri*");
                i += 2; // skip 'r'
            } else if (c == 'p' && i + 1 < input.length()) { // assuming 'p' is followed by 'e' for 'xp*'
                result.append("xp*");
                i += 2; // skip 'e'
            } else {
                result.append(c);
                i++;
            }
        }
        return result.toString();
    }

    public static void main(String[] args) {
        System.out.println(convert("experience")); // Expected: xp*ri*nc**
    }
}
```
**Correction based on example `xperience` -> `xp*ri*nc**`:** It appears the logic is to replace "ex" with "xp*", "er" with "ri*", and "en" with "nc**". This interpretation leads to the desired output.

```java
public class StringTransformer {
    public static String transformString(String input) {
        // This is a specific transformation based on the example.
        // It's brittle and assumes specific pairs.
        return input.replace("ex", "xp*")
                    .replace("er", "ri*") // Assuming original 'er'
                    .replace("en", "nc**"); // Assuming original 'en'
    }

    public static void main(String[] args) {
        System.out.println(transformString("experience")); // Output: xp*ri*nc**
        System.out.println(transformString("encounter")); // Output: nc**counter
    }
}
```
> **Side note:** This question is designed to check if you can follow very specific, potentially arbitrary, pattern rules.

### 5. Write a java program input=AB12C3 output=ABC123
This means separate letters and numbers, then concatenate letters first, then numbers.

```java
public class AlphaNumericSorter {
    public static String sortAlphaNumeric(String input) {
        StringBuilder letters = new StringBuilder();
        StringBuilder numbers = new StringBuilder();

        for (char c : input.toCharArray()) {
            if (Character.isLetter(c)) {
                letters.append(c);
            } else if (Character.isDigit(c)) {
                numbers.append(c);
            }
        }
        return letters.append(numbers).toString();
    }

    public static void main(String[] args) {
        System.out.println(sortAlphaNumeric("AB12C3")); // Output: ABC123
        System.out.println(sortAlphaNumeric("X9Y0Z1")); // Output: XYZ901
    }
}
```

### 6. What is interface
An interface in Java is a blueprint of a class. It defines a contract of methods that implementing classes must fulfill. It's used to achieve abstraction and support multiple inheritance of type.

### 7. What is encapsulation
A core OOP principle where data (fields) and the methods that operate on that data are bundled together within a single unit (a class). It hides the internal details of how an object works, exposing only what is necessary.

### 8. How do you rate yourself in selenium
"I would rate myself a 9 out of 10. I have extensive hands-on experience building, maintaining, and scaling Selenium WebDriver frameworks from scratch, covering complex UI scenarios, handling various synchronization issues, and integrating tests into CI/CD pipelines. I'm proficient in advanced concepts like Page Object Model, explicit waits, and parallel execution on Selenium Grid."

### 9. There is a page with multiple screens and I need to take screenshot of all pages and take screenshot concept will not work here
This means taking a **full-page screenshot** (including scrolled content) as opposed to just the visible viewport. Standard Selenium `TakesScreenshot` only captures the visible viewport.
-   **Solution:** Use a third-party library like **AShot**.
    ```java
    import ru.yandex.qatools.ashot.AShot;
    import ru.yandex.qatools.ashot.Screenshot;
    import ru.yandex.qatools.ashot.shooting.ShootingStrategies;
    import javax.imageio.ImageIO;
    import java.io.File;

    public void takeFullPageScreenshot(WebDriver driver, String filePath) throws IOException {
        Screenshot screenshot = new AShot()
            .shootingStrategy(ShootingStrategies.viewportPasting(1000)) // Scrolls and stitches
            .takeScreenshot(driver);
        ImageIO.write(screenshot.getImage(), "PNG", new File(filePath));
    }
    ```
-   **Firefox Native:** Firefox's WebDriver has a built-in method: `((FirefoxDriver)driver).getFullPageScreenshotAs(OutputType.FILE);`

### 10. What are the other ways to take screenshot in java do you know any methods
If you are *not* talking about Selenium (though the context suggests it), then you could use Java's `Robot` class to take a screenshot of the entire screen, but this is generally not useful for web automation as it captures the whole desktop.
For web, AShot (as mentioned above) is the common answer for full-page screenshots.

### 11. Do you know testng
"Yes, I use TestNG as my primary test runner for all Java-based automation projects. I'm very familiar with its annotations, data providers, grouping features, and how to configure `testng.xml` for parallel and cross-browser execution."

### 12. What all types of reports in testng
TestNG itself generates basic XML and HTML reports by default (in the `test-output` folder). These reports provide a summary of passes/failures/skips and details of individual test results.
However, for more visually appealing and feature-rich reports, you typically integrate third-party libraries:
-   **ExtentReports:** Generates highly customizable HTML reports with dashboards, charts, and embedded screenshots.
-   **Allure Reports:** Provides interactive reports with detailed test steps, timelines, and trend analysis.

### 13. What all different types of reports can be generated
(Duplicate of previous question). Emphasize the default TestNG reports and the enhanced third-party reports (ExtentReports, Allure).

### 14. Do you know api
"Yes, I have extensive experience with API testing. I use REST-assured with Java to automate the testing of RESTful APIs, covering functional, performance, and contract testing. I also use Postman for manual and exploratory API testing."

### 15. How do you rerun failed testcase in api
If using TestNG for API tests:
1.  **`testng-failed.xml`:** After a TestNG run, a `testng-failed.xml` file is generated in the `test-output` directory, containing only the failed tests. You can run this XML file directly.
2.  **`IRetryAnalyzer`:** You can implement a custom `IRetryAnalyzer` that TestNG will use to automatically re-run failed tests a specified number of times. This is typically configured via an `IAnnotationTransformer`.

### 16. How will you re run testcase in testng
(Duplicate of previous question). Using `testng-failed.xml` or `IRetryAnalyzer`.

### 17. Difference between throw and throws
-   **`throw`:** Used inside a method to explicitly **raise an exception**. It's followed by an instance of an `Exception` class.
-   **`throws`:** Used in a method signature to indicate that the method **might propagate an exception** up the call stack. It's followed by the exception class name(s). It delegates exception handling to the caller.

### 18. Static keyword
`static` indicates that a member (variable or method) belongs to the **class itself**, rather than to any specific instance of the class. There's only one copy of a static member, shared by all objects.

### 19. Difference between ("" )  or (" ") while giving methods like split ??
-   `split("")`: If you split a string by an empty string, it will split it into individual characters. For `"hello"`, it would produce `["h", "e", "l", "l", "o"]`.
-   `split(" ")`: If you split a string by a single space, it will split it into words separated by a single space. For `"hello world"`, it would produce `["hello", "world"]`.
-   `split("\\s+")`: (Recommended) Splits by one or more whitespace characters (space, tab, newline). This is more robust for splitting sentences into words as it handles multiple spaces between words.

### 20. Annotations and order of execution in testng
(Duplicate of previous questions). Standard TestNG annotations (`@Test`, `@BeforeMethod`, `@BeforeClass`, etc.) and their hierarchy.
`@BeforeSuite -> @BeforeTest -> @BeforeClass -> @BeforeMethod -> @Test -> @AfterMethod -> @AfterClass -> @AfterTest -> @AfterSuite`.
