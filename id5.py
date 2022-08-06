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
    if num%3 == 0:
        if num%4 == 0 :
            if num%5 ==0:
                if num%6 ==0:
                    if num%7==0:
                        if num%8==0:
                            if num%9==0:
                                if num%10==0:
                                    if num%11==0:
                                        if num%12==0:
                                            if num%13==0:
                                                if num%14==0:
                                                    if num%15==0:
                                                        if num%16==0:
                                                            if num%17==0:
                                                                if num%18==0:
                                                                    if num%19==0:
                                                                        if num%20==0:
                                                                            print(num)
                                                                            j = 1
    if j  == 1:
        break
    num +=1
