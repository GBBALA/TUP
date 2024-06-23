def contar_numeros():
    conteo_positivos = 0
    conteo_negativos = 0
    conteo_neutros = 0

    while True:
        num = int(input("Digite un número: "))
        if num > 0:
            conteo_positivos += 1
        elif num < 0:
            conteo_negativos += 1
        else:
            conteo_neutros += 1

        opcion = input("¿Desea ingresar otro número? (s/n): ")
        if opcion.lower() != "s":
            break

    print(f"La cantidad de números positivos es: {conteo_positivos}")
    print(f"La cantidad de números negativos es: {conteo_negativos}")
    print(f"La cantidad de números neutros es: {conteo_neutros}")

contar_numeros()

