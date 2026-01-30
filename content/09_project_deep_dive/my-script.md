---
title: "My Script: Project Deep Dive"
date: 2026-01-30
draft: false
---

## The "I Was There" Walkthrough

"At Learning Links Foundation, our project was **IntelliLearn**. The biggest challenge I faced was automating the **Adaptive Assessment flow**. 

The system would change the next question based on whether the student got the current one right. This was hard to automate because the flow wasn't linear. 

**What I did:**
I created a data-driven approach using **Scenario Outlines** in Cucumber. I passed different sets of 'Correct' and 'Incorrect' answers from the Feature file to see if the system correctly redirected the student. 

I also integrated our suite with **Jenkins**. I set up a build trigger so that every time the developers pushed code to the `staging` branch, our smoke suite of 20 tests would run automatically. This saved us about 2 hours of manual sanity testing every day."
