---
title: "Project Deep Dive: IntelliLearn"
date: 2026-01-30
draft: false
weight: 9
---

**MEMORIZE THIS.** This is your safety net. If you blank out, revert to this script.

## 1. The "Elevator Pitch" (Answer to: "Tell me about your project")

"I worked on **IntelliLearn**, which is an **EdTech platform** used by the Learning Links Foundation. Ideally, it connects **Teachers** and **Students** for adaptive learning.

The core feature is that it's not just a video player; it adapts to the student. If a student fails a quiz, the system automatically suggests remedial content.

My role was testing the **Teacher Dashboard** (where they upload content) and the **Student Assessment Flow**. We had a **Web Interface** built with React (Frontend) and a **Java/Spring Boot** backend. I was responsible for the **Hybrid Automation Framework** to test the critical flows like 'User Registration' and 'Content Assignment'."

---

## 2. The Architecture (Answer to: "How was the application built?")

Even if you didn't code the backend, you MUST know this:
*   **Frontend:** React.js (This explains why you had to handle dynamic elements/wait issues in Selenium).
*   **Backend:** Java Spring Boot (Microservices architecture - e.g., one service for 'User Auth', one for 'Content').
*   **Database:** MySQL (Where user data is stored).
*   **Communication:** REST APIs (JSON format).

**Your Mental Model:**
"When I test the 'Login' page, the Frontend sends a `POST` request to the Auth Service. If valid, it returns a Token (JWT). I verified this using **Postman**."

---

## 3. Key Modules You "Owned"
Pick these two modules and stick to them. Don't say "I tested everything."

### Module A: The Assessment Engine (Student Side)
*   **Functionality:** Student takes a quiz. Timer counts down. Score is calculated.
*   **What you Automating:**
    1.  Login as Student.
    2.  Navigate to "Pending Assessments".
    3.  Select an option (Radio button) and click "Next".
    4.  Verify the score is displayed at the end.
*   **The "Challenge" here:** "The timer was dynamic. Sometimes the 'Submit' button wouldn't enable until an option was selected. I had to use `ExpectedConditions.elementToBeClickable`."

### Module B: Content Management (Teacher Side)
*   **Functionality:** Teacher uploads a PDF or Video.
*   **What you Automating:**
    1.  Login as Teacher.
    2.  Click "Upload Material".
    3.  Verify the file upload success message.
*   **The "Challenge" here:** "Handling the Windows File Upload dialog. Selenium can't do it directly, so I used the `sendKeys()` method to the input tag, or sometimes `Robot` class."

---

## 4. Specific "Bugs" You Found (Answer to: "Tell me about a bug you found")

**Bug 1: The "Session Timeout" Bug**
*   **Scenario:** A student starts a 30-minute quiz. They answer questions for 10 minutes, then go idle for 20 minutes (thinking/calculating).
*   **The Bug:** When they clicked "Submit", the system logged them out because the session timeout was set to 15 minutes. They lost all answers.
*   **Your Impact:** "I caught this during exploratory testing. We increased the session timeout for 'Active Assessment' pages to 60 minutes."

**Bug 2: The "Duplicate User" Bug**
*   **Scenario:** Creating a user with email `Test@gmail.com` and `test@gmail.com`.
*   **The Bug:** The system treated them as different users (Case Sensitive DB issue), causing data inconsistency.
*   **Your Impact:** "I reported this as a High Priority defect because it affected reporting. The dev fixed the backend validation to normalize emails to lowercase."

---

## 5. Test Data Strategy (Answer to: "How did you manage test data?")

"We didn't want to use real student data (PII). So, I used a **Faker Library** in Java to generate random names and emails for every test run.
For stable data (like a 'Gold User' that always has a subscription), we kept those credentials in a `config.properties` file."

---

## 6. Trap Question: "How many test cases did you automate?"

*   **Don't say:** "All of them" (Impossible).
*   **Don't say:** "100" (Too low for 2.5 years).
*   **Say:** "We had a regression suite of about **450 test cases**. I was personally responsible for automating and maintaining about **40-50 core scenarios** related to the Assessment module, and maintaining the rest."
