def soma(a, b):
    resultado_soma = a+b
    return resultado_soma

def sub(a, b):
    resultado_sub = a-b
    return resultado_sub

def multi(a, b):
    resultado_multi = a * b
    return resultado_multi

def div(a, b):
    if b ==0:
        print("nao existe divisao")
        return None
    else:
        resultado_div = a / b
        return resultado_div



while True:

    print("==menu==")
    print("digite somar para iniciar uma somatoria")
    print("digite subtracao para iniciar uma subtração")
    print("digite multiplicacao para iniciar uma multiplicação")
    print("digite divisao para iniciar uma divisão")
    print("digite sair para sair")

    opcao = input("digite a sua opcao: ")
        
    match opcao:

        case "somar":
            num1 = int(input("digite o valor 1: "))
            num2 = int(input("digite o valor 2: "))

            res = soma(num1, num2)
            print("o valor da soma é: ", res)

        case "subtracao":
            num1 = int(input("digite o valor 1: "))
            num2 = int(input("digite o valor 2: "))

            res = sub(num1, num2)
            print("o valor da subtração é: ", res)

        case "multiplicacao":
            num1 = int(input("digite o valor 1: "))
            num2 = int(input("digite o valor 2: "))

            res = multi(num1, num2)
            print("o valor da multiplicação é: ", res)

        case "divisao":
            num1 = int(input("digite o valor 1: "))
            num2 = int(input("digite o valor 2: "))

            res = div(num1, num2)
            print("o valor da divisão é: ", res)

        case "sair":
            print("saindo..")
            break
