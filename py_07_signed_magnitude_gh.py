#!/usr/bin/env python3
"""
Chapter 7: Signed Magnitude and Signed Two's Complement
Demonstrates three ways to represent binary numbers: unsigned, signed magnitude, signed two's complement
"""

def unsigned_binary_value(binary_str):
    """Interpret binary as unsigned number"""
    return int(binary_str, 2)

def signed_magnitude_value(binary_str):
    """Interpret binary as signed magnitude (MSB is sign)"""
    sign_bit = binary_str[0]
    magnitude = binary_str[1:]
    value = int(magnitude, 2)
    
    return -value if sign_bit == '1' else value

def signed_twos_complement_value(binary_str):
    """Interpret binary as signed two's complement"""
    if binary_str[0] == '0':
        # Positive number
        return int(binary_str, 2)
    else:
        # Negative number - calculate two's complement
        # Flip bits
        flipped = ''.join('0' if bit == '1' else '1' for bit in binary_str)
        # Add 1
        magnitude = int(flipped, 2) + 1
        return -magnitude

def compare_representations(binary_str):
    """Compare all three representations"""
    unsigned = unsigned_binary_value(binary_str)
    signed_mag = signed_magnitude_value(binary_str)
    signed_twos = signed_twos_complement_value(binary_str)
    
    return {
        'binary': binary_str,
        'unsigned': unsigned,
        'signed_magnitude': signed_mag,
        'signed_twos_complement': signed_twos
    }

def decimal_to_signed_representations(decimal, bits=4):
    """Convert decimal to different signed representations"""
    if decimal >= 0:
        # Positive: same for all
        binary = format(decimal, f'0{bits}b')
        return {
            'signed_magnitude': binary,
            'twos_complement': binary
        }
    else:
        # Negative
        magnitude = abs(decimal)
        mag_binary = format(magnitude, f'0{bits}b')
        
        # Signed magnitude: just flip MSB
        signed_mag = '1' + mag_binary[1:]
        
        # Two's complement: flip all bits and add 1
        flipped = ''.join('0' if bit == '1' else '1' for bit in mag_binary)
        # Add 1
        carry = 1
        result = list(flipped)
        for i in range(len(result) - 1, -1, -1):
            if carry == 0:
                break
            if result[i] == '0':
                result[i] = '1'
                carry = 0
            else:
                result[i] = '0'
        twos = ''.join(result)
        
        return {
            'signed_magnitude': signed_mag,
            'twos_complement': twos
        }

def main():
    print("=" * 60)
    print("CHAPTER 7: Unsigned, Signed Magnitude, and Signed Two's Complement")
    print("=" * 60)
    
    # Example 1: Three interpretations of same binary
    print("\n--- Example 1: Different Interpretations ---")
    test_binaries = ["0101", "1101", "1000"]
    
    print("Binary | Unsigned | Signed Mag | Two's Comp")
    print("-------|----------|------------|------------")
    for binary in test_binaries:
        result = compare_representations(binary)
        print(f"{binary}  |    {result['unsigned']:2d}    |     {result['signed_magnitude']:2d}     |     {result['signed_twos_complement']:2d}")
    
    # Example 2: Represent -5 in different formats
    print("\n--- Example 2: Representing -5 (4-bit) ---")
    representations = decimal_to_signed_representations(-5, 4)
    
    print("Number: -5")
    print(f"Signed Magnitude:    {representations['signed_magnitude']}")
    print(f"  (5 = 0101, flip MSB for negative → 1101)")
    
    print(f"\nTwo's Complement:    {representations['twos_complement']}")
    print("  Steps:")
    print("    5 = 0101")
    print("    One's complement: 1010")
    print("    Add 1:            1011")
    
    # Verify
    print(f"\nVerification:")
    print(f"  Signed magnitude {representations['signed_magnitude']} = {signed_magnitude_value(representations['signed_magnitude'])}")
    print(f"  Two's complement {representations['twos_complement']} = {signed_twos_complement_value(representations['twos_complement'])}")
    
    # Example 3: Represent -23 (8-bit)
    print("\n--- Example 3: Representing -23 (8-bit) ---")
    representations = decimal_to_signed_representations(-23, 8)
    
    print("Number: -23")
    print(f"Positive 23:         {format(23, '08b')}")
    print(f"Signed Magnitude:    {representations['signed_magnitude']}")
    print(f"Two's Complement:    {representations['twos_complement']}")
    
    # Example 4: Understanding MSB
    print("\n--- Example 4: Most Significant Bit (MSB) ---")
    print("\nIn signed representations, MSB indicates sign:")
    print("  MSB = 0 → Positive number")
    print("  MSB = 1 → Negative number")
    print("\nIn unsigned, MSB is just another bit:")
    print("  MSB can be 0 or 1, represents magnitude only")
    
    # Example 5: Range comparison
    print("\n--- Example 5: Range for 4-bit Numbers ---")
    print("\nUnsigned (4-bit):")
    print("  Range: 0 to 15")
    print("  0000 = 0, 1111 = 15")
    
    print("\nSigned Magnitude (4-bit):")
    print("  Range: -7 to +7")
    print("  0111 = +7, 1111 = -7")
    print("  Note: Has +0 (0000) and -0 (1000)")
    
    print("\nTwo's Complement (4-bit):")
    print("  Range: -8 to +7")
    print("  0111 = +7, 1000 = -8")
    print("  Note: Only one zero representation")
    
    # Example 6: Special cases
    print("\n--- Example 6: Special Cases (4-bit) ---")
    special = {
        '0000': 'Zero',
        '0111': 'Maximum positive (7)',
        '1000': 'Minimum (signed mag: -0, twos: -8)',
        '1111': 'Maximum negative (-7 or -1)'
    }
    
    print("Binary | Description           | Signed Mag | Two's Comp")
    print("-------|----------------------|------------|------------")
    for binary, desc in special.items():
        sm = signed_magnitude_value(binary)
        tc = signed_twos_complement_value(binary)
        print(f"{binary}  | {desc:20s} | {sm:10d} | {tc:10d}")
    
    print("\n" + "=" * 60)
    print("Key Concepts:")
    print("- Unsigned: All bits represent magnitude")
    print("- Signed Magnitude: MSB=sign, rest=magnitude")
    print("- Two's Complement: Standard for signed integers")
    print("- MSB=0 → positive, MSB=1 → negative (signed)")
    print("- Two's complement has only one zero")
    print("=" * 60)

if __name__ == "__main__":
    main()
