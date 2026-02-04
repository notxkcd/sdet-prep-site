batch = """
<a name="q41"></a>
### 41) A class can not be declared with synchronized keyword. Then, why we call classes like Vector, StringBuffer are synchronized classes?
[Back to TOC](#q41-toc)

**Answer:**
It's a shorthand. It means **all methods** of that class are `synchronized`.
*Modern Context:* In Java 21, for high concurrency, we often prefer classes like `ConcurrentHashMap` or `CopyOnWriteArrayList` over legacy synchronized classes.

---

<a name="q42"></a>
### 42) What is type casting?
[Back to TOC](#q42-toc)

**Answer:**
Assigning a value of one type to another.
- **Widening (Implicit):** `int` to `double`.
- **Narrowing (Explicit):** `double` to `int` (requires `(int)`).

---

<a name="q43"></a>
### 43) How many types of casting are there in Java?
[Back to TOC](#q43-toc)

**Answer:**
1.  **Primitive Casting.**
2.  **Derived (Object) Casting.**

---

<a name="q44"></a>
### 44) What is auto widening and explicit narrowing?
[Back to TOC](#q44-toc)

**Answer:**
- **Auto Widening:** Java automatically converts small types to large ones (`byte` -> `short` -> `int` -> `long`).
- **Explicit Narrowing:** You manually convert large types to small ones (`long` -> `int`), risking data loss.

---

<a name="q45"></a>
### 45) What is auto-up casting and explicit down casting?
[Back to TOC](#q45-toc)

**Answer:**
- **Auto-up casting:** Casting a Child to a Parent. Always safe.
- **Explicit down casting:** Casting a Parent to a Child. Risks `ClassCastException`.
*Modern Tip:* Use **Pattern Matching for `instanceof`** (Java 16+).
```java
if (obj instanceof String s) {
    System.out.println(s.toLowerCase()); // No explicit cast needed!
}
```

---

<a name="q46"></a>
### 46) Can an int primitive type of data implicitly casted to Double derived type?
[Back to TOC](#q46-toc)

**Answer:**
**Yes.** First, `int` is widened to `double`, and then it's auto-boxed into `Double`.

---

<a name="q47"></a>
### 47) What is ClassCastException?
[Back to TOC](#q47-toc)

**Answer:**
A runtime exception thrown when you try to cast an object to a subclass of which it is not an instance.

---

<a name="q48"></a>
### 48) What is boxing and unboxing?
[Back to TOC](#q48-toc)

**Answer:**
- **Boxing:** Primitive to Wrapper (`int` -> `Integer`).
- **Unboxing:** Wrapper to Primitive (`Integer` -> `int`).

---

<a name="q49"></a>
### 49) What is the difference between auto-widening, auto-upcasting and auto-boxing?
[Back to TOC](#q49-toc)

**Answer:**
- **Widening:** Primitive -> Larger Primitive.
- **Upcasting:** Object -> Parent Object.
- **Autoboxing:** Primitive -> Wrapper.

---

<a name="q50"></a>
### 50) What is polymorphism in Java?
[Back to TOC](#q50-toc)

**Answer:**
"Many forms."
1.  **Static (Compile-time):** Method Overloading.
2.  **Dynamic (Runtime):** Method Overriding.

---

<a name="q51"></a>
### 51) What is method overloading in Java?
[Back to TOC](#q51-toc)

**Answer:**
Same method name, different parameter list (type, number, or order) within the same class.

---

<a name="q52"></a>
### 52) What is the method signature?
[Back to TOC](#q52-toc)

**Answer:**
**Method Name + Parameter List**. (Return type and modifiers are NOT part of the signature).

---

<a name="q53"></a>
### 53) How do compiler differentiate overloaded methods from duplicate methods?
[Back to TOC](#q53-toc)

**Answer:**
By the **Method Signature**. If the name and parameters are identical, it's a duplicate.

---

<a name="q54"></a>
### 54) Can we declare one overloaded method as static and another one as non-static?
[Back to TOC](#q54-toc)

**Answer:**
**Yes.** As long as the signatures differ, the static/non-static modifiers don't matter for overloading.

---

<a name="q55"></a>
### 55) Is it possible to have two methods in a class with same method signature but different return types?
[Back to TOC](#q55-toc)

**Answer:**
**No.** It will cause a compile-time error because the signature (name + params) is what matters for uniqueness.

---

<a name="q56"></a>
### 56) Is visibility checked for overloading?
[Back to TOC](#q56-toc)

**Answer:**
**No.** You can have overloaded methods with different access levels (private, public, etc.).

---

<a name="q57"></a>
### 57) Can overloaded methods be synchronized?
[Back to TOC](#q57-toc)

**Answer:**
**Yes.**

---

<a name="q58"></a>
### 58) Can we declare overloaded methods as final?
[Back to TOC](#q58-toc)

**Answer:**
**Yes.**

---

<a name="q59"></a>
### 59) In the below class, is constructor overloaded or is method overloaded?
```java
public class A {
    public A() {} // Constructor
    void A() {}   // Method
}
```
[Back to TOC](#q59-toc)

**Answer:**
**Neither.** One is a constructor, the other is a method (because it has a return type). This is a trick question; don't name methods after your class!

---

<a name="q60"></a>
### 60) Overloading is the best example of dynamic binding. True or false?
[Back to TOC](#q60-toc)

**Answer:**
**False.** Overloading is **Static Binding** (resolved at compile-time). Overriding is Dynamic Binding.

---

<a name="q61"></a>
### 61) Can overloaded method be overrided?
[Back to TOC](#q61-toc)

**Answer:**
**Yes.** You can override any of the overloaded forms in the subclass.

---

<a name="q62"></a>
### 62) What is method overriding in Java?
[Back to TOC](#q62-toc)

**Answer:**
Redefining a parent class method in the subclass with the **exact same signature**.

---

<a name="q63"></a>
### 63) What are the rules for method overriding?
[Back to TOC](#q63-toc)

**Answer:**
1.  **Same Signature:** (Name + Params).
2.  **Compatible Return Type:** (Can be a subclass - Covariant Return Type).
3.  **Visibility:** Cannot be reduced (e.g., public cannot become private).
4.  **Exceptions:** Cannot throw broader checked exceptions.

---

<a name="q64"></a>
### 64) Can we override static methods?
[Back to TOC](#q64-toc)

**Answer:**
**No.** Static methods belong to the class, not instances. If you define the same static method in a subclass, it's called **Method Hiding**.

---

<a name="q65"></a>
### 65) What happens if we change the arguments of overriding method?
[Back to TOC](#q65-toc)

**Answer:**
It becomes **Overloading**, not overriding.

---

<a name="q66"></a>
### 66) Can we override protected method as public?
[Back to TOC](#q66-toc)

**Answer:**
**Yes.** You can increase visibility, but you can't decrease it.

---

<a name="q67"></a>
### 67) Can we change the return type of overriding method from Number to Integer?
[Back to TOC](#q67-toc)

**Answer:**
**Yes.** This is **Covariant Return Type**.
```java
class Parent { Number get() { return 1; } }
class Child extends Parent { Integer get() { return 2; } } // OK!
```

---

<a name="q68"></a>
### 68) Can we override a method without throws with a method with throws?
[Back to TOC](#q68-toc)

**Answer:**
Only for **Unchecked Exceptions** (RuntimeException). You cannot add new *Checked* exceptions.

---

<a name="q69"></a>
### 69) Can we change SQLException to NumberFormatException while overriding?
[Back to TOC](#q69-toc)

**Answer:**
**Yes.** `NumberFormatException` is unchecked, so it's always allowed.

---

<a name="q70"></a>
### 70) Can we change exception from unchecked to checked?
[Back to TOC](#70-toc)

**Answer:**
**No.**

---

<a name="q71"></a>
### 71) How do you refer super class version of overridden method?
[Back to TOC](#71-toc)

**Answer:**
Using the `super` keyword: `super.myMethod()`.

---

<a name="q72"></a>
### 72) Can we override private methods?
[Back to TOC](#72-toc)

**Answer:**
**No.** Subclasses can't see them.

---

<a name="q73"></a>
### 73) Can we remove throws clause while overriding?
[Back to TOC](#73-toc)

**Answer:**
**Yes.**

---

<a name="q74"></a>
### 74) Is it possible to override non-static methods as static?
[Back to TOC](#74-toc)

**Answer:**
**No.**

---

<a name="q75"></a>
### 75) Can we change checked exception to unchecked while overriding?
[Back to TOC](#75-toc)

**Answer:**
**Yes.**

---

<a name="q76"></a>
### 76) Can we change the number of exceptions?
[Back to TOC](#76-toc)

**Answer:**
**Yes**, as long as they are more specific or fewer.

---

<a name="q77"></a>
### 77) Difference between Overloading and Overriding?
[Back to TOC](#77-toc)

**Answer:**
| Feature | Overloading | Overriding |
| :--- | :--- | :--- |
| **Location** | Same class | Parent/Child relationship |
| **Signature** | Must be different | Must be same |
| **Binding** | Static (Compile-time) | Dynamic (Runtime) |

---

<a name="q78"></a>
### 78) What is static and dynamic binding?
[Back to TOC](#78-toc)

**Answer:**
- **Static Binding:** Resolved by compiler (Overloading, private, static, final methods).
- **Dynamic Binding:** Resolved by JVM at runtime (Overriding).

---

<a name="q79"></a>
### 79) Abstract class must have only abstract methods. True or false?
[Back to TOC](#79-toc)

**Answer:**
**False.** It can have both abstract and concrete methods.

---

<a name="q80"></a>
### 80) Is it compulsory for an abstract class to have at least one abstract method?
[Back to TOC](#80-toc)

**Answer:**
**No.** You can mark a class abstract simply to prevent it from being instantiated.

---
"""
with open('ultimate-questions-cheatsheet/Java-Ultimate-Cheat-Sheet.md', 'a') as f:
    f.write(batch)
