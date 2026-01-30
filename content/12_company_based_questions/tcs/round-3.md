---
title: "TCS-3"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

TCS interview questions:
-----------------------

Round 1:

1.explain about ur project and framewrok?
2.where did u use constructor in ur project?
3.explain about oops concept?
4.how u handle pop up in selenium?
5.write code for string reverse?

Round 2:

1.explain about ur project and framewrok?
2.can we create object fr abstract class?if no, then how we can access methods from abstarct class?
3.we are searching webelemnnt in webpage but there is no such element then what is selenium exceptions for single webelement and multiple webelement?
4.how u handle windows in selenium?
5.how to find second largest number in array?

Round 3:

1.explain about ur project and framewrok?
2.can we create object fr abstract class?if no, then how we can access methods from abstarct class?
3.i want to run single test case multiple times in testng?how to do?
4.how to delete code in github? 
5.how to find duplicate number in array?
6.how to reverse number in java?

---

## Answers (No-BS Java QA / SDET Explanations)

### Round 1

#### 1. explain about ur project and framewrok?
Standard question. Describe your project's domain and your role. For the framework, explain the architecture: Java + TestNG + Selenium/REST-assured, Page Object Model, data-driven approach using external files (JSON/Excel), Maven for build, and Jenkins for CI/CD.

#### 2. where did u use constructor in ur project?
"I use constructors primarily in our **Page Object Model (POM)** classes. Each page object class has a constructor that accepts the `WebDriver` instance as a parameter. This is crucial for dependency injection, ensuring that the page object has a driver to interact with the browser.

```java
public class HomePage {
    private WebDriver driver;
    public HomePage(WebDriver driver) {
        this.driver = driver;
    }
    // ... methods using the driver
}
```
"

#### 3. explain about oops concept?
The four pillars: Encapsulation, Abstraction, Inheritance, Polymorphism. Have QA-centric examples ready for each (e.g., POM for Encapsulation, `WebDriver` interface for Abstraction).

#### 4. how u handle pop up in selenium?
This depends on the type of "pop up".
-   **JavaScript Alert:** Use `driver.switchTo().alert()`. Then you can `.accept()`, `.dismiss()`, or `.getText()`.
-   **HTML Modal/Dialog:** This is just a `div` styled to look like a pop up. You handle it like any other web element: find its locator (e.g., the close button) and `.click()` it.
-   **New Window/Tab:** This requires switching window handles using `driver.getWindowHandles()` and `driver.switchTo().window(handle)`.

#### 5. write code for string reverse?
The clean, standard library way:
`new StringBuilder(str).reverse().toString();`

### Round 2

#### 1. explain about ur project and framewrok?
(Repeated)

#### 2. can we create object fr abstract class?if no, then how we can access methods from abstarct class?
-   **Can we create an object?** No. You cannot instantiate an abstract class directly using `new`. That's its purpose.
-   **How to access methods?** You create a **concrete child class** that `extends` the abstract class. Then you create an object of the child class. This child object inherits the (non-private) methods from the abstract parent and can call them.

```java
abstract class Base {
    public void concreteMethod() { System.out.println("Hello"); }
}

class Child extends Base { }

// In main method:
Child obj = new Child();
obj.concreteMethod(); // Accessing the method via the child object.
```

#### 3. we are searching webelemnnt in webpage but there is no such element then what is selenium exceptions for single webelement and multiple webelement?
-   For a single `WebElement` (`driver.findElement()`): Throws `NoSuchElementException`.
-   For multiple `WebElement`s (`driver.findElements()`): Throws **no exception**. It simply returns an empty `List<WebElement>`.

#### 4. how u handle windows in selenium?
Using window handles:
1.  Get the current window's ID: `driver.getWindowHandle()`.
2.  Get all window IDs: `driver.getWindowHandles()`.
3.  Switch between them: `driver.switchTo().window(windowId)`.

#### 5. how to find second largest number in array?
Use streams for a clean solution.

```java
import java.util.Arrays;
import java.util.Comparator;

public int findSecondLargest(int[] arr) {
    return Arrays.stream(arr)
                 .distinct()
                 .boxed()
                 .sorted(Comparator.reverseOrder())
                 .skip(1)
                 .findFirst()
                 .orElseThrow(IllegalStateException::new);
}
```

### Round 3

#### 1. explain about ur project and framewrok?
(Repeated)

#### 2. can we create object fr abstract class?if no, then how we can access methods from abstarct class?
(Repeated) You access them through an instance of a concrete subclass that extends the abstract class.

#### 3. i want to run single test case multiple times in testng?how to do?
You use the `invocationCount` attribute in the `@Test` annotation.

```java
@Test(invocationCount = 10)
public void myTest() {
    // This test logic will be executed 10 times.
}
```
To run them in parallel, you can add `threadPoolSize`: `@Test(invocationCount = 10, threadPoolSize = 5)`.

#### 4. how to delete code in github?
"Deleting code" is just another change that you manage through Git.
1.  **Delete the file locally:** `rm myFile.java` or delete it from your IDE.
2.  **Stage the deletion:** `git add myFile.java` or `git rm myFile.java`. `git status` will show the file as "deleted".
3.  **Commit the deletion:** `git commit -m "refactor: Remove obsolete MyFile.java"`
4.  **Push the change:** `git push origin main`. This will delete the file from the remote repository on GitHub.

To revert a bad commit, you would use `git revert <commit_hash>`.

#### 5. how to find duplicate number in array?
Use a `Set` to track seen numbers.

```java
import java.util.HashSet;
import java.util.Set;

public void findDuplicates(int[] arr) {
    Set<Integer> seen = new HashSet<>();
    Set<Integer> duplicates = new HashSet<>();
    for (int num : arr) {
        if (!seen.add(num)) { // .add() returns false if element is already present
            duplicates.add(num);
        }
    }
    System.out.println("Duplicates: " + duplicates);
}
```

#### 6. how to reverse number in java?
You can do this mathematically with modulo and division, or by converting to a string.

```java
// Mathematical way (handles positive integers)
public int reverseNumber(int num) {
    int reversed = 0;
    while (num != 0) {
        int digit = num % 10;
        reversed = reversed * 10 + digit;
        num /= 10;
    }
    return reversed;
}

// String way (simpler to write)
public int reverseNumberString(int num) {
    String reversedStr = new StringBuilder(String.valueOf(Math.abs(num))).reverse().toString();
    return Integer.parseInt(reversedStr) * (int) Math.signum(num);
}
```
The mathematical way is what interviewers are usually looking for.
