import math
def bas_calc():
    print("Choose what you want to do:"
          "\n 1. Addition"
          "\n 2. Subtraction"
          "\n 3. Multiplication"
          "\n 4. Division"
          "\n 5.percentage")

    choose = int(input("---> "))

    if choose == 1:
        def addition():
            a = int(input("Enter first number: "))
            while True:
                b = input("Enter next number (or type 'end' to finish): ")
                if b.lower() == "end":
                    break
                else:
                    a += int(b)
            return a

        result = addition()
        print("The total sum is:", result)



    elif choose == 2:
        def subtraction():
            a = int(input("Enter first number: "))
            while True:
                b = input("Enter next number (or type 'end' to finish): ")
                if b.lower() == "end":
                    break
                else:
                    a -= int(b)
            return a

        result = subtraction()
        print("The answer of subtraction is:", result)
    elif choose == 3:
        def multiplication():
            a = int(input("Enter first number: "))
            while True:
                b = input("Enter next number (or type 'end' to finish): ")
                if b.lower() == "end":
                    break
                else:
                    a *= int(b)
            return a

        result = multiplication()
        print("The multiplication is:", result)

    elif choose == 4:
        def division():
            a = int(input("Enter first number: "))
            while True:
                try:
                    b = input("Enter next number (or type 'end' to finish): ")

                    if b.lower() == "end":
                        break
                    else:
                        a /= int(b)
                except ZeroDivisionError:
                    print ("A number cannot be divided by zero")
            return a

        result = division()
        print("The division is:", result)
    elif choose == 5:
        def percentage():
            a = int(input("Enter obtained value: "))
            b = int (input ("enter the Total value:"))
            percentage = (a/b)*100
            return percentage
        result = percentage()
        print("The percentage is:", result,"%")


# bas_calc()
