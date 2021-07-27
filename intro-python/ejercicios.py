# dato = input('ingrese dato: ')

# lista = ['hola', 'omar', 'shelsea', 'diana', 'kike']
 
# if lista.count(dato) > 0:
#     print('El dato existe: ', dato)
# else:
#     print('El dato no existe :(', dato)


# CALCULADORA


primero = input('Ingrese primer numero: ')

try:
    primero  = int(primero)
except:
    primero = 'chanchito feliz'


segundo = input('Ingrese segundo numero: ')

try:
    segundo  = int(segundo)
except:
    segundo = 'chanchito feliz'


if primero == 'chanchito feliz' or segundo == 'chanchito feliz':
    print('ingresaste mal un dato, prueba de nuevo solo con numeros')
else:
    print(primero + segundo)


