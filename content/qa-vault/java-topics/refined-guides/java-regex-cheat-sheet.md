---
title: "Java Regex Cheat Sheet"
date: 2026-01-31
draft: false
---

# Java Regex Cheat Sheet (Completed)

**User:** Mohammed Shahid (shahid.xkcd@gmail.com)  
**Status:** Completed & Refined

---

## Prompt:
teach me Java RegeEx And All i need to know No BS , strigh tto the point and give me things to remember so i dont' forget the main thingy so  i can recall without memorizing syntax like a soydev

## Response:
Got you. Here is **Java Regex explained like a systems programmer**, no fluff, no soydev energy.  
This is everything you need to know + how to _actually_ remember it.

* * *

🚀 1. The Only Mental Model You Need
====================================

A regex in Java is just:

```
Pattern  +  Matcher  +  Input String
```

Java’s regex is _basically_ PCRE-lite.

Workflow:

```java
Pattern p = Pattern.compile("regex");
Matcher m = p.matcher("input");
m.find();    // search
m.matches(); // full match
```

* * *

🎯 2. Core Syntax You Must Remember (Minimal, Essential)
========================================================

**Literals**
------------

```
a    → literal 'a'
\.   → dot literal
```

**Character classes**
---------------------

```
[abc]    → a or b or c
[^abc]   → NOT a/b/c
[a-zA-Z] → ranges
```

**Shorthand:**

```
\d  → digits
\D  → non-digits
\w  → letters + digits + _
\W  → not \w
\s  → whitespace
\S  → not whitespace
```

**Quantifiers**
---------------

```
*  → 0+
+  → 1+
?  → 0 or 1
{n}       → exactly n
{n,}      → n or more
{n,m}     → between n and m
```

**Greedy vs Lazy:**

```
.*      → greedy
.*?     → lazy
```

**Anchors**
-----------

```
^   → start of string
$   → end of string
\b  → word boundary
\B  → not boundary
```

**Groups**
----------

```java
(abc)       → capturing group
(?:abc)     → non-capturing
(?=abc)     → lookahead
(?!abc)     → negative lookahead
```

Java does NOT have lookbehind until Java 9+ (now it does):

```java
(?<=abc)  → lookbehind
(?<!abc)  → negative lookbehind
```

* * *

⚙️ 3. Java-Specific Gotchas
===========================

Java needs **double escaping**, because strings process escapes _before_ regex sees them.

Examples:

```java
"\\d"    // becomes \d in regex
"\\."    // literal dot
"\\\\\\
```

**Rule:**  
👉 _If regex uses a `\`, Java needs `\\`._

* * * 

🔥 4. Useful Patterns You Should Memorize (because they appear everywhere)
==========================================================================

| Purpose | Regex | Notes |
| --- | --- | --- |
| Word | `\\w+` | underscores included |
| Integer | `-?\\d+` | optional minus |
| Decimal | `-?\\d+(\\.\\d+)?` | lazy decimal |
| Email | `^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$` | practical, not perfect |
| Whitespace cleanup | `\\s+` | normalize spaces |
| Extract digits | `\\d+` | trivial |

* * *

🧠 5. How To Think About Regex: 3 Rules to Recall Everything
============================================================

### **Rule 1: Regex is a tiny language**

*   Characters = literals
*   `[]` = pick one
*   `()` = group or capture
*   `? * + {}` = repeat
*   `^ $ \b` = borders

If you remember this hierarchy, you almost **never** need to memorize syntax.

### **Rule 2: Escape anything that “means something”**

`.` `+` `*` `?` `(` `)` `[` `]` `^` `$` `\` `|`

→ If you want literal of these, prefix with `\\` in Java.

### **Rule 3: Engine moves left → right**

Match = greedy  
Match? → fallback  
Lookarounds don't consume text

* * *

💻 6. Java Code Snippets You Will Use Constantly
================================================

**Find all occurrences**
------------------------

```java
Pattern p = Pattern.compile("word");
Matcher m = p.matcher(text);

