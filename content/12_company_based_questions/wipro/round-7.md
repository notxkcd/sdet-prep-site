---
title: "Wipro-7"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

Wipro
------
1)Explain STLC and SDLC
2)Explain about regression and how you pick the testcases and tell the example for this
3)Tell me selenium Architecture
?
4)What is a complex test plan?
5)what is Automation testing and what is the advantage for using automation testing?
6)What is the improvement in your project?

---

## Answers (No-BS Java QA / SDET Explanations)

### 1) Explain STLC and SDLC
-   **SDLC (Software Development Life Cycle):** The entire process of developing software, from initial requirements gathering to deployment and maintenance. It's the broader development framework.
-   **STLC (Software Testing Life Cycle):** A subset of the SDLC, focusing specifically on the testing activities. It outlines the phases involved in ensuring quality, from test planning to test closure.

### 2) Explain about regression and how you pick the testcases and tell the example for this
-   **Regression Testing:** The process of retesting existing software functionality after changes (new features, bug fixes) to ensure that the changes haven't introduced new bugs or re-introduced old ones.
-   **How to Pick Test Cases:** You select test cases based on criticality, frequency of execution, and risk.
    1.  **Critical Business Flows:** Core functionalities like login, checkout, user registration.
    2.  **Areas with Frequent Changes:** Parts of the application that are regularly updated.
    3.  **Areas with Known Defect History:** Where bugs have been found in the past.
    4.  **Integration Points:** Test cases covering interactions between different modules.
-   **Example:** For an e-commerce platform, after a new payment gateway is integrated, you'd pick test cases covering:
    -   Successful login.
    -   Product search.
    -   Adding products to cart.
    -   Checkout with existing payment methods.
    -   User profile updates.

### 3) Tell me selenium Architecture
Selenium's architecture has evolved with version 4.
-   **Selenium 3 (Legacy):**
    1.  Selenium Client Library (your Java code).
    2.  JSON Wire Protocol (over HTTP).
    3.  Browser Driver (e.g., ChromeDriver).
    4.  Browser.
-   **Selenium 4 (Current):**
    1.  Selenium Client Library (your Java code).
    2.  **W3C WebDriver Protocol** (over HTTP).
    3.  Browser Driver (e.g., ChromeDriver).
    4.  Browser.
The key change is the direct communication via the W3C WebDriver Protocol, making it more standard and stable. Selenium Grid operates as a hub-and-node system for distributed testing.

### 4) What is a complex test plan?
A test plan is complex if it involves:
-   **Multiple Systems/Integrations:** Testing an application that integrates with many external services or legacy systems.
-   **Diverse Test Types:** Requiring functional, performance, security, usability, and compatibility testing.
-   **Large Scale:** A very large application with many features and modules.
-   **Distributed Teams:** Testers located in different geographical regions.
-   **Regulatory Requirements:** Needing to comply with industry-specific regulations (e.g., HIPAA, GDPR).
-   **New Technologies:** Testing an application built with cutting-edge or unfamiliar technologies.

### 5) what is Automation testing and what is the advantage for using automation testing?
-   **Automation Testing:** Using software to execute pre-scripted tests, compare actual results to expected results, and report findings.
-   **Advantages:**
    -   **Speed:** Executes tests much faster than manual testing.
    -   **Accuracy:** Eliminates human error and performs tests consistently.
    -   **Efficiency:** Frees up human testers for more exploratory and complex testing.
    -   **Scalability:** Can run large numbers of tests and in parallel.
    -   **Cost-Effective (long-term):** Reduces the cost of repeated manual regression testing.
    -   **Earlier Feedback:** Provides faster feedback to developers, supporting CI/CD.

### 6) What is the improvement in your project?
This is asking for an achievement or initiative you led.
"In my project, I led the effort to enhance our test data management strategy. Previously, tests used static, shared data, which caused conflicts in parallel execution. I designed and implemented a dynamic test data factory that generates unique data on-the-fly for each test run. This significantly improved the reliability and repeatability of our automated tests, especially when running in parallel."
(Or discuss improvements in reporting, framework architecture, CI/CD integration, etc.).
