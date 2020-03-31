print("")
print("Esse programa calcula a franquia de internet que será liberada ao cliente com base nos pontos que ele possui")
print("")
pontos = int(input("Qual a pontuação do cliente?: "))
if pontos >= 1000:
    print("\nO cliente receberá mais 3gb em sua franquia de internet!")
elif pontos >= 500:
    print("\nO cliente receberá mais 1,5gb em sua franquia de internet!")
elif pontos >= 200:
    print("\nO cliente receberá mais 500mb em sua franquia de internet!")
else:
    print("\nA pontuação do cliente está muito baixa, por enquanto não poderemos liberar bônus em sua franquia de internet.")
