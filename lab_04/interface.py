from canvas import CanvasCirclesClass
from config import *
from data import algorithms, colors
import tkinter as tk
from tkinter import ttk


class FrameInput(tk.Frame):
    def __init__(self, root, figure):
        super().__init__(root)

        self.figure = figure
        self.data = []

        self.add_input()

    def add_input(self):
        if self.figure == 'circle':
            label_center_circle = tk.Label(self, text='Окружность: центр и радиус', font=FONT_BOLD,
                                           relief='groove')
            label_center_circle.grid(row=0, column=0, columnspan=6, padx=PADX, pady=PADY, sticky=tk.N)

            label_circle_x = tk.Label(self, text='X: ', font=FONT)
            label_circle_x.grid(row=1, column=0, sticky=tk.N)
            entry_circle_x = tk.Entry(self, font=FONT, width=WIDTH)
            entry_circle_x.grid(row=1, column=1, padx=1, sticky=tk.N)
            entry_circle_x.insert(0, '350')

            label_circle_y = tk.Label(self, text='Y: ', font=FONT)
            label_circle_y.grid(row=1, column=2, sticky=tk.N)
            entry_circle_y = tk.Entry(self, font=FONT, width=WIDTH)
            entry_circle_y.grid(row=1, column=3, padx=1, sticky=tk.N)
            entry_circle_y.insert(0, '350')

            label_circle_r = tk.Label(self, text='R: ', font=FONT)
            label_circle_r.grid(row=1, column=4, sticky=tk.N)
            entry_circle_r = tk.Entry(self, font=FONT, width=WIDTH)
            entry_circle_r.grid(row=1, column=5, padx=1, sticky=tk.N)
            entry_circle_r.insert(0, '150')

            self.data = [entry_circle_x, entry_circle_y, entry_circle_r]
            self.grid(row=0, column=1, padx=5, pady=5, sticky=tk.N)

        elif self.figure == 'ellipse':
            label_center_ellipse = tk.Label(self, text='Эллипс: центр и полуоси', font=FONT_BOLD, relief='groove')
            label_center_ellipse.grid(row=0, column=0, columnspan=8, padx=PADX, pady=PADY, sticky=tk.N)

            label_ellipse_x = tk.Label(self, text='X: ', font=FONT)
            label_ellipse_x.grid(row=1, column=0, sticky=tk.N)
            entry_ellipse_x = tk.Entry(self, font=FONT, width=WIDTH)
            entry_ellipse_x.grid(row=1, column=1, padx=1, sticky=tk.N)
            entry_ellipse_x.insert(0, '350')

            label_ellipse_y = tk.Label(self, text='Y: ', font=FONT)
            label_ellipse_y.grid(row=1, column=2, sticky=tk.N)
            entry_ellipse_y = tk.Entry(self, font=FONT, width=WIDTH)
            entry_ellipse_y.grid(row=1, column=3, padx=1, sticky=tk.N)
            entry_ellipse_y.insert(0, '350')

            label_ellipse_a = tk.Label(self, text='a: ', font=FONT)
            label_ellipse_a.grid(row=1, column=4, sticky=tk.N)
            entry_ellipse_a = tk.Entry(self, font=FONT, width=WIDTH)
            entry_ellipse_a.grid(row=1, column=5, padx=1, sticky=tk.N)
            entry_ellipse_a.insert(0, '150')

            label_ellipse_b = tk.Label(self, text='b: ', font=FONT)
            label_ellipse_b.grid(row=1, column=6, sticky=tk.N)
            entry_ellipse_b = tk.Entry(self, font=FONT, width=WIDTH)
            entry_ellipse_b.grid(row=1, column=7, padx=1, sticky=tk.N)
            entry_ellipse_b.insert(0, '150')

            self.data = [entry_ellipse_x, entry_ellipse_y, entry_ellipse_a, entry_ellipse_b]
            self.grid(row=0, column=3, padx=5, pady=5, sticky=tk.N)


