batch = """
<a name="q81"></a>
### 81) Can we use abstract keyword with constructors?
[Back to TOC](#q81-toc)

**Answer:**
**No.** Constructors are used to initialize objects, and an abstract entity cannot be initialized.

---

<a name="q82"></a>
### 82) Why final and abstract can not be used at a time?
[Back to TOC](#q82-toc)

**Answer:**
They are logically opposite. `abstract` *requires* inheritance to be useful, while `final` *prevents* inheritance.

---

<a name="q83"></a>
### 83) Can we instantiate an abstract class?
[Back to TOC](#q83-toc)

**Answer:**
**No.** Even if it contains no abstract methods, once marked `abstract`, it cannot be instantiated.

---

<a name="q84"></a>
### 84) Can we declare abstract methods as private?
[Back to TOC](#q84-toc)

**Answer:**
**No.** Abstract methods must be visible to subclasses so they can be implemented.

---

<a name="q85"></a>
### 85) We can’t instantiate an abstract class. Then why constructors are allowed in abstract class?
[Back to TOC](#q85-toc)

**Answer:**
To initialize fields belonging to the abstract class when a concrete subclass is instantiated. The subclass constructor always calls `super()`.

---

<a name="q86"></a>
### 86) Can we declare abstract methods as static?
[Back to TOC](#q86-toc)

**Answer:**
**No.** Static methods belong to the class and cannot be overridden, but abstract methods *must* be overridden.

---

<a name="q87"></a>
### 87) Can a class contain an abstract class as a member?
[Back to TOC](#q87-toc)

**Answer:**
**Yes.** You can have a field whose type is an abstract class; at runtime, it will point to an instance of a concrete subclass.

---

<a name="q88"></a>
### 88) Abstract classes can be nested. True or false?
[Back to TOC](#q88-toc)

**Answer:**
**True.**

---

<a name="q89"></a>
### 89) Can we declare abstract methods as synchronized?
[Back to TOC](#q89-toc)

**Answer:**
**No.** Synchronization is an implementation detail. Since abstract methods have no body (implementation), they can't be synchronized. However, the overriding method in the subclass can be.

---

<a name="q90"></a>
### 90) Can we declare local inner class as abstract?
[Back to TOC](#q90-toc)

**Answer:**
**Yes.**

---

<a name="q91"></a>
### 91) Can abstract method declaration include throws clause?
[Back to TOC](#q91-toc)

**Answer:**
**Yes.**

---

<a name="q92"></a>
### 92) Can abstract classes have interfaces in it?
[Back to TOC](#q92-toc)

**Answer:**
**Yes.**

---

<a name="q93"></a>
### 93) Can interfaces have constructors, static initializers and instance initializers?
[Back to TOC](#q93-toc)

**Answer:**
**No.** Interfaces are meant to be templates for behavior, not containers for state or initialization logic.
*Modern Context:* Since Java 8, interfaces can have `static` and `default` methods, and since Java 9, they can have `private` methods.

---

<a name="q94"></a>
### 94) Can we re-assign a value to a field of interfaces?
[Back to TOC](#q94-toc)

**Answer:**
**No.** Interface fields are implicitly **`public static final`** (constants).

---

<a name="q95"></a>
### 95) Can we declare an Interface with abstract keyword?
[Back to TOC](#q95-toc)

**Answer:**
**Yes**, but it's redundant. All interfaces are implicitly abstract.

---

<a name="q96"></a>
### 96) For every Interface in java, .class file will be generated after compilation. True or false?
[Back to TOC](#q96-toc)

**Answer:**
**True.**

---

<a name="q97"></a>
### 97) Can we override an interface method with visibility other than public?
[Back to TOC](#q97-toc)

**Answer:**
**No.** All interface methods (except private ones) are implicitly `public`. You cannot reduce visibility when implementing them.

---

<a name="q98"></a>
### 98) Can interfaces become local members of the methods?
[Back to TOC](#98-toc)

**Answer:**
**No.** Interfaces cannot be defined inside a method.

---

<a name="q99"></a>
### 99) Can an interface extend a class?
[Back to TOC](#99-toc)

**Answer:**
**No.** Interfaces can only extend other interfaces.

---

<a name="q100"></a>
### 100) Like classes, do interfaces also extend java.lang.Object class by default?
[Back to TOC](#100-toc)

**Answer:**
**No.** They don't extend anything by default. But they expose all methods of `Object` (like `toString()`, `hashCode()`) to the implementing classes.

---

<a name="q101"></a>
### 101) Can interfaces have static methods?
[Back to TOC](#101-toc)

**Answer:**
**Yes** (since Java 8). They are used for utility methods related to the interface.
```java
interface MyInterface {
    static void help() { System.out.println("Helper method"); }
}
```

---

<a name="q102"></a>
### 102) Can an interface have a class or another interface as it’s members?
[Back to TOC](#102-toc)

**Answer:**
**Yes.** They are implicitly `public` and `static`.

---

<a name="q103"></a>
### 103) What are marker interfaces? What is the use of marker interfaces?
[Back to TOC](#103-toc)

**Answer:**
An interface with **no methods or fields**. It "marks" a class as having a certain property.
**Examples:** `Serializable`, `Cloneable`, `Remote`.
*Modern Context:* **Annotations** have largely replaced marker interfaces.

---

<a name="q104"></a>
### 104) What are the changes made to interfaces from Java 8?
[Back to TOC](#104-toc)

**Answer:**
1.  **Default Methods:** Methods with a body (`default` keyword).
2.  **Static Methods:** Methods with a body (`static` keyword).
3.  **Functional Interfaces:** Interfaces with exactly one abstract method (can be used with Lambdas).

---

<a name="q105"></a>
### 105) What are the changes made to interfaces from Java 9?
[Back to TOC](#105-toc)

**Answer:**
**Private Methods:** Interfaces can now have private methods (and private static methods) to encapsulate common logic between default methods.

---

<a name="q106"></a>
### 106) How many types of nested classes are there in Java?
[Back to TOC](#106-toc)

**Answer:**
1.  **Static Nested Classes.**
2.  **Inner Classes (Non-static):**
    - Member Inner Class.
    - Local Inner Class.
    - Anonymous Inner Class.

---

<a name="q107"></a>
### 107) Can we access non-static members of outer class inside a static nested class?
[Back to TOC](#107-toc)

**Answer:**
**No.** Static nested classes don't have a reference to an instance of the outer class. You'd need to create an object of the outer class to access its members.

---

<a name="q108"></a>
### 108) What are member inner classes in Java?
[Back to TOC](#108-toc)

**Answer:**
Classes defined inside another class (not static). To instantiate them, you **must** have an instance of the outer class.
```java
Outer out = new Outer();
Outer.Inner in = out.new Inner();
```

---

<a name="q109"></a>
### 109) Can member inner classes have static members in them?
[Back to TOC](#109-toc)

**Answer:**
**Yes** (since Java 16). Prior to Java 16, they could only have `static final` constants. Now they can have full static members.

---

<a name="q110"></a>
### 110) Can we access all members of outer class inside a member inner class?
[Back to TOC](#110-toc)

**Answer:**
**Yes**, including `private` members.

---

<a name="q111"></a>
### 111) Can we declare local inner classes as static?
[Back to TOC](#111-toc)

**Answer:**
**No.** Local inner classes are defined inside a block/method and cannot be static.

---

<a name="q112"></a>
### 112) Can we use local inner classes outside the method or block?
[Back to TOC](#112-toc)

**Answer:**
**No.** Their scope is limited to that block.

---

<a name="q113"></a>
### 113) Can we declare local inner classes as private or protected or public?
[Back to TOC](#113-toc)

**Answer:**
**No.** They don't take access modifiers (just like local variables).

---

<a name="q114"></a>
### 114) What is the condition to use local variables inside a local inner class?
[Back to TOC](#114-toc)

**Answer:**
They must be **final** or **effectively final** (never changed after being initialized).

---

<a name="q115"></a>
### 115) What are anonymous inner classes in Java?
[Back to TOC](#115-toc)

**Answer:**
Classes without a name, declared and instantiated at the same time. Often used to implement interfaces on the fly.
```java
Runnable r = new Runnable() {
    @Override
    public void run() { System.out.println("Running..."); }
};
```
*Modern Context:* Usually replaced by **Lambdas** for functional interfaces.

---

<a name="q116"></a>
### 116) What is the main difference between static and non-static nested classes?
[Back to TOC](#116-toc)

**Answer:**
- **Static Nested:** Doesn't need an instance of the outer class.
- **Inner Class (Non-static):** Requires an instance of the outer class to exist.

---

<a name="q117"></a>
### 117) What is the use of final keyword in Java?
[Back to TOC](#117-toc)

**Answer:**
1.  **Final Variable:** Value cannot be changed (Constant).
2.  **Final Method:** Cannot be overridden.
3.  **Final Class:** Cannot be inherited.

---

<a name="q118"></a>
### 118) What is the blank final field?
[Back to TOC](#118-toc)

**Answer:**
A final variable that is not initialized when declared. It **must** be initialized in every constructor.

---

<a name="q119"></a>
### 119) Can we change the state of an object to which a final reference variable is pointing?
[Back to TOC](#119-toc)

**Answer:**
**Yes.** You can't make the variable point to a *different* object, but you can change the *data* inside that object.

---

<a name="q120"></a>
### 120) Difference between abstract methods and final methods?
[Back to TOC](#120-toc)

**Answer:**
- **Abstract:** *Must* be implemented by a subclass.
- **Final:** *Cannot* be overridden by a subclass.

---
"""
with open('ultimate-questions-cheatsheet/Java-Ultimate-Cheat-Sheet.md', 'a') as f:
    f.write(batch)
