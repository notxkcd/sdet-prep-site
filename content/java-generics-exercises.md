---
title: "Java Generics: 60 Practice Exercises & Cheat Sheet"
date: 2026-02-01
draft: false
category: "Java"
description: "A comprehensive guide to Java Generics, from basics to expert-level patterns including PECS, wildcards, and recursive generics."
---

# Java Generics: Comprehensive Practice Guide

This guide contains 60 progressive exercises designed to master Java Generics, covering everything from basic class definitions to advanced concepts like PECS, recursive generics, and reflection.

---

## Part 1: Basic Generics Exercises (1–20)

### Q1: Can you provide 20 progressive Java Generics exercises with step-by-step solutions and variable traces?

Below is a set of 20 Java exercises on Generics, starting from basic to intermediate, with step-by-step solutions and explanations.

#### 1) Create a simple generic class
**Problem:** Create a generic class `Box<T>` that can hold any type of object. Store a value and print it.
```java
class Box<T> {
    private T value;

    public void set(T value) {
        this.value = value;
    }

    public T get() {
        return value;
    }
}

public class Main {
    public static void main(String[] args) {
        Box<Integer> intBox = new Box<>();
        intBox.set(10); // store an Integer
        System.out.println(intBox.get()); // retrieve value
    }
}
```
**Explanation:**
1. `T` is a type parameter.
2. `Box<Integer>` means this box will only store Integers.
3. `set()` stores a value, `get()` retrieves it.

**Step-by-step values:**
- `intBox.set(10)` → `value = 10`
- `intBox.get()` → prints `10`

---

#### 2) Generic method
**Problem:** Write a generic method that prints any type of array.
```java
public class Main {
    public static <T> void printArray(T[] array) {
        for (T element : array) {
            System.out.print(element + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Integer[] numbers = {1, 2, 3};
        String[] names = {"Alice", "Bob"};
        printArray(numbers); // 1 2 3
        printArray(names);   // Alice Bob
    }
}
```
**Explanation:**
- `<T>` before the return type means the method is generic.
- Works for any object type: `Integer`, `String`, etc.

---

#### 3) Generic Pair class
**Problem:** Create a generic `Pair<K, V>` class storing a key-value pair.
```java
class Pair<K, V> {
    private K key;
    private V value;

    public Pair(K key, V value) {
        this.key = key;
        this.value = value;
    }

    public K getKey() { return key; }
    public V getValue() { return value; }
}

public class Main {
    public static void main(String[] args) {
        Pair<String, Integer> pair = new Pair<>("Age", 25);
        System.out.println(pair.getKey());   // Age
        System.out.println(pair.getValue()); // 25
    }
}
```

---

#### 4) Bounded generic
**Problem:** Create a generic method that finds the maximum of two numbers (only numbers allowed).
```java
public class Main {
    public static <T extends Number> double max(T a, T b) {
        return a.doubleValue() > b.doubleValue() ? a.doubleValue() : b.doubleValue();
    }

    public static void main(String[] args) {
        System.out.println(max(10, 20));   // 20.0
        System.out.println(max(3.5, 2.1)); // 3.5
    }
}
```
**Explanation:**
- `T extends Number` → only Number types allowed.
- `doubleValue()` converts any Number to double for comparison.

---

#### 5) Wildcards `?`
**Problem:** Write a method that prints elements of any list.
```java
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static void printList(List<?> list) {
        for (Object obj : list) {
            System.out.print(obj + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        List<Integer> nums = List.of(1,2,3);
        List<String> names = List.of("Alice","Bob");
        printList(nums);
        printList(names);
    }
}
```

---

#### 6) Generic with multiple bounds
**Problem:** Create a method that accepts a type that is both `Number` and `Comparable`.
```java
public class Main {
    public static <T extends Number & Comparable<T>> T max(T a, T b) {
        return a.compareTo(b) > 0 ? a : b;
    }

    public static void main(String[] args) {
        System.out.println(max(10, 20));   // 20
        System.out.println(max(3.5, 2.1)); // 3.5
    }
}
```

---

#### 7) Generic constructor
**Problem:** Create a class with a generic constructor (class itself is not generic).
```java
class MyClass {
    private Object value;

    public <T> MyClass(T value) {
        this.value = value;
    }

    public void show() {
        System.out.println(value);
    }
}

public class Main {
    public static void main(String[] args) {
        MyClass obj1 = new MyClass(10);
        MyClass obj2 = new MyClass("Hello");
        obj1.show(); // 10
        obj2.show(); // Hello
    }
}
```

