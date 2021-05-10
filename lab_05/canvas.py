import algorithm as alg
import config as cfg
import math
import time
import tkinter as tk


class Canvas(tk.Canvas):
    def __init__(self, frame):
        self.frame = frame
        self.width = cfg.CANVAS_WIDTH
        self.height = cfg.CANVAS_HEIGHT
        self.first = cfg.Point(exist=False)
        self.old = cfg.Point(exist=False)
        self.color = 'black'
        self.edges = []

        super().__init__(self.frame, width=self.width, height=self.height, bg='white', highlightbackground='black')
        self.bind('<ButtonPress-1>', self.draw_line)

    def set_pixel(self, point):
        # self.create_rectangle((point.x, point.y) * 2, outline='', fill=point.color)
        self.frame.img.put(point.color, (point.x, point.y))

    def restart(self):
        self.first = cfg.Point(exist=False)
        self.old = cfg.Point(exist=False)

    def draw_line(self, event):
        event_x, event_y = cfg.int_n(event.x), cfg.int_n(event.y)
        if not self.first:
            # self.create_line(event_x, event_y, event_x + 1, event_y, fill=self.color)
            self.set_pixel(cfg.Point(event_x, event_y, self.color))
            self.first = cfg.Point(event_x, event_y, self.color)
            self.old = cfg.Point(event_x, event_y, self.color)
        else:
            try:
                if event.state in cfg.Ctrl:
                    if event_x == self.old.x:
                        m = 0
                    else:
                        m = abs(event_y - self.old.y) / abs(event_x - self.old.x)
                    if m < math.tan(math.pi / 4):
                        new_point = cfg.Point(event_x, self.old.y, self.color)
                    else:
                        new_point = cfg.Point(self.old.x, event_y, self.color)
                else:
                    raise AttributeError
            except AttributeError:
                new_point = cfg.Point(event_x, event_y, self.color)

            self.create_line(self.old.x, self.old.y, new_point.x, new_point.y, fill=self.color)
            # alg.bresenham_int(self, self.old, new_point)
            self.edges.append((self.old, new_point))
            self.old = new_point

    def end_draw(self):
        if self.first and self.old:
            self.edges.append((self.old, self.first))
            # alg.bresenham_int(self, self.old, self.first)
            self.create_line(self.old.x, self.old.y, self.first.x, self.first.y, fill=self.color)
            # self.frame.img.put('black', (2, 2), (100, 100))
            self.restart()

    def delete_all(self):
        self.delete('all')
        self.frame.add_image()
        self.edges = []
        self.restart()

    def inverse_pixel(self, x, y, point_color):
        # s = time.time()
        # print(f'color {x}, {y} from {point_color} to inverse')
        color = alg.get_color(self, x, y)
        # print(x, y, color)
        if color == cfg.WHITE_COLOR:
            self.set_pixel(cfg.Point(x, y, point_color))
        else:
            self.set_pixel(cfg.Point(x, y, 'white'))

        # print(f'time = {time.time() - s}')
