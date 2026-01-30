---
title: "TCS-4"
date: 2026-01-30
draft: false
---

---

## Original Questions

- Tcs Interview Questions:-
-----------------------
1.Tell me about your?
2.How will you rate your self in selenium?
3.Write code to launch a browser?
4.What is webdriver and chromedriver?
5.What is class and interface?
6.What frame work your using in your project and explain it?
7.How will you rate your self in java?
8.Write a java program to fetch word from a sentence?
9.write a code for windowhandling?

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. Tell me about your?
Standard opener. Focus on professional experience, automation skills, tech stack, and a key achievement.

### 2. How will you rate your self in selenium?
Be honest and confident, backing it up with experience. "I would rate myself a 9 out of 10 in Selenium. I have extensive experience building, maintaining, and scaling Selenium WebDriver frameworks from scratch, covering complex UI scenarios, handling various synchronization issues, and integrating tests into CI/CD pipelines. I'm proficient in advanced concepts like Page Object Model, explicit waits, and parallel execution on Selenium Grid."

### 3. Write code to launch a browser?
This typically involves setting up the WebDriver and initializing a browser instance.

```java
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
// For a robust framework, use WebDriverManager to manage driver executables
// import io.github.bonigarcia.wdm.WebDriverManager;

public class BrowserLauncher {
    public static WebDriver launchChrome() {
        // Option 1: Using WebDriverManager (recommended for local execution)
        // WebDriverManager.chromedriver().setup();

        // Option 2: Manually setting system property (if driver is on PATH or specified)
        System.setProperty("webdriver.chrome.driver", "/path/to/chromedriver"); // Replace with actual path

        WebDriver driver = new ChromeDriver();
        driver.manage().window().maximize(); // Maximize browser window
        return driver;
    }

    public static void main(String[] args) {
        WebDriver driver = launchChrome();
        driver.get("https://www.google.com");
        System.out.println("Page Title: " + driver.getTitle());
        driver.quit();
    }
}
```

### 4. What is webdriver and chromedriver?
- **`WebDriver`:** It's an **interface** in Selenium that defines a common set of methods for interacting with web browsers (e.g., `get()`, `findElement()`, `click()`). It's the core of Selenium.
- **`ChromeDriver`:** It's a **class** that implements the `WebDriver` interface. It provides the specific implementation for automating the Google Chrome browser. When you write `WebDriver driver = new ChromeDriver();`, you are coding to the `WebDriver` interface while using the `ChromeDriver` implementation.

### 5. What is class and interface?
- **Class:** A blueprint or template for creating objects. It can define both data (fields) and behavior (methods). Objects are instances of classes.
- **Interface:** A contract. It defines a set of abstract methods that any class implementing the interface *must* provide concrete implementations for. It supports abstraction and multiple inheritance of type.

### 6. What frame work your using in your project and explain it?
"I use a **hybrid, data-driven test automation framework** built on Java.
- **Core Technologies:** TestNG as the test runner, Selenium WebDriver for UI automation, and REST-assured for API testing.
- **Design Pattern:** It's structured using the **Page Object Model (POM)** to separate UI logic from test logic, making tests maintainable.
- **Data Management:** Test data is externalized into JSON files and dynamically supplied to tests via TestNG's `@DataProvider`.
- **Reporting:** We use **ExtentReports** for generating rich HTML reports, integrated via TestNG listeners to capture screenshots on failure.
- **CI/CD:** The entire framework is built using Maven and integrated into a Jenkins pipeline for continuous integration and automated execution."

### 7. How will you rate your self in java?
"I would rate myself an 8 out of 10 in Java. I'm proficient in core Java concepts like OOP, Collections, Exception Handling, and multithreading, and I apply Java best practices to write clean, maintainable, and efficient code for our automation frameworks. I actively use modern Java features and continuously learn, but I recognize that a pure Java developer might have deeper specialized knowledge."

### 8. Write a java program to fetch word from a sentence?
This usually means splitting a sentence into individual words.

```java
import java.util.Arrays;
import java.util.List;

public class WordFetcher {
    public static List<String> fetchWords(String sentence) {
        if (sentence == null || sentence.trim().isEmpty()) {
            return List.of(); // Returns an empty immutable list (Java 9+)
        }
        // Use regex to split by one or more whitespace characters
        String[] wordsArray = sentence.trim().split("\\s+");
        return Arrays.asList(wordsArray);
    }

    public static void main(String[] args) {
        String sentence = "  Java is a  powerful language. ";
        List<String> words = fetchWords(sentence);
        System.out.println("Words in sentence: " + words);
        // Output: [Java, is, a, powerful, language.]
    }
}
```

### 9. write a code for windowhandling?
To switch to a newly opened browser window/tab:

```java
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.By;
import java.time.Duration;
import java.util.Set;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.support.ui.ExpectedConditions;

public class WindowHandler {
    public void switchToNewWindow(WebDriver driver, WebElement linkThatOpensNewWindow) {
        String originalWindowHandle = driver.getWindowHandle(); // Get the current window's ID
        
        linkThatOpensNewWindow.click(); // Perform action that opens a new window

        // Wait for the new window to appear
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        wait.until(ExpectedConditions.numberOfWindowsToBe(2));

        Set<String> allWindowHandles = driver.getWindowHandles(); // Get all window IDs

        for (String handle : allWindowHandles) {
            if (!handle.equals(originalWindowHandle)) {
                driver.switchTo().window(handle); // Switch to the new window
                break;
            }
        }
        // Now 'driver' is focused on the new window
        // You can interact with elements in this new window
        System.out.println("New window title: " + driver.getTitle());

        // To switch back to original:
        // driver.close(); // Close the new window
        // driver.switchTo().window(originalWindowHandle); // Switch back to original
    }
}
```
