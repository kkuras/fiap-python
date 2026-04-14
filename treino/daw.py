notas=[]
print("Digite notas entre 0 e 10 --> -1 para sair")
while True:
    valor = float(input("Nota-->"))
    if valor == -1:
        break
    if valor >= 0 and valor <= 10:
       notas.append(valor)
    else:
        print("Valor inválido")
    print("\n Lista de notas válidas-->",notas)

    if len(notas)>0:
        soma = 0
        maior = notas[0]
        menor = notas[0]

        for n in notas:
            soma+=n

            if n>maior:
                maior = n

            if n<menor:
                menor = n

            media = soma/ len(notas)
            print("\n Media: ", media)
            print("\n Menor nota: ", menor)
            print("\n Maior nota: ", maior)
            print("\n Maior nota: ", maior)
            print("\n quantidade de notas: ", len(notas))
    else:
        print("\n nao existe notas validas")


    aprovados = []
    reprovados = []
    for n in notas:
        if n>=6:
            aprovados.append(n)
        else:
            reprovados.append(n)
    print("aprovado: ", aprovados)
    print("reprovado: ", reprovados)
