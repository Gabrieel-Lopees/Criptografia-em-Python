import random

def gerar_chave(tamanho):
    return ' '.join(chr(random.randint(32, 126)) for _ in range(tamanho))

def cifra_xor(texto, chave):
    return ' '.join(chr(ord(t) ^ ord(k)) for t, k in zip(texto, chave))

texto_plano = input("Digite o texto plano: ")

chave = gerar_chave(len(texto_plano))

texto_cifrado = cifra_xor(texto_plano, chave)

print(f"\nTexto Plano: {texto_plano}")
print(f"Chave Gerada: {chave}")
print(f"Texto Cifrado: {texto_cifrado}")