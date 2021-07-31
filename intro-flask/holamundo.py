from flask import Flask, request, url_for, redirect, abort, render_template

import mysql.connector


midb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dragon97",
    database="prueba"
)


cursor = midb.cursor(dictionary=True)


# va a tener el nombre de main, cuando se ejecute este archivo
app = Flask(__name__)


# decoradores
@app.route('/')  # ruta que le vamos a indicar en el explorador
def index():
    return 'Hola mundo'

# GET, POST,PUT ,PATCH, DELETE
@app.route('/post/<post_id>', methods=['GET', 'POST'])#podemos pasarle parametros
def diana(post_id):
    if request.method == 'GET':
        return 'El id post es: ' + post_id
    else:
        return 'Este es otro metodo y no GET'


#enviar datos de un formulario web a mi servidor de FLASK
@app.route('/formulario', methods=['POST','GET'])
def formulario():
    cursor.execute('select * from Usuario')

    usuarios = cursor.fetchall()
    print(usuarios)
    # abort(403)
    #nota: cuando use redirect poner siempre el return
    # return redirect(url_for('diana', post_id=2)) 
    # print(request.form)
    # print(request.form['llave1'])
    # print(request.form['llave2'])
    #return render_template('template.html') #renderiza un archivo html

    #retornar un objeto JSON
    # return {
    #     "username": 'Marleny Rivera',
    #     "email": "Diana@correo.com"
    # }

    return render_template('template.html', usuarios=usuarios)


@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', mensaje='Hola Mundo')





@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == "POST":

        #obtengo los atibutos del formulario
        username = request.form['username']
        email = request.form['email']
        edad = request.form['edad']

        sql = 'insert into Usuario (username, email, edad) values (%s, %s, %s)'
        values = (username, email, edad)
        cursor.execute(sql, values)
        midb.commit()
        
        return redirect(url_for('formulario'))
    return render_template('crear.html', )