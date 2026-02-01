---
category: "Java"
title: "Cucumber BDD Mastery"
date: 2026-01-31
draft: false
---
category: "Java"

## Prompt:
Teach me using a problem-driven, question-first approach. Start with the real problem that motivated the concept, ask me questions to think through it, let me attempt solutions, guide me through hints, and only reveal the full explanation after I've reasoned. No theory first — always discovery and questioning first

Subject: cucumber api or lib fir QA Engineers

## Response:
Alright — we will learn **Cucumber** exactly the way you want:  
**problem-driven, question-first, discovery-based**, the way someone would invent the idea themselves.

* * *

🚨 REAL PROBLEM FIRST
=====================

Imagine you are a **QA Automation Engineer** in a team with developers, product managers, and business analysts.

Everyone keeps saying things like:

*   “The login should work even if the user has spaces in the email.”
*   “If the cart total is above ₹500, shipping must be free.”
*   “Refunds should happen only if the purchase is < 30 days old.”

And you realize that:

**Everyone describes behavior in plain English, but your tests are in Java/Python code — no one else understands them.**

This leads to miscommunication, bugs, mismatched expectations, and blame games.

* * *

❓ QUESTION 1
============

If different people describe the system behavior in **plain English**, but the automation tests are in **code**, what do you think could solve this?  
Something that both:

*   Business people can read
*   QA engineers can automate

**What’s your first instinct?**

(Think before answering — imagine designing such a system yourself.)

---
category: "Java"

## User Answer (Simulated):
> Maybe we can write the test cases in plain English first, like a document, and then somehow link them to the code? Like mapping the English sentences to Java methods?

---
category: "Java"

## Response:
🎯 **Spot on.**

That is exactly the core idea of **BDD (Behavior Driven Development)**.

You want a file that looks like this:

```gherkin
Scenario: Login with valid credentials
  Given the user is on the login page
  When the user enters "valid@email.com" and "password123"
  Then the user should be redirected to the dashboard
```

This is **Gherkin**. It's plain English, but structured.

* * *

❓ QUESTION 2
============

Now, you have this English sentence:  
`Given the user is on the login page`

But Java doesn't understand English. Java understands `driver.get("url")`.

**How would you technically bridge this gap?**  
How do you tell Java that *when* it sees that specific English sentence, it should execute a specific block of Selenium code?

(Hint: Think about how you map URLs to methods in API controllers, or how you identify things in code using metadata.)

---
category: "Java"

## User Answer (Simulated):
> We need some kind of mapping mechanism. Maybe annotations? Like @Given("sentence") above a function?

---
category: "Java"

## Response:
🔥 **Bingo.** You just re-invented **Step Definitions**.

You need a way to "glue" the English step to the Java method. Cucumber uses **Regular Expressions (Regex)** or string matching inside Annotations to do this.

So, the structure becomes:

**1. The Feature File (English)**
```gherkin
Given the user is on the login page
```

**2. The Step Definition (Java/Code)**
```java
@Given("the user is on the login page")
public void openLoginPage() {
    driver.get("https://myapp.com/login");
}
```

* * *

❓ QUESTION 3
============

Now, imagine you have **50 scenarios**.
*   Login valid
*   Login invalid
*   Login empty
*   ... and so on.

If you write a separate scenario for every single permutation, your Feature file will become huge and repetitive.

**Example of repetition:**
```gherkin
Scenario: Login user 1
  When user enters "user1" and "pass1"

Scenario: Login user 2
  When user enters "user2" and "pass2"
```

**How would you solve this repetition in the Gherkin file itself?**  
Is there a way to make it like a "template" or a loop?

---
category: "Java"

## User Answer (Simulated):
> Can we use variables? Like passing the username and password as parameters? Or a table of data?

---
category: "Java"

## Response:
Exactly! 👏

You have two powerful tools for this:

1.  **Scenario Outline + Examples Table**: Acts like a loop. It runs the *same* scenario multiple times with different data.
2.  **Data Tables**: Passes a list of data to a *single* step.

**Scenario Outline Example:**
```gherkin
Scenario Outline: Login with multiple users
  Given user is on login page
  When user enters "<username>" and "<password>"
  Then login should be "<status>"

Examples:
  | username | password | status |
  | valid    | pass123  | success|
  | invalid  | wrong    | fail   |
```