while (m.find()) {
    System.out.println(m.group());
}
```

**Replace**
-----------

```java
text = text.replaceAll("foo", "bar");
```

**Group extraction**
--------------------

```java
Pattern p = Pattern.compile("Name: (\\w+)");
Matcher m = p.matcher(text);

if (m.find()) {
    System.out.println(m.group(1)); // captured name
}
```

**Match whole string**
----------------------

```java
if (text.matches("\\d+")) {
    // only digits
}
```

* * *

## Prompt:
and also all the methods

## Response:
Here are **ALL the important Java regex methods** — **no BS, no fluff, no soydev explanations**.  
These are the ONLY methods you ever use in real work.

* * *

🔥 PART 1 — `String` Regex Methods
==================================

Java has built-in regex methods _on the `String` class_.  
These are the ones you’ll use 90% of the time.

* * *

**1. `matches(String regex)`**
-------------------------------

Checks _whole string_ matches pattern.

```
"123".matches("\\d+");  // true
```

**Important:** Not for searching. Use `find()` for that.

* * * 

**2. `replaceAll(String regex, String replacement)`**
------------------------------------------------------

Replace ALL matches.

```java
text.replaceAll("\\s+", " ");
```

* * * 

**3. `replaceFirst(String regex, String replacement)`**
--------------------------------------------------------

Replace only the first match.

```java
text.replaceFirst("\\d", "#");
```

* * * 

**4. `split(String regex)`**
-----------------------------

Split by regex.

```java
String[] parts = text.split("\\s+");
```

* * * 

🔥 PART 2 — `Pattern` CLASS METHODS
===================================

`Pattern` = compiled regex.

* * * 

**1. `compile(String regex)`**
-------------------------------

Compile regex to a Pattern.

```java
Pattern p = Pattern.compile("\\d+");
```

* * * 

**2. `matcher(CharSequence input)`**
-------------------------------------

Attach pattern to a string.

```java
Matcher m = p.matcher(text);
```

* * * 

**3. `split(CharSequence input)`**
-----------------------------------

Same as `String.split`, but uses an existing Pattern.

```java
p.split("a b c");
```

* * * 

**4. `matches(String regex, CharSequence input)`**
---------------------------------------------------

Static helper. Rarely used.

```java
Pattern.matches("\\d+", "123");
```

* * * 

**5. Flags with compile**
--------------------------

Flags modify regex behavior.

```java
Pattern.compile("abc", Pattern.CASE_INSENSITIVE);
```

Common flags:

| Flag | Meaning |
| --- | --- |
| `Pattern.CASE_INSENSITIVE` | Ignore case |
| `Pattern.MULTILINE` | ^ and $ match line boundaries |
| `Pattern.DOTALL` | `.` matches newline |
| `Pattern.UNICODE_CASE` | Proper unicode case folding |
| `Pattern.COMMENTS` | Allow whitespace & `#` comments |

Combine flags:

```java
Pattern p = Pattern.compile("abc", Pattern.CASE_INSENSITIVE | Pattern.DOTALL);
```

* * * 

🔥 PART 3 — `Matcher` CLASS METHODS
===================================

This is where ALL the actual work happens.

* * * 

SEARCH METHODS
==============

**1. `find()`**
----------------

Find next match.

```java
while (m.find()) {
    m.group();
}
```

* * * 

**2. `find(int start)`**
-------------------------

Start search at index.

```java
m.find(10);
```

* * * 

**3. `lookingAt()`**
---------------------

Matches from start of string (not full string).

```java
m.lookingAt();
```

* * * 

**4. `matches()`**
-------------------

Full string match.

```java
m.matches();
```

* * * 

GROUP & CAPTURE METHODS
=======================

**5. `group()`**
-----------------

Returns the entire match.

```java
m.group();
```

* * * 

**6. `group(int index)`**
--------------------------

Returns a specific capture group.

```java
m.group(1);
```

* * * 

**7. `groupCount()`**
----------------------

Number of capturing groups.

* * * 

**8. `start()`**
-----------------

Start index of the whole match.

```java
m.start();
```

* * * 

**9. `start(int group)`**
--------------------------

Start of capture group.

* * * 

