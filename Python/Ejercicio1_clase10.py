num = int(input("Digite un número: "))

if num >= 0:
    factorial = 1
    i = 1
    
    while i <= num:
        factorial *= i
        i += 1
    
    print(f"El factorial es: {factorial}")
else:
    print("El número debe ser mayor o igual a 0.")
