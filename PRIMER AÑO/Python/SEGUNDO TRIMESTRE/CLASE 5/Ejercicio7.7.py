# Ejercicio 5: Convertidor de temperaturas
# Realizar dos funciones para convertir de grados celcius
# a fharenheit y visiversa 
#Investigar las formulas

# Función que convierte de celsius a fahrenheit
def celsius_fahrenheit(celsius):
    return celsius * 9/5 + 32  # La presedencia: multiplicación, división y suma

# Función que convierte de fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9  # Respetar la presedencia utilizando paréntesis

celsius = float(input("Digite el valor de celsius: "))
resultado = celsius_fahrenheit(celsius)
print(f"{celsius} C -> {resultado:.2f} F")

fahrenheit = float(input("Digite el valor de fahrenheit: "))
resultado = fahrenheit_celsius(fahrenheit)
print(f"{fahrenheit} F -> {resultado:.2f} C")