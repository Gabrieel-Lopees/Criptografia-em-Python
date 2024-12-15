from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Função para descriptografar a mensagem
def descriptografar(mensagem_encriptada):
    with open("chave_privada.pem", "rb") as f_privada:
        chave_privada = RSA.import_key(f_privada.read())
    
    cifra = PKCS1_OAEP.new(chave_privada)
    mensagem_descriptografada = cifra.decrypt(mensagem_encriptada).decode()
    return mensagem_descriptografada

# Função principal
def main():
    # Lendo a mensagem criptografada do arquivo "mensagem"
    try:
        with open("mensagem", "rb") as f_mensagem:
            mensagem_encriptada = f_mensagem.read()
    except FileNotFoundError:
        print("Erro: O arquivo 'mensagem' não foi encontrado.")
        return
    
    # Descriptografando a mensagem
    mensagem_descriptografada = descriptografar(mensagem_encriptada)
    
    print("Mensagem descriptografada: ", mensagem_descriptografada)

if __name__ == "__main__":
    main()
