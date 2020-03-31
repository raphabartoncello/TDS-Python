from calc import somar, subtrair, multiplicar, dividir

valor1 = float(input("Digite um valor: "))
valor2 = float(input("Digite outro valor: "))

option = int(input(
    "Qual operação iremos realizar?\n 1 - Somar\n 2 - Subtrair\n 3 - Multiplicar\n 4 - Dividir\nDigite a opção desejada: "))

if option == 1:
    soma = somar(valor1, valor2)
    print("A soma é: {}".format(soma))
elif option == 2:
    sub = subtrair(valor1, valor2)
    print("A subtração é: {}".format(sub))
elif option == 3:
    mult = multiplicar(valor1, valor2)
    print("A multiplicação é: {}".format(mult))
elif option == 4:
    div = dividir(valor1, valor2)
    print("A divisão é: {}".format(div))
else:
    print("Insira uma opção válida!")
