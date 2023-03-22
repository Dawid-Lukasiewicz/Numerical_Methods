import sys
sys.path.append("../")

import scipy as sci
import numpy as np

def eig(A, epsilon=1e-10, max_iterations=1000):
    """
    Calculates the eigenvalues and eigenvectors of a square matrix using the QR algorithm.

    Args:
        A (numpy.ndarray): A square matrix.
        epsilon (float): The convergence threshold.
        max_iterations (int): The maximum number of iterations to perform.

    Returns:
        Tuple containing the eigenvalues and eigenvectors of the matrix A.
    """
    # Initialize the eigenvectors to the identity matrix
    n = A.shape[0]
    Q = np.eye(n)

    # Repeat until convergence or maximum number of iterations is reached
    for i in range(max_iterations):
        # Apply the QR decomposition to A
        Q, R = np.linalg.qr(A.dot(Q))

        # Calculate the new matrix A
        A = R.dot(Q)

        # Check for convergence
        if np.abs(A.diagonal() - A.diagonal().min()).max() < epsilon:
            break

    # Extract the eigenvalues and eigenvectors
    eigenvalues = A.diagonal()
    eigenvectors = Q

    return eigenvalues, eigenvectors


def power_method(A, itr):
    # If A not square matrix then return False
    n, m = A.shape
    if not n == m:
        return False

    x = np.ones([n, 1])
    for i in range(itr):
        x = np.dot(A, x)
        h1 = abs(x).max()
        x = x / x.max()
    
    return h1, x

# This method finds smallest just by inverting matrix A
# and perfomring power method on such matrix
def inverse_power_method(A, itr):
    A_inv = sci.linalg.inv(A)  
    h1_inv, x_inv = power_method(A_inv, itr)
    return 1/h1_inv, 1/x_inv

def shifted_power_method(A, itr):
    # If A not square matrix then return False
    n, m = A.shape
    if not n == m:
        return False

    for i in range(itr):
        Q, R = np.linalg.qr(A)
        A = np.dot(R, Q)

    return A

def svd_method(A):
    n, m = A.shape
    rankA = np.linalg.matrix_rank(A)

    matrixW = sci.matmul(A, A.T)
    vectorLambdaU, matrixU = sci.linalg.eig(matrixW)
    print("U = \n", matrixU)

    matrixR = sci.matmul(A.T, A)
    vectorLambdaV, matrixV = sci.linalg.eig(matrixR)
    print("V = \n", matrixV)

    vectorSigma = np.sqrt(vectorLambdaU)
    vectorSigmaNonZero = []
    for index, sigmaVal in enumerate(vectorSigma):
        if sigmaVal > 0:
            vectorSigmaNonZero.append(sigmaVal)

    vectorSigmaNonZero = np.asarray(vectorSigmaNonZero)
    S_diag = np.asarray(np.diag(vectorSigmaNonZero))
    # S = np.asmatrix(np.diag(vectorSigmaNonZero))
    if n == m:
        shape = (n, n)
        print(shape)
        # S = np.resize(S, shape)
    elif m > n and rankA == n:
        S = np.zeros((len(vectorSigmaNonZero), m))
        # S = np.pad(S, ((m-n, 0), (0, 0)), "constant", constant_values=(0))
    elif n > m and rankA == m:
        S = np.zeros((n, len(vectorSigmaNonZero)))
        # S = np.pad(S, ((0, n-m), (0, 0)), "constant", constant_values=(0))

    for i in range(len(S_diag[0])):
        for j in range(len(S_diag[i])):
            S[i][j] = S_diag[i][j].real

    print("S = \n", S)

    return matrixU, S, matrixV
