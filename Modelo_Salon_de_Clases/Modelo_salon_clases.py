"""
Tittle:
Modelo de un salon de clases m * n cualquiera, 
El comportamiento individual de cada individuo se guarda en comportamiento_previo_x,
En la matriz_k, se encuentran las influencias/conecciones que tiene x individuo con los restantes,
    por ejemplo, en el primer elemento de esa matriz, se encuentra una lista de 30 elementosde las interacciones con los demas
    aunque tammbien se encuentra la interaccion consigo mismo aunque sea 0,
Cada "paso siguiente" esta dado por h
El promedio de todos los comportamientos esta dado por parametro_de_orden
"""

import numpy as np
import math

columnas = 6
filas = 5
dimension_array = filas * columnas

h = 0.00001
rng = np.random.default_rng(seed=1)

comportamiento_previo_x = rng.uniform(-1, 1, size=30)
parametro_de_orden = np.sum(comportamiento_previo_x) / dimension_array

matriz_k = np.array([
    [0, 32, 23, 30, 26, 43, 35, 35, 29, 46, 32, 45, 52, 10, 27, 34, 45, 51, 18, 29, 36, 38, 40, 56, 42, 19, 25, 37, 43, 50],
    [14, 0, 12, 16, 26, 38, 46, 16, 51, 18, 28, 35, 48, 51, 19, 20, 30, 43, 53, 16, 32, 23, 37, 41, 53, 60, 17, 25, 58, 39],
    [14, 13, 0, 5, 7, 14, 58, 43, 15, 39, 40, 36, 47, 27, 42, 42, 53, 16, 27, 38, 49, 5, 11, 22, 33, 44, 55, 16, 27, 38],
    [2, 49, 23, 0, 12, 50, 10, 21, 32, 34, 43, 54, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 44, 43, 34, 42, 41, 12, 34, 45],
    [23, 52, 16, 9, 0, 26, 16, 46, 46, 45, 11, 51, 4, 46, 43, 43, 51, 58, 28, 7, 39, 56, 18, 18, 37, 57, 46, 37, 37, 24],
    [19, 46, 48, 52, 16, 0, 24, 38, 13, 38, 39, 20, 49, 37, 24, 14, 25, 36, 47, 58, 52, 41, 17, 28, 39, 50, 30, 10, 20, 40],
    [23, 39, 19, 29, 37, 49, 0, 28, 59, 31, 21, 13, 34, 32, 49, 46, 16, 43, 60, 40, 59, 48, 47, 18, 43, 28, 57, 47, 18, 20],
    [36, 34, 16, 57, 16, 16, 29, 0, 36, 29, 38, 34, 29, 6, 20, 38, 9, 91, 10, 56, 42, 37, 28, 25, 35, 49, 38, 47, 31, 26],
    [25, 25, 10, 51, 42, 42, 27, 16, 0, 27, 18, 17, 16, 15, 55, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 59],
    [58, 57, 12, 11, 32, 25, 16, 43, 23, 0, 32, 26, 6, 20, 56, 58, 31, 32, 25, 51, 15, 24, 42, 43, 41, 31, 13, 8, 2, 1],
    [4, 12, 15, 19, 13, 22, 27, 31, 33, 34, 0, 23, 38, 41, 45, 49, 41, 52, 56, 6, 2, 7, 9, 14, 26, 23, 28, 35, 37, 44],
    [48, 50, 53, 55, 58, 25, 5, 8, 12, 14, 39, 0, 19, 23, 27, 31, 36, 12, 40, 42, 45, 49, 52, 57, 2, 9, 11, 18, 22, 26],
    [36, 35, 39, 44, 47, 51, 23, 54, 56, 59, 3, 7, 0, 45, 12, 16, 16, 16, 42, 21, 25, 29, 34, 38, 41, 45, 48, 52, 56, 58],
    [1, 6, 11, 15, 20, 24, 30, 35, 33, 39, 43, 47, 39, 0, 38, 47, 50, 53, 55, 58, 59, 2, 6, 9, 13, 17, 22, 26, 31, 35],
    [60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 0, 10, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60],
    [60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 10, 0, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60],
    [2, 6, 9, 13, 17, 22, 26, 31, 35, 40, 50, 44, 48, 51, 55, 12, 0, 49, 57, 4, 11, 15, 57, 20, 24, 28, 33, 37, 42, 46],
    [49, 53, 54, 58, 59, 1, 5, 8, 12, 16, 20, 58, 24, 29, 33, 27, 37, 0, 41, 45, 49, 52, 56, 43, 3, 7, 14, 19, 22, 27],
    [31, 35, 40, 44, 48, 51, 53, 57, 58, 4, 9, 11, 30, 15, 18, 23, 27, 30, 0, 46, 36, 42, 45, 47, 57, 51, 54, 58, 2, 7],
    [13, 16, 21, 25, 29, 33, 38, 40, 44, 49, 52, 56, 59, 12, 2, 5, 8, 11, 56, 0, 30, 14, 17, 20, 23, 60, 26, 29, 32, 35],
    [38, 40, 1, 4, 7, 10, 13, 16, 19, 22, 25, 24, 28, 31, 16, 34, 37, 39, 3, 24, 0, 43, 12, 3, 6, 9, 60, 12, 15, 15],
    [18, 21, 24, 27, 30, 33, 36, 39, 1, 4, 7, 10, 13, 16, 19, 6, 22, 25, 28, 31, 46, 0, 44, 34, 37, 40, 2, 58, 11, 23],
    [1, 5, 8, 10, 14, 17, 21, 24, 26, 30, 33, 36, 38, 2, 7, 11, 23, 13, 16, 20, 23, 10, 0, 30, 25, 29, 32, 35, 60, 29],
    [39, 38, 2, 7, 11, 13, 16, 20, 23, 25, 29, 32, 35, 39, 40, 3, 12, 26, 19, 28, 4, 6, 19, 0, 9, 13, 15, 18, 22, 60],
    [25, 27, 31, 33, 36, 38, 2, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 39, 7, 40, 5, 12, 21, 30, 0, 52, 33, 36, 38, 40],
    [2, 14, 16, 30, 2, 6, 8, 11, 15, 17, 20, 24, 27, 29, 23, 32, 35, 38, 40, 21, 3, 7, 10, 13, 46, 0, 39, 16, 19, 22],
    [25, 28, 31, 34, 36, 39, 1, 12, 23, 1, 4, 9, 12, 16, 18, 22, 25, 26, 29, 31, 10, 33, 36, 38, 2, 48, 0, 52, 6, 10],
    [14, 17, 21, 24, 27, 30, 34, 37, 39, 40, 5, 13, 20, 28, 2, 5, 9, 11, 14, 17, 21, 25, 24, 27, 30, 33, 53, 0, 9, 35],
    [38, 40, 1, 4, 7, 10, 13, 16, 19, 22, 26, 29, 32, 36, 39, 3, 8, 12, 15, 18, 20, 25, 16, 28, 31, 34, 37, 3, 0, 30],
    [2, 6, 11, 11, 14, 17, 23, 27, 30, 33, 35, 39, 1, 6, 5, 9, 13, 16, 21, 24, 28, 22, 32, 23, 36, 40, 10, 50, 42, 0]])

