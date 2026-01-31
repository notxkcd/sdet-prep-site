---
title: "Core Java Deep Dive"
date: 2026-01-31
draft: false
---

## 1. Exception Handling Mastery

### Checked vs Unchecked
- **Checked**: Compiler forces you to handle (e.g., `IOException`).
- **Unchecked**: Runtime logic errors (e.g., `NullPointerException`).

### throw vs throws
- **throw**: Used inside a method to actually raise the error.
- **throws**: Used in the method signature to warn callers.

### Modern try-with-resources
Automatically closes resources (files, DB connections) that implement `AutoCloseable`.
```java
try (BufferedReader br = new BufferedReader(new FileReader("config.txt"))) {
    // Logic here
} catch (IOException e) { ... }
```

---

## 2. Functional Programming & Lambdas

**Lambda Expression Syntax:** `(parameters) -> { body }`

### Common Functional Interfaces
- **Predicate**: Returns boolean (Tests a condition).
- **Consumer**: No return (Performs an action).
- **Function**: Input → Output (Transform data).
- **Supplier**: Returns data (Provides a value).

### 💡 Selenium Use Case
```java
wait.until(d -> d.findElement(By.id("login")).isDisplayed());
```

---

## 3. Generics

**Goal:** Type Safety + Reusability. Avoids `ClassCastException`.

- **Type Parameter**: `<T>` - Placeholder for type.
- **Wildcard**: `?` - Represents an unknown type.
- **Bounds**: `<? extends Number>` (Upper bound), `<? super Integer>` (Lower bound).

---

## 4. Modern Java (Switch & Enums)

### Enhanced Switch
```java
String status = switch (result) {
    case PASS -> "Green";
    case FAIL -> "Red";
    default -> "Grey";
};
```

### Power Enums
Enums can have constructors, fields, and methods.
```java
enum Status {
    PASS("✔"), FAIL("✖");
    private final String icon;
    Status(String s) { this.icon = s; }
    public String getIcon() { return icon; }
}
```
