batch = """
<a name="q201"></a>
### 201) What is the default priority of a thread?
[Back to TOC](#q201-toc)

**Answer:**
**5** (`NORM_PRIORITY`).

---

<a name="q202"></a>
### 202) Priority of main thread?
[Back to TOC](#q202-toc)

**Answer:**
**5**. Yes, it can be changed.

---

<a name="q203"></a>
### 203) Purpose of Thread.sleep()?
[Back to TOC](#q203-toc)

**Answer:**
To pause the execution of the **current thread** for a specified amount of time. It does NOT release any locks.

---

<a name="q204"></a>
### 204) Which thread sleeps? (myThread.sleep(5000))
[Back to TOC](#q204-toc)

**Answer:**
The **current thread** (the one that executes the line), which is usually the `main` thread in simple programs. `sleep()` is a static method.

---

<a name="q205"></a>
### 205) Does sleep() release locks?
[Back to TOC](#q205-toc)

**Answer:**
**No.** The thread keeps all the locks it holds while sleeping.

---

<a name="q206"></a>
### 206) Purpose of join()?
[Back to TOC](#q206-toc)

**Answer:**
To make the current thread wait until the thread on which `join()` was called finishes its execution.
```java
Thread t1 = new Thread(() -> { /* task */ });
t1.start();
t1.join(); // Main thread waits for t1 to finish
```

---

<a name="q207"></a>
### 207) What is synchronization?
[Back to TOC](#q207-toc)

**Answer:**
A mechanism to control access to shared resources by multiple threads, preventing **Race Conditions**.
*Modern Context:* For complex coordination, consider **`java.util.concurrent.locks.ReentrantLock`** or **`java.util.concurrent.atomic`** classes.

---

<a name="q208"></a>
### 208) What is an object lock (monitor)?
[Back to TOC](#q208-toc)

**Answer:**
Every object in Java has an internal "Monitor". When a thread enters a `synchronized` block/method, it acquires this lock. No other thread can enter *any* synchronized part of that same object until the lock is released.

---

<a name="q209"></a>
### 209) Synchronize only a part of a method?
[Back to TOC](#q209-toc)

**Answer:**
Use a **Synchronized Block**.
```java
public void myMethod() {
    // non-synchronized code
    synchronized(this) {
        // critical section
    }
}
```

---

<a name="q210"></a>
### 210) Use of synchronized blocks?
[Back to TOC](#q210-toc)

**Answer:**
**Performance.** Synchronizing an entire method is expensive. Blocks allow you to lock only the specific lines that need thread-safety.

---

<a name="q211"></a>
### 211) What is a mutex?
[Back to TOC](#q211-toc)

**Answer:**
Short for "Mutual Exclusion". It's a lock that ensures only one thread can access a resource at a time. In Java, the object monitor acts as a mutex.

---

<a name="q212"></a>
### 212) Synchronized constructors?
[Back to TOC](#q212-toc)

**Answer:**
**No.** It's a compile-time error. Only the thread creating the object has access to it during construction anyway.

---

<a name="q213"></a>
### 213) Synchronized variables?
[Back to TOC](#q213-toc)

**Answer:**
**No.** Use the **`volatile`** keyword to ensure visibility of variable changes across threads, or use **`Atomic`** classes.

---

<a name="q214"></a>
### 214) Static vs Non-static synchronized methods simultaneously?
[Back to TOC](#q214-toc)

**Answer:**
**Yes.** They use different locks. Static methods lock on the **Class object**, while non-static methods lock on the **Instance (this)**.

---

<a name="q215"></a>
### 215) Does a thread release the lock if an exception occurs?
[Back to TOC](#q215-toc)

**Answer:**
**Yes.** Java automatically releases the lock if an exception is thrown within a synchronized block.

---

<a name="q216"></a>
### 216) Synchronized methods or blocks?
[Back to TOC](#q216-toc)

**Answer:**
**Blocks** are preferred because they are more granular and improve performance by reducing the locked time.

---

<a name="q217"></a>
### 217) What is a Deadlock?
[Back to TOC](#q217-toc)

**Answer:**
A situation where two threads are waiting for each other to release locks, and neither can proceed.
*Example:* T1 holds Lock A and wants B; T2 holds Lock B and wants A.

---

<a name="q218"></a>
### 218) Detect deadlocks programmatically?
[Back to TOC](#q218-toc)

**Answer:**
Use **`ThreadMXBean`**.
```java
ThreadMXBean bean = ManagementFactory.getThreadMXBean();
long[] deadlockedThreads = bean.findDeadlockedThreads();
```

---

<a name="q219"></a>
### 219) Lock ordering vs Lock timeout?
[Back to TOC](#q219-toc)

**Answer:**
- **Lock Ordering:** Ensuring all threads acquire locks in the exact same sequence.
- **Lock Timeout:** Using `tryLock(timeout, unit)` so a thread gives up after a while instead of waiting forever.

---

<a name="q220"></a>
### 220) Tips to avoid deadlock?
[Back to TOC](#q220-toc)

**Answer:**
1.  Avoid nested locks.
2.  Use a fixed lock order.
3.  Use **`tryLock`** with a timeout.

---

<a name="q221"></a>
### 221) Inter-thread communication?
[Back to TOC](#q221-toc)

**Answer:**
Using **`wait()`**, **`notify()`**, and **`notifyAll()`**.

---

<a name="q222"></a>
### 222) wait() vs sleep()?
[Back to TOC](#q222-toc)

**Answer:**
| Feature | wait() | sleep() |
| :--- | :--- | :--- |
| **Class** | Object | Thread |
| **Lock** | **Releases lock** | **Keeps lock** |
| **Synchronized** | Must be in sync block | Anywhere |

---

<a name="q223"></a>
### 223) notify() vs notifyAll()?
[Back to TOC](#q223-toc)

**Answer:**
- **`notify()`**: Wakes up ONE random waiting thread.
- **`notifyAll()`**: Wakes up ALL waiting threads. (Safest choice).

---

<a name="q224"></a>
### 224) Why wait/notify are in Object class?
[Back to TOC](#q224-toc)

**Answer:**
Because the **Lock/Monitor** is associated with the **Object**, not the thread.

---

<a name="q225"></a>
### 225) Purpose of interrupt()?
[Back to TOC](#q225-toc)

**Answer:**
To signal a thread that it should stop what it's doing (e.g., wake it up from a `sleep` or `wait`).

---

<a name="q226"></a>
### 226) Check if thread is interrupted?
[Back to TOC](#q226-toc)

**Answer:**
1.  `t.isInterrupted()`: Checks the status.
2.  `Thread.interrupted()`: Checks AND clears the status.

---

<a name="q227"></a>
### 227) isInterrupted() vs interrupted()?
[Back to TOC](#q227-toc)

**Answer:**
`isInterrupted()` is an instance method that only checks. `interrupted()` is a static method that checks and resets the flag to false.

---

<a name="q228"></a>
### 228) Can a thread interrupt itself?
[Back to TOC](#q228-toc)

**Answer:**
**Yes.**

---

<a name="q229"></a>
### 229) Thread States (Life Cycle)?
[Back to TOC](#q229-toc)

**Answer:**
1.  **NEW:** Created but not started.
2.  **RUNNABLE:** Executing or waiting for CPU.
3.  **BLOCKED:** Waiting for a lock.
4.  **WAITING:** Waiting for another thread (wait/join).
5.  **TIMED_WAITING:** Waiting with a timeout (sleep/wait).
6.  **TERMINATED:** Finished execution.

---

<a name="q230"></a>
### 230) State of deadlocked threads?
[Back to TOC](#q230-toc)

**Answer:**
**BLOCKED** or **WAITING**.

---

<a name="q231"></a>
### 231) BLOCKED vs WAITING?
[Back to TOC](#q231-toc)

**Answer:**
- **BLOCKED:** Waiting for a `synchronized` lock.
- **WAITING:** Waiting for a signal from another thread (`wait()`, `join()`).

---

<a name="q232"></a>
### 232) WAITING vs TIMED_WAITING?
[Back to TOC](#q232-toc)

**Answer:**
Indefinite wait vs. waiting for a specific period of time.

---

<a name="q233"></a>
### 233) Call start() twice?
[Back to TOC](#q233-toc)

**Answer:**
**No.** It throws `IllegalThreadStateException`.

---

<a name="q234"></a>
### 234) start() vs run()?
[Back to TOC](#q234-toc)

**Answer:**
- **`start()`**: Creates a new thread and then calls `run()`.
- **`run()`**: Executes the code in the **current** thread (just a normal method call).

---

<a name="q235"></a>
### 235) How to stop a thread?
[Back to TOC](#q235-toc)

**Answer:**
Never use `stop()`. Use a **volatile boolean flag** or **Interrupts**.
```java
// Modern Way
while (!Thread.currentThread().isInterrupted()) {
    // task
}
```

---

<a name="q236"></a>
### 236) If exception occurs in T1, does it affect T2?
[Back to TOC](#q236-toc)

**Answer:**
**No.** Threads are independent. If T1 crashes, T2 continues normally.

---

<a name="q237"></a>
### 237) Thread class vs Runnable interface?
[Back to TOC](#q237-toc)

**Answer:**
**`Runnable`** is better because:
1.  Java only supports single inheritance.
2.  It separates the task from the runner (better design).

---

<a name="q238"></a>
### 238) Program vs Process vs Thread?
[Back to TOC](#q238-toc)

**Answer:**
- **Program:** Set of instructions on disk (Static).
- **Process:** A program in execution (Dynamic).
- **Thread:** A subset of a process (Lightweight).

---

<a name="q239"></a>
### 239) User threads vs Daemon threads?
[Back to TOC](#q239-toc)

**Answer:**
The JVM keeps running as long as there is at least one **User thread** alive. It terminates all **Daemon threads** immediately once all User threads finish.

---

<a name="q240"></a>
### 240) Use of Thread Groups?
[Back to TOC](#240-toc)

**Answer:**
To manage multiple threads as a single unit (e.g., interrupt all threads in a group).
*Modern Context:* Mostly replaced by **`ExecutorService`**.

---
"""
with open('ultimate-questions-cheatsheet/Java-Ultimate-Cheat-Sheet.md', 'a') as f:
    f.write(batch)