class ChoiceFrame(tk.Frame):
    def __init__(self, root, figure):
        super().__init__(root)

        self.root = root
        self.figure = figure

        self.algorithm = tk.IntVar()
        self.algorithm.set(0)
        self.color = tk.IntVar()
        self.color.set(0)

        self.add_choice()

    def add_choice(self):
        column_figure = 0
        if self.figure == 'ellipse':
            column_figure = 1

        label_algorithm_circle = tk.Label(self, text='Выберите способ построения', font=FONT_BOLD,
                                          relief='groove')
        label_algorithm_circle.grid(row=0, column=column_figure, columnspan=3, padx=PADX, pady=PADY, sticky=tk.N)

        for index, algorithm in enumerate(algorithms):
            tk.Radiobutton(self, variable=self.algorithm, value=index, text=algorithm, font=FONT).grid(
                row=index + 1, column=column_figure, columnspan=3, padx=PADX, sticky='wn')

        label_color_circle = tk.Label(self, text='Выберите цвет', font=FONT_BOLD, relief='groove')
        label_color_circle.grid(row=6, column=column_figure, columnspan=3, padx=PADX, pady=PADY, sticky=tk.N)

        row, column = 7, column_figure - 1
        for index, color in enumerate(colors):
            if not index % 2:
                row = 7
                column += 1
            tk.Radiobutton(self, variable=self.color, value=index, text=color, font=FONT).grid(
                row=row, column=column, padx=PADX + 2, sticky='wn')
            row += 1

        if self.figure == 'circle':
            button_create_circle = tk.Button(self, text='Построить окружность', font=FONT,
                                             command=lambda: self.root.create_figure(self.figure))
            button_create_circle.grid(row=9, column=column_figure, columnspan=3, sticky='wen')
            self.grid(row=2, column=1, padx=PADX, pady=PADY, sticky=tk.N)
        elif self.figure == 'ellipse':
            button_create_ellipse = tk.Button(self, text='Построить эллипс', font=FONT,
                                              command=lambda: self.root.create_figure(self.figure))
            button_create_ellipse.grid(row=9, column=column_figure, columnspan=3, sticky='wen')
            self.grid(row=2, column=3, padx=PADX, pady=PADY, sticky=tk.N)


