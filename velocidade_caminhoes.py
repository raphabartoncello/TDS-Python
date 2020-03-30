print("\nEsse programa calcula a velocidade necessária para entregar a mercadoria no prazo acordado.\n")

distancia = float(input("Qual a distância a ser percorrida? (em km): "))
tempo = float(input("\nEm quanto tempo a mercadoria deve ser entregue? (em horas): "))

velocidade_media = distancia/tempo

print("A velocidade média é {} km/h".format(velocidade_media))
