from modulo import saludo, mascotas
from camelcase import CamelCase

print(mascotas)
saludo('Enrique')


c = CamelCase()
s = 'esta oracion necesita CamelCase'
camelcased =  c.hump(s)
print(camelcased)