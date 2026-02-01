# Java string exercises

**User:** Mohammed Shahid (shahid.xkcd@gmail.com)  
**Created:** 12/4/2025 0:51:05  
**Updated:** 2/1/2026 12:52:43  
**Exported:** 2/1/2026 12:52:52  
**Link:** [https://chatgpt.com/c/69308d95-b31c-8324-941a-6e2ff6522280](https://chatgpt.com/c/69308d95-b31c-8324-941a-6e2ff6522280)  

## Prompt:
"I want to practice [Strings] in [java]. Can you give me [20] exercises that start very easy and gradually become harder? I want each exercise to be solved step by step with explanations, and I want to see how variable values change at each step if applicable.

## Response:
Thought for 5s

20 Java string exercises (easy → harder) — each solved step-by-step with variable traces
========================================================================================

Nice — below are **20** progressive Java string exercises. For each: a short problem, a compact Java solution, then a step-by-step walkthrough showing how variables change (where applicable) and short explanations. I kept code runnable and explanations focused so you can practice and trace values.

* * *

1) Length of a string
---------------------

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

**Explanation:** `length()` returns number of UTF-16 code units for simple ASCII strings this matches characters.

* * *

2) Character at an index
------------------------

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

**Explanation:** `charAt` uses zero-based indexing.

* * *

3) Concatenate strings
----------------------

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

**Explanation:** `+` concatenates strings. For many concatenations prefer `StringBuilder`.

* * *

4) Substring extraction
-----------------------

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

**Explanation:** `substring(a,b)` includes `a`, excludes `b`.

* * *

5) First occurrence index
-------------------------

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

**Explanation:** `indexOf` returns -1 if not found.

* * *

6) Last occurrence index
------------------------

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

7) Case change and trim
-----------------------

**Problem:** Given `" Java "`, trim and convert to uppercase.  
**Code**

```java
String s = "  Java  ";
String trimmed = s.trim();
String upper = trimmed.toUpperCase();
System.out.println("[" + upper + "]");
```

**Steps / trace**

*   `s` = `" Java "`
*   `trim()` removes leading/trailing spaces → `"Java"`
*   `toUpperCase()` → `"JAVA"`
*   `upper` = `"JAVA"` → printed `[JAVA]`

* * *

8) Replace characters
---------------------

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

**Explanation:** `replace(char,char)` replaces all occurrences.

* * *

9) contains / startsWith / endsWith
-----------------------------------

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

10) Split and join
------------------

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

11) Reverse a string (manual)
-----------------------------

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

**Explanation:** Using `StringBuilder` is efficient.

* * *

12) Palindrome check (case-insensitive, ignore spaces)
------------------------------------------------------

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

**Explanation:** Normalize then two-pointer compare.

* * *

13) Count vowels and consonants
-------------------------------

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

14) Remove duplicate characters (preserve order)
------------------------------------------------

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

**Explanation:** Works for basic ASCII; for full Unicode use `Set<Character>`.

* * *

15) Anagram check (sort & compare)
----------------------------------

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

**Explanation:** Sorting is O(n log n). For O(n) use frequency arrays.

* * *

16) Simple run-length compress (basic)
--------------------------------------

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

*   i=1: s\[1\]=a == s\[0\]=a → count=2
*   i=2: s\[2\]=a == s\[1\]=a → count=3
*   i=3: s\[3\]=b != s\[2\]=a → append 'a' + 3 → sb="a3", count=1
*   i=4: s\[4\]=b == s\[3\]=b → count=2
*   i=5: s\[5\]=c != s\[4\]=b → append 'b' + 2 → sb="a3b2", count=1
*   i=6 == length → append 'c' +1 → sb="a3b2c1"
*   prints `"a3b2c1"`

**Note:** Not reversible uniquely in all cases (if digits in input) — simple example.

* * *

17) Longest common prefix (array of strings)
--------------------------------------------

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

*   `prefix = "flower"`
*   compare with "flow": does "flow" start with "flower"? No → shorten prefix:
    *   "flowe" → no
    *   "flow" → yes → prefix="flow"
*   compare with "flight": does "flight" start with "flow"? No → shorten:
    *   "flo" → no
    *   "fl" → yes → prefix="fl"
*   result `"fl"`

**Explanation:** Iteratively shrink prefix.

* * *

18) Simple `atoi` (string → int) supporting whitespace and sign (no overflow handling)
--------------------------------------------------------------------------------------

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

