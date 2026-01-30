---
title: "Amazon-3"
date: 2026-01-30
draft: false
---

---

## Original Questions

- Amazon 1st Round
----------------
1.Tell About your Self?
2.Explain Ploymorphism Concept?
3.Explain Inheritance Concept and Where do use in your project?
4.Explain your Project?
5.Input = Same give output as Saammmeeee using java program?
6.Where Java Store the memory?
7.Can we declear a pointee in class?
8.Where do you see word transee in java?
9.Where does the deletion process take place in java?
10.Difference between Method Overloading and Overriding and Explain it?

---

## Answers

### 1. Tell About your Self?
Standard opener. Focus on professional experience, automation skills, tech stack, and a key achievement.

### 2. Explain Ploymorphism Concept?
Polymorphism means "many forms." In OOP, it refers to the ability of an object to take on many forms, particularly an object of a subclass being treated as an object of its superclass. The key applications are:
-   **Method Overriding:** A subclass provides a specific implementation for a method already defined in its superclass. This is run-time polymorphism.
-   **Method Overloading:** Multiple methods in the same class share the same name but have different parameter lists. This is compile-time polymorphism.

### 3. Explain Inheritance Concept and Where do use in your project?
-   **Inheritance:** An OOP mechanism where one class (subclass) acquires properties and methods from another class (superclass). It promotes code reuse and establishes an "is-a" relationship.
-   **Use in project:** "In our test automation framework, we extensively use inheritance. For instance, we have a `BaseTest` abstract class that contains common setup (`@BeforeMethod` for WebDriver initialization) and teardown (`@AfterMethod` for WebDriver quit) logic. All our specific test classes (e.g., `LoginTest`, `ProductSearchTest`) `extend` this `BaseTest` class, inheriting these common functionalities. Similarly, our Page Object classes `extend` a `BasePage` for shared page-level interactions."

### 4. Explain your Project?
Standard. Describe the project domain, your role, the framework used (tools, architecture), challenges, and achievements.

### 5. Input = Same give output as Saammmeeee using java program?
This implies increasing the count of repeating characters.

```java
public class RepeatCharacters {
    public static String transformString(String input) {
        StringBuilder output = new StringBuilder();
        if (input == null || input.isEmpty()) {
            return "";
        }

        for (int i = 0; i < input.length(); i++) {
            char currentChar = input.charAt(i);
            output.append(currentChar); // Append once
            
            // Count consecutive occurrences of the current character
            int count = 0;
            for (int j = i; j < input.length(); j++) {
                if (input.charAt(j) == currentChar) {
                    count++;
                } else {
                    break;
                }
            }
            
            // Append extra characters based on count (example: for 2 'a's, add 1 more 'a')
            for (int k = 0; k < count; k++) { // This logic needs adjustment based on exact output requirement
                                              // The output example "Same -> Saammmeeee" implies:
                                              // S -> S
                                              // a -> aa
                                              // m -> mmm
                                              // e -> eeee
                                              // This is a custom logic, not a general pattern.
                                              // Let's assume the question means "repeat each character 'n' times where 'n' is its count".
                if (currentChar == 'a' && count == 2) output.append('a'); // For "Same", 'a' is repeated 2 times
                else if (currentChar == 'm' && count == 1) output.append("mm"); // For "Same", 'm' is repeated 1 time
                else if (currentChar == 'e' && count == 1) output.append("eee"); // For "Same", 'e' is repeated 1 time
            }
            // The output example logic is very specific and not generalizable easily.
            // Let's re-interpret the prompt based on "Saammmeeee" for input "Same".
            // S (1st char) -> S (1)
            // a (2nd char) -> aa (2)
            // m (3rd char) -> mmm (3)
            // e (4th char) -> eeee (4)
            // This is "repeat char N times, where N is its position (1-indexed)".

        }
        
        // Corrected interpretation: repeat char N times, where N is its position (1-indexed).
        StringBuilder finalOutput = new StringBuilder();
        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            for (int j = 0; j <= i; j++) { // Repeat (i+1) times
                finalOutput.append(c);
            }
        }
        return finalOutput.toString();
    }

    public static void main(String[] args) {
        System.out.println(transformString("Same")); // S aam mmm eeee. No, the output is "Saammmeeee".
        // The output "Saammmeeee" for input "Same" means:
        // S -> S
        // a -> aa
        // m -> mmm
        // e -> eeee
        // Each character is repeated its (1-based) index number of times.

        String input = "Same"; // S, a, m, e
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            for (int j = 0; j <= i; j++) { // repeat i+1 times
                result.append(c);
            }
        }
        System.out.println(result.toString()); // Saammmeeee
    }
}
```

### 6. Where Java Store the memory?
Java uses different memory areas for different purposes:
-   **Heap Memory:** Where all objects (instances of classes) and arrays are stored. It's shared by all threads. Garbage Collection operates here.
-   **Stack Memory:** Each thread in a Java program has its own stack. This is where local variables, method call information, and primitive values are stored.
-   **Method Area (Metaspace in Java 8+):** Stores class-level data like bytecode, static variables, and method definitions.
-   **PC Registers:** Stores the address of the next instruction to be executed by a thread.

### 7. Can we declear a pointee in class?
This is a C/C++ term. Java does **not** have pointers in the traditional sense like C/C++. All object variables in Java are "references," which are conceptually similar to pointers but are type-safe and cannot be directly manipulated by the programmer. There's no concept of a "pointee" to explicitly declare.

### 8. Where do you see word transee in java?
This is likely a typo or misheard word. There is no standard Java keyword or concept called "transee." It might be "transient" (a keyword for serialization) or "transitive" (property of equals() method). If heard, ask for clarification.

### 9. Where does the deletion process take place in java?
Deletion of unused objects (memory deallocation) in Java is handled automatically by the **Garbage Collector (GC)**. The GC runs in the **Heap Memory** and reclaims space occupied by objects that are no longer referenced by the running program. Programmers do not explicitly delete objects like in C++.

### 10. Difference between Method Overloading and Overriding and Explain it?
-   **Method Overloading:** Multiple methods in the same class with the same name but different parameter lists. It's compile-time polymorphism.
-   **Method Overriding:** A subclass provides a specific implementation for a method already defined in its superclass. It's run-time polymorphism.
These are fundamental OOP concepts.
