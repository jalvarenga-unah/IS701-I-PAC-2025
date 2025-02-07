# numpy
# para instalar: pip install numpy
import numpy as np

numpy_list = np.array([1, 2, 3, 4, 5], dtype=float)
list_zeros = np.zeros(10)
arange_list = np.arange(10, 15, 2)
linspace_list = np.linspace(1, 2, 5)

print(numpy_list)
print(numpy_list * 2)
print(list_zeros)
print(arange_list)
print(linspace_list)

lista_2d = np.array([(1.5, 2, 3), (4, 5, 6)], dtype=float)
print(lista_2d.shape)

lista_numeros = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

print(lista_numeros.reshape(-1,1)) # cambair la forma del array

# Slicing

print(lista_numeros[4:9])



