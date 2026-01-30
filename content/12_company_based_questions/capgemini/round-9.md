---
title: "Capgemini-9"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

Capgemini L1 virtual , interviewer Lavanya 
------------------------------------------
1. Tell me about yourself, years of experience,your framework 
2. What is interface 
3. What is abstraction 
4. How is the interface different from abstraction 
5. If there are 3 windows, suppose I have to go to the 3rd window and do a click or pass input how to do? 
6. Go to w3s website , go to start learning css  write a xpath to start learning css now , one of one 
 7. Using that xpath locate the previous element 
8. Write a program to maximum salary in a array  
Input int[] salary={20,40,50,10,31}
 9. What all exceptions you have faced in projects how did you handle it 
10. What is Nostaleexception ?
11. Difference between error and exception 
12. Why do we need runner class in cucumber is it really necessary 
13. What is status code 204 
14. Scenario and scenario outlines difference 
15. If I have 20 tests with smoke, 10 with regression and 20 with adoc 
    15.1) how will you run all these test 
    15.2) if I want any test to run first how will you run it 
    15.3) if there is no priority how test will run 

16. What does delete does in http methods 
17. Put and patch difference 
18. Str=Capgemini, 
18.1 what method will you use to get index of 3, 
18.2 if I want to get index of 9 what will happen 
18.3 what method will you use for checking length
18.4 if I'm checking if letter 'k' is present in the string or not what will happen , will it throw error , exception or what will you get ?

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. Tell me about yourself, years of experience,your framework
Standard opener. Focus on professional experience, specific years in automation, and briefly outline your framework (e.g., "Java, TestNG, Selenium, POM, Data-driven, Jenkins for CI/CD").

### 2. What is interface
An interface defines a contract of behavior. It specifies a set of methods that a class *must* implement. In Java, it's used to achieve abstraction and to support multiple inheritance of type.

### 3. What is abstraction
Abstraction is the concept of hiding complex implementation details and showing only the essential features. It helps manage complexity by providing a simplified view of functionality. In Java, this is achieved through abstract classes and interfaces.

### 4. How is the interface different from abstraction
-   **Abstraction** is a *concept* (hiding details).
-   **Interface** is a *mechanism* in Java to achieve 100% abstraction.
    -   An **abstract class** can provide partial implementation and state, and can have constructors.
    -   An **interface** (pre-Java 8) could only have abstract methods and static final variables, defining a pure contract without implementation or state. (Post-Java 8, interfaces can have `default` and `static` methods with implementations).

### 5. If there are 3 windows, suppose I have to go to the 3rd window and do a click or pass input how to do?
You use window handles and iterate through them.
1.  Get all window handles: `Set<String> allHandles = driver.getWindowHandles();`
2.  Convert the `Set` to an `ArrayList` to access by index: `List<String> handlesList = new ArrayList<>(allHandles);`
3.  Switch to the 3rd window (index 2): `driver.switchTo().window(handlesList.get(2));`
4.  Perform actions (click, send input).
5.  Always switch back to the original window when done with the new one.

### 6. Go to w3s website , go to start learning css write a xpath to start learning css now , one of one
(This requires inspecting the w3schools.com website).
Assuming the element is `<a>` tag with text "Start learning CSS now" inside a `<div>` or similar structure.
A possible XPath: `//a[normalize-space()='Start learning CSS now']`
Or, if there are multiple such links and you need a specific one:
`//div[@class='w3-example']/a[text()='Start learning CSS now']`

### 7. Using that xpath locate the previous element
This would involve using XPath axes. If the "Start learning CSS now" link has a previous sibling that you need, you'd use `preceding-sibling::`.
Example: `//a[normalize-space()='Start learning CSS now']/preceding-sibling::h2` (if an `h2` comes before it).

### 8. Write a program to maximum salary in a array Input int[] salary={20,40,50,10,31}
```java
import java.util.Arrays;

public class MaxSalary {
    public static int findMaxSalary(int[] salaries) {
        if (salaries == null || salaries.length == 0) {
            throw new IllegalArgumentException("Salary array cannot be empty or null.");
        }
        // Using Java 8 Streams
        return Arrays.stream(salaries).max().getAsInt();
    }

    public static void main(String[] args) {
        int[] salaries = {20, 40, 50, 10, 31};
        System.out.println("Maximum salary: " + findMaxSalary(salaries)); // Output: 50
    }
}
```