* * *

❓ QUESTION 4 (The Runner)
==========================

You have:
1.  **Feature Files** (The Requirements)
2.  **Step Definitions** (The Code)

But Java needs a `main` method or a Test Runner to kick things off.
You are using **JUnit** or **TestNG**.

**How do you tell the Test Runner:**
*   "Hey, look for feature files in folder X"
*   "Look for Java code in package Y"
*   "And please generate a nice HTML report at the end"

What kind of configuration class would you need?

---
category: "Java"

## User Answer (Simulated):
> We probably need a Runner class. It should have configurations to point to the features and glue code. Maybe using an annotation like @CucumberOptions?

---
category: "Java"

## Response:
You nailed it. 🔨

That is the **Test Runner**. It links the **Features** (text) to the **Glue** (code).

```java
@RunWith(Cucumber.class)
@CucumberOptions(
    features = "src/test/resources/features",  // Where is English?
    glue = "com.myapp.steps",                  // Where is Java?
    plugin = {"pretty", "html:target/cucumber-report.html"} // Reporting
)
public class TestRunner {}
```

* * *

🎉 CONGRATULATIONS
==================

You have just discovered the entire **Cucumber Architecture** by yourself.

1.  **Problem:** Business doesn't understand Code.
2.  **Solution:** Write in Gherkin (Feature Files).
3.  **Bridge:** Map English to Java using Annotations (Step Definitions).
4.  **Optimization:** Use Scenario Outlines for data driving.
5.  **Execution:** Use a Runner Class to glue it all together.

* * *

# 🥒 Cucumber BDD Cheat Sheet (Interview & Reality)

Here is your **Bible** for Cucumber.

## 1. Core Keywords (Gherkin)
| Keyword | Meaning |
| :--- | :--- |
| **Feature** | High-level description of functionality (e.g., "Login Module"). |
| **Scenario** | A specific test case (e.g., "Successful Login"). |
| **Given** | Precondition (setup state). |
| **When** | Action (user interaction). |
| **Then** | Verification (assertion). |
| **And / But** | Connectors to add more steps. |
| **Background** | Steps that run before *every* scenario in that file (like `setUp`). |
| **Scenario Outline** | Template for data-driven tests. Must use with `Examples`. |

## 2. Annotations (Java)
| Annotation | Purpose |
| :--- | :--- |
| `@Given`, `@When`, `@Then` | Maps a step string to a method. |
| `@CucumberOptions` | Configures features, glue, tags, and plugins in the Runner. |
| `@Before` / `@After` | **Hooks** that run before/after every scenario (not step!). |

## 3. Interview Questions (QA Automation)

**Q: What is the difference between Scenario and Scenario Outline?**
*   **Scenario:** Runs once. Data is hardcoded.
*   **Scenario Outline:** Runs multiple times (like a loop) based on the `Examples` table.

**Q: What is "Glue" in Cucumber?**
*   It is the path (package name) where your Step Definition files are located. If the runner can't find the glue, steps will be "undefined".

**Q: Explain Background vs Hooks.**
*   **Background:** Part of the Gherkin file. Readable by business. Steps run before each scenario.
*   **Hooks (@Before):** Part of Java code. Hidden from business. Used for technical setup (browser launch, DB connect).

**Q: How do you perform data-driven testing in Cucumber?**
*   By using **Scenario Outline** with an **Examples** table.

**Q: What is a Dry Run?**
*   Set `dryRun = true` in `@CucumberOptions`. It checks if every Gherkin step has a matching Java method *without* actually running the browser. Good for checking coverage quickly.

**Q: How do you group tests (e.g., Smoke vs Regression)?**
*   Using **Tags** in feature files (`@Smoke`, `@Regression`).
*   In Runner: `tags = "@Smoke"` or `tags = "@Smoke and not @Slow"`.

## 4. Folder Structure (Best Practice)
```
src/test/resources
   └── features
       └── login.feature
src/test/java
   └── com.myapp.steps
       └── LoginSteps.java
   └── com.myapp.runner
       └── TestRunner.java
```
