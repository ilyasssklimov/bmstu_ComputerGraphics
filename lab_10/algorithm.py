import lab_10.config as cfg
from math import sin, cos


def get_funcs():
    funcs = [lambda x, z: sin(x) * sin(z), lambda x, z: sin(cos(x)) * sin(z), lambda x, z: cos(x) * z / 3]

    return funcs


def is_visible(point):
    return 0 <= point[0] < 900 and 0 <= point[1] < 750


'''
def draw_section(xb, yb, xe, ye, color):
    canvas.create_line(xb, yb, xe, ye, fill=color)


def rotate_trans_matrix(rotate_matrix):
    global trans_matrix
    res_matrix = [[0 for i in range(4)] for j in range(4)]

    for i in range(4):
        for j in range(4):
            for k in range(4):
                res_matrix[i][j] += trans_matrix[i][k] * rotate_matrix[k][j]

    trans_matrix = res_matrix


def trans_point(point):
    # point = (x, y, z)
    point.append(1) # (x, y, z, 1)
    res_point = [0, 0, 0, 0]
    for i in range(4):
        for j in range(4):
            res_point[i] += point[j] * trans_matrix[j][i]

    for i in range(3):
        res_point[i] *= sf # x, y, z ==> SF * x, SF * y, SF * z

    res_point[0] += cfg.FIELD_WIDTH / 2
    res_point[1] += cfg.FIELD_HEIGHT / 2

    return res_point[:3]


def rotate_x():
    value = float(x_entry.get()) / 180 * pi
    rotate_matrix = [ [ 1, 0, 0, 0 ],
                       [ 0, cos(value), sin(value), 0 ],
                       [ 0, -sin(value), cos(value), 0 ],
                       [ 0, 0, 0, 1 ] ]
    rotate_trans_matrix(rotate_matrix)
    solve()


def rotate_y():
    value = float(y_entry.get()) / 180 * pi
    rotate_matrix = [ [ cos(value), 0, -sin(value), 0 ],
                       [ 0, 1, 0, 0 ],
                       [ sin(value), 0, cos(value), 0 ],
                       [ 0, 0, 0, 1 ] ]
    rotate_trans_matrix(rotate_matrix)
    solve()


def rotate_z():
    value = float(z_entry.get()) / 180 * pi
    rotate_matrix = [ [ cos(value), sin(value), 0, 0 ],
                       [ -sin(value), cos(value), 0, 0 ],
                       [ 0, 0, 1, 0 ],
                       [ 0, 0, 0, 1 ] ]
    rotate_trans_matrix(rotate_matrix)
    solve()


def set_sf():
    global sf
    sf = float(scale_entry.get())
    solve()

def set_meta():
    global x_from, x_step, x_to, z_from, z_step, z_to
    x_from = float(xfrom_entry.get())
    x_to = float(xto_entry.get())
    x_step = float(xstep_entry.get())
    z_from = float(zfrom_entry.get())
    z_to = float(zto_entry.get())
    z_step = float(zstep_entry.get())
    solve()




def is_visible(point):
    return 0 <= point[0] < cfg.FIELD_WIDTH and 0 <= point[1] < cfg.FIELD_HEIGHT


def draw_point(x, y, hh, lh):
    if not is_visible([x, y]):
        return False

    if y > hh[x]:
        hh[x] = y
        draw_pixel(x, y)

    elif y < lh[x]:
        lh[x] = y
        draw_pixel(x, y)

    return True


def draw_horizon_part(p1, p2, hh, lh):
    if p1[0] > p2[0]: # хочу, чтобы x2 > x1
        p1, p2 = p2, p1

    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    l = dx if dx > dy else dy
    dx /= l
    dy /= l

    x, y = p1[0], p1[1]

    for _ in range(int(l) + 1):
        if not draw_point(int(round(x)), y, hh, lh):
            return
        x += dx
        y += dy


def draw_horizon(func, hh, lh, fr, to, step, z):
    f = lambda x: func(x, z) # f = f(x, z=const)
    prev = None
    for x in arange(fr, to + step, step):
        # x, z, f(x, z=const)
        current = trans_point([x, f(x), z]) # transformed: Повернуть, масштабировать и сдвинуть в центр экрана
        if prev: # Если это не первая точка (то есть если есть предыдущая)
            draw_horizon_part(prev, current, hh, lh)
        prev = current


def solve():
    clear_canvas()
    f = funcs[func_var.get()]
    high_horizon = [0 for i in range(cfg.FIELD_WIDTH)]
    low_horizon = [cfg.FIELD_HEIGHT for i in range(cfg.FIELD_WIDTH)]

    for z in arange(z_from, z_to + z_step, z_step):
        draw_horizon(f, high_horizon, low_horizon, x_from, x_to, x_step, z)

    for z in arange(z_from, z_to, z_step):
        p1 = trans_point([x_from, f(x_from, z), z])
        p2 = trans_point([x_from, f(x_from, z + z_step), z + z_step])
        canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill=color)
        p1 = trans_point([x_to, f(x_to, z), z])
        p2 = trans_point([x_to, f(x_to, z + z_step), z + z_step])
        canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill=color)

'''