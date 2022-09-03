primes =[]
num = 2

def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

while len(primes) != 2000000 :
    if is_prime(num) == True:
        primes.append(num)
        print(num, len(primes)+1)
    num = num + 1
print(sum(primes))
