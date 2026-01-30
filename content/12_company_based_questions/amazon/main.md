---
title: "Amazon"
date: 2026-01-30
draft: false
---

---

## Original Questions

Amazon
------
1. Tell about yourself
2. Manual vs automation testing 
3. Prerequisites of automation testing 
4. I have a prime video app to check if it is opening and write manual test cases
5. How will you automate the above test cases
6. Locators
7. Functions of the driver explain. 
8. What is regression testing and why it is needed
9. What is selenium 
10. Scenario and test coverage
11. What is the test case
*Second round* 
All scenario based questions bro 
1. 50 test cases are there, how will you choose which test case to automate 
2. You said you configure jenkins , does it mean it is 100% CI
3. CI/CD, so once we configure to jenkins it do mean it is 100% CI/CD
4. What challenge you have faced in last project 
5. Did your company leave you abruptly. 
6. Completed graduation in 2012 have only 4.3 experience
7. Load vs stress testing 
8. Smoke vs sanity
9. Locators 
10. Different types of xpath
11. Syntax for absolute and relative xpath

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. Tell about yourself
Standard.

### 2. Manual vs automation testing
-   **Manual Testing:** A human tester executes test cases, exploring the application to find bugs. It's good for exploratory, usability, and ad-hoc testing where human intuition is valuable. It's slow, prone to human error, and not scalable for regression.
-   **Automation Testing:** A software tool (like Selenium) executes pre-scripted tests. It's excellent for repetitive tasks like regression testing, performance testing, and data-driven testing. It's fast, reliable (when well-written), and scalable.

### 3. Prerequisites of automation testing
1.  **Stable Application:** The application under test should be relatively stable. Automating a constantly changing UI is inefficient.
2.  **Clear Test Cases:** A well-defined set of manual test cases to be automated.
3.  **Skilled Resources:** A team with programming knowledge (e.g., Java) and expertise in automation tools (e.g., Selenium).
4.  **Right Tools:** Selection of appropriate tools for the application technology (e.g., Selenium for web, Appium for mobile).
5.  **Dedicated Environment:** A stable test environment is crucial to avoid false failures.

### 4. I have a prime video app to check if it is opening and write manual test cases
**Feature:** Prime Video App Launch

**Test Cases:**
-   **TC-01 (Happy Path):**
    -   **Step:** Tap on the Prime Video app icon.
    -   **Expected:** App launches, splash screen is displayed, and user is taken to the main home/profile screen within an acceptable time (e.g., < 3 seconds).
-   **TC-02 (Interruption - during launch):**
    -   **Step 1:** Tap on the app icon.
    -   **Step 2:** While the app is launching, receive a phone call.
    -   **Step 3:** Answer and end the call.
    -   **Expected:** The app should resume its launch process or be in a stable state when returned to.
-   **TC-03 (No Network):**
    -   **Step 1:** Turn on airplane mode.
    -   **Step 2:** Tap on the app icon.
    -   **Expected:** App launches and displays a clear "No Internet Connection" error message instead of crashing or hanging.
-   **TC-04 (Low Memory):**
    -   **Step 1:** Open several other memory-intensive apps.
    -   **Step 2:** Tap on the Prime Video app icon.
    -   **Expected:** App launches successfully and performs acceptably, or handles the low-memory situation gracefully.

### 5. How will you automate the above test cases
You would use a mobile automation tool like **Appium**.
-   **TC-01 (Happy Path):** The script would launch the app (defined in Desired Capabilities) and then assert that a key element from the home screen (e.g., the profile icon) is visible within a certain timeout.
-   **TC-02 (Interruption):** Appium has limited capabilities for this. You could use device-specific commands or Android Debug Bridge (ADB) to simulate events, but it's complex.
-   **TC-03 (No Network):** The script would use Appium's built-in methods to turn off WiFi/Data on the device (`driver.setConnection(new ConnectionStateBuilder().withWiFiDisabled().build());`), then launch the app and assert that the "No Connection" element is displayed.

### 6. Locators
The 8 standard Selenium locators: `id`, `name`, `className`, `tagName`, `linkText`, `partialLinkText`, `cssSelector`, `xpath`.

### 7. Functions of the driver explain.
The `WebDriver` object (`driver`) is the main entry point for controlling a browser. Its key functions are:
-   **Navigation:** `driver.get(url)`, `driver.navigate().to/back/forward/refresh()`.
-   **Finding Elements:** `driver.findElement(By)` and `driver.findElements(By)`.
-   **Window/Context Management:** `driver.manage()` (for timeouts, cookies, window size), `driver.switchTo()` (for frames, windows, alerts).
-   **Lifecycle:** `driver.quit()` to end the session.

