---
title: "Trane technologies"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

- Trane technologies
------------------
1. What are all the capabilities you will set for mobile automation write the codes
2. Did you use soap or rest assured 
3. What are all the http methods
4. What is 401 status code for 
5. Write a program to reverse words input : test program
output: program test 
6. What is interface

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. What are all the capabilities you will set for mobile automation write the codes
This refers to **Desired Capabilities** in Appium. These are a set of key-value pairs sent to the Appium server to tell it what kind of automation session you want to start (e.g., what device, platform, and application to run).

```java
import org.openqa.selenium.remote.DesiredCapabilities;
import io.appium.java_client.android.AndroidDriver;
import java.net.URL;

public class AppiumSetup {
    public AndroidDriver setupAndroidDriver() throws Exception {
        DesiredCapabilities caps = new DesiredCapabilities();
        caps.setCapability("platformName", "Android");
        caps.setCapability("deviceName", "emulator-5554"); // Or specific device ID
        caps.setCapability("platformVersion", "11.0");
        caps.setCapability("appPackage", "com.android.settings"); // Example package
        caps.setCapability("appActivity", "com.android.settings.Settings"); // Example activity
        caps.setCapability("automationName", "UiAutomator2"); // For newer Android versions
        caps.setCapability("newCommandTimeout", 60); // Timeout for Appium commands

        // URL of the Appium server
        URL appiumServerURL = new URL("http://127.0.0.1:4723/wd/hub");
        
        AndroidDriver driver = new AndroidDriver(appiumServerURL, caps);
        return driver;
    }
}
```

### 2. Did you use soap or rest assured
"I primarily work with **REST APIs**, so I use **REST-assured** for my API automation. REST-assured is a Java DSL (Domain Specific Language) that simplifies the testing of RESTful web services. I haven't worked with SOAP APIs in my current role, but I understand the principles of SOAP and could adapt if needed."

### 3. What are all the http methods
The standard HTTP methods (verbs):
-   `GET`: Retrieve a resource.
-   `POST`: Create a new resource.
-   `PUT`: Replace an existing resource.
-   `PATCH`: Partially update an existing resource.
-   `DELETE`: Remove a resource.

### 4. What is 401 status code for
`401 Unauthorized`. This status code indicates that the client request has not been completed because it lacks valid authentication credentials for the target resource. Essentially, you tried to access a protected resource without logging in or providing a valid token.

### 5. Write a program to reverse words input : test program output: program test
This means reversing the order of words in a sentence, not reversing individual words.

```java
public class WordOrderReverser {
    public static String reverseWordOrder(String sentence) {
        if (sentence == null || sentence.trim().isEmpty()) {
            return sentence;
        }
        
        // Split the sentence into words by one or more whitespace characters
        String[] words = sentence.trim().split("\\s+");
        
        // Use a StringBuilder to efficiently build the reversed sentence
        StringBuilder reversedSentence = new StringBuilder();
        for (int i = words.length - 1; i >= 0; i--) {
            reversedSentence.append(words[i]);
            if (i > 0) {
                reversedSentence.append(" "); // Add space between words
            }
        }
        return reversedSentence.toString();
    }

    public static void main(String[] args) {
        System.out.println(reverseWordOrder("test program")); // Output: program test
        System.out.println(reverseWordOrder("  hello   world  java  ")); // Output: java world hello
    }
}
```

### 6. What is interface
An interface in Java is a blueprint of a class. It contains abstract methods and static final fields. It specifies a contract: any class that `implements` an interface must provide an implementation for all the abstract methods declared in that interface.
-   **Purpose:** To achieve abstraction and support multiple inheritance of type (a class can implement multiple interfaces).
-   **Example in test automation:** The `WebDriver` interface defines the contract for browser automation. `ChromeDriver`, `FirefoxDriver` all implement this interface.

```
