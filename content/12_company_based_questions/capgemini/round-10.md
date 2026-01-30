---
title: "Capgemini-10"
date: 2026-01-30
draft: false
---

---

## Original Questions

- Capgemini Interview Questions- First Round - F2F - Virtual- 35 mins
1. Explain yourself
2. What are the OOPS concept you are using in your project
3. Polymorphism (Overload and Override)
4. Collection and it types explanation
5. What is the output for given program
class Parent{
void show(){
- system.out.println("parent method");
}
}
- class Child extends Parent{
- private void show(){
- system.out.println("child method");
}
}
- public class Main{
- public static void main(String[]args){
- Parent obj= new Child();
obj.show();
}
6. Explain the cucumber framework
7. Whats is scenario, scenario outline and Background Keywords
8. What are the types of waits and explain where it is used
9. Difference between the severity and priority
10. Difference between string buffer and string builder
11. Explain your latest project ownership
12. Java program - Reverse string

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. Explain yourself
Standard opener. Keep it concise, professional, and focus on your relevant experience (automation skills, tech stack, achievements).

### 2. What are the OOPS concept you are using in your project
"We apply all four OOP concepts in our project:
-   **Encapsulation:** Through the Page Object Model, where locators and methods for a page are encapsulated.
-   **Abstraction:** Using interfaces like `WebDriver` and our own custom interfaces.
-   **Inheritance:** Through `BaseTest` and `BasePage` classes.
-   **Polymorphism:** Through method overloading (e.g., custom `click()` methods) and overriding (e.g., page-specific `verifyPageLoaded()` methods)."

### 3. Polymorphism (Overload and Override)
-   **Method Overloading:** Multiple methods in the same class with the same name but different parameter lists. This is compile-time polymorphism.
-   **Method Overriding:** A subclass provides a specific implementation for a method already defined in its superclass. This is run-time polymorphism, indicated by `@Override`.

### 4. Collection and it types explanation
The Java Collections Framework (`java.util` package) provides interfaces and classes for grouping objects.
-   **`List`:** Ordered collection, allows duplicates (e.g., `ArrayList`, `LinkedList`).
-   **`Set`:** Unordered collection, does not allow duplicates (e.g., `HashSet`, `LinkedHashSet`).
-   **`Map`:** Stores key-value pairs; keys must be unique, values can be duplicated (e.g., `HashMap`, `TreeMap`).

### 5. What is the output for given program
```java
class Parent{
void show(){
System.out.println("parent method");
}
}
class Child extends Parent{
private void show(){ // This method is private in Child
System.out.println("child method");
}
}
public class Main{
public static void main(String[]args){
Parent obj= new Child();
obj.show(); // Calls Parent's show()
}
}
```
**Output:** `parent method`

**Explanation:**
1.  In Java, `private` methods are not inherited. They are effectively sealed within their class.
2.  Therefore, the `private void show()` method in `Child` is a *new*, unrelated method, not an override of `Parent`'s `show()`.
3.  `Parent obj = new Child();` is valid polymorphism.
4.  When `obj.show();` is called, because `obj` is of type `Parent`, and `Parent`'s `show()` method is `public` (default access in this case), the `Parent` class's `show()` method is invoked. If the `Child` class's `show()` method were `public` or `protected`, then the child's `show()` would have been called.

### 6. Explain the cucumber framework
(Repeated). A BDD framework using Gherkin (`Given/When/Then`) in `.feature` files, linked to Java step definitions, executed via a runner class. Promotes collaboration and living documentation.

### 7. Whats is scenario, scenario outline and Background Keywords
-   **`Scenario`:** A single, concrete test case in a feature file.
-   **`Scenario Outline`:** A template for a scenario that runs multiple times with different data provided in an `Examples` table.
-   **`Background`:** A section in a feature file containing `Given` steps that run before every scenario in that file, to set up common preconditions.

### 8. What are the types of waits and explain where it is used
-   **Implicit Wait (Bad):** Global setting, polls DOM. Avoid.
-   **Explicit Wait (Good):** `WebDriverWait` for specific `ExpectedConditions`. Used for dynamic elements.
-   **Fluent Wait (Advanced Explicit Wait):** Configurable polling interval and ignored exceptions. Used for fine-grained control.

### 9. Difference between the severity and priority
-   **Severity:** Technical impact of a bug (e.g., Critical, Major, Minor). Decided by QA.
-   **Priority:** Business urgency to fix a bug (e.g., High, Medium, Low). Decided by Product Owner.

### 10. Difference between string buffer and string builder
Both are mutable string classes:
-   **`StringBuilder`:** Not thread-safe, faster. Use for single-threaded string manipulation.
-   **`StringBuffer`:** Thread-safe (synchronized), slower. Use only if modification from multiple threads is required.

### 11. Explain your latest project ownership
This asks for a specific example of your responsibility and leadership.
"In my latest project, I took ownership of designing and implementing the end-to-end API test suite for our new user authentication microservice. This involved:
-   Analyzing the API specifications and creating test plans.
-   Developing the REST-assured framework to cover all CRUD operations and authentication flows.
-   Integrating these tests into our CI/CD pipeline.
-   Ensuring robust test data management for user creation and deletion.
This contributed to a stable and performant authentication service, and I was the primary go-to person for API quality within that microservice team."

### 12. Java program - Reverse string
`new StringBuilder(str).reverse().toString();`
