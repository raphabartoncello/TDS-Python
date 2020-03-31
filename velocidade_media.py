#Definindo a função

def velocidade_media(distancia, tempo):
    
    velocidade_media = distancia/tempo
    return velocidade_media
    
#Iniciando o programa
print ("\n Essa é uma calculadora de velocidade média!\n")
#Chamando o programa - função

distancia = float(input("Digite a distância percorrida: "))
tempo = float(input("Digite o tempo da viagem: "))
    
print("A velocidade média é {:.2f} km/h".format(velocidade_media(distancia, tempo)))


