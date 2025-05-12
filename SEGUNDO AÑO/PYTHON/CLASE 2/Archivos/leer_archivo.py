archivo = open('\c:\\Users\User\Desktop\LB\UNI\GITHUB\SEGUNDO AÑO\PYTHON''prueba.txt','r', encoding='utf8') # las letras son: 'r' rad, 'a' append, 'w' write 'x'
#print(archivo.read())
#print(archivo.read(15))
#print(archivo.read(5))
#print(archivo.read(10)) #continuamos desde la linea anterior
print(archivo.readline())
print(archivo.readline())
# for linea in archivo:
    # Print(linea): iteramos todos los elemntos del archivo
    # print(archivo.readlines()): accedemos al archivo como si fuera una lista
print(archivo.readline()[5])


# Anexamos información, copiamos a otro archivo
archivo = open('copia.txt', 'r', encoding='utf8')
archivo2 = open('destino.txt', 'a', encoding='utf8')
archivo2.write(archivo.read())
archivo.close() # cerramos el primer archivo
archivo2.close() # cerramos el segundo archivo

print('Se ha terminado el proceso de leer y copiar archivos')