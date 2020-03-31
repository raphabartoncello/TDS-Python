print ("")
print ("Olá, insira seus dados abaixo e verifique se poderá participar da visita de campo com a turma!")
print ("")
email_aluno = input("\nInforme seu email: ")
nota_semestral = float(input("\nInforme a sua nota semestral: "))
if nota_semestral > 8.5:
    print("\nParabéns! Enviamos mais detalhes sobre a visita de campo no seu email: {}".format(email_aluno))
else:
    print("\nInfelizmente você não poderá participar da visita de campo, se esforce mais no próximo semestre!")
