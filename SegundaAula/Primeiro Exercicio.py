import os

arqNome = input("Informe o nome do arquivo: ")
arq = open(arqNome,'r')

print("Escolha essas opções")
print("1 exiba o seu conteúdo na tela")
print("2 acrescente a palavra “Final” no fim do arquivo")
print("3 deixe este arquivo sem conteúdo algum")
print("4 mudar nome do arquivo")
print("5 Encerrar programa")


escolha = int(input())


if escolha == 1:
    words = [word.split(':')[0] for word in arq]
    print(words)
elif escolha == 2:
    arq.close()
    with open(arqNome, 'a') as arq_append:
        arq_append.write("Final")
elif escolha == 3:
    arq.close()
    with open(arqNome,'w') as arq_clear:
        arq_clear.write("")
elif escolha == 4:
    novoNome = input("Informe o novo nome do arquivo: ")
    import os

    os.rename(arqNome, novoNome)  # Renomeia o arquivo
    print(f"O arquivo foi renomeado para: {novoNome}")

else:
    print("Programa encerrado")