---

#### 8) Generic interface
**Problem:** Create a generic interface `Container<T>` with method `getItem`.
```java
interface Container<T> {
    T getItem();
}

class Box<T> implements Container<T> {
    private T item;
    public Box(T item) { this.item = item; }
    public T getItem() { return item; }
}

public class Main {
    public static void main(String[] args) {
        Container<String> box = new Box<>("Hello");
        System.out.println(box.getItem()); // Hello
    }
}
```

---

#### 9) Generic type in static method
**Problem:** Write a static generic method in a class.
```java
class Utils {
    public static <T> void print(T value) {
        System.out.println(value);
    }
}

public class Main {
    public static void main(String[] args) {
        Utils.print(100);
        Utils.print("Hello");
    }
}
```

---

#### 10) Generic array
**Problem:** Create a generic array wrapper class.
```java
class ArrayWrapper<T> {
    private T[] array;

    @SuppressWarnings("unchecked")
    public ArrayWrapper(int size) {
        array = (T[]) new Object[size]; // type erasure workaround
    }

    public void set(int index, T value) { array[index] = value; }
    public T get(int index) { return array[index]; }
}

public class Main {
    public static void main(String[] args) {
        ArrayWrapper<String> arr = new ArrayWrapper<>(3);
        arr.set(0, "A");
        arr.set(1, "B");
        System.out.println(arr.get(0)); // A
        System.out.println(arr.get(1)); // B
    }
}
```

---

#### 11) Generic stack
**Problem:** Create a generic stack with push and pop.
```java
import java.util.ArrayList;

class Stack<T> {
    private ArrayList<T> list = new ArrayList<>();
    public void push(T value) { list.add(value); }
    public T pop() { return list.remove(list.size() - 1); }
    public boolean isEmpty() { return list.isEmpty(); }
}

public class Main {
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();
        stack.push(10);
        stack.push(20);
        System.out.println(stack.pop()); // 20
        System.out.println(stack.pop()); // 10
    }
}
```

---

#### 12) Generic queue
**Problem:** Create a generic queue using `ArrayList`.
```java
import java.util.ArrayList;

class Queue<T> {
    private ArrayList<T> list = new ArrayList<>();
    public void enqueue(T value) { list.add(value); }
    public T dequeue() { return list.remove(0); }
}

public class Main {
    public static void main(String[] args) {
        Queue<String> queue = new Queue<>();
        queue.enqueue("Alice");
        queue.enqueue("Bob");
        System.out.println(queue.dequeue()); // Alice
        System.out.println(queue.dequeue()); // Bob
    }
}
```

---

#### 13) Generic swap method
**Problem:** Write a generic method to swap two elements in an array.
```java
public class Main {
    public static <T> void swap(T[] arr, int i, int j) {
        T temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static void main(String[] args) {
        Integer[] nums = {1,2,3};
        swap(nums, 0, 2);
        for (int n : nums) System.out.print(n + " "); // 3 2 1
    }
}
```

---

#### 14) Bounded wildcard for reading
**Problem:** Sum a list of numbers using `? extends Number`.
```java
import java.util.List;

public class Main {
    public static double sum(List<? extends Number> list) {
        double total = 0;
        for (Number n : list) total += n.doubleValue();
        return total;
    }

    public static void main(String[] args) {
        List<Integer> ints = List.of(1,2,3);
        List<Double> doubles = List.of(1.5, 2.5);
        System.out.println(sum(ints));    // 6.0
        System.out.println(sum(doubles)); // 4.0
    }
}
```

---

#### 15) Generic map-like structure
**Problem:** Create a simple generic map `SimpleMap<K,V>` using `ArrayList`.
```java
import java.util.ArrayList;

class Entry<K,V> {
    K key;
    V value;
    Entry(K k,V v){ key=k; value=v;}
}

class SimpleMap<K,V> {
    ArrayList<Entry<K,V>> list = new ArrayList<>();
    public void put(K key, V value){ list.add(new Entry<>(key,value)); }
    public V get(K key){
        for(Entry<K,V> e: list) if(e.key.equals(key)) return e.value;
        return null;
    }
}

public class Main {
    public static void main(String[] args){
        SimpleMap<String,Integer> map = new SimpleMap<>();
        map.put("Age",25);
        System.out.println(map.get("Age")); // 25
    }
}
```

---

