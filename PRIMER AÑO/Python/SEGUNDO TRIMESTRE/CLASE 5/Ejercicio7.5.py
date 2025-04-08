#  Ejercicio 3: Función Recursica
# Imprimir números de 5 a 1 de manera descendentealquier valor positivo, por ejempolo, si pasamos el 
# valor 5 debe imprimir:
# 5
# 4
# 3
# 2
# 1 
# En caso de ser el núymero 3 debe imprimir:
# 3
# 2
# 1
# Si se ingresan números negativos no imprime nada

def imprimir_numeros_recursivos(numero):
    if numero >= 1:  # Caso Base
        print(numero)
        imprimir_numeros_recursivos(numero-1)  # Caso recursivo
    elif numero == 0:
        return
    elif numero < 0:
        print("Valor ingresado incorrecto...")

# Pedimos al usuario que ingrese el número
numero_ingresado = int(input("Ingrese un número: "))

# Llamamos a la función con el número ingresado
imprimir_numeros_recursivos(numero_ingresado)