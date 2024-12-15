from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os

def gerar_chaves():
    chave = RSA.generate(2048)  
    chave_privada = chave.export_key()  
    chave_publica = chave.publickey().export_key() 
    
    with open("chave_privada.pem", "wb") as f_privada:
        f_privada.write(chave_privada)
    
    with open("chave_publica.pem", "wb") as f_publica:
        f_publica.write(chave_publica)

def criptografar(mensagem):
    with open("chave_publica.pem", "rb") as f_publica:
        chave_publica = RSA.import_key(f_publica.read())
    
    cifra = PKCS1_OAEP.new(chave_publica)
    mensagem_encriptada = cifra.encrypt(mensagem.encode()) 
    return mensagem_encriptada

def descriptografar(mensagem_encriptada):
    with open("chave_privada.pem", "rb") as f_privada:
        chave_privada = RSA.import_key(f_privada.read())
    
    cifra = PKCS1_OAEP.new(chave_privada)
    mensagem_descriptografada = cifra.decrypt(mensagem_encriptada).decode() 
    return mensagem_descriptografada

def main():
    gerar_chaves()
    
    mensagem = input("Digite a mensagem a ser criptografada: ")
    
    mensagem_encriptada = criptografar(mensagem)
    print("Mensagem criptografada foi salva no arquivo 'mensagem'.")
    
    with open("mensagem", "rb") as f_mensagem:
        mensagem_encriptada = f_mensagem.read()
    
    mensagem_descriptografada = descriptografar(mensagem_encriptada)
    print("Mensagem descriptografada: ", mensagem_descriptografada)
    
if __name__ == "__main__":
    main()


 #b's\xc0\x92z\xfaNIA\x04\xb0u\xe3\x96\xb1\xb8\xf4\x98\x92\x12\x11d\xf3\'\xe0\\\xf5\x7f\xdd\x18\xf2#hdU\x12\xd8j\xfd\x13$\x86\x08\x93\x03\xd0\x8bS\xd4h\xc4\xb1\xc7Lw\x16c\xdd\xdd\x9da\xafLc\xcf\x1e\xfc+\'\xdd\xc3\xe3\x0f\x11\xc3{<bC\x03\x93j\x1e\xbf\x96\xe9/\r\xeb\x18_M\xe8\xdfM\xe7\xcc>~-b\xd6\xe9}WiR\x8cc_\xdb\n\t/\xf9\x18\xdb\xe6\x84\xd9f\x88\xcf\xa6!\xa6\x02\xa9k\x9e(\x92\xbb0\x98\xba\xd6BQ^\'!\xca\xaa\xf4R\xb6\xc1]y\xb1v\x12\x88q\xa2\x16\x98\x15\xde\xf7R\xdbcIOy\xe6p\x9f\xe8\x8fcJ\x83f\xb9\xd1P\xce-\x99,\x03\x00aS\x0f\xcb@A:\xb5"\x85\xf9\xb5\xc9\x7f]&\\@W\xe8\xa00\x9d\x1e\xdc\x86\x03\xdd\xe6)\x0e\xa2F3\xe10X\xecw\xfa\xd6\xb7\xa9\x9b\x867c\x17\xab\xf7\xc1g\x85\xcb\xdd\x9b\xf9I__\xc4\xdc\xc6\x16 \x1d\xad\xe7\xdb\x9f\x1fi'