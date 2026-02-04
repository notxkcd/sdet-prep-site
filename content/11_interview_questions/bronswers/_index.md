---
title: "📘 Indium Interview Questions"
date: 2026-01-30
draft: false
---

| 1.  **Self Introduction**
    *   I'm a QA Automation Engineer with [X] years in Java, Selenium, and API testing. I build solid automation frameworks to make sure the product is top-notch.

| 2.  **Project Introduction**
    *   At my last job, I built the test automation for a big e-commerce site using Selenium, TestNG, and RestAssured. My work cut down regression time by about 30%.

| 3.  **Day-to-Day Activities**
    *   I'm in the daily stand-ups, analyzing stories, making test plans, coding automated scripts, and logging any bugs I find.

| 4.  **Agile Methodology**
    *   It's about building things in small pieces instead of all at once. You build a bit, test it, get feedback, and repeat. It’s all about shipping fast and being able to change direction without a big drama.

| 5.  **Flipkart XPath**
    *   You don't use brittle XPaths. Instead of counting positions, you find a stable landmark. Tell Selenium, "find the 'Top Deals' section, then grab the product links inside." That way, it doesn't break if the layout changes a bit.

| 6.  **cURL to Code**
    *   You give the cURL recipe to a library like RestAssured. Tell it the URL and what to get, and it grabs the response. Then you just pull the 'name' field out of the JSON.

| 7.  **String a = 9645788215 — Remove duplicates and find the second largest number**
    *   Throw the numbers into a Set to automatically kill duplicates. Then sort the unique numbers and grab the second one from the end.

| 8.  **Git Conflict Scenario**
    *   If two people change the same file, the second person to push needs to do a `git pull` first. Git will flag the conflict, and they have to merge the changes manually before they can push their own work.

| 9.  **How do you run your test scripts in Jenkins?**
    *   Jenkins is our automation server. We set up a job that watches our Git repo. On a new push, it automatically runs our `mvn test` command and reports if anything broke.

| 10. **What are your roles and responsibilities in your team?**
    *   I'm the quality gatekeeper. I analyze requirements, plan the testing strategy, build the automation, and hunt down bugs before they can escape to production.

| 11. **Tomorrow is release day and you find a high-priority bug — how do you handle it?**
    *   Sound the alarm. Immediately report the bug with clear steps to reproduce. Escalate to the lead and PM so they can make the tough call: delay the release or deploy and pray.

| 12. **What automation challenges have you faced in your last project?**
    *   The biggest headaches are always dynamic elements that change, flaky tests that fail randomly, and just keeping the test suite from becoming a mess as the app grows.

| 13. **When will you perform smoke and sanity testing?**
    *   A smoke test is a quick check to see if a new build is even testable, like "does the app start?". A sanity test is a focused check after a bug fix to make sure the fix works and didn't break anything obvious nearby.

---

## ⚙️ Hexaware Interview Questions

### Round 1

| 1.  **Maven Build Tool**
    *   It's the project's janitor. It manages all your dependencies (the libraries you need) and builds your project into a runnable thing, all based on a `pom.xml` file.

| 2.  **Write any 5 Array methods**
    *   `Arrays.sort()` to order stuff, `Arrays.equals()` to see if two arrays are identical, `Arrays.fill()` to paint the array with one value, `Arrays.binarySearch()` to find something fast, and `Arrays.toString()` for a clean printout.

| 3.  **Method Overloading**
    *   It's having one method name that can handle different types of inputs. You can have `print(String text)` and `print(int number)`, and Java knows which one to call.

| 4.  **Types of Casting**
    *   **Widening** is when you go from a small data type to a big one (like `int` to `double`), no sweat. **Narrowing** is forcing a big type into a small one (like `double` to `int`), where you might lose data.

| 5.  **How to perform a right-click in Selenium?**
    *   The basic WebDriver can't handle complex actions. You need to use the `Actions` class. You pass it the driver and tell it to `contextClick(element).perform()`.

| 6.  **Write Implicit Wait syntax**
    *   It tells the driver to wait a certain amount of time before throwing an exception if it can't find an element. It's a global setting: `driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS)`.

| 7.  **How to scroll using JavaScript Executor?**
    *   When Selenium can't see an element, you use the `JavascriptExecutor` to talk directly to the browser. You execute a script like `window.scrollBy(0, 500)` to move the page.

| 8.  **How to open an incognito browser?**
    *   You use `ChromeOptions`. Just `addArguments("--incognito")` before you create your `ChromeDriver` instance.

| 9.  **Print the first repeated number in the given array**
    *   Use a `HashSet`. Loop through the array and try to add each element to the set. If `add()` returns `false`, it means the element is already in the set, and you've found your first repeat.

### Round 2

| 1.  **Get all hyperlinks and click those containing "todaydeals" text**
    *   First, grab all `<a>` tags into a list of WebElements. Then, loop through the list, get the text of each one, and if it contains "todaydeals", click it and break the loop.

| 2.  **Optimize the above code using waits**
    *   Don't just hope the elements are there. Use an `WebDriverWait` to explicitly wait for the links to be present on the page before you try to interact with them. This makes the script way more stable.

| 3.  **Git workflow in Git commands**
    *   `git clone`, `git checkout -b <new-branch>`, do your work, `git add .`, `git commit -m "message"`, `git pull origin main` to sync, then `git push origin <new-branch>`. Finally, open a Pull Request.

---

## 💡 Comcast Interview Questions

| 1.  **What tools have you used for API testing?**
    *   Postman for manual exploring and quick tests. RestAssured for building powerful automation in Java. JMeter for load testing the API.

| 2.  **How do you validate the API response?**
    *   Check the status code (200, 404, etc.), validate the JSON schema to make sure the structure is right, assert the actual data in the response body, and check important headers.

| 3.  **What automation frameworks have you worked with?**
    *   I've built hybrid frameworks using a Page Object Model (POM). They're data-driven, easy to maintain, and scalable. I've also used BDD with Cucumber.

| 4.  **How do you test authentication mechanisms?**
    *   You test that valid credentials (like a Bearer Token for OAuth 2.0 or an API Key) grant access and invalid ones are rejected. You're basically testing the API's bouncer.

| 5.  **How do you validate database data after UI or API operations?**
    *   You use a JDBC connection to talk to the database directly. After an action, you run a SQL query to fetch the data and assert that it's correct. It's the ultimate source of truth.

| 6.  **How do you run automation tests in a CI/CD pipeline?**
    *   You configure your Jenkins or GitLab pipeline to run your test command (like `mvn test`) automatically after every code commit. If the tests fail, the pipeline stops, and nobody can merge broken code.

| 7.  **How do you ensure test coverage?**
    *   You use tools like JaCoCo to measure code coverage, which shows what lines of code your tests actually run. You also trace your tests back to the requirements to ensure business logic is covered.

| 8.  **How do you handle dynamic web elements in Selenium?**
    *   You write flexible locators. Instead of a rigid XPath, you find elements based on a stable parent or by text that they contain. Explicit waits are also crucial to wait for them to appear.

| 9.  **What is the difference between functional and non-functional testing?**
    *   Functional testing checks if the feature works as expected ("Does the button do the thing?"). Non-functional testing checks how well it works ("Is it fast? Is it secure? Can it handle a million users?").

| 10. **How do you handle request validation in REST APIs?**
    *   You test the API's boundaries. Send requests with missing fields, wrong data types, or invalid values to ensure the API rejects them gracefully and returns a proper error code (like 400 Bad Request).
