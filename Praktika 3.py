#№1
#sum = 0
#a = [1, 2, 3, 4, 5]
#for i in a:
#    sum += i
#print(sum)

#a = [1, 2, 3, 4, 5]
#i = res = 0
#while i <= len(a):
#    res += i
#    i +=1
#print(res)


#№2
#f = open("Primer 2.1.py", 'r')
#for line in f:
#    print (line, end="")
#f.close()

#№3
#f = open("Primer 2.1.py", 'r')
#a = []
#for line in (f):
    #    a.append(line)
   #     a.reverse()
 #       print (a, end="")

#№4
#nominals = [5, 10, 20, 50, 100, 200, 500, 1000]
#suma = int(input())
#kilbanknot = 0
#if suma < nominals[7]:
 #      print ("Введіть більшу суму")
#for i in range(1,suma // 1000 + 1):
 #     if suma // nominals[7] >= 1:
  #             kilbanknot += 1
#print ("Кількість банкнот -", kilbanknot)

#№5

nominals = [5, 10, 20, 50, 100, 200, 500, 1000]
suma = int(input())

if suma > (nominals[0] * 10 + nominals[1] * 10 + nominals[2] * 10 + nominals[3] * 10) or suma % 5 != 0:
       print ("Сума завелика, введіть меншу суму, чи сума не кратна п'яти")


kilbanknot = 1
while True:
    kilbanknot += 1
    if not kilbanknot: continue
    kilbanknot50 = 0
    for i in range(1, suma // 50 + 1):
        if 1 <= suma // nominals[3] <= 10 and suma % 50 == 0:
            kilbanknot50 += 1
    if kilbanknot > 10: break
print("Кількість банкнот 50 грн -", kilbanknot50)

kilbanknot = 1
while True:
    kilbanknot += 1
    if not kilbanknot: continue
    kilbanknot20 = 0
    for i in range(1, suma // 20 + 1):
        if 1 <= suma // nominals[2] <= 10 and suma % 20 == 0:
            kilbanknot20 += 1
    if kilbanknot > 10: break
print("Кількість банкнот 20 грн -", kilbanknot20)

kilbanknot = 1
while True:
    kilbanknot += 1
    if not kilbanknot: continue
    kilbanknot10 = 0
    for i in range(1, suma // 10 + 1):
        if 1 <= suma // nominals[1] <= 10 and suma % 10 == 0:
            kilbanknot10 += 1
    if kilbanknot > 10: break
print("Кількість банкнот 10 грн -", kilbanknot10)

kilbanknot = 1
while True:
    kilbanknot += 1
    if not kilbanknot: continue
    kilbanknot5 = 0
    for i in range(1, suma // 5 + 1):
        if 1 <= suma // nominals[0] <= 10 and suma % 5 == 0:
            kilbanknot5 += 1
    if kilbanknot > 10: break
print("Кількість банкнот 5 грн -", kilbanknot5)

