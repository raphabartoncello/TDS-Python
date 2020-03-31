print ("")
print("Calculadora de bônus a ser pago")
print ("")

faturamento = float(input("\nQual foi o faturamento anual? "))
assinatura = int(input("Qual a sua assinatura? \n1 - Basic \n2 - Silver \n3 - Gold \n4 - Platinum\n"))

if assinatura ==1:
    print("O valor a ser pago é de R${:.2f}".format(faturamento * 0.3))
elif assinatura ==2:
    print("O valor a ser pago é de R${:.2f}".format(faturamento * 0.2))
elif assinatura ==3:
    print("O valor a ser pago é de R${:.2f}".format(faturamento * 0.1))
elif assinatura ==4:
    print("O valor a ser pago é de R${:.2f}".format(faturamento * 0.05))
else:
    print("\nInsira uma assinatura válida, os planos disponíveis são: Basic, Silver, Gold e Platinum, insira o respectivo número conforme orientação inicial.")
