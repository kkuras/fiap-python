# Criação da lista vazia
lista = []
 
# Entrada de dados
while True:
    valor = input("Digite um valor (ou '.' para sair): ")
   
    if valor == ".":
        break
   
    lista.append(valor)  # adiciona o valor na lista
 
# a) Exibir lista original
print("\nLista original:", lista)
 
# b) Remover o último elemento (se a lista não estiver vazia)
if len(lista) > 0:
    removido = lista.pop()  # remove o último elemento
    print("Elemento removido (pop):", removido)
else:
    print("Lista vazia, nada para remover com pop.")
 
print("Lista atual:", lista)
 
# c) Remover um valor informado pelo usuário
valor_remover = input("\nDigite um valor para remover: ")
 
if valor_remover in lista:
    lista.remove(valor_remover)  # remove a primeira ocorrência
    print("Valor removido com sucesso.")
else:
    print("Valor não encontrado na lista.")
 
print("Lista atual:", lista)
 
# d) Buscar índice de um valor
valor_busca = input("\nDigite um valor para buscar posição: ")
 
if valor_busca in lista:
    posicao = lista.index(valor_busca)  # retorna o índice
    print("O valor está na posição:", posicao)
else:
    print("Valor não encontrado.")

# e) Contar ocorrências
valor_contar = input("\nDigite um valor para contar: ")
quantidade = lista.count(valor_contar)
 
print("O valor aparece", quantidade, "vez(es).")
 
# f) Ordenar a lista
lista.sort()  # ordena em ordem crescente
print("\nLista ordenada:", lista)
 
# g) Inverter a lista
lista.reverse()  # inverte a ordem
print("Lista invertida:", lista)