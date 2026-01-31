---
title: "QA Interview Theory Bible"
date: 2026-01-31
draft: false
---

## 1. Software Testing Basics

| Question | Answer |
| --- | --- |
| What is Software Testing? | Verifying if software meets requirements and is defect-free. |
| Verification vs Validation? | Verification: "Are we building it right?" (Process); Validation: "Are we building the right thing?" (Product). |
| Static vs Dynamic Testing? | Static: Code reviews/docs; Dynamic: Executing the software. |
| Test Case vs Scenario? | Scenario is "what" to test; Test Case is "how" to test (steps/data). |

---

## 2. SDLC & STLC

### STLC Phases
1. **Requirement Analysis**: Understand what to test.
2. **Test Planning**: Strategy, scope, resources.
3. **Test Design**: Creating test cases/scripts.
4. **Environment Setup**: Preparing the lab.
5. **Test Execution**: Running tests & logging bugs.
6. **Test Closure**: Final report and analysis.

### Entry & Exit Criteria
- **Entry Criteria**: Conditions to start a phase (e.g., Build deployed).
- **Exit Criteria**: Conditions to finish (e.g., 100% test cases passed, no Critical bugs).

---

## 3. Types & Levels of Testing

| Level | Goal |
| --- | --- |
| **Unit** | Test smallest piece of code (methods). |
| **Integration** | Test interaction between modules. |
| **System** | End-to-end testing of the whole app. |
| **UAT** | Client validation for business readiness. |

| Type | Purpose |
| --- | --- |
| **Smoke** | Check if build is stable enough for further testing. |
| **Sanity** | Quick check of specific bug fixes/changes. |
| **Regression** | Ensure new code hasn't broken existing features. |
| **Exploratory** | Unscripted testing to find edge-case bugs. |

---

## 4. Defect Lifecycle & Management

### Bug Statuses
`New` → `Assigned` → `Open` → `Fixed` → `Pending Retest` → `Verified` → `Closed`.

### Severity vs Priority
- **Severity**: Technical impact (e.g., App crashes - High Severity).
- **Priority**: Business urgency (e.g., Wrong logo on homepage - High Priority).

---

## 5. Agile & Scrum

- **Sprint**: A time-boxed iteration (1-4 weeks).
- **User Story**: A requirement from the user's perspective.
- **Scrum Ceremonies**: Sprint Planning, Daily Stand-up, Sprint Review, Retrospective.
- **DoD (Definition of Done)**: Checklist to ensure a story is complete (Code + Test + Review).