*   `s` = `" -42"`, `i=0`
*   skip spaces: i→1 then i→2 (now at '-')
*   sign: `s.charAt(2)`\='-' → `sign=-1`, `i=3`
*   parse digits:
    *   `s.charAt(3)`\='4' → `num = 0*10 + 4 = 4`, `i=4`
    *   `s.charAt(4)`\='2' → `num = 4*10 + 2 = 42`, `i=5`
*   `result = -1 * 42 = -42` → printed `-42`

**Note:** This code omits overflow checks for simplicity. For production, add Integer.MAX/MIN guarding.

* * *

19) Longest palindromic substring (center expansion)
----------------------------------------------------

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

**Steps / trace (key iterations)**

*   i=0: expand(0,0) gives "b" len=1; expand(0,1) gives 0 → max len=1 → start=0,end=0
*   i=1: expand(1,1) compares 'a' around center, also 'b' vs 'b' at indices 0 &2? s\[0\]=='b', s\[2\]=='b' so expands → len=3 ("bab") → update start=0,end=2
*   i=2,... ultimately longest found length 3 → substring(0,3) `"bab"` (or `"aba"` depending on choices)

**Explanation:** Expand around centers yields O(n²) worst-case but simple to implement.

_(In a real Java file, `expand` should be declared `private static int expand(...)` in same class.)_

* * *

20) Check if two strings are isomorphic
---------------------------------------

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

**Steps / trace for `"egg"` vs `"add"`**

*   i=0: cs='e'(101), ct='a'(97); mapS\['e'\]=0,mapT\['a'\]=0 → set mapS\['e'\]=98, mapT\['a'\]=102.
*   i=1: cs='g', ct='d'; mapS\['g'\]=0,mapT\['d'\]=0 → set mapS\['g'\]=101, mapT\['d'\]=103.
*   i=2: cs='g', ct='d'; mapS\['g'\]==101 and ct+1==101 → consistent → return true

**For `"foo"` vs `"bar"`** trace will detect inconsistency at second 'o' mapping to 'r' vs 'a' and return false.

**Explanation:** Two maps ensure one-to-one mapping.

* * *

### Final notes & practice suggestions

*   Try re-implementing each solution without looking, then step through with a debugger or print intermediate variable values to build intuition.
*   For Unicode-safe solutions (instead of 256 arrays) use `Map<Character, Integer>` or `HashMap` and be mindful of surrogate pairs when working with `char`.
*   For heavier tasks (like longest palindrome) try different inputs and manually trace indices to see how `start` and `end` move.

If you want, I can:

*   produce these as a single Java file with `main` and each exercise in separate methods (so you can run them), or
*   expand any exercise with richer tracing (show variable values per iteration in a table), or
*   create a printable PDF or worksheet with blanks for you to fill before revealing answers.

Which follow-up would you like?

## Prompt:
Sring + Arrays mixed?

## Response:
Ah! You want exercises where **strings and arrays are combined**, so you practice both concepts together — like manipulating strings using arrays, converting between them, splitting strings into arrays, counting, mapping, etc. I can give a **progressive set of exercises** showing how strings and arrays interact. Here’s a list of **10 exercises** (starting easy → harder), with step-by-step solutions and variable traces:

* * *

1) Convert String to char array
-------------------------------

**Problem:** Convert `"hello"` to a char array and print each character.

```java
String s = "hello";
char[] arr = s.toCharArray();
for (int i = 0; i < arr.length; i++) {
    System.out.println(arr[i]);
}
```

**Trace:**

*   `s = "hello"`
*   `arr = ['h','e','l','l','o']`
*   Prints: h e l l o

**Explanation:** `toCharArray()` lets you treat string as an array of chars.

* * *

2) Convert String to array of words
-----------------------------------

**Problem:** Split `"I love Java"` into words.

```java
String s = "I love Java";
String[] words = s.split(" ");
for (String w : words) System.out.println(w);
```

**Trace:**

*   `words = ["I","love","Java"]`
*   Prints: I, love, Java

* * *

3) Reverse a string using a char array
--------------------------------------

```java
String s = "abcd";
char[] arr = s.toCharArray();
for (int i = 0, j = arr.length-1; i < j; i++, j--) {
    char temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}
String rev = new String(arr);
System.out.println(rev);
```

**Trace:**

*   arr=\['a','b','c','d'\]
*   swap: i=0,j=3 → \['d','b','c','a'\]
*   swap: i=1,j=2 → \['d','c','b','a'\] → `"dcba"`

