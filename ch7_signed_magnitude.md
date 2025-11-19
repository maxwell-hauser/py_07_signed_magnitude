# Chapter 7: Unsigned, Signed Magnitude and Signed Two's Complement Binary Numbers

_Originally created 12 February 2021, by Maxwell Hauser — Updated 6 October 2025._

_Builds upon material from Chapter 6: Complements._

---

## Overview
A binary number can be represented in three different ways. As an:

1. unsigned number
2. signed magnitude number
3. signed two’s complement

## Definitions

**1. Unsigned number:**

In an unsigned number, every bit is used to represent the number.

**2. Signed magnitude number:**

In a signed magnitude number, the most significant bit of the number represents the sign. A $0$ in the most significant position represents a positive sign, and $1$ in the most significant position represents a negative sign.

**3. Signed two's complement:**

A signed two's complement applies to a negative number. If the sign of the number is $1$, then the number is represented by signed two's complement.

**Example — Unsigned:**
- $(0101)_2$ = +5
- $(1101)_2$ = +13
- $(1000)_2$ = +8

**Example — Signed Magnitude:**
- $(0101)_2$ = +5
- $(1101)_2$ = -5
- $(1000)_2$ = -0

**Example — Signed Two's Complement:**
- $(0101)_2$ = +5
- $(1101)_2$ = -3
- $(1000)_2$ = -8

---

## Examples
**Example 7.1:** Represent $(-5)_{10}$ with a 4-bit signed magnitude and signed two's complement.

1. To find the signed magnitude of a negative number, first find the unsigned binary representation of the positive version of the number.

2. Then add a sign bit to the front. For example, 5 in unsigned binary is 0101.

3. By adding the sign bit, the result becomes 1101, which represents -5 in signed magnitude.
---
1. To find the signed two’s complement of a negative number, first find the unsigned binary representation of the positive version of the number.

2. Then find the two’s complement of that number. For example, 5 in unsigned binary is 0101.

3. The two’s complement of 0101 is 1011, which represents -5 in signed two’s complement.
---
**Example 7.2:** Represent $(-23)_{10}$ with an 8-bit signed two's complement.

1. First, find the unsigned binary representation of the positive version of the number. $23 = (10111)_2$

2. Then extend it to 8 bits: $(00010111)_2$

3. Next, find the two's complement of that number. $(00010111)_2$ becomes $(11101001)_2$

4. Finally, the result $(11101001)_2$ represents $-23$ in signed two's complement.
