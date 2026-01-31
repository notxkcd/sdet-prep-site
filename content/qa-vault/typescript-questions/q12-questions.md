---
title: "Questions - oops"
date: 2026-01-30
draft: false
---

# TypeScript Programming Interview Questions (Sorted by Difficulty) - oops.md

## Intermediate
- [Demonstrate Type Assertion (Upcasting) in a main function/block.](#demonstrate-type-assertion-upcasting-in-a-main-functionblock)
- [Demonstrate the use of `abstract` class and `private` fields with getters.](#demonstrate-the-use-of-abstract-class-and-private-fields-with-getters)

## Advanced
- [Write a program that demonstrates the four pillars of OOP (Abstraction, Encapsulation, Inheritance, and Polymorphism) using an `Animal` superclass and a `Dog` subclass.](#write-a-program-that-demonstrates-the-four-pillars-of-oop-abstraction-encapsulation-inheritance-and-polymorphism-using-an-animal-superclass-and-a-dog-subclass)

---

# Answers

## Intermediate

### <a id="demonstrate-type-assertion-upcasting-in-a-main-functionblock"></a>Demonstrate Type Assertion (Upcasting) in a main function/block.
```typescript
class Animal {
    move() { console.log("Moving"); }
}
class Dog extends Animal {
    bark() { console.log("Woof!"); }
}

const dog = new Dog();
// Upcasting (implicit in structural typing if compatible, or explicit)
const animal: Animal = dog; 
animal.move();
// animal.bark(); // Error: Property 'bark' does not exist on type 'Animal'.

// Type Assertion (Downcasting)
(animal as Dog).bark(); // Woof!
```
[Back to Top](#intermediate)

### <a id="demonstrate-the-use-of-abstract-class-and-private-fields-with-getters"></a>Demonstrate the use of `abstract` class and `private` fields with getters.
```typescript
abstract class Shape {
    abstract getArea(): number;
}

class Circle extends Shape {
    private _radius: number;

    constructor(radius: number) {
        super();
        this._radius = radius;
    }

    get radius(): number {
        return this._radius;
    }

    getArea(): number {
        return Math.PI * this._radius * this._radius;
    }
}

const c = new Circle(5);
console.log(c.radius); // 5
console.log(c.getArea());
```
[Back to Top](#intermediate)

## Advanced

### <a id="write-a-program-that-demonstrates-the-four-pillars-of-oop-abstraction-encapsulation-inheritance-and-polymorphism-using-an-animal-superclass-and-a-dog-subclass"></a>Write a program that demonstrates the four pillars of OOP (Abstraction, Encapsulation, Inheritance, and Polymorphism) using an `Animal` superclass and a `Dog` subclass.
```typescript
// 1. Abstraction
abstract class Animal {
    // 2. Encapsulation
    private _name: string;

    constructor(name: string) {
        this._name = name;
    }

    get name(): string {
        return this._name;
    }

    abstract makeSound(): void; // Abstract method
}

// 3. Inheritance
class Dog extends Animal {
    constructor(name: string) {
        super(name);
    }

    // 4. Polymorphism (Method overriding)
    makeSound(): void {
        console.log(`${this.name} says Woof!`);
    }
}

class Cat extends Animal {
    makeSound(): void {
        console.log(`${this.name} says Meow!`);
    }
}

const myDog: Animal = new Dog("Buddy");
const myCat: Animal = new Cat("Whiskers");

myDog.makeSound(); // Buddy says Woof!
myCat.makeSound(); // Whiskers says Meow!
```
[Back to Top](#advanced)