def miFuncion():
    print('Mi primera función!')

#miFuncion()

def imprimeDatos(*nombre):
    print('El nombre completo es: ', nombre[1])


imprimeDatos('Diana', 'Gonzales', '25', 'julio 23')


def nombreCompleto(apellido, nombre):
    print(nombre, apellido)

nombreCompleto(nombre='Diana', apellido='Gonzales')



def nombreCompleto2(**kwargs):
    print(kwargs['nombre'], kwargs['apellido'])

nombreCompleto2(nombre='Diana', apellido='Gonzales')


def miFuncion2(argumento = 'kike'):
    print(argumento)

miFuncion2('Batman')
miFuncion2()



def miFuncionLista(lista):
    for el in lista:
        print(el)


miFuncionLista(['chanchito', 'feliz'])


def concatenaNombres(lista):
    i = ''
    for el in lista:
        i = i + el + ' '
    return i

nombres = concatenaNombres(['shelsea', 'omar'])
print(nombres)


def recursion(i):
    if(i < 1):
        return i
    print(i)
    recursion(i - 1)

recursion(6)