def sigmoid(x):
    return (2/ (1 + math.exp(-x)))-1

esquinas = np.array([0,columnas-1,dimension_array-columnas,dimension_array-1])
aristas_superiores = np.arange(1,columnas-1)
aristas_laterales_izquierda = np.arange(columnas, dimension_array-columnas,columnas)
aristas_laterales_derecha = np.arange((2*columnas)-1, dimension_array-columnas+1, columnas)
aristas_inferiores = np.arange(dimension_array-columnas+1, dimension_array-1)

hashmap_index_conections = {0:[np.array([1,columnas]), [32,35]], 5:[np.array([columnas-2,2*columnas-1]), [16,20]], 24:[np.array([dimension_array-(2*columnas),dimension_array-columnas+1]), [7,54]], 29:[np.array([dimension_array-2,dimension_array-columnas-1]), [23,42]]}

for i in range(len(comportamiento_previo_x)):  
    if i in esquinas:
        continue
    else:
        if i in aristas_superiores:
            hashmap_index_conections[i] = [[i-1, i+1, i+columnas], [matriz_k[i][i-1], matriz_k[i][i+1], matriz_k[i][i+columnas]]]
        elif i in aristas_laterales_izquierda:
            hashmap_index_conections[i] = [[i-columnas, i+columnas, i+1], [matriz_k[i][i-columnas], matriz_k[i][i+columnas], matriz_k[i][i+1]]]
        elif i in aristas_laterales_derecha:
            hashmap_index_conections[i] = [[i-columnas, i+columnas, i-1], [matriz_k[i][i-columnas], matriz_k[i][i+columnas], matriz_k[i][i-1]]]
        elif i in aristas_inferiores:
            hashmap_index_conections[i] = [[i-1, i+1, i-columnas], [matriz_k[i][i-1], matriz_k[i][i+1], matriz_k[i][i-columnas]]]
        else:
            hashmap_index_conections[i] = [[i-columnas, i+1, i+columnas, i-1], [matriz_k[i][i-columnas], matriz_k[i][i+1],matriz_k[i][i+columnas], matriz_k[i][i-1]]]


print(comportamiento_previo_x, parametro_de_orden)
resultado_x = comportamiento_previo_x.copy()
while True:
    for i in range(len(comportamiento_previo_x)):
        suma = 0
        for j in range(len(hashmap_index_conections[i][0])):
            suma += hashmap_index_conections[i][1][j] * ((comportamiento_previo_x[i]-comportamiento_previo_x[hashmap_index_conections[i][0][j]])**3)
        resultado_x[i] = comportamiento_previo_x[i] - sigmoid(suma * h)
    comportamiento_previo_x = resultado_x
    parametro_de_orden = np.sum(comportamiento_previo_x) / dimension_array
    print(comportamiento_previo_x, parametro_de_orden)