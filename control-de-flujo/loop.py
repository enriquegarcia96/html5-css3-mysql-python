# i = 0

# while i < 5:
#     i += 1
#     if i == 3:
#         continue
#     print(i)


# for loop

usuarios = ['omar', 'shelsea', 'diana', 'kike']

for usuario in usuarios:
    print(usuario)


usuario = 'chanchito feliz'
for c in usuario:
    print(c)



usuarios = ['omar', 'shelsea', 'diana', 'kike']

for usuario in usuarios:
    if usuario == 'diana':
        break
    print(usuario)




usuarios = ['omar', 'shelsea', 'diana', 'kike']

for usuario in usuarios:
    if usuario == 'diana':
        continue
    print('usando continuo: ',usuario)


# inicia con el numero, hasta donde llegara y incrementa el numero
for x in range(3, 30, 5):
    print(x)
else:
    print('Hemos terminado!!')



usuarios2 = ['omar', 'shelsea', 'diana', 'kike']

edades = [23, 22, 25, 25]

for usuario in usuarios2:
    for edad in edades:
        print(usuario, edad)
