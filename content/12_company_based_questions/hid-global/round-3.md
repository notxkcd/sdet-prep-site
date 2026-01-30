---
title: "HID_Global-3"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

HID Level 2 - 1 hour 20 mins - Virtual
---------------------------------------
1. Introduce yourself with your current projects 
2. Java code strings and char Duplicates
3. How to handle multiple browser
4. What is constructor
5. What is collections
6. Difference between List and Set
7. What is break and continue in Java
8. What are types of string 
9. Whats is overload and Override with example 
10. Explain wrapper class
11. Name few methods you are using for string and collection 
12. Explain Appium Architecture 
13. What are the pre requisite before starting the device automation 
14. What are types of applications 
15. What are the challenges you are facing in Appium testing
16. What are the limitations in appium
17. How to handle the drop-down in appium 
18. How to handle Touch actions in appium
19. How will you handle drop-down in appium
20. What is find element and elements differentiate it
21. Which syntax you are using for scroll up and scroll down in mobile testing
22. What are version you are testing currently in android and iOS
23. Explain the cucumber framework 
24. What are the TestNG annotation 
25. How will you test the automation for different browser parallely
26. How will you find element in appium testing 
27. What is most fastest locators in appium 
28. List out not possible scenarios while performing device automation

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. Introduce yourself with your current projects
Standard.

### 2. Java code strings and char Duplicates
To find duplicate characters in a string, a `Map` is the most common approach to count frequencies.

```java
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;

public class DuplicateChars {
    public void findDuplicates(String input) {
        input.chars()
             .mapToObj(c -> (char) c)
             .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()))
             .entrySet().stream()
             .filter(entry -> entry.getValue() > 1)
             .forEach(entry -> System.out.println("Char '" + entry.getKey() + "' found " + entry.getValue() + " times."));
    }
}
```

### 3. How to handle multiple browser
This is cross-browser testing.
-   **Configuration:** Use a parameter in your `testng.xml` to specify the browser.
-   **Instantiation:** In a `@BeforeMethod` (or similar setup method), use a `switch` statement or factory pattern to instantiate the correct `WebDriver` (`ChromeDriver`, `FirefoxDriver`, etc.) based on the parameter.
-   **Execution:** Run the tests in parallel using Selenium Grid to test on different browsers simultaneously.

### 4. What is constructor
A special method in a class that is called when an object is created. Its purpose is to initialize the object's state. It has the same name as the class and no return type.

### 5. What is collections
The Java Collections Framework is a set of interfaces (`List`, `Set`, `Map`) and classes (`ArrayList`, `HashSet`, `HashMap`) for storing and manipulating groups of objects.

### 6. Difference between List and Set
-   **`List`:** Ordered, indexed collection. Allows duplicate elements.
-   **`Set`:** Unordered collection. Does not allow duplicate elements.

### 7. What is break and continue in Java
-   **`break`:** Immediately terminates the innermost loop (`for`, `while`) or `switch` statement.
-   **`continue`:** Skips the current iteration of the loop and proceeds to the next one.

### 8. What are types of string
In Java, there are two main "types" in terms of how they are created and stored, although both result in a `String` object:
1.  **String Literal:** `String s1 = "hello";`. These are stored in the String Constant Pool for efficiency.
2.  **String Object (using `new`):** `String s2 = new String("hello");`. This forces the creation of a new object on the heap every time.

There are also the mutable string classes: `StringBuilder` (faster, not thread-safe) and `StringBuffer` (slower, thread-safe).

### 9. Whats is overload and Override with example
-   **Overload:** Same method name, different parameters, same class. Example: `public void click(WebElement e)` and `public void click(By locator)`.
-   **Override:** Same method signature in a child class as in a parent class. Example: A child test class overriding a `setup()` method from a `BaseTest` class.

### 10. Explain wrapper class
A class that "wraps" a primitive data type into an object (e.g., `int` -> `Integer`). This is necessary for using primitive values in collections like `ArrayList<Integer>`.

### 11. Name few methods you are using for string and collection
-   **String:** `.length()`, `.charAt()`, `.substring()`, `.equals()`, `.equalsIgnoreCase()`, `.contains()`, `.split()`, `.trim()`.
-   **Collection (List/Set):** `.add()`, `.remove()`, `.size()`, `.isEmpty()`, `.contains()`, `.clear()`.
-   **Map:** `.put()`, `.get()`, `.containsKey()`, `.size()`, `.keySet()`.

### 12. Explain Appium Architecture
Appium is an HTTP server that acts as a middleman. Your test script (client) sends commands using the JSON Wire Protocol to the Appium server. The server interprets these and uses a vendor-specific framework (**XCUITest** for iOS, **UIAutomator2** for Android) to execute the command on the device/emulator. The result is then sent back to your script.

