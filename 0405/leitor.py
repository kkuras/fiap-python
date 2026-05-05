arquivo = open("dados.txt", "w", encoding="utf-8")
arquivo.write("linha 1 - aula de python\n")
arquivo.write("linha 2 - segunda feira\n")
arquivo.close()
print("arquivo criado com sucesso")

arquivo = open("dados.txt", "r", encoding="utf-8")  # corrigido: "r" para leitura
conteudo = arquivo.read()
print("\nconteudo do arquivo")
print(conteudo)
arquivo.close()

arquivo = open("dados.txt", "a", encoding="utf-8")
arquivo.write("linha 3 - amanha tem mentoria\n")
arquivo.close()  # só um close aqui
print("conteudo adicionado com sucesso")

with open("dados.txt", "r", encoding="utf-8") as arquivo:
    print("\n deadline() - le uma linha:")
    print(arquivo.readline())
    linhas = arquivo.readline()
    print(linhas)