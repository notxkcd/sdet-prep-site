---
title: "Questions - oops"
date: 2026-01-30
draft: false
---

# Python Programming Interview Questions (Sorted by Difficulty) - oops.md

## Intermediate
- [Demonstrate treating a subclass instance as a superclass instance (Polymorphism).](#demonstrate-treating-a-subclass-instance-as-a-superclass-instance-polymorphism)
- [Demonstrate the use of `abstract` class (ABC) and `private` (or protected) fields with getters.](#demonstrate-the-use-of-abstract-class-abc-and-private-or-protected-fields-with-getters)

## Advanced
- [Write a program that demonstrates the four pillars of OOP (Abstraction, Encapsulation, Inheritance, and Polymorphism) using an `Animal` superclass and a `Dog` subclass.](#write-a-program-that-demonstrates-the-four-pillars-of-oop-abstraction-encapsulation-inheritance-and-polymorphism-using-an-animal-superclass-and-a-dog-subclass)

---

# Answers

## Intermediate

### <a id="demonstrate-treating-a-subclass-instance-as-a-superclass-instance-polymorphism"></a>Demonstrate treating a subclass instance as a superclass instance (Polymorphism).
```python
class Animal:
    def move(self):
        print("Moving")

class Dog(Animal):
    def bark(self):
        print("Woof!")

dog = Dog()
# In Python, typing is duck typing, but inheritance implies IS-A relationship
animal: Animal = dog 
animal.move()
# animal.bark() # Static checkers would complain, but runtime allows if obj has method
```
[Back to Top](#intermediate)

### <a id="demonstrate-the-use-of-abstract-class-abc-and-private-or-protected-fields-with-getters"></a>Demonstrate the use of `abstract` class (ABC) and `private` (or protected) fields with getters.
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius # Protected convention

    @property
    def radius(self):
        return self._radius

    def get_area(self):
        import math
        return math.pi * self._radius ** 2

c = Circle(5)
print(c.radius)
print(c.get_area())
```
[Back to Top](#intermediate)

## Advanced

### <a id="write-a-program-that-demonstrates-the-four-pillars-of-oop-abstraction-encapsulation-inheritance-and-polymorphism-using-an-animal-superclass-and-a-dog-subclass"></a>Write a program that demonstrates the four pillars of OOP (Abstraction, Encapsulation, Inheritance, and Polymorphism) using an `Animal` superclass and a `Dog` subclass.
```python
from abc import ABC, abstractmethod

# 1. Abstraction
class Animal(ABC):
    def __init__(self, name):
        # 2. Encapsulation
        self.__name = name # Private attribute

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def make_sound(self):
        pass

# 3. Inheritance
class Dog(Animal):
    def make_sound(self):
        # 4. Polymorphism
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} says Meow!")

animals = [Dog("Buddy"), Cat("Whiskers")]
for animal in animals:
    animal.make_sound()
```
[Back to Top](#advanced)