import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg, bitwise_or

R1 = np.array([[1, 1, 1, 1, 0],#a
              [1, 1, 0, 0, 1],#b
              [1, 0, 1, 0, 1],#c
              [1, 0, 0, 1, 1],#d
              [0, 0, 0, 0, 1]])#e
print(" Matrix R1 =", R1)

R3 = R1.T #inverse matrix
R4 = R1 | R3 #combining the matrix with the inverse
R5 = R1 & R3 #section with inverse matrix
print("Equivalence ratio", R5)
R6 = np.zeros((5, 5))
for i in range(0, 5):
    for j in range(0, 5):
        if R1[i][j] > 0 and R3[i][j] == 0:
            R6[i][j] = 1
        else:
            R6[i][j] = 0
print("The relationship of strict advantage", R6) #the difference of the matrix with the inverse
R7 = 1-R1
R8 = R7.T #inverse complement of the matrix
print("Dominance ratio", R1 & R8) #the cross section of the matrix with the inverse complement
R9 = np.ones((5, 5))
R10 = np.zeros((5, 5))
for i in range(0, 5):
    for j in range(0, 5):
        if R9[i][j] > 0 and R4[i][j] == 0:
            R10[i][j] = 1
        else:
            R10[i][j] = 0
R12 = np.zeros((5, 5))
for i in range(0, 5):
    for j in range(0, 5):
        if R10[i][j] == 1 and R5[i][j] == 0 or R10[i][j] == 0 and R5[i][j] == 1:
            R12[i][j] = 1
        else:
            R12[i][j] = R10[i][j] * R5[i][j]
print("Tolerance ratio", R12)
R11 = np.zeros((5, 5))
Minimum = True
for j in range(0, 5):
    while Minimum:
        if R1[i][j] == 0:
            Minimum = False
            print("There are no minimums")
        else:
            Minimum = True
            break
Maximum = True
for i in range(0, 5):
        while Maximum:
            if R1[i][i] == 1:
                Maximum = False
                print("There are no maximums")
            else:
                Maximum = True
                break
Minorant = True
for i in range(0, 5):
    while Minorant:
        if R1[i][j] == 0:
            Minorant = False
            print("There is no R-Minorant")
        else:
            Minorant = True
            break
Magorant = True
for j in range(0, 5):
        while Magorant:
            if R1[i][i] == 1:
                Magorant = False
                print("There is no R-Majorant")
            else:
                Magorant = True
                break

G = nx.from_numpy_matrix(np.matrix(R1), create_using=nx.DiGraph)
layout = nx.spring_layout(G)
nx.draw(G, with_labels=True)
plt.show()

G1 = nx.from_numpy_matrix(np.matrix(R5), create_using=nx.DiGraph)
layout = nx.spring_layout(G)
nx.draw(G, with_labels=True)
plt.show()

G2 = nx.from_numpy_matrix(np.matrix(R6), create_using=nx.DiGraph)
layout = nx.spring_layout(G)
nx.draw(G, with_labels=True)
plt.show()

G3 = nx.from_numpy_matrix(np.matrix(R1 & R8), create_using=nx.DiGraph)
layout = nx.spring_layout(G)
nx.draw(G, with_labels=True)
plt.show()

G3 = nx.from_numpy_matrix(np.matrix(R12), create_using=nx.DiGraph)
layout = nx.spring_layout(G)
nx.draw(G, with_labels=True)
plt.show()

