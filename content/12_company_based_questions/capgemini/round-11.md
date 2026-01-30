---
title: "Capgemini-11"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

Capgemini assessment round interview questions:
-----------------------------------------------

Selenium:

1. What is a hook in Cucumber?
- A piece of code that runs before or after a scenario or feature
- A file that contains the test scenarios for a particular feature
- A file that contains the requirements for a particular feature
- A file that contains the test results for a particular feature

2. Which two commands you use to validate a button?
- VerifyTextPresent and assertTextPresent
- VerifyElementPresent and assertElementPresent
- VerifyAlertPresent and assertAlertPresent
- VerifyAlert and assertAlert

3. Firefox specific settings like: 'addPreference', 'setBinary' can be managed by using the class
- FirefoxProfile
- FirefoxDriver
- FirefoxOptions
- None of the above

4. Which of the following WebDriver is used for Headless browser testing?
- HeadLessDriver
- HtmlUnitWebDriver
- FireFoxDriver
- ChromeDriver

5. How can you run only a specific subset of scenarios in a Cucumber test suite?
- By using the @Subset annotation
- By using tags and specifying them in the Cucumber options
- By placing them in a separate feature file
- By using the @Scenario annotation

JAVA:

1. Evaluate the following Java expression, if x=3, y=5, and z=10:

++2 + y - y* z + z++

- 25
- 28
- 20
- 24

2. Predict the output of following Java program:
java
public class Test2 {
    public static void main(String[] args) {
        StringBuffer s1 = new StringBuffer("Complete");
        s1.setCharAt(1,'i');
        s1.setCharAt(7,'d');
        System.out.println(s1);
    }
}

- Complete
- Iomplete
- Coipleted
- Cimpletd

3. Which option is false about the final keyword?
- A final method cannot be overridden in its subclasses.
- A final class cannot be extended.
- A final class cannot extend other classes.
- A final method can be inherited.

4. Predict the output of following Java program:
java
class Output {
    public static void main(String args[]) {
        int arr[] = {1, 2, 3, 4, 5};
        for (int i = 0; i < arr.length - 2; ++i)
            System.out.print(arr[i] + " ");
    }
}

- 1 2 3 4 5
- 1 2 3
- 1 2
- 1 2 3 4

5. Which of the following is a valid syntax to synchronize the HashMap?
- Map m = hashMap.synchronizeMap();
- HashMap map = hashMap.synchronizeMap();
- Map m1 = Collections.synchronizedMap(hashMap);
- Map m2 = Collection.synchronizeMap(hashMap);

---

## Answers (No-BS Java QA / SDET Explanations)

### Selenium:

#### 1. What is a hook in Cucumber?
**Correct Answer: - A piece of code that runs before or after a scenario or feature**
-   **Explanation:** Cucumber hooks (`@Before`, `@After`) are blocks of code in your step definitions that execute at specific points in the test lifecycle, typically for setup and teardown actions.

#### 2. Which two commands you use to validate a button?
**Correct Answer: - VerifyElementPresent and assertElementPresent**
-   **Explanation:** In TestNG/JUnit, you'd use `Assert.assertTrue(element.isDisplayed())` or check if `driver.findElements(By.locator).size() > 0`. The options are phrased like old Selenium IDE commands, but "ElementPresent" is the closest concept to verifying its existence.

#### 3. Firefox specific settings like: 'addPreference', 'setBinary' can be managed by using the class
**Correct Answer: - FirefoxOptions**
-   **Explanation:** `FirefoxOptions` is the class used to set capabilities and preferences for a Firefox WebDriver session, similar to `ChromeOptions` for Chrome. `FirefoxProfile` is an older class used in Selenium 2/3.

#### 4. Which of the following WebDriver is used for Headless browser testing?
**Correct Answer: - HtmlUnitWebDriver**
-   **Explanation:** `HtmlUnitWebDriver` is a headless browser implementation (a Java library that simulates a browser without a GUI). While Chrome and Firefox also support headless modes (via `ChromeOptions` and `FirefoxOptions`), `HtmlUnitWebDriver` is a specific WebDriver implementation *designed* to be headless.

#### 5. How can you run only a specific subset of scenarios in a Cucumber test suite?
**Correct Answer: - By using tags and specifying them in the Cucumber options**
-   **Explanation:** Cucumber's `@tags` feature is designed for this. You annotate your scenarios (or features) with tags (e.g., `@smoke`, `@regression`) and then specify which tags to `include` or `exclude` in your Cucumber Runner class's `@CucumberOptions`.

### JAVA:

#### 1. Evaluate the following Java expression, if x=3, y=5, and z=10: `++2 + y - y * z + z++`
This expression will cause a **compile-time error** because `++2` is invalid. The `++` operator (increment) can only be applied to a variable, not a literal value.

Assuming the question meant `++x` instead of `++2` for a valid expression:
If `x=3`, `y=5`, `z=10`:
`++x` becomes `4` (x is now 4)
`y` is `5`
`y * z` is `5 * 10 = 50`
`z++` is `10` (z becomes 11 after this step)

So the expression `4 + 5 - 50 + 10` evaluates to `9 - 50 + 10 = -41 + 10 = -31`.

Since the original expression is invalid, none of the options are strictly correct. However, if forced to choose based on an implied valid expression, it highlights understanding of operator precedence and side effects.

#### 2. Predict the output of following Java program:
```java
public class Test2 {
    public static void main(String[] args) {
        StringBuffer s1 = new StringBuffer("Complete");
        s1.setCharAt(1,'i'); // Replaces 'o' at index 1 with 'i' -> "Cimplete"
        s1.setCharAt(7,'d'); // Replaces 'e' at index 7 with 'd' -> "Cimpletd"
        System.out.println(s1);
    }
}
```
**Correct Answer: - Cimpletd**

#### 3. Which option is false about the final keyword?
**Correct Answer: - A final class cannot extend other classes.**
-   **Explanation:**
    -   A `final` method cannot be overridden (True).
    -   A `final` class cannot be extended (True).
    -   A `final` class *can* extend other classes (False, this is the incorrect statement). Example: `String` is a final class, but it still `extends Object`. The `final` keyword prevents it from *being extended*, not from *extending others*.
    -   A `final` method can be inherited (True).

#### 4. Predict the output of following Java program:
```java
class Output {
    public static void main(String args[]) {
        int arr[] = {1, 2, 3, 4, 5};
        for (int i = 0; i < arr.length - 2; ++i) // Loop condition: i < 5 - 2 => i < 3
            System.out.print(arr[i] + " ");
    }
}
```
**Loop execution:**
-   `i = 0`: `0 < 3` is true. Prints `arr[0]` (1).
-   `i = 1`: `1 < 3` is true. Prints `arr[1]` (2).
-   `i = 2`: `2 < 3` is true. Prints `arr[2]` (3).
-   `i = 3`: `3 < 3` is false. Loop terminates.
**Correct Answer: - 1 2 3**

#### 5. Which of the following is a valid syntax to synchronize the HashMap?
**Correct Answer: - Map m1 = Collections.synchronizedMap(hashMap);**
-   **Explanation:** `HashMap` itself is not thread-safe. To get a synchronized (thread-safe) version of a `HashMap`, you use the static factory method `Collections.synchronizedMap()`.
    -   Options 1 and 2 are invalid methods.
    -   Option 4 has a typo (`Collection` instead of `Collections`).
