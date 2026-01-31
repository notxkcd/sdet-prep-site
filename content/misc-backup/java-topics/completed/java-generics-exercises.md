# Java Generics Exercises (Completed)

**User:** Mohammed Shahid (shahid.xkcd@gmail.com)  
**Status:** Completed & Refined

---

## Prompt:
"I want to practice [Generics] in [java]. Can you give me [20] exercises that start very easy and gradually become harder? I want each exercise to be solved step by step with explanations, and I want to see how variable values change at each step if applicable.

## Response:
Absolutely! Let’s create a **progressive set of 20 Java exercises on Generics**, starting from very basic to intermediate-advanced, with **step-by-step solutions and explanations**. We’ll go **slowly at first** so you can understand how generics work in Java.

* * *

**Generics Exercises in Java**
------------------------------

* * *

### **Exercise 1: Create a simple generic class**

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

1.  `T` is a type parameter.
2.  `Box<Integer>` means this box will only store Integers.
3.  `set()` stores a value, `get()` retrieves it.

**Step-by-step values:**

*   `intBox.set(10)` → `value = 10`
*   `intBox.get()` → prints `10`

* * *

### **Exercise 2: Generic method**

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

*   `<T>` before the return type means the method is generic.
*   Works for any object type: `Integer`, `String`, etc.

**Step-by-step values:**

*   `numbers = [1,2,3]`
*   `names = ["Alice","Bob"]`

* * *

### **Exercise 3: Generic Pair class**

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

**Explanation:**

*   `K` = Key type, `V` = Value type
*   You can have different types for each.

* * *

### **Exercise 4: Bounded generic**

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

*   `T extends Number` → only Number types allowed.
*   `doubleValue()` converts any Number to double for comparison.

* * *

### **Exercise 5: Wildcards `?`**

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

**Explanation:**

*   `?` = unknown type
*   Can pass `List<Integer>`, `List<String>`, etc.

* * *

### **Exercise 6: Generic with multiple bounds**

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

**Explanation:**

*   `T extends Number & Comparable<T>` → type must satisfy both constraints.
*   Uses `compareTo()` for comparison instead of converting to double.

* * *

### **Exercise 7: Generic constructor**

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

**Explanation:**

*   Constructor itself is generic, not the class.

* * *

### **Exercise 8: Generic interface**

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

**Explanation:**

*   Interfaces can also be generic.
*   `Box<String>` implements `Container<String>`.

* * *

### **Exercise 9: Generic type in static method**

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

**Explanation:**

*   Static method can be generic; class itself doesn't need to be.

* * *

### **Exercise 10: Generic array**

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

**Explanation:**

*   Cannot directly create `new T[]` → cast from `Object[]`.

* * *

### **Exercise 11: Generic stack**

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

**Explanation:**

*   Works for any type `T`.
*   Uses `ArrayList` internally.

* * *

### **Exercise 12: Generic queue**

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

* * *

### **Exercise 13: Generic swap method**

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

* * *

### **Exercise 14: Bounded wildcard for reading**

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

* * *

### **Exercise 15: Generic map-like structure**

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

* * *

### **Exercise 16: Generic bounded type for numbers**

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

* * *

### **Exercise 17: Generic method with multiple parameters**

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

* * *

### **Exercise 18: Recursive generic type**

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

* * *

### **Exercise 19: Generic comparator**

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

* * *

### **Exercise 20: Generic factory pattern**

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

*   `Class<T>` allows dynamic type creation.
*   Uses reflection to call constructor.
