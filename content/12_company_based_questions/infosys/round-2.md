---
title: "Infosys-2"
date: 2026-01-30
draft: false
---

---

## Original Questions

- Infosys level 2
---------------
Tell abt ur self
Both Project explanation 
Agile process
What is productivity 
Traceability matrix 
Can you do automation without manual testing
Why use n-1 approach 
Explain Estimation
Priority severity 
How will you confirm the complexity of story 
Achievement of the last two project

---

## Answers (No-BS Java QA / SDET Explanations)

### Tell abt ur self
Standard. Keep it professional, concise, and focused on your automation experience.

### Both Project explanation
Be prepared to discuss two distinct projects. For each, cover:
-   The project domain and purpose.
-   Your role and responsibilities.
-   The tech stack you used for automation.
-   A key challenge you faced and how you solved it.

### Agile process
"I work in an Agile environment following the Scrum framework. Our process is built around two-week sprints.
-   It starts with **Sprint Planning**, where we select user stories from the product backlog.
-   We have **Daily Stand-ups** to sync progress and blockers.
-   Throughout the sprint, QA is involved in testing stories as soon as they are ready from development, providing continuous feedback.
-   At the end of the sprint, we have a **Sprint Review** to demo the completed work to stakeholders.
-   Finally, we hold a **Sprint Retrospective** to discuss what went well and what we can improve in the next sprint."

### What is productivity
In a software context, productivity is a measure of the output of a team over a period.
-   **For a development team**, this is often measured by **Velocity** - the number of story points the team consistently completes in a sprint.
-   **For a QA team**, productivity isn't just about the number of test cases written or bugs found. It's about efficiency and impact. Good metrics include:
    -   The percentage of the regression suite that is automated.
    -   The reduction in time for a full regression run.
    -   A low defect leakage rate (fewer bugs escaping to production).

### Traceability matrix
A Requirements Traceability Matrix (RTM) is a document that maps and traces user requirements with test cases. It ensures that every requirement has corresponding test coverage.
-   **Purpose:** To ensure 100% test coverage for all requirements and to perform impact analysis when requirements change.
-   **Modern Implementation:** In Agile teams, this is often handled directly within tools like **Jira** by linking test cases (from plugins like Xray or Zephyr) directly to the user stories they validate.

### Can you do automation without manual testing
"No, you cannot. They serve different purposes.
-   **Automation** is for confirmation and regression. It's excellent at repeatedly checking that existing, known functionality still works.
-   **Manual testing** (specifically, exploratory testing) is for investigation and discovery. A human tester can notice things, ask questions, and explore edge cases that a script would never think to check.
You need automation as a safety net, and you need manual testing to find new and interesting bugs. A good QA strategy relies on both."

### Why use n-1 approach
In testing, the "n-1" approach (or "n-2", etc.) often refers to supporting older versions of software or browsers.
"We use an 'n-1' approach for browser compatibility testing. This means we officially support and run our full regression suite on the **current stable version** of Chrome (n) and the **previous major version** (n-1). This provides a good balance between covering the vast majority of our user base and the cost of maintaining tests for very old, rarely used browser versions."

### Explain Estimation
In Agile, estimation is the process of assigning a relative size to a piece of work (a user story).
-   **Unit:** We use **Story Points**, which are abstract units that represent a combination of effort, complexity, and uncertainty.
-   **Technique:** We use **Planning Poker**. The team discusses a story, and each member privately chooses a Fibonacci-like number (1, 2, 3, 5, 8...) that they feel represents the size. Everyone reveals their number at the same time. If the numbers are far apart, it triggers a discussion to understand different perspectives, and then the team re-votes until a consensus is reached.

### Priority severity
-   **Priority:** The business urgency of fixing a bug. Set by the Product Owner. (High, Medium, Low).
-   **Severity:** The technical impact of the bug on the system. Set by QA. (Critical, Major, Minor).

### How will you confirm the complexity of story
You confirm the complexity of a user story through discussion and analysis during the **Backlog Grooming** or **Sprint Planning** meetings.
As a QA, I contribute by:
1.  **Asking clarifying questions:** "What should happen if the user enters invalid data? What are the performance expectations?"
2.  **Identifying dependencies:** "Does this feature depend on a third-party API that we haven't worked with before?"
3.  **Considering testability:** "Is the feature designed in a way that is easy to automate, or will it require complex workarounds?"
4.  **Breaking it down:** I help break the story down into technical tasks (including testing tasks).
The collective input from development, QA, and product on these points helps the team arrive at an accurate complexity estimate (story points).

### Achievement of the last two project
Be prepared with specific, quantifiable achievements.
-   **Achievement 1:** "On my last project, I led the initiative to parallelize our TestNG regression suite. By refactoring our WebDriver instantiation to be thread-safe and running our tests on a Selenium Grid, I reduced the total regression run time from 4 hours to just 45 minutes, allowing us to run it on every commit."
-   **Achievement 2:** "I designed and implemented a new API test suite from scratch using REST-assured for a critical microservice. This increased our automated test coverage for that service from 0% to over 90% and caught several critical data validation bugs before they reached production."