### 9. What all exceptions you have faced in projects how did you handle it
-   **`NoSuchElementException`:** Handled by using robust locators and, more importantly, **explicit waits** before interacting with elements.
-   **`StaleElementReferenceException`:** Handled by re-finding the element just before interaction or by making the explicit waits intelligent enough to re-locate.
-   **`TimeoutException`:** Indicates a genuine application performance issue or a too-short wait. Handled by investigating the application or adjusting the wait time if justified.
-   **`ElementNotInteractableException`:** Usually solved by scrolling the element into view or waiting for it to become enabled/visible.

### 10. What is Nostaleexception ?
This is likely a typo for **`StaleElementReferenceException`**. Explained in previous answers. It occurs when a `WebElement` reference is no longer valid because the element has been detached from the DOM.

### 11. Difference between error and exception
-   **`Error`:** Represents serious problems that an application should not try to catch. They indicate typically unrecoverable conditions, such as `OutOfMemoryError` or `StackOverflowError`.
-   **`Exception`:** Represents conditions that an application might want to catch and handle.
    -   **Checked Exceptions:** (e.g., `IOException`) Compiler forces you to handle them.
    -   **Unchecked Exceptions (Runtime Exceptions):** (e.g., `NullPointerException`) You are not forced to handle them; they often indicate programming errors.

### 12. Why do we need runner class in cucumber is it really necessary
"Yes, a Runner class is necessary in Cucumber. It serves as the **entry point** for executing your Cucumber tests.
-   It tells JUnit (or TestNG) how to run the Cucumber features.
-   It uses the `@CucumberOptions` annotation to configure:
    -   Where to find your `.feature` files.
    -   Where to find your step definitions (`glue` code).
    -   What plugins to use for reporting.
    -   Which specific scenarios to run (using `tags`).
Without a runner class, Cucumber doesn't know how to start or what to execute."

### 13. What is status code 204
`204 No Content`. This indicates that the server has successfully fulfilled the request, but there is no new content to send back in the response body. This is often used for `DELETE` requests or `PUT` requests that don't need to return data.

### 14. Scenario and scenario outlines difference
-   **`Scenario`:** A single, concrete test case that runs once.
-   **`Scenario Outline`:** A template for a scenario that runs multiple times with different sets of data, specified in an `Examples` table.

### 15. If I have 20 tests with smoke, 10 with regression and 20 with adoc
This refers to TestNG groups.

#### 15.1) how will you run all these test
First, annotate your TestNG `@Test` methods with groups:
```java
@Test(groups = "smoke")
public void loginSmokeTest() {}

@Test(groups = "regression")
public void regressionFlow() {}

@Test(groups = "adhoc") // Not a common group, but for example
public void adhocCheck() {}
```
Then, configure your `testng.xml` to include all these groups:
```xml
<suite name="AllTests">
  <test name="AllGroupTests">
    <groups>
      <run>
        <include name="smoke"/>
        <include name="regression"/>
        <include name="adhoc"/>
      </run>
    </groups>
    <classes>
      <class name="com.yourtests.MyTestClass"/>
    </classes>
  </test>
</suite>
```

#### 15.2) if I want any test to run first how will you run it
Use the `priority` attribute in the `@Test` annotation. Tests with lower priority values run first.
`@Test(priority = 0)` will run before `@Test(priority = 1)`.

#### 15.3) if there is no priority how test will run
If no priority is specified, TestNG will run the tests in an **unpredictable order**. While it often appears to be alphabetical by method name, this behavior is not guaranteed and should not be relied upon. For controlled execution, always use `priority` or `dependsOnMethods`.

### 16. What does delete does in http methods
The `DELETE` HTTP method is used to **remove/delete** a specified resource from the server. It should be idempotent.

### 17. Put and patch difference
-   **`PUT`:** Replaces an existing resource entirely with the new data provided in the request body. (Idempotent).
-   **`PATCH`:** Applies a **partial update** to an existing resource. Only the fields provided in the request body are modified. (Not necessarily idempotent).

### 18. Str=Capgemini, 
#### 18.1 what method will you use to get index of 3,
This means getting the character at index 3.
`String str = "Capgemini";`
`char charAtIndex3 = str.charAt(3);` // Output: 'g' (0-indexed)

#### 18.2 if I want to get index of 9 what will happen
`String str = "Capgemini";` (length is 9)
`str.charAt(9);` // This will throw a `StringIndexOutOfBoundsException` because valid indices are 0 to `length()-1`.

#### 18.3 what method will you use for checking length
`String str = "Capgemini";`
`int length = str.length();` // Output: 9

#### 18.4 if I'm checking if letter 'k' is present in the string or not what will happen , will it throw error , exception or what will you get ?
`String str = "Capgemini";`
`str.contains("k");` // This will return `false`. It will not throw an error or exception.
`str.indexOf('k');` // This will return `-1` (indicating not found).
