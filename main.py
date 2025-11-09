import subprocess
import sys



# Install required libraries (if any)
libraries = ["numpy", "sympy","pandas"]
for lib in libraries:
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
    except subprocess.CalledProcessError:
        print(f"Could not install {lib}, skipping...")

# Ask user for calculator type
option = input(
    "Choose which calculator you want to use --->\n"
    "1. Basic maths calculator\n"
    "2. Advanced maths calculator for solving mathematical problems\n"
    "[like sets, complex numbers, permutations and combinations, etc.]\n"
)

# Basic calculator
if option.lower() == "basic" or option == "1":
    import basic as b
    try:
        b.bas_calc()
    except ValueError:
        print("Invalid choice in basic calculator.")

# Advanced calculator
elif option.lower() == "advanced" or option == "2":
    import complex as c
    try:
        c.calculator()
    except (ValueError, NameError, KeyError, TypeError):
        print("Sorry, there was an error during advanced calculation.")
    except (FloatingPointError, ZeroDivisionError, RuntimeError):
        print("Sorry! Some mathematical confusion occurred in the code.")
    finally:
        print("Calculation done.")

else:
    print("Invalid option. Please choose 1 or 2.")

