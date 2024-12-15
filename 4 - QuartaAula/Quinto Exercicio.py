import itertools
import string
import time
import getpass


PIN_AlVO = getpass.getpass("Digite sua senha(4 PINS): ")
print("Carregando...")

caracteres = string.ascii_letters + string.digits

inicio = time.time()

for tentativa in itertools.product(caracteres, repeat=4):
    pin_tentativa = ' '.join(tentativa)
    if pin_tentativa == PIN_AlVO:
        print(f"pin encontrado: {pin_tentativa}")
        break

fim = time.time()
tempo_total = fim - inicio
print(f"tempo total: {tempo_total: .4f} segundos")