import numpy as np
choose = input ("which type of matrix you want-->"
                "\n 1.1D MATRIX"
                "\n 2.2D MATRIX"
                
                "\n===========>>")
if choose == "1":
    def matrix():
        print ("_"*5,"Matrix calculator","_"*30)
        ind_range=int (input("enter how many numbers you want in the first matrix----->"))
        first_matrix=[]
        for i in range (ind_range):
            element=int(input(f"enter the element of the matrix no.{i+1}----->"))
            first_matrix.append(element)
        index_range2=int(input("enter how many numbers you want in the second matrix----->"))
        second_matrix=[]
        for j in range (index_range2):
            element2 = int(input(f"enter the element of the matrix no.{j+ 1}----->"))
            second_matrix.append(element2)
        first=np.array(first_matrix)
        second=np.array(second_matrix)

        options = input("enter the option you want-->"
                        "\n 1.Addition"
                        "\n 2.Subtraction"
                        "\n 3.Multiplication[element wise]"
                        "\n 4.Matrix multiplication"
                        "\n 5.Transpose"
                        "\n 6. Determinant"
                        "\n 7. Rank"
                        "\n 8.Eigenvalues & Eigenvectors"
                        "input the option you want \n"
                        "----->")
        try:
            if options == "1":
                print("_"*5,"Addition","_"*30)
                addition=first+second
                print (f"The addition of {first }and {second} Matrix is ={addition}")
        except ValueError:
            print ("pleease input the matrices correctly")
        try:
            if options == "2":
                print("_"*5,"subtraction","_"*30)
                addition=first-second
                print (f"The subtraction of {first }and {second} Matrix is ={addition}")
        except ValueError:
            print ("pleease input the matrices correctly")


    # matrix()