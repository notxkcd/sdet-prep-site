# Java Exercises: Strings & Maps (Completed)

**User:** Mohammed Shahid (shahid.xkcd@gmail.com)  
**Status:** Completed & Refined

---

## Prompt:
"I want to practice [String+Collecion Map] in [java]. Can you give me [20] exercises that start very easy and gradually become harder? I want each exercise to be solved step by step with explanations, and I want to see how variable values change at each step if applicable.

## Response:
Absolutely! I can create **20 Java exercises combining Strings and Collections/Maps**, starting from very easy and gradually increasing in difficulty. I’ll solve each step by step and explain variable changes. Let’s go:

* * *

### **Exercise 1: Count Character Frequency**

**Problem:** Given a string, count the frequency of each character.

```java
String str = "hello";
Map<Character, Integer> freq = new HashMap<>();

for (char c : str.toCharArray()) {
    freq.put(c, freq.getOrDefault(c, 0) + 1);
}

System.out.println(freq);
```

**Step by Step:**

*   `str.toCharArray()` → `['h','e','l','l','o']`
*   Iteration 1: `'h'` → freq = `{h=1}`
*   Iteration 2: `'e'` → freq = `{h=1, e=1}`
*   Iteration 3: `'l'` → freq = `{h=1, e=1, l=1}`
*   Iteration 4: `'l'` → freq = `{h=1, e=1, l=2}`
*   Iteration 5: `'o'` → freq = `{h=1, e=1, l=2, o=1}`

* * *

### **Exercise 2: Find Most Frequent Character**

**Problem:** Find the character with the highest frequency from a string.

```java
String str = "banana";
Map<Character, Integer> freq = new HashMap<>();
for (char c : str.toCharArray()) freq.put(c, freq.getOrDefault(c, 0) + 1);

char maxChar = ' ';
int maxFreq = 0;
for (Map.Entry<Character, Integer> entry : freq.entrySet()) {
    if (entry.getValue() > maxFreq) {
        maxFreq = entry.getValue();
        maxChar = entry.getKey();
    }
}

System.out.println(maxChar + " appears " + maxFreq + " times");
```

*   `freq` → `{b=1, a=3, n=2}`
*   Max → `'a'` with 3

* * *

### **Exercise 3: Count Word Frequency**

**Problem:** Count how many times each word appears in a sentence.

```java
String sentence = "java is fun and java is easy";
Map<String, Integer> wordFreq = new HashMap<>();

for (String word : sentence.split(" ")) {
    wordFreq.put(word, wordFreq.getOrDefault(word, 0) + 1);
}

System.out.println(wordFreq);
```

*   Split → `["java","is","fun","and","java","is","easy"]`
*   Output → `{java=2, is=2, fun=1, and=1, easy=1}`

* * *

### **Exercise 4: Store Unique Words in a Set**

```java
String text = "apple orange apple banana";
Set<String> uniqueWords = new HashSet<>(Arrays.asList(text.split(" ")));
System.out.println(uniqueWords);
```

*   Split → `["apple","orange","apple","banana"]`
*   Set → `[apple, orange, banana]` (unordered)

* * *

### **Exercise 5: Convert String to List of Characters**

```java
String str = "hello";
List<Character> chars = new ArrayList<>();
for (char c : str.toCharArray()) chars.add(c);
System.out.println(chars);
```

*   `['h','e','l','l','o']` → `[h, e, l, l, o]`

* * *

### **Exercise 6: Reverse Words Using List**

```java
String sentence = "java is fun";
List<String> words = new ArrayList<>(Arrays.asList(sentence.split(" ")));
Collections.reverse(words);
System.out.println(String.join(" ", words));
```

*   Output → `"fun is java"`

* * *

### **Exercise 7: Remove Duplicate Characters**

```java
String str = "banana";
Set<Character> set = new LinkedHashSet<>();
for (char c : str.toCharArray()) set.add(c);
StringBuilder sb = new StringBuilder();
for (char c : set) sb.append(c);
System.out.println(sb);
```

*   `LinkedHashSet` preserves order → `b`, `a`, `n`
*   Output → `"ban"`

* * *

### **Exercise 8: Group Words by Length**

