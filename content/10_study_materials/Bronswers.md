---
title: "Bronswers"
date: 2026-01-30
draft: false
---
## 📘 Indium Interview Questions

1.  **Self Introduction**
    *   I'm a QA Automation Engineer with [X] years in Java, Selenium, and API testing. I build solid automation frameworks to make sure the product is top-notch.

2.  **Project Introduction**
    *   At my last job, I built the test automation for a big e-commerce site using Selenium, TestNG, and RestAssured. My work cut down regression time by about 30%.

3.  **Day-to-Day Activities**
    *   I'm in the daily stand-ups, analyzing stories, making test plans, coding automated scripts, and logging any bugs I find.

4.  **Agile Methodology**
    *   It's about building things in small pieces instead of all at once. You build a bit, test it, get feedback, and repeat. It’s all about shipping fast and being able to change direction without a big drama.

5.  **Flipkart XPath**
    *   You don't use brittle XPaths. Instead of counting positions, you find a stable landmark. Tell Selenium, "find the 'Top Deals' section, then grab the product links inside." That way, it doesn't break if the layout changes a bit.

6.  **cURL to Code**
    *   You give the cURL recipe to a library like RestAssured. Tell it the URL and what to get, and it grabs the response. Then you just pull the 'name' field out of the JSON.

7.  **String a = 9645788215 — Remove duplicates and find the second largest number**
    *   Throw the numbers into a Set to automatically kill duplicates. Then sort the unique numbers and grab the second one from the end.

8.  **Git Conflict Scenario**
    *   If two people change the same file, the second person to push needs to do a `git pull` first. Git will flag the conflict, and they have to merge the changes manually before they can push their own work.

9.  **How do you run your test scripts in Jenkins?**
    *   Jenkins is our automation server. We set up a job that watches our Git repo. On a new push, it automatically runs our `mvn test` command and reports if anything broke.

10. **What are your roles and responsibilities in your team?**
    *   I'm the quality gatekeeper. I analyze requirements, plan the testing strategy, build the automation, and hunt down bugs before they can escape to production.

11. **Tomorrow is release day and you find a high-priority bug — how do you handle it?**
    *   Sound the alarm. Immediately report the bug with clear steps to reproduce. Escalate to the lead and PM so they can make the tough call: delay the release or deploy and pray.

12. **What automation challenges have you faced in your last project?**
    *   The biggest headaches are always dynamic elements that change, flaky tests that fail randomly, and just keeping the test suite from becoming a mess as the app grows.

13. **When will you perform smoke and sanity testing?**
    *   A smoke test is a quick check to see if a new build is even testable, like "does the app start?". A sanity test is a focused check after a bug fix to make sure the fix works and didn't break anything obvious nearby.

