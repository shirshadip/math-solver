import math

def combination(n , r):
    if 0 <= r <=n or n<r:
        return math.factorial(n) // (math.factorial(r)* math.factorial(n-r))
    else:
        return None
    
#input 
n = int (input ("enter n:"))
r = int (input ("enter r:"))

def combination_calculator():
    result = combination(n, r)
    if result is not None:
        print (f"{n}C{r} = {result}")

    else:
         print("invalid input: r must be between 0 and n")

# if __name__ == "__main__":
#     combination_calculator()