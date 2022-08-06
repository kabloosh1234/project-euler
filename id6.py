import math
a = 0
b = 0

for i in range (1, 101):
    a = a + pow(i, 2)

for i in range (1, 101):
    b = b + i
print(b)
b = pow(b, 2)

print(a)
print(b)
print(b-a)
