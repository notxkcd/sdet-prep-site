---
title: "Hands-on Practical Tasks"
date: 2026-01-30
draft: false
weight: 6
---

Complete these tasks to be "Interview Ready". Do not cheat.

## Task 1: The "Framework" Skeleton
Create a mini-project in Eclipse/IntelliJ with the following structure:
```text
src/main/java
  - com.pages
      - LoginPage.java (Methods: enterUsername, enterPassword, clickLogin)
  - com.base
      - BaseClass.java (WebDriver initialization)
src/test/java
  - com.tests
      - LoginTest.java (Uses @Test from TestNG)
```
**Goal:** Run `LoginTest.java`, it should open Chrome, go to `opensource-demo.orangehrmlive.com`, login, and close.

## Task 2: Data-Driven Test
Modify the above test. Instead of hardcoding "Admin", read the username and password from a `config.properties` file or an Excel sheet (Apache POI).

## Task 3: Rest Assured Basics
Write a standalone Java class to:
| 1.  Send a GET request to `https://reqres.in/api/users/2`
| 2.  Assert that the Status Code is `200`.
| 3.  Assert that the JSON body contains `"first_name": "Janet"`.

## Task 4: SQL Challenge
Assume a table `Students` with columns: `ID`, `Name`, `Marks`.
*   Write a query to find the student with the highest marks.
*   Write a query to find the average marks of all students.

## Task 5: Debugging Scenario
Imagine your test fails with `ElementClickInterceptedException`.
*   **Write down 3 possible reasons why.** (e.g., Overlay overlap, element not scrolled into view, loading spinner still active).
*   **Write the code fix** for one of them (e.g., using JavascriptExecutor).

## Task 6: Jenkins Pipeline (Conceptual)
You are asked to set up a Jenkins job that runs **only smoke tests** every time code is pushed to the `develop` branch.
| 1.  How do you distinguish Smoke tests from Regression tests in your code? (e.g., TestNG groups or Cucumber tags).
| 2.  What Jenkins plugin or feature would you use to trigger the build on push? (GitHub Webhook).
| 3.  Write a simple `crontab` expression to run tests every day at 2 AM. (`0 2 * * *`).
