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

```
(abc)       → capturing group
(?:abc)     → non-capturing
(?=abc)     → lookahead
(?!abc)     → negative lookahead
```

Java does NOT have lookbehind until Java 9+ (now it does):

```
(?<=abc)  → lookbehind
(?<!abc)  → negative lookbehind
```

* * *

⚙️ 3. Java-Specific Gotchas
===========================

Java needs **double escaping**, because strings process escapes _before_ regex sees them.

Examples:

```
"\\d"    // becomes \d in regex
"\\."    // literal dot
"\\\\\\