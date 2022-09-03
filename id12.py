# Highly Divisible Triangular Number
from math import sqrt


def findtri(n):
    triangulars = []
    l = []
    b = []
    for i in range(n + 1):
        for o in range(i + 1):
            l.append(o)
        triangulars.append(sum(l))
        l.clear()
    print(triangulars)


findtri(10)
