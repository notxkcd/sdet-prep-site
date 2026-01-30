---
title: "TCS"
date: 2026-01-30
draft: false
---

---

## Original Questions

- TCS First round -1
--------------------------
1.What is oops?
2.What is abstraction? 
3.Explain stale element exception
4.Explain frame and syntax
5.Explain your project and framework
6.Explain api
7.Explain static?
8.Scenario and Scenario outline uses
9.Use of background keyword?
10.different types of API? 
11.what is method overriding? How to achieve it in your project? 
12.tools for API automation testing?
13.how you will give story points?
14.how will you handle frame? 
15.what is fluent wait? 
16.Explain about Jenkins?
17.how to create a built in Jenkins?
18.Explain your framework?

---

## Answers

### 1. What is oops?
Object-Oriented Programming. It's a programming paradigm based on the concept of "objects", which can contain data (fields or attributes) and code (procedures or methods). The main principles are Encapsulation, Abstraction, Inheritance, and Polymorphism.

### 2. What is abstraction?
Abstraction is the concept of hiding complex implementation details and showing only the essential features of the object. In Java, it's achieved using abstract classes and interfaces. The `WebDriver` interface in Selenium is a perfect example: your code interacts with the `WebDriver` type, abstracting away the specifics of whether it's a `ChromeDriver` or `FirefoxDriver`.

### 3. Explain stale element exception
`StaleElementReferenceException`. This happens when you have a reference to a `WebElement`, but the DOM changes (e.g., due to an AJAX call or navigation), and that element is removed or replaced. Your variable now points to something that is no longer attached to the DOM, hence it's "stale". The only solution is to re-find the element before interacting with it.

### 4. Explain frame and syntax
A "frame" or `iframe` is an HTML tag used to embed another HTML document within the current one. Selenium can only see one document context at a time (the main page or one specific frame).
**Syntax:** You must switch the driver's context to the frame before you can interact with elements inside it.
- `driver.switchTo().frame("frameNameOrId");`
- `driver.switchTo().frame(index);`
- `driver.switchTo().frame(WebElement frameElement);`
To get back out, you use: `driver.switchTo().defaultContent();`

### 5. Explain your project and framework
Standard question. Describe the project domain, your role, the framework architecture (POM, Data-Driven), and the tech stack (Java, Selenium, TestNG, Maven, Jenkins).

### 6. Explain api
Application Programming Interface. It's a set of rules and definitions that allows different software applications to communicate with each other. In web development, this is typically a web API (like a REST API) that uses HTTP requests to get or send data, usually in JSON format.

### 7. Explain static?
`static` is a Java keyword used to declare members that belong to the **class** itself, rather than to any specific instance (object) of the class.
-   **`static` variable:** A class-level variable. There is only one copy, shared among all objects of that class.
-   **`static` method:** A class-level method. It can be called without creating an object of the class (e.g., `Math.random()`). It can only access other static members.
-   **Use Case in QA:** Utility methods that don't depend on object state, like a custom date formatter or a data generator, are often made `static`.

### 8. Scenario and Scenario outline uses
In Cucumber/Gherkin:
-   **`Scenario`:** A single, concrete test case. It runs once with hardcoded values.
-   **`Scenario Outline`:** A template for a data-driven test case. It runs multiple times, once for each row of data provided in an `Examples` table. Used to test the same logic with different inputs.

### 9. Use of background keyword?
In a Cucumber `.feature` file, the `Background` keyword is used to define a set of `Given` steps that are common to all scenarios in that file. It runs before each scenario, reducing repetition and making the scenarios cleaner.

### 10. different types of API?
-   **REST (Representational State Transfer):** The most common type for web services. It's an architectural style that uses standard HTTP methods (`GET`, `POST`, `PUT`, `DELETE`). It's stateless and typically uses JSON for data exchange.
-   **SOAP (Simple Object Access Protocol):** An older protocol. It's more rigid, uses XML for its message format, and has built-in standards for security and transactions (WS-Security).
-   **GraphQL:** A newer query language for APIs. It allows the client to request *exactly* the data it needs, which can be more efficient than REST, where endpoints often return fixed data structures.

### 11. what is method overriding? How to achieve it in your project?
Method overriding is a feature of polymorphism where a subclass provides a specific implementation for a method that is already defined in its parent class.
-   **How to achieve:** The method in the child class must have the same name, parameters, and return type as the method in the parent class. You use the `@Override` annotation to ensure you are correctly overriding a parent method.
-   **Project Example:** "In our framework, we have a `BasePage` class with a `verifyPageIsLoaded()` method. For the `ProductPage`, we override this method to add a specific check for the product price element, which is a condition unique to that page."

### 12. tools for API automation testing?
-   **REST-assured:** A powerful Java library for testing REST APIs. It provides a fluent, BDD-style syntax for writing expressive and maintainable tests.
-   **Postman:** An application for API development and testing. Great for manual/exploratory testing and can be used for automation via its Collection Runner and command-line tool, Newman.
-   **Karate:** A framework that combines API test automation, mocks, and performance testing into a single tool. Tests are written in a Gherkin-like syntax.

### 13. how you will give story points?
Story points are assigned during a **Planning Poker** session with the whole team. It's a relative estimation of effort based on complexity, uncertainty, and volume of work. Each team member privately chooses a Fibonacci-like number (1, 2, 3, 5, 8...). If estimates differ greatly, the team discusses the reasons for the high and low estimates to uncover hidden assumptions, then re-votes until a consensus is reached.

### 14. how will you handle frame?
Answered in question 4. Use `driver.switchTo().frame(...)` to enter a frame and `driver.switchTo().defaultContent()` to exit.

### 15. what is fluent wait?
A `FluentWait` is an advanced type of explicit wait in Selenium. It gives you more configuration options than a standard `WebDriverWait`. You can configure:
-   The maximum timeout.
-   The polling frequency (how often to check the condition).
-   Exceptions to ignore while polling.
`WebDriverWait` is just a convenient subclass of `FluentWait` with sensible defaults.

### 16. Explain about Jenkins?
Jenkins is an open-source automation server used to build CI/CD (Continuous Integration/Continuous Delivery) pipelines. For QA, it's the engine that automates the execution of our test suites, either on a schedule or triggered by code changes, and provides a central place to view results.

### 17. how to create a built in Jenkins?
The question likely means "how to create a **build** in Jenkins".
You create a "job" or "pipeline".
1.  On the Jenkins dashboard, click "New Item".
2.  Give it a name and choose the type. **"Pipeline"** is the modern, recommended choice.
3.  Configure the pipeline. The best practice is to choose "Pipeline script from SCM".
4.  Configure the SCM (Source Code Management) section to point to your Git repository.
5.  Jenkins will then look for a `Jenkinsfile` in your repository root. This file contains the pipeline definition as code, specifying stages like "Build", "Test", and "Deploy".
6.  When the job is run (manually or by a trigger), Jenkins executes the steps defined in the `Jenkinsfile`.

### 18. Explain your framework?
Standard question. Describe the architecture (POM), tech stack (Java/Selenium/TestNG), data-driven approach, reporting, and CI integration.
