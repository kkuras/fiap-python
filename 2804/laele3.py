frase = ""

while True:
    print("\n=== MENU ===")
    print("1 - Digitar frase")
    print("2 - Exibir quantidade de palavras")
    print("3 - Substituir uma palavra")
    print("4 - Verificar se uma palavra existe")
    print("5 - Exibir frase invertida")
    print("6 - Sair")

    opcao = input("\nEscolha uma opção: ")

    match opcao:
        case "1":
            frase = input("Digite a frase: ")

        case "2":
            if frase == "":
                print("Nenhuma frase digitada ainda.")
            else:
                palavras = frase.split()
                print(f"Quantidade de palavras: {len(palavras)}")

        case "3":
            if frase == "":
                print("Nenhuma frase digitada ainda.")
            else:
                antiga = input("Palavra a substituir: ")
                nova = input("Nova palavra: ")
                frase = frase.replace(antiga, nova)
                print(f"Frase atualizada: {frase}")

        case "4":
            if frase == "":
                print("Nenhuma frase digitada ainda.")
            else:
                busca = input("Digite a palavra: ")
                if busca.lower() in frase.lower():
                    print(f"A palavra '{busca}' foi encontrada na frase.")
                else:
                    print(f"A palavra '{busca}' não foi encontrada.")

        case "5":
            if frase == "":
                print("Nenhuma frase digitada ainda.")
            else:
                print(f"Frase invertida: {frase[::-1]}")

        case "6":
            print("Encerrando o programa.")
            break

        case _:
            print("Opção inválida. Tente novamente.")