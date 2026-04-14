#sintaxe: def <nome da funcao> (arg1, arg2, ..........argn)
def soma(a, b):
    resultado = a+b
    return resultado


#chamada
n1 = int(input("digite o valor 1 "))
n2 = int(input("digite o valor 2 "))

res = soma(n1, n2) # valores variaveis com o usuario podendo escolher o valor
#res = soma(5, 3) com valores pre definidos
print("resultado: ", res)

