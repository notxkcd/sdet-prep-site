---
title: "API Testing Q&A Guide"
date: 2026-01-30
draft: false
categories: ["API Testing"]
---

## Questions Only

1. [What are the main components of an HTTP request and response?](#1-what-are-the-main-components-of-an-http-request-and-response)
2. [Explain idempotency in APIs. Why is it important?](#2-explain-idempotency-in-apis-why-is-it-important)
3. [What is API versioning? How would you test it?](#3-what-is-api-versioning-how-would-you-test-it)
4. [What are the different types of API tests?](#4-what-are-the-different-types-of-api-tests)
5. [What is the difference between synchronous and asynchronous API calls?](#5-what-is-the-difference-between-synchronous-and-asynchronous-api-calls)
6. [What are the status codes you mostly get in API testing? What is 429, 501, 500?](#6-what-are-the-status-codes-you-mostly-get-in-api-testing-what-is-429-501-500)
7. [How do you validate the request methods in API?](#7-how-do-you-validate-the-request-methods-in-api)
8. [How do you validate Broken Links in Rest Assured automation?](#8-how-do-you-validate-broken-links-in-rest-assured-automation)
9. [What are all the methods in Rest Assured?](#9-what-are-all-the-methods-in-rest-assured)
10. [What are the dependencies you use for Rest Assured? In which dependency .given().when() is coming?](#10-what-are-the-dependencies-you-use-for-rest-assured-in-which-dependency-givenwhen-is-coming)
11. [Write GET request using payload in Rest Assured.](#11-write-get-request-using-payload-in-rest-assured)
12. [What is API timeout?](#12-what-is-api-timeout)
13. [What is the difference between API and UI Testing?](#13-what-is-the-difference-between-api-and-ui-testing)
14. [What is token generation?](#14-what-is-token-generation)
15. [What is SQL Injection (in API Security)?](#15-what-is-sql-injection-in-api-security)
16. [Once the URL is ready, what is the basic validation you will do?](#16-once-the-url-is-ready-what-is-the-basic-validation-you-will-do)
17. [What is CRUD?](#17-what-is-crud)
18. [Real-time example you tested in API?](#18-real-time-example-you-tested-in-api)
19. [What you found in collections in API?](#19-what-you-found-in-collections-in-api)
20. [How do you approach testing RESTful APIs?](#20-how-do-you-approach-testing-restful-apis)
21. [What tools have you used for API testing?](#21-what-tools-have-you-used-for-api-testing)
22. [How do you validate response data when testing an API?](#22-how-do-you-validate-response-data-when-testing-an-api)
23. [How do you handle testing APIs when dependent services are down?](#23-how-do-you-handle-testing-apis-when-dependent-services-are-down)
24. [What is mocking in API testing?](#24-what-is-mocking-in-api-testing)
25. [Can you describe how you would automate API testing?](#25-can-you-describe-how-you-would-automate-api-testing)
26. [What is contract testing?](#26-what-is-contract-testing)
27. [How would you handle pagination in API testing?](#27-how-would-you-handle-pagination-in-api-testing)
28. [How do you test error handling & edge cases?](#28-how-do-you-test-error-handling-edge-cases)
29. [How do you test API performance?](#29-how-do-you-test-api-performance)
30. [What is rate limiting? How would you test it?](#30-what-is-rate-limiting-how-would-you-test-it)
31. [How do you test API security?](#31-how-do-you-test-api-security)
32. [Explain concurrency testing in APIs.](#32-explain-concurrency-testing-in-apis)
33. [What is throttling? How would you test it?](#33-what-is-throttling-how-would-you-test-it)
34. [How do you test APIs with dynamic states?](#34-how-do-you-test-apis-with-dynamic-states)
35. [If API returns 500, how would you troubleshoot?](#35-if-api-returns-500-how-would-you-troubleshoot)
36. [How do you test backward compatibility?](#36-how-do-you-test-backward-compatibility)
37. [Describe a challenging API testing issue you faced.](#37-describe-a-challenging-api-testing-issue-you-faced)
38. [Banking API test cases?](#38-banking-api-test-cases)
39. [How would you test third-party APIs?](#39-how-would-you-test-third-party-apis)
40. [How do you ensure accuracy in microservices APIs?](#40-how-do-you-ensure-accuracy-in-microservices-apis)
41. [How to handle continuous API testing in CI/CD?](#41-how-to-handle-continuous-api-testing-in-cicd)
42. [Role of API testing in Agile/DevOps?](#42-role-of-api-testing-in-agiledevops)
43. [How do you deal with unclear API documentation?](#43-how-do-you-deal-with-unclear-api-documentation)
44. [How do you test WebSockets or gRPC APIs?](#44-how-do-you-test-websockets-or-grpc-apis)
45. [What is schema validation in API testing?](#45-what-is-schema-validation-in-api-testing)
46. [Can you explain HATEOAS?](#46-can-you-explain-hateoas)
47. [How do you ensure data privacy in API testing (GDPR)?](#47-how-do-you-ensure-data-privacy-in-api-testing-gdpr)
48. [Show API test in Postman.](#48-show-api-test-in-postman)
49. [Write test cases for sample API.](#49-write-test-cases-for-sample-api)
50. [Third-party API is down. How do you test?](#50-third-party-api-is-down-how-do-you-test)

---

## Questions with Answers

### 1. What are the main components of an HTTP request and response?
**Answer:**
- **Request:** Method (GET, POST, etc.), URL, Headers, Body (optional).
- **Response:** Status Code, Headers, Body (data or error message).

### 2. Explain idempotency in APIs. Why is it important?
**Answer:**
- **Idempotency** means performing the same request multiple times should give the same result.
- Example: `DELETE /user/123` will always delete user 123 (if exists).
- **Importance:** Prevents unintended side effects in retry scenarios (e.g., payment APIs).

### 3. What is API versioning? How would you test it?
**Answer:**
- API versioning allows changes without breaking existing clients.
- Approaches: URL-based (`/v1/users`), Header-based, Query-param based.
- **Testing:** Ensure old versions still work, and new versions return correct responses.

### 4. What are the different types of API tests?
**Answer:**
- **Functional** (correctness, CRUD ops).
- **Performance** (latency, load, stress).
- **Security** (auth, SQL injection, data leaks).
- **Integration** (end-to-end flow across services).

### 5. What is the difference between synchronous and asynchronous API calls?
**Answer:**
- **Synchronous:** Client waits for response (blocking). Example: REST calls.
- **Asynchronous:** Client sends request and continues; response comes later via callback/webhook. Example: WebSockets.

### 6. What are the status codes you mostly get in API testing? What is 429, 501, 500?
**Answer:**
- **200:** OK
- **201:** Created
- **400:** Bad Request
- **401:** Unauthorized
- **403:** Forbidden
- **404:** Not Found
- **500:** Internal Server Error
- **501:** Not Implemented
- **429:** Too Many Requests (rate limit exceeded)

### 7. How do you validate the request methods in API?
**Answer:**
- Check if supported methods return correct responses.
- Example: Sending `POST` instead of `GET` should return `405 Method Not Allowed`.

### 8. How do you validate Broken Links in Rest Assured automation?
**Answer:**
- By checking response code for each URL.
- Code snippet:
```java
given().when().get(url).then().statusCode(200);
```

### 9. What are all the methods in Rest Assured?
**Answer:**
- **HTTP methods:** GET, POST, PUT, PATCH, DELETE, OPTIONS, HEAD.
- **Utility methods:** given(), when(), then(), extract(), log(), etc.

### 10. What are the dependencies you use for Rest Assured? In which dependency .given().when() is coming?
**Answer:**
- **Dependencies:** `rest-assured`, `json-path`, `hamcrest`.
- `.given().when().then()` comes from **rest-assured** dependency.

### 11. Write GET request using payload in Rest Assured.
**Answer:**
```java
given()
   .header("Content-Type", "application/json")
   .body("{\"id\": 123}")
.when()
   .get("/users")
.then()
   .statusCode(200);
```

### 12. What is API timeout?
**Answer:**
- Maximum wait time for a response before client aborts request.
- Important for performance testing and preventing infinite waits.

### 13. What is the difference between API and UI Testing?
**Answer:**
- **API Testing:** Validates data, logic, response codes, speed.
- **UI Testing:** Validates design, usability, workflow.

### 14. What is token generation?
**Answer:**
- Token = authentication mechanism (JWT, OAuth).
- Generated after login/authentication and used for secure API calls.

### 15. What is SQL Injection (in API Security)?
**Answer:**
- Malicious query insertion via inputs (`id=1 OR 1=1`).
- Prevented by **parameterized queries & input validation**.

### 16. Once the URL is ready, what is the basic validation you will do?
**Answer:**
- Status Code = 200.
- Response Time.
- Content-Type = expected format (JSON/XML).
- Schema validation.

### 17. What is CRUD?
**Answer:**
- **C:** Create (POST)
- **R:** Read (GET)
- **U:** Update (PUT/PATCH)
- **D:** Delete (DELETE)

### 18. Real-time example you tested in API?
**Answer:**
- Example: E-commerce checkout API. Validated **cart, payment, and order confirmation** flow.

### 19. What you found in collections in API?
**Answer:**
- Postman collections help organize test cases (login, CRUD, workflows).

### 20. How do you approach testing RESTful APIs?
**Answer:**
1. Understand API spec/documentation.
2. Test CRUD operations.
3. Validate response codes & schema.
4. Test negative cases & edge cases.
5. Security & performance validation.

### 21. What tools have you used for API testing?
**Answer:**
- **Manual:** Postman, SoapUI.
- **Automation:** Rest Assured, JMeter, Newman, Karate, Cypress.

### 22. How do you validate response data when testing an API?
**Answer:**
- Compare against schema (JSON schema).
- Assert expected fields, values, types.
- Example in Rest Assured:
```java
body("name", equalTo("Shahid"));
```

### 23. How do you handle testing APIs when dependent services are down?
**Answer:**
- Use **mock servers / stubs**.
- Simulate responses with Postman Mock, WireMock.

### 24. What is mocking in API testing?
**Answer:**
- Simulating API responses when real API/service is unavailable.

### 25. Can you describe how you would automate API testing?
**Answer:**
- Use Rest Assured (Java), Postman + Newman, or Cypress.
- Integrate tests in CI/CD pipeline.

### 26. What is contract testing?
**Answer:**
- Ensures API meets predefined **request/response contract** (fields, types).
- Tools: Pact, Swagger.

### 27. How would you handle pagination in API testing?
**Answer:**
- Validate `limit`, `offset`, `page` params.
- Ensure `next/prev` links work correctly.

### 28. How do you test error handling & edge cases?
**Answer:**
- Invalid inputs, missing fields, wrong methods.
- Check for meaningful error messages + proper codes.

### 29. How do you test API performance?
**Answer:**
- Use JMeter, Locust.
- Metrics: Response time, Throughput, Latency, Error rate.

### 30. What is rate limiting? How would you test it?
**Answer:**
- Restricts number of requests in time window.
- Test by sending bursts of requests → expect `429`.

### 31. How do you test API security?
**Answer:**
- Test for **auth (JWT, OAuth)**.
- Check **vulnerabilities**: SQL Injection, XSS, CSRF, Data leakage.

### 32. Explain concurrency testing in APIs.
**Answer:**
- Test multiple simultaneous requests.
- Validate **race conditions** (e.g., two users buying last product).

### 33. What is throttling? How would you test it?
**Answer:**
- Server intentionally slows responses to avoid overload.
- Test by sending high traffic, check delayed responses.

### 34. How do you test APIs with dynamic states?
**Answer:**
- Example: Shopping cart → Add, Update, Delete, Checkout.
- Validate correct state transitions.

### 35. If API returns 500, how would you troubleshoot?
**Answer:**
- Check logs, request payload, headers.
- Validate backend issues (DB, service failure).

### 36. How do you test backward compatibility?
**Answer:**
- Run tests on old and new versions.
- Ensure old clients still work with updated API.

### 37. Describe a challenging API testing issue you faced.
**Answer (example):**
- API response had inconsistent formats.
- Solved using **JSON schema validation** and collaboration with devs.

### 38. Banking API test cases?
**Answer:**
- Login & Authentication.
- Balance inquiry.
- Fund transfer (valid/invalid accounts).
- Transaction history.
- Rate limiting & security checks.

### 39. How would you test third-party APIs?
**Answer:**
- Use **sandbox environment**.
- Mock/stub third-party responses if unavailable.
- Validate request/response mapping.

### 40. How do you ensure accuracy in microservices APIs?
**Answer:**
- Validate **end-to-end workflows**.
- Cross-check data consistency across services.

### 41. How to handle continuous API testing in CI/CD?
**Answer:**
- Integrate tests using Jenkins, GitHub Actions, GitLab CI.
- Run API test suite after deployment.

### 42. Role of API testing in Agile/DevOps?
**Answer:**
- Fast feedback.
- Shift-left testing.
- Automated regression in CI/CD.

### 43. How do you deal with unclear API documentation?
**Answer:**
- Collaborate with devs.
- Use Swagger/OpenAPI specs.
- Reverse-engineer using tools like Postman capture.

### 44. How do you test WebSockets or gRPC APIs?
**Answer:**
- **WebSockets:** Test message exchange, connection handling.
- **gRPC:** Test protobuf schema, validate request/response using tools like BloomRPC.

### 45. What is schema validation in API testing?
**Answer:**
- Ensures API response follows expected structure (fields, types).
- Example: JSON schema validation.

### 46. Can you explain HATEOAS?
**Answer:**
- **Hypermedia as the Engine of Application State.**
- REST API responses include **links** to navigate resources.
- Example: `GET /orders/123` response contains link to `/orders/123/payment`.

### 47. How do you ensure data privacy in API testing (GDPR)?
**Answer:**
- Mask sensitive data (PII).
- Avoid storing credentials in logs.
- Use secure tokens instead of passwords.

### 48. Show API test in Postman.
**Answer:**
- Send GET request → Check `status=200`, response body.
- Add **tests** in Postman:
```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});
```

### 49. Write test cases for sample API.
**Answer:**
- Status code validation.
- Response schema validation.
- Field presence & values.
- Error handling (invalid input).

### 50. Third-party API is down. How do you test?
**Answer:**
- Use **mock responses**.
- Test integration layer separately.
