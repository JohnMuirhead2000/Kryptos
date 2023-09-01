# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 11:12:49 2023
@author: bvoc5
"""

import math
import numpy

spec_result_file = ""
float_tolerance = 0.000001

# Spectra to test
spec_eig_1 = [2 + numpy.sqrt(14), 4, -1, 2 - numpy.sqrt(14)]
spec_mult_1 = [1, 1, 8, 1]
# Spectra to test
spec_eig_2 = [2 + numpy.sqrt(14), 4, -1, 2 - numpy.sqrt(14)]
spec_mult_2 = [1, 2, 12, 1]

spec_eig_4 = [5, 3, 1, -1, -3, -5]
spec_mult_4 = [1, 5, 10, 10, 5, 1]

spec_eig_5 = [5, numpy.cbrt(98), 2, -3, -numpy.cbrt(98)]
spec_mult_5 = [1, 22, 38, 27, 22]

spec_eig_6 = [6, 4, -3, -8]
spec_mult_6 = [1, 2, 2, 1]

spec_eig_7 = [9, 1, -1, -7]
spec_mult_7 = [1, 6, 8, 1]

spec_eig_8 = [10, 7, 5, 2, 0, -3]
spec_mult_8 = [1, 2, 8, 16, 16, 32]

spec_eig_10 = [10, 7, 5, 0, -2]
spec_mult_10 = [1, 2, 8, 16, 32]


def eigSum(spec_eig, spec_mult, power):
    eig_sum = 0
    mult_index = 0
    for eig in spec_eig:
        eig_sum = eig_sum + (math.pow(eig, power)) * spec_mult[mult_index]
        mult_index = mult_index + 1
    return eig_sum


def numVertices(spec_mult):
    mult_sum = 0
    for mult in spec_mult:
        mult_sum = mult_sum + mult
    return mult_sum


def resolveFloatingArithmetic(float_val):
    if (int(float_val) == float_val):
        return int(float_val)
    else:

        d1 = abs(float_val - math.ceil(float_val))
        d2 = abs(float_val - math.floor(float_val))

        if (d1 < float_tolerance):
            return int(math.ceil(float_val))
        elif (d2 < float_tolerance):
            return int(math.floor(float_val))
        else:
            return "ERROR"


def build_full(spec_eig, spec_mult):

    full = []
    for i in range(len(spec_eig)):
        for j in range(spec_mult[i]):
            full.append(spec_eig[i])
    return full

def check_index(eig, r, t, edges):
    left_side = math.pow(((2 * edges) / (r + math.pow(r, (2/3)))), .5)
    right_side = - (math.pow(((2 * edges) / (t + math.pow(t, (2/3)))), .5))

    return not (eig > left_side or eig < right_side)

        # we have broken the principal!

def zero_triangle_case(verticies, edges, spec_eig, spec_mult):
    full_spec = build_full(spec_eig, spec_mult)
    p = len(full_spec)

    for r in range(1, len(full_spec)+1):
        t = p - r + 1
        eig = full_spec[r-1]
        if not check_index(eig, r, t, edges):
            print("COROLARY 3 BROKE THIS 0 TRIANLGE GRAPH")
            return
    print("COROLARY 3 DID NOT BRAKE THIS 0 TRIANLGE GRAPH")

def specAnalysis(spec_eig, spec_mult, spec_id):
    global spec_result_file

    eig_sum_f = eigSum(spec_eig, spec_mult, 1)
    eig_sum_squared_f = eigSum(spec_eig, spec_mult, 2)
    eig_sum_cubed_f = eigSum(spec_eig, spec_mult, 3)

    eig_sum_i = resolveFloatingArithmetic(eig_sum_f)
    eig_sum_squared_i = resolveFloatingArithmetic(eig_sum_squared_f)
    eig_sum_cubed_i = resolveFloatingArithmetic(eig_sum_cubed_f)

    b1 = (eig_sum_i != "ERROR") and (eig_sum_i == 0)
    b2 = (eig_sum_squared_i != "ERROR") and ((eig_sum_squared_i % 2) == 0)
    b3 = (eig_sum_cubed_i != "ERROR") and ((eig_sum_cubed_i % 6) == 0) and (eig_sum_cubed_i >= 0)
    b4 = 1
    b5 = 1
    b6 = 1

    # Stanley's and Hong's Test:
    spec_rad = max(spec_eig)
    if b2:
        b4 = (spec_rad * (spec_rad + 1) <= eig_sum_squared_i)
        b5 = spec_rad <= numpy.sqrt(eig_sum_squared_i - numVertices(spec_mult) + 1)
        b6 = spec_rad <= numpy.sqrt(eig_sum_squared_i)



    test_result = ""
    if b1 and b2 and b3 and b4 and b5 and b6:
        test_result = "INCONCLUSIVE"
    else:
        test_result = "FAIL"

    spec_result_file.write("SPECTRAL ANALYSIS RESULTS: " + str(spec_id) + "\n")
    spec_result_file.write("Result: " + test_result)
    spec_result_file.write("\n")

    spec_result_file.write("Largest Eigenvalue:  " + str(max(spec_eig)) + "\n")
    spec_result_file.write("Smallest Eigenvalue: " + str(min(spec_eig)) + "\n")
    spec_result_file.write("\n")

    spec_result_file.write("Sum of Eigenvalues (F):         " + str(eig_sum_f) + "\n")
    spec_result_file.write("Sum of Eigenvalues Squared (F): " + str(eig_sum_squared_f) + "\n")
    spec_result_file.write("Sum of Eigenvalues Cubed (F):   " + str(eig_sum_cubed_f) + "\n")
    spec_result_file.write("\n")

    spec_result_file.write("Sum of Eigenvalues (I):         " + str(eig_sum_i) + "\n")
    spec_result_file.write("Sum of Eigenvalues Squared (I): " + str(eig_sum_squared_i) + "\n")
    spec_result_file.write("Sum of Eigenvalues Cubed (I):   " + str(eig_sum_cubed_i) + "\n")
    spec_result_file.write("\n")

    if (b1 and b2 and b3 and b4):
        spec_result_file.write("Number of Vertices:    " + str(numVertices(spec_mult)) + "\n")
        spec_result_file.write("Number of Edges:       " + str(math.ceil(eig_sum_squared_i) / 2) + "\n")
        spec_result_file.write("Number of Triangles:   " + str(math.ceil(eig_sum_cubed_i) / 6) + "\n")

        if math.ceil(eig_sum_cubed_i) / 6 == 0:
            zero_triangle_case(numVertices(spec_mult), math.ceil(eig_sum_squared_i) / 2, spec_eig, spec_mult)

        spec_result_file.write("\n")
        spec_result_file.write("Sum of Vertex Degrees: " + str(eig_sum_squared_i) + "\n")
        spec_result_file.write("Average Vertex Degree: " + str(eig_sum_squared_i / numVertices(spec_mult)) + "\n")

    spec_result_file.write("\n")


def main():
    global spec_result_file

    spec_result_file = open("spec_results.txt", "w")

    specAnalysis(spec_eig_1, spec_mult_1, 1)
    specAnalysis(spec_eig_2, spec_mult_2, 2)
    specAnalysis(spec_eig_4, spec_mult_4, 4)
    specAnalysis(spec_eig_5, spec_mult_5, 5)
    specAnalysis(spec_eig_6, spec_mult_6, 6)
    specAnalysis(spec_eig_7, spec_mult_7, 7)
    specAnalysis(spec_eig_8, spec_mult_8, 8)
    specAnalysis(spec_eig_10, spec_mult_10, 10)

    spec_result_file.close()


if __name__ == "__main__":
    main()
