edad = 80

if edad < 18:
    print('es menor de edad')
    print('estoy dentro aun del if')
elif edad >= 18 & edad < 65: 
    print('es un adulto')
else:
    print('es mayor de edad')

print('esto está fuera del if')

# meses = 3

# match(meses):
#     case 1:
#         print('enero')
#     case 2:
#         print('febrero')
#     case 3:
#         print('marzo')
#     case _:
#         print('mes desconocido') 

mes = 2
meses = {
    1: 'enero',
    2: 'febrero',
    3: 'marzo'
}
print(meses[mes])