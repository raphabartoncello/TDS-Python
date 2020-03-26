print("\nDescriptografia de senha\n")

from datetime import timezone, datetime
agora = datetime.now(tz=timezone.utc)
print("O minuto atual é: {}.".format(agora.strftime("%M")))

min = int(input("\nInforme qual o minuto atual (acima): "))

#calculando o fatorial
contador = min
fatorial = 1

while contador > 0:
    fatorial = fatorial * contador
    contador = contador - 1

palavra = "LIBERDADE"
resultado = str(fatorial)

senha = palavra+resultado

print("\nA senha é {}".format(senha))
