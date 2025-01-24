# Python es un lenguahe Identado

# Variables
nombre: str = 'Juan'  # String
edad: int = 30  # numero entero
altura: float = 1.60  # numero decimal
esMayor = edad > 18  # boolean
# esMayor = False

print(nombre)
# se puede cambiar el valor y el tipo de la variable
# nombre = 60

# print('Hola, me llamo ' + nombre + ' y tengo ' + str(edad) + ' años')
print(f'Hola, me llamo {nombre} y tengo {edad} años')

print('tamaño', len(nombre))

# print("Hola, este es mi primer programa en Python")
# print("Hola mundo en pyhton")

# Listas
postres = ['torta', 'helado', 'galletas']
postres.append('flan')
postres.insert(2, 'chocolate')
# postres.pop() # Elimina el ultimo elemento
# postres.pop(2) # Elimina el elemento en la posicion 2
# postres.clear() # Elimina todos los elementos
postres.remove('galletas')  # Elimina el primer elemento que coincida con el valor

hayGalletas = 'galletas' in postres
print(hayGalletas)
print(postres)
print('j' in 'Juan')

# Tuplas
geo = (1.23, 4.56)  # No se pueden modificar
lat = geo[0]
print(geo[0])

rango = range(0, 10, 3) # 0, 3, 6, 9
print(rango)
