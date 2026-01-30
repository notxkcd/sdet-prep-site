---
title: "My Script: Technical Questions"
date: 2026-01-30
draft: false
---

## 1. Selenium & Framework Answers
*   **On POM:** "I use Page Object Model because it creates a clean separation. If the 'Login' button's ID changes, I only fix it in my `LoginPage` class, and all 50 tests that use it will automatically pass. It makes my framework maintainable."
*   **On Flakiness:** "When a test is flaky, I don't just rerun it. I check if it's a synchronization issue. I replace `Thread.sleep` with `WebDriverWait`. If the element is dynamic, I use custom XPaths with `contains()` or `starts-with()`."

## 2. API Testing Answers
*   **On Rest Assured:** "I use Rest Assured because it's highly readable. For our 'User Profile' API, I write tests that send a GET request, validate the status code is 200, and then parse the JSON to ensure the `email` field matches what’s in our database."

## 3. Java Answers
*   **On Collections:** "In my framework, I use `ArrayList` to store lists of web elements and `HashMap` when I need to read configuration data from my properties files as Key-Value pairs."
