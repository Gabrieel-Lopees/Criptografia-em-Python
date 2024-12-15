import hashlib

def calcular_md5(texto):
    return hashlib.md5(texto.encode()).hexdigest()

def processar_arquivo(arquivo_entrada, arquivo_saida):
    with open(arquivo_entrada, 'r') as entrada, open(arquivo_saida, 'w') as saida:
        for linha in entrada:
            linha = linha.strip()
            if linha:
                hash_md5 = calcular_md5(linha)
                saida.write(f"{hash_md5}\n")

def main():
    arquivo_entrada = 'dictionary.txt'
    arquivo_saida = 'dictionaryMD5.txt'

    processar_arquivo(arquivo_entrada, arquivo_saida)
    print(f"Hashes MD5 armazenados em {arquivo_saida}.")

if __name__ == "__main__":
    main()