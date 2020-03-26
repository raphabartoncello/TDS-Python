print("\n Pesagem da carga total a ser transportada, capacidade por caminhão de 100 caixas.\n")

peso_total = 0
caixa = 1

for x in range(1,101):
    peso_atual = str(input("\nPor favor informe o peso da caixa {}:".format(caixa)))
    caixa = caixa + 1
    peso_atual = peso_atual.replace(",", ".")
    peso_total = float(peso_total) + float(peso_atual)

media = peso_total/100

print("\nO caminhão está carregado com 100 caixas que pesam {:.2f} kg. O peso médio por caixa é de {} kg.".format(peso_total,media))
