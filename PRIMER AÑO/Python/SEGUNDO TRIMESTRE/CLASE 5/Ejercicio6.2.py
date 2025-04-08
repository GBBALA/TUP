# Ejercicio 11: Agenda telefonica
# Hacer un progama que simule una agenda de contactos. Crear un
#diccionario donde la clave sea el nombre del usuario y el valor
# sea el telefono, el progama tendrá el siguiente menpu de opciones:
#   1. Nuevo contacto
#   2. Borrar contacto
#   3. Ver contactos existentes
#   4. Salir

agenda = {}

while True:
    print('\t.:MENU:.')
    print('1. Nuevo contacto')
    print('2. Borrar contacto')
    print('3. Ver contactos existentes')
    print('4. Salir')

    opcion = int(input('Digite una opción de menú: '))

    if opcion == 1:
        nombre = input('Digite el nombre del contacto: ')
        telefono = input('Digite el número de teléfono: ')

        if nombre not in agenda:
            agenda[nombre] = telefono
            print('Contacto agregado exitosamente!')
        else:
            print('Este nombre de contacto ya existe')

    elif opcion == 2:
        nombre = input('Cuál es el nombre del contacto a eliminar: ')
        if nombre in agenda:
            del agenda[nombre]
            print('Se ha eliminado el contacto requerido')
        else:
            print('Este contacto no existe en la agenda')

    elif opcion == 3:
        print('Agenda de contactos:')
        for nombre, telefono in agenda.items():
            print(f"Nombre: {nombre}, Teléfono: {telefono}")

    elif opcion == 4:
        print('Gracias por utilizar su agenda de contactos')
        break