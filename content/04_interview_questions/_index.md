---
title: "SDET Interview Questions"
date: 2026-01-30
draft: false
weight: 4
---

These questions are derived directly from the claims in your resume.

## 1. Selenium & Framework (The Core)
*   **Easy:** How do you handle a dropdown in Selenium? (Select class vs. Bootstrap dropdowns)
*   **Medium:** Explain your current framework structure. Where do you keep your test data? Where are your locators?
*   **Hard:** How do you handle flaky tests in your framework? Do you use `IRetryAnalyzer` in TestNG?
*   **Trap:** You mentioned "Cross-browser testing". How did you handle the browser drivers? Did you use WebDriverManager or Selenium Grid? (If you say "I downloaded the exe manually", you fail).

## 2. Java Fundamentals
*   **Easy:** What is the difference between `ArrayList` and `HashSet`?
*   **Medium:** Explain the concepts of OOPs (Encapsulation, Polymorphism) with real examples from your automation framework. (e.g., "Where did you use Inheritance?")
*   **Hard:** Write a Java program to reverse a string without using the built-in reverse function.
*   **Trap:** "Is Java pass-by-value or pass-by-reference?"

## 3. Cucumber (BDD)
*   **Easy:** What are the three main files in a Cucumber framework? (Feature file, Step Definition, Runner class).
*   **Medium:** How do you pass data from a Feature file to a Step Definition? (Scenario Outline vs DataTable).
*   **Hard:** How do you share state (variables) between two different step definition files? (Dependency Injection / PicoContainer).

## 4. API Testing (Rest Assured)
*   **Easy:** What are the common HTTP methods you have used?
*   **Medium:** How do you validate that an API response code is 200 in Rest Assured?
*   **Hard:** If an API requires an Auth Token, how do you handle that in your test automation?
*   **Trap:** "Have you ever mocked an API response?" (Be honest if you haven't).

## 5. SQL (Database)
*   **Easy:** How do you select all unique records from a table? (`DISTINCT`)
*   **Medium:** Write a query to find the second highest salary from the Employee table.
*   **Trap:** "What is the difference between `DELETE` and `TRUNCATE`?" (Transaction log vs. no log).

## 6. SDLC & STLC (Crucial)
*   **Easy:** What is the difference between Verification and Validation?
*   **Medium:** Explain the STLC (Software Testing Life Cycle) phases you follow in your current project.
*   **Hard:** At what stage should automation ideally begin in the SDLC? (Trap: If you say 'at the end', you lose).
*   **Trap:** "If a bug is found in production, who is responsible?"

## 7. Agile & Scrum
*   **Easy:** What is a Sprint?
*   **Medium:** What do you do if a User Story is not clear during the Sprint?
*   **Hard:** How do you handle a situation where a developer says "It works on my machine"?
*   **Trap:** "Should automation be part of the 'Definition of Done' (DoD)?"

## 8. CI/CD (Jenkins)
*   **Medium:** How do you trigger your automation suite from Jenkins? (Poll SCM, Webhook, or Manual build?)
*   **Trap:** "Where do the Jenkins reports get stored?"
