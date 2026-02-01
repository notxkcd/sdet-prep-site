---
title: "Top 70 Java Collections Interview Questions With Answers (Java 21 Edition)"
date: 2026-02-01
draft: false
---

## Questions

1. <a id="q-1"></a>[1) What is the Java Collection Framework? Why it is introduced?](#a-1)
2. <a id="q-2"></a>[2) What is the root level interface of the Java collection framework?](#a-2)
3. <a id="q-3"></a>[3) What are the **four**** **main core interfaces of the Java collection framework?](#a-3)
4. <a id="q-4"></a>[4) Explain the class hierarchy of Java collection framework?](#a-4)
5. <a id="q-5"></a>[5) Why Map is not inherited from Collection interface although it is a part of Java collection framework?](#a-5)
6. <a id="q-6"></a>[6) What is Iterable interface?](#a-6)
7. <a id="q-7"></a>[7) What are the characteristics of List?](#a-7)
8. <a id="q-8"></a>[8) What are the major implementations of List interface?](#a-8)
9. <a id="q-9"></a>[9) What are the characteristics of ArrayList?](#a-9)
10. <a id="q-10"></a>[10) What are the three marker interfaces implemented by ArrayList?](#a-10)
11. <a id="q-11"></a>[11) What is the default initial capacity of ArrayList?](#a-11)
12. <a id="q-12"></a>[12) What is the main drawback of ArrayList?](#a-12)
13. <a id="q-13"></a>[13) What are the differences between array and ArrayList?](#a-13)
14. <a id="q-14"></a>[14) How Vector is different from ArrayList?](#a-14)
15. <a id="q-15"></a>[15) Why it is recommended not to use Vector class in your code?](#a-15)
16. <a id="q-16"></a>[16) What are the differences between ArrayList and Vector?](#a-16)
17. <a id="q-17"></a>[17) What are the characteristics of Queue?](#a-17)
18. <a id="q-18"></a>[18) Mention the important methods of Queue?](#a-18)
19. <a id="q-19"></a>[19) How Queue differs from List?](#a-19)
20. <a id="q-20"></a>[20) Which popular collection type implements both List and Queue?](#a-20)
21. <a id="q-21"></a>[21) What are the Characteristics of LinkedList?](#a-21)
22. <a id="q-22"></a>[22) What are the differences between ArrayList and LinkedList?](#a-22)
23. <a id="q-23"></a>[23) What is the PriorityQueue?](#a-23)
24. <a id="q-24"></a>[24) What are Deque and ArrayDeque? When they are introduced in Java?](#a-24)
25. <a id="q-25"></a>[25) What are the characteristics of sets?](#a-25)
26. <a id="q-26"></a>[26) What are the major implementations of Set interface?](#a-26)
27. <a id="q-27"></a>[27) What are the differences between List and Set?](#a-27)
28. <a id="q-28"></a>[28) What are the characteristics of HashSet?](#a-28)
29. <a id="q-29"></a>[29) How HashSet works internally in Java?](#a-29)
30. <a id="q-30"></a>[30) What are the characteristics of LinkedHashSet?](#a-30)
31. <a id="q-31"></a>[31) When you prefer LinkedHashSet over HashSet?](#a-31)
32. <a id="q-32"></a>[32) How LinkedHashSet works internally in Java?](#a-32)
33. <a id="q-33"></a>[33) What is SortedSet? Give one Example?](#a-33)
34. <a id="q-34"></a>[34) What is NavigableSet? Give one example?](#a-34)
35. <a id="q-35"></a>[35) What are the characteristics of TreeSet?](#a-35)
36. <a id="q-36"></a>[36) How HashSet, LinkedHashSet and TreeSet differ from each other?](#a-36)
37. <a id="q-37"></a>[37) What are the differences between Iterator and ListIterator?](#a-37)
38. <a id="q-38"></a>[38) How Map interface is different from other three primary interfaces of Java collection framework – List, Set and Queue?](#a-38)
39. <a id="q-39"></a>[39) What are the popular implementations of Map interface?](#a-39)
40. <a id="q-40"></a>[40) What are the characteristics of HashMap?](#a-40)
41. <a id="q-41"></a>[41) How HashMap works internally in Java?](#a-41)
42. <a id="q-42"></a>[42) What is hashing?](#a-42)
43. <a id="q-43"></a>[43) What is the initial capacity of HashMap?](#a-43)
44. <a id="q-44"></a>[44) What is the load factor of HashMap?](#a-44)
45. <a id="q-45"></a>[45) What is the threshold of an HashMap? How it is calculated?](#a-45)
46. <a id="q-46"></a>[46) What is rehashing?](#a-46)
47. <a id="q-47"></a>[47) How initial capacity and load factor affect the performance of an HashMap?](#a-47)
48. <a id="q-48"></a>[48) What are the differences between HashSet and HashMap?](#a-48)
49. <a id="q-49"></a>[49) What are the differences between HashMap and HashTable?](#a-49)
50. <a id="q-50"></a>[50) How do you remove duplicate elements from an ArrayList in Java?](#a-50)
51. <a id="q-51"></a>[51) Which Collection type do you suggest me If I want a sorted collection of objects with no duplicates?](#a-51)
52. <a id="q-52"></a>[52) What are the differences between Fail-Fast Iterators and Fail-Safe Iterators?](#a-52)
53. <a id="q-53"></a>[53) How do you convert an Array to ArrayList and an ArrayList to Array?](#a-53)
54. <a id="q-54"></a>[54) What is the difference between Collection and Collections?](#a-54)
55. <a id="q-55"></a>[55) How collections are different from Java 8 streams?](#a-55)
56. <a id="q-56"></a>[56) How do you convert HashMap to ArrayList in Java?](#a-56)
57. <a id="q-57"></a>[57) What keySet(), values() and entrySet() methods do?](#a-57)
58. <a id="q-58"></a>[58) What is the difference between Iterator and Java 8 Spliterator?](#a-58)
59. <a id="q-59"></a>[59) How do you sort an ArrayList?](#a-59)
60. <a id="q-60"></a>[60) What are the differences between HashMap and ConcurrentHashMap?](#a-60)
61. <a id="q-61"></a>[61) How do you make collections read-only or unmodifiable?](#a-61)
62. <a id="q-62"></a>[62) How do you reverse an ArrayList in Java?](#a-62)
63. <a id="q-63"></a>[63) What are the differences between synchronized HashMap, HashTable and ConcurrentHashMap?](#a-63)
64. <a id="q-64"></a>[64) How do you sort HashMap by keys?](#a-64)
65. <a id="q-65"></a>[65) How do you sort HashMap by values?](#a-65)
66. <a id="q-66"></a>[66) How do you merge two maps with same keys?](#a-66)
67. <a id="q-67"></a>[67) What do you know about Java 9 immutable collections? How they are different from unmodifiable collections returned by the Collections wrapper methods?](#a-67)
68. <a id="q-68"></a>[68) What do you know about Java 10 List.copyOf(), Set.copyOf() and Map.copyOf() methods? Why they are introduced?](#a-68)
69. <a id="q-69"></a>[69) What are the differences between Enumeration And Iterator?](#a-69)
70. <a id="q-70"></a>[70) Which is of type RandomAccess – ArrayList, LinkedList, HashSet and HashMap?](#a-70)

---

# Top 70 Java Collections Interview Questions With Answers
* * *

<a id="a-1"></a>[**1) What is the Java Collection Framework? Why it is introduced?**](#q-1)

Java Collection Framework is a centralized and unified theme to store and manipulate the group of objects. Java Collection Framework provides some predefined classes and interfaces to handle the group of objects. Using this collection framework, you can store the objects as a list or as a set or as a queue or as a map and perform operations like adding or removing or retrieving the objects without much hard work.

Java Collection Framework or simply collections are nothing but the group of objects stored in well defined manner. Earlier, arrays are used to store these group of objects. But, arrays are not re-sizable. They are of fixed size. Size of the arrays can not be changed once they are defined. This causes lots of problem while handling the group of objects. To overcome this drawback of arrays, Java collection framework is introduced in Java from JDK 1.2.

```java
// Modern way (Java 21+) to create a simple list
List<String> frameworkParts = List.of("Interfaces", "Implementations", "Algorithms");
System.out.println(frameworkParts);
```

Although, there were classes like `Dictionary`, `Vector`, `Stack` and `Properties` which handle group of objects better than the arrays. But, each of them handle the objects differently. The way you use `Dictionary` class is totally different from the way you use **`Stack`** class and the way you use **`Vector`** class is different from the way you use `Properties` class. Hence, there needed a central and unifying theme to handle the group of objects. The collection framework is the answer to that.

<a id="a-2"></a>[**2) What is the root level interface of the Java collection framework?**](#q-2)

`java.util.Collection` is the root level interface of the Java collection framework.

```java
Collection<String> col = new ArrayList<>();
col.add("Java 21");
System.out.println(col.size());
```

<a id="a-3"></a>[**3) What are the **four**** **main core interfaces of the Java collection framework?**](#q-3)

The whole Java collection framework is divided into four interfaces – `List`, `Queue`, `Set` and `Map`. In which all except `Map` are inherited from `java.util.Collection` interface.

List : It handles the sequential list of objects. `ArrayList`, `Vector` and `LinkedList` are the major implementation of this interface.

Queue : It handles the special group of objects in which elements are added from one end and removed from another end. `LinkedList` and `PriorityQueue` classes implement this interface.

Set : It handles the group of objects which must contain only unique elements. The major implementations of this interface are `HashSet`, `LinkedHashSet` and `TreeSet`.

Map : This is the one interface in Java Collection Framework which is not inherited from `Collection` interface. It handles the group of objects as key-value pairs. It is implemented by `HashMap`, `LinkedHashMap` and `TreeMap`.

```java
List<String> list = new ArrayList<>();
Queue<String> queue = new LinkedList<>();
Set<String> set = new HashSet<>();
Map<Integer, String> map = new HashMap<>();
```

<a id="a-4"></a>[**4) Explain the class hierarchy of Java collection framework?**](#q-4)

Below diagram shows the class hierarchy of collection framework.

[![Collection framework class hierarchy](https://i0.wp.com/javaconceptoftheday.com/wp-content/uploads/2014/11/CollectionHierarchy.png?resize=776%2C839&ssl=1)](https://i0.wp.com/javaconceptoftheday.com/wp-content/uploads/2014/11/CollectionHierarchy.png?ssl=1)

*Note: From Java 21, we have **Sequenced Collections** which adds `SequencedCollection`, `SequencedSet`, and `SequencedMap` to the hierarchy.*

<a id="a-5"></a>[**5) Why Map is not inherited from Collection interface although it is a part of Java collection framework?**](#q-5)

Map is a collection of key-value pairs where as other collection types like List, Set and Queue are the collection of values. Collection interface has the methods which support only the collection of values but not the collection of key-value pairs. That’s why Map doesn’t inherit Collection interface.

<a id="a-6"></a>[**6) What is Iterable interface?**](#q-6)

`Iterable` interface is a member of `java.lang` package which is extended by `java.util.Collection` interface which is nothing but the root level interface of the Java collection framework. `Iterable` interface has only one method called `iterator()` which returns an `Iterator` object, using that object you can iterate over the elements of Collection. ( `forEach()` and `spliterator()` methods are added to this interface from Java 8). That means these methods will be available in all collection types which are inherited from `Collection` interface.

```java
Iterable<String> it = List.of("A", "B", "C");
it.forEach(System.out::println);
```

<a id="a-7"></a>[**7) What are the characteristics of List?**](#q-7)

*   List Interface represents an ordered or sequential collection of objects.
*   Elements of the lists are ordered using Zero based index.
*   Elements of the lists can be randomly accessed. i.e elements can be inserted at or removed from or retrieved from a specific position using integer index.
*   A list may contain duplicate elements.
*   A list may have multiple null elements.

<a id="a-8"></a>[**8) What are the major implementations of List interface?**](#q-8)

*   ArrayList
*   Vector
*   LinkedList

<a id="a-9"></a>[**9) What are the characteristics of ArrayList?**](#q-9)

*   Size of the ArrayList is not fixed. It can increase and decrease dynamically as we add or delete the elements.
*   Elements are placed according to Zero-based index. That means, first element will be placed at index 0 and last element at index n-1, where ‘n’ is the size of the ArrayList.
*   ArrayList can have any number of null elements.
*   ArrayList can have duplicate elements.
*   As ArrayList implements `RandomAccess`, you can get, set, insert and remove elements of the ArrayList from any arbitrary position.
*   ArrayList is not synchronized. That means, multiple threads can use same ArrayList simultaneously.

```java
ArrayList<Integer> numbers = new ArrayList<>();
numbers.add(10);
numbers.add(0, 5); // Insert at index 0
System.out.println(numbers.get(1)); // Access by index
```

<a id="a-10"></a>[**10) What are the three marker interfaces implemented by ArrayList?**](#q-10)

RandomAccess, Cloneable and Serializable.

<a id="a-11"></a>[**11) What is the default initial capacity of ArrayList?**](#q-11)

Default initial capacity of an ArrayList is 10. This capacity increases automatically as we add more elements to ArrayList. You can also specify initial capacity of an ArrayList while creating it.

<a id="a-12"></a>[**12) What is the main drawback of ArrayList?**](#q-12)

When you insert an element in the middle of the ArrayList, the elements at the right side of that position are shifted one position right and when you delete an element, they will be shifted one position left. This feature of the ArrayList causes some performance issues as shifting of elements is time consuming if ArrayList has lots of elements.

<a id="a-13"></a>[**13) What are the differences between array and ArrayList?**](#q-13)



* Array: Arrays are static in nature. Arrays are fixed length data structures. You can’t change their size once they are created.
  * ArrayList: ArrayList is dynamic in nature. Its size is automatically increased if you add elements beyond its capacity.
* Array: Arrays can hold both primitives as well as objects.
  * ArrayList: ArrayList can hold only objects.
* Array: Arrays can be iterated only through for loop or for-each loop.
  * ArrayList: ArrayList provides iterators to iterate through their elements.
* Array: The size of an array is checked using length attribute.
  * ArrayList: The size of an ArrayList can be checked using size() method.
* Array: Array gives constant time performance for both add and get operations.
  * ArrayList: ArrayList also gives constant time performance for both add and get operations provided adding an element doesn’t trigger resize.
* Array: Arrays don’t support generics.
  * ArrayList: ArrayList supports generics.
* Array: Arrays are not type safe.
  * ArrayList: ArrayList are type safe.
* Array: Arrays can be multi-dimensional.
  * ArrayList: ArrayList can’t be multi-dimensional.
* Array: Elements are added using assignment operator.
  * ArrayList: Elements are added using add() method.

```java
// Array
String[] arr = new String[5];
arr[0] = "Java";

// ArrayList
ArrayList<String> list = new ArrayList<>();
list.add("Java");
```

See More : [Array Vs ArrayList](https://javaconceptoftheday.com/differences-between-array-vs-arraylist-in-java/)

<a id="a-14"></a>[**14) How Vector is different from ArrayList?**](#q-14)

The Vector Class is also dynamically grow-able and shrink-able collection of objects like an ArrayList class. But, the main difference between ArrayList and Vector is that Vector class is synchronized. That means, Vector is thread safe. only one thread can enter into vector object at any moment of time.

[![ArrayList Vs Vector In Java](https://i0.wp.com/javaconceptoftheday.com/wp-content/uploads/2014/12/ArrayListVsVector.png?resize=654%2C493&ssl=1)](https://i0.wp.com/javaconceptoftheday.com/wp-content/uploads/2014/12/ArrayListVsVector.png?ssl=1)

<a id="a-15"></a>[**15) Why it is recommended not to use Vector class in your code?**](#q-15)

Vector class is preferred over ArrayList class when you are developing a multi threaded application. But, precautions need to be taken because vector may reduce the performance of your application as it is thread safe and only one thread is allowed to have object lock at any moment of time and remaining threads have to wait until a thread releases the object lock. So, it is always recommended that if you don’t need thread safe environment, it is better to use ArrayList class than the Vector class.

And also Vector class is often considered as obsolete or “Due for Deprecation” by many experienced Java developers. They always recommend and advise not to use Vector class in your code. They prefer using ArrayList over Vector class.

<a id="a-16"></a>[**16) What are the differences between ArrayList and Vector?**](#q-16)



* ArrayList: ArrayList is not thread safe.
  * Vector: Vector is thread safe.
* ArrayList: As ArrayList is not synchronized, it gives better performance than Vector.
  * Vector: As Vector is synchronized, it is slightly slower than ArrayList.
* ArrayList: ArrayList is not a legacy code.
  * Vector: Vector class is considered as legacy, due for deprecation.


See More : [ArrayList Vs Vector](https://javaconceptoftheday.com/difference-between-arraylist-and-vector-class/)

<a id="a-17"></a>[**17) What are the characteristics of Queue?**](#q-17)

*   Queue is a data structure in which elements are added from one end called tail and removed from another end called head.
*   Queue is first-in-first-out type of data structure. That means an element which is inserted first will be the first element to be removed from the queue.
*   null elements are not allowed in the queue.
*   Queue can have duplicate elements.
*   Queue is not random access. i.e you can’t set or insert or get elements at an arbitrary positions.

<a id="a-18"></a>[**18) Mention the important methods of Queue?**](#q-18)



* Operation: Add an element to the queue.
  * Throws An Exception If operation is not possible: add()
  * Returns null or false if operation is not possible: offer()
* Operation: Retrieve an element from the head of the queue.
  * Throws An Exception If operation is not possible: element()
  * Returns null or false if operation is not possible: peek()
* Operation: Retrieve And Remove an element from the head of the queue.
  * Throws An Exception If operation is not possible: remove()
  * Returns null or false if operation is not possible: poll()

```java
Queue<String> q = new LinkedList<>();
q.offer("First");
q.offer("Second");
System.out.println(q.poll()); // Prints "First"
```

<a id="a-19"></a>[**19) How Queue differs from List?**](#q-19)



* List: Random Access. i.e you can set, get, add or remove elements from an arbitrary position.
  * Queue: No random access. i.e you can’t set, get, add or remove elements from an arbitrary position.
* List: Can have null elements.
  * Queue: No null elements.
* List: It is an ordered collection of objects where elements are added or removed or retrieved randomly using an integer based index.
  * Queue: It is also an ordered collection of objects where elements are added from one end and removed or retrieved from another end.


<a id="a-20"></a>[**20) Which popular collection type implements both List and Queue?**](#q-20)

LinkedList

<a id="a-21"></a>[**21) What are the Characteristics of LinkedList?**](#q-21)

*   Elements in the LinkedList are called as Nodes. Where each node consist of three parts – Reference To Previous Element, Value Of The Element and Reference To Next Element. Below diagram shows how LinkedList looks like.

[![LinkedList Data Structure](https://i0.wp.com/javaconceptoftheday.com/wp-content/uploads/2014/12/HowLinkedListWorks.png?resize=805%2C360&ssl=1)](https://i0.wp.com/javaconceptoftheday.com/wp-content/uploads/2014/12/HowLinkedListWorks.png?ssl=1)

*   Reference To Previous Element of first node and Reference To Next Element of last node are null as there will be no elements before the first node and after the last node.
*   You can add or remove or retrieve the elements at both the ends and also in the middle of the LinkedList.
*   Insertion and removal operations in LinkedList are faster than the ArrayList. Because in LinkedList, there is no need to shift the elements after each insertion and removal. only references of next and previous elements need to be changed.
*   Retrieval of the elements is very slow in LinkedList as compared to ArrayList. Because in LinkedList, you have to traverse from beginning or end (whichever is closer to the element) to reach the element.
*   The LinkedList can be used as stack. It has the methods pop() and push() which make it to function as Stack.
*   The LinkedList can also be used as ArrayList, Queue, Single linked list and doubly linked list.
*   LinkedList can have multiple null elements.
*   LinkedList can have duplicate elements.
*   LinkedList class in Java is not of type Random Access. i.e the elements can not be accessed randomly. To access the given element, you have to traverse the LinkedList from beginning or from end (whichever is closer to the element) to reach the given element.

```java
LinkedList<String> linkedList = new LinkedList<>();
linkedList.addFirst("Head");
linkedList.addLast("Tail");
// In Java 21, LinkedList implements SequencedCollection
linkedList.addFirst("New Head"); 
System.out.println(linkedList.getFirst());
```

<a id="a-22"></a>[**22) What are the differences between ArrayList and LinkedList?**](#q-22)



* ArrayList: ArrayList is an index based data structure where each element is associated with an index.
  * LinkedList: Elements in the LinkedList are called as nodes, where each node consists of three things – Reference to previous element, Actual value of the element and Reference to next element.
* ArrayList: Insertions and Removals in the middle of the ArrayList are very slow. Because after each insertion and removal, elements need to be shifted.
  * LinkedList: Insertions and Removals from any position in the LinkedList are faster than the ArrayList. Because there is no need to shift the elements after every insertion and removal. Only references of previous and next elements are to be changed.
* ArrayList: Insertion and removal operations in ArrayList are of order O(n).
  * LinkedList: Insertion and removal in LinkedList are of order O(1).
* ArrayList: Retrieval of elements in the ArrayList is faster than the LinkedList . Because all elements in ArrayList are index based.
  * LinkedList: Retrieval of elements in LinkedList is very slow compared to ArrayList. Because to retrieve an element, you have to traverse from beginning or end (Whichever is closer to that element) to reach that element.
* ArrayList: Retrieval operation in ArrayList is of order of O(1).
  * LinkedList: Retrieval operation in LinkedList is of order of O(n).
* ArrayList: ArrayList is of type Random Access. i.e elements can be accessed randomly.
  * LinkedList: LinkedList is not of type Random Access. i.e elements can not be accessed randomly. you have to traverse from beginning or end to reach a particular element.
* ArrayList: ArrayList can not be used as a Stack or Queue.
  * LinkedList: LinkedList, once defined, can be used as ArrayList, Stack, Queue, Singly Linked List and Doubly Linked List.
* ArrayList: ArrayList requires less memory compared to LinkedList. Because ArrayList holds only actual data and it’s index.
  * LinkedList: LinkedList requires more memory compared to ArrayList. Because, each node in LinkedList holds data and reference to next and previous elements.
* ArrayList: If your application does more retrieval than the insertions and deletions, then use ArrayList.
  * LinkedList: If your application does more insertions and deletions than the retrieval, then use LinkedList.


See More : [ArrayList Vs LinkedList](https://javaconceptoftheday.com/arraylist-vs-linkedlist-java/)

<a id="a-23"></a>[**23) What is the PriorityQueue?**](#q-23)

PriorityQueue is a class in Java collection framework which implements Queue interface.

The PriorityQueue is a queue in which elements are ordered according to specified Comparator. You have to specify this Comparator while creating a PriorityQueue itself. If no Comparator is specified, elements will be placed in their natural order.

The PriorityQueue is a special type of queue because it is not a First-In-First-Out (FIFO) as in the normal queues. But, elements are placed according to supplied Comaparator.

The PriorityQueue does not allow null elements. Elements in the PriorityQueue must be of Comparable type, If you insert the elements which are not Comparable, you will get ClassCastException at run time.

The head element of the PriorityQueue is always the least element and tail element is always the largest element according to specified Comparator.

```java
PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());
pq.add(10);
pq.add(20);
pq.add(15);
System.out.println(pq.poll()); // Prints 20 (largest because of reverseOrder)
```

<a id="a-24"></a>[**24) What are Deque and ArrayDeque? When they are introduced in Java?**](#q-24)

Deque is an interface which extends the Queue interface and ArrayDeque is the class which implements Deque interface. Both are introduced from Java 6.

The Deque is the short name for “Double Ended Queue“. As the name suggest, Deque is a linear collection of objects which supports insertion and removal of elements from both the ends. The Deque interface defines the methods needed to insert, retrieve and remove the elements from both the ends.

The main advantage of Deque is that you can use it as both **Queue** (FIFO) as well as **Stack** (LIFO). The Deque interface has all those methods required for FIFO and LIFO operations. ArrayDeque class provides implementations for all these methods.

```java
Deque<String> deque = new ArrayDeque<>();
deque.addFirst("Start");
deque.addLast("End");
System.out.println(deque.removeFirst());
```

<a id="a-25"></a>[**25) What are the characteristics of sets?**](#q-25)

*   Set contains only unique elements. It does not allow duplicates.
*   Set can have maximum one null element.
*   Random access of elements is not possible.
*   Order of elements in a set is implementation dependent. HashSet maintains no order. TreeSet elements are ordered according to supplied Comparator (If no Comparator is supplied, elements will be placed in their natural order) and LinkedHashSet maintains insertion order.
*   Set interface contains only methods inherited from Collection interface. It does not have it’s own methods. But, applies restriction on methods so that duplicate elements are always avoided.
*   One more good thing about Set interface is that the stronger contract between equals() and hashCode() methods. According to this contract, you can compare two Set instances of different implementation types (HashSet, TreeSet and LinkedHashSet).
*   Two set instances, irrespective of their implementation types, are said to be equal if they contain same elements.

<a id="a-26"></a>[**26) What are the major implementations of Set interface?**](#q-26)

There are three major implementations of Set interface.

*   HashSet
*   LinkedHashSet
*   TreeSet

<a id="a-27"></a>[**27) What are the differences between List and Set?**](#q-27)



* List: List can have duplicate elements.
  * Set: Set doesn’t allow duplicate elements. It allows only unique elements.
* List: List elements are ordered according zero-based index.
  * Set: Order of elements in a set is implementation dependent. HashSet maintains no order. TreeSet elements are ordered according to supplied Comparator (If no Comparator is supplied, elements will be placed in their natural ascending order) and LinkedHashSet maintains insertion order.
* List: List can have any number of null elements.
  * Set: Set can have maximum one null element.
* List: List elements can be accessed randomly.
  * Set: Set elements can’t be accessed randomly.
* List: Ex : ArrayList, LinkedList
  * Set: Ex : HashSet, LinkedHashSet, TreeSet


<a id="a-28"></a>[**28) What are the characteristics of HashSet?**](#q-28)

*   HashSet implements Set interface.
*   It is a collection of objects which contains only unique elements. It does not allow duplicate elements. If you try to insert a duplicate element, older element will be overwritten.
*   HashSet class internally uses HashMap to store the objects. The elements you enter into HashSet will be stored as keys of HashMap and their values will be a constant.
*   HashSet can have maximum one null element.
*   HashSet doesn’t maintain any order. The order of the elements will be largely unpredictable. And it also doesn’t guarantee that order will remain constant over time.
*   HashSet offers constant time performance for insertion, removal and retrieval operations.
*   HashSet is not synchronized. If you want synchronized HashSet, use Collections.synchronizedSet() method.

<a id="a-29"></a>[**29) How HashSet works internally in Java?**](#q-29)

**HashSet** internally uses HashMap to store it’s elements. Whenever you create a HashSet object, one **HashMap** object associated with it is also created. This HashMap object is used to store the elements you enter in the HashSet. The elements you add into HashSet are stored as keys of this HashMap object. The value associated with those keys will be a constant called PRESENT.

[![How HashSet works internally in Java?](https://i0.wp.com/javaconceptoftheday.com/wp-content/uploads/2015/01/HowHashSetWorks.png?resize=792%2C561&ssl=1)](https://i0.wp.com/javaconceptoftheday.com/wp-content/uploads/2015/01/HowHashSetWorks.png?ssl=1)

See More : [How HashSet works internally in Java?](https://javaconceptoftheday.com/how-hashset-works-internally-in-java/)

<a id="a-30"></a>[**30) What are the characteristics of LinkedHashSet?**](#q-30)

*   LinkedHashSet internally uses LinkedHashMap to store it’s elements just like HashSet which internally uses HashMap to store it’s elements.
*   LinkedHashSet maintains insertion order. This is the main difference between LinkedHashSet and HashSet.
*   LinkedHashSet also gives constant time performance for insertion, removal and retrieval operations. The performance of LinkedHashSet is slightly less than the HashSet as it has to maintain linked list internally to order it’s elements.
*   LinkedHashSet doesn’t allow duplicate elements and allows maximum one null element.
*   Iterator returned by LinkedHashSet is fail-fast. i.e if the LinkedHashSet is modified at any time after the Iterator is created, it throws ConcurrentModificationException.
*   LinkedHashSet is not synchronized. To get the synchronized LinkedHashSet, use Collections.synchronizedSet() method.

<a id="a-31"></a>[**31) When you prefer LinkedHashSet over HashSet?**](#q-31)

LinkedHashSet is preferred over HashSet if you want a unique collection of objects in an insertion order.

<a id="a-32"></a>[**32) How LinkedHashSet works internally in Java?**](#q-32)

LinkedHashSet is an extended version of HashSet. HashSet doesn’t follow any order where as LinkedHashSet maintains insertion order. HashSet uses HashMap object internally to store it’s elements where as LinkedHashSet uses LinkedHashMap object internally to store and process it’s elements.

[![How LinkedHashSet Works Internally In Java?](https://i0.wp.com/javaconceptoftheday.com/wp-content/uploads/2015/01/HowLinkedHashSetWorks.png?resize=745%2C836&ssl=1)](https://i0.wp.com/javaconceptoftheday.com/wp-content/uploads/2015/01/HowLinkedHashSetWorks.png?ssl=1)

See More : [How LinkedHashSet works internally in Java?](https://javaconceptoftheday.com/how-linkedhashset-works-internally-in-java/)

<a id="a-33"></a>[**33) What is SortedSet? Give one Example?**](#q-33)

The SortedSet is an interface which extends Set interface. It’s elements are sorted, that’s why name SortedSet. The elements of the SortedSet are sorted according to supplied Comparator. This Comparator is supplied while creating a SortedSet. If you don’t supply Comparator, elements will be placed in their natural order.

TreeSet is the SortedSet.

<a id="a-34"></a>[**34) What is NavigableSet? Give one example?**](#q-34)

The NavigableSet is an interface which extends SortedSet interface which in turn extends Set interface. 

The NavigableSet is a SortedSet with navigation facilities. The NavigableSet interface provides many methods through them you can easily find closest matches of any given element. It has the methods to find out less than, less than or equal to, greater than and greater than or equal of any element in a SortedSet.

TreeSet is also of type NavigableSet.

<a id="a-35"></a>[**35) What are the characteristics of TreeSet?**](#q-35)

*   The elements in TreeSet are sorted according to specified Comparator. If no Comparator is specified, elements will be placed according to their natural ascending order.
*   Elements inserted in the TreeSet must be of Comparable type and elements must be mutually comparable. If the elements are not mutually comparable, you will get ClassCastException at run time.
*   TreeSet does not allow even a single null element.
*   TreeSet is not synchronized. To get a synchronized TreeSet, use Collections.synchronizedSortedSet() method.
*   TreeSet gives performance of order log(n) for insertion, removal and retrieval operations.
*   Iterator returned by TreeSet is of fail-fast nature. That means, If TreeSet is modified after the creation of Iterator object, you will get ConcurrentModificationException.
*   TreeSet internally uses TreeMap to store it’s elements just like HashSet and LinkedHashSet which use HashMap and LinkedHashMap respectively to store their elements.

```java
TreeSet<String> treeSet = new TreeSet<>();
treeSet.add("Banana");
treeSet.add("Apple");
treeSet.add("Cherry");
System.out.println(treeSet); // Prints [Apple, Banana, Cherry]
```

<a id="a-36"></a>[**36) How HashSet, LinkedHashSet and TreeSet differ from each other?**](#q-36)



* HashSet: HashSet uses HashMap internally to store it’s elements.
  * LinkedHashSet: LinkedHashSet uses  LinkedHashMap internally to store it’s elements.
  * TreeSet: TreeSet uses TreeMap internally to store it’s elements.
* HashSet: HashSet doesn’t maintain any order of elements.
  * LinkedHashSet: LinkedHashSet maintains insertion order of elements. i.e elements are placed as they are inserted.
  * TreeSet: TreeSet orders the elements according to supplied Comparator. If no Comparator is supplied, elements will be placed in their natural ascending order.
* HashSet: HashSet gives better performance than the LinkedHashSet and TreeSet.
  * LinkedHashSet: The performance of LinkedHashSet is between HashSet and TreeSet. It’s performance is almost similar to HashSet. But slightly in the slower side as it also maintains LinkedList internally to maintain the insertion order of elements.
  * TreeSet: TreeSet gives less performance than the HashSet and LinkedHashSet as it has to sort the elements after each insertion and removal operations.
* HashSet: HashSet gives performance of order O(1) for insertion, removal and retrieval operations.
  * LinkedHashSet: LinkedHashSet also gives performance of order O(1) for insertion, removal and retrieval operations.
  * TreeSet: TreeSet gives performance of order O(log(n)) for insertion, removal and retrieval operations.
* HashSet: HashSet uses equals() and hashCode() methods to compare the elements and thus removing the possible duplicate elements.
  * LinkedHashSet: LinkedHashSet also uses equals() and hashCode() methods to compare the elements.
  * TreeSet: TreeSet uses compare() or compareTo() methods to compare the elements and thus removing the possible duplicate elements. It doesn’t use equals() and hashCode() methods for comparison of elements.
* HashSet: HashSet allows maximum one null element.
  * LinkedHashSet: LinkedHashSet also allows maximum one null element.
  * TreeSet: TreeSet doesn’t allow even a single null element. If you try to insert null element into TreeSet, it throws NullPointerException.
* HashSet: HashSet requires less memory than LinkedHashSet and TreeSet as it uses only HashMap internally to store its elements.
  * LinkedHashSet: LinkedHashSet requires more memory than HashSet as it also maintains LinkedList along with HashMap to store its elements.
  * TreeSet: TreeSet also requires more memory than HashSet as it also maintains Comparator to sort the elements along with the TreeMap.
* HashSet: Use HashSet if you don’t want to maintain any order of elements.
  * LinkedHashSet: Use LinkedHashSet if you want to maintain insertion order of elements.
  * TreeSet: Use TreeSet if you want to sort the elements according to some Comparator.


See More : [HashSet Vs LinkedHashSet Vs TreeSet](https://javaconceptoftheday.com/hashset-vs-linkedhashset-vs-treeset-in-java/)

<a id="a-37"></a>[**37) What are the differences between Iterator and ListIterator?**](#q-37)



* Iterator: Using Iterator, you can traverse List, Set and Queue type of objects.
  * ListIterator: But using ListIterator, you can traverse only List objects.
* Iterator: Using Iterator, we can traverse the elements only in forward direction.
  * ListIterator: But, using ListIterator you can traverse the elements in both the directions – forward and backward.
* Iterator: Using Iterator you can only remove the elements from the collection.
  * ListIterator: But using ListIterator, you can perform modifications (insert, replace, remove) on the list.
* Iterator: You can’t iterate a list from the specified index using Iterator.
  * ListIterator: But using ListIterator, you can iterate a list from the specified index.
* Iterator: Methods : hasNext(), next() and remove()
  * ListIterator: Methods : hasNext(), hasPrevious(), next(), previous(), nextIndex(), previousIndex(), remove(), set(), add()

```java
List<String> list = new ArrayList<>(List.of("A", "B", "C"));
ListIterator<String> it = list.listIterator();
while(it.hasNext()) {
    System.out.println(it.next());
}
while(it.hasPrevious()) {
    System.out.println(it.previous()); // Bidirectional!
}
```

See More : [Iterator Vs ListIterator](https://javaconceptoftheday.com/difference-between-iterator-and-listiterator-in-java/)

<a id="a-38"></a>[**38) How Map interface is different from other three primary interfaces of Java collection framework – List, Set and Queue?**](#q-38)

The main difference between Map interface and other three top level interfaces is that it doesn’t inherit from Collection interface. Instead it starts it’s own interface hierarchy for maintaining the key-value associations.

Map stores the data as key-value pairs where each key is associated with a value where as other three interfaces – List, Set and Queue – store only values.

<a id="a-39"></a>[**39) What are the popular implementations of Map interface?**](#q-39)

*   HashMap
*   LinkedHashMap
*   TreeMap

<a id="a-40"></a>[**40) What are the characteristics of HashMap?**](#q-40)

*   HashMap holds the data in the form of key-value pairs where each key is associated with one value.
*   HashMap doesn’t allow duplicate keys. But it can have duplicate values.
*   HashMap can have multiple null values and only one null key.
*   HashMap is not synchronized. To get the synchronized _HashMap_, use _Collections.synchronizedMap()_ method.
*   HashMap maintains no order.
*   HashMap gives constant time performance of O(1) for the operations like _get()_ and _put()_ methods.
*   Default initial capacity of HashMap is 16.

```java
Map<String, Integer> map = new HashMap<>();
map.put("One", 1);
map.put("Two", 2);
System.out.println(map.get("One"));
```

<a id="a-41"></a>[**41) How HashMap works internally in Java?**](#q-41)

See here : [How HashMap works internally in Java?](https://javaconceptoftheday.com/how-hashmap-works-internally-in-java/)

<a id="a-42"></a>[**42) What is hashing?**](#q-42)

The whole HashMap data structure is based on the principle of Hashing. Hashing is nothing but the function or algorithm or method which when applied on any object/variable returns an unique integer value representing that object/variable. This unique integer value is called _hash code_. Hash function or simply hash said to be the best if it returns the same hash code each time it is called on the same object.

<a id="a-43"></a>[**43) What is the initial capacity of HashMap?**](#q-43)

The capacity of an HashMap is the number of buckets in the hash table. The initial capacity is the capacity of an HashMap at the time of its creation. The default initial capacity of the HashMap is 24 i.e 16. The capacity of the HashMap is doubled each time it reaches the threshold. i.e the capacity is increased to 25\=32, 26\=64, 27\=128….. when the threshold is reached.

<a id="a-44"></a>[**44) What is the load factor of HashMap?**](#q-44)

Load factor is the measure which decides when to increase the capacity of the HashMap. The default load factor is 0.75f.

<a id="a-45"></a>[**45) What is the threshold of an HashMap? How it is calculated?**](#q-45)

The threshold of an HashMap is the product of current capacity and load factor.

Threshold = (Current Capacity) \* (Load Factor)

For example, if the HashMap is created with initial capacity of 16 and load factor of 0.75f, then threshold will be,

Threshold = 16 \* 0.75 = 12

That means, the capacity of the _HashMap_ is increased from 16 to 32 after the 12th element (key-value pair) is added into the _HashMap_.

<a id="a-46"></a>[**46) What is rehashing?**](#q-46)

Rehashing is a process where new HashMap object with new capacity is created and all old elements (key-value pairs) are placed into new object after recalculating their hash code. Whenever HashMap reaches its threshold, rehashing takes place.

<a id="a-47"></a>[**47) How initial capacity and load factor affect the performance of an HashMap?**](#q-47)

Whenever _HashMap_ reaches its threshold, rehashing takes place. This process of rehashing is both space and time consuming. So, you must choose the initial capacity, by keeping the number of expected elements (key-value pairs) in mind, so that rehashing process doesn’t occur too frequently.

You also have to be very careful while choosing the load factor. According to _HashMap_ doc, the default load factor of 0.75f always gives best performance in terms of both space and time. For example,

If you choose load factor as 1.0f, then rehashing takes place after filling 100% of the current capacity. This may save the space but it will increase the retrieval time of existing elements. Suppose if you choose load factor as 0.5f, then rehashing takes place after filling 50% of the current capacity. This will increase the number of rehashing operations. This will further degrade the HashMap in terms of both space and time.

So, you have to be very careful while choosing the initial capacity and load factor of an _HashMap_ object. Choose the initial capacity and load factor such that they minimize the number of rehashing operations.

<a id="a-48"></a>[**48) What are the differences between HashSet and HashMap?**](#q-48)



* HashSet: HashSet implements Set interface.
  * HashMap: HashMap implements Map interface.
* HashSet: HashSet stores the data as objects.
  * HashMap: HashMap stores the data as key-value pairs.
* HashSet: HashSet internally uses HashMap.
  * HashMap: HashMap internally uses an array of Entry<K, V> objects.
* HashSet: HashSet doesn’t allow duplicate elements.
  * HashMap: HashMap doesn’t allow duplicate keys, but allows duplicate values.
* HashSet: HashSet allows only one null element.
  * HashMap: HashMap allows one null key and multiple null values.
* HashSet: Insertion operation requires only one object.
  * HashMap: Insertion operation requires two objects, key and value.
* HashSet: HashSet is slightly slower than HashMap.
  * HashMap: HashMap is slightly faster than HashSet.


See More : [HashMap Vs HashSet](https://javaconceptoftheday.com/differences-between-hashmap-vs-hashset-in-java/)

<a id="a-49"></a>[**49) What are the differences between HashMap and HashTable?**](#q-49)



* HashMap: HashMap is not synchronized and therefore it is not thread safe.
  * HashTable: HashTable is internally synchronized and therefore it is thread safe.
* HashMap: HashMap allows maximum one null key and any number of null values.
  * HashTable: HashTable doesn’t allow null keys and null values.
* HashMap: Iterators returned by the HashMap are fail-fast in nature.
  * HashTable: Enumeration returned by the HashTable are fail-safe in nature.
* HashMap: HashMap extends AbstractMap class.
  * HashTable: HashTable extends Dictionary class.
* HashMap: HashMap returns only iterators to traverse.
  * HashTable: HashTable returns both Iterator as well as Enumeration for traversal.
* HashMap: HashMap is fast.
  * HashTable: HashTable is slow.
* HashMap: HashMap is not a legacy class.
  * HashTable: HashTable is a legacy class.
* HashMap: HashMap is preferred in single threaded applications. If you want to use HashMap in multi threaded application, wrap it using Collections.synchronizedMap() method.
  * HashTable: Although HashTable is there to use in multi threaded applications, now a days it is not at all preferred. Because, ConcurrentHashMap is better option than HashTable.


See More : [HashMap Vs HashTable](https://javaconceptoftheday.com/differences-between-hashmap-and-hashtable-in-java/)

<a id="a-50"></a>[**50) How do you remove duplicate elements from an ArrayList in Java?**](#q-50)

Removing Duplicate Elements From ArrayList Using HashSet :

```java
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.stream.Collectors;

public class MainClass
{
    public static void main(String[] args)
    {
        ArrayList<String> listWithDuplicateElements = new ArrayList<>(List.of("JAVA", "J2EE", "JSP", "SERVLETS", "JAVA", "STRUTS", "JSP"));

        // Modern way using Stream API (Java 8+)
        List<String> listWithoutDuplicates = listWithDuplicateElements.stream()
                                             .distinct()
                                             .collect(Collectors.toList());

        // Using HashSet (as per original answer)
        HashSet<String> set = new HashSet<>(listWithDuplicateElements);
        ArrayList<String> listFromSet = new ArrayList<>(set);
        
        System.out.println("Result: " + listFromSet);
    }
}
```


See More : [How To Remove Duplicate Elements From ArrayList In Java?](https://javaconceptoftheday.com/how-to-remove-duplicate-elements-from-arraylist-in-java/)

<a id="a-51"></a>[**51) Which Collection type do you suggest me If I want a sorted collection of objects with no duplicates?**](#q-51)

TreeSet is the best suitable for such scenarios where you want a collection of objects with no duplicates and also sorted based on a particular data field.

<a id="a-52"></a>[**52) What are the differences between Fail-Fast Iterators and Fail-Safe Iterators?**](#q-52)



* Fail-Fast Iterators: Fail-Fast iterators doesn’t allow modifications of a collection while iterating over it.
  * Fail-Safe Iterators: Fail-Safe iterators allow modifications of a collection while iterating over it.
* Fail-Fast Iterators: These iterators throw ConcurrentModificationException if a collection is modified while iterating over it.
  * Fail-Safe Iterators: These iterators don’t throw any exceptions if a collection is modified while iterating over it.
* Fail-Fast Iterators: They use original collection to traverse over the elements of the collection.
  * Fail-Safe Iterators: They use copy of the original collection to traverse over the elements of the collection.
* Fail-Fast Iterators: These iterators don’t require extra memory.
  * Fail-Safe Iterators: These iterators require extra memory to clone the collection.
* Fail-Fast Iterators: Ex : Iterators returned by ArrayList, Vector, HashMap.
  * Fail-Safe Iterators: Ex : Iterator returned by ConcurrentHashMap.


See More : [Fail-Fast Vs Fail-Safe](https://javaconceptoftheday.com/fail-fast-and-fail-safe-iterators-in-java-with-examples/)

<a id="a-53"></a>[**53) How do you convert an Array to ArrayList and an ArrayList to Array?**](#q-53)

Array To ArrayList In Java :

a) Using `Arrays.asList()` Method :

```java
String[] array = {"ANDROID", "JSP", "JAVA"};
ArrayList<String> list = new ArrayList<>(Arrays.asList(array));
```


b) Using `Collections.addAll()` Method

```java
String[] array = {"ANDROID", "JSP", "JAVA"};
ArrayList<String> list = new ArrayList<>();
Collections.addAll(list, array);
```


c) Using Java 8 Streams

```java
String[] array = {"ANDROID", "JSP", "JAVA"};
List<String> list = Arrays.stream(array).toList(); // Java 16+ toList()
```


ArrayList To Array In Java :

```java
ArrayList<String> list = new ArrayList<>(List.of("JAVA", "JSP"));
String[] array = list.toArray(new String[0]); // Recommended way
```


<a id="a-54"></a>[**54) What is the difference between Collection and Collections?**](#q-54)

This is one of the most confusing Java interview question asked many a times to Java freshers. Most of time, this question has been asked to Java freshers to check their basic knowledge about the Java Collection Framework. This question seems confusing because both `Collection` and `Collections` look similar. Both are part of Java collection framework, but both serve different purpose. `Collection` is a top level interface of Java collection framework where as **`Collections`** is an utility class. Below table shows the difference between them.



* Collection: Collection is a root level interface of the Java Collection Framework. Most of the classes in Java Collection Framework inherit from this interface.
  * Collections: Collections is an utility class in java.util package. It consists of only static methods which are used to operate on objects of type Collection.
* Collection: List, Set and Queue are main sub interfaces of this interface.
  * Collections: Collections.max(), Collections.min(), Collections.sort() are some methods of Collections class.


See More : [Collection Vs Collections](https://javaconceptoftheday.com/difference-between-collection-and-collections-in-java/)

<a id="a-55"></a>[**55) How collections are different from Java 8 streams?**](#q-55)



* Collections: Collections are mainly used to store and group the data.
  * Streams: Streams are mainly used to perform operations on data.
* Collections: You can add or remove elements from collections.
  * Streams: You can’t add or remove elements from streams.
* Collections: Collections have to be iterated externally.
  * Streams: Streams are internally iterated.
* Collections: Collections can be traversed multiple times.
  * Streams: Streams are traversable only once.
* Collections: Collections are eagerly constructed.
  * Streams: Streams are lazily constructed.
* Collections: Ex : List, Set, Map…
  * Streams: Ex : filtering, mapping, matching…


See More : [Collections Vs Streams](https://javaconceptoftheday.com/collections-and-streams-in-java/)

<a id="a-56"></a>[**56) How do you convert HashMap to ArrayList in Java?**](#q-56)

```java
Map<Integer, String> map = new HashMap<>();
map.put(1, "A");
map.put(2, "B");

// Convert keys to ArrayList
List<Integer> keys = new ArrayList<>(map.keySet());

// Convert values to ArrayList
List<String> values = new ArrayList<>(map.values());

// Convert entries to ArrayList
List<Map.Entry<Integer, String>> entries = new ArrayList<>(map.entrySet());
```

See More : [Convert HashMap To ArrayList In Java](https://javaconceptoftheday.com/convert-hashmap-to-arraylist-in-java/)

<a id="a-57"></a>[**57) What keySet(), values() and entrySet() methods do?**](#q-57)

keySet(), values() and entrySet() are the methods of Map interface. Hence, they are available in all the implementations of Map interface – HashMap, LinkedHashMap and TreeMap.

keySet() : This method returns a set of keys.

values() : This method returns a Collection of values.

entrySet() : This method returns a set of key-value pairs.

<a id="a-58"></a>[**58) What is the difference between Iterator and Java 8 Spliterator?**](#q-58)



* Iterator: It performs only iteration.
  * Spliterator: It performs splitting as well as iteration.
* Iterator: Iterates elements one by one.
  * Spliterator: Iterates elements one by one or in bulk.
* Iterator: Most suitable for serial processing.
  * Spliterator: Most suitable for parallel processing.
* Iterator: Iterates only collection types.
  * Spliterator: Iterates collections, arrays and streams.
* Iterator: Size is unknown.
  * Spliterator: You can get exact size or estimate of the size.
* Iterator: Introduced in JDK 1.2.
  * Spliterator: Introduced in JDK 1.8.
* Iterator: You can’t extract properties of the iterating elements.
  * Spliterator: You can extract some properties of the iterating elements.
* Iterator: External iteration.
  * Spliterator: Internal iteration.


See More : [Iterator Vs Spliterator](https://javaconceptoftheday.com/differences-between-iterator-vs-spliterator-in-java-8/)

<a id="a-59"></a>[**59) How do you sort an ArrayList?**](#q-59)

An ArrayList can be sorted using `sort()` method of `Collections` class.

_Collections.sort()_ method has two overloaded forms. They are,

1) _sort(List<T> list)_  :  This method sorts the specified list according to natural ordering of its elements.

2) _sort(List<T> list, Comparator<? super T> c)_  : This method sorts the specified list according to supplied Comparator.

```java
ArrayList<String> list = new ArrayList<>(List.of("Z", "A", "M"));
Collections.sort(list); // Natural order
list.sort(Comparator.reverseOrder()); // Java 8+ List.sort()
```

See More : [How To Sort An ArrayList In Java?](https://javaconceptoftheday.com/how-to-sort-An-arraylist-in-java/)

<a id="a-60"></a>[**60) What are the differences between HashMap and ConcurrentHashMap?**](#q-60)



* HashMap: HashMap is not synchronized internally and hence it is not thread safe.
  * ConcurrentHashMap: ConcurrentHashMap is internally synchronized and hence it is thread safe.
* HashMap: HashMap is the part of Java collection framework since JDK 1.2.
  * ConcurrentHashMap: ConcurrentHashMap is introduced in JDK 1.5 as an alternative to HashTable.
* HashMap: HashMap allows maximum one null key and any number of null values.
  * ConcurrentHashMap: ConcurrentHashMap doesn’t allow even a single null key and null value.
* HashMap: Iterators returned by HashMap are fail-fast in nature.
  * ConcurrentHashMap: Iterators returned by ConcurrentHashMap are fail-safe in nature.
* HashMap: HashMap is faster.
  * ConcurrentHashMap: ConcurrentHashMap is slower.
* HashMap: Most suitable for single threaded applications.
  * ConcurrentHashMap: Most suitable for multi threaded applications.


See More : [HashMap Vs ConcurrentHashMap](https://javaconceptoftheday.com/hashmap-vs-concurrenthashmap-in-java/)

<a id="a-61"></a>[**61) How do you make collections read-only or unmodifiable?**](#q-61)

_java.util.Collections_ class provides some unmodifiable wrapper methods to create read only collections in Java. These methods take the _Collection_ type as an argument and returns read only view of the specified collection.

```java
List<String> list = new ArrayList<>();
list.add("Java");
List<String> unmodifiableList = Collections.unmodifiableList(list);
// unmodifiableList.add("Error"); // Throws UnsupportedOperationException
```

<a id="a-62"></a>[**62) How do you reverse an ArrayList in Java?**](#q-62)

An _ArrayList_ can be reversed using _Collections.reverse()_ method.

```java
ArrayList<String> list = new ArrayList<>(List.of("A", "B", "C"));
Collections.reverse(list);

// In Java 21, using SequencedCollection:
List<String> reversed = list.reversed(); // Returns a reversed view
```

<a id="a-63"></a>[**63) What are the differences between synchronized HashMap, HashTable and ConcurrentHashMap?**](#q-63)



* Locking Level
  * Synchronized HashMap: Object Level
  * HashTable: Object Level
  * ConcurrentHashMap: Segment Level
* Synchronized operations
  * Synchronized HashMap: All operations are synchronized.
  * HashTable: All operations are synchronized.
  * ConcurrentHashMap: Only update operations are synchronized.
* How many threads can enter into a map at a time?
  * Synchronized HashMap: Only one thread
  * HashTable: Only one thread
  * ConcurrentHashMap: By default, 16 threads can perform update operations and any number of threads can perform read operations at a time.
* Null Keys And Null Values
  * Synchronized HashMap: Allows one null key and any number of null values.
  * HashTable: Doesn’t allow null keys and null values.
  * ConcurrentHashMap: Doesn’t allow null keys and null values.
* Nature Of Iterators
  * Synchronized HashMap: Fail-Fast
  * HashTable: Fail-Safe
  * ConcurrentHashMap: Fail-Safe
* Introduced In?
  * Synchronized HashMap: JDK 1.2
  * HashTable: JDK 1.1
  * ConcurrentHashMap: JDK 1.5
* When To Use?
  * Synchronized HashMap: Use only when high level of data consistency is required in multi threaded environment.
  * HashTable: Don’t Use. Not recommended as it is a legacy class.
  * ConcurrentHashMap: Use in all multi threaded environment except where high level of data consistency is required.


See More : [Synchronized HashMap Vs HashTable Vs ConcurrentHashMap](https://javaconceptoftheday.com/synchronized-hashmap-vs-hashtable-vs-concurrenthashmap-in-java/)

<a id="a-64"></a>[**64) How do you sort HashMap by keys?**](#q-64)

```java
Map<Integer, String> map = new HashMap<>();
// ... add data
TreeMap<Integer, String> sortedMap = new TreeMap<>(map);
```

<a id="a-65"></a>[**65) How do you sort HashMap by values?**](#q-65)

```java
Map<String, Integer> map = new HashMap<>();
// ... add data
List<Map.Entry<String, Integer>> list = new ArrayList<>(map.entrySet());
list.sort(Map.Entry.comparingByValue());
```

<a id="a-66"></a>[**66) How do you merge two maps with same keys?**](#q-66)

```java
Map<String, Integer> map1 = new HashMap<>(Map.of("A", 1));
Map<String, Integer> map2 = new HashMap<>(Map.of("A", 2, "B", 3));

map2.forEach((key, value) -> 
    map1.merge(key, value, Integer::sum)
);
```

<a id="a-67"></a>[**67) What do you know about Java 9 immutable collections? How they are different from unmodifiable collections returned by the Collections wrapper methods?**](#q-67)

Immutable collections are the collections which can not be modified once they are created. Java 9 has introduced some static factory methods to easily create immutable collections. They are _List.of()_, _Set.of()_ and _Map.of()_.

```java
List<String> immutable = List.of("Java", "21");
// immutable.add("Error"); // Throws UnsupportedOperationException
```

<a id="a-68"></a>[**68) What do you know about Java 10 List.copyOf(), Set.copyOf() and Map.copyOf() methods? Why they are introduced?**](#q-68)

In Java 9, some static factory methods are introduced to easily create immutable collections. They are List.of(), Set.of() and Map.of(). These methods take individual elements as arguments and create immutable collections consisting of those elements. From Java 10, some more static factory methods are introduced to create immutable collections from existing collections. They are List.copyOf(), Set.copyOf() and Map.copyOf(). These methods take whole collection as an argument and create immutable copy of that collection.

```java
List<String> original = new ArrayList<>(List.of("A", "B"));
List<String> immutableCopy = List.copyOf(original);
```

<a id="a-69"></a>[**69) What are the differences between Enumeration And Iterator?**](#q-69)



* Enumeration: Using Enumeration, you can only traverse the collection. You can’t do any modifications to collection while traversing it.
  * Iterator: Using Iterator, you can remove an element of the collection while traversing it.
* Enumeration: Enumeration is introduced in JDK 1.0
  * Iterator: Iterator is introduced from JDK 1.2
* Enumeration: Enumeration is used to traverse the legacy classes like Vector, Stack and HashTable.
  * Iterator: Iterator is used to iterate most of the classes in the collection framework like ArrayList, HashSet, HashMap, LinkedList etc.
* Enumeration: Methods : hasMoreElements() and nextElement()
  * Iterator: Methods : hasNext(), next() and remove()
* Enumeration: Enumeration is fail-safe in nature.
  * Iterator: Iterator is fail-fast in nature.
* Enumeration: Enumeration is not safe and secured due to it’s fail-safe nature.
  * Iterator: Iterator is safer and secured than Enumeration.


See More : [Enumeration Vs Iterator In Java](https://javaconceptoftheday.com/differences-between-enumeration-vs-iterator-in-java/)

<a id="a-70"></a>[**70) Which is of type RandomAccess – ArrayList, LinkedList, HashSet and HashMap?**](#q-70)

ArrayList

Also Read : [Java Collections Interview Questions – Baeldung](https://www.baeldung.com/java-collections-interview-questions)

* * *
