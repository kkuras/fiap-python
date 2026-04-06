nota1 = int(input("digite nota 1: "))
nota2 = int(input("digite nota 2: "))
nota3 = int(input("digite nota 3: "))
nota4 = int(input("digite nota 4: "))
media = (nota1 + nota2 + nota3 + nota4)/4

dias_let = int(input("digite os dias letivos: "))
faltas = int(input("digite as faltas: "))
lim_faltas = dias_let * 0.25


if(media >= 6 and faltas <= lim_faltas):
    print(f"vc foi aprovado por causa das suas notas {media}, e suas faltas {lim_faltas}")
elif media < 6 and faltas > lim_faltas:
    print("Você foi reprovado por nota e falta")
elif (media < 6):
    print("Você foi reprovado por nota")
else:
    print("Você foi reprovado por falta")