#### 16) Generic bounded type for numbers
**Problem:** Create a generic method to calculate average of `T extends Number`.
```java
import java.util.List;

public class Main {
    public static <T extends Number> double average(List<T> list){
        double sum = 0;
        for(T n: list) sum += n.doubleValue();
        return sum/list.size();
    }

    public static void main(String[] args){
        List<Integer> nums = List.of(1,2,3,4);
        System.out.println(average(nums)); // 2.5
    }
}
```

---

#### 17) Generic method with multiple parameters
**Problem:** Create a method that takes two generic lists and returns the first element of the second list.
```java
import java.util.List;

public class Main {
    public static <A,B> B firstOfSecond(List<A> l1, List<B> l2) {
        return l2.get(0);
    }

    public static void main(String[] args){
        List<String> names = List.of("Alice","Bob");
        List<Integer> nums = List.of(10,20);
        System.out.println(firstOfSecond(names, nums)); // 10
    }
}
```

---

#### 18) Recursive generic type
**Problem:** Implement a generic class `Node<T>` for a linked list.
```java
class Node<T> {
    T data;
    Node<T> next;
    Node(T data){ this.data = data; }
}

public class Main {
    public static void main(String[] args){
        Node<Integer> first = new Node<>(1);
        Node<Integer> second = new Node<>(2);
        first.next = second;
        System.out.println(first.data);       // 1
        System.out.println(first.next.data);  // 2
    }
}
```

---

#### 19) Generic comparator
**Problem:** Sort an array of generics using `Comparable<T>`.
```java
import java.util.Arrays;

public class Main {
    public static <T extends Comparable<T>> void sort(T[] arr){
        Arrays.sort(arr);
    }

    public static void main(String[] args){
        Integer[] nums = {3,1,2};
        sort(nums);
        System.out.println(Arrays.toString(nums)); // [1,2,3]
    }
}
```

---

#### 20) Generic factory pattern
**Problem:** Create a generic factory method that creates objects.
```java
class Factory {
    public static <T> T create(Class<T> clazz) throws Exception {
        return clazz.getDeclaredConstructor().newInstance();
    }
}

class Person { public String name="Alice"; }

public class Main {
    public static void main(String[] args) throws Exception {
        Person p = Factory.create(Person.class);
        System.out.println(p.name); // Alice
    }
}
```
**Explanation:**
- `Class<T>` allows dynamic type creation.
- Uses reflection to call constructor.

---

## Part 2: Advanced Generics Exercises (21–40)

### Q2: Could you provide a second batch of 20 advanced Java Generics exercises focusing on PECS, inheritance, and custom data structures?

This batch pushes further into interfaces, inheritance, complex collections, PECS, and custom data structures.

#### 21) Generic interface with multiple implementations
**Problem:** Create a generic interface `Storage<T>` with methods `add(T item)` and `get(int index)`. Implement it for `Box` and `Shelf`.
```java
interface Storage<T> {
    void add(T item);
    T get(int index);
}

import java.util.ArrayList;

class Box<T> implements Storage<T> {
    private ArrayList<T> items = new ArrayList<>();
    public void add(T item){ items.add(item); }
    public T get(int index){ return items.get(index); }
}

class Shelf<T> implements Storage<T> {
    private ArrayList<T> items = new ArrayList<>();
    public void add(T item){ items.add(item); }
    public T get(int index){ return items.get(index); }
}

public class Main {
    public static void main(String[] args){
        Storage<String> box = new Box<>();
        box.add("Apple");
        System.out.println(box.get(0)); // Apple

        Storage<Integer> shelf = new Shelf<>();
        shelf.add(42);
        System.out.println(shelf.get(0)); // 42
    }
}
```
**Step-by-step:**
- `box.add("Apple")` → `items = ["Apple"]`
- `shelf.add(42)` → `items = [42]`

---

#### 22) Generic class extending another generic class
**Problem:** Create a `ColoredBox<T>` extending `Box<T>` that also stores a color.
```java
class Box<T> {
    T value;
    public void set(T value){ this.value = value; }
    public T get(){ return value; }
}

class ColoredBox<T> extends Box<T> {
    String color;
    public void setColor(String color){ this.color = color; }
    public String getColor(){ return color; }
}

public class Main {
    public static void main(String[] args){
        ColoredBox<String> box = new ColoredBox<>();
        box.set("Book");
        box.setColor("Red");
        System.out.println(box.get()); // Book
        System.out.println(box.getColor()); // Red
    }
}
```

---

