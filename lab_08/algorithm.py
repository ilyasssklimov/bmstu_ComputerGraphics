# Алгоритм Кируса-Бека

import config as cfg
import tkinter.messagebox as mb


def get_vector(section):
    return cfg.Vector(section[1].x - section[0].x, section[1].y - section[0].y)


def vector_multiplication(vector_1, vector_2):
    return vector_1.x * vector_2.y - vector_1.y * vector_2.x


def scalar_multiplication(vector_1, vector_2):
    return vector_1.x * vector_2.x + vector_1.y * vector_2.y


def is_convex(edges):
    print(len(edges))
    if len(edges) < 3:
        return False

    first = vector_multiplication(get_vector(edges[0]), get_vector(edges[-1]))
    if first > 0:
        sign = 1
    elif first == 0:
        sign = 0
    else:
        sign = -1

    multi = []
    if not first:
        multi.append(first)

    for i in range(1, len(edges)):
        tmp = vector_multiplication(get_vector(edges[i]), get_vector(edges[i - 1]))
        if multi and not tmp:
            multi.append(tmp)

        if sign * tmp < 0:
            print(i)
            return False

    if len(multi) == len(edges):
        return False
    if sign < 0:
        edges.reverse()

    return True


def get_normal(edge_1, edge_2):
    vector = get_vector(edge_1)
    if vector.x == 0:
        normal = cfg.Vector(1, 0)
    else:
        normal = cfg.Vector(-vector.y / vector.x, 1)

    if scalar_multiplication(normal, -get_vector(edge_2)) < 0:
        normal.negative()

    return normal


def get_normals(edges):
    length = len(edges)
    normals = []
    for i in range(length):
        normals.append(get_normal(edges[i], edges[(i + 1) % length]))

    return normals


def cyrus_beck_cut(canvas, cutter, sections):
    if canvas.start and canvas.old and canvas.start != canvas.old:
        mb.showerror('Ошибка', 'Перед использованием алгоритма необходимо замкнуть область')
        return None

    if not is_convex(cutter):
        mb.showerror('Ошибка', 'Многоугольник должен быть выпуклым')
        return None

    color = canvas.frame.colors['result']
    verteces = []
    for edge in cutter:
        verteces.extend([edge[0].x, edge[0].y])
    canvas.create_polygon(*verteces, outline=canvas.frame.colors['cutter'], fill='white', tag='result')

    normals = get_normals(cutter)
    for section in sections:
        flag_break = False
        t_start, t_end = 0, 1
        d = get_vector(section)
        length = len(cutter)

        for i in range(length):
            if cutter[i][0] != section[0]:
                wi = get_vector([cutter[i][0], section[0]])
            else:
                wi = get_vector([cutter[(i + 1) % length][0], section[0]])

            dck = scalar_multiplication(d, normals[i])
            wck = scalar_multiplication(wi, normals[i])

            if dck == 0:
                if scalar_multiplication(wi, normals[i]) < 0:
                    flag_break = True
                    break
                else:
                    continue

            t = -wck / dck
            if dck > 0:
                if t > t_start:
                    t_start = t
            else:
                if t < t_end:
                    t_end = t

            if t_start > t_end:
                break

        if flag_break:
            continue

        if t_start < t_end:
            canvas.draw_line(cfg.int_n(section[0].x + d.x * t_start), cfg.int_n(section[0].y + d.y * t_start),
                             cfg.int_n(section[0].x + d.x * t_end), cfg.int_n(section[0].y + d.y * t_end),
                             color, 'result')
