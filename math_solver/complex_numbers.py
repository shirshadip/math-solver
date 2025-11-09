import re
import math
import cmath

# Parse complex number like "3+4i" or "-2-3i"
def parse_complex(s):
    s = s.replace(" ", "").replace("−", "-")  # Handle minus signs
    match = re.match(r'^([+-]?\d*\.?\d+)([+-]\d*\.?\d*)i$', s)
    if not match:
        raise ValueError("❌ Invalid format. Use 'a + bi' or 'a - bi'")
    a = float(match.group(1))
    b = float(match.group(2))
    return a, b

# Operations
def modulus(a, b): return (a**2 + b**2)**0.5
def conjugate(a, b): return f"{a} {'-' if b >= 0 else '+'} {abs(b)}i"
def addition(a1, b1, a2, b2): return f"{a1 + a2} + {b1 + b2}i"
def subtraction(a1, b1, a2, b2): return f"{a1 - a2} + {b1 - b2}i"
def multiplication(a1, b1, a2, b2): return f"{a1*a2 - b1*b2} + {a1*b2 + a2*b1}i"
def division(a1, b1, a2, b2):
    denom = a2**2 + b2**2
    if denom == 0: return "⚠️ Division by zero error"
    real = (a1*a2 + b1*b2)/denom
    imag = (b1*a2 - a1*b2)/denom
    return f"{real:.3f} + {imag:.3f}i"
def phase(a, b): return math.atan2(b, a)
def polar_form(a, b): return f"{modulus(a, b):.3f} (cos({phase(a, b):.3f}) + i sin({phase(a, b):.3f}))"
def exponential_form(a, b): return f"{modulus(a, b):.3f} * e^(i * {phase(a, b):.3f})"
def square_root(a, b):
    z = complex(a, b)
    root = cmath.sqrt(z)
    return f"{root.real:.3f} + {root.imag:.3f}i"

# Main Calculator
def complex_calculator():
    try:
        z1 = input("Enter the first complex number (e.g. 3+4i or -2-3i): ")
        a1, b1 = parse_complex(z1)
    except ValueError as e:
        print(e)
        return

    # Optional second number
    z2_input = input("Enter the second complex number (or press Enter to skip): ").strip()
    has_second = False
    if z2_input:
        try:
            a2, b2 = parse_complex(z2_input)
            has_second = True
        except ValueError:
            print("⚠️ Invalid second complex number format. Skipping binary operations.")

    print("\n📘 binary Operations on First Complex Number:")
    print(f"Modulus of {z1} = {modulus(a1, b1):.3f}")
    print(f"Conjugate of {z1} = {conjugate(a1, b1)}")
    print(f"Polar form of {z1} = {polar_form(a1, b1)}")
    print(f"Exponential form of {z1} = {exponential_form(a1, b1)}")
    print(f"Square root of {z1} = {square_root(a1, b1)}")

    if has_second:
        print("\n📘 Binary Operations Between Two Complex Numbers:")
        print(f"Addition: {addition(a1, b1, a2, b2)}")
        print(f"Subtraction: {subtraction(a1, b1, a2, b2)}")
        print(f"Multiplication: {multiplication(a1, b1, a2, b2)}")
        print(f"Division: {division(a1, b1, a2, b2)}")
        print(f"Square root of {z2_input} = {square_root(a2, b2)}")

# Run the program
complex_calculator()
