lista = [10, 20, 30, 40, 50, 60]

print("indice do 1 ao 3: ", lista[1:4])
print("do inicio ate 2: ", lista[:3])
print("do 3 ate o finm: ", lista[3:])

copia = lista[:]
print(copia)
print("pula de 2 em 2: ", lista[::2])

print("invertida: ", lista[::-1])

tupla = (1,2,3,4,5)

print("fatiamento da tu-pla: ", tupla[1:4])

print("=================================")

nome = "python"
print("primeira letra: ", nome[0])
print("fatiamento: ", nome[0:3])
print("inverter: ",  nome[::-1])

print("===============================")

texto = "palmeiras nao tem libertadores"
print("substituicao: ", texto.replace("libertadores", "mundial"))
print("sem espaço: ", texto.strip( ))
palavras = texto.split()
print("dividindo em lista:", palavras)

print("===============")

novo_texto = "-".join(palavras)
print("UNIDO COM -: ", novo_texto)

pos = texto.find("tem")
print("posicao da palavra tem:", pos)
print("existe libertadores:", "libertadores" in texto)

def vogal_maiuscula(texto):
    texto = texto.replace("a", "A")
    texto = texto.replace("e", "E")
    texto = texto.replace("i", "I")
    texto = texto.replace("o", "O")
    texto = texto.replace("u", "U")
    return texto
print(vogal_maiuscula("libertadores"))

print("============================")

def  retorna_indice(texto, caractere):
    indice=[]
    for i in range (len(texto)):
        if texto[i]==caractere:
            indice.append(i)
    return indice
print(retorna_indice("palmeiras nao tem mundial", "a"))

print("============================")

def isfloat(texto):
    if texto.count('.')>1:
        return False
    if texto[0] == '-' or texto[0]=='+':
        texto = texto[1:]
    texto = texto.replace('.', '')
    return texto.isdigit()

print(isfloat("45.78"))
print(isfloat("-12.45"))
print(isfloat("abc"))

def eh_numero(texto):
    if texto[0] == '-' or texto[0]== '+':
        texto = texto[1:]
    for c in texto:
         if c<'0' or c> '9':
              return False
    return True
print(eh_numero("-123"))
print(eh_numero("12a3"))