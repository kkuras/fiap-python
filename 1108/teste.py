dados = """
ana@gmail.com;Notebook;4500;SP
carlos@gmail.com;Mouse;80;RJ
ana@gmail.com;Teclado;250;SP
maria@gmail.com;Monitor;1200;MG
carlos@gmail.com;Headset;350;RJ
joao@gmail.com;Notebook;4500;PR
maria@gmail.com;Mouse;80;MG
"""
 
pedidos = []
 
 
# ============================================================
# PARTE 1 - PROCESSAMENTO DOS DADOS
# ============================================================
 
def processar_dados():
    texto = dados.strip()
    linhas = texto.splitlines()
 
    for linha in linhas:
        campos = linha.split(";")
 
        email = campos[0].strip().lower()
        produto = campos[1].strip().lower()
        valor = float(campos[2].strip())
        estado = campos[3].strip().upper()
 
        pedido = [email, produto, valor, estado]
        pedidos.append(pedido)
 
 
# ============================================================
# PARTE 2 - EXIBIÇÃO DOS PEDIDOS
# ============================================================
 
def exibir_pedidos():
    print("\n================================")
    print("           PEDIDOS")
    print("================================")
 
    if len(pedidos) == 0:
        print("Nenhum pedido cadastrado.")
        return
 
    for pedido in pedidos:
        print("Cliente:", pedido[0],
              "| Produto:", pedido[1],
              "| Valor: R$", pedido[2],
              "| Estado:", pedido[3])
 
 
# ============================================================
# PARTE 3 - ANÁLISE FINANCEIRA
# ============================================================
 
def analise_financeira():
    print("\n================================")
    print("       ANALISE FINANCEIRA")
    print("================================")
 
    if len(pedidos) == 0:
        print("Nenhum pedido cadastrado.")
        return
 
    valores = []
    for pedido in pedidos:
        valores.append(pedido[2])
 
    quantidade = len(valores)
    faturamento = sum(valores)
    ticket_medio = faturamento / quantidade
    maior_venda = max(valores)
    menor_venda = min(valores)
 
    print("Quantidade de pedidos:", quantidade)
    print("Faturamento total: R$", faturamento)
    print("Ticket medio: R$", round(ticket_medio, 2))
    print("Maior venda: R$", maior_venda)
    print("Menor venda: R$", menor_venda)
 
 
# ============================================================
# PARTE 4 - BUSCA
# ============================================================
 
def buscar_cliente():
    print("\n================================")
    print("        BUSCA POR CLIENTE")
    print("================================")
 
    email_busca = input("Digite o e-mail do cliente: ").strip().lower()
 
    encontrado = False
    for pedido in pedidos:
        if pedido[0] == email_busca:
            encontrado = True
            print("Produto:", pedido[1],
                  "| Valor: R$", pedido[2],
                  "| Estado:", pedido[3])
 
    if not encontrado:
        print("Cliente nao encontrado.")
 
 
def buscar_produto():
    print("\n================================")
    print("        BUSCA POR PRODUTO")
    print("================================")
 
    produto_busca = input("Digite o produto: ").strip().lower()
 
    encontrado = False
    for pedido in pedidos:
        if pedido[1] == produto_busca:
            encontrado = True
            print("Cliente:", pedido[0],
                  "| Valor: R$", pedido[2],
                  "| Estado:", pedido[3])
 
    if not encontrado:
        print("Produto nao encontrado.")
 
 
def buscar_estado():
    print("\n================================")
    print("        BUSCA POR ESTADO")
    print("================================")
 
    estado_busca = input("Digite o estado: ").strip().upper()
 
    encontrado = False
    for pedido in pedidos:
        if pedido[3] == estado_busca:
            encontrado = True
            print("Cliente:", pedido[0],
                  "| Produto:", pedido[1],
                  "| Valor: R$", pedido[2])
 
    if not encontrado:
        print("Nenhum pedido encontrado para esse estado.")
 
 
# ============================================================
# PARTE 5 - ANALISES ADICIONAIS (COM TRATAMENTO DE EMPATE)
# ============================================================
 
def produto_mais_pedido():
    print("\n================================")
    print("     PRODUTO(S) MAIS PEDIDOS")
    print("================================")
 
    produtos = []
    for pedido in pedidos:
        produtos.append(pedido[1])
 
    maior_quantidade = 0
    for produto in produtos:
        quantidade = produtos.count(produto)
        if quantidade > maior_quantidade:
            maior_quantidade = quantidade
 
    print("Quantidade de pedidos:", maior_quantidade)
 
    exibidos = []
    for produto in produtos:
        if produtos.count(produto) == maior_quantidade and produto not in exibidos:
            print(produto)
            exibidos.append(produto)
 
 
