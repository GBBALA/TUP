# Ejercicio 01: Crear una función para sumar los valores recibidos de tipi
# númericos, utilizando argumentos variables *args como parametro de la 
# Función y agregar como resultadod la suma de todos los valores pasados
# como argumentos.


def sumar_valores(*args):
 
  suma = 0
  for valor in args:
    suma += valor
  return suma