**10. `end()`**
----------------

End index of match.

```java
m.end();
```

* * * 

**11. `end(int group)`**
-------------------------

End of capture group.

* * * 

REPLACEMENT METHODS
===================

**12. `replaceAll(String replacement)`**
-----------------------------------------

```java
m.replaceAll("#");
```

* * * 

**13. `replaceFirst(String replacement)`**
-------------------------------------------

```java
m.replaceFirst("@");
```

* * * 

**14. `appendReplacement(StringBuilder sb, String replacement)`**
------------------------------------------------------------------

Manual streaming replacement (advanced).

```java
StringBuilder sb = new StringBuilder();
while (m.find()) {
    m.appendReplacement(sb, "REPLACED");
}
m.appendTail(sb);
```

* * * 

**15. `appendTail(StringBuilder sb)`**
---------------------------------------

Finish the streaming replace.

* * * 

OTHER MATCHER METHODS
=====================

**16. `reset()`**
------------------

Send matcher back to start.

```java
m.reset();
```

* * * 

**17. `reset(CharSequence input)`**
------------------------------------

Reset + new string.

```java
m.reset(newInput);
```

* * * 

**18. `pattern()`**
--------------------

Get the Pattern object.

* * * 

**19. `usePattern(Pattern newPattern)`**
-----------------------------------------

Change the pattern used by matcher.

* * * 

**20. `region(int start, int end)`**
-------------------------------------

Search within a substring _without creating a new string_.

```java
m.region(0, 10);
```

* * * 

**21. `regionStart()`, `regionEnd()`**
---------------------------------------

Get region bounds.

* * * 

**22. `hitEnd()`**
-------------------

Check if matcher hit the end of input on the last match attempt.

Rarely needed.

* * * 

**23. `requireEnd()`**
-----------------------

Check if more input _could_ produce a match.

Rare.

* * * 

🧠 MEMORY CHEAT LIST (the REAL essentials)
==========================================

### **Most used 7 methods**

If you remember these you know 90% of Java regex:

```
matches()            // full match
find()               // search
group()              // matched text
group(n)             // capture
replaceAll()         // replace
split()              // split by regex
Pattern.compile()    // compile
```

### **Moderately used**

```java
lookingAt()
start(), end()
reset()
```

### **Rare/Advanced**

```java
appendReplacement()
appendTail()
region()
hitEnd()
requireEnd()
```

* * * 

## Prompt:
yes

## Response:
Great — here is the **ultra-condensed, printable, zero-soydev Java Regex cheat sheet** plus **regex drills** to burn this permanently into your brain.

* * *

⚡ PART 1 — 1-PAGE JAVA REGEX CHEAT SHEET
========================================

(You can literally memorize this in one sitting.)

* * *

🟥 REGEX SYNTAX (THE REAL CORE)
-------------------------------

### **Character Classes**

```
[abc]      a or b or c
[^abc]     NOT a/b/c
[a-zA-Z]   ranges
\d \w \s   digit / word / space
\D \W \S   negations
.          any char (except \n unless DOTALL)
```

### **Quantifiers**

```
*      0+        (greedy)
+      1+
?      0 or 1
{n}    exactly n
{n,}   n or more
{n,m}  between n and m
*? +? ??   lazy versions
```

### **Anchors**

```java
^     start of string
$     end of string
\b    word boundary
\B    not boundary
```

### **Groups**

```java
(...)       capturing group
(?:...)     non-capturing
(?=...)     positive lookahead
(?!...)     negative lookahead
(?<=...)    lookbehind
(?<!...)    negative lookbehind
```

### **Alternation**

```java
a|b   → a or b
```

* * *

🟥 JAVA ESCAPES
---------------

Java needs double escaping.

```java
\\d      \d in regex
\\.      literal dot
\\\\     literal \
```

Rule:  
**If your regex needs 1 slash → Java needs 2**.

* * *

⚡ PART 2 — JAVA REGEX APIS (HARDCORE SHORTLIST)
===============================================

* * *

🟩 `String` class
-----------------

```java
matches(regex)
replaceAll(regex, repl)
replaceFirst(regex, repl)
split(regex)
```

