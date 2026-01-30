---
title: "Cognizant-4"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

Cognizant Level 1
-----------------
1) program for descending order
2) program for position
3)program for vowels count 
4)difference between interface and abstract
5)overload and override
6)write a code for takescreenshots
7)how to handle frames
8)difference between out and post
9)explain code for errors  which you are facing in Api
10) 200 and 201 explain
11)command line in Maven
12 )explain super keyword
13)explain static and final keyword
14)encapsulation
15) Child extends parent

Parent obj = new child();
Child obj= new parent():
Which which obj creation is correct for over riding above class

---

## Answers (No-BS Java QA / SDET Explanations)

### 1) program for descending order
This usually refers to sorting an array or list in descending order.

```java
import java.util.Arrays;
import java.util.Collections;

public class DescendingSort {
    public static void sortArrayDescending(int[] arr) {
        // For primitive arrays, you can convert to Integer array and use Collections.reverseOrder()
        Integer[] IntegerArr = Arrays.stream(arr).boxed().toArray(Integer[]::new);
        Arrays.sort(IntegerArr, Collections.reverseOrder());
        System.out.println("Sorted Descending: " + Arrays.toString(IntegerArr));
    }

    public static void main(String[] args) {
        int[] numbers = {5, 1, 4, 2, 8};
        sortArrayDescending(numbers); // Output: [8, 5, 4, 2, 1]
    }
}
```

### 2) program for position
This is too vague. Clarify with the interviewer. It could mean:
-   Finding the index of an element in an array/list.
-   Finding the position of a substring in a string.
-   Finding the position of a `WebElement` on a page (`element.getLocation()`).

Assuming finding the index of an element:
```java
public int findElementPosition(int[] arr, int target) {
    for (int i = 0; i < arr.length; i++) {
        if (arr[i] == target) {
            return i; // Return the first occurrence index
        }
    }
    return -1; // Not found
}
```

### 3) program for vowels count
```java
public int countVowels(String str) {
    if (str == null) return 0;
    int count = 0;
    String vowels = "aeiouAEIOU";
    for (char c : str.toCharArray()) {
        if (vowels.indexOf(c) != -1) {
            count++;
        }
    }
    return count;
}
```

### 4) difference between interface and abstract
-   **Interface:** Defines a contract (`implements`). Can't have constructors. Class can implement multiple interfaces.
-   **Abstract Class:** Can have abstract and concrete methods (`extends`). Can have instance variables and constructors. Class can extend only one abstract class.

### 5) overload and override
-   **Overload:** Same method name, different parameters, same class (compile-time polymorphism).
-   **Override:** Same method signature, child class provides specific implementation for parent's method (run-time polymorphism).

### 6) write a code for takescreenshots
```java
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import java.io.File;
import java.io.IOException;
import org.apache.commons.io.FileUtils; // From Apache Commons IO

public void takeScreenshot(WebDriver driver, String filePath) {
    File srcFile = ((TakesScreenshot) driver).getScreenshotAs(OutputType.FILE);
    try {
        FileUtils.copyFile(srcFile, new File(filePath));
    } catch (IOException e) {
        e.printStackTrace();
    }
}
```

### 7) how to handle frames
Use `driver.switchTo().frame("frameNameOrId")` to switch into a frame, and `driver.switchTo().defaultContent()` to switch back to the main page.

### 8) difference between out and post
This is likely a typo for **`PUT`** and `POST`.
-   **`PUT`:** Replaces an existing resource (idempotent).
-   **`POST`:** Creates a new resource (not idempotent).

### 9) explain code for errors which you are facing in Api
This is too vague. Likely "exceptions". Mention common API-related exceptions/errors:
-   `IOException` (network issues).
-   `JsonProcessingException` (malformed JSON).
-   HTTP status codes `4xx` (client errors) or `5xx` (server errors).
-   `AssertionError` from failed validations.

### 10) 200 and 201 explain
-   **`200 OK`:** General success status code. Request has succeeded.
-   **`201 Created`:** The request has been fulfilled, and a new resource has been created. Usually returned after a `POST` request.

### 11) command line in Maven
Common Maven command-line commands:
-   `mvn clean`: Cleans the project (deletes `target` directory).
-   `mvn compile`: Compiles source code.
-   `mvn test`: Runs all tests.
-   `mvn package`: Compiles, tests, and packages code into a JAR/WAR.
-   `mvn install`: Packages and installs into local Maven repository.

### 12) explain super keyword
`super` refers to the **parent class (superclass)** object.
-   `super()`: Calls the parent class's constructor (must be the first statement).
-   `super.methodName()`: Calls a method from the parent class (useful when overridden).

### 13) explain static and final keyword
-   **`static`:** Member belongs to the **class**, not an object. Single copy shared by all instances.
-   **`final`:** Makes a variable a constant, a method non-overridable, or a class non-extendable.

### 14) encapsulation
A core OOP concept where data (fields) and methods that operate on them are bundled into a single unit (class). Internal state is hidden via `private` access modifiers, and controlled access is provided via `public` getters/setters.

### 15) Child extends parent

This implies an inheritance hierarchy.
```java
class Parent {}
class Child extends Parent {}
```

#### Parent obj = new child();
This is **correct** and demonstrates polymorphism. A parent class reference (`Parent obj`) can hold an object of a child class (`new Child()`). This is common in real projects (e.g., `WebDriver driver = new ChromeDriver();`).

#### Child obj= new parent():
This is **incorrect**. A child class reference cannot hold an object of its parent class, because the parent object does not contain all the members of the child. This would cause a compile-time error.

#### Which which obj creation is correct for over riding above class
The statement `Parent obj = new Child();` is correct. When `obj.overriddenMethod();` is called, the child's version of the method will execute due to run-time polymorphism.
The code given (`Child extends parent`) doesn't show any overriding. If `Parent` had a method `doSomething()` and `Child` overrode it, then `Parent obj = new Child(); obj.doSomething();` would call the child's `doSomething()`.
