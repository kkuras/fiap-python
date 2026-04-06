
pedido = 36
valor1 = 45.983
valor2 = 2058.4
valor3 = 314.3
valor_decimal = 12
print(f"""
      Pedido.......: {pedido}
      Pedido.......: {pedido:5d}
      Pedido.......: {pedido:05d}
      
      Valor........: {valor1}
      Valor........: {valor2}
      Valor........: {valor3}
      
      Valor........: {valor1:10.2f}
      Valor........: {valor2:10.2f}
      Valor........: {valor3:10.2f}

      Decimal: {valor_decimal} | Octal: {valor_decimal:0} | Hexadecimal: {valor_decimal:x}

""")