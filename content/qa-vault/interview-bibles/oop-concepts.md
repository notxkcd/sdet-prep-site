---
title: "Java OOP Core Concepts"
date: 2026-01-31
draft: false
---

## 1. The Four Pillars of OOP

| Pillar | Concept | Real-world Analogy |
| --- | --- | --- |
| **Encapsulation** | Hiding data using private fields + public methods. | A medical capsule (hides powder, provides safe access). |
| **Abstraction** | Hiding complex logic, showing only essentials. | Car brakes (you press, it stops; internal mechanics hidden). |
| **Inheritance** | Acquiring properties of a parent class. | Family traits (inheriting eye color). |
| **Polymorphism** | One interface, multiple forms. | You (different behavior as a student, son, employee). |

---

## 2. Inheritance & Polymorphism

### Overloading vs Overriding
- **Overloading**: Same method name, different parameters (Compile-time).
- **Overriding**: Same method signature in child class (Runtime).

### Abstract Class vs Interface
- **Abstract Class**: Partial abstraction (can have instance fields and constructors).
- **Interface**: Full contract (defines "what" to do, but not "how").

---

## 3. Class Relationships

- **Association**: General connection ("Teacher works with Student").
- **Aggregation**: "Has-a" relationship (Weak ownership - "Department has Teachers").
- **Composition**: "Part-of" relationship (Strong ownership - "Car has an Engine").

---

## 4. Constructors

- **Default**: Created by Java if you don't define one.
- **Parameterized**: Used to initialize object data during creation.
- **Chaining**: Using `this()` or `super()` to call other constructors.
