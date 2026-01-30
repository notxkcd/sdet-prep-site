---
title: "Capgemini-3"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

- Capgemini Level 1 Hr# Tadepalli
------------------------------
1.Tell about yourselves
2. Roles and Responsibilities
3. How will you write negative scenarios
4. what all the HTTP methods
5. how will you rate yourself in API	
6. full form of J-son
7. difference between post and put 
8. can we use POST method for Updates
9. how much will you rate yourself in selenium
10. how much will you rate yourself in selenium
11. using hashmap find the occurrence of the number 635666666666.66
12. String str= " hello hello world hello" what is the occurance of hello
13. Are you into api manual or api automation ? how long ?
14. any questions for me

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. Tell about yourselves
Standard opening. Be concise, professional, and focus on your relevant experience and skills.

### 2. Roles and Responsibilities
Be specific about what you do day-to-day.
-   "My primary role is an SDET, responsible for designing, developing, and maintaining our automated test suites."
-   "My responsibilities include writing UI tests with Selenium, API tests with REST-assured, integrating these tests into our Jenkins CI/CD pipeline, and analyzing failures."
-   "I also collaborate with developers on bug fixes and with the product team during sprint planning to provide testing estimates."

### 3. How will you write negative scenarios
Negative scenarios test how the system behaves under invalid or unexpected conditions.
-   **Invalid Input:** Test with data that violates business rules (e.g., trying to register with an already existing email, entering text into a number field, submitting a form with required fields empty).
-   **Boundary Violations:** Test values outside the valid range (e.g., entering an age of 17 or 101 when the valid range is 18-100).
-   **Security:** Test for unauthorized access (e.g., a non-admin user trying to access an admin page).
-   **System Errors:** Test how the system responds to external failures (e.g., what happens if a third-party API call fails?).

### 4. what all the HTTP methods
The primary HTTP methods (or verbs) are:
-   `GET`: Retrieve data from a server.
-   `POST`: Create a new resource on the server.
-   `PUT`: Completely replace/update an existing resource.
-   `PATCH`: Partially update an existing resource.
-   `DELETE`: Remove a resource from the server.

### 5. how will you rate yourself in API
Be confident but honest.
"I would rate myself a solid **8 out of 10** in API automation. I'm very comfortable with REST-assured, writing tests for various endpoints, handling authentication, and validating complex JSON responses. I have practical experience integrating these tests into a CI/CD pipeline. I'm always learning more about advanced topics like performance and security testing of APIs, which is why I don't say 10."

### 6. full form of J-son
**JavaScript Object Notation**.

### 7. difference between post and put
-   **`POST`:** Used to **create** a new resource. It is **not idempotent** (calling it twice creates two new resources).
-   **`PUT`:** Used to **update or replace** an existing resource completely. It is **idempotent** (calling it twice with the same data has the same effect as calling it once).

### 8. can we use POST method for Updates
While `PUT` and `PATCH` are the standard HTTP methods for updates, some APIs do use `POST` for updates, especially for complex operations that don't fit the `PUT`/`PATCH` model. For example, a `POST` to `/users/123/reset-password`. It's not strictly RESTful, but it happens. So the answer is, "According to REST principles, `PUT` or `PATCH` should be used for updates. However, it is technically possible for an API to be designed to accept `POST` requests for update operations, although it's not standard practice."

### 9. how much will you rate yourself in selenium
Similar to the API question. "I'd rate myself a **9 out of 10**. I have extensive hands-on experience building and maintaining complex Selenium frameworks from the ground up, using advanced concepts like the Page Object Model, explicit waits, and running tests in parallel on Selenium Grid. I'm very comfortable tackling any UI automation challenge with it."

### 10. how much will you rate yourself in selenium
(This is a duplicate question, likely a typo in the interview notes). Just reiterate your previous answer confidently.

### 11. using hashmap find the occurrence of the number 635666666666.66
This is a trick question. The number is irrelevant. The question is about finding the frequency of *digits* in a number. You'd first convert the number to a string.

```java
import java.util.HashMap;
import java.util.Map;

public class DigitCounter {
    public static void main(String[] args) {
        double number = 635666666666.66;
        // Convert the number to a string and remove the decimal point
        String numStr = String.valueOf(number).replace(".", "");

        Map<Character, Integer> digitCount = new HashMap<>();

        for (char digit : numStr.toCharArray()) {
            digitCount.put(digit, digitCount.getOrDefault(digit, 0) + 1);
        }

        // Print the result
        System.out.println("Occurrence of digits in " + number + ":");
        digitCount.forEach((digit, count) -> 
            System.out.println("Digit '" + digit + "' appears " + count + " times.")
        );
    }
}
```

### 12. String str= " hello hello world hello" what is the occurance of hello
Split the string into words and use a `HashMap` to count the occurrences of each word.

```java
import java.util.HashMap;
import java.util.Map;

public class WordCounter {
    public static void main(String[] args) {
        String str = " hello hello world hello";
        // Trim leading/trailing whitespace and split by one or more spaces
        String[] words = str.trim().split("\\s+");

        Map<String, Integer> wordCount = new HashMap<>();
        for (String word : words) {
            wordCount.put(word, wordCount.getOrDefault(word, 0) + 1);
        }

        System.out.println("The word 'hello' appears " + wordCount.get("hello") + " times.");
        // Output: The word 'hello' appears 3 times.
    }
}
```

### 13. Are you into api manual or api automation ? how long ?
"I do both, but my primary focus and expertise are in **API automation**. I've been writing automated API tests for the last [X] years. I use manual testing with Postman for initial exploration of new endpoints or for quick validation, but I believe in automating all regression and contract tests for reliability and speed."

### 14. any questions for me
Yes, always have questions prepared.
-   "What is the team's current ratio of manual to automated testing?"
-   "What are the biggest quality assurance challenges the team is currently facing?"
-   "What does the onboarding process look like for a new SDET on this team?"

```
