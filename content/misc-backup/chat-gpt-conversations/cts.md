---
title: 'CTS Interview Questions'
date: 2026-01-25T22:32:17+05:30
draft: false
---

# CTS Interview Questions - Complete Answers

## Personal & Behavioral
- [1. Tell about yourself](#1-tell-about-yourself)
- [2. If you find a bug but developer won't accept it, how will you handle?](#2-if-you-find-a-bug-but-developer-wont-accept-it-how-will-you-handle)
- [25. What challenges faced in previous project?](#25-what-challenges-faced-in-previous-project)
- [24. What to discuss in retrospective meeting?](#24-what-to-discuss-in-retrospective-meeting)

## Java & OOPs Concepts
- [3. Explain constructor](#3-explain-constructor)
- [4. Explain `final`, `static`](#4-explain-final-static)
- [5. Difference between `this` and `super`](#5-difference-between-this-and-super)
- [8. Explain encapsulation](#8-explain-encapsulation)

## Programming Questions
- [6. Reverse string word by word](#6-reverse-string-word-by-word)
- [7. Print and sort array values](#7-print-and-sort-array-values)
- [13. Find greater number: a=10, b=15](#13-find-greater-number-a10-b15)

## Selenium Automation
- [2. OOPs in Selenium](#2-oops-in-selenium)
- [9. Mostly used locators in project](#9-mostly-used-locators-in-project)
- [11. Types of XPath](#11-types-of-xpath)
- [12. Window handles usage](#12-window-handles-usage)
- [20. WebElement methods (Facebook login example)](#20-webelement-methods-facebook-login-example)

## Testing Concepts
- [10. Smoke vs Sanity Testing](#10-smoke-vs-sanity-testing)
- [14. Test case format in Xray](#14-test-case-format-in-xray)
- [15. Test case design techniques (Manual)](#15-test-case-design-techniques-manual)
- [16. Build information source](#16-build-information-source)
- [18. What is RTM?](#18-what-is-rtm)
- [19. Black Box Testing](#19-black-box-testing)
- [21. Hook class (Cucumber)](#21-hook-class-cucumber)
- [22. Severity vs Priority](#22-severity-vs-priority)

## Framework & Process
- [23. Project Framework](#23-project-framework)

---

# Answers

## Personal & Behavioral

### <a id="1-tell-about-yourself"></a>1. Tell about yourself
Keep it professional: 2-3 min intro covering education, skills, experience, and current role. Example: "I'm a QA Engineer with 3+ years experience in Selenium automation and manual testing. I specialize in Java-based TestNG frameworks and have worked on e-commerce projects..."
[Back to Top](#personal--behavioral)

### <a id="2-if-you-find-a-bug-but-developer-wont-accept-it-how-will-you-handle"></a>2. If you find a bug but developer won't accept it, how will you handle?
- Reproduce with clear steps + screenshots/video  
- Reference exact requirements/RTM  
- Escalate to Tech Lead/Manager with evidence  
- Log as "Deferred" if business approves workaround  
[Back to Top](#personal--behavioral)

### <a id="25-what-challenges-faced-in-previous-project"></a>25. What challenges faced in previous project?
- Dynamic elements causing flaky tests (solution: explicit waits + custom locators)  
- Parallel execution failures (solution: ThreadLocal WebDriver)  
- Tight deadlines (solution: prioritized smoke suite + CI/CD integration)  
[Back to Top](#personal--behavioral)

### <a id="24-what-to-discuss-in-retrospective-meeting"></a>24. What to discuss in retrospective meeting?
- What went well?  
- What can be improved?  
- Action items with owners  
- Blockers and solutions  
[Back to Top](#personal--behavioral)

## Java & OOPs Concepts

### <a id="3-explain-constructor"></a>3. Explain constructor
Special method called when object is created. Same name as class, no return type.  
```java
public class Test {
    public Test() { // Default constructor
        System.out.println("Object created");
    }
    public Test(int a) { // Parameterized
        System.out.println("Value: " + a);
    }
}
```
[Back to Top](#java--oops-concepts)

### <a id="4-explain-final-static"></a>4. Explain `final`, `static`
- **final**: Cannot be changed. Variables (constants), methods (cannot override), classes (cannot extend)  
- **static**: Belongs to class, not object. Memory allocated once. Variables/methods accessible without object creation  
[Back to Top](#java--oops-concepts)

### <a id="5-difference-between-this-and-super"></a>5. Difference between `this` and `super`
| `this` | `super` |
|--------|---------|
| Current class object | Parent class object |
| Access current class members | Access parent class members |
| Call current class constructor | Call parent class constructor |
[Back to Top](#java--oops-concepts)

### <a id="8-explain-encapsulation"></a>8. Explain encapsulation
Wrapping data (variables) and methods together in a class, hiding internal details using access modifiers (private + getters/setters).  
```java
public class Employee {
    private String name; // Data hiding
    
    public String getName() { return name; } // Public access
    public void setName(String name) { this.name = name; }
}
```
[Back to Top](#java--oops-concepts)

## Programming Questions

### <a id="6-reverse-string-word-by-word"></a>6. Reverse string word by word
```java
public static String reverseWords(String str) {
    String[] words = str.split(" ");
    StringBuilder reversed = new StringBuilder();
    for (int i = words.length - 1; i >= 0; i--) {
        reversed.append(words[i]).append(" ");
    }
    return reversed.toString().trim();
}
// "Hello World" → "World Hello"
```
[Back to Top](#programming-questions)

### <a id="7-print-and-sort-array-values"></a>7. Print and sort array values
```java
int[] arr = {5, 2, 8, 1, 9};
System.out.println("Original: " + Arrays.toString(arr));

// Print
for(int num : arr) {
    System.out.print(num + " ");
}

// Sort
Arrays.sort(arr);
System.out.println("Sorted: " + Arrays.toString(arr));
```
[Back to Top](#programming-questions)

### <a id="13-find-greater-number-a10-b15"></a>13. Find greater number: a=10, b=15
```java
int a = 10, b = 15;
int greater = (a > b) ? a : b;
System.out.println("Greater: " + greater); // Output: 15

// Or using Math.max
int max = Math.max(a, b);
```
[Back to Top](#programming-questions)

## Selenium Automation

### <a id="2-oops-in-selenium"></a>2. OOPs in Selenium
- **Inheritance**: BaseTest class → Test classes  
- **Polymorphism**: Multiple Page classes implementing same interface  
- **Encapsulation**: WebDriver private in Page class, public methods  
- **Abstraction**: Page Object Model hiding implementation  
[Back to Top](#selenium-automation)

### <a id="9-mostly-used-locators-in-project"></a>9. Mostly used locators in project
1. **ID** (fastest) → `driver.findElement(By.id("username"))`  
2. **CSS Selector** → `driver.findElement(By.cssSelector("#login input"))`  
3. **XPath** → `//input[@name='email']`  
[Back to Top](#selenium-automation)

### <a id="11-types-of-xpath"></a>11. Types of XPath
| Type | Syntax | Example |
|------|--------|---------|
| **Absolute** | `/html/body/div/input` | Full path (slow, brittle) |
| **Relative** | `//input[@id='email']` | Starts with // (recommended) |
| **Contains** | `//input[contains(@id,'user')]` | Partial match |
| **Starts-with** | `//input[starts-with(@name,'pass')]` | Begins with text |
[Back to Top](#selenium-automation)

### <a id="12-window-handles-usage"></a>12. Window handles usage
```java
// Get current window
String mainWindow = driver.getWindowHandle();

// Get all windows after clicking new tab/link
Set<String> windows = driver.getWindowHandles();

for(String window : windows) {
    if(!window.equals(mainWindow)) {
        driver.switchTo().window(window);
        // Work on new window
        driver.close();
    }
}
driver.switchTo().window(mainWindow); // Back to main
```
[Back to Top](#selenium-automation)

### <a id="20-webelement-methods-facebook-login-example"></a>20. WebElement methods (Facebook login example)
```java
WebElement email = driver.findElement(By.xpath("//input[@name='email']"));
email.sendKeys("test@gmail.com");           // Type text
email.clear();                              // Clear field
email.click();                              // Click element
System.out.println(email.getText());        // Get text
System.out.println(email.isDisplayed());    // Visible?
email.submit();                             // Form submit
```
[Back to Top](#selenium-automation)

## Testing Concepts

### <a id="10-smoke-vs-sanity-testing"></a>10. Smoke vs Sanity Testing
| Smoke | Sanity |
|-------|--------|
| Basic functionality check | Specific functionality after fix |
| After new build deployment | After major code changes |
| Quick (10-15 mins) | Detailed (30-60 mins) |
| **Example**: Login + Home page loads | **Example**: Login + specific Payment flow |
[Back to Top](#testing-concepts)

### <a id="14-test-case-format-in-xray"></a>14. Test case format in Xray
```
Test: TC_Login_001
Summary: Verify valid login
Precondition: User registered
Steps:
1. Navigate to login page
2. Enter valid credentials
3. Click Login
Expected: User lands on Dashboard
```
[Back to Top](#testing-concepts)

### <a id="15-test-case-design-techniques-manual"></a>15. Test case design techniques (Manual)
- **BC4** (Boundary Value Analysis)  
- **EC** (Equivalence Class Partitioning)  
- **DT** (Decision Table)  
- **SF** (State Transition)  
- **ET** (Error Guessing)  
[Back to Top](#testing-concepts)

### <a id="16-build-information-source"></a>16. Build information source
- **Jenkins dashboard** → Build history/numbers  
- **Artifactory/Nexus** → Deployed JAR/WAR files  
- **Slack/Teams notifications** → Build success alerts  
- **Confluence** → Release notes  
[Back to Top](#testing-concepts)

### <a id="18-what-is-rtm"></a>18. What is RTM?
**Requirement Traceability Matrix** maps:  
Requirements ↔ Test Cases ↔ Defects  
Ensures 100% coverage, no orphaned test cases.
[Back to Top](#testing-concepts)

### <a id="19-black-box-testing"></a>19. Black Box Testing
Testing without knowing internal code structure. Focus on:  
- Inputs → Expected Outputs  
- Functional requirements  
- UI validation  
**Types**: BVA, ECP, Decision Tables  
[Back to Top](#testing-concepts)

### <a id="21-hook-class-cucumber"></a>21. Hook class (Cucumber)
```java
public class Hooks {
    @Before("@smoke")                    // Before smoke tests
    public void beforeSmoke() { setup(); }
    
    @After()                            // After every scenario
    public void tearDown() { driver.quit(); }
    
    @AfterStep                           // After each step
    public void screenshotOnFailure() { /* logic */ }
}
```
[Back to Top](#testing-concepts)

### <a id="22-severity-vs-priority"></a>22. Severity vs Priority
| Severity | Priority |
|----------|----------|
| Impact on system | Urgency to fix |
| **Critical**: App crash | **High**: Business blocker |
| **Major**: Wrong calculation | **Medium**: Non-critical UI |
| **Minor**: Cosmetic | **Low**: Nice-to-have |
[Back to Top](#testing-concepts)

## Framework & Process

### <a id="23-project-framework"></a>23. Project Framework
**Hybrid Framework** (Page Object + TestNG + ExtentReports):  
```
src/
├── pages/           # Page Objects
├── utils/           # Helpers (Excel, Logs)
├── testData/        # Test data
├── tests/           # Test classes
└── reports/         # ExtentReports
```
**Flow**: TestNG.xml → Test classes → Page classes → WebDriver actions  
[Back to Top](#framework--process)