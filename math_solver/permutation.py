import math
def permutation(n, r):
    return math.factorial(n) / math.factorial(n - r)

    if n<0 or r<0:
        return "n and r must be non-negative integers." \
               "Please provide valid inputs."
    
    if r > n:
        return "r cannot be greater than n. Please provide valid inputs."
    
def permutation_calculator():
    try:
        n = int(input("Enter the value of n (total items): "))
        r = int(input("Enter the value of r (items to choose): "))
        result = permutation(n, r)
        print(f"The number of permutations of {n} items taken {r} at a time is: {result}")
    except ValueError:
        print("Invalid input. Please enter non-negative integers for n and r.")
if __name__ == "__main__":
    permutation_calculator()
