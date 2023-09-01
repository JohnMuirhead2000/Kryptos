# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 12:02:26 2023
@author: bvoc5
"""

numRows = 3
numCols = 20

Row1 = ['H', 'E', 'T', 'T', 'P', 'H', 'U', 'E', 'M', 'H', 'E', 'E', 'Z', 'F', 'I', 'S', 'I', 'A', 'Z', 'C']
Row2 = ['L', 'N', 'H', 'R', 'N', 'A', 'I', 'O', 'S', 'E', 'S', 'R', 'L', 'D', 'W', 'E', 'S', 'O', 'P', 'D']
Row3 = ['E', 'R', 'R', 'W', 'W', 'T', 'T', 'N', 'O', 'O', 'B', 'I', 'R', 'O', 'E', 'D', 'N', 'L', 'N', 'T']

cipherMatrix = []
cipherMatrix.append(Row1)
cipherMatrix.append(Row2)
cipherMatrix.append(Row3)

keyMatrix = []
keyMatrix.append(['0', '1', '2'])
keyMatrix.append(['2', '0', '1'])
keyMatrix.append(['1', '2', '0'])

plainMatrix = [[0] * numCols] * numRows
for i in range(int(numCols / numRows)):

    for j in range(3):
        t = [0] * 3

        t[0] = cipherMatrix[0][int(3 * i + j)]
        t[1] = cipherMatrix[1][int(3 * i + j)]
        t[2] = cipherMatrix[2][int(3 * i + j)]

        plainMatrix[0][int(3 * i + j)] = t[int(keyMatrix[0][j])]
        plainMatrix[1][int(3 * i + j)] = t[int(keyMatrix[1][j])]
        plainMatrix[2][int(3 * i + j)] = t[int(keyMatrix[2][j])]

    #print(plainMatrix)
    for line in plainMatrix:
        print(line)


print(plainMatrix)