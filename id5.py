# Smallest multiple
from __future__ import print_function


smallest = []
b2 = []
b3 = []
b5 = []
b7 = []
b11 = []
b13 = []
b17 = []
b19 = []
a = 0

for i in range(145495350):
    if i % 2 == 0:
        b2.append(i)
    elif i % 3 == 0:
        b3.append(i)
    elif i % 5 == 0:
        b5.append(i)
    elif i % 7 == 0:
        b7.append(i)
    elif i % 11 == 0:
        b11.append(i)
    elif i % 13 == 0:
        b13.append(i)
    elif i % 17 == 0:
        b17.append(i)
    elif i % 19 == 0:
        b19.append(i)
    if i in b2 and b3 and b5 and b7 and b11 and b13 and b17 and b19:
        smallest.append(i)
        break
print(smallest)
print(b2, b3, b5, b7, b11, b13, b17, b19)
