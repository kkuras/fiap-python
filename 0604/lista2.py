v = [3, -15, 20, 7, -2]

print("negativos:" )
for num in v:
    if num < 0:
        print(num, end=" ")

positivos_sum = 0
print("\nsoma dos positivos:")
for num in v:
    if num < 0:
        positivos_sum += num
print(positivos_sum)

print("\nimpar")
for impar in v:
    if impar % 2 != 0:
        print(impar, end=" ")

print("\npares e positivos")
for par in v:
    if par % 2 == 0:
        print(par, end=" ")
for num in v:
    if num > 0:
        print(num, end=" ")

valor = int(input("\nDigite o valor existente na lista: "))

if valor in v:
    print(f"o valor {valor} existe na lista")
else:
    print(f"o valor {valor} nao existe na lista")