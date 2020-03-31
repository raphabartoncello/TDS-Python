def somar(a, b):
    return float(a) + float(b)


def subtrair(a, b):
    return float(a) - float(b)


def multiplicar(a, b):
    return float(a) * float(b)


def dividir(a, b):
    return float(a) / float(b)


option = int(input(
    "Qual operação iremos realizar?\n 1 - Somar\n 2 - Subtrair\n 3 - Multiplicar\n 4 - Dividir\nDigite a opção desejada: "))

if option == 1:
    a = float(input("Insira o primeiro valor: "))
    b = float(input("Insira o segundo valor: "))
    print("A soma de {} e {} é: {}".format(a, b, somar(a, b)))
elif option == 2:
    a = float(input("Insira o primeiro valor: "))
    b = float(input("Insira o segundo valor: "))
    print("A subtração de {} e {} é: {}".format(a, b, subtrair(a, b)))
elif option == 3:
    a = float(input("Insira o primeiro valor: "))
    b = float(input("Insira o segundo valor: "))
    print("A multiplicação de {} e {} é: {}".format(a, b, multiplicar(a, b)))
elif option == 4:
    a = float(input("Insira o primeiro valor: "))
    b = float(input("Insira o segundo valor: "))
    if b == 0:
        print("\nNão é possível dividir por 0 em números reais!")
    else:
        print("A divisão de {} e {} é: {}".format(a, b, dividir(a, b)))
else:
    print("Insira uma opção válida!")
