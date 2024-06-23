# Definir variables
calificacion_promedio = 0.0
calificacion_baja = 99999
suma = 0.0
calificacion = 0.0

# Procesar las 10 calificaciones
for i in range(10):
    calificacion = float(input(f"{i + 1}. Digite una calificación: "))
    # Suma interactiva de las calificaciones
    suma += calificacion
    # Calcular la menor calificación
    if calificacion < calificacion_baja:
        calificacion_baja = calificacion

# Calcular calificación promedio
calificacion_promedio = suma / 10

# Mostrar resultados
print(f"La calificación promedio es: {calificacion_promedio}")
print(f"La calificación más baja es: {calificacion_baja}")
