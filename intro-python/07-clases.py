

class Animal:

    # Constructor / # Propiedades
    def __init__(self, nombre: str, raza: str, edad: int):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    # comportamientos

    def comer(self):
        print(f"{self.nombre} está comiendo")
# Fin de la Clase


mascota = Animal(nombre="Firulais", raza="Pastor Aleman", edad=5)
mascota.nombre = 'Apolo'
print(mascota.nombre)
mascota.comer()


class Circulo:

    pi: float = 3.1416

    def __init__(self, radio: float):
        self.radio = radio

    def area(self):
        return self.pi * (self.radio ** 2)


circulo1 = Circulo(radio=5)

# input: metodo que permite ingresar datos por teclado,
# y lo que se ingrese es de tipo strings

valorRadio = None

while valorRadio == None:
    try:
        valorRadio = float(input('Ingrese el radio del circulo: '))
    except ValueError:
        print('El valor ingresado no es un número')

    
circulo1.radio = valorRadio

print(circulo1.area())

# otras instrucciones que no dependen de valorRadio
print('Puedo hacer otras cosas')