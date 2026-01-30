---
title: "Infosys-5"
date: 2026-01-30
draft: false
---

---

## Original Questions

- Infosys L2 round questions
--------------------------
Tell about Yourself
Cucumber framework explanation
Project explanation
Agile methodologies 
Fibonacci series code
Reverse the string code
Selenium webdriver methods
Selenium webelement methods
How will you import your framework in git
Work flow of jira and what it is used for

---

## Answers (No-BS Java QA / SDET Explanations)

### Tell about Yourself
Standard opener. Focus on professional experience, automation skills, tech stack, and a key achievement.

### Cucumber framework explanation
Cucumber is a BDD (Behavior-Driven Development) framework.
-   **Purpose:** To bridge the communication gap between technical and non-technical stakeholders by writing tests in a human-readable language (Gherkin).
-   **Components:**
    -   **Feature Files:** `.feature` files containing scenarios written in Gherkin (`Given/When/Then`).
    -   **Step Definitions:** Java methods that implement the logic for each Gherkin step.
    -   **Runner Class:** A JUnit or TestNG class that triggers and configures the Cucumber tests.
-   **Workflow:** The runner class reads feature files, finds matching step definitions, executes the code, and generates reports.

### Project explanation
Standard. Describe the project domain, your role, the framework used, and key contributions.

### Agile methodologies
Agile is an iterative, incremental approach to software development emphasizing flexibility, collaboration, and rapid delivery of working software. Key principles include:
-   Short development cycles (sprints).
-   Continuous feedback and adaptation.
-   Customer collaboration.
-   Self-organizing teams.

### Fibonacci series code
The Fibonacci series is a sequence where each number is the sum of the two preceding ones, usually starting with 0 and 1. (0, 1, 1, 2, 3, 5, 8, ...)

```java
public class Fibonacci {
    public static void printFibonacci(int count) {
        int a = 0;
        int b = 1;
        System.out.print(a + ", " + b); // Print first two terms
        for (int i = 2; i < count; i++) {
            int next = a + b;
            System.out.print(", " + next);
            a = b;
            b = next;
        }
        System.out.println();
    }
}
```

### Reverse the string code
```java
public String reverseString(String str) {
    if (str == null) return null;
    return new StringBuilder(str).reverse().toString();
}
```

### Selenium webdriver methods
The `WebDriver` interface has many methods for browser interaction:
-   **Navigation:** `get(url)`, `navigate().to(url)`, `navigate().back()`, `navigate().forward()`, `navigate().refresh()`.
-   **Element Finding:** `findElement(By locator)`, `findElements(By locator)`.
-   **Browser Info:** `getTitle()`, `getCurrentUrl()`, `getPageSource()`.
-   **Window/Frame Handling:** `switchTo().window()`, `switchTo().frame()`, `switchTo().alert()`.
-   **Browser Management:** `manage().window().maximize()`, `manage().timeouts()`.
-   **Lifecycle:** `quit()`, `close()`.

### Selenium webelement methods
The `WebElement` interface represents an HTML element on a web page. Key methods:
-   `click()`: Clicks the element.
-   `sendKeys(CharSequence... keysToSend)`: Types text into an input field.
-   `getText()`: Gets the visible text of the element.
-   `getAttribute(String name)`: Gets the value of an attribute (e.g., `href`, `value`).
-   `isDisplayed()`: Checks if the element is visible.
-   `isEnabled()`: Checks if the element is enabled.
-   `isSelected()`: Checks if a checkbox or radio button is selected.
-   `clear()`: Clears the text from an input field.
-   `submit()`: Submits the form the element belongs to.

### How will you import your framework in git
"Importing a framework into Git is essentially adding it to version control.
1.  **Initialize Git:** Navigate to your framework's root directory in the terminal and run `git init`.
2.  **Stage Files:** Use `git add .` to stage all the files in your framework.
3.  **Commit:** Create the initial commit: `git commit -m "Initial commit of automation framework"`.
4.  **Create Remote Repository:** Go to GitHub/GitLab/Bitbucket and create a new empty repository.
5.  **Link Remote:** Link your local repository to the remote one: `git remote add origin <remote_repository_url>`.
6.  **Push:** Push your local code to the remote: `git push -u origin main` (or `master`).
After this, you manage your framework code using standard Git commands (`git pull`, `git push`, `git checkout`, `git merge`, etc.)."

### Work flow of jira and what it is used for
Jira is a project management and issue tracking tool.
-   **Used for:** Managing user stories, tasks, bugs, and other work items throughout the software development lifecycle.
-   **Workflow Example (for a bug):**
    1.  **New:** A QA logs a bug.
    2.  **Open/Assigned:** The bug is triaged and assigned to a developer.
    3.  **In Progress:** Developer starts working on the fix.
    4.  **Fixed:** Developer completes the fix and moves it to a QA environment.
    5.  **Ready for QA:** QA starts verifying the fix.
    6.  **Closed:** QA confirms the fix and closes the bug.
    7.  **Reopened:** If QA finds the bug is not fixed, it goes back to the developer.
This workflow ensures transparency and tracking of every item.
