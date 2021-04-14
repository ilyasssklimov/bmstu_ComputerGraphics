from algorithms import dda, bresenham_int, bresenham_float, bresenham_smooth, wu
from config import *
from efficiency import *
import tkinter as tk
from tkinter import messagebox

from picture import CanvasLines


class MainWindow(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.frame_input = tk.Frame(self)
        self.frame_config = tk.Frame(self)
        self.frame_spectrum = tk.Frame(self)
        self.frame_efficiency = tk.Frame(self)
        self.canvas = CanvasLines(self)

        self.coordinates = list()
        self.length = None
        self.angle = None
        self.length_eff = None
        self.algorithm = tk.IntVar()
        self.algorithm.set(0)
        self.color = tk.IntVar()
        self.color.set(0)

        self.add_canvas()
        self.add_input()
        self.add_choice()
        self.add_spectrum()
        self.add_efficiency()

    def add_canvas(self):
        self.canvas.grid(row=0, column=0, rowspan=20, padx=5, pady=5)

    def add_input(self):
        label_coordinates = tk.Label(self.frame_input, text='Введите координаты отрезка x и y через пробел',
                                     font='Times 13 bold', relief='groove')
        label_coordinates.grid(row=0, column=0, columnspan=8, padx=3, pady=3, sticky=tk.N)

        label_start = tk.Label(self.frame_input, text='Начало отрезка', font='Times 13 italic')
        label_start.grid(row=1, column=0, columnspan=4, sticky=tk.N)

        label_start_x = tk.Label(self.frame_input, text='X:', font='Times 13')
        label_start_x.grid(row=2, column=0, sticky=tk.W)
        entry_start_x = tk.Entry(self.frame_input, font='Times 13', width=6)
        entry_start_x.grid(row=2, column=1, sticky=tk.W)

        label_start_y = tk.Label(self.frame_input, text='Y:', font='Times 13')
        label_start_y.grid(row=2, column=2, sticky=tk.W)
        entry_start_y = tk.Entry(self.frame_input, font='Times 13', width=6)
        entry_start_y.grid(row=2, column=3, sticky=tk.W)

        label_finish = tk.Label(self.frame_input, text='Конец отрезка', font='Times 13 italic')
        label_finish.grid(row=1, column=4, columnspan=4, sticky=tk.N)

        label_finish_x = tk.Label(self.frame_input, text='X:', font='Times 13')
        label_finish_x.grid(row=2, column=4, sticky=tk.W)
        entry_finish_x = tk.Entry(self.frame_input, font='Times 13', width=6)
        entry_finish_x.grid(row=2, column=5, sticky=tk.W)

        label_finish_y = tk.Label(self.frame_input, text='Y:', font='Times 13')
        label_finish_y.grid(row=2, column=6, sticky=tk.W)
        entry_finish_y = tk.Entry(self.frame_input, font='Times 13', width=6)
        entry_finish_y.grid(row=2, column=7, sticky=tk.W)

        self.coordinates.extend([entry_start_x, entry_start_y, entry_finish_x, entry_finish_y])
        self.frame_input.grid(row=0, column=1, padx=5, pady=5, sticky=tk.N)

    def add_choice(self):
        label_algorithm = tk.Label(self.frame_config, text='Выберите алгоритм для построения отрезка',
                                   font='Times 13 bold', relief='groove')
        label_algorithm.grid(row=0, column=0, columnspan=3, padx=3, pady=1, sticky=tk.N)

        for index, algorithm in enumerate(algorithms):
            tk.Radiobutton(self.frame_config, variable=self.algorithm, value=index, text=algorithm, font='Times 13').\
                grid(row=index + 1, column=0, columnspan=3, pady=3, padx=7, sticky=tk.W)

        label_color = tk.Label(self.frame_config, text='Выберите цвет отрезка', font='Times 13 bold', relief='groove')
        label_color.grid(row=7, column=0, columnspan=3, padx=3, pady=1, sticky=tk.N)
        row = 8
        column = -1
        for index, color in enumerate(colors):
            if not index % 2:
                row = 8
                column += 1
            tk.Radiobutton(self.frame_config, variable=self.color, value=index, text=color, font='Times 13').\
                grid(row=row, column=column, pady=2, padx=7, sticky=tk.W)
            row += 1

        button_create = tk.Button(self.frame_config, text='Построить отрезок', font='Times 13',
                                  command=self.draw_line)
        button_create.grid(row=14, column=0, columnspan=3, sticky='we')

        button_clear = tk.Button(self.frame_config, text='Очистить холст', font='Times 13',
                                 command=self.canvas.clear_canvas)
        button_clear.grid(row=15, column=0, columnspan=3, pady=3, sticky='we')

        self.frame_config.grid(row=1, column=1, padx=5, pady=5, sticky=tk.N)

    def add_spectrum(self):
        label_spectrum = tk.Label(self.frame_spectrum, text='Введите угол и длину отрезков для создания\nспектра',
                                  font='Times 13 bold', relief='groove')
        label_spectrum.grid(row=0, column=0, columnspan=4, padx=3, pady=3, sticky=tk.N)

        label_angle = tk.Label(self.frame_spectrum, text='Угол:', font='Times 13')
        label_angle.grid(row=1, column=0, sticky=tk.W)
        entry_angle = tk.Entry(self.frame_spectrum, font='Times 13', width=6)
        entry_angle.grid(row=1, column=1, sticky=tk.W)

        label_length = tk.Label(self.frame_spectrum, text='Длина:', font='Times 13')
        label_length.grid(row=1, column=2, sticky=tk.W)
        entry_length = tk.Entry(self.frame_spectrum, font='Times 13', width=6)
        entry_length.grid(row=1, column=3, sticky=tk.W)

        button_spectrum = tk.Button(self.frame_spectrum, text='Создать отрезки в заданном спектре', font='Times 13',
                                    command=self.create_spectrum)
        button_spectrum.grid(row=2, column=0, columnspan=4, pady=5, sticky='we')

        self.length = entry_length
        self.angle = entry_angle
        self.frame_spectrum.grid(row=2, column=1, padx=5, pady=5, sticky=tk.N)

    def add_efficiency(self):
        label_efficiency = tk.Label(self.frame_efficiency, text='Сравнительные характеристики алгоритмов',
                                    font='Times 13 bold', relief='groove')
        label_efficiency.grid(row=0, column=0, columnspan=2, padx=3, pady=3, sticky=tk.N)

        label_length = tk.Label(self.frame_efficiency, text='Длина отрезка: ', font='Times 13')
        label_length.grid(row=1, column=0, padx=3, pady=3, sticky=tk.N)
        entry_length = tk.Entry(self.frame_efficiency, font='Times 13')
        entry_length.grid(row=1, column=1, padx=3, pady=3, sticky=tk.N)

        button_efficiency = tk.Button(self.frame_efficiency, text='Вывести гистограмму времени', font='Times 13',
                                      command=self.efficiency)
        button_efficiency.grid(row=2, column=0, columnspan=2, padx=3, pady=1, sticky='we')

        button_steps = tk.Button(self.frame_efficiency, text='График зависимости ступенчатости от длины ',
                                 font='Times 13', command=self.steps)
        button_steps.grid(row=3, column=0, columnspan=2, padx=3, pady=1, sticky='we')

        self.length_eff = entry_length
        self.frame_efficiency.grid(row=3, column=1, padx=5, pady=5, sticky=tk.N)

    def draw_line(self):
        x1 = self.coordinates[0].get()
        y1 = self.coordinates[1].get()
        x2 = self.coordinates[2].get()
        y2 = self.coordinates[3].get()
        self.canvas.draw_line((x1, y1, x2, y2), self.algorithm.get(), self.color.get())

    def create_spectrum(self):
        self.canvas.create_spectrum(self.length.get(), self.angle.get(), self.algorithm.get(), self.color.get())

    def efficiency(self):
        algorithms_compare = [dda, bresenham_float, bresenham_int, bresenham_smooth, wu]
        try:
            length = float(self.length_eff.get())
            if length <= 0:
                raise ValueError
        except ValueError:
            return messagebox.showerror('Ошибка', 'Длина отрезка должна являться положительным числом')

        compare_time(algorithms_compare, length, coeffs)

    def steps(self):
        algorithms_compare = [dda_steps, bresenham_float_steps, bresenham_int_steps, bresenham_smooth_steps, wu_steps]
        try:
            length = float(self.length_eff.get())
            if length <= 0:
                raise ValueError
        except ValueError:
            return messagebox.showerror('Ошибка', 'Длина отрезка должна являться положительным числом')

        compare_steps(algorithms_compare, length)
