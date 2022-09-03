import math

# Smallest Multiple
base = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 2 * 3 * 2 * 2 * 3 * 2 * 2 * 2 * 3 * 3 * 2

# upper bound

a = 0
multiples = []
print(base)
for o in range(1, 100000):
    for i in range(1, 21):
        b = base / o
        if b % i == 0:
            a = i
            if a == 20:
                multiples.append(b)


print(a)
multiples.sort
print(multiples[-1])
for i in range(1, 21):
    if 1007760 % i == True:
        print(f"{i} Factor")
    else:
        print(f"{i} Not Factor")
