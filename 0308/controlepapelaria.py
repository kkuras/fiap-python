produtos = []
estoque = []

def buscar_indice(nome):
    if nome in produtos:
        return produtos.index(nome)
    return -1

def listar_produtos():
    print("\n--- Lista de Produtos ---")
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return
 
    for i in range(len(produtos)):
        print(f"{i + 1} - {produtos[i]:.<20}{estoque[i]} unidades")


def cadastrar_produtos():
    n = int(input("Quantos produtos serão cadastrados? "))
 
    for i in range(n):
        nome = input(f"Produto {i + 1}: ")
        qtd = int(input("Quantidade: "))
        produtos.append(nome)
        estoque.append(qtd)


def consultar_produto():
    nome_busca = input("\nDigite o nome do produto que deseja consultar: ")
    indice = buscar_indice(nome_busca)
 
    if indice != -1:
        print("Produto encontrado!")
        print(f"Quantidade: {estoque[indice]}")
    else:
        print("Produto não encontrado.")


def estoque_baixo():
    print("\nProdutos com estoque baixo")
    baixo = []
 
    for i in range(len(produtos)):
        if estoque[i] < 10:
            baixo.append(produtos[i])
 
    if len(baixo) == 0:
        print("Todos os produtos possuem estoque adequado.")
    else:
        for nome in baixo:
            print(nome)
 
 
def maior_estoque():
    if len(estoque) == 0:
        print("\nNenhum produto cadastrado.")
        return

    maior_qtd = estoque[0]
    indice_maior = 0
 
    for i in range(len(estoque)):
        if estoque[i] > maior_qtd:
            maior_qtd = estoque[i]
            indice_maior = i
 
    print("\nProduto com maior estoque")
    print(produtos[indice_maior])
    print(f"Quantidade: {estoque[indice_maior]}")


def atualizar_estoque():
    nome_busca = input("\nQual produto deseja atualizar? ")
    indice = buscar_indice(nome_busca)
 
    if indice != -1:
        nova_qtd = int(input("Digite a nova quantidade: "))
        estoque[indice] = nova_qtd
        print("Estoque atualizado com sucesso!")
        listar_produtos()
    else:
        print("Produto não encontrado.")
 
 
def main():
    cadastrar_produtos()
    listar_produtos()
    consultar_produto()
    estoque_baixo()
    maior_estoque()
    atualizar_estoque()

main()