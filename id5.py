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
