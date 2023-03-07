from sys import exit
import argparse as argp
import numpy as np
#import scipy
from matrix_handle import random_aug_matrix
from matrix_handle import print_augm_matrix
from matrix_handle import import_matrix_from_file

def gauss_elimination(inputMatrix, size):
    e = 0.0001

    # Zero division checking
    for r in range(size):
        if abs(inputMatrix[r][r]) < e:
            exit("Division by zero")

        for k in range(r+1, size):
            ratio = inputMatrix[k][r]/inputMatrix[r][r]

            Ab[k] = Ab[k] - ratio * Ab[r]
    
    print_augm_matrix(inputMatrix, size)

def gauss_elimination_partial_pivot(inputMatrix, size):
    e = 0.0001

    for r in range(size):
        # Searching non-zero value for division
        p = 0 
        while abs(inputMatrix[r][r+p]) < e: p+=1
        # Swapping rows
        inputMatrix[[r, r+p]] = inputMatrix[[r+p, r]]

        for k in range(r+1, size):
            ratio = inputMatrix[k][r]/inputMatrix[r][r]

            Ab[k] = Ab[k] - ratio * Ab[r]
    
    print_augm_matrix(inputMatrix, size)


def back_substitution(solutionVector, inputMatrix, size):
    solutionVector[size-1] = inputMatrix[size-1][size] / inputMatrix[size-1][size-1]

    for r in range(size-2,-1,-1):
        solutionVector[r] = inputMatrix[r][size]
        for k in range(r+1, size):
            solutionVector[r] = solutionVector[r] - inputMatrix[r][k] * solutionVector[k]

        solutionVector[r] = solutionVector[r] / inputMatrix[r][r]

[Ab, N] = import_matrix_from_file("zadania\zad4.txt")

# Solution vector of N elements
x = np.zeros(shape=N)
# Printing augmented matrix
print_augm_matrix(Ab, N)
# Perform gauss elimination
#gauss_elimination(Ab, N)
gauss_elimination_partial_pivot(Ab, N)
# Back substitution of gauss elimination result
back_substitution(x, Ab, N)
print(x, "^T")
