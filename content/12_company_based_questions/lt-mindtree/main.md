---
title: "Lt_Mindtree"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

Lt Mindtree level 1 interview questions :
----------------------------------------

1)Write a code for post requesting for sending body and header
2)Write a code to get  request for a validating response using the json path
3)Write a code for validating response using extract 
4)File upload in Api
5)what is glue 
6) Background 
7)datatable in cucumber 
8)seprate the String and Integer
9) selenium 4th version of above below 
10) Do you have teamlead experience 
11)exceptions in java and selenium
12) what exceptions do you face in your project
13)what is stale element reference exception

---

## Answers (No-BS Java QA / SDET Explanations)

### 1)Write a code for post requesting for sending body and header
Using REST-assured.

```java
import static io.restassured.RestAssured.*;
import io.restassured.http.ContentType;
import org.json.JSONObject; // From org.json library

public class ApiPostRequest {
    public void createResource() {
        // Request Body (JSON)
        JSONObject requestBody = new JSONObject();
        requestBody.put("name", "John Doe");
        requestBody.put("job", "QA Engineer");

        // Perform POST request
        given()
            .baseUri("https://reqres.in/api") // Example API
            .contentType(ContentType.JSON) // Set Content-Type header
            .body(requestBody.toString())  // Set request body
        .when()
            .post("/users")
        .then()
            .statusCode(201) // Expect 201 Created
            .log().all(); // Log request and response for debugging
    }
}
```

### 2)Write a code to get request for a validating response using the json path
Using REST-assured and Hamcrest matchers.

```java
import static io.restassured.RestAssured.*;
import static org.hamcrest.Matchers.*;

public class ApiGetRequestValidation {
    public void getUserDetails() {
        given()
            .baseUri("https://reqres.in/api")
        .when()
            .get("/users/2") // Get user with ID 2
        .then()
            .statusCode(200)
            .body("data.id", equalTo(2)) // Validate specific field using JSONPath
            .body("data.email", equalTo("janet.weaver@reqres.in"))
            .body("data.first_name", equalTo("Janet"))
            .body("data.last_name", equalTo("Weaver"))
            .body("support.url", containsString("reqres.in")); // Validate string content
    }
}
```

### 3)Write a code for validating response using extract
`extract()` is used to get a value from the response body for further processing or for using it in a subsequent API call (chaining).

```java
import static io.restassured.RestAssured.*;
import io.restassured.response.Response;

public class ApiExtractResponse {
    public String createUserAndExtractId() {
        JSONObject requestBody = new JSONObject();
        requestBody.put("name", "Test User");
        requestBody.put("job", "Tester");

        Response response = given()
            .baseUri("https://reqres.in/api")
            .contentType(ContentType.JSON)
            .body(requestBody.toString())
        .when()
            .post("/users");
        
        response.then().statusCode(201); // Assert creation

        // Extract the 'id' from the response
        String userId = response.then().extract().path("id");
        System.out.println("Created User ID: " + userId);
        return userId;
    }
}
```

### 4)File upload in Api
For file uploads, you typically use `multiPart()` in REST-assured.

```java
import static io.restassured.RestAssured.*;
import java.io.File;

public class ApiFileUpload {
    public void uploadFile() {
        File fileToUpload = new File("src/test/resources/my_document.pdf");
        
        given()
            .baseUri("https://api.example.com") // Replace with actual API endpoint
            .multiPart("file", fileToUpload) // "file" is the parameter name expected by the server
            // Optionally, add other form data
            .formParam("description", "My test document") 
        .when()
            .post("/upload")
        .then()
            .statusCode(200) // Expect success status
            .log().all();
    }
}
```

### 5)what is glue
In Cucumber, `glue` refers to the path (package name) where Cucumber should look for **step definition files** (Java classes containing `@Given`, `@When`, `@Then` annotations) and **hooks** (`@Before`, `@After`). It connects your Gherkin feature files to the executable Java code.

### 6) Background
In a Cucumber `.feature` file, the `Background` keyword defines a set of `Given` steps that are executed **before every scenario** in that feature file. It's used to set up a common state or precondition for all scenarios, reducing repetition.

### 7)datatable in cucumber
A `DataTable` is used in Cucumber to pass a collection of data in a tabular format from a Gherkin step to its step definition. This allows for passing complex data structures (like a list of users or product details) without having to repeat them in individual step parameters.

### 8)seprate the String and Integer
This typically means separating letters from numbers in a given string.

```java
public class StringIntegerSeparator {
    public static void separate(String input) {
        StringBuilder letters = new StringBuilder();
        StringBuilder numbers = new StringBuilder();
        for (char c : input.toCharArray()) {
            if (Character.isLetter(c)) {
                letters.append(c);
            } else if (Character.isDigit(c)) {
                numbers.append(c);
            }
        }
        System.out.println("Letters: " + letters);
        System.out.println("Numbers: " + numbers);
    }
}
```

### 9) selenium 4th version of above below
This refers to **Selenium 4's Relative Locators** (also known as Friendly Locators).
They allow you to find an element based on its visual relationship to other known elements on the page.
-   `with(By.tagName("input")).above(By.id("password"))`
-   `with(By.tagName("button")).toLeftOf(By.id("cancelButton"))`
-   `with(By.cssSelector("div.product")).below(By.id("productTitle"))`

### 10) Do you have teamlead experience
"While my primary role has been an individual contributor as an SDET, I have taken on **mentoring responsibilities** for junior team members, provided **technical guidance** on automation best practices, and **led initiatives** for framework enhancements. I'm eager to grow into a formal team lead role in the future."

### 11)exceptions in java and selenium
-   **Java Exceptions:** `NullPointerException`, `IOException`, `IllegalArgumentException`.
-   **Selenium Exceptions:** `NoSuchElementException`, `StaleElementReferenceException`, `TimeoutException`, `ElementNotInteractableException`, `InvalidSelectorException`.

### 12) what exceptions do you face in your project
(Likely a follow-up to the previous question).
"In our project, the most common Selenium exceptions I've faced are `NoSuchElementException` (due to timing or incorrect locators) and `StaleElementReferenceException` (due to dynamic UI updates). I also occasionally encounter `TimeoutException` if a new feature takes longer to load than expected or if the environment is slow."

### 13)what is stale element reference exception
`StaleElementReferenceException` occurs when a `WebElement` reference you previously located becomes "stale" because the element is no longer attached to the DOM (e.g., due to an AJAX update or page navigation). The solution is to re-find the element just before you interact with it.
