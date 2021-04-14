import math


def length(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def get_sides(x, y):
    a = length(x[1], y[1], x[2], y[2])
    b = length(x[0], y[0], x[2], y[2])
    c = length(x[0], y[0], x[1], y[1])
    return [a, b, c]


def get_one_bisector_coordinate(t, sides):
    return (sides[0] * t[0] + sides[1] * t[1] + sides[2] * t[2]) / (sides[0] + sides[1] + sides[2])


def get_bisector_coordinates(x, y):
    sides = get_sides(x, y)
    x0 = get_one_bisector_coordinate(x, sides)
    y0 = get_one_bisector_coordinate(y, sides)
    return x0, y0


def check_triangle(x, y):
    vector_a = (abs(x[1] - x[0]), abs(y[1] - y[0]))
    vector_b = (abs(x[2] - x[0]), abs(y[2] - y[0]))
    return vector_a[0] * vector_b[1] - vector_a[1] * vector_b[0]


def triplets(x, y):
    for i in range(len(x) - 2):
        for j in range(i + 1, len(x) - 1):
            for z in range(j + 1, len(x)):
                x0 = (x[i], x[j], x[z])
                y0 = (y[i], y[j], y[z])
                if check_triangle(x0, y0):
                    yield x0, y0
                else:
                    continue


def cotangent(x1, y1, x2, y2):
    return abs(x2 - x1) / abs(y2 - y1)


def find_result(x1, y1, x2, y2):
    minimum_angle = 0
    triangles = []
    bisectors = []
    flag = False
    for t1 in triplets(x1, y1):
        for t2 in triplets(x2, y2):
            t01 = get_bisector_coordinates(t1[0], t1[1])
            t02 = get_bisector_coordinates(t2[0], t2[1])
            cot = cotangent(t01[0], t01[1], t02[0], t02[1])
            if not flag or cot < minimum_angle:
                flag = True
                triangles = [t1, t2]
                bisectors = [t01, t02]
                minimum_angle = cot

    return triangles, bisectors, minimum_angle


def find_index(x, y, value):
    ind_x = [i for i, elem in enumerate(x) if elem == value[0]]
    ind_y = [i for i, elem in enumerate(y) if elem == value[1]]
    intersection = list(set(ind_x) & set(ind_y))
    ind = intersection[0]
    return ind + 1


def delete_pair(x, y, value):
    ind = find_index(x, y, value)
    del x[ind - 1]
    del y[ind - 1]


def change_pair(x, y, value_old, value):
    ind = find_index(x, y, value_old)
    x[ind - 1] = value[0]
    y[ind - 1] = value[1]
    return x, y
