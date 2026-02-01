---
category: "Java"
title: "Java Programming Exercises"
date: 2026-01-31
draft: false
---
category: "Java"

## Prompt:
I want to practice small programming exercises to develop my intuition and get better at tracking variables and logic flow in my head. Can you give me a set of problems starting from very easy to slightly harder, and walk me through solving them step by step? I want to see how variable values change at each step and understand the reasoning behind each solution." in java

## Response:
Nice — great goal. Below I’ll give you a sequence of 8 short Java exercises (very easy → slightly harder). For each problem you’ll get:

*   The problem statement.
*   A concise Java solution.
*   A **step-by-step trace** showing how the important variables change (line-by-line).
*   A brief explanation of the reasoning.

**Problem 1 — Add and update variables (very easy)**

**Problem:** Given `a = 5` and `b = 3`, compute `c = a + b`. Then set `a = a + 1` and `b = b * 2`. Show variable values after each statement.

```java
int a = 5;           // line 1
int b = 3;           // line 2
int c = a + b;       // line 3
a = a + 1;           // line 4
b = b * 2;           // line 5
```

**Trace:**

| Line | a | b | c |
| --- | --- | --- | --- |
| 1 | 5 | - | - |
| 2 | 5 | 3 | - |
| 3 | 5 | 3 | 8 |
| 4 | 6 | 3 | 8 |
| 5 | 6 | 6 | 8 |

---
category: "Java"

**Problem 2 — Swap two variables**

```java
int x = 10;
int y = 20;
int tmp = x;
x = y;
y = tmp;
```

**Trace:**
x=10, y=20, tmp=10 -> x=20 -> y=10.

---
category: "Java"

**Problem 3 — Factorial using loop**

```java
int n = 5;
int result = 1;
for (int i = 1; i <= n; i++) {
    result = result * i;
}
```

**Trace:**
i=1, res=1 -> i=2, res=2 -> i=3, res=6 -> i=4, res=24 -> i=5, res=120.

---
category: "Java"

**Problem 4 — Max of three values**

```java
int a=7, b=3, c=9, max=a;
if (b > max) max = b;
if (c > max) max = c;
```

**Trace:** max=7 -> check b(3)>7? No -> check c(9)>7? Yes -> max=9.

---
category: "Java"

**Problem 5 — Array Sum & Avg**

```java
int[] arr = {2, 4, 6, 8};
int sum = 0;
for(int x : arr) sum += x;
double avg = (double) sum / arr.length;
```

**Trace:** sum=0 -> 2 -> 6 -> 12 -> 20. Avg = 20/4 = 5.0.

---
category: "Java"

**Problem 6 — Count Vowels**

```java
String s = "hello";
int count = 0;
for(char c : s.toCharArray()) {
    if("aeiou".indexOf(c) != -1) count++;
}
```

**Trace:** 'h' (no), 'e' (yes, count=1), 'l' (no), 'l' (no), 'o' (yes, count=2).

---
category: "Java"

## 🔹 Level 2: 15 More Problems (Loops & Logic)

**Problem 9 — Reverse Number**
1234 -> 4321
```java
int n=1234, rev=0;
while(n>0) {
    rev = rev*10 + n%10;
    n/=10;
}
```

**Problem 10 — Count Digits**
50702 -> 5
```java
int n=50702, count=0;
while(n>0) { n/=10; count++; }
```

**Problem 12 — Palindrome Number**
121 -> true
```java
// Reverse n, then compare original == reversed
```

**Problem 14 — Find Min in Array**
```java
int min = arr[0];
for(int i=1; i<arr.length; i++) if(arr[i] < min) min = arr[i];
```

**Problem 19 — Reverse String**
```java
String s="hello", rev="";
for(int i=s.length()-1; i>=0; i--) rev+=s.charAt(i);
```

**Problem 26 — Bubble Sort (One Pass)**
Moves largest element to end.
```java
for(int i=0; i<a.length-1; i++) {
    if(a[i] > a[i+1]) swap(a, i, i+1);
}
```

---
category: "Java"

## 🔹 Level 3: Logic & Patterns (91-110)

**91. Solid Square**
```java
for(int i=0; i<n; i++) {
    for(int j=0; j<n; j++) System.out.print("*");
    System.out.println();
}
```

**92. Right Triangle**
```java
for(int i=1; i<=n; i++) {
    for(int j=1; j<=i; j++) System.out.print("*");
    System.out.println();
}
```

**96. Pyramid**
```java
for(int i=1; i<=n; i++) {
    for(int s=1; s<=n-i; s++) System.out.print(" ");
    for(int j=1; j<=2*i-1; j++) System.out.print("*");
    System.out.println();
}
```

**100. Floyd's Triangle**
```java
int num=1;
for(int i=1; i<=n; i++) {
    for(int j=1; j<=i; j++) System.out.print(num++ + " ");
    System.out.println();
}
```

---
category: "Java"

## 🔹 Level 4: Data Structures (111-130)

**111. Stack using Array**
```java
class Stack {
    int[] arr = new int[100];
    int top = -1;
    void push(int x) { arr[++top] = x; }
    int pop() { return arr[top--]; }
}
```

**112. Reverse String with Stack**
Push all chars, then pop all chars.

**113. Balanced Parentheses**
Use Stack. Push `(`, `[`, `{`. When closing `)`, check if `pop() == '('`.

**121. Queue using Array**
Needs `front` and `rear` pointers.

**124. First Non-Repeating Char**
Use `Queue` + `Map`. Add char to queue, update map count. While front of queue has count > 1, poll.

---
category: "Java"

## 🔹 Level 5: Logic & Algorithms (131-150)

**131. Sum 1 to N**
`sum += i` in loop.

**134. Prime Check**
Loop `2` to `sqrt(n)`. If `n % i == 0`, false.

**147. Count Vowels**
Iterate chars, check `aeiou`.

**148. Remove Duplicates (String)**
Use `Set` or boolean array for ASCII.

**150. String to Int (atoi)**
`res = res * 10 + (char - '0')`. Handle sign.
