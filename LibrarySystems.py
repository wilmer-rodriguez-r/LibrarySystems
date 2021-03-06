import numpy as np
import matplotlib.pyplot as plt

def graficar(vector_estado):
    vector = [i + 1 for i in range(len(vector_estado))]
    plt.bar(vector, vector_estado)
    return plt.show()

def sistemaDeterProbaCuan(A,B, j):
    for i in range(j):
        B = np.dot(A, B)
    return B


def multipleRendija(num, blancos,k):
    prob = round(1/blancos, 2)
    size, prob_2 = num*blancos+2, round(1/num, 2)
    matriz = [[0 for j in range(size)] for i in range(size)]
    for i in range(size):
        for j in range(size):
            aux = num + (blancos * (j - 1))
            if i == j and i > num:
                matriz[i][j] = 1
            if j == 0 and i in range(1, num + 1):
                matriz[i][j] = prob_2
            if j in range(1, num+1) and i in range(aux + 2-j, aux + blancos + 2-j):
                matriz[i][j] = prob
    a = [1 if i == 0 else 0 for i in range(size)]
    vector = sistemaDeterProbaCuan(matriz, a, k)
    for i in range(k):
        matriz = np.dot(matriz, matriz)
    return vector, matriz


def multipleRendijaCuantico(num, blancos, probabilidades, k):
    size, prob = num*blancos+2, round(1/num**(1/2), 2)
    matriz = [[0 for j in range(size)] for i in range(size)]
    for i in range(size):
        for j in range(size):
            aux = num + (blancos * (j - 1))
            if i == j and i > num:
                matriz[i][j] = 1
            if j == 0 and i in range(1, num + 1):
                matriz[i][j] = prob
            if j in range(1, num+1) and i in range(aux + 2-j, aux + blancos + 2-j):
                matriz[i][j] = probabilidades[abs(aux + 2 - j - i)]
    a = [1 if i == 0 else 0 for i in range(size)]
    vector = sistemaDeterProbaCuan(matriz, a, k)
    for i in range(k):
        matriz = np.dot(matriz, matriz)
    return vector, matriz

print(multipleRendijaCuantico(2, 3, [-1+1j/6**(1/6), -1-1j/6**(1/6), 1-1j/6**(1/6)], 2))
#print(sistemaDeterProbaCuan([[0, 0, 0, 0, 0, 0, 0, 0], [0.71, 0, 0, 0, 0, 0, 0, 0], [0.71, 0, 0, 0, 0, 0, 0, 0], [0, (-0.4082482904638631+0.4082482904638631j), 0, 1, 0, 0, 0, 0], [0, (-0.4082482904638631-0.4082482904638631j), 0, 0, 1, 0, 0, 0], [0, (0.4082482904638631-0.4082482904638631j), (-0.4082482904638631+0.4082482904638631j), 0, 0, 1, 0, 0], [0, 0, (-0.4082482904638631-0.4082482904638631j), 0, 0, 0, 1, 0], [0, 0, (0.4082482904638631-0.4082482904638631j), 0, 0, 0, 0, 1]],[1, 0, 0, 0, 0, 0, 0, 0], 2))