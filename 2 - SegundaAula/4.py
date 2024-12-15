import hashlib

def calcular_hash(nome):
    return hashlib.sha256(nome.encode()).hexdigest()

def ler_nomes(arquivo_nome):
    with open(arquivo_nome, 'r') as arquivo:
        nomes = [linha.strip() for linha in arquivo.readlines()]
    return nomes

def main():
    arquivo_nome = input("Informe o nome do arquivo que tem os nomes.txt dos usuarios: ")

    try:
        nomes = ler_nomes(arquivo_nome)
        for nome in nomes:
            hash_nome = calcular_hash(nome)
            print(f"{nome}: {hash_nome}")
    except FileNotFoundError:
        print(f"Erro: arquivo não encontrado")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()