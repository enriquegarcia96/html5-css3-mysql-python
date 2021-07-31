# libreria para conectarnos con la base de mysql
import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='amor de mi infancia',
    database='prueba'
)


# es un objeto que nos permite interractuar con la base de datos
cursor = midb.cursor()

# # ->listar datos
cursor.execute('select * from Usuario')
resultado = cursor.fetchall()  # devuelve todos los datos de la  base de datos
print(resultado)

#para limitar las consultas
# cursor.execute('select * from Usuario limit 1')
# resultado = cursor.fetchall()  # devuelve todos los datos de la  base de datos
# print(resultado)


# ver definiciones de tablas
#cursor.execute('show create table Usuario')


# insertar datos
# sql = 'insert into Usuario (email, userName, edad) values (%s, %s, %s)'
# values = ('micorreo@corre.com', 'shelsea', 23)


# ->valores a ingresar a la base de datos
# Actualizar datos
sql = 'update Usuario set email = %s where id = %s'
values = ('shelsea@correo.com', 5)
cursor.execute(sql, values)

# ->tomara los datos y ejecutara la consulta de sql directamente con la base de datos
midb.commit()

print(cursor.rowcount)




#eliminar datos
# sql = 'delete from Usuario where id = %s'
# values = (4,)
# cursor.execute(sql, values)

# midb.commit()