* * *

4) Count word frequency using array
-----------------------------------

**Problem:** `"apple banana apple"` → count occurrences using array and split.

```java
String s = "apple banana apple";
String[] words = s.split(" ");
java.util.Map<String,Integer> freq = new java.util.HashMap<>();
for(String w: words) {
    freq.put(w, freq.getOrDefault(w,0)+1);
}
System.out.println(freq);
```

**Trace:**

*   words = \["apple","banana","apple"\]
*   freq after first word → {"apple":1}
*   after "banana" → {"apple":1,"banana":1}
*   after second "apple" → {"apple":2,"banana":1}

* * *

5) Reverse each word in a sentence
----------------------------------

```java
String s = "I love Java";
String[] words = s.split(" ");
for (int i = 0; i < words.length; i++) {
    char[] arr = words[i].toCharArray();
    for (int l = 0, r = arr.length-1; l < r; l++, r--) {
        char temp = arr[l]; arr[l]=arr[r]; arr[r]=temp;
    }
    words[i] = new String(arr);
}
String res = String.join(" ", words);
System.out.println(res);
```

**Trace:**

*   words = \["I","love","Java"\]
*   reverse each: \["I","evol","avaJ"\] → `"I evol avaJ"`

* * *

6) Find longest word in a sentence
----------------------------------

```java
String s = "I love programming";
String[] words = s.split(" ");
String longest = "";
for (String w : words) if (w.length() > longest.length()) longest = w;
System.out.println(longest);
```

**Trace:**

*   words = \["I","love","programming"\]
*   longest → "programming"

* * *

7) Remove duplicate characters using array
------------------------------------------

```java
String s = "banana";
boolean[] seen = new boolean[256];
char[] arr = s.toCharArray();
StringBuilder sb = new StringBuilder();
for (char c : arr) {
    if (!seen[c]) { sb.append(c); seen[c] = true; }
}
System.out.println(sb.toString());
```

**Trace:**

*   arr = \['b','a','n','a','n','a'\]
*   result → `"ban"`

* * *

8) Sort words in a sentence alphabetically
------------------------------------------

```java
String s = "java apple banana";
String[] words = s.split(" ");
java.util.Arrays.sort(words);
String res = String.join(" ", words);
System.out.println(res);
```

**Trace:**

*   words=\["java","apple","banana"\]
*   sorted → \["apple","banana","java"\] → `"apple banana java"`

* * *

9) Count vowels in each word
----------------------------

```java
String s = "hello world";
String[] words = s.split(" ");
for (String w : words) {
    int v=0;
    for (char c : w.toCharArray()) if ("aeiouAEIOU".indexOf(c)>=0) v++;
    System.out.println(w + ": " + v);
}
```

**Trace:**

*   "hello": e,o → 2
*   "world": o → 1

* * *

10) Convert 2D array of characters to strings
---------------------------------------------

```java
char[][] arr = {{'h','i'},{'b','y','e'}};
for (char[] row : arr) {
    String s = new String(row);
    System.out.println(s);
}
```

**Trace:**

*   row1=\['h','i'\] → "hi"
*   row2=\['b','y','e'\] → "bye"

* * *

✅ These exercises gradually mix **strings + arrays**, including `char[]`, `String[]`, and 2D arrays. You can practice indexing, loops, split/join, and mapping.

If you want, I can **make a full 20-exercise series mixing strings + arrays + advanced operations** (like palindrome check per word, word frequency matrix, string rotation, etc.) with **full step-by-step variable tables** for tracing.

Do you want me to do that next?

## Prompt:
"I want to practice [ReGEx] in [java]. Can you give me [20] exercises that start very easy and gradually become harder? I want each exercise to be solved step by step with explanations, and I want to see how variable values change at each step if applicable.

## Response:
Absolutely! Let’s create a **progressive set of 20 Java regex exercises**, starting from very easy and gradually becoming more challenging. Each exercise will include:

*   **Problem statement**
*   **Java code**
*   **Step-by-step explanation**
*   **Variable/trace visualization**

* * *

**Java Regex Exercises (20)**
=============================

* * *

**1) Match a fixed word**
-------------------------

**Problem:** Check if a string equals `"hello"`.

```java
String s = "hello";
boolean matches = s.matches("hello");
System.out.println(matches);
```

**Trace:**

