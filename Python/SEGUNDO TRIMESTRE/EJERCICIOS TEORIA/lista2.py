# lista = Ariel, Liliana, Natalia, Osvaldo

nombres = ['Naty','Osvaldo','Lily', 'Ariel']  
print (nombres)
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

# eliminar todos los elementos

nombres.clear
print(nombres)

# elminar la lista
del nombres
print(nombres)