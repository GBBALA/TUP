class Persona: #Creamos una clase

   def __init__(self,nombre,apellido,edad):      #Definimos el método (Éste se llama Dunder init)  Variables por parámetros
       self.nombre = nombre     #Atributos y Variables
       self.apellido = apellido
       self.edad = edad
       #Atributos de instancia dentro de un método

   def mostrar_detalle(self):
       print(f'Persona:')


persona1 = Persona('Javier','Quiroga',21)  #Instancia de objeto #Necesitamos enviar argumentos

#print(persona1.nombre)
#print(persona1.apellido)
#print(persona1.edad)

#Lo mostramos en una sola línea con INTERPOLACIÓN
print(f'El objeto UNO de la clase Persona: {persona1.nombre} {persona1.apellido}, su edad es: {persona1.edad}')


persona2 = Persona('Ariel','Betancud',40) #Instancia de objeto número dos

#Lo mostramos en una sola línea con INTERPOLACIÓN
print(f'El objeto DOS de la clase Persona: {persona2.nombre} {persona2.apellido}, su edad es: {persona2.edad}')

#Modificación de atributos del objeto UNO

persona1.nombre = 'Javier'
persona1.apellido = 'Diaz'
persona1.edad = 27

print(f'El objeto UNO MODIFICADO de la clase Persona: {persona1.nombre} {persona1.apellido}, su edad es: {persona1.edad}')

# Los atributos son características
# Los métodos son el comportamiento que van a tener los objetos (acciones)

# print(persona2.telefono) el objeto no tiene este atributo,da error
persona3 = Persona("Rogelio", "Romero", 35789546,22, "Teléfono", "2614445557","Calle Lopez", 823, "Manzana", 77, "Casa", 18, Altura=1.83, Peso=105, CFavorito="Azul", Auto="Citroen", Modelo=2021)
persona3.mostrar_detalle()
# print(persona3._dni) esto no se debe utilizar(esta encapsulado), esto dice que deconocemos python.
# persona3.__nombre # Esta totalmente encapsulado

