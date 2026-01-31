---
title: "Euclidean Algorithm"
---

The `Euclidean Algorithm` is a highly efficient method for computing the `greatest common divisor (GCD)` of two integers, the largest number that divides them both without leaving a remainder. The algorithm is based on the principle that the `greatest common divisor` of two numbers does not change if the larger number is replaced by its difference with the smaller number. Since this replacement reduces the larger of the two numbers, repeating this process gives successively smaller pairs of numbers until the two numbers become equal.

This algorithm is one of the oldest algorithms in common use, appearing in Euclid's "Elements" around 300 BC.

## How it Works

### How it Works (Expanded)

The modern version of the `Euclidean Algorithm` uses the remainder of the division of the two numbers instead of subtraction. The principle is that `gcd(a, b) = gcd(b, a mod b)`. The algorithm repeatedly applies this property until the second number becomes 0. The `GCD` is the first number at that point.

---

Example: Find GCD of 48 and 18

1. gcd(48, 18):
- 48 = 2 <em> 18 + 12
- gcd(48, 18) -> gcd(18, 12)

2. gcd(18, 12):
- 18 = 1 </em> 12 + 6
- gcd(18, 12) -> gcd(12, 6)

3. gcd(12, 6):
- 12 = 2 <em> 6 + 0
- gcd(12, 6) -> gcd(6, 0)

4. gcd(6, 0):
- The second number is 0. The GCD is the first number.
- GCD = 6.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
def gcd_euclidean(a, b):
    """
    Computes the greatest common divisor (GCD) of a and b using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

# Example
# a = 48
# b = 18
# print(f"GCD of {a} and {b} is {gcd_euclidean(a, b)}") # Expected: 6
```

### Javascript

```javascript
function gcdEuclidean(a, b) {
    /</em><em>
     </em> Computes the greatest common divisor (GCD) of a and b using the Euclidean algorithm.
     <em>/
    while (b) {
        let temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// const a = 48;
// const b = 18;
// console.log(<code>GCD of ${a} and ${b} is ${gcdEuclidean(a, b)}</code>); // Expected: 6
```

### Typescript

```typescript
function gcdEuclideanTS(a: number, b: number): number {
    /</em><em>
     </em> Computes the greatest common divisor (GCD) of a and b using the Euclidean algorithm.
     */
    while (b) {
        let temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// const aTS = 48;
// const bTS = 18;
// console.log(<code>GCD of ${aTS} and ${bTS} is ${gcdEuclideanTS(aTS, bTS)}</code>); // Expected: 6
```

### Cpp

```cpp
#include <iostream>
#include <numeric> // std::gcd in C++17

// Manual implementation for clarity
int gcdEuclidean(int a, int b) {
    while (b) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// int main() {
//     int a = 48;
//     int b = 18;
//     std::cout << "GCD of " << a << " and " << b << " is " << gcdEuclidean(a, b) << std::endl; // 6
//     // Using std::gcd from C++17
//     // std::cout << "GCD using std::gcd: " << std::gcd(a, b) << std::endl;
// }
```

### Go

```go
package main

import "fmt"

func gcdEuclidean(a, b int) int {
    for b != 0 {
        a, b = b, a%b
    }
    return a
}

// func main() {
//     a := 48
//     b := 18
//     fmt.Printf("GCD of %d and %d is %d\n", a, b, gcdEuclidean(a, b)) // 6
// }
```

### D

```d
import std.stdio;
import std.numeric; // For std.numeric.gcd

// Manual implementation for clarity
int gcdEuclidean(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// void main() {
//     int a = 48;
//     int b = 18;
//     writeln("GCD of ", a, " and ", b, " is ", gcdEuclidean(a, b)); // 6
//     // Using std.numeric.gcd
//     // writeln("GCD using std.numeric.gcd: ", gcd(a, b));
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

The `Euclidean Algorithm` is remarkably simple and elegant, whether implemented iteratively or recursively.

---

**Iterative Implementation:**
- The function `gcdEuclidean(a, b)` takes two non-negative integers.
- A `while` loop continues as long as `b` is not zero.
- Inside the loop:
- `a` is updated to the value of `b`.
- `b` is updated to `a mod b` (the remainder of `a` divided by `b`).
- In some languages (like Python), this can be done in a single line: `a, b = b, a % b`.

    </li>
- When the loop terminates (i.e., `b` is 0), `a` holds the `GCD`.

**Recursive Implementation (Conceptual):**
- **Base Case:** If `b` is 0, return `a`.
- **Recursive Step:** Otherwise, return `gcdEuclidean(b, a % b)`.

[Back to Implementation](#implementation)

## Applications

### Application

The `Euclidean Algorithm` is a cornerstone of number theory and has widespread use in computer science:
- **Simplifying Fractions:** To reduce a fraction to its simplest form, you divide both the numerator and the denominator by their `GCD`.
- **Modular Arithmetic and Cryptography:** It is the key component of the **Extended Euclidean Algorithm**, which is used to find modular inverses. This is essential for public-key cryptography systems like RSA.
- **Solving Diophantine Equations:** Finding integer solutions to equations of the form `ax + by = c`.
- **Computer Graphics:** Used in algorithms that involve patterns and repetitions, such as calculating texture coordinates.
- **Music Theory:** The Euclidean algorithm can be used to generate musical rhythms by distributing beats as evenly as possible over a fixed number of time steps.

