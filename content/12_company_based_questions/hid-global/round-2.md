---
title: "HID_Global-2"
date: 2026-01-30
draft: false
---

---

## Original Questions

HID Global Interview Questions:
-------------------------------
>>Java Question - "1am a C0dingF4n 0r Pr0gr4mm3r or S0ftw4r3 D3v3l0p3r"
1. Split the letters and number and print
2. Print the frequency of integer and letters
3. Sum the integer
4. Collection End to End questions
5. oops concept (Polymorphism and Inheritance)
6. Explain Primitive and non Primitive data types
>> Selenium Questions:
1. How will you handle different browser and what will you do if any one of browser is not working as expected
2. Diff between final, finally and finalize
3. What are the possible xpaths can be able to taken with the given WebElements "Given Page: Facebook Login page"
>> Frameworks:
1. What are the annotations you are handling in your projects?
2. Tell about assertions and usages in your frameworks?
3. Framework explanations
4. How you push the codes and what are the tools are using for it and explain the hierarchy 
5. How will you validate the project to be working good or not . What are all the steps you verified it meets the expectations?
>> Testing related questions:
1. Difference between severity and priority and explain with the real time scenarios?
2. Defect Managements?
3. What are all the steps you are following to triage bugs and how will you handle with developers team?
4. What are all the devices you are handling in your testing?
>> Appium related questions:
1. Types of applications?
2. Define Appium Architecture?
3. What are all not Possible to while handling devices with Appium and explain it why?
4. Explain the Appium frameworks with the keywords which is using in your testing cycles?
>> Intro Questions:-
1. Introduce yourself
2. Explain your projects and framework
3. Day to Day activities

---

## Answers (No-BS Java QA / SDET Explanations)

### >> Java Questions

#### 1. Split the letters and number and print
```java
public class Splitter {
    public static void split(String input) {
        StringBuilder letters = new StringBuilder();
        StringBuilder numbers = new StringBuilder();
        for (char c : input.toCharArray()) {
            if (Character.isLetter(c)) {
                letters.append(c);
            } else if (Character.isDigit(c)) {
                numbers.append(c);
            }
        }
        System.out.println("Letters: " + letters);
        System.out.println("Numbers: " + numbers);
    }
    public static void main(String[] args) {
        split("1am a C0dingF4n 0r Pr0gr4mm3r or S0ftw4r3 D3v3l0p3r");
    }
}
```

#### 2. Print the frequency of integer and letters
```java
import java.util.Map;
import java.util.stream.Collectors;

public class Frequency {
    public static void getFreq(String input) {
        System.out.println("Letter Frequency:");
        input.chars()
             .mapToObj(c -> (char) c)
             .filter(Character::isLetter)
             .map(Character::toLowerCase)
             .collect(Collectors.groupingBy(c -> c, Collectors.counting()))
             .forEach((letter, count) -> System.out.println(letter + ": " + count));
        
        System.out.println("\nDigit Frequency:");
        input.chars()
             .mapToObj(c -> (char) c)
             .filter(Character::isDigit)
             .collect(Collectors.groupingBy(c -> c, Collectors.counting()))
             .forEach((digit, count) -> System.out.println(digit + ": " + count));
    }
}
```

#### 3. Sum the integer
```java
public class SumDigits {
    public static int sum(String input) {
        int total = 0;
        for (char c : input.toCharArray()) {
            if (Character.isDigit(c)) {
                total += Character.getNumericValue(c);
            }
        }
        return total;
    }
    public static void main(String[] args) {
        System.out.println("Sum: " + sum("1am a C0dingF4n 0r Pr0gr4mm3r or S0ftw4r3 D3v3l0p3r")); // 1+0+4+0+0+4+3+0+4+3+3+0+3
    }
}
```

#### 4. Collection End to End questions
This means they want to know everything about the Collections Framework:
-   **Interfaces:** `List` (ordered, duplicates), `Set` (unordered, unique), `Queue`, `Map` (key-value).
-   **Implementations:** `ArrayList` vs `LinkedList`, `HashSet` vs `LinkedHashSet` vs `TreeSet`, `HashMap` vs `TreeMap`.
-   **Usage:** When to use a `List` (order matters) vs a `Set` (uniqueness matters) vs a `Map` (lookups by key).

#### 5. oops concept (Polymorphism and Inheritance)
-   **Inheritance:** Reusing code from a parent class (`extends`). A `BaseTest` class that all test classes inherit from is a prime example.
-   **Polymorphism:** Method overriding. A child class provides a specific implementation of a parent's method. For example, `WebDriver driver = new ChromeDriver();` is polymorphism in action.

