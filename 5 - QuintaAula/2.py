# A)

import hashlib

texto = input("Digite seu texto: ")
def calcular_md5(texto):
    hash_md5 = hashlib.md5()

    hash_md5.update(texto.encode('utf-8'))
    return hash_md5.hexdigest()

hash_resultado = calcular_md5(texto)

print("O hash MD5 da string é: ", hash_resultado)

# B)

import hashlib

texto = input("Digite seu texto: ")
def calcular_sha256(texto):
    hash_256 = hashlib.sha256()

    hash_256.update(texto.encode('utf-8'))
    return hash_256.hexdigest()

hash_resultado = calcular_sha256(texto)

print("O hash SHA 256 da string é: ", hash_resultado)