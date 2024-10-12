import math #Importamos la clase math para hacer usod e la función sqrt(Raiz cuadrada)
# Dada la siguiente tupla

tupla = (13, 1, 8, 3, 2, 5, 8) # definimos la tupla 
# Crear una lista que solo incluyta los números menores a 5 
# e imprima por consola [1, 3, 2]

lista = [] # definimos lista
# Filtramos los elemontos menores a 5 de la tupla
for elemento in tupla:
    if elemento <  5:
        lista.append(elemento)
print(lista)

#Ejercicio de matematicas
# Para sacar la raíz cuadrada de un número positivo

numero = int(input('Digite un numero positivo'))
while numero < 0:
    print('ERROR -> Deberia ser un número positivo')
    numero = int(input('Digite un número positivo'))
    print(f'\nSu raíz cuadrada es: {math.sqrt(numero):.2f}')

