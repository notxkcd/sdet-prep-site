---
title: "Expleo-6"
date: 2026-01-30
draft: false
---

---

## Original Questions

Expleo level 2:
---------------
Explain your resume or cv
Take a Google page and take the xpath for search box 
Go to the amazon.in and search mobiles take the first mobile option take the xpath of it
And take that page how many mobiles count on that page 
That page highlight the mobile colour how to take that colour what method you use
Explain the wait concept in the selenium
Types of explicit wait write the syntax for that
Write the duplicate removal program 
Types of xpath
Which locator is effective
Which xpath will be more efficient

---

## Answers (No-BS Java QA / SDET Explanations)

### Explain your resume or cv
Standard "walk me through your resume" question. Be prepared to highlight your most relevant experience, skills, and accomplishments that align with the job description. Focus on impact and results.

### Take a Google page and take the xpath for search box
(Requires inspecting Google.com).
The search box on Google's homepage usually has a `name="q"`.
XPath: `//textarea[@name='q']` or `//input[@name='q']` (depending on the element type).
CSS Selector: `textarea[name='q']` or `input[name='q']`.

### Go to the amazon.in and search mobiles take the first mobile option take the xpath of it
(Requires inspecting Amazon.in after searching for "mobiles").
Assuming the first mobile option is within a search result container and has a link to its product page.

Conceptual XPath: `(//div[@data-component-type='s-search-result'])[1]//a`
This means:
1.  `//div[@data-component-type='s-search-result']`: Find all `div` elements that are search result containers.
2.  `[1]`: Select the first one.
3.  `//a`: Find any `<a>` (link) descendant within that first result.

### And take that page how many mobiles count on that page
This means counting the number of mobile product listings on a search results page.
You identify a common locator for each product listing container and use `findElements()`.
```java
List<WebElement> mobileListings = driver.findElements(By.xpath("//div[@data-component-type='s-search-result']"));
int count = mobileListings.size();
System.out.println("Number of mobile listings: " + count);
```

### That page highlight the mobile colour how to take that colour what method you use
You use the `getCssValue()` method of a `WebElement`.
1.  Locate the element that has the highlight color (e.g., a border, background, or text color).
2.  Call `element.getCssValue("property-name")`.
    -   To get background color: `element.getCssValue("background-color")`
    -   To get border color: `element.getCssValue("border-color")`
    -   To get text color: `element.getCssValue("color")`
The returned value will usually be in RGBA format (e.g., "rgba(255, 0, 0, 1)").

### Explain the wait concept in the selenium
Waits are essential for synchronizing the test script with the web application's state. They prevent `NoSuchElementException` or `StaleElementReferenceException` due to asynchronous loading.
-   **Implicit Wait:** Global setting, bad practice.
-   **Explicit Wait (`WebDriverWait`):** Recommended. Waits for a *specific condition* to be met.
-   **Fluent Wait:** More configurable explicit wait.

### Types of explicit wait write the syntax for that
Explicit waits use `WebDriverWait` combined with `ExpectedConditions`.
-   **`ExpectedConditions.visibilityOfElementLocated(By locator)`:** Waits for an element to be visible in the DOM.
-   **`ExpectedConditions.elementToBeClickable(By locator)`:** Waits for an element to be visible and enabled so it can be clicked.
-   **`ExpectedConditions.alertIsPresent()`:** Waits for a JavaScript alert to appear.
-   **`ExpectedConditions.titleContains(String title)`:** Waits for the page title to contain specific text.

**Syntax:**
```java
WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
WebElement element = wait.until(ExpectedConditions.elementToBeClickable(By.id("myButton")));
element.click();
```

### Write the duplicate removal program
To remove duplicates from an array of integers.

```java
import java.util.Arrays;
import java.util.LinkedHashSet;
import java.util.Set;

public class DuplicateRemover {
    public static int[] removeDuplicates(int[] arr) {
        // Using Java 8 Streams is the most concise
        return Arrays.stream(arr).distinct().toArray();
        
        /* // Using a Set manually (preserves order with LinkedHashSet)
        Set<Integer> uniqueElements = new LinkedHashSet<>();
        for (int i : arr) {
            uniqueElements.add(i);
        }
        return uniqueElements.stream().mapToInt(Integer::intValue).toArray();
        */
    }
}
```

### Types of xpath
-   **Absolute XPath:** Starts from the root `/html`. Very brittle.
-   **Relative XPath:** Starts with `//`. Robust and flexible.

### Which locator is effective
The effectiveness depends on the context and stability of the application.
1.  **`id`:** Most effective if unique and stable. Fastest.
2.  **`cssSelector`:** Highly effective, especially for complex selections, and generally faster than XPath.
3.  **`xpath`:** Most powerful for complex traversals (e.g., by text, axes), but can be slower and sometimes less readable.

### Which xpath will be more efficient
Generally, simple, direct XPaths are efficient.
-   **More efficient:** `//input[@id='username']` or `//button[@name='login']`.
-   **Less efficient:** XPaths that scan the entire DOM extensively, like `//*[contains(text(), 'some text')]` (unless narrowed down), or very long absolute XPaths.
-   **Prioritize:** Start your XPath from a unique parent if possible.
In practice, `cssSelector` is often more performant than XPath when both can achieve the same result.
