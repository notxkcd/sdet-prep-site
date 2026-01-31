---
title: "API Testing Interview Questions"
date: 2026-01-30
draft: false
categories: ["API Testing"]
---

## Beginner (Basics & Concepts)
1. [Explain API?](#1-explain-api)
2. [What is an API?](#2-what-is-an-api)
3. [What are the different types of API?](#3-what-are-the-different-types-of-api)
4. [What is the full form of J-SON?](#4-what-is-the-full-form-of-j-son)
5. [Explain CRUD operations?](#5-explain-crud-operations)
6. [What are the main components of an HTTP request and response?](#6-what-are-the-main-components-of-an-http-request-and-response)
7. [What are common status codes you get in API testing?](#7-what-are-common-status-codes-you-get-in-api-testing)
8. [What is the difference between POST and PUT?](#8-what-is-the-difference-between-post-and-put)
9. [What is the difference between PUT and PATCH?](#9-what-is-the-difference-between-put-and-patch)
10. [What is the difference between GET and POST?](#10-what-is-the-difference-between-get-and-post)
11. [What is the difference between synchronous and asynchronous API calls?](#11-what-is-the-difference-between-synchronous-and-asynchronous-api-calls)
12. [Explain idempotency in APIs? Why is it important?](#12-explain-idempotency-in-apis-why-is-it-important)
13. [What is API versioning and why is it needed?](#13-what-is-api-versioning-and-why-is-it-needed)
14. [What are query parameters and path parameters?](#14-what-are-query-parameters-and-path-parameters)

## Intermediate (Tools & Methods)
1. [What tools have you used for API testing (Manual & Automation)?](#tools-used)
2. [How do you use Postman for API testing?](#postman-testing)
3. [Explain Postman tool extensions?](#postman-extensions)
4. [How do you use authentication in Postman?](#postman-authentication)
5. [How do you use collections in Postman?](#postman-collections)
6. [How do you use environments and variables in Postman?](#postman-variables)
7. [Explain the concept of Rest Assured?](#rest-assured-concept)
8. [What are all the methods in Rest Assured?](#rest-assured-methods)
9. [What are the dependencies needed for Rest Assured?](#rest-assured-dependencies)
10. [What is chaining in Rest Assured?](#rest-assured-chaining)
11. [How do you validate the status code in Rest Assured?](#validate-status-code)
12. [How do you validate the response body in Rest Assured?](#validate-response-body)
13. [Explain .given(), .when(), and .then() in Rest Assured?](#given-when-then)
14. [How do you handle JSON response validation?](#json-validation)
15. [What is mocking in API testing and what tools do you use?](#api-mocking)
16. [What is contract testing and why is it important?](#contract-testing)

## Advanced (Scenarios & Architecture)
1. [How do you approach testing RESTful APIs from scratch?](#approach-testing)
2. [How do you cover end-to-end API testing?](#end-to-end-testing)
3. [How do you handle API testing when dependent services are down?](#dependent-services-down)
4. [What is SQL Injection in API security testing?](#sql-injection-api)
5. [Explain concurrency testing in APIs?](#concurrency-testing)
6. [If an API returns a 500 error, how would you troubleshoot it?](#troubleshoot-500-error)
7. [How do you test backward compatibility of an API?](#backward-compatibility)
8. [Describe a challenging API testing issue you have faced and how you resolved it?](#challenging-issue)
9. [How do you integrate API tests into a CI/CD pipeline?](#cicd-integration)
10. [How do you validate response data integrity against a database?](#data-integrity-db)
11. [How do you perform performance testing for APIs?](#api-performance)
12. [Write a code snippet for a POST request in Rest Assured?](#post-request-code)

---

## Questions with Answers

### Beginner (Basics & Concepts) - Answers

### 1. Explain API? {#1-explain-api}
**Answer**: API stands for **Application Programming Interface**. It acts as a bridge that allows two software applications to communicate and share data with each other.

### 2. What is an API? {#2-what-is-an-api}
**Answer**: It's a set of rules and protocols that specify how software components should interact. Think of it as a waiter in a restaurant taking your order (request) to the kitchen (server) and bringing back your food (response).

### 3. What are the different types of API? {#3-what-are-the-different-types-of-api}
**Answer**:
1. **REST** (Representational State Transfer) - Most popular for web.
2. **SOAP** (Simple Object Access Protocol) - XML based, highly secure.
3. **GraphQL** - Allows clients to request exactly the data they need.
4. **gRPC** - High performance, used in microservices.

### 4. What is the full form of J-SON? {#4-what-is-the-full-form-of-j-son}
**Answer**: **JavaScript Object Notation**. It is a lightweight data-interchange format that is easy for humans to read and write and easy for machines to parse.

### 5. Explain CRUD operations? {#5-explain-crud-operations}
**Answer**:
- **C**: Create (**POST**)
- **R**: Read (**GET**)
- **U**: Update (**PUT/PATCH**)
- **D**: Delete (**DELETE**)

### 6. What are the main components of an HTTP request and response? {#6-what-are-the-main-components-of-an-http-request-and-response}
**Answer**:
- **Request**: URL, Method (GET/POST), Headers, Body (Payload).
- **Response**: Status Code, Headers, Body (JSON/XML).

### 7. What are common status codes you get in API testing? {#7-what-are-common-status-codes-you-get-in-api-testing}
**Answer**:
- **200**: OK (Success)
- **201**: Created (Success after POST)
- **400**: Bad Request (Client error)
- **401**: Unauthorized (Auth missing)
- **403**: Forbidden (No permission)
- **404**: Not Found
- **500**: Internal Server Error

### 8. What is the difference between POST and PUT? {#8-what-is-the-difference-between-post-and-put}
**Answer**:
- **POST**: Used to create a **new** resource. Not idempotent (multiple calls create multiple resources).
- **PUT**: Used to update/replace an existing resource. It is **idempotent** (multiple calls yield the same result).

### 9. What is the difference between PUT and PATCH? {#9-what-is-the-difference-between-put-and-patch}
**Answer**:
- **PUT**: Replaces the **entire** resource with the new body.
- **PATCH**: Performs a **partial update** (only changes the fields provided in the body).

### 10. What is the difference between GET and POST? {#10-what-is-the-difference-between-get-and-post}
**Answer**:
- **GET**: Retrieves data. Data is visible in the URL.
- **POST**: Submits data. Data is hidden in the request body (more secure for sensitive info).

### 11. What is the difference between synchronous and asynchronous API calls? {#11-what-is-the-difference-between-synchronous-and-asynchronous-api-calls}
**Answer**:
- **Synchronous**: Client waits for the server to process the request and respond (blocking).
- **Asynchronous**: Client sends the request and continues its work; server notifies the client via callback/webhook when done (non-blocking).

### 12. Explain idempotency in APIs? Why is it important? {#12-explain-idempotency-in-apis-why-is-it-important}
**Answer**: An operation is idempotent if it can be performed multiple times without changing the result beyond the initial application. **GET, PUT, DELETE** are idempotent. It's important for ensuring system stability during retries.

### 13. What is API versioning and why is it needed? {#13-what-is-api-versioning-and-why-is-it-needed}
**Answer**: Versioning (e.g., `v1`, `v2`) allows you to make changes to your API without breaking existing client integrations.

### 14. What are query parameters and path parameters? {#14-what-are-query-parameters-and-path-parameters}
**Answer**:
- **Path Param**: Part of the URL path used to identify a specific resource (e.g., `/users/{id}`).
- **Query Param**: Appended after `?` to filter or sort results (e.g., `/users?sort=desc`).

### Intermediate (Tools & Methods) - Answers

### 1. What tools have you used for API testing? {#tools-used}
**Answer**: I use **Postman** for manual testing and exploratory work, and **Rest Assured** (Java) for automated regression suites.

### 2. How do you use Postman for API testing? {#postman-testing}
**Answer**: I create requests (GET/POST), set headers and body, add assertions in the "Tests" tab (JavaScript), and use the collection runner for group execution.

### 3. Explain Postman tool extensions? {#postman-extensions}
**Answer**: Extensions like **Interceptor** allow you to capture browser requests and send them directly to Postman for debugging.

### 4. How do you use authentication in Postman? {#postman-authentication}
**Answer**: In the "Auth" tab of a request or collection. Common types: **Bearer Token**, **Basic Auth**, and **API Key**.

### 5. How do you use collections in Postman? {#postman-collections}
**Answer**: I group related API requests (e.g., "Login Flow") into a collection to organize them, share them with the team, and run them as a suite.

### 6. How do you use environments and variables in Postman? {#postman-variables}
**Answer**: I define environments (QA, Prod) to store dynamic values like `baseUrl` or `token`. I use `{{variable_name}}` syntax to refer to them in requests.

### 7. Explain the concept of Rest Assured? {#rest-assured-concept}
**Answer**: Rest Assured is a Java library used to automate REST APIs. it uses a **Domain Specific Language (DSL)** that makes tests readable and easy to write.

### 8. What are all the methods in Rest Assured? {#rest-assured-methods}
**Answer**:
- HTTP: `get()`, `post()`, `put()`, `delete()`, `patch()`.
- BDD: `given()`, `when()`, `then()`.
- Utility: `extract()`, `log()`, `auth()`.

### 9. What are the dependencies needed for Rest Assured? {#rest-assured-dependencies}
**Answer**: `rest-assured`, `json-path` (for parsing JSON), and `hamcrest` (for assertions) are typically added to the `pom.xml`.

### 10. What is chaining in Rest Assured? {#rest-assured-chaining}
**Answer**: It's the process of using the output of one request (e.g., a token from login) as the input for the next request.

### 11. How do you validate the status code in Rest Assured? {#validate-status-code}
**Answer**:
```java
then().statusCode(200);
```

### 12. How do you validate the response body in Rest Assured? {#validate-response-body}
**Answer**: Using Hamcrest matchers:
```java
then().body("name", equalTo("Shahid"));
```

### 13. Explain .given(), .when(), and .then() in Rest Assured? {#given-when-then}
**Answer**:
- **given()**: Prerequisities (headers, params, body).
- **when()**: The action (GET/POST request).
- **then()**: Validations (status code, body assertions).

### 14. How do you handle JSON response validation? {#json-validation}
**Answer**: I use **JsonPath** to navigate through the response tree or **POJO deserialization** to map JSON to Java objects.

### 15. What is mocking in API testing and what tools do you use? {#api-mocking}
**Answer**: Simulating an API response when the real service is down or under development. I use **Postman Mock Servers** or **WireMock**.

### 16. What is contract testing and why is it important? {#contract-testing}
**Answer**: It ensures that the producer (server) and consumer (client) agree on the data format. If the API structure changes, contract tests fail instantly.

### Advanced (Scenarios & Architecture) - Answers

### 1. How do you approach testing RESTful APIs from scratch? {#approach-testing}
**Answer**:
1. Review documentation (Swagger).
2. Identify endpoints and methods.
3. Test positive/negative scenarios.
4. Validate status codes and schema.
5. Automate using Rest Assured.

### 2. How do you cover end-to-end API testing? {#end-to-end-testing}
**Answer**: By creating a workflow: `Create User` -> `Login` -> `Update Profile` -> `Delete User`. I pass data from one response to the next request.

### 3. How do you handle API testing when dependent services are down? {#dependent-services-down}
**Answer**: I use **Mocking (Stubbing)** to simulate the behavior of the unavailable service so I can continue testing my module.

### 4. What is SQL Injection in API security testing? {#sql-injection-api}
**Answer**: An attack where malicious SQL code is inserted into API inputs to manipulate the database. I test this by sending characters like `' OR 1=1 --` in the payload.

### 5. Explain concurrency testing in APIs? {#concurrency-testing}
**Answer**: Testing how the API handles multiple simultaneous requests. I check for **race conditions** or database locks.

### 6. If an API returns a 500 error, how would you troubleshoot it? {#troubleshoot-500-error}
**Answer**:
1. Check the server logs (Splunk/ELK).
2. Verify the request payload and headers.
3. Check the database connectivity and health.

### 7. How do you test backward compatibility of an API? {#backward-compatibility}
**Answer**: By running my regression suite against both the old version and the new version to ensure old clients don't break.

### 8. Describe a challenging API testing issue you have faced and how you resolved it? {#challenging-issue}
**Answer**: Handling a complex nested JSON response with dynamic keys. I resolved it by using **JsonPath** filters and regular expressions.

### 9. How do you integrate API tests into a CI/CD pipeline? {#cicd-integration}
**Answer**: By creating a Jenkins job that runs `mvn test`. I use **Newman** for running Postman collections in the pipeline.

### 10. How do you validate response data integrity against a database? {#data-integrity-db}
**Answer**: I use **JDBC** in my automation framework to query the database and then compare the DB result with the API response body.

### 11. How do you perform performance testing for APIs? {#api-performance}
**Answer**: I use **JMeter**. I define thread groups, set the load, and monitor metrics like **Response Time**, **Throughput**, and **Error Rate**.

### 12. Write a code snippet for a POST request in Rest Assured? {#post-request-code}
**Answer**:
```java
given()
    .header("Content-Type", "application/json")
    .body(payload)
.when()
    .post("/endpoint")
.then()
    .statusCode(201);
```