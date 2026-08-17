# ============================================================
# PARTE 1 - LISTA
# ============================================================

# Criamos uma lista representando um aluno.
#
# Cada informação ocupa uma posição (índice).

aluno_lista = [
    "Ana",
    20,
    "Sistemas de Informação"
]


# Os índices começam em 0.
#
# 0 -> nome
# 1 -> idade
# 2 -> curso

print("Nome:", aluno_lista[0])

print("Idade:", aluno_lista[1])

print("Curso:", aluno_lista[2])


# ============================================================
# PARTE 2 - DICIONÁRIO
# ============================================================

# Agora representamos o mesmo aluno utilizando
# um dicionário.
#
# Diferentemente da lista, não precisamos lembrar
# qual é o índice de cada informação.
#
# Utilizamos CHAVE -> VALOR.

aluno = {
    "nome": "Ana",
    "idade": 20,
    "curso": "Sistemas de Informação"
}
# Para acessar uma informação, utilizamos sua chave.
print("\nNome:", aluno["nome"])
print("Idade:", aluno["idade"])
print("Curso:", aluno["curso"])


# ============================================================
# PARTE 3 - ADICIONANDO E ALTERANDO INFORMAÇÕES
# ============================================================

# Podemos adicionar uma nova informação ao dicionário.

aluno["email"] = "ana@email.com"


# Podemos alterar uma informação existente.

aluno["idade"] = 21


print("\nAluno atualizado:")

print(aluno)


print("coco")
print("\nNome:", aluno["nome"])
print("Idade:", aluno["idade"])
print("Curso:", aluno["curso"])

del aluno["email"]

print("\n removi email")
print(aluno)


print("\ncahave")
print(aluno.keys())

print("\nvaor")
print(aluno.values())

print("\niten")
print(aluno.items())

print("\ndado")
for chave, valor in aluno.items():
    print(chave,"i", valor)

# ==================================
print("eisso pai ain ain ain ain")

try:
    chave = input("digite a informação que deseja ").lower()
    print("resultado", aluno[chave])

except KeyError:
    print("erro: essa informação nao existe no cadastro ")


print("\nconsulta")
print(
    aluno.get("telefone")
)

print(aluno.get("telefone", "telefone nao cadastrado"))


produtos = [{
    "nome": "notebook",
    "preco": 4500,
    "quantidade": 10,
    "categoria": "informatica"
},
{
    "nome": "mouse",
    "preco": 80,
    "quantidade": 25,
    "categoria": "periferico"
},
{
    "nome": "teclado",
    "preco": 250,
    "quantidade": 15,
    "categoria": "periferico"
}
]
print("\nproduto")
#produtos = []
for produto in produtos: 
    print("produto:", produto["nome"])
    print("preco:", produto["preco"])
    print("quantidade:", produto["quantidade"])
    print("categoria:", produto["categoria"])

print("\nbusca")
produto_busca = input("digite o nome d oroduto: ").strip().lower()
encontrado = False
for produto in produtos:
    if produto["nome"].lower() == produto_busca:
        print("\nproduto encontrado")
        print("produto:", produto["nome"])
        print("preco:", produto["preco"])
        print("quantidade:", produto["quantidade"])
        print("categoria:", produto["categoria"])
        encontrado = True

if encontrado == False:
    print("\nnao achei o tal do produto")

try:
    nome = input("nome produto:" ).strip()

    if nome == "":
        raise ValueError("o nome nao pode ser vazio")
    preco = float(input("preco: "))

    if preco <= 0:
        raise ValueError("o preco maior que zero")
    quantidade = int(input("quantidade: "))

    if quantidade <= 0:
        raise ValueError("quantidade maior q zero")
    categoria = input("qual categoria: ").strip()

    if categoria == "":
        raise ValueError("categoria nao pode ser vazio")


    novo_produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade,
        "categoria": categoria
    }
    produtos.append(novo_produto)
    print("\n novo produto adicionado com sucesso")

except ValueError as erro:
    print("\nErro:", erro)