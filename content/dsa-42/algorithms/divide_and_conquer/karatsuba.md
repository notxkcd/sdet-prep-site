---
title: "Karatsuba Algorithm"
---

The `Karatsuba Algorithm` is an efficient algorithm for multiplying large integers. It was one of the first "fast" multiplication algorithms, discovered by Anatoly Karatsuba in 1960. It uses a `divide and conquer` approach to multiply two `n`-digit numbers in `O(n^log2(3))`, which is approximately `O(n^1.585)`, a significant improvement over the classical grade-school multiplication algorithm which is `O(n^2)`.

The algorithm reduces the number of recursive multiplications from four (in the naive divide and conquer approach) to just three, which is the source of its improved time complexity.

## How it Works

### How it Works (Expanded)

The standard `divide and conquer` approach for multiplying two `n`-digit numbers `x` and `y` would involve splitting them into two halves:
    `x = a <em> 10^(n/2) + b`
    `y = c </em> 10^(n/2) + d`
    The product `x<em>y` would then be:
    `x </em> y = (a*c) * 10^n + (a*d + b*c) * 10^(n/2) + (b*d)`
    This requires four multiplications: `a*c`, `a*d`, `b*c`, and `b*d`.

Karatsuba's key insight was to compute the middle term `(a*d + b*c)` with only one additional multiplication, by calculating `(a+b)*(c+d)` and then subtracting the already computed `a*c` and `b<em>d`.

---

Karatsuba's Method:

1. Let `z0 = b </em> d` (1st multiplication)
2. Let `z2 = a <em> c` (2nd multiplication)
3. Let `z1 = (a+b) </em> (c+d)` (3rd multiplication)
4. The middle term is then `z1 - z2 - z0`.

The final product is:
`x * y = z2 * 10^n + (z1 - z2 - z0) <em> 10^(n/2) + z0`

This requires only three multiplications (`a</em>c`, `b*d`, `(a+b)*(c+d)`), hence the improved performance.

