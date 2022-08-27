from goofyAh import factors
facts = []
cont = 100
temp = 0
while len(facts) != 500:
    for i in range(1, cont+1):
        temp += i

    if len(factors(temp)) == 500:
        facts.append(facts)
        break
    print(temp)
    cont += 1
print("the number:", temp)
