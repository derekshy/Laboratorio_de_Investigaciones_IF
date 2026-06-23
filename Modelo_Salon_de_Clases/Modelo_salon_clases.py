# version 0
import random
import numpy as np
import math
h = 0.00000000001

matriz_k = np.array([[0, 32, 0, 0, 0, 0, 35, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [14, 0, 12, 0, 0, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 13, 0, 5, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 23, 0, 12, 0, 0, 0, 0, 34, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 9, 0, 26, 0, 0, 0, 0, 0, 0, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 16, 0, 0, 0, 0, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [23, 0, 0, 0, 0, 0, 0, 28, 0, 0, 0, 0, 34, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 34, 0, 0, 0, 0, 29, 0, 36, 0, 0, 0, 0, 86, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 10, 0, 0, 0, 0, 16, 0, 27, 0, 0, 0, 0, 55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 11, 0, 0, 0, 0, 23, 0, 32, 0, 0, 0, 0, 58, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 13, 0, 0, 0, 0, 34, 0, 23, 0, 0, 0, 0, 41, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 20, 0, 0, 0, 0, 39, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 23, 0, 0, 0, 0, 0, 0, 45, 0, 0, 0, 0, 42, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 35, 0, 0, 0, 0, 39, 0, 38, 0, 0, 0, 0, 58, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 70, 0, 0, 0, 0, 60, 0, 10, 0, 0, 0, 0, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 60, 0, 0, 0, 0, 10, 0, 60, 0, 0, 0, 0, 60, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 12, 0, 49, 0, 0, 0, 0, 57, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 58, 0, 0, 0, 27, 0, 0, 0, 0, 0, 0, 0, 43, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 0, 0, 0, 0, 0, 0, 46, 0, 0, 0, 0, 57, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 56, 0, 30, 0, 0, 0, 0, 60, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 0, 0, 0, 24, 0, 43, 0, 0, 0, 0, 60, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 46, 0, 44, 0, 0, 0, 0, 58, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 0, 0, 0, 0, 10, 0, 30, 0, 0, 0, 0, 60, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26, 0, 0, 0, 0, 19, 0, 0, 0, 0, 0, 0, 60], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 52, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 0, 0, 0, 0, 46, 0, 39, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 48, 0, 52, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 0, 0, 0, 0, 53, 0, 9, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 0, 0, 0, 3, 0, 30], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 0, 0, 0, 0, 42, 0]])
comportamiento_previo_x = [random.uniform(-1, 1) for x in range(30)]

columnas = 6
filas = 5
dimension_array = filas * columnas

def sigmoid(x):
    return (2/ (1 + math.exp(-x)))-1

esquinas = np.array([0,columnas-1,dimension_array-columnas,dimension_array-1])
aristas_superiores = np.arange(1,columnas-1)
aristas_laterales_izquierda = np.arange(columnas, dimension_array-columnas,columnas)
aristas_laterales_derecha = np.arange((2*columnas)-1, dimension_array-columnas+1, columnas)
aristas_inferiores = np.arange(dimension_array-columnas+1, dimension_array-1)
hashmap_index_conections = {0:[[1,6], [32,35]], 5:[[4,11], [16,20]], 24:[[18,25], [7,54]], 29:[[28,23], [23,42]]}

for i in range(len(comportamiento_previo_x)):  
    if i in esquinas:
        continue
    else:
        if i in aristas_superiores:
            hashmap_index_conections[i] = [[i-1, i+1, i+6], [matriz_k[i][i-1], matriz_k[i][i+1], matriz_k[i][i+6]]]
        elif i in aristas_laterales_izquierda:
            hashmap_index_conections[i] = [[i-6, i+6, i+1], [matriz_k[i][i-6], matriz_k[i][i+6], matriz_k[i][i+1]]]
        elif i in aristas_laterales_derecha:
            hashmap_index_conections[i] = [[i-6, i+6, i-1], [matriz_k[i][i-6], matriz_k[i][i+6], matriz_k[i][i-1]]]
        elif i in aristas_inferiores:
            hashmap_index_conections[i] = [[i-1, i+1, i-6], [matriz_k[i][i-1], matriz_k[i][i+1], matriz_k[i][i-6]]]
        else:
            hashmap_index_conections[i] = [[i-6, i+1, i+6, i-1], [matriz_k[i][i-6], matriz_k[i][i+1],matriz_k[i][i+6], matriz_k[i][i-1]]]


print(comportamiento_previo_x)
resultado_x = comportamiento_previo_x.copy()
for i in range(5):
    for i in range(len(comportamiento_previo_x)):
        suma = 0
        for j in range(len(hashmap_index_conections[i][0])):
            suma += hashmap_index_conections[i][1][j] * (comportamiento_previo_x[i]-hashmap_index_conections[i][0][j])**3
        resultado_x[i] = sigmoid(comportamiento_previo_x[i] - suma * h)
    comportamiento_previo_x = resultado_x
    print(comportamiento_previo_x)