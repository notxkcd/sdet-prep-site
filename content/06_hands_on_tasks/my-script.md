---
title: "My Script: Practical Code"
date: 2026-01-30
draft: false
---

## 1. Java: Reverse a String
"I prefer using a `StringBuilder` for efficiency, or a simple `for` loop if asked to show logic:"
```java
public String reverse(String str) {
    String rev = "";
    for(int i = str.length()-1; i >= 0; i--) {
        rev = rev + str.charAt(i);
    }
    return rev;
}
```

## 2. Selenium: Handling Windows/Popups
"I use `driver.getWindowHandles()` to get the set of IDs, then iterate through them to switch focus:"
```java
String parent = driver.getWindowHandle();
Set<String> allWindows = driver.getWindowHandles();
for(String handle : allWindows) {
    if(!handle.equals(parent)) {
        driver.switchTo().window(handle);
    }
}
```

## 3. SQL: The Join Query
"To find a student's marks from two tables (Students and Exams):"
```sql
SELECT s.Name, e.Marks 
FROM Students s 
JOIN Exams e ON s.ID = e.StudentID 
WHERE e.Subject = 'Math';
```
