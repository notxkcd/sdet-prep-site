---
title: "Learn JS Before TS"
date: 2026-01-31
draft: false
---

## Prompt:
I'm planning to learn TypeScript for playwright or test automation, so should I learn JavaScript first, then learn TypeScript, or TypeScript is just enough?

## Response:
Short answer: **You _can_ start directly with TypeScript**, but **knowing basic JavaScript fundamentals first will make your learning smoother and faster.**

* * *

📌 Why JavaScript first helps
-----------------------------

TypeScript is built **on top of JavaScript**, so everything in JS still applies.  
Without JS fundamentals, TS might feel confusing because you’ll struggle with:

| Concept | Needed in JS? | Needed in TS? | Why it matters in testing |
| --- | --- | --- | --- |
| Variables, loops, functions | ✔ | ✔ | Writing test logic |
| Promises & async/await | ✔ | ✔ | Handling waits, navigation, timeouts |
| Callbacks & events | ✔ | ✔ | Browser interactions |
| Classes/objects | ✔ | ✔ | Better test structure & POM |
| Types, interfaces | ✖ | ✔ | Writing maintainable, scalable test code |
| Generics & advanced types | ✖ | ✔ | Useful in larger automation frameworks |

If you learn TypeScript without knowing JS, you’ll learn both at the same time — possible, but slower.

* * *

Recommended Learning Path
-------------------------

### If you want a **smooth progressive path**

1.  Learn **JavaScript basics (ES6)**
    *   variables (`let`, `const`)
    *   functions
    *   arrays & loops
    *   objects
    *   **async/await**
2.  Move to **TypeScript**
3.  Then **Playwright + Test Automation**

### If you want **fast track (minimum JS first, then TS)**

⚡ Do **1 week JavaScript fundamentals**, then jump into **TypeScript + Playwright** together.

* * *

Practical Timeline for Automation Goal
--------------------------------------

| Stage | Duration | Outcome |
| --- | --- | --- |
| Learn JavaScript basics | 5–10 days | Enough to read/write basic code |
| Learn TypeScript fundamentals | 1–2 weeks | Interfaces, types, classes |
| Learn Playwright | 2–3 weeks | Automate UI tests |
| Build Automation Framework | 3–6 weeks | POM, reporting, CI, fixtures |

* * *

In simple words
---------------

If your main goal is **Playwright automation**, then:

> 🔥 Learn **basic JavaScript first**, then switch to **TypeScript**.  
> You don't need to master JS deeply — just fundamentals.

* * *

## Prompt:
Teach me objects in js . No BS straightforward point explanation needed

## Response:
Understood. Straight, clean explanations only.

* * *

📌 **JavaScript Objects — Quick & Clear**
=========================================

### 1\. What is an object?

A collection of **key-value pairs**.

```js
const user = {
  name: "Shahid",
  age: 15
};
```

### 2\. Access values

```js
user.name
user["age"]
```

### 3\. Add / Update value

```js
user.city = "Chennai";
user.age = 16; // update
```

### 4\. Delete property

```js
delete user.city;
```

### 5\. Methods (functions inside objects)

```js
const user = {
  name: "Shahid",
  greet() {
    return "Hello " + this.name;
  }
};

user.greet(); // "Hello Shahid"
```

### 6\. `this` inside object

Refers to **object itself**.

```js
const car = {
  brand: "BMW",
  info() {
    console.log(this.brand);
  }
};

car.info(); // BMW
```

### 7\. Object inside object (nested)

```js
const obj = {
  person: {
    name: "Ali"
  }
};

obj.person.name;
```

### 8\. Loop through object keys

```js
for (let key in user) {
  console.log(key, user[key]);
}
```

### 9\. Get all keys/values

```js
Object.keys(user);
Object.values(user);
Object.entries(user);
```

### 10\. Spread & clone object

```js
const copy = { ...user };
```

### 11\. Destructuring (extract values)

```js
const { name, age } = user;
```

### 12\. Check if key exists

```js
"user" in window;         // generic example
"name" in user;           // true
user.hasOwnProperty("age"); // true
```

* * *

## Prompt:
Yess a bunch of 16 exercises gradually improve and never forget it any

## Response:
Great — here are **16 exercises**, starting super easy → gradually advanced.  
Do them **by typing**, not just reading.

* * *

🧠 **Objects Mastery Exercises (1 → 16 difficulty increases)**
==============================================================

### **Level 1 — Basics**

