def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

def factors(x):
    yes = []
    for i in range(1, x + 1):
        if x % i == 0:
            yes.append(i)
    return yes
