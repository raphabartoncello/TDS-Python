print("\nVotação para escolher o melhor dia da semana para realização das lives\n")
print("Informe abaixo a quantidade de votos de cada dia da semana:")
segunda = int(input("\nQuantos alunos votaram na segunda-feira? "))
votos = segunda
terca = int(input("\nQuantos alunos votaram na terça-feira? "))
votos = votos + terca
quarta = int(input("\nQuantos alunos votaram na quarta-feira? "))
votos = votos + quarta
quinta = int(input("\nQuantos alunos votaram na quinta-feira? "))
votos = votos + quinta
sexta = int(input("\nQuantos alunos votaram na sexta-feira? "))
votos = votos + sexta
print("\n A quantidade total de votos foi de {}".format(votos))
if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print("\nA segunda-feira recebeu mais votos, venceu com {} votos, o que equivale a {:.2f}%.".format(segunda, (segunda/votos)*100))
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print("\nA terça-feira recebeu mais votos, venceu com {} votos, o que equivale a {:.2f}%.".format(terca, (terca/votos)*100))
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print("\nA quarta-feira recebeu mais votos, venceu com {} votos, o que equivale a {:.2f}%.".format(quarta, (quarta/votos)*100))
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print("\nA quinta-feira recebeu mais votos, venceu com {} votos, o que equivale a {:.2f}%.".format(quinta, (quinta/votos)*100))
elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    print("\nA sexta-feira recebeu mais votos, venceu com {} votos, o que equivale a {:.2f}%.".format(sexta, (sexta/votos)*100))
else:
    print("\nNão houve votação ou todos os dias receberam a mesma quantidade de votos.")
