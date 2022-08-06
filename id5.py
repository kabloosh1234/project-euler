# Smallest multiple

# Solution 1
from collections import Counter
from primePy import primes


def find_primes(n):
    prime_factors = Counter()
    for i in primes.upto(n):
        while n % i == 0:
            n /= i
            prime_factors[i] += 1
    return prime_factors


factors = Counter()
for i in range(2, 21):
    _factors = find_primes(i)
    print(i, _factors)
    for p in _factors:
        factors[p] = max(_factors[p], factors[p])

print(factors)
ans = 1
for p in factors:
    ans *= p ** factors[p]

print(ans)


# Solution 2
j = 0
num = 200000000
for i in range(10000000000):
    if num%3 == 0 and num%4 == 0 and num%5 == 0 and num%6 == 0 and num%7 == 0 and num%8 == 0 and num%9 == 0 and num%10 == 0 and num%11 == 0 and num%12 == 0 and num%13 == 0 and num%14 == 0 and num%15 == 0 and num%16 == 0 and num%17 == 0 and num%18 == 0 and num%19 == 0 and num%20 == 0 :
        j = 1
    if j  == 1:
            break
    num +=1