*   `s = "hello"`
*   `"hello".matches("hello")` → true
*   prints: `true`

**Explanation:** `matches` checks full string match.

* * *

**2) Match any single character**
---------------------------------

**Problem:** Check if string `"a"` is any character.

```java
String s = "a";
boolean matches = s.matches(".");
System.out.println(matches);
```

*   `.` matches **any single character**
*   `s="a"` → matches → true

* * *

**3) Match a digit**
--------------------

**Problem:** Check if `"7"` is a digit.

```java
String s = "7";
boolean matches = s.matches("\\d");
System.out.println(matches);
```

*   `\\d` matches `[0-9]`
*   `"7"` → true

* * *

**4) Match a word character**
-----------------------------

**Problem:** `"a"` or `"5"` or `"_"` → word character

```java
String s = "_";
boolean matches = s.matches("\\w");
System.out.println(matches);
```

*   `\\w` = `[a-zA-Z0-9_]` → true

* * *

**5) Match multiple digits**
----------------------------

**Problem:** `"12345"` → only digits

```java
String s = "12345";
boolean matches = s.matches("\\d+");
System.out.println(matches);
```

*   `\\d+` = one or more digits
*   `"12345"` → matches → true

* * *

**6) Match optional character**
-------------------------------

**Problem:** `"color"` or `"colour"`

```java
String s = "colour";
boolean matches = s.matches("colou?r");
System.out.println(matches);
```

*   `u?` → zero or one occurrence
*   `"colour"` → true, `"color"` → true

* * *

**7) Match beginning and end**
------------------------------

**Problem:** `"java123"` starts with `"java"`

```java
String s = "java123";
boolean matches = s.matches("^java.*");
System.out.println(matches);
```

*   `^java` → start with java
*   `.*` → any characters after
*   `"java123"` → true

* * *

**8) Extract numbers from string**
----------------------------------

**Problem:** `"abc123xyz"` → extract `"123"`

```java
String s = "abc123xyz";
java.util.regex.Matcher m = java.util.regex.Pattern.compile("\\d+").matcher(s);
if (m.find()) System.out.println(m.group());
```

**Trace:**

*   `\\d+` → matches one or more digits
*   m.find() → finds `"123"` → printed `"123"`

* * *

**9) Replace digits with `#`**
------------------------------

```java
String s = "Phone: 123-456";
String replaced = s.replaceAll("\\d", "#");
System.out.println(replaced);
```

**Trace:**

*   `\\d` → each digit replaced → `"Phone: ###-###"`

* * *

**10) Split string by digits**
------------------------------

```java
String s = "apple1banana2cherry";
String[] parts = s.split("\\d");
System.out.println(java.util.Arrays.toString(parts));
```

**Trace:**

*   split at digits → \["apple", "banana", "cherry"\]

* * *

**11) Match email (basic)**
---------------------------

```java
String s = "abc@example.com";
boolean matches = s.matches("\\w+@\\w+\\.\\w+");
System.out.println(matches);
```

*   `\\w+` → letters/digits/underscore
*   `@` → literal
*   `.` → literal dot (escaped as `\\.`)
*   `"abc@example.com"` → true

* * *

**12) Match phone number**
--------------------------

```java
String s = "123-456-7890";
boolean matches = s.matches("\\d{3}-\\d{3}-\\d{4}");
System.out.println(matches);
```

*   `\\d{3}` → exactly 3 digits
*   `"123-456-7890"` → true

* * *

**13) Validate simple date**
----------------------------

```java
String s = "2025-12-04";
boolean matches = s.matches("\\d{4}-\\d{2}-\\d{2}");
System.out.println(matches);
```

*   matches format `YYYY-MM-DD` → true

* * *

**14) Find all words**
----------------------

```java
String s = "Hello Java Regex";
java.util.regex.Matcher m = java.util.regex.Pattern.compile("\\w+").matcher(s);
while (m.find()) System.out.println(m.group());
```

*   `\\w+` → words
*   prints: `Hello`, `Java`, `Regex`

* * *

**15) Extract all numbers from text**
-------------------------------------

```java
String s = "I have 2 apples and 10 bananas";
java.util.regex.Matcher m = java.util.regex.Pattern.compile("\\d+").matcher(s);
while (m.find()) System.out.println(m.group());
```

*   prints: 2, 10

* * *

**16) Validate IP address (basic)**
-----------------------------------

