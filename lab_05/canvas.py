import algorithm as alg
import config as cfg
import math
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
        self.create_rectangle((point.x, point.y) * 2, outline='', fill=point.color)

    def restart(self):
        self.first = cfg.Point(exist=False)
        self.old = cfg.Point(exist=False)

    def draw_line(self, event):
        print(str(self.old))
        if not self.first:
            self.create_line(event.x, event.y, event.x + 1, event.y, fill=self.color)
            self.first = cfg.Point(event.x, event.y, self.color)
            self.old = cfg.Point(event.x, event.y, self.color)
        else:
            try:
                if event.state == cfg.Ctrl:
                    if event.x == self.old.x:
                        m = 0
                    else:
                        m = abs(event.y - self.old.y) / abs(event.x - self.old.x)
                    if m < math.tan(math.pi / 4):
                        new_point = cfg.Point(event.x, self.old.y)
                    else:
                        new_point = cfg.Point(self.old.x, event.y)
                else:
                    raise AttributeError
                    # new_point = cfg.Point(event.x, event.y)
            except AttributeError:
                print('Tut')
                new_point = cfg.Point(event.x, event.y)

            self.create_line(self.old.x, self.old.y, new_point.x, new_point.y, fill=self.color)
            print(f'old = {str(self.old)}, new = {str(new_point)}')
            self.edges.append((self.old, cfg.Point(new_point.x, new_point.y, self.color)))
            self.old = cfg.Point(new_point.x, new_point.y, self.color)

    def end_draw(self):
        if self.first and self.old:
            self.edges.append((self.old, self.first))
            self.create_line(self.old.x, self.old.y, self.first.x, self.first.y, fill=self.color)
            print(f'old = {str(self.old)}, new = {str(self.first)}')
            self.restart()

    def delete_all(self):
        self.delete('all')
        self.restart()

    def reverse_pixel(self, x, y, point_color):
        color = alg.get_color(x, y)
        if color == cfg.WHITE_COLOR:
            self.set_pixel(cfg.Point(x, y, point_color))
        else:
            self.set_pixel(cfg.Point(x, y, 'white'))
