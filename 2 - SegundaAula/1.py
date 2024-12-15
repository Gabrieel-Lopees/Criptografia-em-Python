import os

arqNome = input("Informe o nome do arquivo: ")
arq = open(arqNome, 'r+')

while True:
    print("Escolha uma das opções:")
    print("1 - Exibir o seu conteúdo na tela")
    print("2 - Acrescentar a palavra 'Final' no fim do arquivo")
    print("3 - Deixar este arquivo sem conteúdo algum")

    escolha = int(input("Digite sua escolha: "))

    if escolha == 1:
        arq.seek(0)
        words = [word.strip() for word in arq]
        print(words)
    elif escolha == 2:
        arq.seek(0, os.SEEK_END)
        arq.write("Final\n")
        arq = open(arqNome, 'r+')
    elif escolha == 3:
        arq.truncate()
        arq = open(arqNome, 'r+')
    else:
        print("entrada errada")

    continuar = input("continuar? (s/n): ")
    if continuar.lower() != 's':
        break

arq.close()
