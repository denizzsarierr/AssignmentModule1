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



