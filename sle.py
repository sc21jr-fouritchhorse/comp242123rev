import sys

import numpy as np


def swap_rows(A):
    return np.argsort(A[:, 0])
def make_upper_triangular(A):
    for i in range(0, A.shape[0]):
        for j in range(i + 1, A.shape[0]):
            A[j] = A[j] - (A[i] * A[j, i] / A[i, i])
    return A

def backward_subst(T, b):

    return T

def main():
    np.random.seed(42)

    # Generate a random 6x6 matrix
    my_mat = np.random.randint(0, 20, size=(6, 6))
    my_vec = np.random.randint(0, 20, size=(6));
    print(my_mat)
    print(my_vec)
    print(make_upper_triangular(my_mat[swap_rows(my_mat)]))
    print(my_vec[swap_rows(my_mat)])
    return 0


if __name__ == '__main__':
    sys.exit(main())
