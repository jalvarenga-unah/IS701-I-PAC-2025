original = [1, 2, 3, 4, 5]

# copia = original  # no es una copia, es una referencia
copia = original.copy()

original.remove(4)

print('original', original)
print('copia', copia)

# Diccionarios: objetos de tipo clave:valor
# mascota = {
#     'nombre':'Apolo',
#     'edad': 3,
# }
mascota = dict(nombre='Apolo', edad=3)

# mascota.pop('edad') # Elimina la clave 'edad'
print(mascota)

mascota['raza']  = 'Terrier'
print(mascota)

print(mascota.keys())
print(mascota.items())

print(mascota['nombre'])
print(mascota['raza'])
print(mascota.get('edad'))
