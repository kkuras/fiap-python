dados = """
ana@gmail.com;Notebook;4500;SP
carlos@gmail.com;Mouse;80;RJ
ana@gmail.com;Teclado;250;SP
maria@gmail.com;Monitor;1200;MG
carlos@gmail.com;Headset;350;RJ
joao@gmail.com;Notebook;4500;PR
maria@gmail.com;Mouse;80;MG
"""

linhas = dados.splitlines()

linha = linhas[0]
dado = linha.split(";")
cliente = dado[0].strip().lower()
produto = dado[1].strip().lower()
preco = float(dado[2].strip())
estado = dado[3].strip().upper()


registro = [cliente, produto, preco, estado]
registros = []

linha = linhas[0]
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
          "produto:", registro[1],
          "preco:", registro[2],
          "estado: ", registro[3])

mostrar_listar()