---
title: "Comcast Interview Questions"
date: 2026-01-30
draft: false
---

---

| 1. **What tools have you used for API testing?**

   * Examples: Postman, Rest Assured, SoapUI, Swagger, Newman, Karate, etc.

| 2. **How do you validate the API response?**

   * Verify status codes, response body, headers, and schema.
   * Validate using assertions in automation frameworks (e.g., `assertEquals(response.getStatusCode(), 200)` in Rest Assured).

| 3. **What automation frameworks have you worked with?**

   * Example answers:

     * TestNG or JUnit with Selenium
     * BDD (Cucumber)
     * Hybrid Framework (Data-Driven + Keyword-Driven)
     * API Framework with Rest Assured or Karate

| 4. **How do you test authentication mechanisms?**

   * Validate OAuth 2.0 / JWT tokens / Basic Auth / API keys.
   * Handle authentication via headers or pre-request scripts in Postman.
   * Automate token generation and injection using scripts or setup methods in test frameworks.

| 5. **How do you validate database data after UI or API operations?**

   * Use JDBC connection or ORM tools (like Hibernate) to query the database.
   * Compare UI/API response data with DB query results for consistency.

| 6. **How do you run automation tests in a CI/CD pipeline?**

   * Integrate test execution in Jenkins / GitLab CI / Azure DevOps / GitHub Actions.
   * Trigger tests automatically on code push or pull requests.
   * Generate and publish test reports (Extent, Allure, JUnit XML).

| 7. **How do you ensure test coverage?**

   * Maintain traceability between requirements and test cases.
   * Use coverage tools (like JaCoCo, SonarQube) for automation coverage.
   * Regularly review missing scenarios and update regression suites.

| 8. **How do you handle dynamic web elements in Selenium?**

   * Use dynamic XPath or CSS locators with partial matches (`contains()`, `starts-with()`).
   * Use `WebDriverWait` and expected conditions.
   * Identify stable attributes or parent-child hierarchies for reliable element targeting.

| 9. **What’s the difference between functional and non-functional testing?**

   * **Functional Testing:** Validates *what* the system does (features, business logic).
   * **Non-Functional Testing:** Validates *how* the system performs (performance, security, usability, reliability).

| 10. **How do you handle request validation in REST APIs?**

    * Validate input parameters, headers, and payload before sending requests.
    * Use schema validation (JSON Schema) to ensure request/response format.
    * Apply negative testing for invalid or missing parameters.

---
