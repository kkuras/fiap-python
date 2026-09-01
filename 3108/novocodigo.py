from pathlib import Path
import webbrowser
import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    resposta = requests.get(url, timeout=10)
    resposta.raise_for_status()

    usuarios = resposta.json()

    # 3. Pede a cidade ao usuário
    cidade_desejada = input("Digite a cidade para filtrar: ").strip().lower()

    # Filtra a lista comparando em minúsculas (evita erro de maiúscula/minúscula)
    usuarios_filtrados = [
        u for u in usuarios
        if u["address"]["city"].lower() == cidade_desejada
    ]

    total = len(usuarios_filtrados)

    html = f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>usuario api</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 20px;
        }}
        .card {{
            background-color: #fff;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 16px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            max-width: 400px;
        }}
        .card h2 {{
            margin-top: 0;
        }}
    </style>
</head>
<body>
<h1>Usuários cadastrados</h1>
<p>Cidade filtrada: {cidade_desejada.title()}</p>
<p><strong>Total de usuários encontrados: {total}</strong></p>
<hr>
"""

    # 5. Mensagem caso não haja usuários
    if total == 0:
        html += "<p>Nenhum usuário encontrado para essa cidade.</p>"
    else:
        for usuario in usuarios_filtrados:
            nome = usuario["name"]
            email = usuario["email"]
            cidade = usuario["address"]["city"]
            telefone = usuario["phone"]  # 2. campo telefone

            # 1. cada usuário dentro de um card (div com class="card")
            html += f"""
    <div class="card">
        <h2>{nome}</h2>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>Cidade:</strong> {cidade}</p>
        <p><strong>Telefone:</strong> {telefone}</p>
    </div>
"""

    html += """
</body>
</html>
"""

    with open("usuario.html", "w", encoding="utf-8") as arquivo:
        arquivo.write(html)

    arquivo_html = Path("usuario.html").resolve()
    endereco = arquivo_html.as_uri()
    webbrowser.open(endereco)
    print("criado com sucesso")
    print("abrindo navegador")

except requests.exceptions.ConnectionError:
    print("erro de conexao")
    print("ve a net ai")

except requests.exceptions.Timeout:
    print("\n tempo dms", "tenta dnv pai")

except requests.exceptions.HTTPError as erro:
    print("\n erro no http", erro)