```java
String[] words = {"apple", "bat", "cat", "dog", "banana"};
Map<Integer, List<String>> lengthMap = new HashMap<>();
for (String word : words) {
    lengthMap.computeIfAbsent(word.length(), k -> new ArrayList<>()).add(word);
}
System.out.println(lengthMap);
```

*   Output → `{3=[bat, cat, dog], 5=[apple], 6=[banana]}`

* * *

### **Exercise 9: Find Palindrome Words**

```java
String sentence = "madam racecar apple";
List<String> palindromes = new ArrayList<>();
for (String word : sentence.split(" ")) {
    if (word.equals(new StringBuilder(word).reverse().toString())) palindromes.add(word);
}
System.out.println(palindromes);
```

*   Output → `[madam, racecar]`

* * *

### **Exercise 10: Count Vowels in a String**

```java
String str = "education";
Map<Character, Integer> vowels = new HashMap<>();
for (char c : str.toCharArray()) {
    if ("aeiou".indexOf(c) != -1) vowels.put(c, vowels.getOrDefault(c, 0) + 1);
}
System.out.println(vowels);
```

*   Output → `{e=1, u=1, a=1, i=1, o=1}`

* * *

### **Exercise 11: Map Words to Their First Letter**

```java
String[] words = {"apple","bat","ball","cat"};
Map<Character, List<String>> firstLetterMap = new HashMap<>();
for (String word : words) {
    firstLetterMap.computeIfAbsent(word.charAt(0), k -> new ArrayList<>()).add(word);
}
System.out.println(firstLetterMap);
```

*   Output → `{a=[apple], b=[bat, ball], c=[cat]}`

* * *

### **Exercise 12: Count Word Length Frequency**

```java
String[] words = {"apple","bat","ball","cat"};
Map<Integer, Integer> lengthFreq = new HashMap<>();
for (String word : words) {
    lengthFreq.put(word.length(), lengthFreq.getOrDefault(word.length(), 0) + 1);
}
System.out.println(lengthFreq);
```

*   Output → `{3=3, 5=1}`

* * *

### **Exercise 13: Most Frequent Word**

```java
String sentence = "apple bat apple ball cat bat apple";
Map<String, Integer> freq = new HashMap<>();
for (String word : sentence.split(" ")) freq.put(word, freq.getOrDefault(word, 0) + 1);

String maxWord = "";
int maxCount = 0;
for (Map.Entry<String, Integer> e : freq.entrySet()) {
    if (e.getValue() > maxCount) { maxCount = e.getValue(); maxWord = e.getKey(); }
}
System.out.println(maxWord + " -> " + maxCount);
```

*   Output → `"apple -> 3"`

* * *

### **Exercise 14: Sort Map by Value**

```java
Map<String, Integer> map = Map.of("apple",3,"bat",2,"cat",5);
map.entrySet().stream()
    .sorted(Map.Entry.<String, Integer>comparingByValue())
    .forEach(System.out::println);
```

*   Output → `bat=2, apple=3, cat=5`

* * *

### **Exercise 15: Count Substring Occurrences**

```java
String text = "java java java";
String sub = "java";
int count = 0;
int index = 0;
while ((index = text.indexOf(sub, index)) != -1) { count++; index += sub.length(); }
System.out.println(count);
```

*   Output → `3`

* * *

### **Exercise 16: Group Words by First and Last Letter**

```java
String[] words = {"apple","bat","ball","cat"};
Map<String, List<String>> map = new HashMap<>();
for (String word : words) {
    String key = "" + word.charAt(0) + word.charAt(word.length()-1);
    map.computeIfAbsent(key, k -> new ArrayList<>()).add(word);
}
System.out.println(map);
```

*   Output → `{aa=[apple], bt=[bat], bl=[ball], ct=[cat]}`

* * *

### **Exercise 17: Reverse Each Word in a String**

```java
String sentence = "java is fun";
StringBuilder sb = new StringBuilder();
for (String word : sentence.split(" ")) sb.append(new StringBuilder(word).reverse()).append(" ");
System.out.println(sb.toString().trim());
```

*   Output → `"avaj si nuf"`

* * *

### **Exercise 18: Character Position Map**

```java
String str = "banana";
Map<Character, List<Integer>> posMap = new HashMap<>();
for (int i = 0; i < str.length(); i++) {
    char c = str.charAt(i);
    posMap.computeIfAbsent(c, k -> new ArrayList<>()).add(i);
}
System.out.println(posMap);
```

