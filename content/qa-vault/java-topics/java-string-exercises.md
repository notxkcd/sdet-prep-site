---
category: "Java"
title: "Java String Exercises"
date: 2026-01-31
draft: false
---
category: "Java"

## Prompt:
"I want to practice [Strings] in [java]. Can you give me [20] exercises that start very easy and gradually become harder? I want each exercise to be solved step by step with explanations, and I want to see how variable values change at each step if applicable.

## Response:
Nice — below are **20** progressive Java string exercises. For each: a short problem, a compact Java solution, then a step-by-step walkthrough showing how variables change (where applicable) and short explanations. I kept code runnable and explanations focused so you can practice and trace values.

* * *

**1) Length of a string**
---------------------
category: "Java"

**Problem:** Given `s = "hello"`, print its length.  
**Code**

```java
String s = "hello";
int len = s.length();
System.out.println(len);
```

**Steps / trace**

*   `s` = `"hello"`
*   `s.length()` computes number of characters: count each char: h(1) e(2) l(3) l(4) o(5) → result `5`
*   `len` = `5` → printed `5`

* * *

**2) Character at an index**
------------------------
category: "Java"

**Problem:** Find character at index `2` in `"hello"`.  
**Code**

```java
String s = "hello";
char c = s.charAt(2);
System.out.println(c);
```

**Steps / trace**

*   `s` = `"hello"`
*   Indexing: 0→'h', 1→'e', 2→'l'
*   `c` = `'l'` → printed `l`

* * *

**3) Concatenate strings**
----------------------
category: "Java"

**Problem:** Join `"hello"` and `"world"` with a space.  
**Code**

```java
String a = "hello";
String b = "world";
String joined = a + " " + b;
System.out.println(joined);
```

**Steps / trace**

*   `a` = `"hello"`, `b` = `"world"`
*   `a + " "` → `"hello "`
*   `"hello " + b` → `"hello world"`
*   `joined` = `"hello world"`

* * *

**4) Substring extraction**
-----------------------
category: "Java"

**Problem:** Extract `"ell"` from `"hello"`.  
**Code**

```java
String s = "hello";
String sub = s.substring(1, 4); // start inclusive, end exclusive
System.out.println(sub);
```

**Steps / trace**

*   `s` = `"hello"`
*   `s.substring(1,4)` picks chars at indices 1,2,3 → 'e','l','l' → `"ell"`
*   `sub` = `"ell"`

* * *

**5) First occurrence index**
-------------------------
category: "Java"

**Problem:** Find index of `"lo"` in `"hello world"`.  
**Code**

```java
String s = "hello world";
int idx = s.indexOf("lo");
System.out.println(idx);
```

**Steps / trace**

*   `s` = `"hello world"`
*   scan: `"he"(0) "el"(1) "ll"(2) "lo"(3)` → match at starting index `3`
*   `idx` = `3`

* * *

**6) Last occurrence index**
------------------------
category: "Java"

**Problem:** Last index of `'l'` in `"hello world"`.  
**Code**

```java
String s = "hello world";
int last = s.lastIndexOf('l');
System.out.println(last);
```

**Steps / trace**

*   `s` = `"hello world"`, positions of 'l' are indices 2,3,9
*   `lastIndexOf` returns `9`
*   `last` = `9`

* * *

**7) Case change and trim**
-----------------------
category: "Java"

**Problem:** Given `" Java "`, trim and convert to uppercase.  
**Code**

```java
String s = "  Java  ";
String trimmed = s.trim();
String upper = trimmed.toUpperCase();
System.out.println("[" + upper + "]");
```

**Steps / trace**

*   `s` = `"  Java  "`
*   `trim()` removes leading/trailing spaces → `"Java"`
*   `toUpperCase()` → `"JAVA"`
*   `upper` = `"JAVA"` → printed `[JAVA]`

* * *

**8) Replace characters**
---------------------
category: "Java"

**Problem:** Replace all `'a'` with `'@'` in `"banana"`.  
**Code**

```java
String s = "banana";
String r = s.replace('a', '@');
System.out.println(r);
```

**Steps / trace**

*   `s` = `"banana"`
*   replace: b a n a n a → b @ n @ n @ → `"b@n@n@"`
*   `r` = `"b@n@n@"`

* * *

**9) contains / startsWith / endsWith**
-----------------------------------
category: "Java"

**Problem:** Check if `"hello.java"` contains `"java"`, starts with `"he"`, ends with `".java"`.  
**Code**

```java
String s = "hello.java";
boolean has = s.contains("java");
boolean sw = s.startsWith("he");
boolean ew = s.endsWith(".java");
System.out.println(has + ", " + sw + ", " + ew);
```

**Steps / trace**

*   `s` = `"hello.java"`
*   `contains("java")` → true
*   `startsWith("he")` → true
*   `endsWith(".java")` → true
*   prints `true, true, true`

