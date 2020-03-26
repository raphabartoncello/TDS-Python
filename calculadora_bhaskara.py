print ("")
print ("Bem vinda(o) a calculadora de Bhaskara!")
print ("")
import math
a = float(input("Informe o valor de A: "))
b = float(input("\nInforme o valor de B: "))
c = float(input("\nInforme o valor de C: "))

# x = -b +- ((b^2 - 4ac)^1/2)/2a

delta = b * b - 4 * a *c
if delta > 0.0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("\nPara a equação {}x² + {}x + {} = 0, obtivemos os seguintes valores: x1 = {} e x2 = {}".format(a, b, c, x1, x2))
else:
    if delta == 0:
        x = (-b + math.sqrt(delta)) / (2 * a)
        print("\nPara a equação {}x² + {}x + {} = 0, obtivemos o seguinte valor: x = {}".format(a, b, c, x))
    else:
        print("\nPara a equação {}x² + {}x + {} = 0, não existem valores reais para x".format(a, b, c))
