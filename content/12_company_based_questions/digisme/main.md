---
title: "DigiSME"
date: 2026-01-30
draft: false
---

---

## Original Questions

- Company Name : DigiSME
-----------------------
Round : 1  Test case writing for a Payment done via scanner option(Given Time duration 5 Mins)

Round : 2 Definition and Scenario based Questions. 
(Depends upon candidate Answer Questions raised)
* Explain Sanity Testing
* Explain Regression Testing
* Tomorrow Product needs to be realized but one of our teammates found a few defects, what will you do? 
*Root Cause analysis and where you did in your project.
* Application needs to be released within hrs, As a manager I am telling you to do smoke testing , what is your approach to handle this?
* Explain Exhaustive testing.
* Explain Defect Management and what tool you have used so far?
* Explain Agile?
* Explain Projects done so far.
* Explain BVP and  Priority / Severity.
* What is deferred means?
* Worked on any Cloud platform.
* Explain SaaS project.
* Explain Nods and Pods in Azure. What is the use of it when it comes to Web application.
* Explain Test Bed
* Explain the environment which you have worked so far.
* Design is important if yes / no then why? 
* What is compatibility testing? Where did you used and most faced challenges.
* What is fragmentation?
* Explain Audit with your experience.

Round : 3 HR rounds ( General Discussion about the project, place, CTC discussion ).

---

## Answers (No-BS Java QA / SDET Explanations)

### Round 1: Test case writing for a Payment done via scanner option

This is a test design question. You need to think about positive, negative, and edge cases for a QR code payment flow.

**Feature:** Payment via QR Code Scanner

**Positive Scenarios:**
-   **TC-01:** Scan a valid, supported QR code -> payment details screen is displayed correctly with correct recipient and amount.
-   **TC-02:** Complete payment with sufficient funds -> success message displayed, amount deducted, recipient receives funds.

**Negative Scenarios:**
-   **TC-03:** Scan an invalid/corrupted QR code -> "Invalid QR Code" error message displayed.
-   **TC-04:** Scan an expired QR code -> "QR Code Expired" error message displayed.
-   **TC-05:** Scan a QR code for an unsupported payment type (e.g., a simple URL QR code) -> appropriate error message displayed.
-   **TC-06:** Attempt payment with insufficient funds -> "Insufficient balance" error message displayed.
-   **TC-07:** Cancel the payment transaction at the confirmation screen -> user is returned to the previous screen, no funds are deducted.

**Edge/Other Scenarios:**
-   **TC-08:** Lose network connectivity *after* scanning but *before* confirming payment -> appropriate "Network Error" message displayed, transaction is not completed.
-   **TC-09:** Test with a very blurry or poorly lit QR code -> verify scanner's tolerance level.
-   **TC-10:** Test with a very small or very large QR code on screen.

### Round 2: Definition and Scenario based Questions

#### Explain Sanity Testing
A narrow and deep test performed after a minor code change or bug fix. Its purpose is to quickly verify that the change works as expected and has not broken any closely related functionality. It's a "check if the change is sane" test.

#### Explain Regression Testing
A broad and deep test suite run after code changes to ensure that the new changes have not broken any existing, previously working functionality in the application. It's usually automated due to its repetitive nature.

#### Tomorrow Product needs to be realized but one of our teammates found a few defects, what will you do?
This is a risk assessment and communication question.
1.  **Triage Immediately:** The first step is to quickly assess the defects. What is their **severity** and **priority**?
2.  **Analyze Impact:**
    -   If they are **high-severity** bugs in critical features (e.g., checkout is broken), I would immediately recommend **halting the release**.
    -   If they are **low-severity** bugs with workarounds (e.g., a cosmetic issue on a minor page), I would document them, and we could proceed with the release while planning to fix them in the next cycle.
3.  **Communicate:** I would clearly communicate my findings and risk assessment to the Product Manager, Test Lead, and relevant stakeholders. The final decision to release or not is a business decision, but it's my responsibility to provide all the necessary quality data to make that decision an informed one.

#### Root Cause analysis and where you did in your project.
Root Cause Analysis (RCA) is a process for discovering the fundamental cause of a problem.
"In my project, we performed RCA for every critical production bug. For example, we had an issue where orders were getting duplicated. The RCA involved:
1.  **Identifying the problem:** Orders were being created twice.
2.  **Analyzing the data:** We checked server logs, database records, and API traffic. We noticed the `POST /orders` endpoint was being hit twice in quick succession from the UI.
3.  **Finding the root cause:** The root cause wasn't the API; it was the frontend code. The 'Submit' button was not being disabled after the first click, allowing users on slow networks to click it twice, firing two separate API calls.
4.  **Implementing a solution:** The fix was to disable the button on the frontend immediately after the first click. We also discussed adding an idempotency key to the backend API as a secondary safeguard."

#### Application needs to be released within hrs, As a manager I am telling you to do smoke testing , what is your approach to handle this?
"My approach would be to execute a rapid, risk-based smoke test focused on the absolute most critical business flows.
1.  **Identify Critical Paths:** I would immediately identify the top 3-5 'can't fail' user journeys. For an e-commerce site, this would be: User Login, Product Search, Add to Cart, and Checkout.
2.  **Execute Manually (if faster):** Given the time constraint, I would execute these flows manually, as running an automated suite might take longer.
3.  **Focus on Happy Path:** The goal of a smoke test is not to find edge-case bugs, but to confirm that the core functionality is not broken. I would stick to the 'happy path'.
4.  **Report Immediately:** I would provide a clear 'Go' or 'No-Go' recommendation based on the results as quickly as possible. If any of these critical paths fail, it's a 'No-Go'."