* * *

**10) Split and join**
------------------
category: "Java"

**Problem:** Split `"a,b,c"` by `,` and join with `-`.  
**Code**

```java
String s = "a,b,c";
String[] parts = s.split(",");
String joined = String.join("-", parts);
System.out.println(joined);
```

**Steps / trace**

*   `s` = `"a,b,c"`
*   `split(",")` → `["a","b","c"]`
*   `String.join("-", parts)` → `"a-b-c"`

* * *

**11) Reverse a string (manual)**
-----------------------------
category: "Java"

**Problem:** Reverse `"abcd"` → `"dcba"`.  
**Code**

```java
String s = "abcd";
StringBuilder sb = new StringBuilder();
for (int i = s.length()-1; i >= 0; i--) {
    sb.append(s.charAt(i));
}
String rev = sb.toString();
System.out.println(rev);
```

**Steps / trace (iteration)**

*   `s` = `"abcd"`, length=4, indices: 0:a,1:b,2:c,3:d
*   i=3 → append 'd' → sb="d"
*   i=2 → append 'c' → sb="dc"
*   i=1 → append 'b' → sb="dcb"
*   i=0 → append 'a' → sb="dcba"
*   `rev` = `"dcba"`

* * *

**12) Palindrome check**
------------------------------------------------------
category: "Java"

**Problem:** Check if `"A man a plan a canal Panama"` is a palindrome (ignore spaces/case).  
**Code**

```java
String s = "A man a plan a canal Panama";
String cleaned = s.replaceAll("\\s+", "").toLowerCase();
boolean isPal = true;
for (int i = 0, j = cleaned.length() - 1; i < j; i++, j--) {
    if (cleaned.charAt(i) != cleaned.charAt(j)) { isPal = false; break; }
}
System.out.println(isPal);
```

**Steps / trace**

*   `s` = `"A man a plan a canal Panama"`
*   `cleaned` = remove spaces → `"AmanaplanacanalPanama"` → `toLowerCase()` → `"amanaplanacanalpanama"`
*   length = 21
*   compare pairs (i=0 vs j=20): 'a'=='a' ... all match → `isPal=true`

* * *

**13) Count vowels and consonants**
-------------------------------
category: "Java"

**Problem:** For `"hello"`, count vowels and consonants.  
**Code**

```java
String s = "hello";
int vowels = 0, consonants = 0;
String vowelsSet = "aeiouAEIOU";
for (char ch : s.toCharArray()) {
    if (!Character.isLetter(ch)) continue;
    if (vowelsSet.indexOf(ch) >= 0) vowels++;
    else consonants++;
}
System.out.println(vowels + " vowels, " + consonants + " consonants");
```

**Steps / trace**

*   `s` = `"hello"` characters: h e l l o
*   h → consonant (c=1)
*   e → vowel (v=1)
*   l → consonant (c=2)
*   l → consonant (c=3)
*   o → vowel (v=2)
*   result: `2 vowels, 3 consonants`

* * *

**14) Remove duplicate characters (preserve order)**
------------------------------------------------
category: "Java"

**Problem:** From `"banana"`, produce `"ban"`.  
**Code**

```java
String s = "banana";
StringBuilder sb = new StringBuilder();
boolean[] seen = new boolean[256];
for (char ch : s.toCharArray()) {
    if (!seen[ch]) {
        sb.append(ch);
        seen[ch] = true;
    }
}
String result = sb.toString();
System.out.println(result);
```

**Steps / trace**

*   start: `seen` all false, sb=""
*   'b' → not seen → sb="b", mark b=true
*   'a' → not seen → sb="ba", mark a=true
*   'n' → not seen → sb="ban", mark n=true
*   'a' → seen → skip
*   'n' → seen → skip
*   'a' → seen → skip
*   `result` = `"ban"`

* * *

**15) Anagram check (sort & compare)**
----------------------------------
category: "Java"

**Problem:** Determine if `"listen"` and `"silent"` are anagrams.  
**Code**

```java
String a = "listen", b = "silent";
char[] ca = a.toCharArray(), cb = b.toCharArray();
java.util.Arrays.sort(ca);
java.util.Arrays.sort(cb);
boolean anagram = java.util.Arrays.equals(ca, cb);
System.out.println(anagram);
```

**Steps / trace**

*   a → \['l','i','s','t','e','n'\] → sorted → \['e','i','l','n','s','t'\]
*   b → \['s','i','l','e','n','t'\] → sorted → \['e','i','l','n','s','t'\]
*   arrays equal → `true`

* * *

**16) Simple run-length compress**
--------------------------------------
category: "Java"

**Problem:** Compress `"aaabbc"` → `"a3b2c1"`.  
**Code**