*   Output → `{b=[0], a=[1, 3, 5], n=[2, 4]}`

* * *

### **Exercise 19: Find Anagrams in List**

```java
String[] words = {"bat","tab","cat"};
Map<String, List<String>> anagrams = new HashMap<>();
for (String w : words) {
    char[] arr = w.toCharArray(); Arrays.sort(arr);
    String key = new String(arr);
    anagrams.computeIfAbsent(key, k -> new ArrayList<>()).add(w);
}
System.out.println(anagrams);
```

*   Output → `{abt=[bat, tab], act=[cat]}`

* * *

### **Exercise 20: Most Common Character in Each Word**

```java
String[] words = {"apple","banana","carrot"};
Map<String, Character> mostCommon = new HashMap<>();

for (String word : words) {
    Map<Character, Integer> freq = new HashMap<>();
    for (char c : word.toCharArray()) freq.put(c, freq.getOrDefault(c,0)+1);
    char maxChar = ' '; int maxFreq = 0;
    for (Map.Entry<Character,Integer> e : freq.entrySet()) if (e.getValue() > maxFreq) { maxFreq = e.getValue(); maxChar = e.getKey(); }
    mostCommon.put(word, maxChar);
}
System.out.println(mostCommon);
```

*   Output → `{apple=p, banana=a, carrot=r}`

* * *

✅ These exercises gradually increase from **simple character counting to grouping, mapping, and analyzing words** with Maps and Collections.

* * *

## Prompt:
yes yesss

## Response:
Perfect! Let’s go **next level**: 20 exercises combining **Strings + Lists + Sets + advanced Map manipulations**, with **step-by-step visual tracking of variable values** so you can really see how data changes. I’ll make it progressively harder.

* * *

### **Exercise 1: Split String into Characters (List)**

**Problem:** Convert a string into a `List<Character>` and print each character.

```java
String str = "java";
List<Character> chars = new ArrayList<>();
for (char c : str.toCharArray()) chars.add(c);
System.out.println(chars);
```

**Step by Step (Variables Table):**

| Step | c | chars |
| --- | --- | --- |
| 1 | 'j' | \[j\] |
| 2 | 'a' | \[j, a\] |
| 3 | 'v' | \[j, a, v\] |
| 4 | 'a' | \[j, a, v, a\] |

**Output:** `[j, a, v, a]`

* * *

### **Exercise 2: Remove Duplicate Words (Set)**

```java
String sentence = "java is fun and java is easy";
Set<String> unique = new LinkedHashSet<>(Arrays.asList(sentence.split(" ")));
System.out.println(unique);
```

| Step | Word added | unique |
| --- | --- | --- |
| 1 | java | \[java\] |
| 2 | is | \[java, is\] |
| 3 | fun | \[java, is, fun\] |
| 4 | and | \[java, is, fun, and\] |
| 5 | java | \[java, is, fun, and\] |
| 6 | is | \[java, is, fun, and\] |
| 7 | easy | \[java, is, fun, and, easy\] |

**Output:** `[java, is, fun, and, easy]`

* * *

### **Exercise 3: Word Length Map**

```java
String[] words = {"apple","bat","ball","cat"};
Map<Integer, List<String>> lengthMap = new HashMap<>();
for (String w : words) lengthMap.computeIfAbsent(w.length(), k -> new ArrayList<>()).add(w);
System.out.println(lengthMap);
```

| Step | word | length | lengthMap |
| --- | --- | --- | --- |
| 1 | apple | 5 | {5=\[apple\]} |
| 2 | bat | 3 | {5=\[apple\], 3=\[bat\]} |
| 3 | ball | 4 | {5=\[apple\], 3=\[bat\], 4=\[ball\]} |
| 4 | cat | 3 | {5=\[apple\], 3=\[bat, cat\], 4=\[ball\]} |

**Output:** `{3=[bat, cat], 4=[ball], 5=[apple]}`

* * *

### **Exercise 4: Count Vowels in Words (Map)**

```java
String[] words = {"apple","banana"};
Map<String, Map<Character,Integer>> vowelMap = new HashMap<>();

for (String w : words) {
    Map<Character,Integer> freq = new HashMap<>();
    for (char c : w.toCharArray()) if ("aeiou".indexOf(c)!=-1) freq.put(c,freq.getOrDefault(c,0)+1);
    vowelMap.put(w,freq);
}
System.out.println(vowelMap);
```