#### 23) Generic method with multiple bounds and inheritance
**Problem:** Create a generic method that accepts types implementing `Comparable` and `Number`.
```java
public class Main {
    public static <T extends Number & Comparable<T>> T max(T a, T b) {
        return a.compareTo(b) > 0 ? a : b;
    }

    public static void main(String[] args){
        System.out.println(max(10, 20));   // 20
        System.out.println(max(3.5, 2.1)); // 3.5
    }
}
```
**Step-by-step:**
- `a.compareTo(b)` compares numeric values.
- Ensures `T` supports numeric operations and comparisons.

---

#### 24) PECS Principle (Producer Extends, Consumer Super)
**Problem:** Write methods that **read** and **write** lists using wildcards.
```java
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static void addIntegers(List<? super Integer> list){
        list.add(10);
        list.add(20);
    }

    public static void printNumbers(List<? extends Number> list){
        for(Number n: list) System.out.println(n);
    }

    public static void main(String[] args){
        List<Number> numbers = new ArrayList<>();
        addIntegers(numbers);
        printNumbers(numbers);
    }
}
```
**Explanation:**
- `? super Integer` → safe to **write** Integers.
- `? extends Number` → safe to **read** Numbers.

---

#### 25) Generic stack using bounded type
**Problem:** Restrict a generic stack to store only `Number`.
```java
import java.util.ArrayList;

class NumberStack<T extends Number> {
    private ArrayList<T> list = new ArrayList<>();
    public void push(T value){ list.add(value); }
    public T pop(){ return list.remove(list.size() - 1); }
}

public class Main {
    public static void main(String[] args){
        NumberStack<Integer> stack = new NumberStack<>();
        stack.push(1);
        stack.push(2);
        System.out.println(stack.pop()); // 2
    }
}
```

---

#### 26) Generic pair swapping
**Problem:** Write a generic method to swap values of a `Pair<K,V>`.
```java
class Pair<K,V>{
    K key; V value;
    Pair(K k,V v){ key=k; value=v;}
    public void swap(){ K temp=key; key=(K)value; value=(V)temp; } // unsafe cast
}

public class Main {
    public static void main(String[] args){
        Pair<Object,Object> pair = new Pair<>("Hello", 100);
        pair.swap();
        System.out.println(pair.key);   // 100
        System.out.println(pair.value); // Hello
    }
}
```
**Note:** Casts are required; type safety is compromised. Shows **limitations of generics**.

---

#### 27) Generic linked list
**Problem:** Implement a generic singly linked list.
```java
class Node<T>{
    T data; Node<T> next;
    Node(T data){ this.data = data; }
}

class LinkedList<T>{
    Node<T> head;
    public void add(T value){
        Node<T> node = new Node<>(value);
        if(head==null) head=node;
        else {
            Node<T> temp=head;
            while(temp.next!=null) temp=temp.next;
            temp.next=node;
        }
    }
    public void print(){
        Node<T> temp=head;
        while(temp!=null){
            System.out.print(temp.data+" ");
            temp=temp.next;
        }
        System.out.println();
    }
}

public class Main {
    public static void main(String[] args){
        LinkedList<String> list = new LinkedList<>();
        list.add("A");
        list.add("B");
        list.print(); // A B
    }
}
```

---

#### 28) Generic tree node
**Problem:** Create a generic tree node storing children.
```java
import java.util.List;
import java.util.ArrayList;

class TreeNode<T>{
    T data;
    List<TreeNode<T>> children = new ArrayList<>();
    TreeNode(T data){ this.data=data; }
}

public class Main {
    public static void main(String[] args){
        TreeNode<String> root = new TreeNode<>("Root");
        TreeNode<String> child1 = new TreeNode<>("Child1");
        TreeNode<String> child2 = new TreeNode<>("Child2");
        root.children.add(child1);
        root.children.add(child2);

        System.out.println(root.data);           // Root
        System.out.println(root.children.get(0).data); // Child1
    }
}
```

---

#### 29) Generic comparator with lambda
**Problem:** Sort a generic array using `Comparable` and a lambda.
```java
import java.util.Arrays;

public class Main {
    public static <T extends Comparable<T>> void sortArray(T[] arr){
        Arrays.sort(arr, (a,b)->a.compareTo(b));
    }

    public static void main(String[] args){
        String[] names = {"Bob","Alice"};
        sortArray(names);
        System.out.println(Arrays.toString(names)); // [Alice, Bob]
    }
}
```

---

