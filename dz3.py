for fizz in range (1,21):#, int(input("Enter 2.1 number"))
    for buzz in range (1,21):#, int(input("Enter 2.2 number"))
        for a in range(1,21):#, int(input("Enter 2.3 number"))

            for c in range (1, a +1):

                if (c % fizz == 0) and (c % buzz == 0):
                    print("FB")
                elif c % fizz == 0:
                    print ("F")
                elif c % buzz == 0:
                    print ("B")
                else:
                    print(c)
