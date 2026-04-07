lista = []

opcao = -1

while True:
    print("====MENU====")
    print("1 - add")
    print("2 - remove")
    print("3 - valor espe")
    print("4 - buscar")
    print("5 - contar")
    print("6 - ordenar lista")
    print("7 - inververter")
    print("8 - exibir")
    print("0 - sair")
    
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        valor = input("Digite um valor: ")
        lista.append(valor)
    elif opcao == 2:
        if len(lista) > 0:
            removido = lista.pop()
            print("Elemento removido:", removido)


list_especf = input("\nDeseja remover um valor especifico?(s/n): ")
if list_especf == "s":
    remover = input("\nDigite o valor que queria remover: ")
    if remover in lista:
        lista.remove(remover)
        print("Valor removido com sucesso.")
    else:
        print("Valor não encontrado na lista.")
elif list_especf == "n":
    print("Nenhum valor foi removido")
print("\nLista:", lista)


busca = input("\nDigite um valor para buscar posição: ")
if busca in lista:
    posicao = lista.index(busca)  # retorna o índice
    print("O valor está na posição:", posicao)
else:
    print("Valor não encontrado.")
print("\nLista:", lista)

valor_contar = input("\nDigite um valor para contar: ")
quantidade = lista.count(valor_contar)
print("O valor aparece", quantidade, "vez(es).")
    
lista.sort()
print("\nLista ordenada:", lista)

lista.reverse()
print("Lista invertida:", lista)

sair = input("\nPara sair do sistema digite '.' ")

    