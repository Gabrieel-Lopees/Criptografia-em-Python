import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
import getpass

def gerar_chave():
    return os.random(32)

def cripto(conteudo, chave):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(chave), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    pad_conteudo = conteudo + b' ' * (16 - len(conteudo) % 16)

    conteudo_criptografado = ecnryptor.update(pad_conteudo) + encryptor.finalize()

    return base64.b64encode(iv + conteudo_criptografado).decode('utf-8')

def des(conteudo_criptografado, chave):
    conteudo_criptografado = base64.b64decode(conteudo_criptografado.encode('utf-8'))
    iv = conteudo_criptografado[:16]
    conteudo_criptografado = conteudo_criptografado[16:]

    cipher = Cipher(algorithms.AES(chave), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    coneudo_descriptografado = decryptor.update(conteudo_criptografado) + decryptor.finalize()
    return conteudo_descriptografado.rstrip().decode('utf-8')

def pedir_senha():
    return getpass.getpass("Digite a senha do diário: ")

def diario():
    arquivo_diario = "diario.txt.enc"

    if os.path.exists(arquivo_diario):
        senha = pedir_senha()
        chave = senha.encode('utf-8')[:32]

        with open(arquivo_diario, 'r') as file:
            conteudo_criptografado = file.read()

        try:
            conteudo = des(conteudo_criptografado, chave)
            print("\nDiario: \n", conteudo)
        except:
            print("Erro")
            return

        nova = input("\nGostaria de adicionar algo ao diário? (y/n): ")
        if nova_entrada() == 's':
            conteudo += "\n\n" + input("\t 'Ex: Sexta, 3 de janeiro de 2024' \n\tNova entrada")

        conteudo_criptografado = criptografar(conteudo.encode('utf-8'), chave)
        with open(arquivo_diario, 'w') as file:
            file.write(conteudo_criptografado)
        print("Diario atualizado e fechado")

    else:
        senha = pedir_senha()
        chave = senha.encode('utf-8')[:32]

        conteudo = input("Digite sua primeira entrada no diário: ")

        conteudo_criptografado = cripto(conteudo.encode('utf-8'), chave)
        with open(arquivo_diario, 'w') as file:
            file.write(conteudo_criptografado)
        print("Diario criado e fechado.")




if __name__ == "__main__":
    diario()
