# String replacement exercises

**User:** Mohammed Shahid (shahid.xkcd@gmail.com)  
**Created:** 12/4/2025 1:28:18  
**Updated:** 12/4/2025 1:30:22  
**Exported:** 1/31/2026 18:04:37  
**Link:** [https://chatgpt.com/c/69309656-67a0-832f-a9f1-10675bb0f1bd](https://chatgpt.com/c/69309656-67a0-832f-a9f1-10675bb0f1bd)  

## Prompt:
"I want to practice [String replacement] in [java]. Can you give me [20] exercises that start very easy and gradually become harder? I want each exercise to be solved step by step with explanations, and I want to see how variable values change at each step if applicable. After each problem, ask me to predict the result before showing the solution so I can train my intuition.

## Response:
Absolutely! Let's do a **progressive set of 20 Java exercises on String replacement**. Each exercise will start simple and gradually become more challenging. For each, I’ll explain step by step and show variable changes. I’ll **ask you to predict the result first**, so you can practice intuition.

* * *

**Exercise 1: Simple character replacement**
--------------------------------------------

**Problem:** Replace `'a'` with `'b'` in `"apple"`.

```java
String word = "apple";
String result = word.replace('a', 'b');
System.out.println(result);
```

**Step by step:**

1.  `word = "apple"`
2.  `.replace('a', 'b')` → replaces all `'a'` characters with `'b'`.

**Your turn:** What do you think `result` will be?

* * *

**Exercise 2: Replace substring**
---------------------------------

**Problem:** Replace `"cat"` with `"dog"` in `"the cat sat"`.

```java
String sentence = "the cat sat";
String result = sentence.replace("cat", "dog");
System.out.println(result);
```

**Step by step:**

1.  `sentence = "the cat sat"`
2.  `.replace("cat", "dog")` → finds `"cat"` and replaces it.

**Predict:** What is `result`?

* * *

**Exercise 3: Replace multiple occurrences**
--------------------------------------------

**Problem:** Replace `'l'` with `'x'` in `"hello world"`.

```java
String text = "hello world";
String result = text.replace('l', 'x');
System.out.println(result);
```

**Step by step:**

*   Original string: `"hello world"`
*   Replace `'l'` → every `'l'` becomes `'x'`

**Predict:** What is `result`?

* * *

**Exercise 4: No match replacement**
------------------------------------

**Problem:** Replace `'z'` with `'a'` in `"java"`.

```java
String word = "java";
String result = word.replace('z', 'a');
System.out.println(result);
```

**Step by step:**

*   `'z'` is not in `"java"`, so string stays the same.

**Predict:** What is `result`?

* * *

**Exercise 5: Replace first occurrence of substring**
-----------------------------------------------------

**Problem:** Replace only the first `"cat"` with `"dog"` in `"cat cat cat"`.

```java
String sentence = "cat cat cat";
String result = sentence.replaceFirst("cat", "dog");
System.out.println(result);
```

**Step by step:**

*   `.replaceFirst` replaces **only the first match**.

**Predict:** What is `result`?

* * *

**Exercise 6: Regex replacement**
---------------------------------

**Problem:** Replace all digits with `'*'` in `"a1b2c3"`.

```java
String str = "a1b2c3";
String result = str.replaceAll("\\d", "*");
System.out.println(result);
```

**Step by step:**

1.  `\\d` → regex for digits
2.  `.replaceAll` → replaces all matches

**Predict:** What is `result`?

* * *

**Exercise 7: Case sensitive replacement**
------------------------------------------

**Problem:** Replace `"Java"` with `"Python"` in `"I love java and Java"`.

```java
String str = "I love java and Java";
String result = str.replace("Java", "Python");
System.out.println(result);
```

**Step by step:**

*   `"Java"` (uppercase J) is replaced; `"java"` (lowercase j) is **not replaced**.

**Predict:** What is `result`?

* * *

**Exercise 8: Replace using regex for letters**
-----------------------------------------------

**Problem:** Replace all vowels with `'*'` in `"hello world"`.

```java
String str = "hello world";
String result = str.replaceAll("[aeiou]", "*");
System.out.println(result);
```

**Step by step:**

*   `[aeiou]` → matches any vowel
*   Replace all vowels with `'*'`

**Predict:** What is `result`?

* * *

**Exercise 9: Remove whitespace**
---------------------------------

**Problem:** Remove all spaces in `"I am learning Java"`.

```java
String str = "I am learning Java";
String result = str.replace(" ", "");
System.out.println(result);
```

**Step by step:**

*   Replace `" "` with empty string `""`
*   All spaces are removed

**Predict:** What is `result`?

* * *

**Exercise 10: Replace multiple characters using regex**
--------------------------------------------------------

**Problem:** Replace all digits and vowels with `'#'` in `"a1b2c3"`.

```java
String str = "a1b2c3";
String result = str.replaceAll("[aeiou0-9]", "#");
System.out.println(result);
```

**Step by step:**

*   `[aeiou0-9]` → matches vowels + digits
*   Replaced with `'#'`

**Predict:** What is `result`?

* * *

**Exercise 11: Chain replacements**
-----------------------------------

**Problem:** Replace `'a'` with `'o'`, then `'o'` with `'u'` in `"java"`.

```java
String str = "java";
String result = str.replace('a', 'o').replace('o', 'u');
System.out.println(result);
```

**Step by step:**

1.  `'a'` → `'o'` → `"jovo"`
2.  `'o'` → `'u'` → `"juvu"`

**Predict:** What is `result`?

* * *

**Exercise 12: Replace ignoring case using regex**
--------------------------------------------------

**Problem:** Replace `"java"` with `"Python"` ignoring case in `"I love JAVA and java"`.

```java
String str = "I love JAVA and java";
String result = str.replaceAll("(?i)java", "Python");
System.out.println(result);
```

**Step by step:**

*   `(?i)` → regex flag for **ignore case**
*   Both `"JAVA"` and `"java"` replaced

**Predict:** What is `result`?

* * *

**Exercise 13: Replace words with boundary check**
--------------------------------------------------

**Problem:** Replace `"cat"` with `"dog"` only as a full word in `"concatenate cat catapult"`.

```java
String str = "concatenate cat catapult";
String result = str.replaceAll("\\bcat\\b", "dog");
System.out.println(result);
```

**Step by step:**

*   `\\b` → word boundary
*   Only standalone `"cat"` replaced

**Predict:** What is `result`?

* * *

**Exercise 14: Replace digits with different length**
-----------------------------------------------------

**Problem:** Replace digits with `"X"` in `"User1234"`.

```java
String str = "User1234";
String result = str.replaceAll("\\d", "X");
System.out.println(result);
```

**Step by step:**

*   `"1234"` → each digit → `"X"`
*   Result string length stays same

**Predict:** What is `result`?

* * *

**Exercise 15: Replace multiple words**
---------------------------------------

**Problem:** Replace `"cat"` with `"dog"` and `"mouse"` with `"cheese"` in `"cat and mouse"`.

```java
String str = "cat and mouse";
String result = str.replace("cat", "dog").replace("mouse", "cheese");
System.out.println(result);
```

**Step by step:**

1.  `"cat"` → `"dog"` → `"dog and mouse"`
2.  `"mouse"` → `"cheese"` → `"dog and cheese"`

**Predict:** What is `result`?

* * *

**Exercise 16: Replace using a map (advanced)**
-----------------------------------------------

**Problem:** Replace `"apple"` → `"orange"`, `"banana"` → `"kiwi"` in `"I like apple and banana"`.

```java
String str = "I like apple and banana";
str = str.replace("apple", "orange").replace("banana", "kiwi");
System.out.println(str);
```

**Predict:** What is `str`?

* * *

**Exercise 17: Replace special characters**
-------------------------------------------

**Problem:** Replace all punctuation with `'-'` in `"Hello, world!"`.

```java
String str = "Hello, world!";
String result = str.replaceAll("\\p{Punct}", "-");
System.out.println(result);
```

**Step by step:**

*   `\\p{Punct}` → all punctuation
*   `","` → `"-"`, `"!"` → `"-"`

**Predict:** What is `result`?

* * *

**Exercise 18: Replace multiple spaces with single space**
----------------------------------------------------------

**Problem:** Replace consecutive spaces with a single space in `"I am here"`.

```java
String str = "I   am   here";
String result = str.replaceAll("\\s+", " ");
System.out.println(result);
```

**Predict:** What is `result`?

* * *

**Exercise 19: Remove all non-alphanumeric characters**
-------------------------------------------------------

**Problem:** Remove everything except letters and numbers from `"Hello! 123, World?"`.

```java
String str = "Hello! 123, World?";
String result = str.replaceAll("[^a-zA-Z0-9]", "");
System.out.println(result);
```

**Step by step:**

*   `[^a-zA-Z0-9]` → anything not a letter or number
*   Remove all matches

**Predict:** What is `result`?

* * *

**Exercise 20: Complex chain with regex and replace**
-----------------------------------------------------

**Problem:** Replace vowels with `'*'` and digits with `'#'` in `"Hello 2025 World"`.

```java
String str = "Hello 2025 World";
String result = str.replaceAll("[aeiouAEIOU]", "*").replaceAll("\\d", "#");
System.out.println(result);
```

**Predict:** What is `result`?

* * *

✅ This set gradually moves from **simple char replacement** → **regex** → **chaining and maps** → **complex replacements**.

* * *

If you want, I can **also provide a “prediction + solution table” for all 20 exercises**, where I show **your step-by-step reasoning** and the **final output** so you can compare your intuition to reality.

Do you want me to do that next?

## Prompt:
more 20 porblms with regx invvd on the same topic

## Response:
Perfect! Let’s do **another 20 Java exercises on String replacement**, this time focusing **heavily on regex (`replaceAll`, `replaceFirst`)**. Each one will increase in difficulty and involve **regex patterns, character classes, boundaries, and advanced replacement tricks**. I’ll still ask you to predict the result before showing the solution.

* * *

**Exercise 21: Replace all uppercase letters with `*`**
-------------------------------------------------------

```java
String str = "Hello World!";
String result = str.replaceAll("[A-Z]", "*");
System.out.println(result);
```

**Predict:** What will `result` be?

* * *

**Exercise 22: Replace all lowercase letters with `#`**
-------------------------------------------------------

```java
String str = "Hello World!";
String result = str.replaceAll("[a-z]", "#");
System.out.println(result);
```

**Predict:** What will `result` be?

* * *

**Exercise 23: Replace first digit only**
-----------------------------------------

```java
String str = "Room 123";
String result = str.replaceFirst("\\d", "X");
System.out.println(result);
```

**Predict:** What will `result` be?

* * *

**Exercise 24: Replace all whitespace with underscore**
-------------------------------------------------------

```java
String str = "I love Java";
String result = str.replaceAll("\\s", "_");
System.out.println(result);
```

**Predict:** What will `result` be?

* * *

**Exercise 25: Replace only the first vowel**
---------------------------------------------

```java
String str = "banana";
String result = str.replaceFirst("[aeiou]", "*");
System.out.println(result);
```

**Predict:** What will `result` be?

* * *

**Exercise 26: Replace word at the beginning**
----------------------------------------------

```java
String str = "Hello World Hello";
String result = str.replaceFirst("^Hello", "Hi");
System.out.println(result);
```

**Predict:** What will `result` be?

* * *

**Exercise 27: Replace word at the end**
----------------------------------------

```java
String str = "Hello World Hello";
String result = str.replaceFirst("Hello$", "Hi");
System.out.println(result);
```

**Predict:** What will `result` be?

* * *

**Exercise 28: Replace consecutive identical letters**
------------------------------------------------------

```java
String str = "bookkeeper";
String result = str.replaceAll("(.)\\1", "$1");
System.out.println(result);
```

**Predict:** What will `result` be?

* * *

**Exercise 29: Replace all non-digits with `*`**
------------------------------------------------

```java
String str = "a1b2c3";
String result = str.replaceAll("\\D", "*");
System.out.println(result);
```

**Predict:** What will `result` be?

* * *

**Exercise 30: Replace multiple spaces with comma**
---------------------------------------------------

```java
String str = "I   am   here";
String result = str.replaceAll("\\s+", ",");
System.out.println(result);
```

**Predict:** What will `result` be?

* * *

**Exercise 31: Replace words with specific length**
---------------------------------------------------

```java
String str = "I am here for fun";
String result = str.replaceAll("\\b\\w{2}\\b", "XX");
System.out.println(result);
```

**Predict:** What will `result` be?

* * *

**Exercise 32: Replace numbers of specific length**
---------------------------------------------------

```java
String str = "My pin is 1234 and code 567";
String result = str.replaceAll("\\b\\d{3}\\b", "###");
System.out.println(result);
```

**Predict:** What will `result` be?

* * *

**Exercise 33: Replace HTML-like tags**
---------------------------------------

```java
String str = "<div>Hello</div>";
String result = str.replaceAll("<.*?>", "");
System.out.println(result);
```

**Predict:** What will `result` be?

* * *

**Exercise 34: Remove all punctuation except `.`**
--------------------------------------------------

```java
String str = "Hello, world! How are you?";
String result = str.replaceAll("[\\p{Punct}&&[^.]]", "");
System.out.println(result);
```

**Predict:** What will `result` be?

* * *

**Exercise 35: Replace all vowels at word boundary**
----------------------------------------------------

```java
String str = "apple orange";
String result = str.replaceAll("\\b[aeiouAEIOU]", "*");
System.out.println(result);
```

**Predict:** What will `result` be?

* * *

**Exercise 36: Replace repeated whitespace with single space**
--------------------------------------------------------------

```java
String str = "This    is   Java";
String result = str.replaceAll("\\s{2,}", " ");
System.out.println(result);
```

**Predict:** What will `result` be?

* * *

**Exercise 37: Mask email address**
-----------------------------------

```java
String str = "Contact me at test@example.com";
String result = str.replaceAll("(\\w+)@(\\w+\\.\\w+)", "$1@****");
System.out.println(result);
```

**Predict:** What will `result` be?

* * *

**Exercise 38: Remove digits at start of string**
-------------------------------------------------

```java
String str = "123abc456";
String result = str.replaceFirst("^\\d+", "");
System.out.println(result);
```

**Predict:** What will `result` be?

* * *

**Exercise 39: Replace last word using lookahead**
--------------------------------------------------

```java
String str = "I like Java programming";
String result = str.replaceAll("\\w+$", "Python");
System.out.println(result);
```

**Predict:** What will `result` be?

* * *

**Exercise 40: Replace multiple patterns using regex alternation**
------------------------------------------------------------------

```java
String str = "cat dog bird";
String result = str.replaceAll("cat|dog", "pet");
System.out.println(result);
```

**Predict:** What will `result` be?

* * *

These exercises now include **regex anchors, groups, lookahead, repetition, alternation, character classes**, etc., which are all **common patterns in string replacement problems**.

* * *

If you want, I can **continue with 20 more “expert-level” regex replacement problems**, including **conditional replacements, backreferences, and dynamic replacements**, which will be really challenging and powerful for mastering Java regex.

Do you want me to prepare that next?



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)