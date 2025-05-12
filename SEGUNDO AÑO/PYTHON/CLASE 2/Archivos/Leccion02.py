# Declaramos una variable
try:
    archivo = open("prueba.txt", "w", encoding = 'utf8') # La w es de write que significa escribir
    archivo.write('Progamamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Los acentos son importantes para las palabras\n')
    archivo.write('como por ejemplo: acción, ejecución y producción\n')
    archivo.write('las letras son:\n"r" read leer, \n"a" append anexa, \n"w" write escribe, \n"x" crea un archivo ')
    archivo.write('\nt esta es para texto o text, \nb archivos binarios, \nw+ lee y escribe, r+\n ')
    archivo.write('con esto terminamos')
   
except Exception as e:
    print(e)
finally: # Siempre se ejecuta
    archivo.close() # Con esto se debe de cerrar el archivo

# archivo.write('todo quedo perfe'):  este es un error