alunos   = []

opcao = -1

while True:
    print("====MENU====")
    print("1 - cadastrar o aluno")
    print("2 - exibir todos os alunos")
    print("3 - remover pelo nome")
    print("4 - Buscar aluno pelo nome (mostrar nota)")
    print("5 - Exibir média das notas")
    print("6 - Exibir aluno com maior nota")
    print("7 - Ordenar alunos por nome")
    print("8 - Ordenar alunos por nota")
    print("9 - sair")
    
    opcao = int(input("Escolha uma opção: "))

    match opcao: 

        case 1:
            nome = input("Nome: ")
            nota = float(input("Nota: "))
 
            aluno = {"nome": nome, "nota": nota}
            alunos.append(aluno)
 
            print("Aluno cadastrado com sucesso!")

        case 2:
            if len(alunos) == 0:
                print("Nenhum aluno cadastrado.")
            else:
                for a in alunos:
                    print("Nome:", a["nome"], "| Nota:", a["nota"])

        # 3 - Remover
        case 3:
            nome = input("Nome do aluno a remover: ")
            encontrado = False
 
            for a in alunos:
                if a["nome"] == nome:
                    alunos.remove(a)
                    encontrado = True
                    print("Aluno removido.")
                    break
 
            if not encontrado:
                print("Aluno não encontrado.")
 
      # 4 - Buscar
        case 4:
            nome = input("Nome do aluno: ")
            encontrado = False
 
            for a in alunos:
                if a["nome"] == nome:
                    print("Nota:", a["nota"])
                    encontrado = True
                    break
 
            if not encontrado:
                print("Aluno não encontrado.")
 
              # 5 - Média
        case 5:
            if len(alunos) == 0:
                print("Sem dados.")
            else:
                soma = 0
                for a in alunos:
                    soma += a["nota"]
 
                media = soma / len(alunos)
                print("Média:", media)
 
         # 6 - Maior nota
        case 6:
            if len(alunos) == 0:
                print("Nenhum aluno.")
            else:
                maior = alunos[0]
 
                for a in alunos:
                    if a["nota"] > maior["nota"]:
                        maior = a
 
                print("Maior nota:", maior["nome"], "-", maior["nota"])

        # 7 - Ordenar por nome
        case 7:
            alunos.sort(key=lambda x: x["nome"])
            print("Ordenado por nome.")

         # 8 - Ordenar por nota
        case 8:
            alunos.sort(key=lambda x: x["nota"])
            print("Ordenado por nota.")

              # 0 - Sair
        case 0:
            print("Encerrando sistema...")

                    # Caso padrão
        case _:
            print("Opção inválida.")