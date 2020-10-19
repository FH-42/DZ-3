f = open('dz3.py')
first_line = f.readlines()
#print (first_line[0])

first_line[0] = list(range(1,21))
#print(first_line[0])
b = list(first_line[0])
print(b)
fizz = b[3] #int(input("Enter first number"))
buzz = b[6]#int(input("Enter second number"))
a = b[19]#int(input("Enter the third one"))

for c in range (1, a +1):

    if (c % fizz == 0) and (c % buzz == 0):
        print("FB")
    elif c % fizz == 0:
        print ("F")
    elif c % buzz == 0:
        print ("B")
    else:
        print(c)


#for first_line in f:
#    print(first_line)
#f.close()
