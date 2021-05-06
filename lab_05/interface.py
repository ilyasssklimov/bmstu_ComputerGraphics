import algorithm as alg
import canvas as cv
import config as cfg
from config import FONT, FONT_BOLD, WIDTH, PADX, PADY
import tkinter as tk
import tkinter.messagebox as mb
import PIL
from PIL import ImageTk


class MainWindowClass(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.canvas = cv.Canvas(self)
        self.add_canvas()

        self.img = None
        self.add_image()

        self.frame_input = tk.Frame(self)
        self.coors = None
        self.add_input()

        self.frame_color = tk.Frame(self)
        self.color = tk.IntVar()
        self.color.set(0)
        self.add_color()

        self.frame_buttons = tk.Frame(self)
        self.mode = tk.IntVar()
        self.mode.set(0)
        self.add_buttons()

    def add_canvas(self):
        self.canvas.grid(row=0, column=0, rowspan=3, padx=5, pady=5)

    def add_image(self):
        self.img = tk.PhotoImage(width=self.canvas.width, height=self.canvas.height, file='img/bg.png')
        self.canvas.create_image((self.canvas.width / 2, self.canvas.height / 2), image=self.img, state='normal')

    def add_input(self):
        text = 'Введите координаты\nдля следующей\nточки через пробел\n(либо сделайте\nэто мышью)'
        cfg.create_label(self.frame_input, text, FONT_BOLD, 0, 0, PADX, PADY, tk.N, 'groove')
        entry_coors = cfg.create_entry(self.frame_input, FONT, 1, 0, PADX, PADY, tk.N)
        cfg.create_button(self.frame_input, 'Добавить', FONT, 2, 0, PADX, PADY, 1, 'WE', self.draw_point)
        self.coors = entry_coors
        self.frame_input.grid(row=0, column=1, padx=5, pady=5, sticky=tk.N)

    def add_color(self):
        cfg.create_label(self.frame_color, 'Выберите цвет', FONT_BOLD, 0, 0, PADX, PADY, tk.N, 'groove')
        for i, color in enumerate(cfg.colors):
            cfg.create_radiobutton(self.frame_color, self.color, i, color, FONT, i + 1, 0, PADX, 0, 'WN')
        cfg.create_button(self.frame_color, 'Поменять цвет', FONT, 7, 0, PADX, 0, 1, 'WE', self.change_color)
        cfg.create_label(self.frame_color, '(Холст будет очищен)', 'Times 10', 8, 0, PADX, 0, tk.N)
        self.frame_color.grid(row=1, column=1, padx=5, pady=5, sticky=tk.N)

    def add_buttons(self):
        cfg.create_button(self.frame_buttons, 'Замкнуть фигуру', FONT, 0, 0, PADX, PADY, 1, 'WE', self.canvas.end_draw)
        cfg.create_button(self.frame_buttons, 'Очистить холст', FONT, 1, 0, PADX, PADY, 1, 'WE', self.canvas.delete_all)
        cfg.create_button(self.frame_buttons, 'Закрасить фигуру', FONT, 2, 0, PADX, PADY, 1, 'WE',
                          lambda: alg.algorithm_partition(self.canvas, False if self.mode.get() == 0 else True))

        cfg.create_radiobutton(self.frame_buttons, self.mode, 0, 'Без задержки', FONT, 3, 0, PADX, PADY, 'WN')
        cfg.create_radiobutton(self.frame_buttons, self.mode, 1, 'C задержкой', FONT, 4, 0, PADX, PADY, 'WN')

        self.frame_buttons.grid(row=2, column=1, padx=5, pady=5, sticky=tk.N)

    def change_color(self):
        color = self.color.get()
        self.canvas.color = list(cfg.colors.values())[color]
        self.canvas.delete_all()

    def draw_point(self):
        coors = self.coors.get().split()
        try:
            for i in range(0, len(coors), 2):
                color = self.color.get()
                self.canvas.color = list(cfg.colors.values())[color]
                point = cfg.Point(float(coors[i]), float(coors[i + 1]), color)
                self.canvas.draw_line(point)
                self.coors.insert(0, '')
        except ValueError:
            mb.showerror('Ошибка', 'Каждая координата должна быть числом')
        except IndexError:
            mb.showerror('Ошибка', 'Количество координат должно быть больше нуля и четным числом')
