lista = []

while True:
    valor = input("Digite um valor (ou '.' para sair): ")
    if valor == ".":
        break

    lista.append(valor)

print("Conteudo da lista:", lista)