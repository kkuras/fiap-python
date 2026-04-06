vendas_total = int(input("Digite a quantidade de vendas: "))
if(vendas_total>=1000):
    desconto5 = vendas_total * (5/100)
    print(f"o total de vendas foi de {vendas_total} e seu desconto é {desconto5}")
else:
    desconto3 = vendas_total * (3/100)
    print(f"o total de vendas foi de {vendas_total} e seu desconto é {desconto3}")