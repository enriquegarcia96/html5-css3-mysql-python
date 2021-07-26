# acá va a un comentario
if 3 > 5:  # acá va a un comentario
    print('Esto no se va a imprimir')

# if 5 > 3: # acá va a otro comentario
#     print('5 es mayor a 3')

x = 5
y = 'chanchito feliz'

# print(x, y)

email = 'enrique@gmail.com'

print(email)

mi_var = 'chanchito'
MIVAR = 'chanchito'
a, b, c = 'kike', 'diana', 'marleny'

# print(a,b, c)

valor1 = valor2 = valor3 = 'chanchito feliz'
print(valor1, valor2, valor3)

# concatenacion
inicio = 'Hola '
final = 'mundo'

# print(inicio + final)


# tipos de datos
palabra = 'hola mundo'  # string
oracion = "hola mundo comilla doble"

entero = 20  # integer
conDecimales = 20.2  # float
complejo = 1j

# print(palabra, oracion, entero ,conDecimales, complejo)

lista = ['Hola', 'Mundo', 'Diana']
lista2 = lista.copy()  # copea la lista
lista.append('Shelsea')  # agrega nuevos elementos a la lista
# lista.clear() # elimina todos los elementos de la lista


print(lista, lista2.count(3))
# cuenta los elementos que se encuentra dentro de la lista
print(len(lista), len(lista2))


largoLista = len(lista)
largoLista2 = len(lista2)

print("de otra manera", largoLista, largoLista2)


print(lista[2])  # para aceder a los indices a una lista


# eliminar elementos de una lista
# lista.pop() #este elimina el ultimo elemento de las lista
# lista.remove('Hola') # Este elimina un elemento por su valor

lista.reverse()
lista.sort()
tupla = ('hola', 'Omar', 'somos', 'Tupla')
listaDeTupla = list(tupla)  # transforma la tupla en una lista
listaDeTupla.append('García')
print(listaDeTupla)
# print(tupla.index('somos')) # devuelve el indice en donde se encuentra

rango = range(6)
print(rango)


# Diccionario
diccionario = {
    "nombre": "chanchito feliz",
    "raza": "persa",
    "edad": 5
}

# print(diccionario)
# print(diccionario['nombre'])
# print(diccionario['raza'])
# print(diccionario.get('nombre'))
diccionario['nombre'] = 'Fluffy'  # para cambiar la propiedad
print(len(diccionario))


diccionario['ronronea'] = 'Si'
print(diccionario)
# diccionario.pop('ronronea') ## elimina la llave
# diccionario.popitem() #elimina la ultima llave
# copiaGatito = diccionario.copy()
copiaGatito = dict(diccionario)  # hace una copia del diccionario
# del diccionario['ronronea']
diccionario.clear()  # elimina todas las propiedades
print(diccionario, copiaGatito)

print("diccionaio dentro de otros diccionario")


fluffy = {
    "Fluffy": {
        "nombre": "Fluffy",
        "edad": 4
    },
}

mamba = {
    "nombre": "Black Manba",
    "edad": 12
}
gatitos = {
    "Fluffy": fluffy,
    "Mamba": mamba
}


print(gatitos)

perritos = dict(nombre="chanchito feliz", edad=6)
print(perritos)


# Booleanos
verdarero = True
falso = False

print(verdarero, falso)
