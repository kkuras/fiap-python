v = [12, -7, 25, -30, 8]

soma = sum(v)

print("soma", soma)

print("\npositivos:" )
for num in v:
    if num > 0:
        print(num, end=" ")

negativos_sum = 0
print("\nsoma dos negativos:")
for num in v:
    if num < 0:
        negativos_sum += num
print("soma negativos: ",negativos_sum)

print("\npar")
for par in v:
    if par % 2 == 0:
        print(par, end=" ")

print("\npositivos e impares:" )
for num in v:
    if num > 0:
        print(num, end=" ")
for num in v:
    if num % 2 != 0:
        print(num, end=" ")

valor = int(input("\nDigite o valor existente na lista: "))

if valor in v:
    print(f"o valor {valor} existe na lista")
else:
    print(f"o valor {valor} nao existe na lista")
        
