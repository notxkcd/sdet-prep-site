---
title: "Capgemini-7"
date: 2026-01-30
draft: false
---

---

## Original Questions (UNTOUCHED)

Capgemini
---------
Programs - character occurrence
1. Windows handling 
2. Http methods
3. Xpath
4. How will you validate the given xpath is correct or not
5. Alert 
6. How will you handle status codes
7. Program - Anagram, palindrome 
8. Duplicate removal program
9. Staleelement exception
10. Roles and responsibilities
11.how will you validate the xpath

---

## Answers (No-BS Java QA / SDET Explanations)

### Programs - character occurrence
This means counting the frequency of each character in a string.

```java
import java.util.HashMap;
import java.util.Map;

public class CharOccurrence {
    public static void countCharacterOccurrence(String str) {
        if (str == null || str.isEmpty()) {
            System.out.println("String is empty or null.");
            return;
        }

        Map<Character, Integer> charCounts = new HashMap<>();
        for (char c : str.toCharArray()) {
            charCounts.put(c, charCounts.getOrDefault(c, 0) + 1);
        }

        System.out.println("Character Occurrences:");
        charCounts.forEach((character, count) -> 
            System.out.println("'" + character + "': " + count)
        );
    }

    public static void main(String[] args) {
        countCharacterOccurrence("Capgemini");
    }
}
```

### 1. Windows handling
This refers to handling multiple browser windows or tabs. You use `driver.getWindowHandle()` (current window ID), `driver.getWindowHandles()` (all window IDs), and `driver.switchTo().window(handle)` to switch focus.

### 2. Http methods
The verbs used in HTTP requests: `GET` (retrieve), `POST` (create), `PUT` (replace/update), `PATCH` (partial update), `DELETE` (remove).

### 3. Xpath
A query language for selecting nodes in an XML/HTML document. It's a key locator strategy in Selenium, allowing flexible element identification based on attributes, text, and DOM relationships.

### 4. How will you validate the given xpath is correct or not
1.  **Browser Developer Tools:** The easiest way. Open the browser's DevTools (F12), go to the Elements tab, and use `Ctrl+F` (or `Cmd+F`) to open the search bar. Paste your XPath there. It will show you if the XPath matches any elements and highlight them.
2.  **Selenium `findElements()`:** In your code, `driver.findElements(By.xpath(yourXpath))`. If the returned list is empty (`.isEmpty()`), the XPath is incorrect (or the element is not present). This won't throw an exception, so it's a safe check.

### 5. Alert
This refers to handling browser native JavaScript alerts. You switch to the alert using `driver.switchTo().alert()` and then interact with it using methods like `accept()`, `dismiss()`, or `getText()`.

### 6. How will you handle status codes
In API automation (using REST-assured), you validate status codes in the `.then()` part of your request chain.
Example: `response.then().statusCode(200);` or `response.then().statusCode(equalTo(200));` (using Hamcrest matchers).

### 7. Program - Anagram, palindrome
-   **Anagram:** Two strings are anagrams if they contain the same characters in a different order (e.g., "listen" and "silent"). Check by sorting character arrays and comparing.
    ```java
    import java.util.Arrays;
    public boolean isAnagram(String s1, String s2) {
        char[] arr1 = s1.toCharArray(); Arrays.sort(arr1);
        char[] arr2 = s2.toCharArray(); Arrays.sort(arr2);
        return Arrays.equals(arr1, arr2);
    }
    ```
-   **Palindrome:** A string that reads the same forwards and backward (e.g., "madam", "racecar"). Check by reversing the string and comparing.
    ```java
    public boolean isPalindrome(String str) {
        String reversed = new StringBuilder(str).reverse().toString();
        return str.equalsIgnoreCase(reversed);
    }
    ```

### 8. Duplicate removal program
To remove duplicates from an array or list, convert it to a `Set` (which by definition does not allow duplicates) and then convert it back to a list/array if needed.

```java
import java.util.Arrays;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

public class DuplicateRemover {
    public static <T> List<T> removeDuplicates(List<T> list) {
        return list.stream().distinct().collect(Collectors.toList());
    }

    public static int[] removeDuplicates(int[] array) {
        return Arrays.stream(array).distinct().toArray();
    }
}
```

### 9. Staleelement exception
`StaleElementReferenceException`. Occurs when a `WebElement` reference is no longer valid because the underlying DOM element has changed or been removed. The solution is to re-find the element before interaction.

### 10. Roles and responsibilities
Standard. Describe your day-to-day as an SDET/QA Automation Engineer, including framework development, test scripting, CI/CD integration, bug reporting, and team collaboration.

### 11. how will you validate the xpath
(Duplicate of question 4). Use browser DevTools or `driver.findElements(By.xpath(yourXpath)).isEmpty()`.