#### 30) Generic bounded list filter
**Problem:** Filter a list of `T extends Number` and return only values > threshold.
```java
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static <T extends Number> List<T> filterGreater(List<T> list, double threshold){
        List<T> result = new ArrayList<>();
        for(T n: list) if(n.doubleValue() > threshold) result.add(n);
        return result;
    }

    public static void main(String[] args){
        List<Integer> nums = List.of(1,5,10);
        System.out.println(filterGreater(nums, 4)); // [5, 10]
    }
}
```

---

#### 31) Generic enum method
**Problem:** Write a generic method that prints all enum values.
```java
enum Color { RED, GREEN, BLUE }

public class Main {
    public static <T extends Enum<T>> void printEnum(T[] values){
        for(T v: values) System.out.println(v);
    }

    public static void main(String[] args){
        printEnum(Color.values());
    }
}
```

---

#### 32) Generic type with default value
**Problem:** Create a generic `Container<T>` with default value.
```java
class Container<T>{
    T value;
    Container(T defaultValue){ value=defaultValue; }
    T get(){ return value; }
}

public class Main {
    public static void main(String[] args){
        Container<String> c = new Container<>("Hello");
        System.out.println(c.get()); // Hello
    }
}
```

---

#### 33) Generic bounded wildcard producer
**Problem:** Copy elements from `List<? extends T>` to `List<T>`.
```java
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static <T> void copyList(List<? extends T> src, List<T> dest){
        dest.addAll(src);
    }

    public static void main(String[] args){
        List<Integer> src = List.of(1,2);
        List<Number> dest = new ArrayList<>();
        copyList(src, dest);
        System.out.println(dest); // [1,2]
    }
}
```

---

#### 34) Generic bounded wildcard consumer
**Problem:** Add elements to a list using `? super T`.
```java
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static <T> void addAll(List<? super T> list, T... elements){
        for(T e: elements) list.add(e);
    }

    public static void main(String[] args){
        List<Number> numbers = new ArrayList<>();
        addAll(numbers, 1, 2, 3);
        System.out.println(numbers); // [1,2,3]
    }
}
```

---

#### 35) Generic method with multiple types
**Problem:** Swap elements between two lists of generic types.
```java
import java.util.List;

public class Main {
    public static <A,B> void swapFirst(List<A> list1, List<B> list2){
        A temp = list1.get(0);
        list1.set(0, (A) list2.get(0)); // unsafe cast
        list2.set(0, (B) temp);
    }

    public static void main(String[] args){
        List<Object> l1 = List.of("Hello");
        List<Object> l2 = List.of(100);
        // swapFirst(l1,l2); // would require mutable lists
    }
}
```

---

#### 36) Generic singleton
**Problem:** Create a singleton using generics.
```java
class Singleton<T>{
    private static Singleton<?> instance;
    private T value;
    private Singleton(T value){ this.value=value; }
    public static <T> Singleton<T> getInstance(T value){
        if(instance==null) instance = new Singleton<>(value);
        return (Singleton<T>) instance;
    }
    public T getValue(){ return value; }
}

public class Main {
    public static void main(String[] args){
        Singleton<String> s = Singleton.getInstance("Hello");
        System.out.println(s.getValue()); // Hello
    }
}
```

---

#### 37) Generic iterable
**Problem:** Make a generic container iterable.
```java
import java.util.Iterator;
import java.util.ArrayList;

class Container<T> implements Iterable<T> {
    private ArrayList<T> items = new ArrayList<>();
    public void add(T item){ items.add(item); }
    public Iterator<T> iterator(){ return items.iterator(); }
}

public class Main {
    public static void main(String[] args){
        Container<String> c = new Container<>();
        c.add("A"); c.add("B");
        for(String s: c) System.out.print(s+" "); // A B
    }
}
```

---

#### 38) Generic recursive type
**Problem:** Create a generic tree with recursive type bounds.
```java
class Node<T extends Node<T>> {
    T next;
}

class MyNode extends Node<MyNode> {
    String name;
    MyNode(String name){ this.name=name; }
}

public class Main {
    public static void main(String[] args){
        MyNode a = new MyNode("A");
        MyNode b = new MyNode("B");
        a.next = b;
        System.out.println(a.next.name); // B
    }
}
```

---

#### 39) Generic type with lambda comparator
**Problem:** Sort a list of generics using a lambda comparator.
```java
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static <T> void sortList(List<T> list, java.util.Comparator<T> cmp){
        list.sort(cmp);
    }

    public static void main(String[] args){
        List<String> names = new ArrayList<>(List.of("Bob","Alice"));
        sortList(names, (a,b)->a.compareTo(b));
        System.out.println(names); // [Alice, Bob]
    }
}
```

---

