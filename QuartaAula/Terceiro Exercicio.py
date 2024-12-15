import hashlib

def criptografar_senha(senha):
    hash_obj= hashlib.sha512(senha.encode())
    
    return hash_obj.hexdigest()

usuario = input("Digite o nome do usuario: ")
senha = input("Digite a sua senha: ")
senha_criptografada = criptografar_senha(senha)

with open("usuarios.txt", "a") as arquivo:
           arquivo.write(f"{usuario}: {senha_criptografada}\n")
           
print("Usuario e senha armazenados com sucesso em usuarios.txt")