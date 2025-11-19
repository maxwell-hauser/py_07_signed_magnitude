# Chapter 7: Signed Numbers (Signed Magnitude and Two's Complement)

## Overview

This chapter explores different methods of representing signed (positive and negative) numbers in binary systems. We'll compare unsigned, signed magnitude, and two's complement representations to understand their advantages and disadvantages.

## Key Concepts

### Three Methods of Binary Number Representation

#### 1. Unsigned Binary
- **Only positive numbers** (and zero)
- All bits represent magnitude
- **No sign bit**
- Range: 0 to 2^n - 1

#### 2. Signed Magnitude
- **MSB is sign bit:** 0 = positive, 1 = negative
- **Remaining bits represent magnitude**
- Simple and intuitive
- Has **two zeros** (+0 and -0)

#### 3. Two's Complement
- **MSB is sign bit:** 0 = positive, 1 = negative
- **Negative numbers:** Two's complement of positive value
- **One zero** only
- **Industry standard**

## Unsigned Binary Representation

### Characteristics
- **Sign:** No sign; all values are positive
- **Range (n bits):** 0 to 2^n - 1
- **Usage:** Counts, addresses, quantities that can't be negative

### Examples (8-bit)
```
Binary      Decimal
00000000  →    0
00000001  →    1
01111111  →  127
10000000  →  128  (not -128!)
11111111  →  255  (largest value)
```

### 8-bit Unsigned Range: 0 to 255

```
Min: 00000000₂ = 0₁₀
Max: 11111111₂ = 255₁₀
```

## Signed Magnitude Representation

### Characteristics
- **MSB:** Sign bit (0=positive, 1=negative)
- **Remaining bits:** Magnitude (absolute value)
- **Intuitive:** Similar to how humans write numbers
- **Problem:** Two representations of zero

### Format (n bits)
```
[Sign bit][Magnitude bits]
    1 bit    (n-1) bits
```

### Examples (8-bit)
```
Binary      Sign  Magnitude  Value
00000000  →  +      0      →   +0
10000000  →  -      0      →   -0  (problem!)
00000101  →  +      5      →   +5
10000101  →  -      5      →   -5
01111111  →  +    127      → +127
11111111  →  -    127      → -127
```

### 8-bit Signed Magnitude Range: -127 to +127

```
Most positive:  01111111₂ = +127₁₀
Most negative:  11111111₂ = -127₁₀
Positive zero:  00000000₂ = +0₁₀
Negative zero:  10000000₂ = -0₁₀ (wasteful!)
```

### Converting Signed Magnitude

**Binary to Decimal:**
1. Check MSB for sign
2. Convert remaining bits to decimal
3. Apply sign

```
11010110₂ (signed magnitude):
  MSB = 1 (negative)
  1010110₂ = 86₁₀
  Result: -86₁₀
```

**Decimal to Binary:**
1. Convert absolute value to binary
2. Set MSB to 0 (positive) or 1 (negative)

```
-42₁₀ (8-bit signed magnitude):
  |−42| = 42₁₀ = 0101010₂
  Set MSB = 1: 10101010₂
```

### Arithmetic with Signed Magnitude

**Problem:** Addition/subtraction is complex!

```
(+5) + (-3):
  Can't just add: 00000101 + 10000011 = 10001000 = -8? ✗
  Must: Compare magnitudes, subtract smaller from larger, determine sign
```

**Why It's Complicated:**
- Must compare magnitudes before operating
- Different logic for addition vs subtraction
- Must handle sign separately
- Hardware is complex

## Two's Complement Representation (Review)

### Characteristics
- **MSB:** Sign bit (0=positive, 1=negative)
- **Negative numbers:** Two's complement form
- **One zero** representation
- **Simple arithmetic:** Addition works normally

### Format (n bits)
All bits contribute to value (positional notation with MSB negative)

### Examples (8-bit)
```
Binary      Value    Explanation
00000000  →   0      Only one zero!
00000101  →  +5      Positive (MSB=0)
11111011  → -5       Two's complement of 00000101
01111111  → +127     Most positive
10000000  → -128     Most negative
11111111  → -1       Two's complement of 00000001
```

### 8-bit Two's Complement Range: -128 to +127

```
Most positive:  01111111₂ = +127₁₀
Most negative:  10000000₂ = -128₁₀  (asymmetric!)
Zero:           00000000₂ = 0₁₀     (only one)
Minus one:      11111111₂ = -1₁₀
```

### Why Two's Complement Wins

**Advantages:**
1. **Single zero:** No wasted bit pattern
2. **Simple addition:** A + B works directly (no special sign logic)
3. **Simple subtraction:** A - B = A + two's_comp(B)
4. **Efficient hardware:** One adder for both addition and subtraction
5. **Consistent:** All operations follow same rules

## Comparison of All Three Methods

### Same Binary, Different Interpretations

```
Binary: 10000101

Unsigned:          133
Signed Magnitude:  -5
Two's Complement: -123
```

### Range Comparison (8 bits)

| Method | Range | Number of Zeros | Sign Bit |
|--------|-------|-----------------|----------|
| **Unsigned** | 0 to 255 | 1 | None |
| **Signed Magnitude** | -127 to +127 | 2 (±0) | Yes (MSB) |
| **Two's Complement** | -128 to +127 | 1 | Yes (MSB) |

### Visual Comparison

