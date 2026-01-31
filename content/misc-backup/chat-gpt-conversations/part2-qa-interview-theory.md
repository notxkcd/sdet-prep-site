# QA Interview Prep - Part 2: Testing Theory, Functional Interfaces, and Collections

This file contains the detailed interview preparation material for Testing Theory, API/DB Testing, Functional Interfaces, and the Java Collections Framework.

## Table of Contents
- [4. Testing Theory](#4-testing-theory)
- [5. API & Database Testing](#5-api--database-testing)
- [6. Functional Interfaces](#6-functional-interfaces)
- [7. Java Collections Framework](#7-java-collections-framework)

---

## 4. Testing Theory

### Q: What are the key theory questions related to software testing that I should expect in an interview?

**Answer:**

Excellent 👏 — this is the **missing piece** many automation testers overlook.

Even if you’re great at Java + Selenium, most Indian interviews (especially for **2–3 years of QA experience**) will include **pure testing theory questions** — to check your _foundation as a tester_.

These questions come from **manual testing, SDLC, STLC, test design, defect lifecycle, and QA principles.**

Here’s your **complete list of 50+ theory questions** — all that you can expect in interviews.  
I’ve grouped them topic-wise, so it’s super easy to remember.

#### 🧪 QA & Testing Theory Questions (2-Year Automation Tester)

**📘 1️⃣ Software Testing Basics**

| # | Question | What They’re Checking |
| --- | --- | --- |
| 1 | What is software testing? | Core definition |
| 2 | Why is testing important? | Purpose of QA |
| 3 | What is the difference between verification and validation? | QA vs QC clarity |
| 4 | What are the 7 principles of testing? | ISTQB fundamentals |
| 5 | What is the difference between QA and QC? | Process vs Product |
| 6 | What are static and dynamic testing? | Code review vs execution |
| 7 | What is a test case? | Documentation basics |
| 8 | What is a test scenario? | Requirement-based testing |
| 9 | What is a test plan? | Planning knowledge |
| 10 | What is a test strategy? | Organizational approach |

**⚙️ 2️⃣ SDLC & STLC**

| # | Question | What They’re Checking |
| --- | --- | --- |
| 11 | What is SDLC? | Software development phases |
| 12 | What are different SDLC models? | Waterfall, Agile, V-Model |
| 13 | What is STLC? | Testing lifecycle |
| 14 | What are the phases of STLC? | Requirement → Closure |
| 15 | What is entry and exit criteria? | Test phase control |
| 16 | What are deliverables in STLC? | Test plan, test cases, report |
| 17 | Difference between SDLC and STLC? | Development vs testing flow |

**🧩 3️⃣ Types & Levels of Testing**

| # | Question | What They’re Checking |
| --- | --- | --- |
| 18 | What are different levels of testing? | Unit, Integration, System, UAT |
| 19 | What are different types of testing? | Functional, Non-functional |
| 20 | What is smoke testing? | Build verification |
| 21 | What is sanity testing? | Quick validation |
| 22 | Difference between smoke and sanity testing? | Sequence and purpose |
| 23 | What is regression testing? | Impact verification |
| 24 | What is retesting? | Fixed defect validation |
| 25 | What is system testing? | Full application test |
| 26 | What is acceptance testing? | Business validation |
| 27 | What is ad-hoc testing? | Exploratory skills |

**🧠 4️⃣ Test Design Techniques**

| # | Question | What They’re Checking |
| --- | --- | --- |
| 28 | What are black-box testing techniques? | Functional testing |
| 29 | What is boundary value analysis (BVA)? | Range-based test design |
| 30 | What is equivalence partitioning (EP)? | Input categorization |
| 31 | What is decision table testing? | Conditional logic |
| 32 | What is state transition testing? | Workflow testing |
| 33 | What is use-case testing? | Business scenario coverage |
| 34 | What are white-box testing techniques? | Code-level testing |
| 35 | What is statement, branch, and path coverage? | Code coverage metrics |

**🐞 5️⃣ Defect / Bug Lifecycle**

| # | Question | What They’re Checking |
| --- | --- | --- |
| 36 | What is a defect or bug? | Core definition |
| 37 | What is the defect life cycle? | New → Closed flow |
| 38 | What are different defect statuses? | New, Open, Fixed, Retest, Closed |
| 39 | What are severity and priority? | Impact vs urgency |
| 40 | Who decides severity and priority? | Tester vs business |
| 41 | What is defect leakage and defect clustering? | QA principles |
| 42 | What is root cause analysis (RCA)? | Analytical thinking |

**🧭 6️⃣ Agile & Scrum Methodology**

| # | Question | What They’re Checking |
| --- | --- | --- |
| 43 | What is Agile methodology? | Adaptive model understanding |
| 44 | What is Scrum? | Agile framework |
| 45 | What are Scrum ceremonies? | Sprint planning, daily standup, etc. |
| 46 | What are roles in Scrum? | PO, SM, Dev team |
| 47 | What is a sprint? | Iteration concept |
| 48 | What is a user story? | Agile requirement |
| 49 | What is story point estimation? | Effort-based sizing |
| 50 | What is sprint retrospective? | Continuous improvement |
| 51 | What is the difference between Agile and Waterfall? | Flexibility vs rigidity |

**🧾 7️⃣ Test Metrics & Reporting**

| # | Question | What They’re Checking |
| --- | --- | --- |
| 52 | What are test metrics? | Measurement of testing progress |
| 53 | Examples of test metrics | Defect density, Test coverage, Pass % |
| 54 | What is traceability matrix (RTM)? | Requirement → Test mapping |
| 55 | What is test coverage? | Completeness of testing |
| 56 | What is defect density? | Quality measurement |

**🔐 8️⃣ Environment, Data & Tools**

| # | Question | What They’re Checking |
| --- | --- | --- |
| 57 | What is test environment? | Where testing happens |
| 58 | What is test data? | Input values for testing |
| 59 | What tools do you use for bug tracking? | Jira, Bugzilla, etc. |
| 60 | What tools do you use for test management? | TestLink, Zephyr, Xray |
| 61 | How do you handle test data management? | Reuse, anonymization |
| 62 | What are some challenges you faced during testing? | Experience & communication |

**⚡ 9️⃣ Automation-Specific Theory**

| # | Question | What They’re Checking |
| --- | --- | --- |
| 63 | What is automation testing? | Purpose & benefits |
| 64 | What are the advantages of automation testing? | Speed, coverage, accuracy |
| 65 | What are limitations of automation testing? | Not suitable for UI or ad-hoc |
| 66 | What is a hybrid framework? | Combination of data-driven + keyword-driven |
| 67 | What is data-driven testing? | Test with multiple data sets |
| 68 | What is keyword-driven testing? | Action-based framework |
| 69 | What is the difference between manual and automation testing? | Manual effort vs tool-based |
| 70 | When do you automate a test case? | Stable, repeatable, high-impact tests |

**🧭 10️⃣ QA Mindset / Scenario Questions**

| # | Question | What They’re Checking |
| --- | --- | --- |
| 71 | What will you do if you find a defect just before release? | Judgment & communication |
| 72 | How do you prioritize test cases? | Risk-based thinking |
| 73 | What if a developer disagrees with your bug? | Professional handling |
| 74 | How do you handle incomplete requirements? | QA adaptability |
| 75 | What are the qualities of a good tester? | Attitude & analytical skill |

#### 🔥 Quick Tip for You (2-Year QA Automation Tester in India)

| Area | % Focus in Interview | Tip |
| --- | --- | --- |
| Core Java | 20% | Practice small snippets daily |
| Selenium + TestNG + Framework | 40% | Be ready to explain your own framework |
| Testing Theory | 30% | Revise from this sheet |
| Tools (Jenkins, Git, Jira) | 10% | Mention real usage examples |

---

## 5. API & Database Testing

### Q: What questions should I prepare for regarding Postman, Rest Assured, and MySQL database testing?

**Answer:**

Excellent — that’s exactly what most **modern QA automation interviews (especially in India)** now focus on beyond Selenium:

💥 **API testing (Postman + RestAssured)** +  
💥 **Database validation (MySQL / JDBC)**

So here’s a **dedicated list** — separated and crystal clear — of what you can expect **for 2-year QA automation engineers** working with Java, Selenium, Postman, and DB validation.

#### 🧠 API Testing & Database Validation Interview Questions (Postman + RestAssured + MySQL)

_(Focused for 2-year Indian QA Automation roles)_

**🧩 1️⃣ POSTMAN INTERVIEW QUESTIONS (Manual API Testing)**

| # | Question | Short, Interview-Ready Answer |
| --- | --- | --- |
| 1 | What is Postman? | A GUI tool for testing REST APIs by sending requests and viewing responses. |
| 2 | What is an API? | Interface that allows two systems to communicate via requests/responses. |
| 3 | What are the HTTP methods used in APIs? | GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS. |
| 4 | Difference between GET and POST? | GET retrieves data; POST sends new data to the server. |
| 5 | What is the structure of an HTTP request? | Method, URL, Headers, Body, and Params. |
| 6 | What is the structure of an HTTP response? | Status code, Headers, and Body. |
| 7 | What are Headers in Postman? | Meta information like `Content-Type`, `Authorization`. |
| 8 | What is the use of Params in Postman? | Send query/path parameters (like `?id=1`). |
| 9 | How do you send authentication in Postman? | Through Basic Auth, Bearer Token, OAuth 2.0, or API Key tabs. |
| 10 | What are Collections in Postman? | Groups of related API requests. |
| 11 | What is a Postman Environment? | Set of key-value pairs used to store environment-specific variables. |
| 12 | What are Pre-request Scripts? | JS code that runs before sending the request. |
| 13 | What are Tests in Postman? | JS snippets run after receiving the response for validation. |
| 14 | How do you write a basic assertion in Postman? | `pm.test("Status code is 200", function() { pm.response.to.have.status(200); });` |
| 15 | What is a Collection Runner? | Runs all requests in a collection sequentially with optional data file. |
| 16 | How do you use variables in Postman? | Use `{{variableName}}` syntax. |
| 17 | How can you share Postman collections? | Export as JSON or via Postman workspace link. |
| 18 | How do you run data-driven tests in Postman? | Use Collection Runner with a CSV/JSON file. |
| 19 | How do you generate code snippets in Postman? | “Code” option → select language (like Java, Python). |
| 20 | How do you export Postman results? | Use Newman (CLI) to run and export reports. |

**💻 2️⃣ REST ASSURED (Java API Automation Framework)**

| # | Question | Short, Interview-Ready Answer |
| --- | --- | --- |
| 21 | What is RestAssured? | A Java library for testing REST APIs using simple, readable syntax. |
| 22 | What Maven dependency do you need? | `<dependency><groupId>io.rest-assured</groupId><artifactId>rest-assured</artifactId></dependency>` |
| 23 | How to send a simple GET request? | `given().when().get("url").then().statusCode(200);` |
| 24 | How to send POST with a JSON body? | `given().body(json).post("url");` |
| 25 | How to validate response status? | `.then().statusCode(200);` |
| 26 | How to validate response body field? | `.body("key", equalTo("value"));` |
| 27 | How to extract data from response? | `response.jsonPath().getString("key");` |
| 28 | How to send query parameters? | `.queryParam("id", "1")` |
| 29 | How to send path parameters? | `.pathParam("id", 2)` |
| 30 | How to send headers? | `.header("Content-Type", "application/json")` |
| 31 | How to handle authentication in RestAssured? | `.auth().basic("user", "pass")` or `.auth().oauth2("token")` |
| 32 | What is given/when/then syntax? | BDD style for readability. |
| 33 | How to validate JSON schema? | Use `matchesJsonSchemaInClasspath("schema.json")` |
| 34 | How to log request and response? | `.log().all()` |
| 35 | How to handle complex nested JSON? | Use `JsonPath` or `JSONObject`. |
| 36 | How to use RequestSpecification and ResponseSpecification? | Define reusable request/response patterns. |
| 37 | How do you run RestAssured tests with TestNG? | Annotate with `@Test` and integrate RestAssured code. |
| 38 | How do you parameterize RestAssured tests? | Use TestNG DataProvider or property files. |
| 39 | How do you send multipart/form-data? | `.multiPart("file", new File("path"))` |
| 40 | How do you generate reports in API automation? | Integrate with Allure or ExtentReports. |

**🧠 3️⃣ DATABASE TESTING (MySQL + JDBC)**

| # | Question | Short, Interview-Ready Answer |
| --- | --- | --- |
| 41 | What is Database Testing? | Verifying backend data for correctness, integrity, and consistency. |
| 42 | What are types of DB testing? | Data validation, schema validation, stored procedure testing. |
| 43 | What tool/tech do you use for DB testing? | MySQL + JDBC + SQL queries. |
| 44 | What is JDBC? | Java Database Connectivity — API to connect and query databases. |
| 45 | How do you connect to a MySQL DB using Java? | `DriverManager.getConnection("jdbc:mysql://localhost:3306/db", "user", "pass");` |
| 46 | What is a JDBC driver? | Software that enables Java to interact with databases. |
| 47 | What is a ResultSet? | Object representing DB query result. |
| 48 | How do you execute a SQL query in Java? | `Statement stmt = conn.createStatement(); stmt.executeQuery("SELECT * FROM table");` |
| 49 | How do you validate DB results in automation? | Compare DB values with UI/API output. |
| 50 | How do you handle DB connection closing? | `conn.close()` in finally block. |
| 51 | What are common SQL commands you use? | `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `JOIN`, `WHERE`. |
| 52 | How do you check duplicate records? | `SELECT col, COUNT(*) FROM table GROUP BY col HAVING COUNT(*) > 1;` |
| 53 | What is a Primary Key? | Unique identifier for table rows. |
| 54 | What is a Foreign Key? | References key in another table. |
| 55 | What is a JOIN? | Combines rows from multiple tables. |
| 56 | Difference between INNER JOIN and LEFT JOIN? | INNER = common rows, LEFT = all left + matched right. |
| 57 | How do you handle DB data setup before tests? | Run SQL scripts in `@BeforeTest`. |
| 58 | How do you integrate DB tests with RestAssured? | Use DB validation after API response check. |
| 59 | How do you fetch single value from DB? | `resultSet.getString("column_name")` |
| 60 | What’s normalization? | Process of organizing data to reduce redundancy. |

**⚙️ 4️⃣ SCENARIO-BASED QUESTIONS (Real-World QA Automation)**

| # | Question | Expected Approach |
| --- | --- | --- |
| 61 | How do you validate if data inserted via API appears in DB? | Call POST API → Get ID → Run SELECT query in DB → Assert values match. |
| 62 | How do you test if DB constraints are working? | Try inserting invalid data → Expect error code. |
| 63 | How do you test pagination in API? | Validate total count, page limits, next/prev links. |
| 64 | How do you test response time? | `response.time()` in RestAssured → assert within limit. |
| 65 | How do you test file upload API? | Use Postman/RestAssured `multipart/form-data`. |
| 66 | How do you test authentication API? | Invalid token → expect 401; valid token → expect 200. |
| 67 | How do you chain API requests? | Use one API’s output (like token or ID) as input to another. |
| 68 | How do you verify data consistency between UI and API? | Compare UI field and API JSON field values. |
| 69 | How do you store credentials in automation securely? | Environment variables or encrypted config files. |
| 70 | How do you manage multiple environments (QA, UAT, Prod)? | Externalize base URLs in config or Jenkins parameters. |

**🧩 Bonus: Common SQL Queries to Know for QA**

| Type | Example |
| --- | --- |
| Count rows | `SELECT COUNT(*) FROM users;` |
| Get recent record | `SELECT * FROM orders ORDER BY created_at DESC LIMIT 1;` |
| Find null values | `SELECT * FROM table WHERE column IS NULL;` |
| Filter by pattern | `SELECT * FROM users WHERE email LIKE '%gmail.com';` |
| Join tables | `SELECT u.name, o.amount FROM users u JOIN orders o ON u.id = o.user_id;` |
| Delete test data | `DELETE FROM orders WHERE id=123;` |

---

## 6. Functional Interfaces

### Q: Can you explain the functional interfaces Predicate, Consumer, Function, Supplier, and BiFunction with QA examples?

**Answer:**

Perfect 😎 — you’re in full-on mastery mode now.  
Let’s continue with the same **crisp, structured, QA-tester-friendly format**.  
This one’s the **ultimate cheat sheet** for:

#### ⚡ Functional Interfaces in Java (Predicate, Consumer, Function, Supplier, BiFunction)

**🧠 1️⃣ What Is a Functional Interface?**

> A **functional interface** has **exactly one abstract method**.  
> It can have **default** or **static** methods too.

💡 Think: “A Lambda’s home.” — Every lambda needs a functional interface.

**🧩 2️⃣ Common Built-in Functional Interfaces (java.util.function)**

| Interface | Method | Description |
| --- | --- | --- |
| **Predicate<T>** | `boolean test(T t)` | Tests a condition (returns true/false) |
| **Consumer<T>** | `void accept(T t)` | Performs an action (no return) |
| **Function<T,R>** | `R apply(T t)` | Converts T → R (input → output) |
| **Supplier<T>** | `T get()` | Supplies a value (no input) |
| **BiFunction<T,U,R>** | `R apply(T t, U u)` | Takes 2 inputs → 1 output |

**🧠 3️⃣ Why QA Engineers Need These**

Functional interfaces are used:

*   To filter or validate test data (Predicate)
*   To perform actions on each element (Consumer)
*   To transform data types (Function)
*   To generate test data (Supplier)
*   To combine or compare two inputs (BiFunction)

**⚙️ 4️⃣ Predicate<T> — Tests a Condition**

**Used For:** Validation or filtering.

**✅ Example:**

```java
Predicate<String> isLong = s -> s.length() > 5;
System.out.println(isLong.test("India"));     // false
System.out.println(isLong.test("Automation")); // true
```

💡 **In QA:** Filter dropdown values, verify conditions, etc.

**⚙️ 5️⃣ Consumer<T> — Performs Action (No Return)**

**Used For:** Logging, printing, performing actions.

**✅ Example:**

```java
Consumer<String> printUpper = s -> System.out.println(s.toUpperCase());
printUpper.accept("selenium"); // SELENIUM
```

**⚙️ 6️⃣ Function<T, R> — Input → Output Transformer**

**Used For:** Converting data from one form to another.

**✅ Example:**

```java
Function<String, Integer> length = s -> s.length();
System.out.println(length.apply("Automation")); // 10
```

**⚙️ 7️⃣ Supplier<T> — Supplies Data (No Input)**

**Used For:** Providing data (random, default, or test data).

**✅ Example:**

```java
Supplier<String> otp = () -> String.valueOf((int)(Math.random() * 10000));
System.out.println(otp.get());
```

**⚙️ 8️⃣ BiFunction<T, U, R> — Two Inputs → One Output**

**Used For:** Combining or comparing two inputs.

**✅ Example:**

```java
BiFunction<Integer, Integer, Integer> add = (a, b) -> a + b;
System.out.println(add.apply(10, 20)); // 30
```

**🧠 1️⃣1️⃣ Common Interview Q&A**

| Question | Short Answer |
| --- | --- |
| What is a functional interface? | Interface with one abstract method |
| What is Predicate used for? | Test a condition and return boolean |
| What is Consumer used for? | Perform an action without returning |
| What is Function used for? | Transform one type to another |
| What is Supplier used for? | Provide data without input |
| Difference between Consumer and Supplier? | Consumer = takes input, Supplier = gives output |
| Difference between Function and BiFunction? | BiFunction takes two inputs |
| How are lambdas related? | Lambdas implement functional interfaces |
| Where are these in Selenium? | Filtering lists, mapping data, logging actions |

---

## 7. Java Collections Framework

### Q: I need a guide for Java Collections, specifically focusing on List, Set, Map, and Queue, with examples relevant to QA automation.

**Answer:**

Perfect 😎 — I love how consistent and serious you are about this.  
I’ve locked in your **context** (👉 2-year QA Automation Engineer in India, preparing for interviews, wants _zero confusion_, simple logic, fast recall, and real QA use cases).

So here’s your next **gold chapter** in the “QA Automation Master Series” —  
crafted exactly in your preferred style 👇

#### ⚡ Java Collections Framework — QA Automation Edition (2025 Master Notes)

**🧠 1️⃣ What Is the Collections Framework?**

> The **Collections Framework** in Java is a set of **interfaces and classes** used to **store, manipulate, and process groups of objects** efficiently.

💡 Think of it as:  
➡ Arrays = fixed size, primitive  
➡ Collections = dynamic size, object-based, super powerful

**🧩 2️⃣ Why QA Engineers Need Collections**

In Automation Testing (Java + Selenium), collections are used for:

*   Storing **WebElements** (lists, dropdowns, etc.)
*   Holding **test data** (names, emails, expected outputs)
*   Comparing **UI vs API data**
*   Reading and validating **Excel/DB results**

💡 If you can master Lists, Sets, Maps → you already cover 90% of data handling in automation.

**🧠 3️⃣ Core Interfaces (Root to Leaf)**

| Interface | Description | Common Implementations |
| --- | --- | --- |
| **Collection** | Root of all collections | List, Set, Queue |
| **List** | Ordered, allows duplicates | ArrayList, LinkedList |
| **Set** | Unordered, no duplicates | HashSet, LinkedHashSet, TreeSet |
| **Queue** | FIFO structure | PriorityQueue, LinkedList |
| **Map** | Key-value pairs | HashMap, LinkedHashMap, TreeMap |

**⚙️ 4️⃣ List Interface — Ordered & Duplicates Allowed**

**✅ Key Features:**

*   Maintains **insertion order**
*   Allows **duplicate elements**
*   Access via **index**

**Example:**

```java
List<String> names = new ArrayList<>();
names.add("Selenium");
names.add("Java");
names.add("Selenium");
System.out.println(names); // [Selenium, Java, Selenium]
```

**Common Methods:**

| Method | Description |
| --- | --- |
| `add()` | Add element |
| `get()` | Retrieve by index |
| `remove()` | Remove element |
| `size()` | Count elements |
| `contains()` | Check presence |
| `clear()` | Empty list |