### 13. What are the pre requisite before starting the device automation
-   **Software:** Java JDK, Node.js (for Appium server), Android Studio (for Android SDK, emulators), Xcode (for iOS simulators, drivers), an IDE (IntelliJ/Eclipse).
-   **Appium Setup:** Appium server installed, Appium Inspector for locating elements.
-   **Device/Emulator:** A configured Android emulator or iOS simulator, or a real device with developer mode enabled and connected via USB.
-   **Application:** The `.apk` (Android) or `.app` (iOS) file of the application to be tested.
-   **Desired Capabilities:** A set of key-value pairs defining the test session (e.g., `platformName`, `deviceName`, `app` path, `automationName`).

### 14. What are types of applications
-   **Native:** Built specifically for one OS (iOS/Android).
-   **Mobile Web:** A website accessed via a mobile browser.
-   **Hybrid:** A web app wrapped in a native shell.

### 15. What are the challenges you are facing in Appium testing
-   **Locator Strategy:** Locators can be less stable than on web. `accessibilityId` is preferred.
-   **Synchronization:** App screen transitions and network calls require robust explicit waits.
-   **Setup Complexity:** Managing different OS versions, Appium versions, and device configurations can be complex.
-   **Gestures:** Automating complex gestures like multi-touch or precise swipes can be tricky.
-   **Execution Speed:** Emulators/simulators can be slow, making test runs long.

### 16. What are the limitations in appium
-   Cannot automate OS-level settings or notifications outside the context of your app.
-   Slower than native testing frameworks like Espresso/XCUITest.
-   Cannot directly test interactions between two different applications.
-   Limited support for testing hardware-dependent features (e.g., camera, fingerprint scanner).

### 17. How to handle the drop-down in appium
There is no `Select` class like in Selenium. You treat dropdowns as a series of taps.
1.  Tap the dropdown element to open the list of options.
2.  The options will appear in a new view or overlay.
3.  Locate the desired option element (e.g., by its text) and tap it.

### 18. How to handle Touch actions in appium
You use the `TouchAction` class (or the newer W3C Actions API).
```java
// Legacy TouchAction example for a swipe
TouchAction action = new TouchAction(driver);
action.press(PointOption.point(startX, startY))
      .waitAction(WaitOptions.waitOptions(Duration.ofMillis(500)))
      .moveTo(PointOption.point(endX, endY))
      .release()
      .perform();
```

### 19. How will you handle drop-down in appium
Duplicate of question 17.

### 20. What is find element and elements differentiate it
-   `findElement()`: Returns one `WebElement`. Throws exception if not found.
-   `findElements()`: Returns a `List<WebElement>`. Returns an empty list if none are found.

### 21. Which syntax you are using for scroll up and scroll down in mobile testing
You typically use the `TouchAction` class or JavaScript Executor. There is no simple `.scroll()` method.
```java
// Example using TouchAction to scroll down
Dimension size = driver.manage().window().getSize();
int startX = size.getWidth() / 2;
int startY = (int) (size.getHeight() * 0.8);
int endY = (int) (size.getHeight() * 0.2);

new TouchAction(driver)
    .press(PointOption.point(startX, startY))
    .waitAction(WaitOptions.waitOptions(Duration.ofMillis(200)))
    .moveTo(PointOption.point(startX, endY))
    .release()
    .perform();
```

### 22. What are version you are testing currently in android and iOS
Be specific. "We primarily target recent versions. For Android, our test devices run Android 11 and 12. For iOS, we focus on iOS 14 and 15."

### 23. Explain the cucumber framework
It's a BDD framework that allows writing tests in human-readable Gherkin, which are then linked to executable Java code (step definitions).

### 24. What are the TestNG annotation
`@Test`, `@BeforeSuite`, `@AfterSuite`, `@BeforeTest`, `@AfterTest`, `@BeforeClass`, `@AfterClass`, `@BeforeMethod`, `@AfterMethod`, `@DataProvider`.

### 25. How will you test the automation for different browser parallely
Using **Selenium Grid** and **TestNG's parallel execution** feature. You define a suite in `testng.xml` with multiple `<test>` tags, each with a different browser parameter. Then you set `parallel="tests"` on the `<suite>` tag.

### 26. How will you find element in appium testing
Appium supports several locator strategies:
-   **`accessibilityId`:** **Most preferred.** A unique ID for accessibility. Cross-platform.
-   **`id`:** Uses the native `resource-id` on Android and `name` on iOS.
-   **`xpath`:** Powerful but slowest. Use as a last resort.
-   **`className`:** Uses the native class name (e.g., `android.widget.TextView`).
-   **`name`:** (Deprecated)
-   **UIAutomator (Android only) / Predicate String (iOS only):** Native, powerful search capabilities.

### 27. What is most fastest locators in appium
**`accessibilityId`** and **`id`** are generally the fastest and most recommended. `xpath` is the slowest.

### 28. List out not possible scenarios while performing device automation
Same as "limitations of Appium".
-   Automating OS settings.
-   Testing interactions between different apps.
-   Testing system-level notifications or incoming calls.
-   Biometric authentication (fingerprint, face ID).
-   Testing complex hardware sensor inputs.
