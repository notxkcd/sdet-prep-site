---
title: "Qapitol Qa Interview Questions"
date: 2026-01-30
draft: false
---

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
