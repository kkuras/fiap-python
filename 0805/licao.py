dados = """
ana@gmail.com;Notebook;4500;SP
carlos@gmail.com;Mouse;80;RJ
ana@gmail.com;Teclado;250;SP
maria@gmail.com;Monitor;1200;MG
carlos@gmail.com;Headset;350;RJ
joao@gmail.com;Notebook;4500;PR
maria@gmail.com;Mouse;80;MG
"""

linhas = dados.split()
registros = []

def mostrar_listar():
    for linha in linhas:
        dado = linha.split(";")
        cliente = dado[0].strip().lower()
        produto = dado[1].strip().lower()
        preco = float(dado[2].strip())
        estado = dado[3].strip().upper()
        registro = [cliente, produto, preco, estado]
        registros.append(registro)

    for registro in registros:
         print("cliente:", registro[0],
                "| produto:", registro[1],
                "| valor:", registro[2], 
                "| estado:", registro[3])
         
precos = []
def calcular_estatistica():
    
    for registro in registros:
        precos.append(registro[2])

    quantidade = len(precos)
    faturamento = sum(precos)
    ticket_medio = faturamento / quantidade
    maior_venda = max(precos)
    menor_venda = min(precos)

    print("quantidade de pedidos:", quantidade)
    print("faturamento total: R$", faturamento)
    print("ticket medio: R$", round(ticket_medio, 2))
    print("maior venda: R$", maior_venda)
    print("menor venda: R$", menor_venda)

def buscar():
    print("================================")
    print("buscar por: 1-cliente | 2-produto | 3-estado")
    opcao = input("digite a opcao: ").strip()

    match opcao:
        case "1":
            indice = 0
            termo = input("digite o email do cliente: ").strip().lower()
        case "2":
            indice = 1
            termo = input("digite o produto: ").strip().lower()
        case "3":
            indice = 3
            termo = input("digite o estado: ").strip().upper()
        case _:
            print("opcao invalida")
            return

    encontrados = []
    for registro in registros:
        if registro[indice] == termo:
            encontrados.append(registro)

    if len(encontrados) == 0:
        print("nenhum pedido encontrado")
    else:
        for registro in encontrados:
            print("cliente:", registro[0], "| produto:", registro[1], "| valor:", registro[2], "| estado:", registro[3])

def contar_ocorrencias(indice):
    # conta quantas vezes cada valor aparece naquela posicao do registro
    contagem = {}
    for registro in registros:
        chave = registro[indice]
        if chave in contagem:
            contagem[chave] = contagem[chave] + 1
        else:
            contagem[chave] = 1
    return contagem

def analisar():
    print("================================")

    contagem_produtos = contar_ocorrencias(1)  # indice 1 = produto
    produto_mais_vendido = max(contagem_produtos, key=contagem_produtos.get)
    print("produto que mais aparece:", produto_mais_vendido, "(" + str(contagem_produtos[produto_mais_vendido]) + " vezes)")

    contagem_clientes = contar_ocorrencias(0)  # indice 0 = cliente
    cliente_top = max(contagem_clientes, key=contagem_clientes.get)
    print("cliente com mais pedidos:", cliente_top, "(" + str(contagem_clientes[cliente_top]) + " pedidos)")

    contagem_estados = contar_ocorrencias(3)  # indice 3 = estado
    estado_top = max(contagem_estados, key=contagem_estados.get)
    print("estado com mais pedidos:", estado_top, "(" + str(contagem_estados[estado_top]) + " pedidos)")


def ordenar_por_valor():
    print("================================")
    print("pedidos em ordem crescente de valor:")

    registros_ordenados = sorted(registros, key=lambda registro: registro[2])

    for registro in registros_ordenados:
        print("cliente:", registro[0], "| produto:", registro[1], "| valor:", registro[2], "| estado:", registro[3])

mostrar_listar()
calcular_estatistica()
buscar()
analisar()
ordenar_por_valor()