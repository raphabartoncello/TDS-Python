print("\nVamos calcular quantas calorias você ingeriu hoje?")

qtdade = int(input("\nQuantos alimentos você ingeriu hoje?: "))
contador = 1
caloria_total = 0

if qtdade <= 1:

    caloria = str(input("\nQuantas calorias tem o alimento número ingerido?: "))
    caloria = caloria.replace(",", ".")
    caloria_total = float(caloria)
    print("\nA quantidade total de calorias consumidas foi de {:.2f} calorias.".format(caloria_total))

else:
    print("\nVocê consumiu {} alimentos.".format(qtdade))
    for contador in range(1, (qtdade+1)):
        media = caloria_total/qtdade
        caloria = str(input("\nQuantas calorias tem o alimento número {}: ".format(contador)))
        contador = contador + 1
        caloria = caloria.replace(",", ".")
        caloria_total = float(caloria_total) + float(caloria)

    consumo_total = caloria_total

    print("\nA quantidade total de calorias consumidas nos {} alimentos informados foi de {:.2f} calorias, totalizando uma média de {:.2f} calorias por alimento ingerido.".format(qtdade,consumo_total,media))
