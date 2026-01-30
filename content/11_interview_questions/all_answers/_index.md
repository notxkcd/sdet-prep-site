---
title: "🧠 QA Automation Interview Answers"
date: 2026-01-30
draft: false
---

---

## 📘 Indium Interview Questions

1. **Self Introduction**
   I’m a QA Automation Engineer skilled in Java, Selenium, and API testing. I love automating manual flows and improving test efficiency.

2. **Project Introduction**
   Automated regression and smoke tests for web and API using Selenium + RestAssured. Integrated with Jenkins for CI.

3. **Day-to-Day Activities**
   Review test cases → Automate new scenarios → Run regression → Debug failed tests → Update reports.

4. **Agile Methodology**
   Work in sprints, attend daily standups, plan & review, deliver automation per sprint stories.

5. **Flipkart XPath for Top/Best Deals**

   ```xpath
   //div[contains(text(),'Top Deals') or contains(text(),'Best Deals')]
   ```

6. **Extract 'name' from cURL response (API test)**

   ```java
   Response res = given().get(url);
   String name = res.jsonPath().getString("name");
   ```

7. **Remove duplicates & find 2nd largest digit**

   ```java
   String a = "9645788215";
   int second = a.chars().distinct().map(c->c-'0').sorted().toArray()[8];
   ```

8. **Git Conflict Scenario**
   Pull latest → Resolve conflicts → Rebuild → Push merged code → Then PR.

9. **Run Tests in Jenkins**
   Create a Maven job → Set repo URL → Run `mvn clean test` in Build section.

10. **Roles & Responsibilities**
    Automate regression, maintain framework, log bugs, integrate with CI/CD, support manual QA.

11. **High-Priority Bug on Release Day**
    Report immediately → Reproduce → Log JIRA → Inform lead → Retest fix quickly.

12. **Automation Challenges**
    Dynamic XPaths, sync issues, flaky tests, unstable environments, and API data dependencies.

13. **Smoke vs Sanity**

    * **Smoke:** Check main flow after build.
    * **Sanity:** Verify bug fixes or small change areas.

---

## ⚙️ Hexaware Interview Questions

### Round 1

1. **Introduction**
   QA Engineer with Java, Selenium, and API testing hands-on. Focused on reliable automation.

2. **Maven Build Tool**
   Manages project dependencies, builds via `pom.xml`, and runs tests using `mvn test`.

3. **5 Array Methods**
   `sort()`, `copyOf()`, `equals()`, `fill()`, `toString()`.

4. **Method Overloading**
   Same name, different parameters or types. Done at compile-time.

5. **Types of Casting**

   * Primitive: Widening/Narrowing
   * Object: Upcasting/Downcasting

6. **Right-click in Selenium**

   ```java
   new Actions(driver).contextClick(element).perform();
   ```

7. **Implicit Wait Syntax**

   ```java
   driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
   ```

8. **Scroll using JS Executor**

   ```java
   ((JavascriptExecutor)driver).executeScript("window.scrollBy(0,500)");
   ```

9. **Open Incognito Browser**

   ```java
   ChromeOptions opt = new ChromeOptions();
   opt.addArguments("--incognito");
   new ChromeDriver(opt);
   ```

10. **First Repeated Number in Array**

```java
int[] a={1,2,3,4,5,2,3,4};
Set<Integer> s=new HashSet<>();
for(int n:a) if(!s.add(n)){System.out.println(n);break;}
```

11. **Critical Challenges**
    Element loading issues, test data setup, flaky CI builds, API auth errors.

12. **Project Explanation**
    Automated e-commerce regression suite with Selenium + RestAssured + Jenkins integration.

---

### Round 2

1. **Launch Browser & Open deals.com**

   ```java
   WebDriver d=new ChromeDriver();
   d.get("https://deals.com");
   ```

2. **Click Links Containing "todaydeals"**

   ```java
   for(WebElement e:d.findElements(By.tagName("a")))
       if(e.getText().contains("todaydeals")) e.click();
   ```

3. **Optimize with Waits**

   ```java
   new WebDriverWait(d, Duration.ofSeconds(10))
       .until(ExpectedConditions.elementToBeClickable(By.linkText("todaydeals")));
   ```

4. **Day-to-Day Activities**
   Script writing, running suites, fixing failed cases, logging bugs, and updating CI jobs.

5. **Framework Challenges**
   Handling dynamic waits, test data reuse, parallel execution, and flaky locators.

6. **Roles & Responsibilities**
   Build automation, support releases, maintain CI pipeline, report defects.

7. **Git Workflow**

   ```bash
   git clone → git branch → git add → git commit → git push → PR → merge
   ```

8. **Jenkins Configuration**
   Create job → Connect Git repo → Add Maven command → Schedule or trigger via commit.

9. **Framework Explanation**
   Hybrid (Data + Keyword + POM) with TestNG, Extent Reports, and Maven build.

---

## 💡 Comcast Interview Questions

1. **API Testing Tools**
   Postman, RestAssured, Newman, JMeter.

2. **Validate API Response**
   Check status code, headers, response time, and JSON fields via assertions.

3. **Automation Frameworks**
   Hybrid, BDD (Cucumber), POM with TestNG and Maven.

4. **Test Authentication Mechanisms**
   Use tokens, OAuth, or Basic Auth headers in API calls.

5. **Validate Database Data**
   Use JDBC to query DB → Compare results with API/UI response.

6. **Run Tests in CI/CD**
   Trigger automation via Jenkins after build → Run tests → Publish reports.

7. **Ensure Test Coverage**
   Map test cases to requirements → Use coverage tools → Track via dashboard.

8. **Handle Dynamic Web Elements**
   Use dynamic XPath/CSS + waits + contains/text() methods.

9. **Functional vs Non-Functional**

   * **Functional:** Feature correctness.
   * **Non-Functional:** Performance, security, usability.

10. **Request Validation in REST APIs**
    Use schema validation and negative tests to verify input correctness.

---
