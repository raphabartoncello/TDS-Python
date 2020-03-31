print("")
print("Olá, venha participar do campeonato da FIAP! Para se inscrever basta preencher os campos abaixo:")
print("")
RM = input("Qual o seu RM?: ")
Idade = int(input("\n Qual a sua idade?: "))
if Idade >= 18:
    print("\nParabéns, sua inscrição foi finalizada aluno {}!".format(RM))
    print ("\nEnviamos mais informações no seu email de cadastro.")
else:
    autorizacao = input("\nVocê é menor de idade, você possui autorização do seu responsável legal? (Sim ou Não): ")
    autorizacao = autorizacao.lower()
    if autorizacao == "sim":
        print("\nParabéns, sua inscrição foi finalizada aluno {}!".format(RM))
        print ("\nEnviamos mais informações no seu email de cadastro.")
    else:
        print("\nSua inscrição não foi finalizada, para participar do campeonato sendo menor de idade é necessário possuir autorização do responsável legal.")
