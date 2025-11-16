
def vector_calc():
    choose = int (input ("enter what do you want to do:\n"
                         "1.dot product:\n"
                         "2.cross product:\n"))

    if choose == 1 :
        print ("the input for the first vector ")
        i_cap1 = int (input ("what is the i cap ?:"))
        j_cap1 = int (input ("what is the j cap ?:"))
        k_cap1 = int (input ("what is the k cap ?:"))
        print ("the input for the second vector ")
        i_cap2 =int (input ("what is the i cap ?:"))
        j_cap2 =int (input ("what is the j cap ?:"))
        k_cap2 =int (input ("what is the k cap ?:"))

        print (f"the dot product of  a vector and b vector is :A.B===>{i_cap1*i_cap2+j_cap1*j_cap2+k_cap1*k_cap2}"
               )
    if choose == 2 :
        print("the input for the first vector ")
        i_cap1 = int(input("what is the i cap ?:"))
        j_cap1 = int(input("what is the j cap ?:"))
        k_cap1 = int(input("what is the k cap ?:"))
        print("the input for the second vector ")
        i_cap2 = int(input("what is the i cap ?:"))
        j_cap2 = int(input("what is the j cap ?:"))
        k_cap2 = int(input("what is the k cap ?:"))

        print (f"the cross product of the two vectors are :AXB===>{j_cap1*k_cap2 - k_cap1*j_cap2}i + {k_cap1*i_cap2-i_cap1*k_cap2}j+{i_cap1*j_cap2-j_cap1*i_cap2}k")
# vector_calc()
