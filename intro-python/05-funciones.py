def saludo():
    print("Hola, ¿cómo estás?")
    print('sigo en la función')
    return "Hola"
    print('codigo muerto')

# valor = saludo()


otraFuncion = saludo

otraFuncion = 'una cadena'

# print(saludo())
# print(otraFuncion)


def suma(a: int, b: int):
    '''
        Esta función es imperativo que reciba argumentos 
        de tipo int (entero)
    '''
    return a + b


def formulaCuadratica(a, b, c):
    '''
        Esta función recibe los coeficientes de una ecuación
        cuadrática y devuelve las dos soluciones posibles
    '''
    x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
    return x1, x2


result = suma(b=4, a=6)  # argumentos posicionales
# print(result)

# print(formulaCuadratica(c=1, b=-5, a=6))  # argumentos con nombre

def suma2(*argumentos:int):

    return sum(argumentos)

# suma2(7,5,'hola','mundo','soy','una','tupla')
# print('la suma2: ',suma2(7,5,5,6,9,5,3,2,1,2,3,4))

# keywords arguments    
def suma3(**kwargs) -> int :
    print(kwargs)

    return sum(kwargs.values())

diccionario = {'a': 1, 'b': 2, 'c': 3}

print(suma3(**diccionario))
print(suma3(test=1, test2=2, test3=3, test4=4, test5=5))