1.  Create an object `student` with `name`, `age`, `grade`.
2.  Access and print each property of the object using `.` operator.
3.  Add a new property `school` to `student`.
4.  Update the `grade` to something new.
5.  Delete the `school` property.

* * *

### **Level 2 — Methods & this**

6.  Add a method `introduce()` inside `student` that prints  
    `"My name is ___ and I'm ___ years old."` using `this`.
7.  Create an object `calculator` with methods: `add(a,b)` and `multiply(a,b)`.

* * *

### **Level 3 — Nested & loops**

8.  Create an object `person` with `name`, `age`, and an address object `{city, country}`.  
    Print `country`.
9.  Loop through `person` using `for...in` and print key + value.

* * *

### **Level 4 — Built-in object methods**

10.  Use `Object.keys(person)` and print the result.
11.  Use `Object.values(person)` and print the result.
12.  Use `Object.entries(person)` and print key:value pairs.

* * *

### **Level 5 — Copying & merging**

13.  Create a clone of `person` using `{...person}`. Modify the clone; original must not change.
14.  Merge two objects:

```js
const a = {x:1, y:2};
const b = {y:5, z:3};
```

Result should be `{x:1, y:5, z:3}` (y overrides).

* * *

### **Level 6 — Destructuring & advanced**

15.  From object

```js
const user = { name:"Shahid", age:15, favLang:"JS" };
```

Extract `name` and `favLang` using **destructuring**.

16.  **INTERVIEW-STYLE QUESTION**  
    Create an array of objects:

```js
const users = [
  {name:"A", age:12},
  {name:"B", age:17},
  {name:"C", age:15}
];
```

Write code to **print names of users whose age ≥ 15**.

* * *

## Prompt:
Yes with amswers

## Response:
Here are **all 16 exercises with clean, no-BS answers**.  
Read → Type → Run → Understand. That’s how you never forget it.

* * *

✅ **Answers**
=============

* * *

### **1\. Create student object**

```js
const student = {
  name: "Shahid",
  age: 15,
  grade: "A"
};
```

### **2\. Access & print**

```js
console.log(student.name);
console.log(student.age);
console.log(student.grade);
```

### **3\. Add new property**

```js
student.school = "ABC School";
```

### **4\. Update existing property**

```js
student.grade = "A+";
```

### **5\. Delete property**

```js
delete student.school;
```

* * *

### **6\. Add method with `this`**

```js
student.introduce = function() {
  console.log(`My name is ${this.name} and I'm ${this.age} years old.`);
};

student.introduce();
```

* * *

### **7\. Calculator object**

```js
const calculator = {
  add(a, b) { return a + b; },
  multiply(a, b) { return a * b; }
};

console.log(calculator.add(2, 3));
console.log(calculator.multiply(4, 5));
```

* * *

### **8\. Nested object**

```js
const person = {
  name: "Ali",
  age: 20,
  address: {
    city: "Mumbai",
    country: "India"
  }
};

console.log(person.address.country);
```

* * *

### **9\. Loop through object**

```js
for (let key in person) {
  console.log(key, person[key]);
}
```

* * *

### **10\. Object.keys**

```js
console.log(Object.keys(person));
```

### **11\. Object.values**

```js
console.log(Object.values(person));
```

### **12\. Object.entries**

```js
console.log(Object.entries(person));
```

* * *

### **13\. Clone object using spread**

```js
const clone = { ...person };
clone.name = "Changed"; // original won't change

console.log(person.name); // Ali
console.log(clone.name);  // Changed
```

* * *

### **14\. Merge objects**

```js
const a = { x:1, y:2 };
const b = { y:5, z:3 };

const merged = { ...a, ...b };
console.log(merged); // {x:1, y:5, z:3}
```

* * *

### **15\. Destructuring**

```js
const user = { name:"Shahid", age:15, favLang:"JS" };

const { name, favLang } = user;

console.log(name, favLang);
```

* * *

### **16\. Filter array of objects (age ≥ 15)**

```js
const users = [
  {name:"A", age:12},
  {name:"B", age:17},
  {name:"C", age:15}
];

users
  .filter(u => u.age >= 15)
  .forEach(u => console.log(u.name));
