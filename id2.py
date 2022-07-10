# Even Fibonacci numbers

a, b = 0, 1
maximum = 4_000_000

even_terms = []
while a + b <= maximum:
    fib = a + b
    if fib % 2 == 0:
        even_terms.append(fib)
    a, b = b, fib

print(sum(even_terms))
