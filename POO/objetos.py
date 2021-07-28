# Clases
class Usuario:
    def  __init__(self, nombre, apellido): #se ejecuta cuando creamos una instancia de la clase. #self hace una referencia a una instancia que creo 
        #propiedades
        self.nombre = nombre
        self.apellido = apellido

# Metodos
    def saludo(self):
        print('Hola, mi nombre es', self.nombre, self.apellido)



# Herencia
class Admin(Usuario):
    def superSaludo(self):
        print('Hola, me llamo, ', self.nombre, 'y soy administrador')



#instancia
usuario = Usuario('Diana', 'Rivera')

# hacedo a los metodos
usuario.saludo()
usuario.nombre = 'Enrique'
usuario.saludo()
# del usuario.nombre
# #usuario.saludo()
# del usuario

admin = Admin('Shelsea', 'Administrador')
admin.saludo()
admin.superSaludo()


# Ejercicio de herencia
print('Ejercicio de Herencia')
class Animal: 
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print('Hola, soy un', self.tipo ,'y mi sonido es el', self.onomatopeya)


class Gato(Animal):
    tipo = 'gato'
    def __init__(self, nombre, onomatopeya):
        Animal.__init__(self, nombre, onomatopeya)#extiendo la clase padres
        print('Hola soy un gato extendido!')
    
class Perro(Animal):
    tipo = 'perro'
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya) # hace referencia a la clase padre, extendiendo el metodo init
        print('Instanciando un perro')

class Canario(Animal):
    tipo = 'canario'


gato = Gato('Luna', 'Maullido')
gato.saludo()


perro = Perro('Lazi', 'ladrido')
perro.saludo()

canario = Canario('Piolin', 'silvido')
canario.saludo()


