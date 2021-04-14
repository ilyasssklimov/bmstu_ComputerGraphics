from math import sqrt, sin, cos, radians


def turn_x(center_x, x, center_y, y, beta):
    return float(center_x + (x - center_x) * cos(radians(beta)) + (y - center_y) * sin(radians(beta)))


def turn_y(center_x, x, center_y, y, beta):
    return float(center_y - (x - center_x) * sin(radians(beta)) + (y - center_y) * cos(radians(beta)))


def transform(center_t, kt, t):
    return float(kt * t + center_t * (1 - kt))


def body_params(center_x, center_y):
    x1 = center_x - 40
    y1 = center_y - 70
    x2 = center_x + 160
    y2 = center_y + 70
    return x1, y1, x2, y2, min(x1, x2) + abs(x2 - x1) // 2, min(y1, y2) + abs(y2 - y1) // 2


def head_params(center_x, center_y):
    x1 = center_x - 120
    y1 = center_y - 40
    x2 = center_x - 40
    y2 = center_y + 40
    return x1, y1, x2, y2, min(x1, x2) + abs(x2 - x1) // 2, min(y1, y2) + abs(y2 - y1) // 2


def eye_left_params(center_x, center_y):
    x1 = center_x - 100
    y1 = center_y - 20
    x2 = center_x - 90
    y2 = center_y - 10
    return x1, y1, x2, y2, min(x1, x2) + abs(x2 - x1) // 2, min(y1, y2) + abs(y2 - y1) // 2


def eye_right_params(center_x, center_y):
    x1 = center_x - 75
    y1 = center_y - 20
    x2 = center_x - 65
    y2 = center_y - 10
    return x1, y1, x2, y2, min(x1, x2) + abs(x2 - x1) // 2, min(y1, y2) + abs(y2 - y1) // 2


def solve_equation_oval(a, b, x, x_center, y_center):
    y_quadratic = (1 - (x - x_center) ** 2 / a ** 2) * b ** 2
    try:
        return (x, sqrt(y_quadratic) + y_center), (x, -sqrt(y_quadratic) + y_center)
    except ValueError:
        return None


def get_oval_point(x1, y1, x2, y2, x_center, y_center):
    a = abs(x2 - x1) / 2
    b = abs(y2 - y1) / 2
    coordinates_tuples = []
    coordinates = []
    for x in range(x1, x2 + 1, 1):
        result = solve_equation_oval(a, b, x, x_center, y_center)
        if result:
            coordinates_tuples.extend(result)

    coordinates_tuples = coordinates_tuples[::2] + list(reversed(coordinates_tuples[1::2]))

    for coordinate in coordinates_tuples:
        coordinates.append(coordinate[0])
        coordinates.append(coordinate[1])

    return coordinates

