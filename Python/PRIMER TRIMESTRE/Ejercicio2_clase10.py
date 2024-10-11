n_elementos = int(input("Digite la cantidad de elementos a ingresar: "))
suma_pares = 0
conteo_pares = 0
suma_impares = 0
conteo_impares = 0

numeros = []

for i in range(n_elementos):
    num = int(input("Digite un número: "))
    numeros.append(num)

for numero in numeros:
    if numero % 2 == 0:
        suma_pares += numero
        conteo_pares += 1
    else:
        suma_impares += numero
        conteo_impares += 1

if conteo_pares == 0:
    print("No se han digitado números pares")
else:
    promedio_pares = suma_pares / conteo_pares
    print("La suma de los números pares es:", suma_pares)
    print("El conteo de los números pares es:", conteo_pares)
    print("El promedio de los números pares es:", promedio_pares)

if conteo_impares == 0:
    print("No se han digitado números impares")
else:
    promedio_impares = suma_impares / conteo_impares
    print("La suma de los números impares es:", suma_impares)
    print("El conteo de los números impares es:", conteo_impares)
    print("El promedio de los números impares es:", promedio_impares)