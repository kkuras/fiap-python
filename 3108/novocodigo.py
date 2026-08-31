import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    resposta = requests.get(
        url,
        timeout=10
    )

    resposta.raise_for_status()


    usuarios = resposta.json()

    html = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>usario api</title>
</head>
<body>
<h1>usuario cadastrado</h1>
<p> dados </p>
<hr>
    
</body>
</html>
"""

    for usuario in usuarios:
        nome = usuario["name"]
        email = usuario["email"]
        cidade = usuario["address"]["city"]