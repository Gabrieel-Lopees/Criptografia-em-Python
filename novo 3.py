from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os

# Função para gerar as chaves RSA
def gerar_chaves():
    chave = RSA.generate(2048)  
    chave_privada = chave.export_key()  
    chave_publica = chave.publickey().export_key() 
    
    # Salvando as chaves em arquivos
    with open("chave_privada.pem", "wb") as f_privada:
        f_privada.write(chave_privada)
    
    with open("chave_publica.pem", "wb") as f_publica:
        f_publica.write(chave_publica)
    print("Chaves geradas e salvas em 'chave_privada.pem' e 'chave_publica.pem'.")

# Função para criptografar a mensagem e salvar no arquivo 'mensagem'
def criptografar(mensagem):
    with open("chave_publica.pem", "rb") as f_publica:
        chave_publica = RSA.import_key(f_publica.read())
    
    cifra = PKCS1_OAEP.new(chave_publica)
    mensagem_encriptada = cifra.encrypt(mensagem.encode()) 
    
    with open("mensagem", "wb") as f_mensagem:
        f_mensagem.write(mensagem_encriptada)
    print("Mensagem criptografada foi salva no arquivo 'mensagem'.")
    
    return mensagem_encriptada

# Função para descriptografar a mensagem
def descriptografar():
    with open("chave_privada.pem", "rb") as f_privada:
        chave_privada = RSA.import_key(f_privada.read())
    
    # Lendo a mensagem criptografada do arquivo
    try:
        with open("mensagem", "rb") as f_mensagem:
            mensagem_encriptada = f_mensagem.read()
    except FileNotFoundError:
        print("Erro: O arquivo 'mensagem' não foi encontrado.")
        return
    
    cifra = PKCS1_OAEP.new(chave_privada)
    mensagem_descriptografada = cifra.decrypt(mensagem_encriptada).decode()
    return mensagem_descriptografada

# Função principal com o menu de opções
def main():
    while True:
        print("\nEscolha uma opção:")
        print("1. Gerar novas chaves.")
        print("2. Gerar um arquivo 'mensagem' (criptografando uma mensagem).")
        print("3. Descriptografar uma mensagem no arquivo 'mensagem'.")
        print("4. Sair.")
        
        opcao = input("Digite o número da opção desejada: ")
        
        if opcao == "1":
            gerar_chaves()
        
        elif opcao == "2":
            mensagem = input("Digite a mensagem a ser criptografada: ")
            criptografar(mensagem)
        
        elif opcao == "3":
            mensagem_descriptografada = descriptografar()
            if mensagem_descriptografada:  # Só imprime a mensagem se a descriptografia for bem-sucedida
                print("Mensagem descriptografada:", mensagem_descriptografada)
        
        elif opcao == "4":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
