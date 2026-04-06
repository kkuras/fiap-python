dias_let = int(input("informe os dias letivos: "))
faltas = int(input("informe a quantidade de faltas: "))
limite_faltas = dias_let * 25/100

if(faltas > limite_faltas):
    print("reprovado")
else:
    print("aprovado")