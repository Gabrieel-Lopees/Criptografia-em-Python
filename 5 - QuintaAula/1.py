'''import hmac
from hashlib import md5
key = b'DECLARATION'
h = hmac.new(key,b' ',md5)
# adicona o conteudo da mensagem

h.update(b'Teste de HMAC!!!')
#imprime a assinatura/hash HMAC
print (h.hexdigest() )'''

## Testar o codigo abaixo no baseado Linux
'''
import crypt
from cryptography.fernet import Fernet
cahve = Fernet.generate_key()
cipher_suite = Fernet(chave)
mensagem_cifrada = cipher_suite.encrypt(b'Minha mensagem secreta hiuhiuhiuhiu')
'''

#

import hashlib

texto = input("Digite seu texto: ")
def calcular_md5(texto):
    hash_md5 = hashlib.md5()

    hash_md5.update(texto.encode('utf-8'))
    return hash_md5.hexdigest()

hash_resultado = calcular_md5(texto)

print("O hash MD5 da string é: ", hash_resultado)