```java
String ip = "192.168.1.1";
boolean matches = ip.matches("(\\d{1,3}\\.){3}\\d{1,3}");
System.out.println(matches);
```

*   `(\\d{1,3}\\.){3}` → three groups of 1-3 digits + dot
*   `\\d{1,3}` → last segment
*   `"192.168.1.1"` → true

* * *

**17) Match repeated words**
----------------------------

```java
String s = "hi hi hello hello";
java.util.regex.Matcher m = java.util.regex.Pattern.compile("\\b(\\w+)\\s+\\1\\b").matcher(s);
while (m.find()) System.out.println(m.group());
```

*   `(\\w+)` → capture word
*   `\\1` → same word repeated
*   prints: `hi hi`, `hello hello`

* * *

**18) Extract hashtags**
------------------------

```java
String s = "I love #java and #regex";
java.util.regex.Matcher m = java.util.regex.Pattern.compile("#\\w+").matcher(s);
while (m.find()) System.out.println(m.group());
```

*   prints: `#java`, `#regex`

* * *

**19) Split by multiple separators**
------------------------------------

```java
String s = "apple,banana;cherry|date";
String[] parts = s.split("[,;|]");
System.out.println(java.util.Arrays.toString(parts));
```

*   `[ ,;| ]` → split by any of the characters
*   prints: \["apple","banana","cherry","date"\]

* * *

**20) Validate strong password**
--------------------------------

**Criteria:** At least 8 chars, one uppercase, one lowercase, one digit, one special char

```java
String pw = "Abc123@!";
boolean matches = pw.matches("(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).{8,}");
System.out.println(matches);
```

*   `(?=.*[0-9])` → at least one digit
*   `(?=.*[a-z])` → one lowercase
*   `(?=.*[A-Z])` → one uppercase
*   `(?=.*[@#$%^&+=])` → one special char
*   `.{8,}` → min 8 characters
*   `"Abc123@!"` → true

* * *

✅ These 20 exercises gradually introduce:

*   Matching literals & meta-characters
*   Quantifiers (`+`, `*`, `{n,m}`, `?`)
*   Character classes (`\\d`, `\\w`)
*   Anchors (`^`, `$`)
*   Groups & backreferences
*   Practical patterns (email, phone, date, IP, password)

* * *

If you want, I can **make a fully worked Java file** with **all 20 exercises**, where **every variable is printed at each step**, so you can **see exactly how matches/groups change** — kind of like a debug trace table.

Do you want me to do that next?

## Prompt:
yess

## Response:
Perfect! I can make a **full Java program** containing all 20 regex exercises, with **step-by-step debug-style prints**, showing:

*   Variable values at key steps
*   Regex matches and groups
*   Arrays/collections when multiple matches are found

Here’s a **complete runnable Java file**:

