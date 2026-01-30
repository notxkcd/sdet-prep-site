---
title: "QualityKiosk_2025-09"
date: 2026-01-30
draft: false
---

---

## Original Questions

- QualityKiosk -Kochin (28/09/2025)
---------------------------------
1.	Introduce your self
2.	Do you work in cucumber framework? Please explain your framework?
3.	Where you execute your test in Cucumber?
4.	What are the things you have in your runner Class ?
5.	How to do fetch data from excel, explain with code?
6.	What is Scenario outline in Cucumber?
7.	Reverse the string using for loop?
8.	Have you work in Agile and explain the process?
9.	What is bug life cycle?
10.	Did you use git in your project and what is  git conflict?
11.	How to you resolve git conflict?
12.	What is Assert? Can we able to write automation without Assert?
13.	Explain difference between Implicity and Explicity waits?

---

## Answers (No-BS Java QA / SDET Explanations)

### 1. Introduce your self
Standard opener. Keep it concise, professional, and focus on your relevant experience (automation skills, tech stack, achievements).

### 2. Do you work in cucumber framework? Please explain your framework?
"Yes, I have extensive experience working with the Cucumber framework. Our framework is a Java-based BDD (Behavior-Driven Development) framework.
-   **Architecture:** It follows the Page Object Model (POM) for UI interaction.
-   **Components:** We write high-level business scenarios in Gherkin in `.feature` files. These scenarios are linked to our Java Step Definitions, which contain the actual Selenium WebDriver automation code.
-   **Test Data:** We use Cucumber's `Scenario Outline` and `Data Tables` for data-driven testing.
-   **CI/CD:** The framework is built with Maven and integrated into our Jenkins CI/CD pipelines, allowing us to run automated tests continuously."

### 3. Where you execute your test in Cucumber?
-   **Locally:** During development and debugging from my IDE (e.g., IntelliJ, Eclipse) by running the Cucumber Runner class.
-   **CI/CD Pipeline:** The primary execution environment is our **Jenkins pipeline**. Tests are triggered automatically on every code push or on a schedule (e.g., nightly builds) against dedicated QA or Staging environments.

### 4. What are the things you have in your runner Class ?
A Cucumber Runner class is a Java class that serves as the entry point for executing Cucumber tests.
-   **`@RunWith(Cucumber.class)`:** Annotation to tell JUnit to run this class with Cucumber.
-   **`@CucumberOptions`:** Annotation to configure Cucumber's behavior:
    -   `features`: Path to the `.feature` files.
    -   `glue`: Path to the step definition packages (the "glue code").
    -   `plugin`: Specifies reporting formats (e.g., HTML, JSON, Pretty).
    -   `tags`: Filters which scenarios to run (e.g., `@smoke`, `not @wip`).
    -   `dryRun`: Checks for missing step definitions without actual execution.
    -   `monochrome`: Makes console output more readable.

### 5. How to do fetch data from excel, explain with code?
You need the **Apache POI** library.
1.  **Dependency:** Add Apache POI (`poi-ooxml`) to `pom.xml`.
2.  **Utility Method:** Create a method that:
    -   Takes file path and sheet name.
    -   Uses `FileInputStream` to open the Excel file.
    -   Creates an `XSSFWorkbook` (for .xlsx) or `HSSFWorkbook` (for .xls).
    -   Gets the desired sheet.
    -   Iterates through rows and cells to read data.
3.  **Integration with Cucumber:**
    -   Create a custom step definition that calls this utility.
    -   Or, wrap it in a `@DataProvider` if you're using TestNG as the Cucumber runner.

```java
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class ExcelReader {
    public List<List<String>> readData(String filePath, String sheetName) throws IOException {
        List<List<String>> data = new ArrayList<>();
        FileInputStream fis = new FileInputStream(filePath);
        Workbook workbook = new XSSFWorkbook(fis); // For .xlsx files
        Sheet sheet = workbook.getSheet(sheetName);

        for (Row row : sheet) {
            List<String> rowData = new ArrayList<>();
            for (Cell cell : row) {
                rowData.add(cell.toString()); // Get cell value as string
            }
            data.add(rowData);
        }
        workbook.close();
        fis.close();
        return data;
    }
}
```

### 6. What is Scenario outline in Cucumber?
A `Scenario Outline` is Cucumber's way to achieve **data-driven testing**. It defines a template for a scenario that is run multiple times with different input values. It uses `<placeholders>` in its steps, and an `Examples` table provides the data for these placeholders. Each row in the `Examples` table executes the scenario once.

### 7. Reverse the string using for loop?
While `StringBuilder.reverse()` is preferred, this demonstrates basic loop manipulation.

```java
public class StringReverser {
    public static String reverseStringWithLoop(String str) {
        if (str == null || str.isEmpty()) {
            return str;
        }
        char[] charArray = str.toCharArray();
        StringBuilder reversed = new StringBuilder();
        for (int i = charArray.length - 1; i >= 0; i--) {
            reversed.append(charArray[i]);
        }
        return reversed.toString();
    }
}
```

### 8. Have you work in Agile and explain the process?
"Yes, I have several years of experience working in an **Agile (Scrum)** environment. We work in two-week sprints. The process involves daily stand-ups, sprint planning, backlog refinement, sprint reviews, and retrospectives. As QA, I'm involved from the beginning, helping refine stories, writing tests, automating, and providing continuous feedback."

### 9. What is bug life cycle?
The journey of a defect from discovery to resolution: New -> Open/Assigned -> Fixed -> Ready for QA -> Closed (or Reopened).

### 10. Did you use git in your project and what is git conflict?
"Yes, we use **Git** for version control. A **Git conflict** occurs when two or more developers make conflicting changes to the same lines in the same file, and Git cannot automatically merge those changes. It flags the conflict, requiring manual intervention."

### 11. How to you resolve git conflict?
1.  **Pull latest changes:** First, ensure my local branch is up-to-date with the remote: `git pull`.
2.  **Attempt merge:** `git merge <other_branch>`. Git will identify the conflicts.
3.  **Edit conflicted files:** Open the files marked as conflicted. Git inserts special markers (`<<<<<<<`, `=======`, `>>>>>>>`) showing the conflicting sections. I manually edit the file to combine the correct changes, removing the markers.
4.  **Stage resolved files:** `git add <resolved_file>`.
5.  **Commit:** `git commit -m "Resolved merge conflict"`.

### 12. What is Assert? Can we able to write automation without Assert?
-   **Assert:** A statement that checks if a condition is true. If the condition is false, the assertion fails, and the test is typically terminated and marked as failed. Used to verify expected outcomes.
-   **Without Assert:** You *could* write automation without explicit asserts, but it would be pointless. The tests would run, but you would have no way of knowing if the application is behaving correctly or if any bugs were found. Automation without assertions is just exercising the application, not testing it.

### 13. Explain difference between Implicity and Explicity waits?
-   **Implicit Wait (Bad):** A global setting for the WebDriver that makes it poll the DOM for a specified time when `findElement` cannot immediately find an element. It's imprecise and can hide real timing issues.
-   **Explicit Wait (Good):** (`WebDriverWait` with `ExpectedConditions`) Waits for a *specific condition* to be true for a maximum amount of time. It's targeted, reliable, and makes tests more stable.
