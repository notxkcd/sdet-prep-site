---
title: "Qapitol_QA-2"
date: 2026-01-30
draft: false
---

---

## Original Questions

Qapitol QA Interview Questions:
-------------------------------
What is chaining in API Testing ?
Can we create an Object for an abstract class?
What is the interface?
What is the path and query param?
Write a program the find count of palindrome strings in the given string and print the highest length palindrome.And also occurrence of each character count in that palindrome strings.

---

## Answers (No-BS Java QA / SDET Explanations)

### What is chaining in API Testing ?
API chaining refers to the process where the output (response) of one API request is used as the input (request) for a subsequent API request. This allows you to test complex workflows or business processes that involve multiple API calls.
-   **Example:**
    1.  Make a `POST` request to `/login` to get an authentication token.
    2.  Use that token in the `Authorization` header of a `GET` request to `/profile` to retrieve user details.
    3.  Use a `userId` from the `/profile` response to make a `GET` request to `/orders/{userId}`.
REST-assured supports this naturally with its fluent API, allowing you to extract values and reuse them.

### Can we create an Object for an abstract class?
No. An abstract class cannot be instantiated directly using the `new` keyword. Its purpose is to be extended by concrete subclasses. You must create an object of a concrete subclass that implements all the abstract methods of the abstract class.

### What is the interface?
An interface in Java is a blueprint of a class. It defines a contract of methods that a class `implements`. Interfaces are used to achieve abstraction, enforce a standard behavior, and support multiple inheritance of type in Java.

### What is the path and query param?
These are two ways to pass data in a URL for HTTP requests.
-   **Path Parameters (Path Params):**
    -   Part of the URL path itself.
    -   Used to identify a specific resource or resource hierarchy.
    -   Example: `GET /users/{userId}/orders/{orderId}` where `userId` and `orderId` are path parameters.
-   **Query Parameters (Query Params):**
    -   Appended to the URL after a `?` symbol, as key-value pairs separated by `&`.
    -   Used for filtering, sorting, pagination, or providing optional parameters.
    -   Example: `GET /products?category=electronics&sort=price&page=2` where `category`, `sort`, and `page` are query parameters.

### Write a program the find count of palindrome strings in the given string and print the highest length palindrome.And also occurrence of each character count in that palindrome strings.
This is a complex coding problem combining multiple string manipulation and map concepts.

```java
import java.util.HashMap;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class PalindromeAnalyzer {

    // Helper to check if a string is a palindrome (ignoring case and non-alphanumeric)
    private static boolean isPalindrome(String s) {
        String cleaned = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        if (cleaned.isEmpty()) return false; // An empty string is not a palindrome for this context
        return cleaned.equals(new StringBuilder(cleaned).reverse().toString());
    }

    // Main method to find palindromes and analyze
    public static void analyzePalindromes(String text) {
        if (text == null || text.isEmpty()) {
            System.out.println("Input string is empty.");
            return;
        }

        // Pattern to find words. \b matches word boundaries, \w+ matches one or more word characters. 
        Pattern pattern = Pattern.compile("\\b\\w+\\b"); 
        Matcher matcher = pattern.matcher(text); // Use original text for word finding

        int palindromeCount = 0;
        String longestPalindromeWord = "";
        
        while (matcher.find()) {
            String word = matcher.group();
            if (isPalindrome(word)) {
                palindromeCount++;
                if (word.length() > longestPalindromeWord.length()) {
                    longestPalindromeWord = word;
                }
            }
        }

        System.out.println("Total palindrome words found: " + palindromeCount);
        System.out.println("Highest length palindrome word: " + longestPalindromeWord);

        if (!longestPalindromeWord.isEmpty()) {
            System.out.println("Occurrence of each character in longest palindrome ('" + longestPalindromeWord + "'):");
            Map<Character, Integer> charCounts = new HashMap<>();
            String cleanedLongest = longestPalindromeWord.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
            for (char c : cleanedLongest.toCharArray()) {
                charCounts.put(c, charCounts.getOrDefault(c, 0) + 1);
            }
            charCounts.forEach((c, count) -> System.out.println("'" + c + "': " + count));
        }
    }

    public static void main(String[] args) {
        String input = "Madam is a civic engineer. Racecar is another example. A man, a plan, a canal: Panama.";
        analyzePalindromes(input);
        /* Expected output for input "Madam is a civic engineer. Racecar is another example. A man, a plan, a canal: Panama.":
        Total palindrome words found: 4 (Madam, a, civic, Racecar)
        Highest length palindrome word: Racecar
        Occurrence of each character in longest palindrome ('racecar'):
        'r': 2
        'a': 2
        'c': 2
        'e': 1
        */
        
        // Example for a phrase as a palindrome:
        String input2 = "A man, a plan, a canal: Panama";
        // To count this as one palindrome, you would process the entire cleaned string:
        if (isPalindrome(input2)) {
            System.out.println("\nFull phrase is a palindrome: " + input2);
            Map<Character, Integer> charCounts = new HashMap<>();
            String cleanedPhrase = input2.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
            for (char c : cleanedPhrase.toCharArray()) {
                charCounts.put(c, charCounts.getOrDefault(c, 0) + 1);
            }
            System.out.println("Char counts in phrase: " + charCounts);
        }
    }
}
```
