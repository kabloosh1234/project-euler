def chain (num):
    y = 1
    while num !=1:
        if num%2 == 1:
            num = 3*num+1
            y+=1

        if num%2 == 0:
            num = num/2
            y+=1
    return y

high = 0
highNum = 0

for i in range(100,1000000):
    p = chain(i)
    if p > high:
        high = p
        highNum = i
    print(i)
print(p)
print(highNum)