#### 40) Generic factory with Supplier
**Problem:** Create objects of any type using `Supplier<T>`.
```java
import java.util.function.Supplier;

public class Main {
    public static <T> T create(Supplier<T> supplier){
        return supplier.get();
    }

    public static void main(String[] args){
        String s = create(() -> "Hello");
        Integer n = create(() -> 42);
        System.out.println(s); // Hello
        System.out.println(n); // 42
    }
}
```

---

## Part 3: Expert Generics Exercises (41–60)

### Q3: Could you provide a final batch of 20 expert-level Java Generics exercises covering nested generics, covariance/contravariance, and complex patterns?

This final batch focuses on nested generics, covariance/contravariance, advanced collections, trees/graphs, and real-world patterns.

#### 41) Nested generic classes
**Problem:** Create a generic class `Outer<T>` with a nested generic class `Inner<U>`.
```java
class Outer<T> {
    T outerValue;
    Outer(T outerValue){ this.outerValue = outerValue; }

    class Inner<U> {
        U innerValue;
        Inner(U innerValue){ this.innerValue = innerValue; }
        void printValues() {
            System.out.println("Outer: " + outerValue + ", Inner: " + innerValue);
        }
    }
}

public class Main {
    public static void main(String[] args){
        Outer<String> outer = new Outer<>("Hello");
        Outer<String>.Inner<Integer> inner = outer.new Inner<>(100);
        inner.printValues(); // Outer: Hello, Inner: 100
    }
}
```

---

#### 42) Generic matrix class
**Problem:** Create a generic 2D matrix.
```java
class Matrix<T> {
    private T[][] data;
    @SuppressWarnings("unchecked")
    Matrix(int rows, int cols){ data = (T[][]) new Object[rows][cols]; }
    void set(int r, int c, T value){ data[r][c] = value; }
    T get(int r, int c){ return data[r][c]; }
}

public class Main {
    public static void main(String[] args){
        Matrix<Integer> m = new Matrix<>(2,2);
        m.set(0,0,1);
        m.set(1,1,4);
        System.out.println(m.get(0,0)); // 1
        System.out.println(m.get(1,1)); // 4
    }
}
```

---

#### 43) Generic bounded type with multiple constraints
**Problem:** Create a method that works for `T extends Number & Comparable<T>` to find minimum.
```java
public class Main {
    public static <T extends Number & Comparable<T>> T min(T a, T b){
        return a.compareTo(b) < 0 ? a : b;
    }
    public static void main(String[] args){
        System.out.println(min(5, 3));   // 3
        System.out.println(min(2.5, 3.5)); // 2.5
    }
}
```

---

#### 44) Generic enum with bounded types
```java
enum Direction { UP, DOWN, LEFT, RIGHT }

class Utils {
    public static <T extends Enum<T>> void printAll(T[] values){
        for(T v: values) System.out.println(v);
    }
}

public class Main {
    public static void main(String[] args){
        Utils.printAll(Direction.values());
    }
}
```

---

#### 45) Generic comparator for nested generics
```java
import java.util.List;
import java.util.ArrayList;
import java.util.Comparator;

class Box<T extends Comparable<T>> {
    T value;
    Box(T value){ this.value = value; }
}

public class Main {
    public static void main(String[] args){
        List<Box<Integer>> boxes = new ArrayList<>();
        boxes.add(new Box<>(10));
        boxes.add(new Box<>(5));

        boxes.sort((a,b)->a.value.compareTo(b.value));
        System.out.println(boxes.get(0).value); // 5
    }
}
```

---

#### 46) Covariance example with wildcards
```java
import java.util.List;
import java.util.ArrayList;

class Animal { void speak(){ System.out.println("Animal"); } }
class Dog extends Animal { void speak(){ System.out.println("Dog"); } }

public class Main {
    public static void makeAnimalsSpeak(List<? extends Animal> list){
        for(Animal a: list) a.speak();
    }
    public static void main(String[] args){
        List<Dog> dogs = List.of(new Dog(), new Dog());
        makeAnimalsSpeak(dogs); // Dog Dog
    }
}
```

---

#### 47) Contravariance example with wildcards
```java
import java.util.List;
import java.util.ArrayList;

class Writer<T>{
    void write(List<? super T> list, T value){ list.add(value); }
}

public class Main {
    public static void main(String[] args){
        List<Animal> animals = new ArrayList<>();
        Writer<Dog> dogWriter = new Writer<>();
        dogWriter.write(animals, new Dog());
        System.out.println(animals.size()); // 1
    }
}
```

---

