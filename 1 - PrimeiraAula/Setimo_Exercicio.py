num = int(input ("Escreva uma numero e dirá se é primo ou n: "))

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"O numero {num} não é primo")
            break
        else:
            print(f"o numero {num} é primo")
            break
    
else:
        print(f"o numero {num} não é primo")