class SpectrumFrame(tk.Frame):
    def __init__(self, root, figure):
        super().__init__(root)

        self.root = root
        self.figure = figure

        self.choice_axis = tk.IntVar()
        self.choice_axis.set(0)

        self.data = []

        self.add_spectrum()

    def add_spectrum(self):
        column_figure = 0
        if self.figure == 'circle':
            column_figure = 0
            label_center_circle = tk.Label(self, text='Построение спектра окружностой', font=FONT_BOLD, relief='groove')
            label_center_circle.grid(row=0, column=column_figure, columnspan=6, padx=3, pady=3, sticky=tk.N)
        elif self.figure == 'ellipse':
            column_figure = 2
            label_center_circle = tk.Label(self, text='Построение спектра эллипсов', font=FONT_BOLD, relief='groove')
            label_center_circle.grid(row=0, column=column_figure, columnspan=6, padx=3, pady=3, sticky=tk.N)

        label_spectrum_x = tk.Label(self, text='X:', font=FONT)
        label_spectrum_x.grid(row=1, column=column_figure, sticky=tk.N)
        entry_spectrum_x = tk.Entry(self, font=FONT, width=WIDTH)
        entry_spectrum_x.grid(row=1, column=column_figure + 1, padx=1, sticky=tk.N)

        label_spectrum_y = tk.Label(self, text='Y:', font=FONT)
        label_spectrum_y.grid(row=1, column=column_figure + 2, sticky=tk.N)
        entry_spectrum_y = tk.Entry(self, font=FONT, width=WIDTH)
        entry_spectrum_y.grid(row=1, column=column_figure + 3, padx=1, sticky=tk.N)

        label_spectrum_n = tk.Label(self, text='n:', font=FONT)
        label_spectrum_n.grid(row=1, column=column_figure + 4, sticky=tk.N)
        entry_spectrum_n = tk.Entry(self, font=FONT, width=WIDTH)
        entry_spectrum_n.grid(row=1, column=column_figure + 5, padx=1, sticky=tk.N)

        if self.figure == 'circle':
            label_spectrum_r_start = tk.Label(self, text='R1: ', font=FONT)
            label_spectrum_r_start.grid(row=2, column=column_figure, sticky=tk.N)
            entry_spectrum_r_start = tk.Entry(self, font=FONT, width=WIDTH + 2)
            entry_spectrum_r_start.grid(row=2, column=column_figure + 1, columnspan=2, padx=1, sticky=tk.N)

            label_spectrum_r_finish = tk.Label(self, text='R2: ', font=FONT)
            label_spectrum_r_finish.grid(row=2, column=column_figure + 3, sticky=tk.N)
            entry_spectrum_r_finish = tk.Entry(self, font=FONT, width=WIDTH + 2)
            entry_spectrum_r_finish.grid(row=2, column=column_figure + 4, columnspan=2, padx=1, sticky=tk.N)

            button_create_spectrum = tk.Button(self, text='Построить спектр', font=FONT,
                                               command= lambda: self.root.create_spectrum(self.figure))
            button_create_spectrum.grid(row=3, column=column_figure, padx=3, pady=3, columnspan=6, sticky='wen')
            self.data = [entry_spectrum_x, entry_spectrum_y, entry_spectrum_n,
                         entry_spectrum_r_start, entry_spectrum_r_finish]
            self.grid(row=4, column=1, padx=5, pady=5, sticky=tk.N)
        elif self.figure == 'ellipse':
            tk.Radiobutton(self, variable=self.choice_axis, value=0, text='').grid(row=4, column=0,
                                                                                   padx=1, pady=2, sticky=tk.W)
            label_spectrum_a1 = tk.Label(self, text='a1: ', font=FONT)
            label_spectrum_a1.grid(row=4, column=column_figure, padx=3, pady=3, sticky='en')
            entry_spectrum_a1 = tk.Entry(self, font=FONT, width=WIDTH + 2)
            entry_spectrum_a1.grid(row=4, column=column_figure + 1, columnspan=2, padx=3, pady=3, sticky=tk.N)

            label_spectrum_b1 = tk.Label(self, text='b1: ', font=FONT)
            label_spectrum_b1.grid(row=4, column=column_figure + 3, padx=3, pady=3, sticky=tk.N)
            entry_spectrum_b1 = tk.Entry(self, font=FONT, width=WIDTH + 2)
            entry_spectrum_b1.grid(row=4, column=column_figure + 4, columnspan=2, padx=3, pady=3, sticky=tk.N)

            tk.Radiobutton(self, variable=self.choice_axis, value=1, text='').grid(row=5, column=0,
                                                                                   padx=1, pady=2, sticky=tk.W)
            label_spectrum_a2 = tk.Label(self, text='a2: ', font=FONT)
            label_spectrum_a2.grid(row=5, column=column_figure, padx=3, pady=3, sticky=tk.N)
            entry_spectrum_a2 = tk.Entry(self, font=FONT, width=WIDTH + 2)
            entry_spectrum_a2.grid(row=5, column=column_figure + 1, columnspan=2, padx=3, pady=3, sticky=tk.N)

            label_spectrum_b2 = tk.Label(self, text='b2: ', font=FONT)
            label_spectrum_b2.grid(row=5, column=column_figure + 3, padx=3, pady=3, sticky=tk.N)
            entry_spectrum_b2 = tk.Entry(self, font=FONT, width=WIDTH + 2)
            entry_spectrum_b2.grid(row=5, column=column_figure + 4, columnspan=2, padx=3, pady=3, sticky=tk.N)

            button_create_spectrum = tk.Button(self, text='Построить спектр', font=FONT,
                                               command= lambda: self.root.create_spectrum(self.figure))
            button_create_spectrum.grid(row=6, column=column_figure, padx=3, pady=3, columnspan=6, sticky='wen')

            self.data = [entry_spectrum_x, entry_spectrum_y, entry_spectrum_n, entry_spectrum_a1, entry_spectrum_a2,
                         entry_spectrum_b1, entry_spectrum_b2]
            self.grid(row=4, column=3, padx=5, pady=5, sticky=tk.N)


