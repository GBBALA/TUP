# Ejercicio 8: Menú interactivo - Cajero automatico
# Hacer un progama que simule un cajero automatico con un saldo
# inicial de 1000$ y tendra el siguiente menú de opciones
#  1. Ingresar dinero de la cuenta
#  2. Retirar dinero de la cuenta
#  3. Mostrar dinero disponible
#  4. Salir 
saldo = 1000

while True:
    print("\t.:MENÚ:.")
    print("1. Ingresar dinero en la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero disponible")
    print("4. Salir")

    opcion = int(input("Digite una opción de menú: "))
    print()

    if opcion == 1:
        extra = float(input("Cuanto dinero desea ingresar -> "))
        saldo += extra
        print(f"Dinero en la cuenta al momento: {saldo}")
    elif opcion == 2:
        retirar = float(input("Cuanto dinero desea retirar -> "))
        if retirar > saldo:
            print("No tiene esa cantidad de dinero")
        else:
            saldo -= retirar
            print(f"Dinero en la cuenta al momento: {saldo}")
    elif opcion == 3:
        print(f"Dinero en la cuenta al momento: {saldo}")
    elif opcion == 4:
        print("Gracias por utilizar su cajero automático, hasta pronto")
        break
    else:
        print("Error, se equivocó de opción de menú")