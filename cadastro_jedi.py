jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]

option = int(input("Olá, esse é o cadastro de jedis, insira o número da opção desejada conforme legenda abaixo:\n \n 1 - Exibir lista\n 2 - Buscar um jedi específico \n 3 - Adicionar jedi\n 4 - Adicionar jedi à uma posição específica\n 5 - Remover jedi \n \nQual a opção desejada: "))

if option == 1:
    print("\nA lista de jedi é: \n{}".format(jedi))
elif option == 2:
    name = input("\nDigite o nome do jedi que deseja pesquisar: ")
    if name in jedi:
        print("\nO jedi {} está cadastrado. ".format(name))
    else:
        print("\nO jedi {} não está cadastrado. ".format(name))
elif option == 3:
    name = input("\nDigite o nome que deseja inserir: ")
    jedi.append(name)
    print("\nA lista atualizada é: \n {}".format(jedi))
    end = int(input("\nDeseja manter as alterações? \n 1- Manter\n 2 - Desfazer\n"))
    if end == 1:
        print("\nA lista se mantém: \n {}".format(jedi))
    elif end == 2:
        jedi.pop()
        print("\nA lista atualizada é: \n {}".format(jedi))
    else:
        print("\nInsira uma opção válida!")
elif option == 4:
    pos = int(input("\nDigite a posição que deseja inserir: "))
    name = input("\nDigite o nome que deseja inserir: ")
    jedi.insert(pos, name)
    print("\nA lista atualizada é: \n {}".format(jedi))
    end = int(input("\nDeseja manter as alterações? \n 1- Manter\n 2 - Desfazer\n"))
    if end == 1:
        print("\nA lista se mantém: \n {}".format(jedi))
    elif end == 2:
        jedi.pop()
        print("\nA lista atualizada é: \n {}".format(jedi))
    else:
        print("\nInsira uma opção válida!")
elif option == 5:
    name = input("\nDigite o nome do jedi que deseja excluir da lista: ")
    jedi.remove(name)
    print("\nA lista atualizada é: \n {}".format(jedi))
    end = int(input("\nDeseja manter as alterações? \n 1- Manter\n 2 - Desfazer\n"))
    if end == 1:
        print("\nA lista se mantém: \n {}".format(jedi))
    elif end == 2:
        jedi.pop()
        print("\nA lista atualizada é: \n {}".format(jedi))
    else:
        print("\nInsira uma opção válida!")
else:
    print("\nInsira uma opção válida!")
