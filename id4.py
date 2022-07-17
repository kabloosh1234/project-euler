# Largest palindrome product
palindromes = []
products = []


for i in range(100, 1000):
    for o in range(100, 1000):
        products.append(i * o)

for product in products:
    # a = products.pop()
    # for c in reversed(a):
    #     for u in charl:
    #         intpal.append(int(u))
    #     s = [str(int) for int in intpal]
    #     num = int("".join(s))
    #     palindromes.append(num)
    #     charl.clear()
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
