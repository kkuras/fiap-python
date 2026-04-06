num1 = int(input("digite numero1: "))
num2 = int(input("digite numero2: "))
num3 = int(input("digite numero3: "))

maior = num1
if(num2 > maior):
    maior = num2
if num3 > maior:
    maior = num3
print(maior)