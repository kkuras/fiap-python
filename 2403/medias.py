##soma = 0

 ## for i in range(5):
    ##num = int(input(f"Digite o {i+1} numero:"))
    ##soma += num #somatoria dos numeros informados pelo usuarios

##media = soma / 5 #calculo da media
##print(media)

cont = 1
soma = 0
while cont <= 5:
    num = int(input("Digite o numero: "))
    soma += num
    cont +=1
media = soma / (cont -1)
print(media)