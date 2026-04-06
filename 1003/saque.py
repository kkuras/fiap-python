saque = int (input("Ola, por favor insira o valor que voce deseja sacar: "))
 
n100 = saque // 100 #sera armazenado a quantidade de notas de 100
saque = saque % 100 #resto da divisao, para descobriro quanto falta

n50 = saque // 50 #valor inteiro do quociente da divisao
saque = saque % 50 #valor inteiro do resto da divisao

n20 = saque // 20
saque = saque % 20

n10 = saque // 10
saque = saque % 10

n5 = saque // 5
saque = saque % 5

print("\qnQuantidade de notas:")
if n100 > 0:
    print("Notas de 100:", n100)
if n50 > 0:
    print("Notas de 50:", n50)
if n20 > 0:
    print("Notas de 20:", n20)
if n10 > 0:
    print("Notas de 10:", n10)
