num = int(input("Escreva um numero e dirá se é primo ou não: "))

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"O número {num} não é primo")
            break
    else:
        print(f"O número {num} é primo")
else:
    print(f"O número {num} não é primo")