def cliente_mais_pedidos():
    print("\n================================")
    print("     CLIENTE(S) COM MAIS PEDIDOS")
    print("================================")
 
    emails = []
    for pedido in pedidos:
        emails.append(pedido[0])
 
    maior_quantidade = 0
    for email in emails:
        quantidade = emails.count(email)
        if quantidade > maior_quantidade:
            maior_quantidade = quantidade
 
    print("Quantidade de pedidos:", maior_quantidade)
 
    exibidos = []
    for email in emails:
        if emails.count(email) == maior_quantidade and email not in exibidos:
            print(email)
            exibidos.append(email)
 
 
def estado_mais_pedidos():
    print("\n================================")
    print("     ESTADO(S) COM MAIS PEDIDOS")
    print("================================")
 
    estados = []
    for pedido in pedidos:
        estados.append(pedido[3])
 
    maior_quantidade = 0
    for estado in estados:
        quantidade = estados.count(estado)
        if quantidade > maior_quantidade:
            maior_quantidade = quantidade
 
    print("Quantidade de pedidos:", maior_quantidade)
 
    exibidos = []
    for estado in estados:
        if estados.count(estado) == maior_quantidade and estado not in exibidos:
            print(estado)
            exibidos.append(estado)
 
 
def analises_adicionais():
    produto_mais_pedido()
    cliente_mais_pedidos()
    estado_mais_pedidos()
 
 
# ============================================================
# PARTE 6 - ORDENAÇÃO
# ============================================================
 
def ordenar_valores():
    print("\n================================")
    print("   VALORES EM ORDEM CRESCENTE")
    print("================================")
 
    valores = []
    for pedido in pedidos:
        valores.append(pedido[2])
 
    valores_ordenados = sorted(valores)
    print(valores_ordenados)
 
 
# ============================================================
# DESAFIO 2 - CADASTRO SEGURO DE PEDIDOS
# ============================================================
 
def cadastrar_pedido():
    print("\n================================")
    print("        CADASTRAR PEDIDO")
    print("================================")
 
    # --- E-MAIL ---
    while True:
        email = input("E-mail: ").strip().lower()
        if email == "":
            print("Erro: o e-mail nao pode ser vazio. Tente novamente.")
            continue
        break
 
    # --- PRODUTO ---
    while True:
        produto = input("Produto: ").strip().lower()
        if produto == "":
            print("Erro: o produto nao pode ser vazio. Tente novamente.")
            continue
        break
 
    # --- VALOR ---
    while True:
        valor_texto = input("Valor: ").strip()
 
        try:
            valor = float(valor_texto)
        except ValueError:
            print("Erro: o valor deve ser numerico. Tente novamente.")
            continue
 
        if valor <= 0:
            print("Erro: o valor deve ser maior que zero. Tente novamente.")
            continue
 
        break
 
    # --- ESTADO ---
    while True:
        estado = input("Estado (sigla com 2 letras, ex: SP): ").strip().upper()
 
        if estado == "":
            print("Erro: o estado nao pode ser vazio. Tente novamente.")
            continue
 
        if len(estado) != 2 or not estado.isalpha():
            print("Erro: o estado deve ser uma sigla valida com 2 letras. Tente novamente.")
            continue
 
        break
 
    pedido = [email, produto, valor, estado]
    pedidos.append(pedido)
 
    print("\nPedido cadastrado com sucesso!")
    print("Cliente:", pedido[0],
          "| Produto:", pedido[1],
          "| Valor: R$", pedido[2],
          "| Estado:", pedido[3])
 
 
# ============================================================
# DESAFIO EXTRA - MENU
# ============================================================
 
def menu():
    while True:
        print("\n================================")
        print("       ANALISADOR DE PEDIDOS")
        print("================================")
        print("1 - Listar pedidos")
        print("2 - Cadastrar pedido")
        print("3 - Buscar por cliente")
        print("4 - Buscar por produto")
        print("5 - Buscar por estado")
        print("6 - Exibir analise financeira")
        print("7 - Sair")
 
        opcao = input("Escolha uma opcao: ").strip()
 
        match opcao:
            case "1":
                exibir_pedidos()
            case "2":
                cadastrar_pedido()
            case "3":
                buscar_cliente()
            case "4":
                buscar_produto()
            case "5":
                buscar_estado()
            case "6":
                analise_financeira()
            case "7":
                print("\nEncerrando o programa. Ate logo!")
                break
            case _:
                print("\nOpcao invalida. Tente novamente.")
 
 
# ============================================================
# EXECUÇÃO PRINCIPAL
# ============================================================
 
processar_dados()
exibir_pedidos()
analise_financeira()
analises_adicionais()
ordenar_valores()
menu()