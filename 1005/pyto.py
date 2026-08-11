dados = "Ana;Notebook;4500"

print(type(dados))

campos = dados.split(";")
print(campos)
print(type(campos))

nome = "        Ana        "

nome.strip() #retirar espaços em branco

nome.strip().lower()
print(nome)
print(nome.strip())
print(nome.strip().lower())

dados = """
ana@gmail.com.br;notebook;4500
carlos@gmail.com.br;mouse;80
ana@gmail.com.br;teclado;250
maria@gmail.com.br;monitor;300
carlos@gmail.com.br;headset;350
joao@gmail.com.br;notebook;5000
 """


dados = dados.strip()
linhas = dados.splitlines()
print(linhas)
print(len(linhas))

linha = linhas[0]
print(linha)

campos = linha.split(";")
print(campos)

email = campos[0].strip().lower()
produto = campos[1].strip().lower()
preco = float(campos[2].strip())
print(type(preco))
print(type(campos[2]))

registro = [email, produto, preco]
print(registro)

registros = []
for linha in linhas: 
    campos = linha.split(";")
    email = campos[0].lower()
    produto = campos[1].strip().lower()
    preco = float(campos[2].strip())
    registro = [email, produto, preco]
    registros.append(registro)

for registro in registros:
    
    print(registros)

    
for registro in registros:
   print("cliente:", registro[0],
          "produto:", registro[1],
          "preco:", registro[2]) 

print("================================")

precos = []
for registro in registros:
    precos.append(registro[2])
    len(precos) #quantidade de precos
    sum(precos) #somatoria
    max(precos) #maior preco
    max(precos) #menor preco
    media = sum(precos) / len(precos)
    print(media)
    precos_ordenados = sorted(precos)
    print(precos_ordenados)

    #busca de produtos
    print("busca")
    produto_busca = input("digite o produto: ").strip().lower()
    for registro in registros:
        if registro[1] == produto_busca:
            print("cliente:", registro[1],
                      "valor:", registro[2])