```

* * *

## Prompt:
D

## Response:
Perfect. Here are **20 mixed exercises** combining **Objects × Arrays × Functions** with increasing difficulty.  
Short, clean, practical — exactly what you need to become fluent.

* * *

🔥 **20 Practice Exercises (Mixed)**
====================================

Try them **yourself first**.  
**Answers will be given only when you request.**

* * *

### **Level 1 — Warm-up**

1.  Create an array of 3 student objects with `name`, `age`.
2.  Print the name of the 2nd student.
3.  Add a new student object to the array using `.push()`.
4.  Remove the last student using `.pop()`.

* * *

### **Level 2 — Loops**

5.  Loop through all students and print `"Name: X, Age: Y"`.
6.  Count how many students are age ≥ 18.
7.  Return only the names using `.map()`.

* * *

### **Level 3 — Functions + Objects**

8.  Write a function `getAdultStudents(students)` that returns array of students age ≥ 18.
9.  Write a function `addStudent(students, studentObj)` to add a student to array.
10.  Write a function that takes a student object & prints `"Hello <name>"`.

* * *

### **Level 4 — Searching & Filtering**

11.  Given an array of objects, find a student by name using `.find()`.
12.  Remove a student by name using `.filter()`.

* * *

### **Level 5 — Sorting**

13.  Sort students by **age ascending**.
14.  Sort students by **name alphabetically**.

* * *

### **Level 6 — Reduce**

15.  Use `.reduce()` to calculate **total age of all students**.
16.  Use `.reduce()` to find **oldest student**.

* * *

### **Level 7 — Real Logic**

17.  Convert:

```js
{ name:"Ali", marks:[80, 75, 90] }
```

Write code to calculate **average marks** using reduce.

18.  Create an array:

```js
[
 {product:"Pen", price:10},
 {product:"Book", price:120},
 {product:"Pencil", price:5}
]
```

Return **total price**.

* * *

### **Level 8 — Mini Automation-style**

19.  Given array:

```js
const tests = [
 {name:"Login Test", status:"passed"},
 {name:"Signup Test", status:"failed"},
 {name:"Checkout Test", status:"passed"}
];
```

Print **all passed tests only**.

20.  From the same data, print:

```
Total tests: X
Passed: X
Failed: X
```

* * *

## Prompt:
Didn't i asked answers as well

## Response:
You're right — you asked for exercises **with answers included**, my bad.  
Here are all **20 exercises _with answers_** — straight, clean & understandable.

* * *

🚀 **Solutions**
================

(Use same example dataset for most answers)

```js
let students = [
  {name:"Arun", age:17},
  {name:"Ben", age:19},
  {name:"Cathy", age:16}
];
```

* * *

### **1\. Array of student objects**

```js
let students = [
  {name:"Arun", age:17},
  {name:"Ben", age:19},
  {name:"Cathy", age:16}
];
```

### **2\. Print name of 2nd student**

```js
console.log(students[1].name);
```

### **3\. Add a new student**

```js
students.push({name:"David", age:18});
```

### **4\. Remove last student**

```js
students.pop();
```

* * *

### **5\. Loop & print**

```js
for (let s of students) {
  console.log(`Name: ${s.name}, Age: ${s.age}`);
}
```

### **6\. Count age >= 18**

```js
let count = students.filter(s => s.age >= 18).length;
console.log(count);
```

### **7\. Return only names**

```js
let names = students.map(s => s.name);
console.log(names);
```

* * *

### **8\. Function: get adults**

```js
function getAdultStudents(arr) {
  return arr.filter(s => s.age >= 18);
}

console.log(getAdultStudents(students));
```

### **9\. Add student via function**

```js
function addStudent(arr, studentObj) {
  arr.push(studentObj);
}

addStudent(students, {name:"Esha", age:20});
console.log(students);
```

### **10\. Print hello**

```js
function greet(student) {
  console.log(`Hello ${student.name}`);
}

greet(students[0]);
```

* * *

### **11\. Find student by name**

```js
let found = students.find(s => s.name === "Ben");
console.log(found);
```

### **12\. Remove student by name**

```js
students = students.filter(s => s.name !== "Ben");
console.log(students);
```

* * *

### **13\. Sort by age asc**

```js
students.sort((a,b) => a.age - b.age);
console.log(students);
```

### **14\. Sort by name**

```js
students.sort((a,b) => a.name.localeCompare(b.name));
console.log(students);
```

* * *

### **15\. Total age using reduce**

```js
let totalAge = students.reduce((sum,s) => sum + s.age, 0);
console.log(totalAge);
```

### **16\. Oldest student using reduce**

```js
let oldest = students.reduce((max,s) => s.age>max.age ? s : max);
console.log(oldest);
```

* * *

### **17\. Average marks**

```js
const studentMarks = { name:"Ali", marks:[80,75,90] };

