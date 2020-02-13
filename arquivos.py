'''
try:
    file = open("Dados.txt", "r")
    for linha in file:
        campos = linha.split(';')
        print(campos)
    file.close()
except IOError as error:
    print("ERRO: ", error)

try:
    file = open('Dados.txt','r')
    for linha in file:
        campos = linha.split(';')
        print("id: ", campos[0])
        print("Nome: ", campos[1])
        print("Fone: ", campos[2])
    file.close()
except IOError as error:
    print("ERRO: ", error)


try:
    file = open('Dados.txt', 'r')
    id = 1
    for linha in file:
        id = id + 1 # contar o número de registros
    file.close()

    file = open('Dados.txt','a') # anexando no fim do arquivo
    nome = "Pessoa"
    while nome != "":
        print("id: ", id)
        nome = input("Nome: ")
        if nome != "":
            fone = input("Fone: ")
            linha = str(id) + ";" + nome + ";" + fone + ";" + "\n"
            file.write(linha)
            id = id + 1
    file.close()
except IOError as error:
    print("ERRO: ", error)



try:
    file = open('FileNew', 'w') # cria novo arquivo texto
    id = 1 # cuidado, apaga se existir
    nome = "Pessoa"
    while nome != "":
        print("id: ", id)
        nome = input("Nome: ")
        if nome != "":
            fone = input("Fone: ")
            linha = str(id) + ";" + nome + ";" + fone + ";" + "\n"
            file.write(linha)
            id = id + 1
    file.close()
except IOError as error:
    print("ERRO: ", error)


try:
    file = open("Dados.txt", "r")
    posicao = 1
    while posicao != 0:
        posicao = int(input("Posição [0 - Sair]: "))
        file.seek(0, 0) # reinicializa o cursor do arquivo no início
        imprimiu = False
        for linha in file:
            campos = linha.split(';')
            if campos[0] == str(posicao):
                imprimiu = True
                print("id: ", campos[0])
                print("Nome: ", campos[1])
                print("Fone: ", campos[2])
        if not imprimiu:
            print("Erro: Registro não encontrado")
    file.close()
except IOError as error:
    print("ERRO: ", error)
'''

try:
    file = open("Dados.txt", "r")
    nome = "Pessoa"
    while nome != "":
        nome = input("Nome: ")
        file.seek(0, 0)
        imprimiu = False
        for linha in file:
            campos = linha.split(';')
            if nome == campos[1]:
                imprimiu = True
                print("id: ", campos[0])
                print("Nome: ", campos[1])
                print("Fone: ", campos[2])
        if not imprimiu:
            print("Erro: Nome não encontrado")
    file.close()
except IOError as error:
    print("ERRO: ", error)
