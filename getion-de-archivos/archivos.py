c = open('chanchito.txt', 'w') # nos permite abrir el archivo

# print(c.read()) # lee la totalidad del archivo
# print(c.readline())


# lee cada linea del archivo de manera independiente
# for x in c:
#     print(x)

c.write('\nagregaremos una nueva linea a nuestro archivo')#escribe un nueva linea

c.close() # cierra el archivo

x = open('chanchito.txt')
print(x.read())


# import os 

# if os.path.exists('chanchito.txt'):
#     os.remove('chanchito.txt')
# else:
#     print('El archivo no existe')


# #eliminar una carpeta
# os.rmdir('micarpeta') 







