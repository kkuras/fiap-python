maior = 0
for num in range(5):
    numero = int(input(f"digite {num+1} numero: "))
    if numero > maior:
        maior = numero

print(maior)