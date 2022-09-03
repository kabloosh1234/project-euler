import math

# Smallest Multiple


a = 0
multiples = []
for o in range(1, round(math.sqrt(math.factorial(20)))):
    for i in range(1, 21):
        b = math.factorial(20) / o
        if b % i == 0:
            a = i
            if a == 20:
                multiples.append(b)
print(multiples)
