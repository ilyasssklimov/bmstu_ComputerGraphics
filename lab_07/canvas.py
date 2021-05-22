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

        self.cutter_1 = cfg.Point(exist=False)
        self.cutter_2 = cfg.Point(exist=False)
        self.section_1 = cfg.Point(exist=False)
        self.section_2 = cfg.Point(exist=False)

        self.color = 'black'
        self.edges = []

        super().__init__(self.frame, width=self.width, height=self.height, bg='white', highlightbackground='black')
        self.bind('<ButtonPress-1>', self.draw_section)
        self.bind('<ButtonPress-3>', self.draw_cutter)

    def draw_line(self, x1, y1, x2, y2, color, tag=None):
        self.create_line(x1, y1, x2, y2, fill=color, tag=tag)

    def draw_rectangle(self, start, finish, color, tag=None):
        x1, y1, x2, y2 = start.x, start.y, finish.x, finish.y

        self.draw_line(x1, y1, x1, y2, color, tag=tag)
        self.draw_line(x1, y2, x2, y2, color, tag=tag)
        self.draw_line(x2, y2, x2, y1, color, tag=tag)
        self.draw_line(x2, y1, x1, y1, color, tag=tag)

        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1

        self.frame.cutter['left'] = x1
        self.frame.cutter['bottom'] = y1
        self.frame.cutter['right'] = x2
        self.frame.cutter['top'] = y2

    def draw_cutter(self, event):
        color = self.frame.colors['cutter']
        if not self.cutter_1:
            self.cutter_1.set(cfg.int_n(event.x), cfg.int_n(event.y), color)
        else:
            self.cutter_2.set(cfg.int_n(event.x), cfg.int_n(event.y), color)
            self.delete('cutter')
            self.delete('result')
            self.draw_rectangle(self.cutter_1, self.cutter_2, color, tag='cutter')
            self.cutter_1.clear()
            self.cutter_2.clear()

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
        self.cutter_1.clear()
        self.cutter_2.clear()
        self.section_1.clear()
        self.section_2.clear()