### 8. What is regression testing and why it is needed
Regression testing is re-running existing tests to ensure that new code changes have not broken old, previously working functionality. It's needed because software is complex and a change in one area can have unforeseen consequences in another. It provides a safety net that builds confidence for releases.

### 9. What is selenium
Selenium is an open-source suite of tools for automating web browsers. It's primarily used for writing automated tests for web applications. Its core component is **Selenium WebDriver**.

### 10. Scenario and test coverage
-   **Scenario:** In BDD/Cucumber, a scenario is a single, executable test case that describes a specific behavior of the system.
-   **Test Coverage:** A metric used to measure the extent to which testing has "covered" the application. It can mean different things:
    -   **Requirements Coverage:** What percentage of the specified requirements have at least one test case?
    -   **Code Coverage:** What percentage of the application's source code is executed by the tests (usually unit tests)?
    -   The goal is to increase test coverage to reduce the risk of undiscovered bugs.

### 11. What is the test case
A test case is a set of actions executed to verify a particular feature or functionality. It consists of a title, preconditions, a sequence of steps (actions and expected results), and postconditions.

### *Second round*

#### 1. 50 test cases are there, how will you choose which test case to automate
You use a risk-based and ROI-based approach. I would prioritize automating tests that are:
1.  **Business Critical:** Tests for core business workflows (e.g., login, checkout, payment).
2.  **Repetitive:** Tests that are part of the regression or smoke suite and run frequently.
3.  **Data-Driven:** Tests that need to be run with many different data combinations.
4.  **Stable:** Tests for features that are not expected to change frequently.
5.  **Hard to Perform Manually:** Tests that involve complex calculations or setups that are prone to human error.

I would *not* prioritize automating one-time tests, usability tests, or tests for highly unstable features.

#### 2. You said you configure jenkins , does it mean it is 100% CI
"No, configuring Jenkins is a necessary step, but it doesn't automatically mean you have 100% Continuous Integration. CI is a *practice*, not just a tool. True CI means that **every developer on the team merges their code into the main branch at least once a day**, and each merge triggers an automated build and test run. If developers are working on long-lived feature branches for weeks without merging, you are not practicing CI, even if you have Jenkins."

#### 3. CI/CD, so once we configure to jenkins it do mean it is 100% CI/CD
"No. CI (Continuous Integration) is the 'build and test' part. CD (Continuous Delivery/Deployment) is the next step.
-   **Continuous Delivery:** Means that every change that passes the CI tests is automatically deployed to a production-like staging environment. The final push to production is a manual, business decision.
-   **Continuous Deployment:** Is the most advanced stage, where every change that passes all automated tests is **automatically deployed to production** without any human intervention.
Just setting up Jenkins to run tests achieves the 'automated build and test' part, but you need automated deployment scripts and a high degree of confidence in your test suite to achieve true CI/CD."

#### 4. What challenge you have faced in last project
Have a specific, technical example ready (e.g., flaky tests due to timing, test data management for parallel runs, unstable locators).

#### 5. Did your company leave you abruptly.
This is an HR question to check for red flags. Be professional. "No, my departure was planned. I'm seeking a new role to pursue different challenges and opportunities for growth."

#### 6. Completed graduation in 2012 have only 4.3 experience
This is a question about a potential gap in your resume. Be prepared to explain it honestly and briefly (e.g., "I took some time off for personal reasons/to explore another field, and re-entered the IT industry in [Year], where I have been focused ever since.").

#### 7. Load vs stress testing
-   **Load Testing:** Measures system performance under expected, realistic load conditions. The goal is to identify performance bottlenecks and determine the system's normal capacity.
-   **Stress Testing:** Pushes the system beyond its normal capacity to see how and when it breaks. The goal is to determine the system's breaking point and check its failure recovery behavior.

#### 8. Smoke vs sanity
-   **Smoke Test:** Broad and shallow. Checks if a new build is stable enough to test.
-   **Sanity Test:** Narrow and deep. Checks if a small bug fix or change works as expected.

#### 9. Locators
(Repeated) The 8 types used by Selenium to find elements.

#### 10. Different types of xpath
-   **Absolute:** From the root of the document (`/html/...`). Brittle.
-   **Relative:** From anywhere in the document (`//...`). Flexible and preferred.

You can also talk about using **axes** (`following-sibling`, `ancestor`), **functions** (`contains()`, `text()`), and **logical operators** (`and`, `or`) to build complex relative XPaths.

#### 11. Syntax for absolute and relative xpath
-   **Absolute:** `/html/body/div[1]/div/h1`
-   **Relative:** `//h1[@id='main-title']`
