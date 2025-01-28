rango = range(5, 10, 2)
cadena = "Hola mundo"
lista = [1, 2, 3, 4, 5]
diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Bogotá"}

for value in diccionario:
    print(diccionario[value])

for clave, value in diccionario.items():
    print(f' "{clave}" => "{value}"')

while True:
    print("Hola")
    print("Mundo")
    break