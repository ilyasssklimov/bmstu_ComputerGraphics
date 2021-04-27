import config as cfg
import tkinter as tk


class Canvas(tk.Canvas):
    def __init__(self, frame):
        self.frame = frame
        self.width = cfg.CANVAS_WIDTH
        self.height = cfg.CANVAS_HEIGHT
        self.first = cfg.Point(exist=False)
        self.old = cfg.Point(exist=False)
        self.color = 'black'

        super().__init__(self.frame, width=self.width, height=self.height, bg='white', highlightbackground='black')

        self.bind('<ButtonPress-1>', self.draw_line)

    def restart(self):
        self.first = self.old = cfg.Point(exist=False)

    def draw_line(self, event):
        if not self.first:
            self.create_line(event.x, event.y, event.x + 1, event.y, fill=self.color)
            self.first = cfg.Point(event.x, event.y, self.color)
            self.old = cfg.Point(event.x, event.y, self.color)
        else:
            self.create_line(self.old.x, self.old.y, event.x, event.y, fill=self.color)
            self.old = cfg.Point(event.x, event.y, self.color)

    def end_draw(self):
        if self.first and self.old:
            self.create_line(self.old.x, self.old.y, self.first.x, self.first.y, fill=self.color)
            self.restart()

    def delete_all(self):
        self.delete('all')
        self.restart()
