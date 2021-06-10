import config as cfg
from math import sin, cos


def get_funcs():
    funcs = [lambda x, z: sin(x) * sin(z), lambda x, z: sin(cos(x)) * sin(z), lambda x, z: cos(x) * z / 3]

    return funcs


def is_visible(point):
    return 0 <= point[0] < 900 and 0 <= point[1] < 750


def rotate_matrix(transform_matrix, rotate_matrix_):
    res_matrix = [[0 for i in range(4)] for j in range(4)]

    for i in range(4):
        for j in range(4):
            for k in range(4):
                res_matrix[i][j] += transform_matrix[i][k] * rotate_matrix_[k][j]

    transform_matrix = res_matrix
    return transform_matrix
