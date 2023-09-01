import math
import numpy as np


def matrix_mul(matrix1, matrix2):
    result = []

    # assumes matrix 2 is actualyl a vecotr

    for i in range(len(matrix1)):
        total = 0
        for j in range(len(matrix1)):
            total = total + matrix2[i] * matrix1[i][j]
        result.append(total)

    return result


def hill_cipher(Message, key):


    msgMatrix = []
    for i in range(len(Message)):
        if Message[i].isupper():
            msgMatrix.append(ord(Message[i]) - 64 - 1)
        else:
            msgMatrix.append(ord(Message[i]) - 97 - 1)

    result = matrix_mul(matrix, msgMatrix)


def run_with_text(message, key):
    # step 1, build matrix size of key; assume key length is even square
    matrix = []
    dimension = int(math.sqrt(len(key)))
    for i in range(dimension):
        matrix.append([])
        for j in range(dimension):
            if key[i * dimension + j].isupper():
                # upper case
                matrix[i].append(ord(key[i * dimension + j]) - 64 - 1 + 26)
            else:
                # lower case
                matrix[i].append(ord(key[i * dimension + j]) - 97 - 1)

    hill_cipher(message, matrix)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    message = "POH"
    key = "GYBNQKURP"
    run_with_text(message, key)
    run_with_numbers(message, key)
    hill_cipher(Message, key)
