import sys

import numpy as np


def swap_rows(A):
    return np.argsort(-A[:,0])

def make_upper_triangular(A, b):
    for i in range(0, A.shape[0]):
        for j in range(i + 1, A.shape[0]):
            quot =  A[j][i]/A[i][i]
            A[j] = A[j] - A[i] * quot
            b[j] = b[j] - b[i] * quot
    return A, b

def backward_subst(A, b):
    x = np.zeros_like(b)
    #x[end] = b[end] / A[end,end]
    for i in range(A.shape[0]-1, -1, -1):
        sum = 0
        for j in range(i + 1,A.shape[0]):
            sum += A[i,j] * x[j]
        x[i] = (b[i] - sum)/A[i][i]
    return x

def main():
    np.random.seed(42)

    # Generate a random 6x6 matrix
    dimensions = 3
    my_mat = np.random.randint(1, 10, size=(dimensions, dimensions))
    my_vec = np.random.randint(-25, 25, size=(dimensions))
    #my_mat = np.array([[2, 1, 4],[0, 1.5, 0], [0, 0, 2]])
    #my_vec = np.array([12, 3, 4])
    print(my_mat)
    print(my_vec)
    swapped_ind = swap_rows(my_mat)
    triangular, b = make_upper_triangular(my_mat[swapped_ind], my_vec[swapped_ind])
    print(triangular)
    print(b)
    print(backward_subst(triangular, b))

    return 0


if __name__ == '__main__':
    sys.exit(main())