let avg = studentMarks.marks.reduce((a,b)=>a+b,0) / studentMarks.marks.length;
console.log(avg);
```

* * *

### **18\. Total price**

```js
const products = [
  {product:"Pen", price:10},
  {product:"Book", price:120},
  {product:"Pencil", price:5}
];

let total = products.reduce((sum,p) => sum + p.price, 0);
console.log(total);
```

* * *

### **19\. Print passed tests**

```js
const tests = [
 {name:"Login Test", status:"passed"},
 {name:"Signup Test", status:"failed"},
 {name:"Checkout Test", status:"passed"}
];

tests.filter(t => t.status==="passed")
     .forEach(t => console.log(t.name));
```

* * *

### **20\. Test summary**

```js
let totalTests = tests.length;
let passed = tests.filter(t => t.status==="passed").length;
let failed = tests.filter(t => t.status==="failed").length;

console.log(`Total tests: ${totalTests}`);
console.log(`Passed: ${passed}`);
console.log(`Failed: ${failed}`);
```

* * *

## Prompt:
Now asymc await

## Response:
Straight to the point. No fluff.  
You will learn **async/await**, **promises**, **fetch style workflow**, and get **practice + answers**.

* * *

📌 What is async/await?
=======================

*   `async` makes a function return a **promise**.
*   `await` pauses execution **until a promise is resolved**.
*   Helps write async code like it's **synchronous**.

* * *

🔥 Basic Format
===============

```js
async function func() {
  let result = await somePromise;
  console.log(result);
}
```

* * *

1\. Simple Example
==================

```js
function wait(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function run() {
  console.log("Start");
  await wait(1000);
  console.log("End after 1s");
}

run();
```

* * *

2\. Returning Values
====================

```js
function getData() {
  return new Promise(resolve => resolve("Hello"));
}

async function run() {
  let data = await getData();
  console.log(data); // "Hello"
}

run();
```

* * *

3\. Using async with fetch type (real world style)
==================================================

```js
async function fetchUsers() {
  const res = await fetch("https://jsonplaceholder.typicode.com/users");
  const data = await res.json();
  console.log(data);
}

fetchUsers();
```

* * *

4\. Error Handling (Must Know)
==============================

```js
async function run() {
  try {
    let res = await fetch("wrong-url");
    let data = await res.json();
    console.log(data);
  } catch (err) {
    console.log("Error:", err.message);
  }
}

run();
```

* * *

5\. Run multiple async tasks in parallel
========================================

```js
async function run(){
  let p1 = fetch("https://jsonplaceholder.typicode.com/todos/1");
  let p2 = fetch("https://jsonplaceholder.typicode.com/todos/2");

  const results = await Promise.all([p1,p2]);
  console.log("Both done", results);
}

run();
```

* * *

🧠 Practice Exercises (with answers below)
==========================================

Try yourself first → Then check answers.

* * *

**Exercises:**
--------------

1.  Create a function `delay(ms)` that waits given milliseconds using promise.
2.  Write async function that prints:
    ```
    Step1
    (wait 1s)
    Step2
    ```
3.  Create an async function `getNumber()` that returns number 50 after 2 seconds.
4.  Use `async/await` to fetch users from an API.
5.  Handle fetch error using `try/catch`.
6.  Run two promises simultaneously using `Promise.all`.

* * *

### **Answers**

### 1.

```js
function delay(ms){
  return new Promise(res => setTimeout(res, ms));
}
```

### 2.

```js
async function steps(){
  console.log("Step1");
  await delay(1000);
  console.log("Step2");
}
steps();
```

### 3.

```js
function getNumber(){
  return new Promise(res => setTimeout(()=>res(50),2000));
}

async function showNum(){
  let num = await getNumber();
  console.log(num);
}
showNum();
```

### 4.

```js
async function getUsers(){
  const res = await fetch("https://jsonplaceholder.typicode.com/users");
  const data = await res.json();
  console.log(data);
}
getUsers();
```

### 5.

```js
async function safeFetch(){
  try{
    const res = await fetch("wrong-url");
    const data = await res.json();
    console.log(data);
  }catch(e){
    console.log("Fetch failed:", e.message);
  }
}
safeFetch();
```

### 6.

```js
async function parallel(){
  const [u1,u2] = await Promise.all([
    fetch("https://jsonplaceholder.typicode.com/todos/1"),
    fetch("https://jsonplaceholder.typicode.com/todos/2")
  ]);
  console.log("Done", u1, u2);
}
parallel();
```

* * *

## Prompt:
A

## Response:
Nice. Now we go deeper — **Promises + chaining + real understanding**.  
Simple examples → visual understanding → then exercises with answers.

* * *

🔥 PROMISES DEEP DIVE — No BS
=============================

### A promise has 3 states:

| State | Meaning |
| --- | --- |
| `pending` | still running |
| `fulfilled` | completed successfully (`resolve`) |
| `rejected` | failed (`reject`) |

* * *

Basic Structure
===============

```js
let promise = new Promise((resolve, reject) => {
  resolve("Success");
  // or reject("Error");
});
```

* * *

`.then()`, `.catch()`, `.finally()`
===================================

```js
promise
 .then(result => console.log(result))
 .catch(error => console.log(error))
 .finally(()=> console.log("Done"));
```

* * *

🔹 Example 1 — resolve
======================

```js
const p = new Promise(res => res("OK"));

p.then(x => console.log(x)); // OK
```

* * *

🔹 Example 2 — reject
=====================

```js
const p = new Promise((res, rej)=> rej("Failed"));

p.catch(err => console.log(err)); // Failed
```

* * *

🔥 Chaining `.then()` (Important!)
==================================

```js
new Promise(res => res(2))
  .then(x => x*2)     // returns 4
  .then(x => x+5)     // returns 9
  .then(x => console.log(x)); // 9
```

Each `.then()` receives previous output.

* * *

Async/Await Equivalent
======================

```js
async function run(){
  let x = 2;
  x = x*2;
  x = x+5;
  console.log(x);
}
run();
```

Same outcome.

* * *

🔥 Promise that takes time
==========================

```js
function delay(msg, time){
  return new Promise(res => setTimeout(()=>res(msg), time));
}

delay("Hello", 1000).then(console.log);
```

* * *

🔥 Promise Chain with delay
===========================

```js
delay("Step1", 1000)
.then(x => { console.log(x); return delay("Step2",1000) })
.then(x => { console.log(x); return delay("Done",1000) })
.then(x => console.log(x));
```

* * *

🔥 Parallel Promises vs Sequential
==================================

### Sequential (one after another)

```js
await delay("A", 1000);
await delay("B", 1000);
await delay("C", 1000);
// total ~3s
```

### Parallel (same time)

```js
await Promise.all([
 delay("A",1000),
 delay("B",1000),
 delay("C",1000),
]);
// total ~1s
```

* * *

🧠 Exercises (Try first — then see answers below)
=================================================

1.  Create a promise that resolves `"Loaded"`.
2.  Create a promise that rejects `"Error"` and catch it.
3.  Chain `.then()` so numbers go: **5 → 10 → 20 → 21**
4.  Convert same chain using async/await.
5.  Make a function `getData()` return data after 2sec using promise.
6.  Chain it and print `"Done"` at end.
7.  Create two promises that finish in 2s & 3s — run in parallel.
8.  Handle both result success using `.then()`.
9.  Wrap code in async/await version.

* * *

ANSWERS ✔
=========

### 1.

```js
let p = new Promise(res => res("Loaded"));
p.then(console.log);
```

### 2.

```js
let p = new Promise((res,rej)=> rej("Error"));
p.catch(console.log);
```

### 3.

```js
new Promise(res => res(5))
 .then(x => x*2)   //10
 .then(x => x*2)   //20
 .then(x => x+1)   //21
 .then(console.log);
```

### 4.

```js
async function run(){
  let x = 5;
  x = x*2;
  x = x*2;
  x = x+1;
  console.log(x);
}
run();
```

### 5.

```js
function getData(){
  return new Promise(res=> setTimeout(()=>res("DATA"),2000));
}
```

### 6.

```js
getData()
 .then(d => { console.log(d); return "Done" })
 .then(console.log);
```

### 7 & 8.

```js
let p1 = new Promise(res=>setTimeout(()=>res("P1 done"),2000));
let p2 = new Promise(res=>setTimeout(()=>res("P2 done"),3000));

Promise.all([p1,p2]).then(console.log);
```

### 9.

```js
async function run(){
  const result = await Promise.all([p1,p2]);
  console.log(result);
}
run();
```

* * *

## Prompt:
Now teach me same way java threads

## Response:
Perfect — I'll teach **Java Threads** in the same clean, no-nonsense style as JS async/await.  
Step-by-step, short examples, then exercises with answers.

* * *

🚀 Java Threads — Quick & Clear
===============================

### What is a thread?

A **separate flow of execution** inside a program.

One program = Many threads running **in parallel**.

* * *

1\. Creating a Thread (Method 1 — extend Thread class)
======================================================

```java
class MyThread extends Thread {
    public void run() {
        System.out.println("Thread running...");
    }
}

public class Main {
    public static void main(String[] args) {
        MyThread t = new MyThread();
        t.start(); // START, not run()
    }
}
```

✔ `start()` creates a new thread → calls `run()` internally  
❌ Never call `run()` manually to start a new thread

* * *

2\. Creating a Thread (Method 2 — implement Runnable)
=====================================================

```java
class MyTask implements Runnable {
    public void run() {
        System.out.println("Runnable Thread working...");
    }
}

public class Main {
    public static void main(String[] args) {
        Thread t = new Thread(new MyTask());
        t.start();
    }
}
```

* * *

3\. Anonymous Runnable (quick method)
=====================================

```java
Thread t = new Thread(() -> {
    System.out.println("Lambda thread running");
});
t.start();
```

* * *

4\. Sleep (like delay)
======================

```java
Thread.sleep(1000); // 1 sec
```

Example:

```java
Thread t = new Thread(() -> {
    try {
        System.out.println("Start");
        Thread.sleep(1000);
        System.out.println("End after 1s");
    } catch(Exception e){}
});
t.start();
```

* * *

5\. Join (wait for thread to finish)
====================================

```java
Thread t = new Thread(() -> {
    try { Thread.sleep(2000); } catch(Exception e){}
    System.out.println("Task done");
});

t.start();
t.join(); // main waits here

System.out.println("Main continues");
```

* * *

6\. Multiple Threads
====================

```java
for(int i=1;i<=5;i++){
    final int num = i;
    new Thread(() -> System.out.println("Thread " + num)).start();
}
```

* * *

7\. Thread Priority
===================

```java
t.setPriority(Thread.MAX_PRIORITY); // highest
t.setPriority(Thread.MIN_PRIORITY); // lowest
```

* * *

8\. Synchronization (stop race problems)
========================================

When many threads share same resource.

```java
class Counter {
    int count = 0;

    synchronized void increment() {
        count++;
    }
}
```

`synchronized` ensures only **one thread** can access method at a time.

* * *

9\. ExecutorService (Modern, recommended way)
=============================================

Better than manually creating threads.

```java
import java.util.concurrent.*;

ExecutorService service = Executors.newFixedThreadPool(3);

service.submit(() -> System.out.println("Task 1"));
service.submit(() -> System.out.println("Task 2"));

service.shutdown();
```

* * *

🧠 Practice Exercises (Answers below)
=====================================

Try mentally first.

1.  Create a thread class that prints `"Hello Thread"`.
2.  Create Runnable thread using lambda.
3.  Start 3 threads printing 1–3 numbers.
4.  Make a thread sleep for 1 second.
5.  Create two threads — main waits for both using `join()`.
6.  Create shared Counter class and increment count using 5 threads.
7.  Run 5 tasks using `ExecutorService`.

* * *

✔ Answers
=========

### 1.

```java
class T extends Thread {
    public void run(){ System.out.println("Hello Thread"); }
}
new T().start();
```

### 2.

```java
new Thread(() -> System.out.println("Lambda run")).start();
```

### 3.

```java
for(int i=1;i<=3;i++){
    int x=i;
    new Thread(() -> System.out.println(x)).start();
}
```

### 4.

```java
new Thread(() -> {
    try { Thread.sleep(1000); } catch(Exception e){}
    System.out.println("Done");
}).start();
```

### 5.

```java
Thread t1 = new Thread(() -> System.out.println("T1"));
Thread t2 = new Thread(() -> System.out.println("T2"));

t1.start();
t2.start();

t1.join();
t2.join();
System.out.println("Main End");
```

### 6.

```java
class Counter {
    int count=0;
    synchronized void inc(){ count++; }
}

Counter c = new Counter();

for(int i=0;i<5;i++){
    new Thread(() -> {
        for(int j=0;j<1000;j++) c.inc();
    }).start();
}

// wait a bit or join threads
System.out.println(c.count);
```

### 7.

```java
ExecutorService ex = Executors.newFixedThreadPool(5);
for(int i=1;i<=5;i++){
    int num=i;
    ex.submit(() -> System.out.println("Task " + num));
}
ex.shutdown();
```

* * *

## Prompt:
T1

## Response:
Here is **Track T1 — Java Threads Basics** explained in the **same clean, no-nonsense style** + exercises.

* * *

**🧵 What is a Thread in Java?**
================================

A **thread is a small unit of execution**.  
Your program (process) can run **multiple threads simultaneously**.

* * *

**Two Ways to Create a Thread**
===============================

### **1) Extending `Thread` class**

```java
class MyThread extends Thread {
    public void run() {                     // runs when thread starts
        System.out.println("Thread is running...");
    }
}

public class Main {
    public static void main(String[] args) {
        MyThread t = new MyThread();
        t.start();                          // ⚠️ start() → runs in new thread
    }
}
```

* * *

### **2) Implementing `Runnable` (recommended)**

```java
class MyTask implements Runnable {
    public void run() {
        System.out.println("Task executed by thread");
    }
}

public class Main {
    public static void main(String[] args) {
        Thread t = new Thread(new MyTask());
        t.start();
    }
}
```

* * *

**start() vs run()**
====================

| Method | Behavior |
| --- | --- |
| **start()** | Creates a new thread + calls run() in parallel |
| **run()** | Just a normal method call (NO new thread) |

* * *

**Thread Sleep**
================

```java
Thread.sleep(1000);   // pauses thread for 1 sec
```

* * *

**Thread with Loop**
====================

```java
class CounterTask implements Runnable {
    public void run() {
        for(int i=1;i<=5;i++){
            System.out.println("Count: " + i);
        }
    }
}
```

* * *

**Thread Naming**
=================

```java
Thread t = new Thread(new MyTask(),"Worker-1");
t.start();
System.out.println(t.getName());
```

* * *

**Join() — wait for a thread to finish**
========================================

```java
t1.start();
t2.start();

t1.join();   // main waits until t1 finishes
t2.join();
```

* * *

🔥 **8 practice exercises (basic → medium)**
============================================

Try them. **Tell me “answers” when done.**

### **Level 1**

1.  Create a thread using `Thread` class that prints `"Hello from thread"`.
2.  Create a thread using `Runnable` interface.

* * *

### **Level 2**

3.  Create a thread that prints numbers 1 to 10 with **100ms delay**.
4.  Start **two threads at the same time**; both print `"Working..."`.

* * *

### **Level 3**

5.  Create **two threads**:
    *   Thread A prints 1→5
    *   Thread B prints A→E

Run them **without order guarantee**.

* * *

### **Level 4**

6.  Use `join()` to ensure A finishes before B starts.
7.  Print the **current thread name** inside `run()`.

* * *

### **Level 5**

8.  Create **3 threads** and print:

```
Thread-X started
Thread-X running
Thread-X finished
```

* * *

## Prompt:
A

## Response:
Great — **T2: Thread Synchronization**  
Clean explanation + small examples + exercises.

* * *

🔒 Why Synchronization?
=======================

When **multiple threads access shared data**, results become unpredictable.

Example **problem without sync**:

```java
class Counter implements Runnable {
    int count = 0;

    public void run() {
        for(int i=0; i<1000; i++)
            count++;                     // shared data → race condition
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Counter c = new Counter();

        Thread t1 = new Thread(c);
        Thread t2 = new Thread(c);

        t1.start(); t2.start();
        t1.join(); t2.join();

        System.out.println(c.count);     // often < 2000 because race
    }
}
```

Two threads update same variable → **race condition**.

* * *

⭐ Fix using `synchronized`
==========================

```java
class Counter implements Runnable {
    int count = 0;

    public synchronized void increment() {
        count++;                         // only 1 thread enters at a time
    }

    public void run() {
        for(int i = 0; i < 1000; i++)
            increment();
    }
}
```

Now result = **2000 always**.

* * *

`synchronized` can be used on:
==============================

| Use | Example |
| --- | --- |
| **Method** | `synchronized void increment()` |
| **Block** | `synchronized(this) { count++; }` |
| **Static method** | `static synchronized void f()` |
| **Sync on custom lock** | `synchronized(lockObj) { ... }` |

* * *

### **Block synchronization example**

```java
class Bank {
    private int balance = 1000;

    public void withdraw(int amt){
        synchronized(this){
            balance -= amt;
        }
    }
}
```

* * *

⚠ Without sync, expected issues:
================================

*   Wrong calculation
*   Overwriting values
*   Dirty reads
*   Inconsistent output

* * *

🔥10 Exercises (Do them — then I give answers)
==============================================

### **Easy**

1.  Create a `Counter` class & increment count 1000 times in 2 threads using `synchronized`.
2.  Sync using **block** instead of method.

### **Medium**

3.  Create a `BankAccount` class with:
    *   balance
    *   `deposit()` & `withdraw()` synchronized
4.  Simulate 2 people withdrawing money simultaneously.
5.  Add `Thread.sleep(200)` inside withdraw to force race condition.

### **Harder**

6.  Create static counter variable, update using `static synchronized`.
7.  Create a lock `Object lock = new Object()` and sync on it.
8.  Shared array: two threads push values into ArrayList safely.
9.  Create 3 threads updating shared score safely.
10.  Print:

```
Thread-1 done
Thread-2 done
Total Score = X
Correct always!
```

* * *

## Prompt:
A

## Response:
Perfect — **T3: Deadlock** (clean, simple, unforgettable)

* * *

❗ What is Deadlock?
===================

Deadlock happens when **two threads are waiting for each other to release locks**,  
so **both get stuck forever**.

* * *

🔥 Deadlock Example (classic)
=============================

```java
class A {}
class B {}

public class DeadlockDemo {
    public static void main(String[] args) {

        final A a = new A();
        final B b = new B();

        Thread t1 = new Thread(() -> {
            synchronized (a) {
                System.out.println("T1 locked A");
                try { Thread.sleep(100); } catch(Exception e) {}
                synchronized (b) {
                    System.out.println("T1 locked B");
                }
            }
        });

        Thread t2 = new Thread(() -> {
            synchronized (b) {
                System.out.println("T2 locked B");
                try { Thread.sleep(100); } catch(Exception e) {}
                synchronized (a) {
                    System.out.println("T2 locked A");
                }
            }
        });

        t1.start();
        t2.start();
    }
}
```

### **Output:**

```
T1 locked A
T2 locked B
(Program hangs forever)
```

* * *

🛠 How to Fix Deadlock?
=======================

**Rule:** Always acquire locks in the **same order**.

*   Thread 1: Lock A → Lock B
*   Thread 2: Lock A → Lock B (NOT B → A)

* * *

🧠 Practice Exercises (Answers below)
=====================================

1.  Write a program that causes a deadlock.
2.  Fix the deadlock by changing lock order.
3.  Use `tryLock()` (from `ReentrantLock`) to avoid waiting forever.

* * *

## Prompt:
T2

## Response:
Here is **Track T2 — Advanced Concurrency**  
(Locks, Atomic Variables, Volatile, ReentrantLock)

* * *

🚀 **1. ReentrantLock (Better than synchronized)**
==================================================

More flexible than `synchronized`.

```java
import java.util.concurrent.locks.*;

class Counter {
    int count = 0;
    Lock lock = new ReentrantLock();

    void increment() {
        lock.lock();
        try {
            count++;
        } finally {
            lock.unlock(); // Always unlock in finally
        }
    }
}
```

*   **Advantage:** `tryLock()` (try to lock, but don't wait forever).

* * *

🚀 **2. Atomic Variables (Fastest)**
====================================

For simple counters, use `AtomicInteger` (thread-safe without locks).

```java
import java.util.concurrent.atomic.AtomicInteger;

AtomicInteger count = new AtomicInteger(0);

count.incrementAndGet(); // ++count
count.getAndIncrement(); // count++
count.addAndGet(5);      // += 5
```

* * *

🚀 **3. Volatile Keyword**
==========================

Ensures value is read from **main memory**, not CPU cache.

```java
volatile boolean running = true;
```

Used for **flags** that one thread writes and others read.

* * *

🔥 **5 Advanced Exercises**
===========================

1.  Replace `synchronized` with `ReentrantLock` in a Counter.
2.  Use `AtomicInteger` to count thread executions.
3.  Create a thread that stops when `volatile boolean stop = true`.
4.  Use `tryLock()` to avoid deadlock (if lock busy, print "Busy" and skip).
5.  Implement a thread-safe List using `Collections.synchronizedList`.

* * *

You have mastered Threads basics + Advanced concurrency basics!
