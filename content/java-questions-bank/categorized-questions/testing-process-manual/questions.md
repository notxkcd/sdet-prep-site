---
title: "Manual Testing & Process Interview Questions"
date: 2026-01-30
draft: false
categories: ["Testing Process"]
---

## Beginner (Definitions & Types)
1. [What is Manual Testing?](#1-what-is-manual-testing)
2. [Difference between Manual and Automation testing?](#2-difference-between-manual-and-automation-testing)
3. [What is a Test Case and what are its components?](#3-what-is-a-test-case-and-what-are-its-components)
4. [Difference between a Test Case and a Test Scenario?](#4-difference-between-a-test-case-and-a-test-scenario)
5. [Explain Smoke testing?](#5-explain-smoke-testing)
6. [Explain Sanity testing?](#6-explain-sanity-testing)
7. [Difference between Smoke and Sanity testing?](#7-difference-between-smoke-and-sanity-testing)
8. [What is Regression testing and why is it needed?](#8-what-is-regression-testing-and-why-is-it-needed)
9. [What is Retesting and how is it different from Regression?](#9-what-is-retesting-and-how-is-it-different-from-regression)
10. [What is Unit testing?](#10-what-is-unit-testing)
11. [What is Integration testing?](#11-what-is-integration-testing)
12. [Explain System testing?](#12-explain-system-testing)
13. [What is UAT (User Acceptance Testing)?](#13-what-is-uat-user-acceptance-testing)
14. [Explain Exploratory and Ad-hoc testing?](#14-explain-exploratory-and-ad-hoc-testing)
15. [What is White box and Black box testing?](#15-what-is-white-box-and-black-box-testing)

## Intermediate (Life Cycle & Bug Management)
1. [Explain SDLC (Software Development Life Cycle)?](#sdlc-process)
2. [Explain STLC (Software Testing Life Cycle)?](#stlc-process)
3. [Explain the Bug Life Cycle in detail?](#bug-life-cycle)
4. [What is the difference between a Bug, Defect, Error, and Failure?](#bug-defect-error)
5. [Explain Severity and Priority with real-time examples?](#severity-vs-priority)
6. [How do you raise a bug? What steps do you follow?](#how-to-raise-bug)
7. [What are the common tools for bug tracking (e.g., JIRA, Azure DevOps)?](#bug-tracking-tools)
8. [What is the RTM (Requirements Traceability Matrix)?](#rtm-matrix)
9. [What is a Test Plan and what does it contain?](#test-plan)
10. [What is a Test Strategy?](#test-strategy)
11. [Explain Entry and Exit criteria in testing?](#entry-exit-criteria)
12. [What is Boundary Value Analysis (BVA)?](#bva-technique)
13. [What is Equivalence Partitioning (EP)?](#ep-technique)

## Advanced (Management & Scenarios)
1. [How do you handle a situation where a developer rejects your bug?](#developer-rejects-bug)
2. [What will you do if a critical defect is found just before a release?](#defect-before-release)
3. [Scenario: A production bug is found after sign-off. What is your approach?](#production-bug-found)
4. [How do you decide which test cases to automate?](#what-to-automate)
5. [What is Defect Density and Defect Leakage?](#defect-metrics)
6. [Explain the difference between functional and non-functional testing?](#functional-vs-non-functional)
7. [How do you prioritize test cases in a regression suite when time is limited?](#prioritize-regression)
8. [What is the impact of "Shift Left Testing" in your project?](#shift-left-testing)
9. [Explain SIT (System Integration Testing) and CIT (Continuous Integration Testing) environments?](#sit-cit-environments)
10. [What are your roles and responsibilities in the current testing cycle?](#tester-responsibilities)

---

## Questions with Answers

### Beginner (Definitions & Types) - Answers

### 1. What is Manual Testing? {#1-what-is-manual-testing}
**Answer**: Manual testing is the process where a human tester executes test cases without using any automated tools. The tester plays the role of an end-user to find bugs and ensure the software meets the requirements.

### 2. Difference between Manual and Automation testing? {#2-difference-between-manual-and-automation-testing}
**Answer**:
- **Manual**: Better for UI/UX, ad-hoc, and one-time tests. Requires more time and human effort.
- **Automation**: Better for regression, load, and repetitive tests. Fast execution and reliable, but requires an initial setup and scripting effort.

### 3. What is a Test Case and what are its components? {#3-what-is-a-test-case-and-what-are-its-components}
**Answer**: A set of actions performed on a system to determine if it satisfies requirements.
- **Components**: ID, Description, Pre-conditions, Steps, Test Data, Expected Result, Actual Result, Status.

### 4. Difference between a Test Case and a Test Scenario? {#4-difference-between-a-test-case-and-a-test-scenario}
**Answer**:
- **Test Scenario**: A high-level description of "what" to test (e.g., Verify Login).
- **Test Case**: A detailed step-by-step description of "how" to test (e.g., enter username, enter password, click login).

### 5. Explain Smoke testing? {#5-explain-smoke-testing}
**Answer**: A quick test performed on a new build to verify that the **critical functionalities** work. It is also called "Build Verification Testing."

### 6. Explain Sanity testing? {#6-explain-sanity-testing}
**Answer**: A subset of regression testing that focuses on a **specific module** or bug fix to ensure that the changes work as expected without affecting existing related logic.

### 7. Difference between Smoke and Sanity testing? {#7-difference-between-smoke-and-sanity-testing}
**Answer**:
- **Smoke**: Checks the stability of the entire build (Initial check).
- **Sanity**: Checks specific logic or bug fixes (Specific check).

### 8. What is Regression testing and why is it needed? {#8-what-is-regression-testing-and-why-is-it-needed}
**Answer**: Rerunning tests on previously working software after a code change to ensure no new bugs were introduced in the existing functionalities.

### 9. What is Retesting and how is it different from Regression? {#9-what-is-retesting-and-how-is-it-different-from-regression}
**Answer**:
- **Retesting**: Testing a specific bug fix to ensure it is resolved.
- **Regression**: Testing other parts of the system to ensure the fix didn't break anything else.

### 10. What is Unit testing? {#10-what-is-unit-testing}
**Answer**: Testing individual components or pieces of code (functions/methods) in isolation, usually done by developers.

### 11. What is Integration testing? {#11-what-is-integration-testing}
**Answer**: Testing how different modules or services work together as a group.

### 12. Explain System testing? {#12-explain-system-testing}
**Answer**: Testing the complete, integrated software product to evaluate the system's compliance with its specified requirements.

### 13. What is UAT (User Acceptance Testing)? {#13-what-is-uat-user-acceptance-testing}
**Answer**: The final phase of testing done by the client or end-users to ensure the product is "fit for use" before moving to production.

### 14. Explain Exploratory and Ad-hoc testing? {#14-explain-exploratory-and-ad-hoc-testing}
**Answer**:
- **Ad-hoc**: Informal testing done without documentation or specific plan.
- **Exploratory**: Testing where the tester simultaneously learns, designs, and executes tests based on their experience and intuition.

### 15. What is White box and Black box testing? {#15-what-is-white-box-and-black-box-testing}
**Answer**:
- **White box**: Testing internal structures or workings of an application (Code-level).
- **Black box**: Testing the application without knowing the internal code (Requirement-level).

### Intermediate (Life Cycle & Bug Management) - Answers

### 1. Explain SDLC (Software Development Life Cycle)? {#sdlc-process}
**Answer**: The entire process of building software: Requirements -> Analysis -> Design -> Coding -> Testing -> Deployment -> Maintenance.

### 2. Explain STLC (Software Testing Life Cycle)? {#stlc-process}
**Answer**: The phases of testing: Requirements Analysis -> Test Planning -> Test Design -> Environment Setup -> Test Execution -> Test Closure.

### 3. Explain the Bug Life Cycle in detail? {#bug-life-cycle}
**Answer**: New -> Assigned -> Open -> Fixed -> Pending Retest -> Retest -> Verified -> Closed. (Other statuses: Reopened, Deferred, Rejected, Duplicate).

### 4. What is the difference between a Bug, Defect, Error, and Failure? {#bug-defect-error}
**Answer**:
- **Error**: A mistake in the code made by a developer.
- **Bug/Defect**: Found during the testing phase.
- **Failure**: When the end-user finds a defect in production.

### 5. Explain Severity and Priority with real-time examples? {#severity-vs-priority}
**Answer**:
- **Severity**: Impact on the system (Technical). Example: App crash (High).
- **Priority**: Impact on the business (Urgency). Example: Logo missing on homepage (High priority, Low severity).

### 6. How do you raise a bug? What steps do you follow? {#how-to-raise-bug}
**Answer**: I use JIRA. I include: Summary, Description, Steps to reproduce, Expected vs Actual result, Screenshots/Videos, Severity, and the Environment details.

### 7. What are the common tools for bug tracking? {#bug-tracking-tools}
**Answer**: JIRA, Bugzilla, HP ALM (QC), Azure DevOps.

### 8. What is the RTM (Requirements Traceability Matrix)? {#rtm-matrix}
**Answer**: A document that maps requirements to test cases to ensure 100% test coverage and no missed requirements.

### 9. What is a Test Plan and what does it contain? {#test-plan}
**Answer**: A high-level document describing the scope, approach, resources, and schedule of testing activities.

### 10. What is a Test Strategy? {#test-strategy}
**Answer**: A static, long-term document that defines the testing standards and protocols for the entire organization or project.

### 11. Explain Entry and Exit criteria in testing? {#entry-exit-criteria}
**Answer**:
- **Entry**: Conditions that must be met before testing starts (e.g., Requirements approved).
- **Exit**: Conditions that must be met to stop testing (e.g., 100% test cases executed, 0 critical bugs).

### 12. What is Boundary Value Analysis (BVA)? {#bva-technique}
**Answer**: A technique focusing on testing values at the boundaries (Min, Min-1, Min+1, Max, Max+1).

### 13. What is Equivalence Partitioning (EP)? {#ep-technique}
**Answer**: Dividing input data into valid and invalid partitions where each value in a partition is expected to behave the same way.

### Advanced (Management & Scenarios) - Answers

### 1. How do you handle a situation where a developer rejects your bug? {#developer-rejects-bug}
**Answer**: I re-verify the bug locally, provide more evidence (logs/screenshots), and if disagreement persists, I bring it to the attention of the Test Lead or discuss it in a triage meeting.

### 2. What will you do if a critical defect is found just before a release? {#defect-before-release}
**Answer**: I immediately inform the Product Owner and stakeholders. We perform a **Risk Assessment** to decide whether to delay the release, fix it immediately (Hotfix), or release with a known issue (Deferred).

### 3. Scenario: A production bug is found after sign-off. What is your approach? {#production-bug-found}
**Answer**: I perform a **Root Cause Analysis (RCA)** to understand why the bug was missed during testing. We then fix it, retest, and update our regression suite to prevent it from happening again.

### 4. How do you decide which test cases to automate? {#what-to-automate}
**Answer**: Based on:
1. Frequency of execution (Regression).
2. Business criticality.
3. Complex calculations.
4. Time-consuming manual steps.

### 5. What is Defect Density and Defect Leakage? {#defect-metrics}
**Answer**:
- **Defect Density**: Number of defects per size of the software (e.g., bugs per 1000 lines of code).
- **Defect Leakage**: Bugs found by the end-user after the product is released.

### 6. Explain the difference between functional and non-functional testing? {#functional-vs-nonfunctional}
**Answer**:
- **Functional**: Verifies "what" the system does (Login, Checkout).
- **Non-functional**: Verifies "how" the system behaves (Performance, Security, Usability).

### 7. How do you prioritize test cases in a regression suite when time is limited? {#prioritize-regression}
**Answer**: I focus on the **P0 (Critical)** cases, recently changed modules, and areas with historically high defect rates.

### 8. What is the impact of "Shift Left Testing" in your project? {#shift-left-testing}
**Answer**: It means testing starts much earlier in the SDLC (during requirement/design phases). This helps in catching bugs early, reducing the cost of fixing them.

### 9. Explain SIT (System Integration Testing) and CIT (Continuous Integration Testing) environments? {#sit-cit-environments}
**Answer**:
- **SIT (System Integration Testing)**: Environment where different systems/modules are integrated and tested together.
- **CIT (Continuous Integration Testing)**: Environment where tests run automatically as part of the build pipeline.

### 10. What are your roles and responsibilities in the current testing cycle? {#tester-responsibilities}
**Answer**: Analyzing requirements, creating test plans/cases, executing manual and automated tests, bug reporting, and collaborating with developers in Agile sprints.