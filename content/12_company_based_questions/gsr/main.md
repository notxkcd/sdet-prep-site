---
title: "GSR"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

- GSR-Interview questions-L2
---------------------------
1.how to round decimal without using any methods
2.static import
3.count the repeated character count
4.reverse the number
5.declare the 2d array and transpose the array
6.sprint refinement
7.you are in current sprint, you receive new build that time what test you prefere.
8.status codes
9.put,post methods 
10.header request and header response
11.Thirtparty API not available that time how you test
12.API-Testing-mocker 
13.Difference b/w Assert anf verify
14.cucumber options 
15.Project folder stracture
16.why constructor can't be override?reason?
17.without sendkeys how to pass values?syntax
18.getWindowHandles return type and syntax?
19.how to you raise bug?what are all the steps you follow?
20.what are all the interfaces using in your project
21.Explain Wait concept in java 
22.Explain checked and unchecked Exception 
23.In your project bug will find at production side ,how will you handle.

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. how to round decimal without using any methods
This is a trick question. You can't meaningfully round a decimal *value* without using a method or a cast. The interviewer might be looking for a simple type-casting solution to truncate the decimal.

```java
double d = 10.75;
int roundedDown = (int) d; // This truncates, not rounds. Result is 10.
```
A more "manual method" way to round to the nearest integer:
```java
int rounded = (int) (d + 0.5); // Result is 11.
```
The correct answer is to show you know this is a riddle and that in real code, you'd use `Math.round()`. "In production code, I would always use `Math.round()` for clarity and correctness. To answer the riddle, you could add 0.5 and cast to an `int` to simulate rounding."

### 2. static import
A `static import` allows you to import `static` members (fields and methods) of a class directly into your code, so you can call them without specifying the class name.
-   **Without static import:** `Assert.assertEquals(actual, expected);`
-   **With static import:**
    ```java
    import static org.testng.Assert.assertEquals;
    
    // ... later in the code
    assertEquals(actual, expected); // No need for "Assert."
    ```
It can make code more concise, but overusing it can make it harder to read by obscuring where methods are coming from.

### 3. count the repeated character count
This means finding the frequency of each character. A `Map` is the standard solution.

```java
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;

public class CharCounter {
    public void countChars(String str) {
        Map<Character, Long> frequencies = str.chars()
            .mapToObj(c -> (char) c)
            .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
        
        frequencies.forEach((character, count) -> {
            if (count > 1) {
                System.out.println("'" + character + "' repeated " + count + " times.");
            }
        });
    }
}
```

### 4. reverse the number
Use modulo and division arithmetic.

```java
public int reverseNumber(int num) {
    int reversed = 0;
    while (num != 0) {
        int digit = num % 10;
        reversed = reversed * 10 + digit;
        num /= 10;
    }
    return reversed;
}
```

### 5. declare the 2d array and transpose the array
-   **Declaration:** `int[][] matrix = { {1, 2, 3}, {4, 5, 6} };`
-   **Transpose:** Swapping rows with columns. The element at `[i][j]` moves to `[j][i]`.

```java
public int[][] transpose(int[][] matrix) {
    int rows = matrix.length;
    int cols = matrix[0].length;
    int[][] transposedMatrix = new int[cols][rows];

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            transposedMatrix[j][i] = matrix[i][j];
        }
    }
    return transposedMatrix;
}
```

### 6. sprint refinement
Also known as **Backlog Grooming**. It's a meeting where the team reviews upcoming items in the product backlog to clarify requirements, add details, and provide initial estimates. This ensures stories are "ready" for future sprints.

### 7. you are in current sprint, you receive new build that time what test you prefere.
When a new build is deployed to the QA environment, the first thing to do is a **Smoke Test**. It's a quick, high-level test of the most critical functionalities to ensure the build is stable and "testable." If the smoke test fails, the build is rejected, and no further testing is wasted on it.

### 8. status codes
Standard HTTP response codes (e.g., `200 OK`, `201 Created`, `404 Not Found`, `500 Internal Server Error`).

### 9. put,post methods
-   `POST`: To **create** a new resource.
-   `PUT`: To **replace/update** an existing resource completely.

### 10. header request and header response
-   **Request Headers:** Metadata sent by the client to the server (e.g., `Content-Type`, `Authorization`, `Accept`).
-   **Response Headers:** Metadata sent by the server back to the client (e.g., `Content-Type`, `Content-Length`, `Date`).

### 11. Thirtparty API not available that time how you test
You use **API mocking** or **stubbing**.
You create a mock server that simulates the third-party API. This mock server is configured to return predefined responses (success, error, etc.) when your application calls it. This allows you to test your application's logic in isolation, verifying how it handles different responses from the dependency without needing the actual third-party service to be available.