**Step Table for `"apple"`:**

| c | freq |
| --- | --- |
| a | {a=1} |
| p | {a=1} |
| p | {a=1} |
| l | {a=1} |
| e | {a=1, e=1} |

**Step Table for `"banana"`:**

| c | freq |
| --- | --- |
| b | {} |
| a | {a=1} |
| n | {a=1} |
| a | {a=2} |
| n | {a=2} |
| a | {a=3} |

**Output:** `{apple={a=1, e=1}, banana={a=3}}`

* * *

### **Exercise 5: Map Words to First Letter**

```java
String[] words = {"apple","bat","ball","cat"};
Map<Character, List<String>> firstLetterMap = new HashMap<>();
for (String w : words) firstLetterMap.computeIfAbsent(w.charAt(0), k->new ArrayList<>()).add(w);
System.out.println(firstLetterMap);
```

| Step | word | firstChar | Map State |
| --- | --- | --- | --- |
| 1 | apple | a | {a=\[apple\]} |
| 2 | bat | b | {a=\[apple\], b=\[bat\]} |
| 3 | ball | b | {a=\[apple\], b=\[bat, ball\]} |
| 4 | cat | c | {a=\[apple\], b=\[bat, ball\], c=\[cat\]} |

**Output:** `{a=[apple], b=[bat, ball], c=[cat]}`

* * *

### **Exercise 6: Reverse Words Using List**

```java
String sentence = "java is fun";
List<String> words = new ArrayList<>(Arrays.asList(sentence.split(" ")));
Collections.reverse(words);
System.out.println(String.join(" ", words));
```

| Step | words |
| --- | --- |
| init | \[java, is, fun\] |
| reverse | \[fun, is, java\] |

**Output:** `"fun is java"`

* * *

### **Exercise 7: Find Longest Word**

```java
String sentence = "java is fun programming";
String[] words = sentence.split(" ");
String longest = "";
for(String w: words) if(w.length()>longest.length()) longest=w;
System.out.println(longest);
```

| Step | w | longest |
| --- | --- | --- |
| java | java | java |
| is | is | java |
| fun | fun | java |
| programming | programming | programming |

**Output:** `"programming"`

* * *

### **Exercise 8: Map Characters to Their Positions**

```java
String str = "banana";
Map<Character,List<Integer>> charPos = new HashMap<>();
for(int i=0;i<str.length();i++) {
    char c=str.charAt(i);
    charPos.computeIfAbsent(c,k->new ArrayList<>()).add(i);
}
System.out.println(charPos);
```

| i | c | charPos |
| --- | --- | --- |
| 0 | b | {b=\[0\]} |
| 1 | a | {b=\[0\], a=\[1\]} |
| 2 | n | {b=\[0\], a=\[1\], n=\[2\]} |
| 3 | a | {b=\[0\], a=\[1,3\], n=\[2\]} |
| 4 | n | {b=\[0\], a=\[1,3\], n=\[2,4\]} |
| 5 | a | {b=\[0\], a=\[1,3,5\], n=\[2,4\]} |

**Output:** `{b=[0], a=[1, 3, 5], n=[2, 4]}`

* * *

### **Exercise 9: Sort Words by Length**

```java
String[] words = {"apple","bat","ball","cat"};
List<String> list = new ArrayList<>(Arrays.asList(words));
list.sort(Comparator.comparingInt(String::length));
System.out.println(list);
```

| word | length |
| --- | --- |
| bat | 3 |
| cat | 3 |
| ball | 4 |
| apple | 5 |

**Output:** `[bat, cat, ball, apple]`

* * *

### **Exercise 10: Count Words Starting with Each Letter**

```java
String[] words = {"apple","bat","ball","cat","ant"};
Map<Character,Integer> startCount = new HashMap<>();
for(String w: words) startCount.put(w.charAt(0), startCount.getOrDefault(w.charAt(0),0)+1);
System.out.println(startCount);
```

| Step | word | Map |
| --- | --- | --- |
| apple | a | {a=1} |
| bat | b | {a=1,b=1} |
| ball | b | {a=1,b=2} |
| cat | c | {a=1,b=2,c=1} |
| ant | a | {a=2,b=2,c=1} |

**Output:** `{a=2, b=2, c=1}`