* * * 

🟩 Pattern
----------

```java
Pattern.compile(regex)
matcher(input)
split(input)
```

### Flags

```java
Pattern.CASE_INSENSITIVE
Pattern.MULTILINE
Pattern.DOTALL
Pattern.COMMENTS
```

Combine:

```java
Pattern.compile("abc", Pattern.CASE_INSENSITIVE | Pattern.DOTALL)
```

* * * 

🟩 Matcher Methods (Everything you need)
----------------------------------------

```java
find()
find(start)

matches()
lookingAt()

group()
group(n)
groupCount()

start()
start(n)
end()
end(n)

replaceAll(repl)
replaceFirst(repl)

appendReplacement(sb, repl)
appendTail(sb)

reset()
reset(newInput)

region(start, end)
regionStart()
regionEnd()
```

* * * 

⚡ PART 3 — MEMORY “ANCHORS” (RECALL WITHOUT MEMORIZING)
=======================================================

This is the **mental model** to reconstruct regex instantly:

### 🔥 **Regex = Scanner + Rules**

*   `[]` → selection
*   `()` → capture
*   `*+?{}` → repetition
*   `^$` → borders
*   `\` → escape
*   `|` → OR

### 🔥 **Regex engine goes left → right**

Greedy = “take everything, backtrack later”  
Lazy = “take nothing, expand when needed”

### 🔥 **Java always sees your string BEFORE regex sees it**

Which is why you escape double.

* * *

⚡ PART 4 — 20 PRACTICE DRILLS (GRADUALLY HARDER)
================================================

Do these and you become a regex killer.

* * *

🔹 Level 1 — Basics
-------------------

**1. Match a 10-digit mobile number**

```java
\\d{10}
```

**2. Match lowercase letters only**

```java
[a-z]+
```

**3. Match a filename ending in .txt**

```java
.+\\.txt
```

* * *

🔹 Level 2 — Groups & Captures
------------------------------

**4. Extract first name and last name**  
Pattern:

```java
(\\w+) (\\w+)
```

**5. Match integers with optional sign**

```java
[-+]?\\d+
```

**6. Match a decimal number**

```java
-?\\d+(?:\\.\\d+)?
```

* * *

🔹 Level 3 — Boundaries & Anchors
---------------------------------

**7. Match a whole line containing only letters**

```java
^[a-zA-Z]+$
```

**8. Match a word boundary “cat”**

```java
\\bcat\\b
```

* * *

🔹 Level 4 — Replace
--------------------

**9. Replace multiple spaces with 1**

```java
replaceAll("\\s+", " ");
```

**10. Extract only digits from a string**

```java
find("\\d+")
```

* * * 

🔹 Level 5 — Lookaheads
-----------------------

**11. Number followed by “kg”**

```java
\\d+(?=kg)
```

**12. Capture only if not followed by “bad”**

```java
good(?!boy)
```

* * * 

🔹 Level 6 — Lookbehinds
------------------------

(Works in Java 9+)

**13. Digits preceded by ₹**

```java
(?<=₹)\\\\d+
```

* * * 

🔹 Level 7 — Harder Patterns
----------------------------

**14. Match an email**

```java
^[^@\\s]+@[^@\\s]+\\.`[^@\\s]+$
```

**15. Match a URL (practical one)**

```java
https?://[^\\s]+
```

* * * 

🔹 Level 8 — Real-World
-----------------------

**16. Extract key=value pairs**

```java
(\\w+)=(\\w+)
```

**17. Match a date (YYYY-MM-DD)**

```java
\\d{4}-\\d{2}-\\d{2}
```

* * * 

🔹 Level 9 — You’re now advanced
--------------------------------

**18. Match Java identifiers**

```java
[a-zA-Z_$][a-zA-Z0-9_$]*
```

**19. Validate hex color**

```java
#?[0-9a-fA-F]{6}
```

* * * 

🔥 Final Boss
-------------

**20. Balanced parentheses (regex hack)**

```java
\\((?:[^()]+|\\([^()]*\\\\))*\\)
```