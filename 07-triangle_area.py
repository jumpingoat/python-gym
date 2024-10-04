import numpy as np
import matplotlib.pyplot as plt

A = []
print('Podaj współrzędne x i y wierzchołka A, oddzielając je Enterem')

# iteracja po dwóch współrzędnych dla A
for i in range(0, 2):
    elt = int(input())

    A.append(elt)  # dodajemy te wartości do A

B = []
print('Podaj współrzędne x i y wierzchołka B, oddzielając je Enterem')

for i in range(0, 2):
    elt2 = int(input())

    B.append(elt2)

C = []
print('Podaj współrzędne x i y wierzchołka C, oddzielając je Enterem')

for i in range(0, 2):
    elt3 = int(input())

    C.append(elt3)

pole = np.int([A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1])] / 2)
print(pole)


plt.plot([A[0], C[0], B[0], A[0]], [A[1], C[1], B[1], A[1]], 'b')
plt.show()