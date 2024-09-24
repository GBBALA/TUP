# Ejercicio 1: Iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3
# Ejemplo de ejecucion: 0,3,6,9
print('Rango de 0 a 10 con números divisibles entre 3')
for i in range(11):
    if i % 3 == 0:
        print(i)


# Ejercicio 2: Crear un rango de numeros de 2 a 6 a iprimelos
# Ejemplo de Ejecucion 2,3,4,5,6
print('Rango con valores de inicio = 2 y fin = 6')
rango = range(2, 7)
for i in rango:
    print (i)

# Ejercicio 3: Crear un rango de 3 a 10 pero con incrimento de 2 en 2, en lugar de 1 en 1
# Ejemplo de ejecución: 3,5,7,9
print('Rango con vbalores de inicio = 3, fin = 10, incremento 2' )
for i in range (3, 11, 2):
    print (i)

