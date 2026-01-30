---
title: "Agilisium"
date: 2026-01-30
draft: false
---

---

## Original Questions

Agilisium Interview questions:

- What are all the manual testing you done?
- Explain unit testing?
- Where will you main your test cases?
- What parameter you use for testing in postman?
- Given a URL and write the logic to link all the link given in the website?
- What is the repo you used in your project?
- How will you test using postman tool?
- When will you do retrospective?
- Day to day activities?
- About Agile?
- Do you have experience in SQL?
- Given a scenario based on the current project and asked if you missed some major criteria what will happen in this case?
- How will you handle git conflict?

---

## Answers (No-BS Java QA / SDET Explanations)

### What are all the manual testing you done?
This question checks the breadth of your testing knowledge. A good SDET is still a good tester first.
"While my focus is on automation, I perform several types of manual testing as part of our process:
-   **Exploratory Testing:** On new features, I conduct session-based exploratory testing to discover issues that scripted tests might miss. I create a charter, execute tests on the fly, and document my findings.
-   **Smoke Testing:** If automation isn't ready for a brand new feature, I'll perform a quick manual smoke test to ensure the core functionality isn't broken before accepting it into the test environment.
-   **Usability Testing:** I provide feedback on user experience and workflow issues from a user's perspective, which is often found during exploratory testing.
-   **Bug Re-testing/Verification:** I manually verify that bug fixes have actually solved the reported problem."

### Explain unit testing?
Unit testing is the practice of testing the smallest possible piece of testable software in an application, in isolation from the rest of the system.
-   **What is a "unit"?** Typically a single method or class.
-   **Who writes them?** Primarily developers. They write unit tests for the code they produce.
-   **Why?** To verify that the logic of that single unit works as expected. They are fast, easy to run, and provide a tight feedback loop for the developer.
-   **Tools:** In Java, this is done with frameworks like **JUnit** or **TestNG** and mocking libraries like **Mockito** to isolate the unit from its dependencies.

As a QA automation engineer, you need to understand unit tests because they form the base of the testing pyramid. A healthy project has a large number of fast unit tests.

### Where will you main your test cases?
The interviewer probably means "maintain".
"We maintain our test cases in a dedicated Test Case Management (TCM) tool. In my last project, we used **Jira with the Xray plugin**.
-   This allowed us to write and organize our manual and automated test cases directly within Jira.
-   We could link each test case to a specific user story, which gave us clear traceability from requirement to test.
-   When our automated tests ran in Jenkins, we used Xray's REST API to push the results back into Jira, so we always had a live dashboard of our test coverage and pass/fail rates for each story."

Other valid answers: TestRail, qTest, or even just well-organized `.feature` files in a Git repo if you're doing pure BDD.

### What parameter you use for testing in postman?
Postman uses several types of "parameters" to construct an HTTP request.
1.  **Path Parameters:** Part of the URL path itself, used to identify a specific resource. Example: `/users/:userId` where `:userId` is the parameter. In Postman, you'd write `/users/{{userId}}` and define the `userId` variable in the "Path Variables" section.
2.  **Query Parameters:** Key-value pairs appended to the URL after a `?`. Used for filtering and sorting. Example: `/articles?sort=desc&page=2`. In Postman, you enter these in the "Params" tab.
3.  **Headers:** Key-value metadata sent with the request, like `Content-Type: application/json` or `Authorization: Bearer <token>`. Entered in the "Headers" tab.
4.  **Request Body:** The data payload sent with `POST` or `PUT` requests, usually in JSON format. Entered in the "Body" tab.

### Given a URL and write the logic to link all the link given in the website?
This question is phrased strangely. It likely means "write the logic to **validate** all the links on a given URL." This is the classic "broken link checker" test.

The logic is:
1.  Use Selenium to navigate to the given URL.
2.  Find all anchor tags: `List<WebElement> links = driver.findElements(By.tagName("a"));`
3.  Loop through the list of `WebElement`s.
4.  For each element, get the `href` attribute.
5.  If the `href` is valid (not null, not empty, starts with `http`), use a Java HTTP client (`HttpURLConnection` or Apache `HttpClient`) to make a `HEAD` request to the URL. A `HEAD` request is better than `GET` because it only fetches the headers, not the whole page, making it much faster.
6.  Check the HTTP response code. If the code is `400` or greater, log the URL as a broken link.

> **Side Note:** You need to handle multiple threads to make this run in a reasonable amount of time on a page with many links. `links.parallelStream().forEach(...)` is a good way to do this.

### What is the repo you used in your project?
"We used **Git** for version control, and our remote repository was hosted on **GitHub** (or Bitbucket, or GitLab). We followed a feature-branching workflow. For any new feature or bug fix, we'd create a new branch, commit our code to it, and then open a pull request to have it reviewed and merged into the main `develop` branch."

