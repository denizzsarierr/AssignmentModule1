# Version 2.0
import numpy as np

def dot_product(X,Y):

    return np.dot(X,Y)

def inverse(X):

    return np.linalg.inv(X)

def transpose(X):

    return X.transpose()

def power(X,n):

    return np.linalg.matrix_power(X,n)

def operations(X,Y,n):

    print(f"Dot Product of X and Y: {dot_product(X,Y)}")
    print("===========================================")
    print(f"Inverse of X: {inverse(X)}")
    print("===========================================")
    print(f"Transpose of X: {transpose(X)}")
    print("===========================================")
    print(f"X to the power of {n}: {power(X,n)}")




