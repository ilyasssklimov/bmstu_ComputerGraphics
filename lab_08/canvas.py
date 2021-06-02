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

        self.start = cfg.Point(exist=False)
        self.old = cfg.Point(exist=False)
        self.section_1 = cfg.Point(exist=False)
        self.section_2 = cfg.Point(exist=False)

        self.color = 'black'

        super().__init__(self.frame, width=self.width, height=self.height, bg='white', highlightbackground='black')
        self.bind('<ButtonPress-1>', self.draw_section)
        self.bind('<ButtonPress-3>', self.draw_cutter)

    def draw_line(self, x1, y1, x2, y2, color, tag=None):
        self.create_line(x1, y1, x2, y2, fill=color, tag=tag)

    def draw_cutter(self, event):
        color = self.frame.colors['cutter']
        event_x, event_y = cfg.int_n(event.x), cfg.int_n(event.y)
        if not self.start:
            self.delete('cutter')
            self.delete('result')
            self.frame.cutter = []
            self.draw_line(event_x, event_y, event_x + 1, event_y, self.color, 'cutter')
            self.start = cfg.Point(event_x, event_y, color)
            self.old = cfg.Point(event_x, event_y, color)
        else:
            try:
                if event.state in cfg.Ctrl:
                    if event_x == self.old.x:
                        m = 0
                    else:
                        m = abs(event_y - self.old.y) / abs(event_x - self.old.x)
                    if m < math.tan(math.pi / 4):
                        new_point = cfg.Point(event_x, self.old.y, color)
                    else:
                        new_point = cfg.Point(self.old.x, event_y, color)
                else:
                    raise AttributeError
            except AttributeError:
                new_point = cfg.Point(event_x, event_y, color)

            self.draw_line(self.old.x, self.old.y, new_point.x, new_point.y, color, 'cutter')
            self.frame.cutter.append([self.old, new_point])
            self.old = new_point

    def end_cutter(self):
        if self.start and self.old:
            color = self.frame.colors['cutter']
            self.frame.cutter.append((self.old, self.start))
            self.draw_line(self.old.x, self.old.y, self.start.x, self.start.y, color, 'cutter')
            self.start = cfg.Point(exist=False)
            self.old = cfg.Point(exist=False)

    def draw_section(self, event):
        event_x, event_y = cfg.int_n(event.x), cfg.int_n(event.y)
        color = self.frame.colors['section']
        if not self.section_1:
            self.section_1.set(event_x, event_y, color)
        else:
            if event.state not in cfg.Ctrl:
                self.section_2.set(event_x, event_y, color)

            else:
                if event_x == self.section_1.x:
                    m = 0
                else:
                    m = abs(event_y - self.section_1.y) / abs(event_x - self.section_1.x)
                if m < math.tan(math.pi / 4):
                    self.section_2.set(event_x, self.section_1.y, color)
                else:
                    self.section_2.set(self.section_1.x, event_y, color)

            self.draw_line(self.section_1.x, self.section_1.y, self.section_2.x, self.section_2.y, color)
            self.frame.section.append([self.section_1, self.section_2])
            self.section_1 = cfg.Point(exist=False)
            self.section_2 = cfg.Point(exist=False)

    def delete_all(self):
        self.delete('all')
        self.frame.section = []
        self.frame.cutter = []
        self.start.clear()
        self.old.clear()
        self.section_1.clear()
        self.section_2.clear()