### How will you test using postman tool?
Postman is used for both manual/exploratory API testing and for creating automated checks.
1.  **Exploratory Testing:** I start by creating a new request. I set the HTTP method (`GET`, `POST`, etc.), enter the endpoint URL, add any necessary authorization (like a Bearer Token), and add headers and a request body if needed. I send the request and inspect the response:
    -   Is the status code correct (e.g., `200 OK`, `201 Created`)?
    -   Is the response body structured correctly (valid JSON)?
    -   Does the data in the response look right?
    -   Are the response headers correct (e.g., `Content-Type`)?
    -   How long did it take?
2.  **Automated Checks:** In the "Tests" tab of a Postman request, you can write JavaScript code to run assertions after the response is received.
    ```javascript
    // Example Postman tests
    pm.test("Status code is 200", function () {
        pm.response.to.have.status(200);
    });

    pm.test("Response contains user ID", function () {
        var jsonData = pm.response.json();
        pm.expect(jsonData.user.id).to.eql("123");
    });
    ```
3.  **Collections:** I organize these requests into a "Collection" for a specific feature or service. Then I can use the **Collection Runner** to run all the requests and their associated tests in sequence. This collection can also be exported and run from the command line using **Newman**, Postman's command-line runner, for CI/CD integration.

### When will you do retrospective?
A sprint retrospective is held at the **end of every sprint**, after the Sprint Review but before the next Sprint Planning meeting.

### Day to day activities?
Standard question.
-   Morning: Daily stand-up meeting to sync with the team.
-   During the day:
    -   Analyze new user stories from the sprint backlog.
    -   Design and write new automated tests (UI or API).
    -   Execute test suites against new builds.
    -   Perform exploratory testing on new features.
    -   Investigate test failures, report bugs in Jira.
    -   Collaborate with developers to debug and verify fixes.
    -   Maintain and refactor the test framework.

### About Agile?
"Agile is an iterative approach to software development that focuses on delivering value to customers in small increments. Instead of a single 'big bang' release, we work in short cycles called sprints. The core idea is to embrace change, collaborate closely with the customer, and continuously improve the process. My team follows the Scrum framework, which is the most popular way to implement Agile."

### Do you have experience in SQL?
"Yes. I am proficient in writing basic to intermediate SQL queries. In my automation framework, I often use JDBC to connect to our application's database to:
-   **Set up test data:** Inserting a specific user or product into the database before a test runs.
-   **Verify results:** Querying the database after a test action to confirm that the data was correctly written or updated by the application.
-   **Clean up:** Deleting test data created during the test run to ensure test isolation."

### Given a scenario based on the current project and asked if you missed some major criteria what will happen in this case?
This tests your sense of responsibility and process.
"If I realized that a major requirement or acceptance criterion was missed during testing, the impact could be severe—it could mean a critical bug leaks into production.
My immediate actions would be:
1.  **Escalate Immediately:** I would notify the Test Lead, my Product Owner, and the development team right away. Transparency is key.
2.  **Assess the Impact:** We would quickly assess the risk. Has the code already been deployed? If so, what is the potential impact on users?
3.  **Halt the Release (if possible):** If we're pre-release, I would strongly advocate for halting the release until we can test the missing criteria and fix any associated bugs.
4.  **Root Cause Analysis:** After the immediate fire is out, I would initiate a root cause analysis. Why was this missed? Was the requirement unclear? Was our test plan incomplete? We would then update our process (e.g., improve our backlog grooming checklist, enhance our peer review process for test cases) to prevent it from happening again."

### How will you handle git conflict?
A Git conflict occurs when you try to merge a branch that has changes that conflict with changes in the target branch (e.g., both branches edited the same line of code).

**The process to resolve it:**
1.  **Don't panic.** Git will mark the conflicted files clearly.
2.  **Pull the latest changes:** First, make sure my local branch is up to date: `git checkout main` and `git pull`.
3.  **Merge:** Switch back to my feature branch (`git checkout my-feature-branch`) and try to merge the main branch into it: `git merge main`.
4.  **Identify Conflicts:** Git will now report the conflict and mark the areas in the conflicted file(s) with `<<<<<<<`, `=======`, and `>>>>>>>`.
5.  **Resolve the Conflict:** I will open the conflicted file in my IDE. I will look at the two conflicting blocks of code: the "incoming" change from `main` and "my" change. I will talk to the developer who wrote the incoming change if necessary, and manually edit the file to incorporate the correct logic, then delete the Git conflict markers.
6.  **Stage and Commit:** Once the file is correct, I will stage the resolved file: `git add <conflicted-file-name>`.
7.  **Complete the Merge:** I will then commit the merge: `git commit`. Git usually provides a default merge commit message. After that, my branch is conflict-free and ready to be pushed.