#### 6. Explain Primitive and non Primitive data types
-   **Primitive:** 8 basic types (`int`, `char`, `boolean`, etc.). They hold values directly and are not objects.
-   **Non-Primitive (Reference):** Objects. They hold a reference (memory address) to the actual object data. Includes `String`, `Array`, and any class you create.

### >> Selenium Questions

#### 1. How will you handle different browser and what will you do if any one of browser is not working as expected
-   **Handling Different Browsers:** Use a factory pattern or a `switch` statement in your `@BeforeMethod` setup, driven by a parameter from `testng.xml`.
    ```java
    @Parameters("browser")
    public void setup(String browserName) {
        switch (browserName.toLowerCase()) {
            case "firefox": driver = new FirefoxDriver(); break;
            case "edge": driver = new EdgeDriver(); break;
            default: driver = new ChromeDriver(); break;
        }
    }
    ```
-   **If One Browser Fails:** This is a bug. First, ensure the issue is not with your script (e.g., a timing issue specific to Firefox). If the application functionality is truly broken on only one browser, you raise a high-priority bug, clearly stating that it's a cross-browser compatibility issue.

#### 2. Diff between final, finally and finalize
-   **`final`:** Keyword. Makes a variable constant, a method non-overridable, or a class non-extendable.
-   **`finally`:** Block. Part of `try-catch`. Always executes. Used for cleanup (`driver.quit()`)
-   **`finalize()`:** Method. Called by the garbage collector before destroying an object. Deprecated and should not be used.

#### 3. What are the possible xpaths can be able to taken with the given WebElements "Given Page: Facebook Login page"
This is a practical test. For the email/phone input field:
-   `//input[@id='email']` (by ID, best)
-   `//input[@name='email']` (by name)
-   `//input[@data-testid='royal_email']` (by a test-specific attribute)
-   `//input[contains(@aria-label, 'Email address')]` (by partial attribute text)
For the "Log In" button:
-   `//button[@name='login']` (by name)
-   `//button[text()='Log In']` (by exact text, can be brittle if text changes)

### >> Frameworks

#### 1. What are the annotations you are handling in your projects?
"In TestNG, I primarily use `@Test`, `@BeforeMethod`, `@AfterMethod`, `@DataProvider`, and `@Parameters`. In Cucumber, I use `@Given`, `@When`, `@Then`."

#### 2. Tell about assertions and usages in your frameworks?
"We use TestNG assertions.
-   **Hard Asserts (`Assert.assertEquals`)** are used for critical checkpoints. If a hard assert fails, the test stops immediately. We use this to validate things like a successful login.
-   **Soft Asserts (`SoftAssert`)** are used when we want to validate multiple, non-critical things on a page and see all failures at once. For example, checking all the labels on a form. We instantiate `SoftAssert`, make multiple assertions, and then call `softAssert.assertAll()` at the end of the test."

#### 3. Framework explanations
Standard question. Cover architecture, design, tools, and CI/CD integration.

#### 4. How you push the codes and what are the tools are using for it and explain the hierarchy
-   **Tool:** We use **Git** for version control and **GitHub** as our remote repository host.
-   **Hierarchy/Workflow (Git Flow variant):**
    1.  A `main` branch that always reflects production-ready code.
    2.  A `develop` branch where all new development is integrated.
    3.  For any new feature or bugfix, I create a **feature branch** from `develop` (e.g., `feature/login-test`).
    4.  I commit my code to my local feature branch (`git commit`).
    5.  I push my feature branch to the remote repository (`git push origin feature/login-test`).
    6.  I then open a **Pull Request (PR)** on GitHub to merge my feature branch into `develop`.
    7.  The PR is peer-reviewed, and once approved and all automated checks (like our test suite in Jenkins) pass, it's merged.

#### 5. How will you validate the project to be working good or not . What are all the steps you verified it meets the expectations?
This describes the entire testing process.
1.  **Requirement Analysis:** Ensure requirements are clear and testable.
2.  **Test Planning & Design:** Write comprehensive test cases covering positive, negative, and edge cases.
3.  **Unit & Integration Tests:** Verify that developers have covered their code with unit tests and that basic integrations work.
4.  **Functional & Regression Testing:** Execute our automated API and UI regression suites to ensure new changes haven't broken existing functionality.
5.  **New Feature Testing:** Perform automated and exploratory testing on new features.
6.  **UAT/Stakeholder Review:** Demo the feature to the product owner for acceptance.
7.  **Final Validation:** Passing all these steps, with no critical bugs outstanding, verifies the project meets expectations.