```java
import java.util.regex.*;
import java.util.*;

public class RegexExercisesDebug {
    public static void main(String[] args) {
        System.out.println("=== Exercise 1: Match fixed word ===");
        String s1 = "hello";
        boolean m1 = s1.matches("hello");
        System.out.println("s1 = " + s1 + ", matches(\"hello\") = " + m1);
        
        System.out.println("\n=== Exercise 2: Match any single character ===");
        String s2 = "a";
        boolean m2 = s2.matches(".");
        System.out.println("s2 = " + s2 + ", matches(\".\") = " + m2);
        
        System.out.println("\n=== Exercise 3: Match a digit ===");
        String s3 = "7";
        boolean m3 = s3.matches("\\d");
        System.out.println("s3 = " + s3 + ", matches(\"\\\\d\") = " + m3);
        
        System.out.println("\n=== Exercise 4: Match a word character ===");
        String s4 = "_";
        boolean m4 = s4.matches("\\w");
        System.out.println("s4 = " + s4 + ", matches(\"\\\\w\") = " + m4);
        
        System.out.println("\n=== Exercise 5: Match multiple digits ===");
        String s5 = "12345";
        boolean m5 = s5.matches("\\d+");
        System.out.println("s5 = " + s5 + ", matches(\"\\\\d+\") = " + m5);
        
        System.out.println("\n=== Exercise 6: Optional character ===");
        String s6 = "colour";
        boolean m6 = s6.matches("colou?r");
        System.out.println("s6 = " + s6 + ", matches(\"colou?r\") = " + m6);
        
        System.out.println("\n=== Exercise 7: Starts with java ===");
        String s7 = "java123";
        boolean m7 = s7.matches("^java.*");
        System.out.println("s7 = " + s7 + ", matches(\"^java.*\") = " + m7);
        
        System.out.println("\n=== Exercise 8: Extract numbers ===");
        String s8 = "abc123xyz";
        Pattern p8 = Pattern.compile("\\d+");
        Matcher mt8 = p8.matcher(s8);
        while(mt8.find()) {
            System.out.println("Found number: " + mt8.group());
        }
        
        System.out.println("\n=== Exercise 9: Replace digits with # ===");
        String s9 = "Phone: 123-456";
        String replaced9 = s9.replaceAll("\\d", "#");
        System.out.println("Before: " + s9 + ", After: " + replaced9);
        
        System.out.println("\n=== Exercise 10: Split by digits ===");
        String s10 = "apple1banana2cherry";
        String[] parts10 = s10.split("\\d");
        System.out.println("s10 = " + s10);
        System.out.println("Split parts: " + Arrays.toString(parts10));
        
        System.out.println("\n=== Exercise 11: Basic email match ===");
        String s11 = "abc@example.com";
        boolean m11 = s11.matches("\\w+@\\w+\\.\\w+");
        System.out.println("s11 = " + s11 + ", matches email pattern = " + m11);
        
        System.out.println("\n=== Exercise 12: Phone number ===");
        String s12 = "123-456-7890";
        boolean m12 = s12.matches("\\d{3}-\\d{3}-\\d{4}");
        System.out.println("s12 = " + s12 + ", matches pattern = " + m12);
        
        System.out.println("\n=== Exercise 13: Simple date YYYY-MM-DD ===");
        String s13 = "2025-12-04";
        boolean m13 = s13.matches("\\d{4}-\\d{2}-\\d{2}");
        System.out.println("s13 = " + s13 + ", matches date pattern = " + m13);
        
        System.out.println("\n=== Exercise 14: Find all words ===");
        String s14 = "Hello Java Regex";
        Pattern p14 = Pattern.compile("\\w+");
        Matcher mt14 = p14.matcher(s14);
        while(mt14.find()) {
            System.out.println("Word found: " + mt14.group());
        }
        
        System.out.println("\n=== Exercise 15: Extract all numbers ===");
        String s15 = "I have 2 apples and 10 bananas";
        Matcher mt15 = Pattern.compile("\\d+").matcher(s15);
        while(mt15.find()) System.out.println("Number: " + mt15.group());
        
        System.out.println("\n=== Exercise 16: Validate IP address ===");
        String ip16 = "192.168.1.1";
        boolean m16 = ip16.matches("(\\d{1,3}\\.){3}\\d{1,3}");
        System.out.println("IP = " + ip16 + ", matches = " + m16);
        
        System.out.println("\n=== Exercise 17: Repeated words ===");
        String s17 = "hi hi hello hello";
        Pattern p17 = Pattern.compile("\\b(\\w+)\\s+\\1\\b");
        Matcher mt17 = p17.matcher(s17);
        while(mt17.find()) System.out.println("Repeated: " + mt17.group());
        
        System.out.println("\n=== Exercise 18: Extract hashtags ===");
        String s18 = "I love #java and #regex";
        Matcher mt18 = Pattern.compile("#\\w+").matcher(s18);
        while(mt18.find()) System.out.println("Hashtag: " + mt18.group());
        
        System.out.println("\n=== Exercise 19: Split by multiple separators ===");
        String s19 = "apple,banana;cherry|date";
        String[] parts19 = s19.split("[,;|]");
        System.out.println("s19 = " + s19);
        System.out.println("Split: " + Arrays.toString(parts19));
        
        System.out.println("\n=== Exercise 20: Strong password ===");
        String pw20 = "Abc123@!";
        boolean m20 = pw20.matches("(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).{8,}");
        System.out.println("Password = " + pw20 + ", strong? = " + m20);
    }
}
```

* * *

### ✅ Features of this file

1.  Every exercise prints **inputs, outputs, and matches**.
2.  Exercises 8, 14, 15, 17, 18 show **all matches with `Matcher`**, like a debug trace.
3.  Arrays/collections printed with `Arrays.toString()` to **see variable contents**.
4.  Covers **simple → advanced regex patterns**.

* * *

If you want, I can make an **enhanced version** where **every exercise prints step-by-step variable table** like:

| Step | Variable | Value | Explanation |

This is super useful for **learning regex visually**.

Do you want me to do that next?



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)