#### 48) Generic map with bounded wildcards
```java
import java.util.Map;
import java.util.HashMap;

class Utils {
    public static void copy(Map<String, ? extends Number> src, Map<String, Number> dest){
        for(String k: src.keySet()) dest.put(k, src.get(k));
    }
}

public class Main {
    public static void main(String[] args){
        Map<String,Integer> src = Map.of("A",1);
        Map<String,Number> dest = new HashMap<>();
        Utils.copy(src,dest);
        System.out.println(dest.get("A")); // 1
    }
}
```

---

#### 49) Nested generics in collections
```java
import java.util.List;
import java.util.ArrayList;

class Wrapper<T>{
    T value;
    Wrapper(T value){ this.value=value; }
}

public class Main {
    public static void main(String[] args){
        List<Wrapper<List<String>>> list = new ArrayList<>();
        List<String> names = List.of("Alice","Bob");
        list.add(new Wrapper<>(names));
        System.out.println(list.get(0).value.get(0)); // Alice
    }
}
```

---

#### 50) Generic tree traversal
```java
import java.util.List;
import java.util.ArrayList;

class TreeNode<T>{
    T data; List<TreeNode<T>> children = new ArrayList<>();
    TreeNode(T data){ this.data=data; }
}

public class Main {
    public static <T> void printTree(TreeNode<T> root){
        System.out.println(root.data);
        for(TreeNode<T> child: root.children) printTree(child);
    }
    public static void main(String[] args){
        TreeNode<String> root = new TreeNode<>("Root");
        TreeNode<String> c1 = new TreeNode<>("C1");
        TreeNode<String> c2 = new TreeNode<>("C2");
        root.children.add(c1);
        root.children.add(c2);
        printTree(root); // Root C1 C2
    }
}
```

---

#### 51) Generic graph node
```java
import java.util.List;
import java.util.ArrayList;

class GraphNode<T>{
    T data; List<GraphNode<T>> neighbors = new ArrayList<>();
    GraphNode(T data){ this.data=data; }
}

public class Main {
    public static void main(String[] args){
        GraphNode<String> a = new GraphNode<>("A");
        GraphNode<String> b = new GraphNode<>("B");
        a.neighbors.add(b);
        System.out.println(a.neighbors.get(0).data); // B
    }
}
```

---

#### 52) Generic bounded type with method reference
```java
import java.util.Arrays;

public class Main {
    public static <T extends Comparable<T>> void sortArray(T[] arr){
        Arrays.sort(arr, T::compareTo);
    }
    public static void main(String[] args){
        Integer[] nums = {3,1,2};
        sortArray(nums);
        System.out.println(Arrays.toString(nums)); // [1,2,3]
    }
}
```

---

#### 53) Generic stream processing
```java
import java.util.List;

public class Main {
    public static <T> void printList(List<T> list){
        list.stream().forEach(System.out::println);
    }
    public static void main(String[] args){
        List<String> names = List.of("Alice","Bob");
        printList(names); // Alice Bob
    }
}
```

---

#### 54) Generic bounded wildcard for producer-consumer
```java
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static <T> void copyList(List<? extends T> src, List<? super T> dest){
        dest.addAll(src);
    }
    public static void main(String[] args){
        List<Integer> src = List.of(1,2);
        List<Number> dest = new ArrayList<>();
        copyList(src,dest);
        System.out.println(dest); // [1,2]
    }
}
```

---

#### 55) Recursive generics for tree nodes
```java
class Node<T extends Node<T>>{
    T next;
}

class MyNode extends Node<MyNode>{
    String name;
    MyNode(String name){ this.name=name; }
}

public class Main {
    public static void main(String[] args){
        MyNode a = new MyNode("A");
        MyNode b = new MyNode("B");
        a.next = b;
        System.out.println(a.next.name); // B
    }
}
```

---

#### 56) Generic type with bounded constructor
```java
class Utils {
    public static <T extends Number> T createDefault(Class<T> clazz) throws Exception {
        return clazz.getDeclaredConstructor().newInstance();
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        Integer n = Utils.createDefault(Integer.class); // creates 0
        System.out.println(n); // 0
    }
}
```

---

#### 57) Generic recursive method
```java
import java.util.List;

public class Main {
    public static <T> void printListRecursive(List<T> list, int index){
        if(index==list.size()) return;
        System.out.println(list.get(index));
        printListRecursive(list,index+1);
    }
    public static void main(String[] args){
        List<String> names = List.of("Alice","Bob");
        printListRecursive(names,0); // Alice Bob
    }
}
```

