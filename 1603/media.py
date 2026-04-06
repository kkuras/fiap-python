num1 = float(input("digite sua nota 1: "))
num2 = float(input("digite sua nota 2: "))
num3 = float(input("digite sua nota 3: "))
num4 = float(input("digite sua nota 4: "))

media = (num1 + num2 + num3 + num4)/4
if(media>= 7.0):
    print(f"Parabens! vc passou de ano, quer saber mesmo assim sua media? tabom ela ficou: {media}")
else:
    print(f"tu nao passou de ano :(, sua media é {media}")