#### Explain Exhaustive testing.
Exhaustive testing means testing every possible combination of inputs and preconditions. In any non-trivial application, this is **impossible** and impractical. The number of combinations grows exponentially. This is *why* we use test design techniques like Equivalence Partitioning and Boundary Value Analysis to select a small, but effective, subset of test cases.

#### Explain Defect Management and what tool you have used so far?
Defect management is the process of identifying, logging, tracking, and resolving defects. The goal is to ensure all bugs are properly documented and addressed. "I've used **Jira** for defect management. The process involves logging a bug with detailed information, which then goes through a workflow (e.g., Open, In Progress, Ready for QA, Closed)."

#### Explain Agile?
Agile is an iterative approach to software development focused on collaboration, customer feedback, and delivering value in small increments (sprints).

#### Explain Projects done so far.
Standard question. Be prepared to talk about 1-2 projects in detail.

#### Explain BVP and Priority / Severity.
-   **BVA (Boundary Value Analysis):** A test design technique that focuses on testing the "boundaries" of input ranges, as this is where errors are most likely to occur.
-   **Priority vs. Severity:**
    -   **Severity:** Technical impact of the bug.
    -   **Priority:** Business urgency to fix the bug.

#### What is deferred means?
A "deferred" defect is one that the team has acknowledged as a valid bug, but has decided **not to fix** in the current release cycle. It's postponed to be fixed in a future release, usually because it's low priority and the resources are needed for more critical issues.

#### Worked on any Cloud platform.
"Yes, our entire test infrastructure, including Jenkins and Selenium Grid, was hosted on **AWS (Amazon Web Services)**. I have experience working with EC2 instances for our test agents." (Or Azure, or GCP).

#### Explain SaaS project.
SaaS stands for **Software as a Service**. It's a software delivery model where the application is centrally hosted by a provider and accessed by customers over the internet via a web browser.
-   **Examples:** Salesforce, Google Workspace, Slack.
-   **Testing implications:** Testing focuses on web application testing, API integrity, security, performance, and cross-browser compatibility. You don't have to worry about installation on a user's machine.

#### Explain Nods and Pods in Azure. What is the use of it when it comes to Web application.
This is a Kubernetes question, often used with Azure Kubernetes Service (AKS).
-   **Node:** A Node is a worker machine (a virtual or physical machine) where your application runs. It's part of a Kubernetes cluster.
-   **Pod:** A Pod is the smallest, most basic deployable object in Kubernetes. It represents a single instance of a running process in your cluster. A Pod runs on a Node. A Pod encapsulates one or more containers (like Docker containers).
-   **Use for Web Application:** You would package your web application (e.g., your Spring Boot backend or your React frontend) into a Docker container. You then tell Kubernetes to run that container inside a Pod. Kubernetes manages scheduling these Pods onto Nodes, handling networking, scaling, and ensuring the application stays running. This provides a scalable and resilient way to host web applications.

#### Explain Test Bed
A Test Bed is another term for a **Test Environment**. It's the complete setup of hardware, software, network configuration, and data on which the test cases are executed.

#### Explain the environment which you have worked so far.
"I've worked with several environments:
-   **Local:** My own machine for writing and debugging new tests.
-   **Dev:** A shared environment for developers to do initial integration.
-   **QA:** A stable, dedicated environment where the QA team performs most of its testing.
-   **Staging/UAT:** A production-like environment for final regression testing and user acceptance testing before a release.
-   **Production:** The live environment."

#### Design is important if yes / no then why?
"Yes, design is critically important, both for the application and for the test framework.
-   **Application Design:** A well-designed application is easier to test, maintain, and scale. Good design promotes testability.
-   **Test Framework Design:** A well-designed framework (e.g., using POM, being data-driven) is crucial. Without good design, an automation suite quickly becomes a tangled, unmaintainable mess that is expensive to update and produces unreliable results."

#### What is compatibility testing? Where did you used and most faced challenges.
-   **What:** Testing to ensure the application works correctly across different browsers, operating systems, devices, and screen resolutions.
-   **Where Used:** "We performed cross-browser compatibility testing for our web application, running our regression suite against the latest versions of Chrome, Firefox, and Safari."
-   **Challenges:**
    -   **Minor Rendering Differences:** The biggest challenge is often minor CSS differences that cause elements to overlap or misalign in one browser but not another, leading to test failures.
    -   **Browser-Specific Behavior:** Occasionally, a JavaScript feature might behave slightly differently in a specific browser, requiring a conditional workaround in the test script.
    -   **Maintaining Infrastructure:** Managing a Selenium Grid with different browser versions can be complex. We eventually moved to a cloud testing platform to simplify this.

#### What is fragmentation?
In the context of mobile testing, **device fragmentation** is the challenge posed by the enormous variety of hardware, screen sizes, and OS versions available, especially on Android. An app that works perfectly on a Google Pixel with Android 12 might have issues on a Samsung device with Android 10 due to manufacturer customizations or different screen aspect ratios. This makes comprehensive compatibility testing very difficult.

#### Explain Audit with your experience.
In a software context, an audit is a formal review of a process or system to ensure it complies with a set of standards, regulations, or requirements.
"In a previous project in the financial domain, we underwent regular audits. My role was to provide evidence from our test management tool (Jira/Xray) to the auditors. I had to demonstrate a clear **Requirements Traceability Matrix (RTM)**, showing that every business requirement had corresponding test cases, and provide the execution history of those tests to prove that they were run and passed before each release."
