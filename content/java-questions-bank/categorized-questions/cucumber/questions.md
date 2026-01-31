---
title: "Cucumber & BDD Interview Questions"
date: 2026-01-30
draft: false
categories: ["Cucumber"]
---

## Beginner (Basics & Gherkin)
1. [What is Cucumber?](#1-what-is-cucumber)
2. [Why do we use Cucumber?](#2-why-do-we-use-cucumber)
3. [What is BDD (Behavior Driven Development)?](#3-what-is-bdd-behavior-driven-development)
4. [What is a Feature File?](#4-what-is-a-feature-file)
5. [What are the keywords used in a Feature File (Given, When, Then, And, But)?](#5-what-are-the-keywords-used-in-a-feature-file-given-when-then-and-but)
6. [Explain the purpose of the Background keyword?](#6-explain-the-purpose-of-the-background-keyword)
7. [What is a Scenario and a Scenario Outline?](#7-what-is-a-scenario-and-a-scenario-outline)
8. [What is the purpose of Example tables in Cucumber?](#8-what-is-the-purpose-of-example-tables-in-cucumber)
9. [What are Tags in Cucumber and how are they used?](#9-what-are-tags-in-cucumber-and-how-are-they-used)
10. [Explain the Gherkin language?](#10-explain-the-gherkin-language)

## Intermediate (Implementation & Configuration)
1. [What is a Step Definition file?](#step-definition)
2. [What is a Runner Class in Cucumber?](#runner-class)
3. [Explain Cucumber Options (`@CucumberOptions`)?](#cucumber-options)
4. [What is the use of `dryRun` in Cucumber?](#dryrun-usage)
5. [What is `monochrome` in Cucumber?](#monochrome-usage)
6. [What are Hooks in Cucumber (Before and After)?](#cucumber-hooks)
7. [Difference between Background and Hooks?](#background-vs-hooks)
8. [What is the `glue` parameter in Cucumber?](#glue-parameter)
9. [How do you handle Data Tables in Cucumber?](#data-tables)
10. [How do you pass test data in a Scenario Outline?](#pass-data-outline)
11. [How do you generate reports in Cucumber?](#cucumber-reports)

## Advanced (Framework & Integration)
1. [Explain the Cucumber framework architecture?](#cucumber-architecture)
2. [How do you achieve parallel execution in Cucumber?](#parallel-execution)
3. [How do you run failed test cases in Cucumber?](#failed-tests-cucumber)
4. [How do you use Page Factory with Cucumber?](#pagefactory-cucumber)
5. [What are listeners in the Cucumber framework?](#cucumber-listeners)
6. [How do you re-use step definitions across different feature files?](#reusable-steps)
7. [Difference between Cucumber and TestNG?](#cucumber-vs-testng)
8. [Difference between BDD and TDD?](#bdd-vs-tdd)
9. [How do you integrate Cucumber with Maven and Jenkins?](#cucumber-maven-jenkins)
10. [Scenario: How would you write negative test cases in a feature file?](#negative-scenarios)

---

## Questions with Answers

### Beginner (Basics & Gherkin) - Answers

### 1. What is Cucumber? {#1-what-is-cucumber}
**Answer**: Cucumber is an open-source test automation tool that supports **Behavior Driven Development (BDD)**. It allows you to write test scenarios in plain, human-readable English (Gherkin).

### 2. Why do we use Cucumber? {#2-why-do-we-use-cucumber}
**Answer**: To bridge the communication gap between business stakeholders (Product Owners) and technical teams (Devs/QA). It ensures everyone understands the requirements through living documentation.

### 3. What is BDD (Behavior Driven Development)? {#3-what-is-bdd-behavior-driven-development}
**Answer**: BDD is a process where the team collaborates to define how the software should behave from the user's perspective. It uses examples to clarify requirements and then automates those examples as tests.

### 4. What is a Feature File? {#4-what-is-a-feature-file}
**Answer**: A file with the `.feature` extension that contains one or more test scenarios written in Gherkin. It describes a specific feature or module of the application.

### 5. What are the keywords used in a Feature File (Given, When, Then, And, But)? {#5-what-are-the-keywords-used-in-a-feature-file-given-when-then-and-but}
**Answer**:
- **Given**: Describes the initial state or context.
- **When**: Describes the action taken by the user.
- **Then**: Describes the expected outcome or result.
- **And/But**: Used to add more steps to the above keywords without repeating them.

### 6. Explain the purpose of the Background keyword? {#6-explain-the-purpose-of-the-background-keyword}
**Answer**: Used to define steps that are common to all scenarios in a feature file. It runs **before each scenario**, reducing code duplication.

### 7. What is a Scenario and a Scenario Outline? {#7-what-is-a-scenario-and-a-scenario-outline}
**Answer**:
- **Scenario**: A single test case with a specific set of steps.
- **Scenario Outline**: A template used to run the same scenario multiple times with different sets of data provided in an **Examples** table.

### 8. What is the purpose of Example tables in Cucumber? {#8-what-is-the-purpose-of-example-tables-in-cucumber}
**Answer**: Used only with `Scenario Outline` to provide multiple rows of data inputs and expected results, allowing for data-driven testing within the feature file.

### 9. What are Tags in Cucumber and how are they used? {#9-what-are-tags-in-cucumber-and-how-are-they-used}
**Answer**: Tags (e.g., `@smoke`, `@regression`) are used to group and filter scenarios. You can specify which tags to run or skip in the **Runner Class**.

### 10. Explain the Gherkin language? {#10-explain-the-gherkin-language}
**Answer**: Gherkin is a plain-text language with a specific structure that Cucumber uses to understand scenarios. It uses a set of special keywords (Given, When, Then) to give structure to the requirements.

### Intermediate (Implementation & Configuration) - Answers

### 1. What is a Step Definition file? {#step-definition}
**Answer**: A Java class that maps the Gherkin steps in the feature file to actual automation code. It contains the logic to interact with the application.

### 2. What is a Runner Class in Cucumber? {#runner-class}
**Answer**: A Java class that uses the `@RunWith(Cucumber.class)` annotation to execute the tests. It coordinates the feature files and step definitions.

### 3. Explain Cucumber Options (`@CucumberOptions`)? {#cucumber-options}
**Answer**: An annotation in the Runner Class used to configure test execution. It includes parameters like `features` (path to feature files), `glue` (path to step definitions), `tags`, and `plugin`.

### 4. What is the use of `dryRun` in Cucumber? {#dryrun-usage}
**Answer**: When set to `true`, Cucumber checks if every Gherkin step has a matching step definition without actually executing the tests. It helps identify missing snippets.

### 5. What is `monochrome` in Cucumber? {#monochrome-usage}
**Answer**: When set to `true`, it makes the console output more readable by removing unreadable characters and formatting the text cleanly.

### 6. What are Hooks in Cucumber (Before and After)? {#cucumber-hooks}
**Answer**: Methods that run before or after each scenario. `@Before` is often used for setup (launching browser), and `@After` for teardown (taking screenshots, closing browser).

### 7. Difference between Background and Hooks? {#background-vs-hooks}
**Answer**:
- **Background**: Defined in the **feature file**; steps are visible to everyone.
- **Hooks**: Defined in **code** (Java); invisible to business users, used for technical setup/cleanup.

### 8. What is the `glue` parameter in Cucumber? {#glue-parameter}
**Answer**: It specifies the package location where the step definition classes and hooks are stored.

### 9. How do you handle Data Tables in Cucumber? {#data-tables}
**Answer**: By using the `DataTable` argument in the step definition. You can convert it into a `List<Map<String, String>>` or `List<List<String>>` to iterate through the data.

### 10. How do you pass test data in a Scenario Outline? {#pass-data-outline}
**Answer**: By using placeholders in the steps like `<username>` and providing values in the `Examples:` table under the corresponding column header.

### 11. How do you generate reports in Cucumber? {#cucumber-reports}
**Answer**: By adding the `plugin` parameter in `@CucumberOptions`. Common formats are `pretty`, `html:target/report.html`, and `json:target/report.json`.

### Advanced (Framework & Integration) - Answers

### 1. Explain the Cucumber framework architecture? {#cucumber-architecture}
**Answer**: It consists of three layers:
1. **Business Layer**: Feature files (Gherkin).
2. **Translation Layer**: Step Definitions (Glue).
3. **Technical Layer**: Page Objects and Automation Utilities (Selenium).

### 2. How do you achieve parallel execution in Cucumber? {#parallel-execution}
**Answer**: By using the **TestNG Runner** with the `parallel` attribute or by using the **Maven Surefire Plugin** with the `cucumber-jvm-parallel-plugin`.

### 3. How do you run failed test cases in Cucumber? {#failed-tests-cucumber}
**Answer**: Use the `rerun` plugin in `@CucumberOptions` to store failed scenarios in a `.txt` file, then create a separate runner to execute that file.

### 4. How do you use Page Factory with Cucumber? {#pagefactory-cucumber}
**Answer**: Initialize the elements in the constructor of the Step Definition or Page class using `PageFactory.initElements(driver, this)`.

### 5. What are listeners in the Cucumber framework? {#cucumber-listeners}
**Answer**: Listeners (via TestNG or custom plugins) are used to perform actions based on test events, such as logging results or taking screenshots on failure.

### 6. How do you re-use step definitions across different feature files? {#reusable-steps}
**Answer**: As long as the steps are in the package specified by the `glue` option, Cucumber will automatically find and reuse them globally across all feature files.

### 7. Difference between Cucumber and TestNG? {#cucumber-vs-testng}
**Answer**:
- **Cucumber**: A BDD tool for collaboration; uses English scenarios.
- **TestNG**: A testing framework for developers/testers; uses Java annotations and has more advanced execution control.

### 8. Difference between BDD and TDD? {#bdd-vs-tdd}
**Answer**:
- **TDD (Test Driven Development)**: Developer writes a failing unit test first, then writes code to make it pass.
- **BDD (Behavior Driven Development)**: Focuses on system behavior through collaboration; tests are written in English before code.

### 9. How do you integrate Cucumber with Maven and Jenkins? {#cucumber-maven-jenkins}
**Answer**: Use Maven to manage dependencies and run tests via `mvn test`. In Jenkins, create a pipeline or freestyle job that executes this Maven command and parses the Cucumber JSON reports.

### 10. Scenario: How would you write negative test cases in a feature file? {#negative-scenarios}
**Answer**: Create a scenario with invalid data (e.g., wrong password) and use a **Then** step to verify that the application displays the correct error message.