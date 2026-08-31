import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    resposta = requests.get(
        url,
        timeout=10
    )

    resposta.raise_for_status()

    usuarios = resposta.json()

    print("\n======================")
    print(" usuario api")
    print("\n======================")

    for usuario in usuarios:
        print("ID:", usuario["id"],
              "| nome:", usuario["name"],
              "| email:", usuario["email"])

        
    nome_busca = input("\ndigite parte do nome que deseja buscar: ").strip().lower()

    encontrado = False

    for usuario in usuarios:
        nome = usuario["name"].strip().lower()

        if nome_busca in nome:
            encontrado= True
            print("\nusuario acho")
            print("id:", usuario["id"])
            print("nome:", usuario["name"])
            print("email:", usuario["email"])
            print("telefone:", usuario["phone"])
            print("cidade:", usuario["address"]["city"])

    if encontrado == False:
        print("\nnenhum usuario acho")

except requests.exceptions.ConnectionError:
    print("\n erro de conecao", "tenta dnv pai")

except requests.exceptions.Timeout:
    print("\n tempo dms", "tenta dnv pai")


except requests.exceptions.HTTPError as erro:
    print("\n erro no http", erro)

except KeyError as erro:
    print("\ncampo nao acho", erro)

except ValueError:
    print("\nnao interpreto")