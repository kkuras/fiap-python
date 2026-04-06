v = [45, -89, 32, -12, 33]

total = sum(v)


print("vetor: ",v)
print("soma: ",total)

print("negativos:" )
for num in v:
    if num < 0:
        print(num, end=" ")

print("\nimpar")
for impar in v:
    if impar % 2 != 0:
        print(impar, end=" ")

print("\npar")
for par in v:
    if par % 2 == 0:
        print(par, end=" ")

valor = int(input("\nDigite o valor existente na lista:"))

if valor in v:
    print(f"o valor {valor} existe na lista")
else:
    print(f"o valor {valor} nao existe na lista")