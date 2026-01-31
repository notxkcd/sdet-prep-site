---
title: "Java Collections & Streams Mastery"
date: 2026-01-31
draft: false
---

## 1. Collections Framework Hierarchy

```
             Collection (Interface)
               /       |       \
          List       Set       Queue
           |           |          |
   ArrayList   HashSet  LinkedList  PriorityQueue ...
```

### Key Differences

| Interface | Ordered? | Duplicates? | Use Case |
| --- | --- | --- | --- |
| **List** | ✅ Yes | ✅ Yes | Test data, dropdown options. |
| **Set** | ❌ No | ❌ No | Unique IDs, browser handles. |
| **Map** | ❌ No | ❌ No (Keys) | Config properties, Test data pairs. |

---

## 2. Stream API (Pipeline Logic)

**Goal:** Process data declaratively (What to do) rather than imperatively (How to do).

### The Pipeline Structure
`Source` → `Intermediate Operations (Lazy)` → `Terminal Operation (Result)`

### Common Operations

| Operation | Type | Purpose |
| --- | --- | --- |
| `filter()` | Intermediate | Removes unwanted items (e.g., `status != "FAIL"`). |
| `map()` | Intermediate | Transforms data (e.g., `String -> Integer`). |
| `sorted()` | Intermediate | Reorders the flow. |
| `collect()` | Terminal | Converts stream back to a List/Set/Map. |
| `count()` | Terminal | Returns the number of elements. |

### 💡 Example (Selenium Context)
```java
List<String> texts = elements.stream()
    .map(WebElement::getText)
    .filter(t -> t.startsWith("Login"))
    .toList();
```

---

## 3. Collectors API (The Soul of Streams)

| Collector | Purpose |
| --- | --- |
| `toList()` | Gathers result into a List. |
| `groupingBy()` | Groups data by a field (e.g., group tests by result status). |
| `joining()` | Concatenates strings with a delimiter. |
| `toMap()` | Converts list items into key-value pairs. |

```