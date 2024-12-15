#Exercicio 1

'''print("Olá Mundo")'''

#Exercicio 2

'''x = int(input ("Variavel X:"))
y = int(input ("Variavel Y: "))

if x > y:
    print("X é maior que Y!")
elif y == x: 
    print("São iguais!")
    
else:
    print("Y é maior que X!")'''
    
#Exercicio 3
    
'''x = int(input ("Variavel X:"))
y = int(input ("Variavel Y: "))
z = int(input ("Variavel Z: "))

#verificar se é Z
if x > z and y > z:
    print("Z é a menor")
#verificar se é X
elif z > x and y > x: 
    print("X é a menor")
#verificar se é Y
else:
    print("Y é a menor")'''
    
#Exercicio 4

'''i = int(input ("Escreva sua variavel: "))

while i < 1000:
    print(i)
    i += 1'''
    
#Exercicio 5

'''num = int(input ("Escreva uma variavel: "))

for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")'''
    
#Exercicio 6

'''num = int(input ("Escreva uma numero e dirá se é par ou n: "))

if num % 2 == 0:
    print("Seu numero {num} é par")
    
else:
    print("Seu numero {num} é impar")'''

#Exercicio 7

num = int(input ("Escreva uma numero e dirá se é primo ou n: "))

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"O numero {num} não é primo")
            break
        else:
            print(f"o numero {num} é primo")
    
else:
        print(f"o numero {num} não é primo")
            
