# QA Interview Prep - Part 1: File IO, Threads, and Core QA Questions

This file contains the detailed interview preparation material for Java File Handling, Threading, and the initial set of 2-year experience QA questions.

## Table of Contents
- [1. Java File Handling & IO](#1-java-file-handling--io)
- [2. Java Threads & Concurrency](#2-java-threads--concurrency)
- [3. QA Automation Interview Prep (2 Years Exp)](#3-qa-automation-interview-prep-2-years-exp)

---

## 1. Java File Handling & IO

### Q: I find Java's file handling libraries confusing (File, Files, FileInputStream, etc.). Can you explain the different generations of file APIs and provide a clear mental model?

**Answer:**

You’re **100% right** — this is _the_ biggest confusion almost every Java beginner (and even intermediate devs) hits.  
Java’s standard library is _massive_, and it doesn’t help that there are a ton of classes with **similar names** (`File`, `Files`, `FileInputStream`, `FileReader`, `BufferedReader`, etc.) that all seem to “handle files,” but each does something _slightly different._

Let’s break it down so it finally _clicks_ — like a “mental map” for Java file handling 👇

#### 🗺️ The Big Picture: 3 Generations of File APIs

| Generation | Package | Main Classes | Purpose | Example |
| --- | --- | --- | --- | --- |
| **Old (Pre-Java 7)** | `java.io` | `File`, `FileInputStream`, `FileReader`, `BufferedReader`, `PrintWriter`, `ObjectInputStream`, etc. | Basic file handling (streams and readers/writers) | For small, simple file I/O |
| **New (Java 7+)** | `java.nio.file` | `Files`, `Paths`, `Path`, `FileChannel`, `StandardOpenOption`, etc. | Modern, faster, more powerful file API | Used for modern apps, large files, async I/O |
| **Hybrid Utilities** | `java.util` + `java.util.stream` | Stream + NIO integration | Combine file access with modern Java Streams | Useful for reading lines, filtering, mapping |

#### 📂 The Main Confusions Explained

| Class | Belongs to | What It Represents | Use Case | Notes |
| --- | --- | --- | --- | --- |
| `File` | `java.io` | A **file or folder path** (not actual content) | Check if file exists, delete, rename | Old-style. Use `Path` now instead. |
| `Path` | `java.nio.file` | Modern version of `File` | Better path handling, safer | Use this instead of `File` in new code |
| `Files` | `java.nio.file` | A **utility class** with static methods | Read/write entire files, copy, move, delete | Think of it like “FileUtils” |
| `FileReader` | `java.io` | Reads **characters** from a file | Reading text files (slow) | Often wrapped by `BufferedReader` |
| `BufferedReader` | `java.io` | Reads text line-by-line efficiently | `new BufferedReader(new FileReader(...))` | Better performance |
| `FileInputStream` | `java.io` | Reads **bytes** (binary data) | Reading images, PDFs, etc. | Don’t use for text |
| `FileOutputStream` | `java.io` | Writes **bytes** | Saving binary files | Paired with `FileInputStream` |
| `PrintWriter` | `java.io` | Writes **text** | Writing readable text files | Easy-to-use writer |
| `Scanner` | `java.util` | Reads **text tokens** | Quick input reading (from file or stdin) | Great for parsing |

#### 🧠 Mental Model

You can think of Java’s file handling like **layers of control:**

| Simplicity → Power |
| --- |
| `Scanner` / `PrintWriter` → Very easy |
| `BufferedReader` / `BufferedWriter` → Line-based, efficient |
| `FileInputStream` / `FileOutputStream` → Byte-level control |
| `Files` / `Path` → High-level static utilities, modern API |
| `FileChannel` → Low-level, memory-mapped I/O for big files |

#### 💡 Quick Cheatsheet

**✅ Read All Lines (Modern Way)**

```java
import java.nio.file.*;

public class ReadExample {
    public static void main(String[] args) throws Exception {
        Path path = Paths.get("data.txt");
        for (String line : Files.readAllLines(path)) {
            System.out.println(line);
        }
    }
}
```

**✅ Write to File (Modern Way)**

```java
import java.nio.file.*;
import java.util.*;

public class WriteExample {
    public static void main(String[] args) throws Exception {
        Path path = Paths.get("output.txt");
        List<String> lines = List.of("Hello", "World");
        Files.write(path, lines);
    }
}
```

**✅ Stream-based Reading**

```java
Files.lines(Paths.get("data.txt"))
     .filter(line -> line.contains("error"))
     .forEach(System.out::println);
```

#### 🧩 Rule of Thumb

| If you want to… | Use |
| --- | --- |
| Read/write small text files quickly | `Files.readAllLines` / `Files.write` |
| Read a big file efficiently | `BufferedReader` |
| Read binary data (images, etc.) | `FileInputStream` |
| Write text line by line | `BufferedWriter` or `PrintWriter` |
| Work with paths (cross-platform) | `Path`, `Paths`, `Files` |
| Do advanced stuff (async, large files) | `FileChannel` / `AsynchronousFileChannel` |

---

### Q: Which specific class should I use to read `.properties` configuration files in Java?

**Answer:**

Excellent question — this one’s **very common** and **very specific** 👏

When you’re reading a **`.properties` file** (key-value configuration file like `config.properties`),  
you should use **`java.util.Properties`**, not `FileReader`, `BufferedReader`, or `Files` directly.

#### ✅ The Correct Class: `java.util.Properties`

The `Properties` class is **made for this exact purpose** — it can:

*   Load from a file or stream
*   Retrieve values by key
*   Even store them back to a file

#### 🧾 Example: Reading a `.properties` file

**config.properties**

```
username=admin
password=secret123
timeout=30
```

**Java code:**

```java
import java.io.FileInputStream;
import java.io.IOException;
import java.util.Properties;

public class ReadProperties {
    public static void main(String[] args) throws IOException {
        Properties props = new Properties();

        try (FileInputStream fis = new FileInputStream("config.properties")) {
            props.load(fis);  // Load key=value pairs
        }

        String user = props.getProperty("username");
        String pass = props.getProperty("password");
        int timeout = Integer.parseInt(props.getProperty("timeout", "10"));

        System.out.println("Username: " + user);
        System.out.println("Password: " + pass);
        System.out.println("Timeout: " + timeout);
    }
}
```

#### ⚙️ What’s Happening Here

| Concept | What It Does |
| --- | --- |
| `Properties` | A subclass of `Hashtable` that stores key–value pairs (Strings only). |
| `load(InputStream)` | Reads `.properties` formatted text. |
| `getProperty(String key)` | Retrieves a value by key. |
| `store(OutputStream, String comments)` | Writes properties back to a file. |

#### ✅ Alternate (Modern) Way with `Files` and `Path`

If you want to use **modern APIs** instead of `FileInputStream`, you can do this:

```java
import java.nio.file.*;
import java.io.IOException;
import java.util.Properties;

public class ReadPropsModern {
    public static void main(String[] args) throws IOException {
        Properties props = new Properties();

        try (var reader = Files.newBufferedReader(Path.of("config.properties"))) {
            props.load(reader);
        }

        System.out.println(props.getProperty("username"));
    }
}
```

Same result — but this version uses `java.nio.file` (modern and cross-platform safe).

#### 🧠 In short:

| You want to... | Use |
| --- | --- |
| Read `.properties` file | ✅ `java.util.Properties.load()` |
| Write `.properties` file | ✅ `Properties.store()` |
| Handle JSON config | Use `Gson` or `Jackson` |
| Handle YAML config | Use `SnakeYAML` |

---

## 2. Java Threads & Concurrency

### Q: Can you explain Java Threads and their methods using simple, straightforward examples that are easy to remember and avoid confusion?

**Answer:**

Perfect 👏 — this is one of the _most important_ and _most confusing_ Java topics for beginners, so let’s make it **crystal clear** and **memorable forever**.  
We’ll go step-by-step, like a mini crash course.

#### 🧠 What is a Thread?

➡️ A **thread** is just a **path of execution** — like a “mini program” running inside your main program.

Your Java program **always starts with one thread** — called the **main thread**.

When you create a new thread, you’re telling Java:

> “Hey, run this piece of code _in parallel_ with the main thread.”

#### 🧩 2 Ways to Create Threads in Java

| Way | How | When to use |
| --- | --- | --- |
| ✅ **Extending `Thread` class** | Create a subclass of `Thread` and override `run()` | Simple cases |
| ✅ **Implementing `Runnable` interface** | Pass a `Runnable` object to a `Thread` | Preferred — more flexible |

#### 🧱 Way 1: Extending `Thread` class

```java
class MyThread extends Thread {
    public void run() {
        // code that runs in this thread
        for (int i = 1; i <= 5; i++) {
            System.out.println("Thread: " + i);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        MyThread t = new MyThread(); // create
        t.start(); // start the thread

        for (int i = 1; i <= 5; i++) {
            System.out.println("Main: " + i);
        }
    }
}
```

**🧠 Key point:**

*   **Never call `run()` directly.**  
    `start()` internally calls `run()` **in a new thread**.
*   If you call `run()` manually → it just runs in the same thread (no parallelism).

#### 🧱 Way 2: Implementing `Runnable`

```java
class MyTask implements Runnable {
    public void run() {
        for (int i = 1; i <= 5; i++) {
            System.out.println("Worker: " + i);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Thread t = new Thread(new MyTask());
        t.start();

        for (int i = 1; i <= 5; i++) {
            System.out.println("Main: " + i);
        }
    }
}
```

✅ This is better because:

*   You can extend another class.
*   `Runnable` is just an interface — clean separation between _task_ and _thread_.

#### 🧩 Thread Lifecycle

| State | Meaning | Trigger |
| --- | --- | --- |
| **New** | Thread created but not started | `new Thread()` |
| **Runnable** | Ready to run | After `start()` |
| **Running** | Actively executing | CPU picked it |
| **Blocked / Waiting** | Waiting for something | `sleep()`, `join()`, `wait()` |
| **Terminated** | Finished | `run()` ended or stopped |

#### ⚙️ Common Thread Methods (with examples)

| Method | Description | Example |
| --- | --- | --- |
| `start()` | Starts the thread (calls `run()` in new thread) | `t.start()` |
| `run()` | Code that runs in the thread | Override this method |
| `sleep(ms)` | Pause thread temporarily | `Thread.sleep(1000)` |
| `join()` | Wait for another thread to finish | `t.join()` |
| `setName("name")` | Set thread’s name | `t.setName("Worker")` |
| `getName()` | Get name | `t.getName()` |
| `setPriority(1-10)` | Change scheduling priority | `t.setPriority(Thread.MAX_PRIORITY)` |
| `isAlive()` | Check if thread still running | `t.isAlive()` |
| `currentThread()` | Get current running thread | `Thread.currentThread().getName()` |
| `interrupt()` | Interrupts sleeping or waiting thread | `t.interrupt()` |

#### 💡 Simple Example Showing Most Methods

```java
class Task extends Thread {
    public void run() {
        System.out.println(getName() + " started.");
        for (int i = 1; i <= 5; i++) {
            System.out.println(getName() + " → " + i);
            try {
                Thread.sleep(500); // pause for half a second
            } catch (InterruptedException e) {
                System.out.println(getName() + " was interrupted!");
            }
        }
        System.out.println(getName() + " finished.");
    }
}

public class ThreadDemo {
    public static void main(String[] args) throws InterruptedException {
        Task t1 = new Task();
        Task t2 = new Task();

        t1.setName("Worker-1");
        t2.setName("Worker-2");

        t1.start();
        t2.start();

        // Wait for both to finish
        t1.join();
        t2.join();

        System.out.println("Main thread finished after both workers.");
    }
}
```

**🧠 Explanation:**

*   `start()` → begins execution in a new thread.
*   `sleep(500)` → pauses for 0.5 sec.
*   `join()` → makes main wait for threads.
*   Each thread prints its name → you see _parallel interleaving_.

#### ⚠️ Common Mistakes to Avoid

| Mistake | What Happens |
| --- | --- |
| Calling `run()` instead of `start()` | Runs in same thread (no concurrency) |
| Not handling `InterruptedException` | Compiler error for `sleep()` or `join()` |
| Using shared variables without sync | Race conditions (unexpected behavior) |

#### 🧩 Optional — Anonymous Threads (Shortcut)

```java
new Thread(() -> {
    System.out.println("Anonymous thread running");
}).start();
```

✔️ Clean, modern Java style (lambda).

#### 🧠 How to Never Forget This

1.  **Remember the 2 ways:**  
    🔹 `extends Thread` → “I’m the thread.”  
    🔹 `implements Runnable` → “I’m the job. Thread runs me.”
2.  **Remember `start()` ≠ `run()`**  
    ➤ `start()` = start new thread  
    ➤ `run()` = normal method
3.  **Lifecycle**: New → Runnable → Running → Waiting → Dead
4.  **Important trio**:
    *   `sleep()` → pause
    *   `join()` → wait for other
    *   `interrupt()` → wake it up / stop waiting

---

## 3. QA Automation Interview Prep (2 Years Exp)

### Q: I am a Java QA Automation Tester with 2 years of experience. Can you provide 20-30 solid interview questions relevant to the Indian market, covering Core Java, Selenium, TestNG, and API testing?

**Answer:**

Perfect 👏 — since you’re a **2-year QA Automation Tester (Java + Selenium)**, most Indian interviews (especially for MNCs or service companies like TCS, Infosys, Cognizant, Accenture, Capgemini, or mid-level product firms) will test you on **hands-on automation logic**, **framework understanding**, **core Java**, and **API testing basics**.

Below is a **solid, realistic 25-question set** — these are the _actual style of questions_ asked to testers with your experience level in India 🇮🇳.

#### 💼 Core Java for Automation (10 questions)

| # | Question | What They’re Checking |
| --- | --- | --- |
| 1 | What’s the difference between `==` and `.equals()` in Java? | Understanding of object comparison |
| 2 | What are `String`, `StringBuilder`, and `StringBuffer`? When to use which? | Immutable vs mutable strings |
| 3 | Explain the difference between `ArrayList` and `LinkedList`. | Data structure choice |
| 4 | What are `HashMap` and `HashSet`? | Key-value vs unique elements |
| 5 | Explain `final`, `finally`, and `finalize`. | Keyword confusion clarity |
| 6 | What is a `static` method or variable in Java? | Memory model understanding |
| 7 | What’s the difference between `throw` and `throws`? | Exception handling clarity |
| 8 | What are `checked` and `unchecked` exceptions? | Handling in Selenium/Java |
| 9 | How do you handle synchronization in Java? (e.g., `synchronized` block) | Thread-safety understanding |
| 10 | What’s the difference between `wait()`, `sleep()`, and `notify()`? | Thread control fundamentals |

#### 🧪 Selenium & Automation Frameworks (10 questions)

| # | Question | What They’re Checking |
| --- | --- | --- |
| 11 | Difference between `findElement()` and `findElements()`? | Locator basics |
| 12 | How do you handle dynamic XPaths? | Practical locator strategy |
| 13 | What is the difference between `driver.close()` and `driver.quit()`? | Resource management |
| 14 | What are different waits in Selenium? Explain `Implicit`, `Explicit`, `Fluent`. | Sync handling |
| 15 | How do you handle alerts, frames, and multiple windows? | Practical UI handling |
| 16 | How do you take screenshots in Selenium? | Common task |
| 17 | What is Page Object Model (POM)? Why use it? | Framework design |
| 18 | What is Page Factory? Difference from POM? | Advanced structure |
| 19 | How do you handle file upload/download using Selenium? | Practical automation |
| 20 | How do you execute your tests in parallel? | TestNG / Selenium Grid knowledge |

#### 🔗 TestNG, Framework & Reporting (5 questions)

| # | Question | What They’re Checking |
| --- | --- | --- |
| 21 | What are annotations in TestNG? | Understanding of flow (`@BeforeTest`, `@AfterMethod`, etc.) |
| 22 | Difference between `@BeforeMethod` and `@BeforeTest`? | Lifecycle control |
| 23 | How do you group and prioritize tests in TestNG? | Test organization |
| 24 | How do you generate reports in TestNG? | Result management |
| 25 | How do you handle dependencies between tests? (`dependsOnMethods`) | Test flow control |

#### 🌐 API Testing (using RestAssured or Postman) (5 questions)

| # | Question | What They’re Checking |
| --- | --- | --- |
| 26 | What is the difference between `GET`, `POST`, `PUT`, and `DELETE`? | REST fundamentals |
| 27 | What’s the structure of an HTTP response? | Headers, body, status |
| 28 | How do you validate status code and response body in RestAssured? | Practical hands-on |
| 29 | How do you handle authentication (Basic, Bearer Token)? | API security awareness |
| 30 | What is JSONPath and how do you extract values using it? | Data extraction skill |

#### 💬 Bonus HR + Scenario-Based (5 bonus questions)

| # | Question | What They’re Checking |
| --- | --- | --- |
| 31 | What’s your framework structure? Explain the layers. | Understanding of architecture |
| 32 | How do you manage test data? (Excel, JSON, DB?) | Data-driven approach |
| 33 | How do you integrate Selenium tests with CI/CD (Jenkins)? | Real-world usage |
| 34 | If an element is not clickable, what’s your debugging process? | Practical problem-solving |
| 35 | How do you ensure reusability and maintainability in your framework? | Coding best practices |

#### ⚡ Pro Tip for 2-Year QA Automation Interviews

👉 **Most Indian interviews (especially L1–L2)** want you to:

*   **Write short Java code snippets** (loops, string ops, collections)
*   **Explain framework setup** (folders: `testcases/`, `pages/`, `utils/`, `drivers/`)
*   **Show clarity** — not fancy terms, just _practical understanding_

### Q: Can you also include important interview questions for Cucumber, Jenkins, and Git?

**Answer:**

Excellent 👏 — that’s exactly what most **Indian QA automation interviews** expect from someone with **~2 years of experience** — Java + Selenium + TestNG + **Cucumber + Jenkins + Git**.

Let’s extend your previous 30 questions to **40 total**, covering all these areas clearly, no fluff — just _real interview-style questions_.

#### 🥒 4️⃣ Cucumber BDD (Behavior Driven Development) (5 Questions)

| # | Question | What They’re Checking |
| --- | --- | --- |
| 26 | What is Cucumber and why use it? | BDD concept |
| 27 | What is a Feature file? What does it contain? | `Feature`, `Scenario`, `Given-When-Then` |
| 28 | What are Step Definitions? | Glue code mapping |
| 29 | What are Hooks (`@Before`, `@After`) in Cucumber? | Pre/post steps |
| 30 | How do you integrate Cucumber with TestNG or JUnit? | Runner class setup |

#### ⚙️ 5️⃣ Jenkins (CI/CD Integration) (5 Questions)

| # | Question | What They’re Checking |
| --- | --- | --- |
| 31 | What is Jenkins? | CI/CD concept |
| 32 | How do you integrate your Selenium framework with Jenkins? | Build job setup |
| 33 | How do you schedule Jenkins jobs? | Build triggers |
| 34 | How do you pass parameters (browser/env) in Jenkins? | Parameterized build |
| 35 | How do you generate reports and view them in Jenkins? | HTML reports, TestNG plugin |

#### 🌿 6️⃣ Git / Version Control (5 Questions)

| # | Question | What They’re Checking |
| --- | --- | --- |
| 36 | What is Git and why is it used? | Version control |
| 37 | Difference between `git pull` and `git fetch` | Repo sync |
| 38 | How do you create a new branch and switch to it? | `git checkout -b feature-xyz` |
| 39 | How do you resolve merge conflicts? | Practical Git knowledge |
| 40 | What is `.gitignore` used for? | Ignoring files in repo |

#### 💬 Bonus: Scenario-Based QA Questions (Indian Style)

| Question | What They’re Checking |
| --- | --- |
| If a test fails in Jenkins, what’s your debugging approach? | Practical problem-solving |
| How do you manage credentials (username/password) in automation securely? | Data management |
| What’s your folder structure in your framework? | Framework clarity |
| How do you handle test data for multiple environments? | Config design |
| How do you report test failures to developers? | Communication and tools (Jira, etc.) |

#### ⚡ Tip Sheet — What Indian Interviewers _Actually_ Expect at 2 Years

| Area | Expectation | Focus |
| --- | --- | --- |
| Java | Confident in OOPs, Collections, Exception Handling | Write small snippets |
| Selenium | Locators, Waits, Actions | Handle dynamic pages |
| TestNG | Lifecycle + parallel execution | Test structure |
| Cucumber | Feature file + glue + runner understanding | Clear link between them |
| Jenkins | Basic pipeline setup | Running automation daily/nightly |
| Git | Daily commands + merge fix | Collaboration readiness |
