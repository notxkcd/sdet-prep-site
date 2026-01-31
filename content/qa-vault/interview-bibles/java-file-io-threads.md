---
title: "Java File IO & Threads Mastery"
date: 2026-01-31
draft: false
---

## 1. Java File Handling & IO

### Generations of File APIs

| Generation | Package | Main Classes | Purpose |
| --- | --- | --- | --- |
| **Old (Pre-Java 7)** | `java.io` | `File`, `FileInputStream`, `FileReader`, `BufferedReader` | Basic file handling |
| **New (Java 7+)** | `java.nio.file` | `Files`, `Paths`, `Path` | Modern, faster API |
| **Hybrid Utilities** | `java.util.stream` | Stream + NIO integration | Combine file access with Streams |

### The Main Classes Explained

| Class | Purpose | Notes |
| --- | --- | --- |
| `File` | Represents a file/folder path | Old-style. Use `Path` instead. |
| `Path` | Modern version of `File` | Better path handling. |
| `Files` | Utility class with static methods | Think of it like “FileUtils”. |
| `BufferedReader` | Reads text line-by-line efficiently | Best for performance. |
| `FileInputStream` | Reads **bytes** (binary data) | Use for images, PDFs, etc. |
| `Properties` | For `.properties` files | Key-value config handler. |

### 💡 Quick Code Snippets

**Read All Lines (Modern Way)**
```java
Path path = Paths.get("data.txt");
List<String> lines = Files.readAllLines(path);
```

**Write to File**
```java
Path path = Paths.get("output.txt");
Files.write(path, List.of("Hello", "World"));
```

---

## 2. Java Threads & Concurrency

### What is a Thread?
A **thread** is just a **path of execution** — like a “mini program” running inside your main program.

### Ways to Create Threads

| Method | Implementation | Note |
| --- | --- | --- |
| **Extending `Thread`** | `class MyT extends Thread` | Simple, but less flexible. |
| **Implementing `Runnable`** | `class MyTask implements Runnable` | Preferred - allows extending other classes. |

### ⚙️ Common Thread Methods

| Method | Description |
| --- | --- |
| `start()` | Begins execution in a new thread. |
| `run()` | The actual code the thread executes. |
| `sleep(ms)` | Pauses thread temporarily. |
| `join()` | Waits for another thread to finish. |
| `synchronized` | Prevents race conditions on shared data. |

### 💡 Simple Example
```java
Thread t1 = new Thread(() -> {
    System.out.println("Lambda thread running...");
});
t1.start();
t1.join(); // Main waits for t1
```

### 🧠 Interview Memory Hooks
1. **start() vs run()**: `start()` creates a new thread; `run()` is just a normal method call.
2. **Runnable**: "I am the job. Thread runs me."
3. **Synchronization**: Essential for thread-safety in parallel test execution.