### 12. API-Testing-mocker
This directly follows the previous question.
"A 'mocker' or mock server is a tool used in API testing to simulate a real API. Tools like **WireMock**, **MockServer**, or even Postman's built-in mocking feature allow you to create a fake API endpoint. You can program it to listen for specific requests and return specific, predictable responses. This is essential for isolating your application and testing how it behaves when a dependency is unavailable or returns an error."

### 13. Difference b/w Assert anf verify
-   **Assert (Hard Assert):** Immediately fails the test and stops execution. Use for critical checks.
-   **Verify (Soft Assert):** Records the failure but allows the test to continue. All failures are reported at the end. Use for non-critical checks where you want to see all failures at once. Implemented in TestNG via the `SoftAssert` class.

### 14. cucumber options
The `@CucumberOptions` annotation on a runner class configures the test run. Key options include `features`, `glue`, `tags`, and `plugin`.

### 15. Project folder stracture
Describe your standard Maven project structure: `src/test/java` for test code (runners, step definitions, page objects), `src/test/resources` for non-code assets (feature files, config, test data), and the `pom.xml` at the root.

### 16. why constructor can't be override?reason?
Constructors are not regular methods; they are special code blocks for creating and initializing an object.
-   **Reason:** Overriding is about changing the behavior of an inherited method in a child class. A constructor's job is to initialize the object of its *own* class. A child class has its own constructor to initialize itself. The child's constructor *can* call the parent's constructor using `super()`, but it cannot override it. Also, overriding relies on runtime polymorphism, but constructors are resolved at compile time.

### 17. without sendkeys how to pass values?syntax
You can use `JavascriptExecutor`. This is a backdoor that directly manipulates the DOM.

```java
WebElement element = driver.findElement(By.id("myInput"));
JavascriptExecutor js = (JavascriptExecutor) driver;
js.executeScript("arguments[0].value='myValue';", element);
```
This should only be used if `sendKeys()` is not working for some reason.

### 18. getWindowHandles return type and syntax?
-   **Return Type:** `Set<String>`
-   **Syntax:** `Set<String> allWindowHandles = driver.getWindowHandles();`
It returns a set of unique string IDs for all currently open browser windows/tabs.

### 19. how to you raise bug?what are all the steps you follow?
"I raise bugs in Jira. The steps are:
1.  Verify the bug is reproducible and not a duplicate.
2.  Click 'Create' and select 'Bug' as the issue type.
3.  Write a clear, concise **Title**.
4.  In the **Description**, provide detailed **Steps to Reproduce**.
5.  Clearly state the **Expected Result** vs. the **Actual Result**.
6.  Provide **Environment Details** (Browser, OS, App Version).
7.  **Attach evidence**: Screenshots, videos, and relevant log files.
8.  Assign a **Severity** and link it to the relevant user story."

### 20. what are all the interfaces using in your project
"In our Selenium framework, we use several core interfaces:
-   `WebDriver`: The main interface for browser interaction.
-   `WebElement`: To represent HTML elements.
-   `TakesScreenshot`: For capturing screenshots.
-   `JavascriptExecutor`: For running JavaScript.
In our framework design, we've also created our own interfaces, like an `IConfigReader` interface, to allow for different implementations of configuration reading (e.g., from properties files vs. JSON)."

### 21. Explain Wait concept in java
In the context of multi-threading, `wait()`, `notify()`, and `notifyAll()` are methods from the `Object` class used for inter-thread communication. A thread can call `wait()` on an object to pause its execution and release the lock on that object. It will only wake up when another thread calls `notify()` or `notifyAll()` on the *same object*. This is a low-level concurrency mechanism.

### 22. Explain checked and unchecked Exception
-   **Checked Exception:** An exception that the compiler forces you to handle (with `try-catch` or `throws`). They represent predictable problems (e.g., `IOException`, `SQLException`).
-   **Unchecked Exception (Runtime Exception):** An exception you are not required to handle. They usually represent programming errors (e.g., `NullPointerException`, `ArrayIndexOutOfBoundsException`).

### 23. In your project bug will find at production side ,how will you handle.
"When a production bug is found, the response needs to be immediate and systematic.
1.  **Acknowledge and Verify:** First, I would immediately try to reproduce the bug in the production and staging environments to confirm its validity and understand its scope.
2.  **Triage & Communication:** I'd work with the team to assess its severity and impact on users. This information is communicated immediately to the Product Manager and stakeholders to decide on a course of action (e.g., hotfix, rollback).
3.  **Root Cause Analysis (Post-Fix):** Once the immediate fire is out, we conduct a thorough RCA to understand *why* the bug was missed. Was there a gap in our test cases? Did our regression suite not cover this scenario?
4.  **Improve the Process:** Based on the RCA, I would update our test suite. I'd write a new automated regression test that specifically covers this bug to ensure it never happens again."
