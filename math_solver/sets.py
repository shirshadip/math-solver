def set_calculator():
    a = set(input("Enter the first set (comma-separated): ").split(","))
    b = set(input("Enter the second set (comma-separated): ").split(","))
    operation = input("Enter the operation (union, intersection, difference, symmetric_difference): ").strip().lower()
    if operation == "union":
        result = a.union(b)
        print (f"The union of the sets is: {result}")
    elif operation == "intersection":
        result = a.intersection(b)
        print (f"The intersection of the sets is: {result}")
    elif operation == "difference":
        result = a.difference(b)
        print (f"The difference of the sets is: {result}")
    elif operation == "symmetric_difference":
        result = a.symmetric_difference(b)
        print (f"The symmetric difference of the sets is: {result}")
    else:
        print("Invalid operation. Please enter one of the following: union, intersection, difference, symmetric_difference.")
    return result
# set_calculator()