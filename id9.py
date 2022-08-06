from math import sqrt
a = 1
b = 1
c = 1

firm = False

for i in range(2):
    while firm == False :
        while firm == False :
            while firm == False :
                if sqrt(a) + sqrt(b) + sqrt(c) == 1000 :
                    firm = True
                    print(sqrt(a) + sqrt(b) + sqrt(c))

            c +=1
        b += 1
    a +=1