```java
String s = "aaabbc";
StringBuilder sb = new StringBuilder();
int count = 1;
for (int i = 1; i <= s.length(); i++) {
    if (i < s.length() && s.charAt(i) == s.charAt(i-1)) {
        count++;
    } else {
        sb.append(s.charAt(i-1)).append(count);
        count = 1;
    }
}
System.out.println(sb.toString());
```

**Steps / trace**

*   i=1: s[1]=a == s[0]=a → count=2
*   i=2: s[2]=a == s[1]=a → count=3
*   i=3: s[3]=b != s[2]=a → append 'a' + 3 → sb="a3", count=1
*   i=4: s[4]=b == s[3]=b → count=2
*   i=5: s[5]=c != s[4]=b → append 'b' + 2 → sb="a3b2", count=1
*   i=6 == length → append 'c' +1 → sb="a3b2c1"
*   prints `"a3b2c1"`

* * *

**17) Longest common prefix**
--------------------------------------------
category: "Java"

**Problem:** Given `["flower","flow","flight"]` find longest common prefix → `"fl"`.  
**Code**

```java
String[] arr = {"flower","flow","flight"};
if (arr.length == 0) { System.out.println(""); return; }
String prefix = arr[0];
for (int i = 1; i < arr.length; i++) {
    while (!arr[i].startsWith(prefix)) {
        prefix = prefix.substring(0, prefix.length()-1);
        if (prefix.isEmpty()) break;
    }
}
System.out.println(prefix);
```

**Steps / trace**

*   `prefix` = `"flower"`
*   compare with "flow": does "flow" start with "flower"? No → shorten prefix:
    *   "flowe" → no
    *   "flow" → yes → prefix="flow"
*   compare with "flight": does "flight" start with "flow"? No → shorten:
    *   "flo" → no
    *   "fl" → yes → prefix="fl"
*   result `"fl"`

* * *

**18) Simple `atoi` (string → int)**
--------------------------------------------------------------------------------------
category: "Java"

**Problem:** Convert `" -42"` → `-42`.  
**Code**

```java
String s = "  -42";
int i = 0, n = s.length();
// skip whitespace
while (i < n && Character.isWhitespace(s.charAt(i))) i++;
int sign = 1;
if (i < n && (s.charAt(i) == '+' || s.charAt(i) == '-')) {
    if (s.charAt(i) == '-') sign = -1;
    i++;
}
int num = 0;
while (i < n && Character.isDigit(s.charAt(i))) {
    num = num * 10 + (s.charAt(i) - '0');
    i++;
}
int result = sign * num;
System.out.println(result);
```

**Steps / trace**

*   `s` = `"  -42"`, `i=0`
*   skip spaces: i→1 then i→2 (now at '-')
*   sign: `s.charAt(2)`	='-' → `sign=-1`, `i=3`
*   parse digits:
    *   `s.charAt(3)`	='4' → `num = 0*10 + 4 = 4`, `i=4`
    *   `s.charAt(4)`	='2' → `num = 4*10 + 2 = 42`, `i=5`
*   `result = -1 * 42 = -42` → printed `-42`

* * *

**19) Longest palindromic substring**
----------------------------------------------------
category: "Java"

**Problem:** For `"babad"` find longest palindromic substring (`"bab"` or `"aba"`).  
**Code**

```java
String s = "babad";
if (s == null || s.length() < 1) { System.out.println(""); return; }
int start = 0, end = 0;
for (int i = 0; i < s.length(); i++) {
    int len1 = expand(s, i, i);     // odd length
    int len2 = expand(s, i, i+1);   // even length
    int len = Math.max(len1, len2);
    if (len > end - start + 1) {
        start = i - (len - 1) / 2;
        end = i + len / 2;
    }
}
System.out.println(s.substring(start, end + 1));

// helper
static int expand(String s, int left, int right) {
    while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
        left--; right++;
    }
    return right - left - 1; // length
}
```

* * *

**20) Check if two strings are isomorphic**
---------------------------------------
category: "Java"

**Problem:** Determine if `"egg"` and `"add"` are isomorphic (`'e'->'a', 'g'->'d'`), but `"foo"` and `"bar"` are not.  
**Code**

```java
String s = "egg", t = "add";
boolean iso = areIsomorphic(s, t);
System.out.println(iso);

static boolean areIsomorphic(String s, String t) {
    if (s.length() != t.length()) return false;
    int[] mapS = new int[256]; // store mapping to char+1
    int[] mapT = new int[256];
    for (int i = 0; i < s.length(); i++) {
        char cs = s.charAt(i), ct = t.charAt(i);
        if (mapS[cs] == 0 && mapT[ct] == 0) {
            mapS[cs] = ct + 1; // store mapped char
            mapT[ct] = cs + 1;
        } else {
            if (mapS[cs] != ct + 1 || mapT[ct] != cs + 1) return false;
        }
    }
    return true;
}
```

**Explanation:** Two maps ensure one-to-one mapping.

```
