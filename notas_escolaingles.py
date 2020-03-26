print("\n Esse sistema calcula a nota dos 50 alunos da sala que estudam na escola de inglês JoWell Sant'ana")

print("\n Vamos começar com as notas dos alunos ímpares: ")

contador_impar = 1
somanotas_impar = 0

for contador_impar in range(1,50,2):
    notas_impar = str(input("\nInsira a nota do(a) aluno(a) {}: ".format(contador_impar)))
    contador_impar = contador_impar + 2
    notas_impar = notas_impar.replace(",", ".")
    somanotas_impar = float(somanotas_impar) + float(notas_impar)

media_impar = float(somanotas_impar/25)

print("\nA média da nota dos alunos ímpares da sala é de {}.".format(media_impar))

print("\n Agora vamos calcular as notas dos alunos pares: ")

contador_par = 2
somanotas_par = 0

for contador_par in range(2,51,2):
    notas_par = str(input("\nInsira a nota do(a) aluno(a) {}: ".format(contador_par)))
    contador_par = contador_par + 2
    notas_par = notas_par.replace(",", ".")
    somanotas_par = float(somanotas_par) + float(notas_par)

media_par = float(somanotas_par/25)

print("\nA média da nota dos alunos pares da sala é de {}.".format(media_par))

print("\nOs 25 alunos ímpares obtiveram a média de {:.2f} e os 25 alunos pares obtiveram a média de {:.2f}".format(media_impar,media_par))

if media_par > media_impar:
    print("\nOs alunos pares tiveram um melhor desempenho.")
elif media_par < media_impar:
    print("\nOs alunos ímpares tiveram um melhor desempenho.")
else:
    print("\nO desempenho dos alunos pares e ímpares foi igual!")
