valores = []

while True:
    numero = int(input("Digite um numero (999 para interromper): )"))
    if numero == 999:
        break
    
    valores.append(numero)

valores.sort()
print("Valores em ordem : ", valores)