class MainWindowClass(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.canvas = CanvasCirclesClass(self)

        self.add_canvas()

        self.frame_input_circle = FrameInput(self, 'circle')
        self.frame_input_ellipse = FrameInput(self, 'ellipse')

        self.add_separators()

        self.frame_choice_circle = ChoiceFrame(self, 'circle')
        self.frame_choice_ellipse = ChoiceFrame(self, 'ellipse')

        self.frame_spectrum_circle = SpectrumFrame(self, 'circle')
        self.frame_spectrum_ellipse = SpectrumFrame(self, 'ellipse')

        self.spectrum_data = []

        self.frame_both = tk.Frame(self)

        self.data_circle = []
        self.data_ellipse = []

        # self.add_choice_circle()
        # self.add_spectrum()
        # self.add_both()

    def add_separators(self):
        ttk.Separator(self, orient='horizontal').grid(row=1, column=1, columnspan=3, pady=5, sticky='we')
        ttk.Separator(self, orient='vertical').grid(row=0, column=2, rowspan=5, padx=5, sticky='ns')
        ttk.Separator(self, orient='horizontal').grid(row=3, column=1, columnspan=3, pady=5, sticky='we')

    def add_canvas(self):
        self.canvas.grid(row=0, column=0, rowspan=5, padx=5, pady=5)

    def create_figure(self, figure):
        if figure == 'circle':
            data_figure = self.frame_input_circle.data
        else:
            data_figure = self.frame_input_ellipse.data

        x = data_figure[0].get()
        y = data_figure[1].get()
        if figure == 'circle':
            r = data_figure[2].get()
            self.canvas.draw_circle([x, y, r], self.frame_choice_circle.algorithm.get(),
                                    self.frame_choice_circle.color.get())
        elif figure == 'ellipse':
            a = data_figure[2].get()
            b = data_figure[3].get()
            self.canvas.draw_ellipse([x, y, a, b], self.frame_choice_ellipse.algorithm.get(),
                                     self.frame_choice_ellipse.color.get())

    def add_both(self):
        button_delete = tk.Button(self.frame_both, text='Очистить холст', font='Times 13',
                                  command=self.canvas.delete_all, width=33)
        button_delete.grid(row=0, column=0, sticky='we')

        self.frame_both.grid(row=3, column=1, padx=5, pady=5, sticky=tk.N)

    def create_spectrum(self, figure):
        if figure == 'circle':
            spectrum_data = self.frame_spectrum_circle.data
        else:
            spectrum_data = self.frame_spectrum_ellipse.data

        x = spectrum_data[0].get()
        y = spectrum_data[1].get()
        n = spectrum_data[2].get()
        if figure == 'circle':
            r0 = spectrum_data[3].get()
            r1 = spectrum_data[4].get()
            self.canvas.draw_spectrum_circle([x, y, r0], r1, n, self.frame_choice_circle.algorithm.get(),
                                             self.frame_choice_circle.color.get())
        elif figure == 'ellipse':
            if self.choice_axis == 0:
                t1 = self.spectrum_data[3].get()
                t2 = self.spectrum_data[4].get()
            else:
                t1 = self.spectrum_data[5].get()
                t2 = self.spectrum_data[6].get()

            # self.canvas.draw_spectrum_ellipse()
