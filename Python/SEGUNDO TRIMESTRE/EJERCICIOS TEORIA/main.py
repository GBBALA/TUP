# lista = Ariel, Liliana, Natalia, Osvaldo

nombres = ['Naty','Osvaldo','Lily', 'Ariel']  
print (nombres)  
# dentro de una lista pueden haber distintos datos strings, logicos, numericos 
print (nombres[0])
print (nombres[1])
print (nombres[3])
print (nombres[-1])
print (nombres[-2])

print (nombres[0:2]) # solo muesta el indice 0, 1 pero no el indice 2 
# ir del inicio de la lista al indice (sin incluirlo)
print (nombres[ :3]) # indices a mostrar 0, 1, 2
# desde el indice indicado hasta el final  
print(nombres[1: ])
# Modificamos un valor
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)
# Iterar una lista
for nombre in nombres: # nombre es singular, la lista es prular
    print(nombres)
else:
    print('se han acabado los elementos de la lista')

# preguntamos cuantos elementos tiene
print(len(nombres)) # le pasamos como parametro la lista

# agregamos un elemento

nombres.append('Marcelo')
print(nombres)

# Inseratar un elemento en un indice especifico
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3, 'Debora')
print(nombres)

# Eliminamos un elemento 
nombres.remove('Alberto')
print(nombres)

# Eliminar el ultimo elemento
nombres.pop()
print(nombres)

# Eliminar un indice especifico
del nombres[2]
print(nombres)

# TUPLAS
cocina = ('cuchara', 'cuchillo', 'tenedor')
print (cocina [0])
# mostrar de manera inversa
print(cocina[-1])
# Acceder a un rango 
print(cocina[0:2])

# Ejemplo
verduras = ('Papa', )  # Una tupla necesita aunque sea de un elemento: la coma
# de lo contrario solo seria un tipo de str cadena

# Recorremos los elementos de la tupla
for cocinar in cocina: # Print esta usando \n para saltos de líneas
    print(cocinar, end= ' ') # Usamos end= para eliminar los saltos de linea

cocinaLista= list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print('\n', cocina)