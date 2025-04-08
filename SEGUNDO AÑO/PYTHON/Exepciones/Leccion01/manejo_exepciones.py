resultado = None

a = int(input('Digite el primer número: '))
b = int(input('Digite el segundo número: '))
resultado = a / b # modificamos
try:
    resultado = a/b # modificamos
except TypeError as e:
    print(f'TypeError - Ocurrio un error: {type(e)}')
except ZeroDivisionError as e:
    print(f'Ocurrio un error: {e}')
except Exception as e:
    print(f'Exeption - Ocurrio un error: {type(e)}')
else:
    print('No se arrojo ninguna exepción')


print(f'El resultado es: {resultado}')
print('seguimos...')