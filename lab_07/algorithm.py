import config as cfg
import time

# Простой алгоритм отсечения

MASK_LEFT = 0b0001
MASK_RIGHT = 0b0010
MASK_BOTTOM = 0b0100
MASK_TOP = 0b1000


def find_vertical(section, index, cutter):
    if section[index].y > cutter['top']:
        return [section[index].x, cutter['top']]
    elif section[index].y < cutter['bottom']:
        return [section[index].x, cutter['bottom']]
    else:
        return section[index]


def set_codes(point, cutter):
    code = 0b0000
    if point.x < cutter['left']:
        code += MASK_LEFT
    if point.x > cutter['right']:
        code += MASK_RIGHT
    if point.y < cutter['bottom']:
        code += MASK_BOTTOM
    if point.y > cutter['top']:
        code += MASK_TOP

    return code


def cut_simple(canvas, cutter, sections):
    color = canvas.frame.colors['result']
    canvas.create_rectangle(cutter['left'], cutter['bottom'], cutter['right'], cutter['top'], fill='white', tag='result')
    start = time.time()
    for section in sections:
        s = []

        for point in section:
            s.append(set_codes(point, cutter))

        if s[0] == 0 and s[1] == 0:
            canvas.draw_line(section[0].x, section[0].y, section[1].x, section[1].y, color, 'result')
            continue

        if s[0] & s[1]:
            continue

        cur_index = 0
        result = []

        if s[0] == 0:
            cur_index = 1
            result.append([section[0].x, section[0].y])
        elif s[1] == 0:
            result.append([section[1].x, section[1].y])
            cur_index = 1
            section.reverse()
            s.reverse()

        while cur_index < 2:
            if section[0].x == section[1].x:
                result.append(find_vertical(section, cur_index, cutter))
                cur_index += 1
                continue

            m = (section[1].y - section[0].y) / (section[1].x - section[0].x)

            if s[cur_index] & MASK_LEFT:
                y = cfg.int_n(m * (cutter['left'] - section[cur_index].x) + section[cur_index].y)
                if cutter['top'] >= y >= cutter['bottom']:
                    result.append([cutter['left'], y])
                    cur_index += 1
                    continue

            elif s[cur_index] & MASK_RIGHT:
                y = cfg.int_n(m * (cutter['right'] - section[cur_index].x) + section[cur_index].y)
                if cutter['top'] >= y >= cutter['bottom']:
                    result.append([cutter['right'], y])
                    cur_index += 1
                    continue

            if m == 0:
                cur_index += 1
                continue

            if s[cur_index] & MASK_TOP:
                x = cfg.int_n((cutter['top'] - section[cur_index].y) / m + section[cur_index].x)
                if cutter['right'] >= x >= cutter['left']:
                    result.append([x, cutter['top']])
                    cur_index += 1
                    continue

            elif s[cur_index] & MASK_BOTTOM:
                x = cfg.int_n((cutter['bottom'] - section[cur_index].y) / m + section[cur_index].x)
                if cutter['right'] >= x >= cutter['left']:
                    result.append([x, cutter['bottom']])
                    cur_index += 1
                    continue

            cur_index += 1

        if result:
            canvas.draw_line(cfg.int_n(result[0][0]), cfg.int_n(result[0][1]),
                             cfg.int_n(result[1][0]), cfg.int_n(result[1][1]), color, 'result')

    return time.time() - start
