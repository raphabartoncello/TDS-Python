altura = float(input("Qual a sua altura? (Ex: 1.75): "))
peso = float(input("\nQual o seu peso? (Ex: 60.50): "))
alturaIMC = float(altura ** 2)
IMC = peso / alturaIMC
print("\n Seu IMC é {:.2f}".format(IMC))
if IMC < 16:
    print("\nDe acordo com o seu IMC você está na categoria Baixo peso grau III")
elif IMC <= 17:
    print("\nDe acordo com o seu IMC você está na categoria Baixo peso grau II")
elif IMC <= 18.49:
     print("\nDe acordo com o seu IMC você está na categoria Baixo peso grau I")
elif IMC <= 24.99:
     print("\nDe acordo com o seu IMC você está na categoria Peso Ideal")
elif IMC <= 29.99:
     print("\nDe acordo com o seu IMC você está na categoria Sobrepeso")
elif IMC <= 34.99:
     print("\nDe acordo com o seu IMC você está na categoria Obesidade grau I")
elif IMC <= 39.99:
     print("\nDe acordo com o seu IMC você está na categoria Obesidade grau II")
elif IMC >= 40:
     print("\nDe acordo com o seu IMC você está na categoria Obesidade grau III")
else: print("\nNão foi possível realizar o cálculo, por favor tente novamente")
