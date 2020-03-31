def somar(a, b):
    return float(a) + float(b)


def subtrair(a, b):
    return float(a) - float(b)


def multiplicar(a, b):
    return float(a) * float(b)


def dividir(a, b):
    if b == 0:
        print("\nNão é possível dividir por 0 em números reais!")
    else:
        return float(a) / float(b)