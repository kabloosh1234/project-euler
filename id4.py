# Largest palindrome product

# Solution 1
palindromes = []
products = []

for i in range(100, 1000):
    for o in range(100, 1000):
        products.append(i * o)

for product in products:
    ispalindrome = False
    product = str(product)
    reversedpro = []
    for c in reversed(product):
        reversedpro.append(c)
    reverse = "".join(reversedpro)
    if reverse == product:
        ispalindrome = True

    if ispalindrome == True:
        palindromes.append(int(product))

palindromes.sort()
print(palindromes[-1])

# Solution 2
num = 0
palindromes=[]
for i in range(100,1000):
    for j in range(100,1000):
        num = i*j
        if str(num) == str(num)[::-1]:
            palindromes.append(num)
print(max(palindromes))
