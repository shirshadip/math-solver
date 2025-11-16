def sec():
    choose = input ("choose what do you want to evaluate -->"
                    "\n1.last term [t(n)]:"
                    "\n2.sum of the series [s(n)]:"
                    "\n3.evaluate the first term [a]:")
    if choose == "1"or choose =="last terms" or choose == "t(n)" :
        def tn():
            a = int(input ("enter the first term[a]-> "))
            n = int (input ("enter the number of terms[n]-> "))
            d= int (input ("enter the common difference of the series[d]-> "))
            return a+(n-1)*d
        print("the last term is ---->",tn())
    elif choose == "2" or choose == "sum of the series" or choose == "s(n)":
        def sn ():
            n = int(input("enter the number of terms[n]-> "))
            a = int(input("enter the first term[a]-> "))
            give = input("is tn is given?[y/n]-> ")
            if give == "y":
                tn = int (input("enter the last number of series[t(n)]-> "))
                return n/2*(a+tn)
            elif give == "n":
                a = int(input("enter the first term[a]-> "))
                n = int(input("enter the number of terms[n]-> "))
                d = int(input("enter the common difference of the series[d]-> "))
                tn = a+(n-1)*d
                return n/2*(a+tn)

            else:
                print ("please enter y or n")
        print(sn())
    if choose== "3" or choose == "a" or choose=="first term":
        def a ():
            what = input("where do you want to evaluate -->"
                         "\n1.from tn->"
                         "\n2.from sn->")
            if what=="1" or what=="tn":
                tn = int (input("what is tn ->"))
                n = int (input("what is n ->"))
                d = int (input("what is d ->"))
                return tn -(n-1)*d
            elif what=="2" or what=="sn":
                tn = int (input("what is tn ->"))
                n = int (input("what is n ->"))
                sn = int (input("what is sn ->"))
                return (sn/2*n)-tn
            else :
                print ("enter corerct values ")
        print (a())

# sec()