---

#### 58) Generic bounded type for numeric operations
```java
import java.util.List;

public class Main {
    public static <T extends Number> double sumList(List<T> list){
        double sum=0;
        for(T n: list) sum+=n.doubleValue();
        return sum;
    }
    public static void main(String[] args){
        List<Integer> nums = List.of(1,2,3);
        System.out.println(sumList(nums)); // 6.0
    }
}
```

---

#### 59) Generic Optional type handling
```java
import java.util.Optional;

public class Main {
    public static <T> void printOptional(Optional<T> opt){
        opt.ifPresent(System.out::println);
    }
    public static void main(String[] args){
        Optional<String> opt = Optional.of("Hello");
        printOptional(opt); // Hello
    }
}
```

---

#### 60) Complex nested generics with maps and lists
```java
import java.util.List;
import java.util.Map;

public class Main {
    public static void main(String[] args){
        Map<String, List<Integer>> map = Map.of("A", List.of(1,2,3));
        System.out.println(map.get("A").get(0)); // 1
    }
}
```

---

## Part 4: Java Generics Cheat Sheet

### Q4: Could you provide a comprehensive Java Generics cheat sheet summarizing all 60 exercises and key patterns like PECS and recursive generics?

Below is a structured cheat sheet covering the core patterns, rules, and examples from the 60 exercises.

---

### **1. Basics of Generics**

| Concept | Example | Explanation |
| --- | --- | --- |
| Generic Class | `class Box<T>{ T value; }` | T can be any type (Integer, String, etc.) |
| Generic Method | `public <T> T getValue(T value){ return value; }` | Allows method to work with any type |
| Generic Interface | `interface Storage<T>{ void add(T item); T get(int index); }` | Interface works for multiple types |

---

### **2. Generic Methods & Bounded Types**

| Feature | Example | Explanation |
| --- | --- | --- |
| Bounded Type | `<T extends Number>` | Restrict type to Number or subclasses |
| Multiple Bounds | `<T extends Number & Comparable<T>>` | Type must be Number & Comparable |

---

### **3. PECS – Wildcards (Producer Extends, Consumer Super)**

| Wildcard | Meaning | Example |
| --- | --- | --- |
| `? extends T` | Can **read** T | `List<? extends Number>` |
| `? super T` | Can **write** T | `List<? super Integer>` |

---

### **4. Collections & Nested Generics**

*   **Nested generic lists:** `List<Wrapper<List<String>>>`
*   **Generic maps:** `Map<String, List<Integer>>`
```java
Map<String, List<Integer>> map = Map.of("A", List.of(1,2));
System.out.println(map.get("A").get(0)); // 1
```

---

### **5. Generic Data Structures**

| Structure | Example | Notes |
| --- | --- | --- |
| LinkedList | `LinkedList<T>` | Generic nodes `Node<T>` |
| Tree | `TreeNode<T>` | Recursive generics for children |
| Graph | `GraphNode<T>` | Generic adjacency lists |
| Stack | `NumberStack<T extends Number>` | Restrict to numeric operations |
| Matrix | `Matrix<T>` | Generic 2D array |

---

### **6. Interfaces & Inheritance**

*   **Generic interface implementation:**
```java
interface Storage<T>{ void add(T item); T get(int index); }
class Box<T> implements Storage<T>{ /*...*/ }
```
*   **Extending generic classes:**
```java
class ColoredBox<T> extends Box<T> { String color; }
```

---

### **7. Advanced Patterns**

| Pattern | Example | Notes |
| --- | --- | --- |
| Singleton | `Singleton<T>` | Generic singleton |
| Factory | `Supplier<T>` | Create objects generically |
| Optional | `Optional<T>` | Safe value handling |
| Enum | `<T extends Enum<T>>` | Print all enum constants |

---

### **8. Recursive Generics & Covariance/Contravariance**

| Concept | Example |
| --- | --- |
| Recursive | `Node<T extends Node<T>>` |
| Covariance | `List<? extends Animal>` → read only |
| Contravariance | `List<? super Dog>` → write only |

---

### **9. Key Tips**

1.  **Remember PECS:** `Producer Extends, Consumer Super`.
2.  **Use bounded types** for constraints: `<T extends Number>`.
3.  **Nested generics** help model complex structures.
4.  **Recursive generics** for trees/graphs.
5.  **Wildcard rules:**
    *   Read-only → `? extends T`.
    *   Write-only → `? super T`.

---

*This guide covers essential Java Generics patterns used in interviews and real-world development.*
