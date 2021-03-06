import unittest
import LibrarySystems as ls
import numpy as np
import matplotlib.pyplot as plt


class TestStringMethods(unittest.TestCase):

    def test_sistema_deter(self):
        matriz = np.array([[0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 1, 0, 0],
                           [0, 1, 0, 0, 0, 1],
                           [0, 0, 1, 0, 0, 0],
                           [0, 0, 0, 0, 1, 0],
                           [1, 0, 0, 0, 0, 0]])
        vector_estado = np.array([6, 0, 3, 5, 3, 8])
        B = vector_estado[:]
        clicks = 5000
        for i in range(clicks):
            B = np.dot(matriz, B)
        ls.graficar(vector_estado)
        self.assertTrue((B == ls.sistemaDeterProbaCuan(matriz, vector_estado, clicks)).all())
        clicks = 4000
        B = vector_estado[:]
        for i in range(clicks):
            B = np.dot(matriz, B)
        self.assertTrue((B == ls.sistemaDeterProbaCuan(matriz, vector_estado, clicks)).all())

    def test_sistema_proba(self):
        matriz = np.array([[0, 1/6, 5/6],
                           [1/3, 1/2, 1/6],
                           [2/3, 1/3, 0]])
        vector_estado = np.array([1/6, 1/6, 2/3])
        B = vector_estado[:]
        clicks = 5000
        for i in range(clicks):
            B = np.dot(matriz, B)
        self.assertTrue((B == ls.sistemaDeterProbaCuan(matriz, vector_estado, clicks)).all())
        clicks = 4000
        B = vector_estado[:]
        for i in range(clicks):
            B = np.dot(matriz, B)
        self.assertTrue((B == ls.sistemaDeterProbaCuan(matriz, vector_estado, clicks)).all())


    def test_sistema_cuant(self):
        matriz = np.array([[1/2**(1/2), 1/2**(1/2), 0],
                           [-1j/2**(1/2), 1j/2**(1/2), 0],
                           [2/3, 1/3, 0]])
        vector_estado = np.array([1/6, 1/6, 2/3])
        B = vector_estado[:]
        clicks = 5000
        for i in range(clicks):
            B = np.dot(matriz, B)
        self.assertTrue((B == ls.sistemaDeterProbaCuan(matriz, vector_estado, clicks)).all())
        clicks = 4000
        B = vector_estado[:]
        for i in range(clicks):
            B = np.dot(matriz, B)
        self.assertTrue((B == ls.sistemaDeterProbaCuan(matriz, vector_estado, clicks)).all())

    def test_multiple_rendija_proba(self):
        vector_estado = np.array([0, 0, 0, 1/6, 1/6, 1/3, 1/6, 1/6])
        rendijas, blancos, clicks = 2, 3, 2
        for i in range(len(vector_estado)):
            vector_estado[i] = round(vector_estado[i], 1)
        vector_estado_calculado = ls.multipleRendija(rendijas, blancos, clicks)[0]
        for i in range(len(vector_estado_calculado)):
            vector_estado_calculado[i] = round(vector_estado_calculado[i], 1)
        self.assertTrue((vector_estado == vector_estado_calculado).all())
        vector_estado = np.array([0, 0, 0, 0, 0.1089, 0.1089, 0.2178, 0.1089, 0.2178, 0.1089, 0.1089])
        rendijas, blancos, clicks = 3, 3, 2
        for i in range(len(vector_estado)):
            vector_estado[i] = round(vector_estado[i], 1)
        vector_estado_calculado = ls.multipleRendija(rendijas, blancos, clicks)[0]
        for i in range(len(vector_estado_calculado)):
            vector_estado_calculado[i] = round(vector_estado_calculado[i], 1)
        self.assertTrue((vector_estado == vector_estado_calculado).all())

    def test_multiple_rendija_cuant(self):
        vector_estado = np.array([0, 0, 0,
       -0.71+0.52670383j, -0.71-0.52670383j,  0.  +0.j        ,
       -0.71-0.52670383j,  0.71-0.52670383j])
        rendijas, blancos, clicks, probs = 2, 3, 2, [-1+1j/6**(1/6), -1-1j/6**(1/6), 1-1j/6**(1/6)]
        for i in range(len(vector_estado)):
            vector_estado[i] = np.round(vector_estado[i], 1)
        vector_estado_calculado = ls.multipleRendijaCuantico(2, 3, [-1+1j/6**(1/6), -1-1j/6**(1/6), 1-1j/6**(1/6)], 2)[0]
        for i in range(len(vector_estado_calculado)):
            vector_estado_calculado[i] = np.round(vector_estado_calculado[i], 1)
        print(vector_estado, vector_estado_calculado)
        self.assertTrue((vector_estado == vector_estado_calculado).all())


if __name__ == '__main__':
    unittest.main()