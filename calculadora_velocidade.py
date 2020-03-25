print("")
print("Olá, vamos calcular a velocidade média percorrida?")
print("")
distancia = float(input("Informe a distância percorrida em metros:"))
print("")
tempo = float(input("Informe em quantos minutos foi percorrida essa distância:"))
print("")
vel_media = distancia / tempo
print("A velocidade média foi de {:.2f} metros/minutos para percorrer {} metros em {} minutos.".format(vel_media,distancia,tempo))