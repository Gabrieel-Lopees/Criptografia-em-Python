import hashlib

target_hash  = 'ad9be0b5d43f9e2aba895f3ede723aa1'

def calcular_md5(texto):
    return hashlib.md5(texto.encode('utf-8')).hexdigest()
def ataque_forca_bruta(target_hash):
    for i in range(10000):
        pin = f"{i:04d}"

        hash_resultado = calcular_md5(pin)

        if hash_resultado == target_hash:
            return pin
    return None

pin_encontrado = ataque_forca_bruta(target_hash)

if pin_encontrado:
    print(f"O pint encontrado é: {pin_encontrado}")
else:
    print("O pin não foi encontrado.")