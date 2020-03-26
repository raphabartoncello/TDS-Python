print ("")
print ("Bem vinda(o) a calculadora de descontos!")
print ("")
valor_compra = input("Qual o valor total da compra?: ")
valor_compra = valor_compra.replace(",", ".")
desconto = str(input("\nDigite o cupom de desconto: "))
desconto = desconto.upper()
valor_final = float
if desconto == "NIVER10":
    valor_final = float(valor_compra) * 0.9
else:
    valor_final = str(valor_compra)
    print("\nPor favor digite um cupom de desconto válido.")
print("\nO valor final da compra é de R${:.2f}".format(valor_final))
