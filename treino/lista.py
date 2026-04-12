alunos = []

opcao = -1

while True:

    print("===MENU===")
    print("digite 1 para cadastrar um aluno")
    print("digite 2 para ver todos os alunos")
    print("digite 3 para mostrar a media")
    print("digite 4 para mostrar a maior nota")
    print("digite 5 para sair")

    opcao = int(input("\nEscolha a opção: "))

    match opcao:


        case 1:
            nome = input("Digite o nome do aluno: ")
            nota = float(input("Digite a nota do aluno: "))

            alunos.append([nome, nota])

            print("aluno cadastrado")


        case 2:
            if len(alunos) == 0:
                print("Nenhum aluno cadastrado")
            else:
                for aluno in alunos:
                    print("Nome:", aluno[0], "| Nota:", aluno[1])

        case 3:
            soma = 0
            for aluno in alunos:
                soma += aluno[1]

            media = soma / len(alunos)

            print("Media: ", media)

        case 4:
            
            maior = alunos[0]

            for aluno in alunos:
                if aluno[1] > maior[1]:
                    maior = aluno

            print("maior nota: ", maior[0], "-", maior[1])


        case 5:
            print("Saindo..")
            break

