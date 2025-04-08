
class Persona2:

    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        print('Estamos utilizando el método get para nombre')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        print('Estamos utilizando el método set para nombre')
        self._nombre = nombre

    @property
    def apellido(self):
        print('Estamos utilizando el método get para apellido')
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        print('Estamos utilizando el método set para apellido')
        self._apellido = apellido

    @property
    def edad(self):
        print('Estamos utilizando el método get para edad')
        return self._edad

    @edad.setter
    def edad(self, edad):
        print('Estamos utilizando el método set para edad')
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

if __name__ == '__main__':


    persona1 = Persona2('Carlos', 'González', 40)
    print(persona1.nombre)
    print(persona1.apellido)
    print(persona1.edad)

    persona1.nombre = 'Carlos Eduardo'
    persona1.apellido = 'González'
    persona1.edad = 41
    print(persona1.mostrar_detalles())

    # Objeto número dos
    persona2 = Persona2('Lucía', 'Pérez', 29)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)

    persona2.nombre = 'Lucía María'
    persona2.apellido = 'Pérez'
    persona2.edad = 30
    print(persona2.mostrar_detalles())

    # Objeto número tres
    persona3 = Persona2('Miguel', 'Ramírez', 50)
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)

    persona3.nombre = 'Miguel Ángel'
    persona3.apellido = 'Ramírez'
    persona3.edad = 51
    print(persona3.mostrar_detalles())

    print(__name__)
  