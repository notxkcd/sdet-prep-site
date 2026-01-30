---
title: "Capgemini-13"
date: 2026-01-30
draft: false
---

---

## Original Questions

Capgemini 1st Round Interview Questions:
-----------------------------------------
1.self introduction
2. Cucumber framework
3. static method and how to call in another class
4.interface
5.final keyword
6. have you integrate Jenkins in your project
7.git commands for code push and code pull
8. what getWindowhandles method will return?
9.what is query parameter and path parameter?
10.how will you call global variable in API?
11.http methods?
12.Coding:
int a=123454644;
int b=4;  occurrence of b in a , count and index number.
13.TakeScreenshot method
14.how will you take the screenshot for failed test cases alone in cucumber framework
15.how will you take the screenshot for full page.
16.git conflict

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. self introduction
Standard opener. Keep it concise, professional, and focus on your relevant experience (automation skills, tech stack, achievements).

### 2. Cucumber framework
A BDD framework that uses Gherkin (`Given/When/Then`) to describe application behavior in `.feature` files, which are then linked to executable code (step definitions) written in Java. Promotes collaboration and living documentation.

### 3. static method and how to call in another class
-   **`static` method:** A method that belongs to the class itself, not to any specific object of the class.
-   **How to call:** You call a static method directly using the class name, without needing to create an object of that class.
    ```java
    public class MyUtils {
        public static void helperMethod() {
            System.out.println("This is a static helper method.");
        }
    }
    // To call from another class:
    MyUtils.helperMethod();
    ```

### 4. interface
An interface defines a contract of abstract methods that a class `implements`. It's used to achieve abstraction and support multiple inheritance of type.

### 5. final keyword
A modifier that makes a variable a constant, a method non-overridable, or a class non-extendable.

### 6. have you integrate Jenkins in your project
"Yes, I have integrated Jenkins into my project. I've configured Jenkins jobs (pipelines) to pull code from our Git repository, automatically build the project with Maven, and execute our automated test suites on every code commit. This provides continuous integration and immediate feedback on the quality of our code."

### 7. git commands for code push and code pull
-   **`git push origin <branch_name>`:** Uploads local commits to the remote repository.
-   **`git pull origin <branch_name>`:** Fetches new commits from the remote repository and merges them into the current local branch.

### 8. what getWindowhandles method will return?
`driver.getWindowHandles()` returns a `Set<String>`. This `Set` contains unique string IDs (handles) for all currently open browser windows or tabs controlled by the WebDriver instance.

### 9. what is query parameter and path parameter?
-   **Query Parameters:** Key-value pairs appended to a URL after a `?`, used for filtering, sorting, or providing optional parameters (e.g., `/products?category=electronics&sort=price`).
-   **Path Parameters:** Variables embedded directly within the URL path, used to identify a specific resource or resource hierarchy (e.g., `/users/{userId}/orders/{orderId}`).

### 10. how will you call global variable in API?
In API testing, "global variable" often refers to a variable defined in a tool like Postman that is accessible across all requests in a collection or environment. In REST-assured (Java), if you have global configuration like a base URI or API key, you'd typically manage it in a configuration class (e.g., a `ConfigReader`) and access it via Java methods. You can also define them using `RestAssured.baseURI`, `RestAssured.port`, etc.

### 11. http methods?
The standard verbs for HTTP requests: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`.

### 12. Coding: int a=123454644; int b=4; occurrence of b in a , count and index number.
```java
public class NumberDigitOccurrences {
    public static void findOccurrences(int number, int digitToFind) {
        String numStr = String.valueOf(number);
        char charToFind = String.valueOf(digitToFind).charAt(0);

        int count = 0;
        StringBuilder indices = new StringBuilder();

        for (int i = 0; i < numStr.length(); i++) {
            if (numStr.charAt(i) == charToFind) {
                count++;
                indices.append(i).append(" ");
            }
        }
        System.out.println("Number: " + number + ", Digit to find: " + digitToFind);
        System.out.println("Occurrence count: " + count); // Output: 4 for digit 4
        System.out.println("Indices: " + indices.toString().trim()); // Output: 4 7 8 9 (if 4s are at those indices)
    }

    public static void main(String[] args) {
        findOccurrences(123454644, 4); // Example: a=123454644, b=4
    }
}
```

### 13. TakeScreenshot method
```java
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import java.io.File;
import java.io.IOException;
import org.apache.commons.io.FileUtils; // Requires Apache Commons IO

public void captureScreenshot(WebDriver driver, String filePath) {
    File srcFile = ((TakesScreenshot) driver).getScreenshotAs(OutputType.FILE);
    try {
        FileUtils.copyFile(srcFile, new File(filePath));
    } catch (IOException e) {
        e.printStackTrace();
    }
}
```

### 14. how will you take the screenshot for failed test cases alone in cucumber framework
This is usually handled by integrating with TestNG/JUnit listeners.
1.  **Cucumber `@After` Hook:** In a Cucumber `@After` hook (which runs after each scenario), you check `Scenario.isFailed()`. If true, you call your screenshot utility.
    ```java
    @After
    public void tearDown(Scenario scenario) {
        if (scenario.isFailed()) {
            final byte[] screenshot = ((TakesScreenshot) driver).getScreenshotAs(OutputType.BYTES);
            scenario.attach(screenshot, "image/png", "failure_screenshot"); // Embed in Cucumber report
            // Also save to file using FileUtils if needed
        }
        if (driver != null) driver.quit();
    }
    ```
2.  **TestNG `ITestListener`:** If using TestNG as your Cucumber runner, you can implement `ITestListener`'s `onTestFailure()` method, which is specifically designed for this.

### 15. how will you take the screenshot for full page.
Using a third-party library like **AShot**.
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

### 16. git conflict
A Git conflict occurs when changes to the same lines of code in a file are made in different branches, and Git cannot automatically merge them. Manual resolution is required.
