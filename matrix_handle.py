from random import uniform
import numpy as np
import re

def print_augm_matrix(inputMatrix, size):
    for r in range(size):
        print("[ ", end="")
        for c in range(size):
            print(" ", inputMatrix[r][c], " ", end="")
        print("| ", inputMatrix[r][size], " ]")
    print("")

def random_aug_matrix(inputMatrix, size):
    for r in range(size):
        for c in range(size):
            inputMatrix[r][c] = uniform(0, 10)
        inputMatrix[r][size] = uniform(0, 10)

def import_matrix_from_file(fileName):
    file = open(fileName, "r")

    # Read the first line and load it to 2d array
    line = file.readline()
    offset = len(line)
    line = re.sub("\n", "", line)
    array2d = np.array(re.split(" ", line, maxsplit=0))
    array2d = [float(i) for i in array2d]
    matrixSize = len(array2d)
    
    # Offset for new line
    file.seek(offset)

    #  Iterating through all the rest
    for line in file:
        line = re.sub("\n", "", line)
        array = re.split(" ", line, maxsplit=0)
        array = [float(i) for i in array]
        array2d = np.vstack((array2d, array))

    file.close()
    importedMatrix = np.asarray(array2d)
    return [importedMatrix, matrixSize-1]
