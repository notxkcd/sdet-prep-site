---
category: "Java"
title: "Find Third Occurrence Regex"
date: 2026-01-31
draft: false
---
category: "Java"

## Prompt:
How to find the third occurance of a word in regex java

## Response:
To find the **third occurrence of a word using regex in Java**, regex _alone_ cannot directly say “give me the 3rd match.”  
But you **can** use regex + Java’s matcher loop to get the 3rd occurrence.

* * *

✅ **Method 1 — Using Matcher and loop (recommended)**
=====================================================

```java
import java.util.regex.*;

public class Main {
    public static void main(String[] args) {
        String text = "apple banana apple grape apple orange";
        String word = "apple";

        Pattern pattern = Pattern.compile("\\b" + word + "\\b");
        Matcher matcher = pattern.matcher(text);

        int count = 0;
        while (matcher.find()) {
            count++;
            if (count == 3) {  // third occurrence
                System.out.println("3rd occurrence at index: " + matcher.start());
                System.out.println("Matched word: " + matcher.group());
                break;
            }
        }

        if (count < 3) {
            System.out.println("Less than 3 occurrences found.");
        }
    }
}
```

### **Output**

```
3rd occurrence at index: 23
Matched word: apple
```

* * *

✅ **Method 2 — Regex lookahead (if you only need to check existence)**
======================================================================

If you just want to match the 3rd occurrence **position**, you can hack it with a lookahead:

```regex
(?:.*?apple){3}
```

In Java:

```java
Pattern pattern = Pattern.compile("(?:.*?\\bapple\\b){3}");
Matcher matcher = pattern.matcher(text);

if (matcher.find()) {
    System.out.println("Position after 3rd occurrence: " + matcher.end());
}
```

But this finds the _position after_ the 3rd match, not the occurrence itself.

* * *

❌ **Regex cannot directly return “the 3rd match”**
==================================================

You must iterate through matches or use a lookahead trick.  
**Looping with `Matcher.find()` is the cleanest and correct Java approach.**

* * *

## Prompt:
Generally what's the best approach

## Response:
The **best and cleanest approach in Java** is:

✅ **Use `Matcher.find()` in a loop and stop at the 3rd match.**
===============================================================

This is considered the **standard**, **readable**, and **reliable** way.

* * *

✔ Why this is the best approach?
--------------------------------
category: "Java"

### **1. Regex engines are designed to return _all_ matches, one at a time**

Regex itself cannot say:

> “Give me only the 3rd occurrence.”

So Java’s `Matcher.find()` loop is the _intended_ API.

* * *

### **2. Works for all patterns**

Whether you search a word, digits, or complex patterns — same logic works.

* * *

### **3. Easy to debug and maintain**

Other approaches like lookahead hacks are confusing and fragile.

* * * 

### **4. Allows reading start/end indexes easily**

You get:

*   `matcher.start()`
*   `matcher.end()`
*   `matcher.group()`

All directly for the 3rd match.

* * *

✅ **Best approach — the one professionals use**
-----------------------------------------------
category: "Java"

```java
Pattern p = Pattern.compile("apple");
Matcher m = p.matcher(text);

for (int i = 0; i < 3 && m.find(); i++) {
    if (i == 2) { // 0 = 1st, 1 = 2nd, 2 = 3rd
        System.out.println("3rd occurrence at index: " + m.start());
    }
}
```

* * *

✔ Summary
---------
category: "Java"

| Approach | Good? | Why |
| --- | --- | --- |
| **Matcher.find() loop** | ⭐⭐⭐⭐⭐ | Most stable, readable, works everywhere |
| Lookaheads `(.*?pattern){3}` | ⭐ | Hacky, hard to maintain |
| Split and count | ⭐⭐ | Works but loses index positions |
| Custom parser | ⭐⭐⭐ | Only for complex cases |

* * *

## Prompt:
Good morning, good evening Good night 

To 

Good morning, good evening bad night

## Response:
If you simply want to change **“good night” → “bad night”** while keeping the rest the same, you can just use a replace.

### **Java**

```java
String text = "Good morning, good evening Good night";
String updated = text.replaceAll("(?i)good night", "bad night");
System.out.println(updated);
```

### Output

```
Good morning, good evening bad night
```

### Explanation

*   `(?i)` makes it **case-insensitive** so it matches `Good night`, `good night`, etc.
*   Only the **“good night”** part changes, the rest stays the same.

```