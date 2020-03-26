print("\nDescriptografia de senha\n")

from datetime import datetime
agora = datetime.now()
print ("Agora é {}".format(agora))

min = int(input("\nInforme qual o minuto atual (hora acima): "))

#calculando o fatorial
contador = min
fatorial = 1
print("\nO valor de {}! é:\n".format(contador))
while contador > 0:
    print("{} ".format(contador), end='')
    print("x " if contador > 1 else " = ", end='')
    fatorial = fatorial * contador
    print("{}".format(fatorial))
    contador = contador - 1

palavra = "LIBERDADE"
resultado = str(fatorial)

senha = palavra+resultado

print("\nA senha é {}".format(senha))
