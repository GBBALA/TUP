# Ejercicio 3: Isertar elemtos y ordenarlos
# Pedir números y meterlos en una lista, cuando el usuario
# introduzca un número 0, nuestro progama dejaría de insertar
# por ultimo, mostrar los números ordenados de manor a mayor

lista = []
salir = False

while not salir:
    numero = int(input("Digite un número: "))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)

lista.sort()  # La lista esta ordenada con esta función
print(f"\nLista ordenada: \n{lista}")