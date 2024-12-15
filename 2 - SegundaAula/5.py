import hashlib

def hash_senha(senha):
    return hashlib.sha512(senha.encode()).hexdigest()

def armazena_usuario(nome_arquivo, usuario, senha_hash):
    with open(nome_arquivo, 'a') as arquivo:
        arquivo.write(f"{usuario}:{senha_hash}\n")

def main():
    nome_arquivo = 'usuario.txt'

    usuario = input("informe o nome de usuario: ")
    senha = input("informe a senha: ")

    senha_hash = hash_senha(senha)
    armazena_usuario(nome_arquivo, usuario, senha_hash)

    print(f"usuario {usuario} armazenado com sucesso!!")

if __name__ == "__main__":
    main()