[Jump to Code Walkthrough](#code-walkthrough)

## Implementation {#implementation}

### Python

```python
def karatsuba(x, y):
    """
    Multiplies two large integers using Karatsuba's algorithm.
    Assumes x and y are integers.
    """
    # Base case for recursion
    if x < 10 or y < 10:
        return x </em> y

    # Convert numbers to strings to find length and split
    str_x = str(x)
    str_y = str(y)
    n = max(len(str_x), len(str_y))
    
    # Pad shorter string with zeros to make lengths equal
    str_x = str_x.zfill(n)
    str_y = str_y.zfill(n)

    # Split numbers into halves
    m = n // 2
    high1, low1 = int(str_x[:-m]), int(str_x[-m:])
    high2, low2 = int(str_y[:-m]), int(str_y[-m:])
    
    # Recursive steps
    z0 = karatsuba(low1, low2)
    z2 = karatsuba(high1, high2)
    z1 = karatsuba(low1 + high1, low2 + high2)
    
    # Combine results
    # x<em>y = z2</em>10^n + (z1-z2-z0)<em>10^(n/2) + z0
    # For n being potentially odd, m2 is used for the upper half split
    m2 = n - m
    return (z2 </em> 10*<em>(m2 + m)) + ((z1 - z2 - z0) </em> 10*<em>m) + z0


# Example
# x = 12345678901234567890
# y = 98765432109876543210
# print(karatsuba(x, y))
# print(x </em> y) # Verify with standard multiplication
```

### Javascript

```javascript
function karatsuba(x, y) {
    // Base case for recursion
    if (x < 10 || y < 10) {
        return x <em> y;
    }

    // Convert numbers to strings to find length and split
    const strX = String(x);
    const strY = String(y);
    const n = Math.max(strX.length, strY.length);
    
    // Split numbers into halves
    const m = Math.floor(n / 2);

    const high1 = Math.floor(x / 10<strong>m);
    const low1 = x % (10</strong>m);
    const high2 = Math.floor(y / 10<strong>m);
    const low2 = y % (10</strong>m);
    
    // Recursive steps
    const z0 = karatsuba(low1, low2);
    const z2 = karatsuba(high1, high2);
    const z1 = karatsuba(low1 + high1, low2 + high2);
    
    // Combine results
    // x</em>y = z2<em>10^n + (z1-z2-z0)</em>10^(n/2) + z0
    // BigInt is used here to handle potentially very large numbers
    const powerOf10_2m = BigInt(10)*<em>BigInt(2</em>m);
    const powerOf10_m = BigInt(10)*<em>BigInt(m);

    return BigInt(z2) </em> powerOf10_2m + (BigInt(z1) - BigInt(z2) - BigInt(z0)) <em> powerOf10_m + BigInt(z0);
}

// const x = 12345678901234567890n; // Use BigInt for large numbers
// const y = 98765432109876543210n;
// console.log(String(karatsuba(x, y)));
// console.log(String(x </em> y)); // Verify with standard multiplication
```

### Typescript

```typescript
function karatsubaTS(x: bigint, y: bigint): bigint {
    // Base case for recursion
    if (x < 10n || y < 10n) {
        return x <em> y;
    }

    // Convert numbers to strings to find length and split
    const strX = String(x);
    const strY = String(y);
    const n = Math.max(strX.length, strY.length);
    
    // Split numbers into halves
    const m = Math.floor(n / 2);

    const powerOf10_m = 10n <strong> BigInt(m);
    const high1 = x / powerOf10_m;
    const low1 = x % powerOf10_m;
    const high2 = y / powerOf10_m;
    const low2 = y % powerOf10_m;
    
    // Recursive steps
    const z0 = karatsubaTS(low1, low2);
    const z2 = karatsubaTS(high1, high2);
    const z1 = karatsubaTS(low1 + high1, low2 + high2);
    
    // Combine results
    const powerOf10_2m = 10n </strong> BigInt(2 </em> m);
    return z2 <em> powerOf10_2m + (z1 - z2 - z0) </em> powerOf10_m + z0;
}

// const xTS = 12345678901234567890n; // Use BigInt for large numbers
// const yTS = 98765432109876543210n;
// console.log(karatsubaTS(xTS, yTS).toString());
// console.log((xTS <em> yTS).toString()); // Verify with standard multiplication
```

### Cpp

```cpp
#include <string>
#include <iostream>
#include <algorithm> // For std::max
#include <cmath> // For pow

// Note: C++ doesn't have built-in support for arbitrarily large integers.
// This implementation uses <code>long long</code> and will overflow for very large numbers.
// A real-world implementation would require a custom BigInt library.

long long karatsuba(long long x, long long y) {
    // Base case for recursion
    if (x < 10 || y < 10) {
        return x </em> y;
    }

    // Convert numbers to strings to find length
    std::string str_x = std::to_string(x);
    std::string str_y = std::to_string(y);
    int n = std::max(str_x.length(), str_y.length());
    
    // Split numbers into halves
    int m = n / 2;
    long long p = std::pow(10, m);

    long long high1 = x / p;
    long long low1 = x % p;
    long long high2 = y / p;
    long long low2 = y % p;
    
    // Recursive steps
    long long z0 = karatsuba(low1, low2);
    long long z2 = karatsuba(high1, high2);
    long long z1 = karatsuba(low1 + high1, low2 + high2);
    
    // Combine results
    long long p2 = std::pow(10, 2 <em> m);
    return (z2 </em> p2) + ((z1 - z2 - z0) <em> p) + z0;
}

// int main() {
//     long long x = 12345;
//     long long y = 6789;
//     std::cout << karatsuba(x, y) << std::endl; // 83810205
//     std::cout << x </em> y << std::endl; // Verify
//     return 0;
// }
```

### Go

```go
package main

import (
    "fmt"
    "math/big"
    "strconv"
    "math"
)

// This implementation uses Go's big.Int to handle arbitrarily large integers.
func karatsuba(x, y <em>big.Int) </em>big.Int {
    // Base case
    if x.Cmp(big.NewInt(10)) < 0 || y.Cmp(big.NewInt(10)) < 0 {
        res := new(big.Int)
        return res.Mul(x, y)
    }

    // Find length n and m
    n := float64(maxLen(x.String(), y.String()))
    m := math.Floor(n / 2)
    mBig := big.NewInt(int64(m))

    // Power of 10
    powerOf10_m := new(big.Int).Exp(big.NewInt(10), mBig, nil)
    powerOf10_2m := new(big.Int).Exp(big.NewInt(10), new(big.Int).Mul(big.NewInt(2), mBig), nil)
    
    // Split numbers
    high1 := new(big.Int).Div(x, powerOf10_m)
    low1 := new(big.Int).Mod(x, powerOf10_m)
    high2 := new(big.Int).Div(y, powerOf10_m)
    low2 := new(big.Int).Mod(y, powerOf10_m)

    // Recursive steps
    z0 := karatsuba(low1, low2)
    z2 := karatsuba(high1, high2)
    z1 := karatsuba(new(big.Int).Add(low1, high1), new(big.Int).Add(low2, high2))
    
    // Combine results: z2 <em> 10^(2</em>m) + (z1 - z2 - z0) <em> 10^m + z0
    term1 := new(big.Int).Mul(z2, powerOf10_2m)
    term2 := new(big.Int).Sub(z1, z2)
    term2.Sub(term2, z0)
    term2.Mul(term2, powerOf10_m)
    
    result := new(big.Int).Add(term1, term2)
    result.Add(result, z0)
    
    return result
}

func maxLen(s1, s2 string) int {
    if len(s1) > len(s2) {
        return len(s1)
    }
    return len(s2)
}

// func main() {
//     xStr := "12345678901234567890"
//     yStr := "98765432109876543210"

//     x := new(big.Int)
//     x.SetString(xStr, 10)
    
//     y := new(big.Int)
//     y.SetString(yStr, 10)

//     fmt.Println(karatsuba(x, y))
//     fmt.Println(new(big.Int).Mul(x, y)) // Verify
// }
```

### D

```d
import std.stdio;
import std.bigint; // Requires a library, e.g., std.bigint for proper handling

// This implementation uses D's built-in <code>BigInt</code> from <code>std.bigint</code>.
// If not using a standard library BigInt, <code>long</code> will overflow quickly.

BigInt karatsuba(BigInt x, BigInt y) {
    // Base case
    if (x < 10 || y < 10) {
        return x </em> y;
    }

    // Get length n and m
    string strX = x.toString();
    string strY = y.toString();
    size_t n = max(strX.length, strY.length);
    size_t m = n / 2;

    // Power of 10
    BigInt powerOf10_m = BigInt(10) ^^ m;

    // Split numbers
    BigInt high1 = x / powerOf10_m;
    BigInt low1 = x % powerOf10_m;
    BigInt high2 = y / powerOf10_m;
    BigInt low2 = y % powerOf10_m;

    // Recursive steps
    BigInt z0 = karatsuba(low1, low2);
    BigInt z2 = karatsuba(high1, high2);
    BigInt z1 = karatsuba(low1 + high1, low2 + high2);

    // Combine results
    BigInt powerOf10_2m = BigInt(10) ^^ (2 <em> m);
    return (z2 </em> powerOf10_2m) + ((z1 - z2 - z0) <em> powerOf10_m) + z0;
}

// void main() {
//     BigInt x = BigInt("12345678901234567890");
//     BigInt y = BigInt("98765432109876543210");
//     writeln(karatsuba(x, y));
//     writeln(x </em> y); // Verify
// }
```

## Code Walkthrough {#code-walkthrough}

[Back to Implementation](#implementation)

### Code Walkthrough

The `Karatsuba Algorithm` is a recursive function that multiplies large numbers by splitting them into smaller halves and combining the results using only three recursive multiplications.

---

**`karatsuba(x, y)` Function:**
- **Base Case:** If `x` or `y` is a single-digit number (or small enough), it returns their product using standard multiplication. This is a crucial step to terminate the recursion.
- **Find `n` and `m`:** The length `n` of the larger number is determined. The split point `m` is chosen, typically as `n/2`.
- **Split Numbers:** The numbers `x` and `y` are split into high and low parts based on the split point `m`. For a number `x` and a base of 10, this is:
- `high = x / 10^m`
- `low = x % 10^m`

        (This part requires careful handling of large numbers, often using `BigInt` libraries or string manipulation in languages without native large integer support.)
    </li>
- **Recursive Calls:** Three recursive calls are made to compute the required products:
- `z0 = karatsuba(low1, low2)` (product of the low parts)
- `z2 = karatsuba(high1, high2)` (product of the high parts)
- `z1 = karatsuba(low1 + high1, low2 + high2)` (product of the sums of parts)

    </li>
- **Combine Results:** The final product is assembled using Karatsuba's formula:
        `result = (z2 * 10^(2*m)) + ((z1 - z2 - z0) * 10^m) + z0`</li>
- This involves shifting the terms `z2` and `(z1 - z2 - z0)` by the appropriate powers of 10 (or base 2) and summing them up.

[Back to Implementation](#implementation)

## Applications

### Application

The `Karatsuba Algorithm` has significant applications in areas requiring high-precision arithmetic:
- **Cryptography:** Many cryptographic systems, such as RSA, rely on arithmetic with very large numbers (e.g., 2048-bit or 4096-bit numbers). Karatsuba's algorithm is a fundamental building block for the multiplication operations in these systems.
- **Computer Algebra Systems:** Software like Mathematica, Maple, and SymPy use Karatsuba's algorithm (and other fast multiplication algorithms) for polynomial multiplication and other high-precision calculations.
- **Scientific Computing:** In fields requiring very high precision, such as number theory research, astronomy, and physics simulations, where standard floating-point numbers are not sufficient.
- **Large Number Libraries:** `BigInt` libraries in various programming languages often use Karatsuba's algorithm as part of their multiplication implementation, switching to it from standard multiplication when the numbers exceed a certain size.

