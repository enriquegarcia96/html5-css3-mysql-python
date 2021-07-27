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

if primero == 'chanchito feliz':
    print('El valor ingresado no es un entero')
    exit()

segundo = input('Ingrese segundo numero: ')

try:
    segundo  = int(segundo)
except:
    segundo = 'chanchito feliz'

if segundo == 'chanchito feliz':
    print('El valor ingresado no es un entero')
    exit()

simbolo = input('ingrese operacion: ')

if simbolo == '+':
    print('suma: ',primero + segundo)
elif simbolo == '-':
    print('Resta: ',primero - segundo)
elif simbolo == '*':
    print('Multiplicacion: ', primero * segundo)
elif simbolo == '/':
    print('Division: ', primero / segundo)
else:
    print('El simbilo no es valido')


