nomes    = []

def adicionar():
    nome = input("Digite o nome para cadastrar: ").strip()
    if nome =="":
        print("nome invalido")
    else:
        nomes.append(nome)
        print("nome cadastrado")

def listar():
    if len(nomes) == 0:
                print("Lista vazia!")
    else:
        for n in nomes:
            print(n)

def maiusculo():
    for m in nomes:
         print(m.upper())

def buscador():
    buscar = input("Digite o nome: ")

    for nome in nomes:
        if buscar.lower() == nome.lower():
            print("Nome encontrado: ", nome)
            break 
    else:
        print("Nome não encontrado.")

def invertido():
    for inv in nomes:
         print(inv[::-1])

opcao = -1

while True:

    print("===MENU===")
    print("digite 1 para cadastrar um aluno")
    print("digite 2 para ver todos os alunos")
    print("digite 3 para mostrar nome em maiusculo")
    print("digite 4 para buscar um nome")
    print("digite 5 para exibir nome invertido")
    print("digite 6 para sair")

    opcao = int(input("\nEscolha a opção: "))
    match opcao:
        case 1:
            adicionar()

        case 2:
            listar()
                
        case 3:
            maiusculo()

        case 4:
            buscador()

        case 5:
            invertido()
              
        case 6:
            print("Saindo..")
            break

