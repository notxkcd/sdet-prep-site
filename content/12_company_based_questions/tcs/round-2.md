---
title: "TCS-2"
date: 2026-01-30
draft: false
---

---

## Original Questions

- TCS Second round -2
-----------------------------
1.Difference between product backlog and sprint backlog. 
2.How do we use Variable and class which is same in another class in java .
3.API postman tool extensions
4.How do we use code in API postman tool for taking results.
5.Oops concept .
6.Selenium latest software version .
7.Are you learning any new tool
8.Which tool are you using for raising bugs.

---

## Answers

### 1. Difference between product backlog and sprint backlog.
-   **Product Backlog:** This is the master list of everything that might be needed in the product. It contains all features, requirements, enhancements, and fixes. It's owned and prioritized by the **Product Owner**. It's a living document for the entire lifecycle of the project.

-   **Sprint Backlog:** This is a subset of the Product Backlog. It contains only the items that the development team has committed to completing in the **current sprint**. It's owned and managed by the **Development Team**. A new sprint backlog is created for each sprint.

| Feature         | Product Backlog                               | Sprint Backlog                                  |
| :-------------- | :-------------------------------------------- | :---------------------------------------------- |
| **Owner**       | Product Owner                                 | Development Team                                |
| **Scope**       | All desired features for the entire product   | Only the work planned for the current sprint    |
| **Duration**    | Lifespan of the project                       | Lifespan of one sprint                          |
| **Source**      | Business requirements, user feedback, etc.    | Pulled from the top of the Product Backlog      |

### 2. How do we use Variable and class which is same in another class in java .
The question is ambiguous, but it likely means "How do you access members (variables and methods) of one class from another class?".

1.  **Creating an Object:** The most common way. You create an instance (object) of the class you want to use, and then call its `public` members using the object reference.
    ```java
    ClassA objA = new ClassA();
    objA.publicMethod();
    int value = objA.publicVariable;
    ```
2.  **Inheritance:** If `ClassB` `extends` `ClassA`, it inherits all of `ClassA`'s `public` and `protected` members and can use them directly.
3.  **Static Members:** If the variable or method in `ClassA` is `static`, you don't need to create an object. You can access it directly using the class name: `ClassA.staticMethod();`.

### 3. API postman tool extensions
Postman itself is a complete application. It doesn't have "extensions" in the same way a web browser does. However, it integrates with many other tools and has features that extend its core functionality:
-   **Newman:** The command-line runner for Postman. It allows you to run your Postman collections from a terminal or as part of a CI/CD pipeline.
-   **API Mocking:** Postman allows you to create mock servers that return example responses, which is useful for testing a client when the real API isn't ready.
-   **API Monitoring:** You can set up monitors to run your collections on a schedule in Postman's cloud to check for API health and performance.
-   **Integrations:** Postman can integrate with tools like GitHub (to sync your collections), Jenkins (to run Newman), and many others.

### 4. How do we use code in API postman tool for taking results.
You use JavaScript code in the **"Tests"** tab of a request. This code runs *after* the response is received.
-   **Accessing the response:** The response data is available in the `pm.response` object.
-   **Writing Assertions:** You use `pm.test()` to define an assertion. Inside, you can use Chai.js assertion library syntax (`pm.expect()`) to validate the results.

```javascript
// Example Postman test script
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Response body contains a user with the correct ID", function () {
    // Parse the JSON response
    const jsonData = pm.response.json();
    // Assert a value from the response
    pm.expect(jsonData.data.id).to.eql(2);
});
```

### 5. Oops concept .
The four pillars:
-   **Encapsulation:** Bundling data and methods, hiding implementation (Page Object Model).
-   **Abstraction:** Hiding complexity, showing only essential features (`WebDriver` interface).
-   **Inheritance:** Reusing code from a parent class (`BaseTest` class).
-   **Polymorphism:** Method overriding (e.g., in page objects) and overloading (e.g., utility methods).

### 6. Selenium latest software version .
"The latest major version is **Selenium 4**. As of my last update, the specific minor versions are constantly being updated, but the key is that we are on the Selenium 4.x track, which is fully W3C WebDriver protocol compliant." (A quick search before an interview can give you the exact latest version, e.g., 4.1.2, 4.2.0, etc., which shows you are current).

### 7. Are you learning any new tool
This shows you are passionate and proactive about your career. Always have an answer.
-   "Yes, I'm currently dedicating time to learning **Playwright**. I'm interested in its different architectural approach, particularly its auto-waits and tracing capabilities, to see how it compares to Selenium for handling modern, dynamic web applications."
-   "I've been learning **k6** for performance testing. I want to expand my skills beyond functional testing and be able to contribute to load and stress testing of our APIs."

### 8. Which tool are you using for raising bugs.
"We use **Jira** for all bug tracking and defect management. I'm responsible for writing clear, detailed bug reports that include steps to reproduce, expected vs. actual results, environment details, and attaching relevant logs and screenshots."
