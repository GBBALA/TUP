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

# del cocina # esto es para eliminar una tupla

#Tipo set 
planetas = {'Marte','Júpiter', 'Venus'}
print(len(planetas)) # Usamos la función len = length (largo)

#Revisar si un elemento existe dentro de set
print('Júpiter'in planetas)

# Agregar un elemento
planetas.add('Tierra') #add es una función 
print(planetas)

#Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove('Júpiter') # Esta funcion ante un mal ingreso u inexistencia dale elemento da error
print(planetas)
planetas.discard('tierra') # Esta función no nos presenta ningún error
print(planetas)

# Limpiar set o conjunto
planetas.clear()
print(planetas)

# Eliminar set o conjunto
#del planetas 
#print(planetas) # Al eliminar da un error

# 'Maradona':10 Un diccionario esta compuesto por dos elemtos
# UNA LLAVE Y UN VALOR
# dict(key,value)
diccionario = {
    'IDE':'Integrated Development Enviroment',
    'POO':'Progamación Orientada a Objetos',
    'SABD':'Sistema de Administración de Base de Datos'
}
# Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con llave(key)
print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificamos elementos 
diccionario['IDE'] = 'Entorno de Desarollo Integrado'
print(diccionario)

# Como recorrer los elementos
for termino in diccionario: # Recorremos mostrando solo las llaves
    print(termino)

# Necesitamos una función para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino) # Muestra solo las llaves

for valor in diccionario.values(): # Usamos una función para acceder al valor
    print(valor)
 # Compromabr la existencia de algun elemnto


print('IDE'in diccionario) #devuelve un booleano 

# Agregar un elemto
diccionario['PK'] = 'Primary key'
print(diccionario)


# Eliminar un elemento
diccionario.pop('SABD') 
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario # el diccionario se borro
# Concatenamos listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1+lista2
print(lista3)




lista3.extend([7, 8, 9]) # Función para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5)) # Función para ubicar el índice esta el valor ingresado
# print(lista3.index(0)) # Esto daria error por no ser el elemento parte de la lista

# Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1)) # Cuenta cuantos valores iguales hay dentrod e la lista

# Para poner al reves una lista
lista3.reverse()
print(lista3)

# para que una lista se multiplique repitiendo repitiendo sus elementos
lista3 = lista3 * 2
print(lista3)

# Métodos de ordenamiento en python es una función
lista3.sort() # Ordena los elementos ascendentemete 
print(lista3)
lista3.sort(reverse=True) # Ordena descendentemente
print(lista3)
# REPASO DE TUPOLAS
tupla = (4, 'Hola', 6, [1, 2, 78], 4, 'Hola')  # La lista se inserta dentro de la tupla


print(4 in tupla) # Acción booleana, su respuesta es de tipo booleana
# Lo que podemos usar dentro de las tuplas son: index, count, len
# En tuplas se puede convertir de tupla a lista
# Repaso de set o conjunto
# Definir un conjunto
conjunto1 = {'bye'}
conjunto2 = {7, 'Hola'}

print(conjunto2)
conjunto1.add('hola')
print(conjunto1)
print(3 not in conjunto1)  # Pregunta si el número 3 no está en conjunto1

# como hacer la Igualdad de  dos conjuntos
print(conjunto1 == conjunto2)  # Compara si ambos conjuntos son iguales

# Operaciones en conjuntos
# Unión de conjuntos (elementos presentes en cualquiera de los dos)
conjunto3 = conjunto1 | conjunto2  
print(conjunto3)

# Intersección de conjuntos (elementos en común)
conjunto3 = conjunto1 & conjunto2  
print(conjunto3)

# Diferencia de conjuntos (elementos en conjunto1 que no están en conjunto2)
conjunto3 = conjunto1 - conjunto2  
print(conjunto3)

# Diferencia inversa (elementos en conjunto2 que no están en conjunto1)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

# elementos que no comparten o son diferentes entre ambos
conjunto3 = conjunto1 ^ conjunto2  
print(conjunto3)
# Subconjunto y superconjunto
conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3))  # Si conjunto2 es subconjunto de conjunto3
print(conjunto1.issubset(conjunto3))  
print(conjunto3.issubset(conjunto1))  
print(conjunto3.issubset(conjunto2))  

# Disjuntos (sin elementos en común)
print(conjunto2.issubset(conjunto3))
print(conjunto3.issuperset(conjunto2))
print(conjunto3.issuperset(conjunto3))

# Como saber si ambos conjuntos son disconexos, esto es si comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2)) #No hay cosas en comun

# Convertir conjunto en inmutable (frozenset)
conjunto1 = frozenset(conjunto1)  
# frozenset hace que el conjunto sea inmutable, por lo que ya no se puede modificar.
# Repaso diccionarios
diccionarioNuevo = {'Azul': 'Blue', 'Rojo': 'Red', 'Verde': 'Green', 'Amarillo': 'Yellow'}
print(diccionarioNuevo)


# Eliminar un elemento del diccionario
diccionarioNuevo.pop('Azul')
print(diccionarioNuevo)

# Diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {
    'Ariel': {'Edad': 40, 'Altura': 1.83},
    'Osvaldo': [45, 1.85],
    'Natalia': [35, 1.67]
}
print(diccionario2)
# Selección Argentina
seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 Millones', 'Posición': 'Extremo Derecho'},
    11: {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 Millones', 'Posición': 'Extremo Derecho'},
    24: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 Millones', 'Posición': 'Media Punta'},
    19: {'Nombre': 'Nicolás Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 Millones', 'Posición': 'Defensa Central'},
    1: {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 Millones', 'Posición': 'Portero'}
}
print(seleccionArgentina)

# Mostrar jugadores con bucle
for llave, valor in seleccionArgentina.items():
    print(f'{llave}: {valor}')

# Agregar tarea de más jugadores
# seleccionArgentina[número] = {...} (agregar más jugadores según el mismo formato)

print(f'Tenemos cargados en el diccionario la cantidad de jugadores: {len(seleccionArgentina)}')

# Pilas usando listas
pila = [1, 2, 3]

# Agregar elementos a la pila (al final)
pila.extend([4, 5])
print(pila)

# Sacar elementos de la pila (del final)
elementoBorrado = pila.pop()  # Quita el último elemento
print(f'Sacamos el elemento {elementoBorrado}')
print(f'La pila ahora quedó así: {pila}')

# Colas usando listas (estructura FIFO: First In, First Out)
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

# Agregar elementos al final de la cola
cola.extend(['Natalia', 'Jose'])
print(cola)

# Atender clientes (sacar elementos del frente de la cola)
for _ in range(5):
    cliente_atendido = cola.pop(0)
    print(f'Atendido el cliente: {cliente_atendido}')
    print(cola)