### >> Testing related questions

#### 1. Difference between severity and priority and explain with the real time scenarios?
-   **Severity:** Technical impact. (QA decides).
-   **Priority:** Business urgency. (Product Owner decides).
-   **Real-time Scenario:** A typo of the company logo on the homepage. **Severity** is trivial (doesn't break anything), but **Priority** is high (it's embarrassing and needs to be fixed immediately).

#### 2. Defect Managements?
This means the process of managing defects. "We use **Jira** for defect management. The lifecycle is:
1.  QA finds and reports a bug with detailed steps, logs, and screenshots (`New`).
2.  The bug is triaged and assigned to a developer (`Open`).
3.  Developer fixes the code (`Fixed`).
4.  The fix is deployed to a QA environment, and the bug is marked `Ready for QA`.
5.  QA re-tests the original scenario. If it passes, the bug is `Closed`. If not, it's `Reopened` with comments."

#### 3. What are all the steps you are following to triage bugs and how will you handle with developers team?
-   **Triage:** When a bug is found, I first ensure it's a valid defect by reproducing it consistently. I check that it's not a duplicate of an existing bug. I then assign a `Severity` based on its technical impact.
-   **Handling with Developers:** I believe in collaboration, not confrontation. When a developer disputes a bug, I:
    1.  Re-verify my steps and the environment.
    2.  Ask them to join a quick screen-share session to reproduce the bug together.
    3.  If it's an ambiguity in requirements, I involve the Product Owner to clarify the expected behavior.

#### 4. What are all the devices you are handling in your testing?
"Our primary focus is web, so we test across desktop browsers (Chrome, Firefox, Safari). We also perform compatibility testing on mobile browsers using Chrome DevTools' device emulation. For specific mobile testing, we use a cloud device farm like BrowserStack to run tests on real iOS and Android devices."

### >> Appium related questions

#### 1. Types of applications?
-   **Native Apps:** Built specifically for an OS (iOS or Android) using native SDKs (Swift/Objective-C for iOS, Java/Kotlin for Android).
-   **Mobile Web Apps:** Websites accessed through a mobile browser.
-   **Hybrid Apps:** A mix of both. They are web apps wrapped in a native container, allowing them to be installed like a native app and access some device features. Built with frameworks like React Native, Ionic, or Flutter.

#### 2. Define Appium Architecture?
Appium is an HTTP server that exposes a REST API.
1.  **Client (Test Script):** Your Selenium/Appium test script sends commands (as JSON objects) to the Appium server. This is the JSON Wire Protocol.
2.  **Appium Server:** Listens for these commands, interprets them, and then uses a specific driver to translate them into commands that the mobile platform understands.
3.  **Vendor-Provided Frameworks:**
    -   On **iOS**, Appium uses Apple's **XCUITest** framework.
    -   On **Android**, Appium uses Google's **UIAutomator2** framework.
4.  **Device:** The command is executed on the emulator, simulator, or real device, and the result is sent back to the Appium server, which then responds to your test script.

#### 3. What are all not Possible to while handling devices with Appium and explain it why?
-   **Testing OS-level features:** Appium cannot automate testing of things outside the context of your application, like Android settings, notifications tray (completely), or interactions between two different apps.
-   **Heavy reliance on hardware:** Cannot test features that depend heavily on specific hardware sensors not available in emulators (e.g., complex accelerometer/gyroscope movements, barometer).
-   **Very low-level interactions:** Cannot test things like incoming phone calls or SMS interruptions directly (though you can simulate some of this).

#### 4. Explain the Appium frameworks with the keywords which is using in your testing cycles?
This is about your specific Appium test framework.
"Our Appium framework mirrors our Selenium framework. We use the Page Object Model, where each screen of the mobile app has its own class. Key 'keywords' or methods we use are wrappers around Appium commands:
-   `tap(element)`: A reusable method that waits for an element to be clickable and then taps it.
-   `swipe(direction)`: A method that performs a swipe gesture.
-   `enterText(element, text)`: A method to enter text into an input field."

### >> Intro Questions

#### 1. Introduce yourself
Standard.

#### 2. Explain your projects and framework
Standard.

#### 3. Day to Day activities
Standard.
