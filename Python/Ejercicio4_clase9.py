calificacion_promedio = 0.0
calificacion_baja = 99999
suma = 0.0
calificacion = 0.0


for i in range(10):
    calificacion = float(input(f"{i + 1}. Digite una calificación: "))
    suma += calificacion

    if calificacion < calificacion_baja:
        calificacion_baja = calificacion

calificacion_promedio = suma / 10


print(f"La calificación promedio es: {calificacion_promedio}")
print(f"La calificación más baja es: {calificacion_baja}")
