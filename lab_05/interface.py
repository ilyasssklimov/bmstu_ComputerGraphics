import canvas as cv
import config as cfg
from config import FONT, FONT_BOLD, WIDTH, PADX, PADY
import tkinter as tk


class MainWindowClass(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.canvas = cv.Canvas(self)
        self.add_canvas()

        self.frame_color = tk.Frame(self)
        self.color = tk.IntVar()
        self.color.set(0)
        self.add_color()

        self.frame_buttons = tk.Frame(self)
        self.add_buttons()

    def add_canvas(self):
        self.canvas.grid(row=0, column=0, rowspan=2, padx=5, pady=5)

    def add_color(self):
        cfg.create_label(self.frame_color, 'Выберите цвет', FONT_BOLD, 0, 0, PADX, PADY, tk.N, 'groove')
        for i, color in enumerate(cfg.colors):
            cfg.create_radiobutton(self.frame_color, self.color, i, color, FONT, i + 1, 0, PADX, 0, 'WN')
        cfg.create_button(self.frame_color, 'Поменять цвет', FONT, 7, 0, PADX, 0, 1, 'WE', self.change_color)
        cfg.create_label(self.frame_color, '(Холст будет очищен)', 'Times 10', 8, 0, PADX, 0, tk.N)
        self.frame_color.grid(row=0, column=1, padx=5, pady=5, sticky=tk.N)

    def add_buttons(self):
        cfg.create_button(self.frame_buttons, 'Замкнуть линию', FONT, 0, 0, PADX, PADY, 1, 'WE', self.canvas.end_draw)
        cfg.create_button(self.frame_buttons, 'Очистить холст', FONT, 1, 0, PADX, PADY, 1, 'WE', self.canvas.delete_all)
        self.frame_buttons.grid(row=1, column=1, padx=5, pady=5, sticky=tk.N)

    def change_color(self):
        color = self.color.get()
        self.canvas.color = list(cfg.colors.values())[color]
        self.canvas.delete_all()
