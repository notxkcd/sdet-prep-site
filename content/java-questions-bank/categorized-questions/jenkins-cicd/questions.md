---
title: "Jenkins & CI/CD Interview Questions"
date: 2026-01-30
draft: false
categories: ["CI/CD"]
---

## Beginner (Basics & Definitions)
1. [Explain Jenkins?](#1-explain-jenkins)
2. [What is the purpose of Jenkins?](#2-what-is-the-purpose-of-jenkins)
3. [What is the use of Jenkins in automation?](#3-what-is-the-use-of-jenkins-in-automation)
4. [What is CI/CD?](#4-what-is-cicd)
5. [Explain CI and CD?](#5-explain-ci-and-cd)
6. [What is a CI/CD pipeline?](#6-what-is-a-cicd-pipeline)
7. [What is the difference between CI and CD?](#7-what-is-the-difference-between-ci-and-cd)
8. [As a tester, how do you use Jenkins?](#8-as-a-tester-how-do-you-use-jenkins)
9. [Have you integrated Jenkins in your project?](#9-have-you-integrated-jenkins-in-your-project)

## Intermediate (Configuration & Usage)
1. [How to create a build in Jenkins?](#create-jenkins-build)
2. [How do you configure Jenkins for a project?](#configure-jenkins)
3. [In Jenkins, where do you set the periodic time?](#jenkins-scheduling)
4. [Where do you find the console output in Jenkins?](#jenkins-console-output)
5. [How do you trigger a Jenkins job from GitHub?](#trigger-jenkins-github)
6. [How do you configure a CI/CD pipeline for execution?](#configure-cicd-pipeline)
7. [Explain the use of Jenkins in an Automation Framework?](#jenkins-automation-framework)
8. [How do you run your automation scripts through Jenkins?](#run-scripts-jenkins)
9. [How do you handle parameters in Jenkins?](#jenkins-parameters)

## Advanced (Scenarios & Troubleshooting)
1. [Does configuring Jenkins mean it is 100% CI/CD? Explain?](#is-it-100-percent-cicd)
2. [Scenario: Code is correct locally but fails via Jenkins. What are the possible causes?](#jenkins-local-vs-remote-failure)
3. [How long does it take to run your regression suite in Jenkins?](#regression-execution-time)
4. [If the 4th script fails, will the subsequent scripts run?](#jenkins-failure-logic)
5. [How do you generate and share reports from Jenkins?](#jenkins-reports)
6. [Explain the integration of CI/CD with Git and cloud tools?](#cicd-git-cloud)
7. [Explain the end-to-end flow from code commit to deployment?](#cicd-end-to-end-flow)

---

## Questions with Answers

### Beginner (Basics & Definitions) - Answers

### 1. Explain Jenkins? {#1-explain-jenkins}
**Answer**: Jenkins is an open-source automation server that helps automate the parts of software development related to building, testing, and deploying, facilitating **Continuous Integration (CI)**.

### 2. What is the purpose of Jenkins? {#2-what-is-the-purpose-of-jenkins}
**Answer**: To automate repetitive tasks like compiling code, running automated tests, and deploying the application to various environments, ensuring faster feedback for developers.

### 3. What is the use of Jenkins in automation? {#3-what-is-the-use-of-jenkins-in-automation}
**Answer**: It acts as an orchestrator. Instead of running scripts manually on a local machine, Jenkins runs them on a server (often triggered automatically), generates reports, and notifies the team.

### 4. What is CI/CD? {#4-what-is-cicd}
**Answer**:
- **Continuous Integration (CI)**: Frequently merging code changes into a central repository and automatically running builds/tests.
- **Continuous Delivery (CD)**: Automatically deploying the code to a staging or production environment.

### 5. Explain CI and CD? {#5-explain-ci-and-cd}
**Answer**: **CI** ensures code is always in a working state. **CD** ensures that the software is always ready to be released to the user.

### 6. What is a CI/CD pipeline? {#6-what-is-a-cicd-pipeline}
**Answer**: A series of automated steps (Build -> Test -> Deploy) that code goes through to get from a developer's machine to the production server.

### 7. What is the difference between CI and CD? {#7-what-is-the-difference-between-ci-and-cd}
**Answer**: CI focuses on the **build and test** phases; CD (Deployment) focuses on the **release** phase.

### 8. As a tester, how do you use Jenkins? {#8-as-a-tester-how-do-you-use-jenkins}
**Answer**: I use it to schedule regression suites, run tests against different environments (QA, Staging), and monitor test results and reports after each deployment.

### 9. Have you integrated Jenkins in your project? {#9-have-you-integrated-jenkins-in-your-project}
**Answer**: Yes, I have set up Jenkins jobs to run Maven-based Selenium tests automatically whenever a pull request is merged in GitHub.

### Intermediate (Configuration & Usage) - Answers

### 1. How to create a build in Jenkins? {#create-jenkins-build}
**Answer**: By creating a "New Item," selecting "Freestyle project" or "Pipeline," and defining the "Build" step (e.g., executing a shell command or a Maven goal like `mvn test`).

### 2. How do you configure Jenkins for a project? {#configure-jenkins}
**Answer**: I define the source code management (Git URL), set build triggers (Webhook), provide the build environment (Java/Maven setup), and specify post-build actions (Archiving artifacts/Sending email).

### 3. In Jenkins, where do you set the periodic time? {#jenkins-scheduling}
**Answer**: Under the **"Build Triggers"** section, I use the **"Build periodically"** option and provide a Cron-like syntax (e.g., `0 0 * * *` for midnight).

### 4. Where do you find the console output in Jenkins? {#jenkins-console-output}
**Answer**: In the dashboard, click on the specific Build number, and then click on **"Console Output"** in the sidebar to see the real-time logs.

### 5. How do you trigger a Jenkins job from GitHub? {#trigger-jenkins-github}
**Answer**: By setting up a **GitHub Webhook**. I provide the Jenkins URL in the GitHub repository settings so that it notifies Jenkins on every `git push`.

### 6. How do you configure a CI/CD pipeline for execution? {#configure-cicd-pipeline}
**Answer**: I use a **Jenkinsfile** (Pipeline as Code) to define different `stages` like `Checkout`, `Build`, `Run Tests`, and `Publish Reports`.

### 7. Explain the use of Jenkins in an Automation Framework? {#jenkins-automation-framework}
**Answer**: It bridges the gap between code and results. It ensures that every time code changes, the entire suite runs automatically, keeping the quality high without manual effort.

### 8. How do you run your automation scripts through Jenkins? {#run-scripts-jenkins}
**Answer**: By configuring a job to pull the latest code from Git and executing the Maven command `mvn clean test` in the build step.

### 9. How do you handle parameters in Jenkins? {#jenkins-parameters}
**Answer**: I use the **"This project is parameterized"** option. I can pass values like `browser_type` or `env` which are then used in the scripts as system properties.

### Advanced (Scenarios & Troubleshooting) - Answers

### 1. Does configuring Jenkins mean it is 100% CI/CD? {#is-it-100-percent-cicd}
**Answer**: No. Jenkins is just a tool. **CI/CD** is a process. To be 100%, you need a culture of frequent commits, high test coverage, automated feedback loops, and a stable deployment process.

### 2. Scenario: Code is correct locally but fails via Jenkins. Why? {#jenkins-local-vs-remote-failure}
**Answer**:
1. Environment differences (different Java/Maven versions).
2. Missing dependencies on the server.
3. Network issues (Jenkins server can't access the URL).
4. Headless mode issues (scripts not configured for headless browser).

### 3. How long does it take to run your regression suite in Jenkins? {#regression-execution-time}
**Answer**: Our suite of 200 tests takes about 1 hour when run sequentially, but we reduced it to 15 minutes using **parallel execution**.

### 4. If the 4th script fails, will the subsequent scripts run? {#jenkins-failure-logic}
**Answer**: Yes, if configured as a Freestyle job with TestNG. However, in a **Pipeline**, if a stage fails, the entire pipeline usually stops unless `catchError` or `post` blocks are used.

### 5. How do you generate and share reports from Jenkins? {#jenkins-reports}
**Answer**: I use the **"HTML Publisher Plugin"** to display Extent or Allure reports directly on the build page and configure email notifications for the team.

### 6. Explain the integration of CI/CD with Git and cloud tools? {#cicd-git-cloud}
**Answer**: Git handles versioning, Jenkins handles the pipeline, and cloud platforms like **AWS** or **Azure** provide the scalable infrastructure to run tests or host the app.

### 7. Explain the end-to-end flow from code commit to deployment? {#cicd-end-to-end-flow}
**Answer**:
1. Developer pushes code to GitHub.
2. Webhook triggers Jenkins.
3. Jenkins pulls code, compiles, and runs unit tests.
4. If successful, it runs automated regression tests.
5. If tests pass, it deploys the artifact to the Staging server.