batch = """
<a name="q1"></a>
### 1) What are the main features of Java? (Updated for Java 21)
[Back to TOC](#q1-toc)

**Answer:**
Think **"POSH-R"** + **Modern Scalability**.
- **Platform Independent:** "Write Once, Run Anywhere" via the JVM.
- **Object-Oriented:** Everything is centered around objects (and now **Records** for data).
- **Simple & Secure:** No pointers, automatic memory management, and a robust security manager.
- **Highly Robust:** Strong exception handling and **Garbage Collection**.
- **Modern Concurrency:** Now includes **Virtual Threads** (Project Loom) for massive scalability.

```java
// Modern Java 21 Feature: Virtual Threads
public class Main {
    public static void main(String[] args) {
        // Creating a virtual thread - lightweight and efficient!
        Thread.ofVirtual().start(() -> {
            System.out.println("Hello from a Virtual Thread!");
        });
    }
}
```

---

<a name="q2"></a>
### 2) What is the latest version of Java?
[Back to TOC](#q2-toc)

**Answer:**
**Java 21** is the current major **LTS (Long Term Support)** version. It introduced stable Virtual Threads and Sequenced Collections. Java 25 is expected to be the next LTS.

---

<a name="q3"></a>
### 3) What are the fundamental principles of object oriented programming?
[Back to TOC](#q3-toc)

**Answer:**
Remember **A-PIE**:
1.  **A**bstraction: Hiding complexity (Interfaces/Abstract Classes).
2.  **P**olymorphism: One interface, many forms (Overloading/Overriding).
3.  **I**nheritance: Acquiring properties from a parent (now enhanced with **Sealed Classes** for controlled inheritance).
4.  **E**ncapsulation: Protecting data (using private fields and modern **Records**).

---

<a name="q4"></a>
### 4) What do you mean by inheritance in Java?
[Back to TOC](#q4-toc)

**Answer:**
It allows a "Child" class to inherit fields and methods from a "Parent" class.
```java
class Animal {
    void eat() { System.out.println("Eating..."); }
}

class Dog extends Animal {
    void bark() { System.out.println("Barking..."); }
}

// Dog now has both eat() and bark() methods.
```

---

<a name="q5"></a>
### 5) What are the different types of inheritance?
[Back to TOC](#q5-toc)

**Answer:**
1.  **Single:** A -> B
2.  **Multilevel:** A -> B -> C
3.  **Hierarchical:** A -> B, A -> C
4.  **Multiple:** (Only via **Interfaces**)
5.  **Hybrid:** Combination of the above.

---

<a name="q6"></a>
### 6) does Java supports multiple inheritance? If not, why?
[Back to TOC](#q6-toc)

**Answer:**
**No**, not through classes. 
**Why?** To avoid the **Diamond Problem**. If Class C extends both A and B, and both have a method `run()`, Class C wouldn't know which one to execute.

---

<a name="q7"></a>
### 7) If Java doesn’t supports multiple inheritance, then how do you implement multiple inheritance in Java?
[Back to TOC](#q7-toc)

**Answer:**
Using **Interfaces**. A class can implement as many interfaces as it needs.
```java
interface Swimmer { void swim(); }
interface Flyer { void fly(); }

class Duck implements Swimmer, Flyer {
    public void swim() { System.out.println("Swimming..."); }
    public void fly() { System.out.println("Flying..."); }
}
```

---

<a name="q8"></a>
### 8) What is the parent class of all classes in Java?
[Back to TOC](#q8-toc)

**Answer:**
`java.lang.Object`. Every class you create implicitly extends `Object`.

---

<a name="q9"></a>
### 9) Do interfaces also inherited from java.lang.Object class?
[Back to TOC](#q9-toc)

**Answer:**
**No.** Interfaces do not extend `Object`. However, they implicitly declare all of `Object`'s public methods (like `toString()`, `equals()`), so any implementation of an interface will have these methods.

---

<a name="q10"></a>
### 10) How do you restrict a member of a class from inheriting to it’s sub classes?
[Back to TOC](#q10-toc)

**Answer:**
Use the **`private`** modifier. Private members are only visible within their own class.

---

<a name="q11"></a>
### 11) Can a class extend itself?
[Back to TOC](#q11-toc)

**Answer:**
**No.** It would cause a compile-time error.

---

<a name="q12"></a>
### 12) Do constructors and initializers also inherited to sub classes?
[Back to TOC](#q12-toc)

**Answer:**
**No.** Constructors are not inherited. However, the subclass constructor **must** call the parent constructor (implicitly or explicitly via `super()`).

---

<a name="q13"></a>
### 13) What happens if both, super class and sub class, have a field with same name?
[Back to TOC](#q13-toc)

**Answer:**
This is called **Variable Hiding**. The subclass field "hides" the superclass field.
```java
class Parent { String name = "Parent"; }
class Child extends Parent { 
    String name = "Child"; 
    void print() {
        System.out.println(name);       // Child
        System.out.println(super.name); // Parent
    }
}
```

---

<a name="q14"></a>
### 14) Do static members also inherited to sub classes?
[Back to TOC](#q14-toc)

**Answer:**
**Yes**, but they are not overridden; they are **hidden**. You should access them using the class name.

---

<a name="q15"></a>
### 15) What is the difference between super() and this()?
[Back to TOC](#q15-toc)

**Answer:**
- `super()`: Calls the **Parent** class constructor.
- `this()`: Calls another constructor in the **Same** class.
*Both must be the first line in a constructor.*

---

<a name="q16"></a>
### 16) What are the differences between static initializers and instance initializers?
[Back to TOC](#q16-toc)

**Answer:**
- **Static Initializer (`static {}`):** Runs once when the class is loaded.
- **Instance Initializer (`{}`):** Runs every time an object is created, before the constructor.

---

<a name="q17"></a>
### 17) How do you instantiate a class using Java 8+ method references?
[Back to TOC](#q17-toc)

**Answer:**
Using `ClassName::new`.
```java
Supplier<ArrayList<String>> listSupplier = ArrayList::new;
ArrayList<String> list = listSupplier.get();
```

---

<a name="q18"></a>
### 18) Can you create an object without using new operator in Java?
[Back to TOC](#q18-toc)

**Answer:**
**Yes.** 
1. `Class.newInstance()` (Reflection - Deprecated since Java 9, use `getDeclaredConstructor().newInstance()`).
2. `clone()` method.
3. Deserialization.
4. `ClassName::new` (Method Reference).

---

<a name="q19"></a>
### 19) What is constructor chaining?
[Back to TOC](#q19-toc)

**Answer:**
The process of one constructor calling another constructor (using `this()` or `super()`).

---

<a name="q20"></a>
### 20) Can we call sub class constructor from a super class constructor?
[Back to TOC](#q20-toc)

**Answer:**
**No.** The parent exists before the child; it has no knowledge of the child's constructors.

---

<a name="q21"></a>
### 21) Do constructors have return type?
[Back to TOC](#q21-toc)

**Answer:**
**No.** If you add a return type, it's no longer a constructor; it's just a method that happens to have the same name as the class.

---

<a name="q22"></a>
### 22) What is no-arg constructor?
[Back to TOC](#q22-toc)

**Answer:**
A constructor with no parameters. If you don't define any constructor, Java provides a **default no-arg constructor** for you.

---

<a name="q23"></a>
### 23) What is the use of private constructors?
[Back to TOC](#q23-toc)

**Answer:**
To **prevent instantiation**.
**Common Uses:**
1. **Singleton Pattern:** `private MyClass() {}`
2. **Utility Classes:** (e.g., `java.lang.Math`).

---

<a name="q24"></a>
### 24) Can we use this() and super() in a method?
[Back to TOC](#q24-toc)

**Answer:**
**No.** They can only be used in **constructors**.

---

<a name="q25"></a>
### 25) What is the difference between class variables and instance variables?
[Back to TOC](#q25-toc)

**Answer:**
- **Class Variables (`static`):** One copy shared by all objects.
- **Instance Variables:** Each object has its own unique copy.

---

<a name="q26"></a>
### 26) What is the constructor overloading?
[Back to TOC](#q26-toc)

**Answer:**
Defining multiple constructors with different parameter lists to initialize objects in different ways.

---

<a name="q27"></a>
### 27) What is the difference between constructor and method?
[Back to TOC](#q27-toc)

**Answer:**
- **Constructor:** Initializes an object, no return type, name must match the class.
- **Method:** Defines behavior, has a return type, can have any name.

---

<a name="q28"></a>
### 28) What are the differences between static and non-static methods?
[Back to TOC](#q28-toc)

**Answer:**
- **Static:** Belongs to the class. Can be called without an object. Cannot access `this` or instance variables.
- **Non-Static:** Belongs to the object. Needs an instance to be called.

---

<a name="q29"></a>
### 29) Can we overload main() method?
[Back to TOC](#q29-toc)

**Answer:**
**Yes**, but the JVM will only call the standard `public static void main(String[] args)` as the entry point.

---

<a name="q30"></a>
### 30) Can we declare main() method as private?
[Back to TOC](#q30-toc)

**Answer:**
**Yes**, it will compile, but the JVM will throw a runtime error because it can't find a *public* entry point.

---

<a name="q31"></a>
### 31) Can we declare main() method as non-static?
[Back to TOC](#q31-toc)

**Answer:**
**No.** The JVM must be able to call `main()` without creating an object of the class.

---

<a name="q32"></a>
### 32) Why main() method must be static?
[Back to TOC](#q32-toc)

**Answer:**
To avoid the "Chicken and Egg" problem. If `main` weren't static, the JVM would need to create an object to call it, but it wouldn't know *which* constructor to use.

---

<a name="q33"></a>
### 33) Can we change the return type of a main() method?
[Back to TOC](#q33-toc)

**Answer:**
**No.** It must be `void`.

---

<a name="q34"></a>
### 34) How many types of modifiers are there in Java?
[Back to TOC](#q34-toc)

**Answer:**
1.  **Access Modifiers:** (public, protected, default, private).
2.  **Non-access Modifiers:** (static, final, abstract, synchronized, volatile, etc.).

---

<a name="q35"></a>
### 35) What are access modifiers in Java?
[Back to TOC](#q35-toc)

**Answer:**
- `private`: Class only.
- `default`: Package only.
- `protected`: Package + Subclasses.
- `public`: Everywhere.

---

<a name="q36"></a>
### 36) What are non-access modifiers in Java?
[Back to TOC](#36-toc)

**Answer:**
- `static`: Class-level member.
- `final`: Unchangeable (Constant class/method/variable).
- **`sealed` (Java 17+):** Limits which classes can extend it.
- `synchronized`: Thread-safe.

---

<a name="q37"></a>
### 37) Can a method or a class be final and abstract at the same time?
[Back to TOC](#37-toc)

**Answer:**
**No.** `abstract` means "must be extended/implemented," and `final` means "cannot be extended/implemented."

---

<a name="q38"></a>
### 38) Can we declare a class as private?
[Back to TOC](#38-toc)

**Answer:**
Only for **Inner Classes**. Top-level classes can only be `public` or `default`.

---

<a name="q39"></a>
### 39) Can we declare an abstract method as private?
[Back to TOC](#39-toc)

**Answer:**
**No.** It must be visible to subclasses to be implemented.

---

<a name="q40"></a>
### 40) Can we use synchronized keyword with class?
[Back to TOC](#40-toc)

**Answer:**
**No.** You synchronize methods or blocks, not the entire class definition.

---
"""
with open('ultimate-questions-cheatsheet/Java-Ultimate-Cheat-Sheet.md', 'a') as f:
    f.write(batch)
