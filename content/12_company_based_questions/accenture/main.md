---
title: "Accenture"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

Accenture interview questions
-----------------------------
1.tell about urself
2.explain about project and framework used in project?why using cucumber ,why not testng?
3.how to passing data from excel?what are the steps to use excel in eclipse?
4.what are the criticalbugs u found in ur project ?
5. do u have any idea API testing and Appium tool?
6.what will u do if developer wont accept the bug and how will u manage this situation? 

Java

1.difference between == and .equals?
2.what is abstraction  and explain?
3.what is different between throw and throws?
4.String s="Selenium";

tell a logic for this output "Slnium"

Selenium

1.Which version of selenium you used  in ur project and what is different between older and new version?
2.how to handle windows in selenium?
3.write xpath syntax,how to handle dynamic webelement?
4.what are the disadvantages using selenium?
5.WebDriver Driver=new WebDriver();   

check the above syntax and tell whether correct or incorrect?

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. tell about urself
Standard opener. Focus on professional experience, skills, and accomplishments.

### 2. explain about project and framework used in project?why using cucumber ,why not testng?
First, explain your project and framework (Java, Selenium, POM, etc.). Then address the "why Cucumber" question.

"Our framework is a Java-based BDD framework. We chose **Cucumber** on top of **TestNG** because our project had a strong need for collaboration with business analysts who were not programmers. Cucumber allowed us to write our test scenarios in plain-English Gherkin, which the BAs could read, review, and even help write. This ensured our tests were perfectly aligned with the business requirements and served as living documentation. We still used **TestNG** as the underlying test runner to manage our test suites, run tests in parallel, and generate reports, so we got the benefits of both tools."

> **Side Note:** It's not "Cucumber vs. TestNG". They work together. Cucumber is for BDD specification; TestNG is for execution and orchestration. This is a key distinction to make.

### 3. how to passing data from excel?what are the steps to use excel in eclipse?
You use the **Apache POI** library.
**Steps:**
1.  **Add Dependency:** Add the Apache POI dependency (`poi` and `poi-ooxml`) to your `pom.xml` file in your Maven project.
2.  **Create Utility Class:** Write a Java utility class with methods to:
    -   Open an Excel file (`FileInputStream` and `XSSFWorkbook`).
    -   Select a specific sheet (`workbook.getSheet("Sheet1")`).
    -   Get the number of rows and columns.
    -   Read data from a specific cell (`row.getCell(colNum).getStringCellValue()`).
3.  **Use in `@DataProvider`:** Create a TestNG `@DataProvider` method. Inside this method, call your Excel utility to read the data and populate a 2D `Object[][]` array.
4.  **Consume Data:** Your `@Test` method then consumes this data from the provider.

Eclipse itself doesn't have special steps; it's all handled through your Java code and Maven dependencies.

### 4. what are the criticalbugs u found in ur project ?
Be ready with a specific, real example.
"I found a critical bug in our payment processing module where, under a specific race condition (if the user double-clicked the 'Submit' button very quickly), the system would sometimes authorize the credit card twice but only create one order. This could lead to customers being overcharged. It was a high-severity, high-priority bug because of its financial impact."

### 5. do u have any idea API testing and Appium tool?
"Yes.
-   **API Testing:** I have hands-on experience testing REST APIs using **REST-assured** with Java. I write automated tests to validate status codes, response bodies, and business logic. I also use **Postman** for manual and exploratory API testing.
-   **Appium:** I have a solid understanding of Appium as a tool for mobile test automation. I know its architecture—how it uses the WebDriver protocol to send commands to native testing frameworks like XCUITest for iOS and UIAutomator2 for Android—and I have experience writing basic scripts and locating elements using `accessibilityId` and `xpath`."

### 6. what will u do if developer wont accept the bug and how will u manage this situation?
This tests your collaboration skills.
1.  **Stay Professional:** Don't get into an argument.
2.  **Reproduce Together:** The most effective step is to ask the developer for a quick screen-share session to reproduce the bug together, on your machine or theirs. This eliminates any "it works on my machine" issues.
3.  **Review the Requirements:** Revisit the user story or requirement document. Is the expected behavior clearly defined?
4.  **Involve the Product Owner:** If the disagreement is about how the feature *should* work, the Product Owner is the final authority and can clarify the requirement for both of you.

### Java

#### 1. difference between == and .equals?
-   `==`: An operator. For primitives, it compares values. For objects, it compares memory addresses (do the references point to the same object?).
-   `.equals()`: A method. For objects, it should be used to compare their content/state. Classes like `String` override it to provide this content comparison. By default (in the `Object` class), it behaves just like `==`.

#### 2. what is abstraction and explain?
Abstraction is hiding complex implementation details and exposing only the essential functionalities. It's about simplifying a complex system by modeling classes appropriate to the problem. In Java, this is achieved with **abstract classes** and **interfaces**. The `WebDriver` interface is the perfect example in test automation.

#### 3. what is different between throw and throws?
-   **`throw`:** A keyword used to **manually throw an exception** at a specific point in the code.
    ```java
    if (age < 18) {
        throw new IllegalArgumentException("User must be 18 or older.");
    }
    ```
-   **`throws`:** A keyword used in a method signature to declare that the method **might throw one or more specific checked exceptions**. It delegates the responsibility of handling the exception to the calling method.
    ```java
a   public void readFile() throws IOException {
        // ... code that might throw an IOException
    }
    ```

#### 4. String s="Selenium"; tell a logic for this output "Slnium"
This means removing the character 'e'.

```java
String s = "Selenium";
String result = s.replace("e", ""); 
System.out.println(result); // Slnium
```

### Selenium

#### 1. Which version of selenium you used in ur project and what is different between older and new version?
"I'm using **Selenium 4**. The biggest difference from Selenium 3 is that Selenium 4 is fully **W3C WebDriver protocol compliant**, which makes tests more stable and consistent across browsers. It also introduced new features like **Relative Locators** (e.g., `toLeftOf()`, `below()`), and native integration with the **Chrome DevTools Protocol (CDP)**."

#### 2. how to handle windows in selenium?
Using window handles.
1.  Get the current window handle: `driver.getWindowHandle()`.
2.  Get all open window handles: `driver.getWindowHandles()`.
3.  Switch between them using `driver.switchTo().window(handleId)`.

#### 3. write xpath syntax,how to handle dynamic webelement?
-   **XPath Syntax:** `//tagName[@attribute='value']`. Example: `//input[@id='username']`.
-   **Handling Dynamic WebElements:** You write an XPath that doesn't rely on the dynamic part.
    -   Use `contains()`: `//div[contains(@id, 'user-id-')]`
    -   Use `starts-with()`: `//div[starts-with(@id, 'user-id-')]`
    -   Use a stable parent and axes: `//div[@class='stable-parent']/descendant::button`
    -   Use a combination with `and`/`or`: `//button[@type='submit' and contains(text(), 'Login')]`

#### 4. what are the disadvantages using selenium?
1.  **Only supports web browsers:** Cannot automate desktop or mobile native apps.
2.  **Steep Learning Curve:** Handling synchronization (waits), setting up a robust framework, and managing a Grid can be complex.
3.  **No built-in reporting:** Requires integration with third-party tools like TestNG, ExtentReports, etc.
4.  **No built-in image validation:** Can't verify images or visual layout without external libraries.

#### 5. WebDriver Driver=new WebDriver(); check the above syntax and tell whether correct or incorrect?
**Incorrect.** `WebDriver` is an **interface**. You cannot create an object of an interface using `new`.

You must instantiate a concrete class that implements the interface.
-   **Correct syntax:** `WebDriver driver = new ChromeDriver();`
