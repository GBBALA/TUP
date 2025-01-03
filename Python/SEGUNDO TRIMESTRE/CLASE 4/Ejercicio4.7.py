# Ejercicio 2: Modificar los elementos de una lista
# Llenar una lista con los números del 1 al 10m luego modificar los
# elementos de la lista multoplicandolos por un valor ingresado por el usuario

lista = list(range(1, 11))
print('Lista Original')
for i in lista:
    print(i, end='-')

valor = int(input('\nDigite un valor a multiplicar: '))
# Multiplicamos todos los elementos de la lista
for indice, i in enumerate(lista):  # Función para modificar los índices de la lista
    lista[indice] *= valor  # El iterador solo recorre los índices, en esta línea se multiplica

print(f'Lista final con los elementos multiplicados por {valor}')
for i in lista:
    print(i, end='-')