```
Decimal    Unsigned    Signed Mag    Two's Comp
+127       01111111    01111111      01111111
+5         00000101    00000101      00000101
+1         00000001    00000001      00000001
+0         00000000    00000000      00000000
-0         --------    10000000      --------
-1         --------    10000001      11111111
-5         --------    10000101      11111011
-127       --------    11111111      10000001
-128       --------    --------      10000000
128        10000000    --------      --------
255        11111111    --------      --------
```

## Learning Objectives

By the end of this chapter, you should be able to:
- Distinguish between unsigned, signed magnitude, and two's complement
- Convert numbers in each representation
- Understand the range of each representation
- Explain the advantages of two's complement
- Identify which representation is being used from context
- Recognize the sign bit in signed representations
- Explain why two's complement is the industry standard

## Python Example

Run the interactive example:

```bash
python ch07_signed_numbers.py
```

### What the Example Demonstrates

1. **Unsigned Interpretation:** Reading binary as unsigned values
2. **Signed Magnitude:** Understanding sign bit and magnitude
3. **Two's Complement:** Modern standard representation
4. **Same Binary, Different Values:** How interpretation affects meaning
5. **Range Comparisons:** Valid ranges for each method
6. **Conversion Examples:** Converting between representations
7. **Practical Applications:** When to use each method

### Sample Output

```
============================================================
CHAPTER 7: Signed Number Representations
============================================================

--- Example 1: Same Binary, Three Interpretations ---
Binary: 10000101

Unsigned interpretation:           133
Signed Magnitude interpretation:   -5
Two's Complement interpretation:  -123

--- Example 2: Range Comparison (8-bit) ---
Unsigned:         0 to 255 (256 values)
Signed Magnitude: -127 to +127 (255 values, 2 zeros)
Two's Complement: -128 to +127 (256 values, 1 zero)
...
```

## Real-World Applications

### Unsigned Numbers
- **Memory Addresses:** Always positive
- **Array Indices:** Non-negative positions
- **Counters:** Loop iterations, event counts
- **File Sizes:** Cannot be negative
- **RGB Color Values:** 0-255 per channel
- **Ports/IDs:** Network ports, process IDs

### Two's Complement (Standard for Signed)
- **Integer Variables:** int, short, long in C/C++/Java
- **Signed Data Types:** int8_t, int16_t, int32_t, int64_t
- **ALU Operations:** CPU arithmetic
- **Temperature Sensors:** Negative and positive values
- **Financial Calculations:** Debits and credits
- **Coordinate Systems:** Positive and negative positions

### Signed Magnitude (Rare)
- **Floating-Point Sign:** IEEE 754 uses sign bit + magnitude for exponent
- **Some DSPs:** Certain digital signal processors
- **Educational:** Teaching signed number concepts
- **Legacy Systems:** Some older computers

## Common Questions

**Q: Why doesn't signed magnitude use all 256 patterns in 8 bits?**  
A: Because +0 (00000000) and -0 (10000000) are different bit patterns for the same value, wasting one pattern.

**Q: Why is two's complement range asymmetric?**  
A: The bit pattern 10000000 represents -128, which has no positive equivalent in 8 bits. This gives us one extra negative number.

**Q: How do computers know which interpretation to use?**  
A: The compiler/programmer specifies the data type. The hardware doesn't care—it's the same binary. For example, `unsigned char` vs `signed char`.

**Q: Can I convert between these representations?**  
A: Yes, but you must be careful about range. A value valid in unsigned (e.g., 200) may not be representable in signed 8-bit (-128 to 127).

**Q: Why learn signed magnitude if it's not used?**  
A: Understanding it helps you appreciate why two's complement is superior. Also, sign-magnitude concepts appear in floating-point representation.

## Interpretation Depends on Context

The **same bit pattern** means different things depending on the data type:

```c
uint8_t u = 0xFF;    // u = 255 (unsigned)
int8_t  s = 0xFF;    // s = -1  (two's complement)

// Same bits (11111111), different interpretation!
```

### C/C++ Data Types

| Type | Representation | 8-bit Range |
|------|----------------|-------------|
| `unsigned char` | Unsigned | 0 to 255 |
| `signed char` | Two's Complement | -128 to 127 |
| `char` | Implementation-defined | Usually signed |

## Key Takeaways

- Same binary can represent different values depending on interpretation
- ➕ Unsigned: All positive, 0 to 2^n - 1
- Signed Magnitude: Intuitive but has two zeros
- 🏆 Two's Complement: Industry standard, efficient arithmetic
- MSB = sign bit in signed representations
- Two's complement has asymmetric range (one more negative)
- Data type determines interpretation, not the bits themselves
- Two's complement enables simple hardware for arithmetic

## Practice Exercises

1. Interpret 10110010 as unsigned, signed magnitude, and two's complement
2. What is -50₁₀ in 8-bit signed magnitude?
3. What is -50₁₀ in 8-bit two's complement?
4. Find the ranges for 16-bit unsigned, signed magnitude, and two's complement
5. Why can't -128 be represented in 8-bit signed magnitude?
6. Convert 11111111 to decimal in all three representations
7. Explain why two's complement addition is simpler than signed magnitude addition
8. What happens if you interpret an unsigned 200 as a signed two's complement value?

## Further Study

- Learn binary arithmetic with two's complement (Chapter 8)
- Study overflow detection in signed arithmetic
- Explore sign extension when increasing bit width
- Investigate floating-point representation (Chapter 9)
- Learn about saturating vs wrapping arithmetic

---

**Course Navigation:**  
← Previous: [Chapter 6 - Complements](../ch6_complements/) | Next: [Chapter 8 - Binary Arithmetic](../ch8_binary_addition_subtraction/) →
