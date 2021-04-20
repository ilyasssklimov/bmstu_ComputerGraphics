from algorithms_circle import *
from algorithms_ellipse import *
from canvas import CanvasCirclesClass
from config import *
from data import algorithms, colors
from efficiency import compare_time_circle, compare_time_ellipse
import tkinter as tk
from tkinter import ttk


class FrameInput(tk.Frame):
    def __init__(self, root, figure):
        super().__init__(root)

        self.figure = figure
        self.data = []

        self.add_input()

    def add_input(self):
        create_label(self, 'X: ', FONT, 1, 0, 0, 0, tk.N)
        entry_x = create_entry(self, FONT, 1, 1, 1, 0, tk.N, WIDTH)

        create_label(self, 'Y: ', FONT, 1, 2, 0, 0, tk.N)
        entry_y = create_entry(self, FONT, 1, 3, 1, 0, tk.N, WIDTH)

        if self.figure == 'circle':
            create_label(self, 'Окружность: центр и радиус', FONT_BOLD, 0, 0, PADX, PADY, tk.N, 'groove', 6)

            create_label(self, 'R: ', FONT, 1, 4, 0, 0, tk.N)
            entry_circle_r = create_entry(self, FONT, 1, 5, 0, 0, tk.N, WIDTH)

            self.data = [entry_x, entry_y, entry_circle_r]
            self.grid(row=0, column=1, padx=5, pady=5, sticky=tk.N)

        elif self.figure == 'ellipse':
            create_label(self, 'Эллипс: центр и полуоси', FONT_BOLD, 0, 0, PADX, PADY, tk.N, 'groove', 8)

            create_label(self, 'a: ', FONT, 1, 4, 0, 0, tk.N)
            entry_ellipse_a = create_entry(self, FONT, 1, 5, 1, 0, tk.N, WIDTH)

            create_label(self, 'b: ', FONT, 1, 6, 0, 0, tk.N)
            entry_ellipse_b = create_entry(self, FONT, 1, 7, 1, 0, tk.N, WIDTH)

            self.data = [entry_x, entry_y, entry_ellipse_a, entry_ellipse_b]
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

        create_label(self, 'Выберите способ построения', FONT_BOLD, 0, column_figure, PADX, PADY, tk.N, 'groove', 3)

        for index, algorithm in enumerate(algorithms):
            create_radiobutton(self, self.algorithm, index, algorithm, FONT, index + 1, column_figure, PADX, 0, 'wn', 3)

        create_label(self, 'Выберите цвет', FONT_BOLD, 6, column_figure, PADX, PADY, tk.N, 'groove', 3)

        row, column = 7, column_figure - 1
        for index, color in enumerate(colors):
            if not index % 2:
                row = 7
                column += 1
            create_radiobutton(self, self.color, index, color, FONT, row, column, PADX + 2, 0, 'wn')
            row += 1

        text, column = '', 0
        if self.figure == 'circle':
            text = 'Построить окружность'
            column = 1
        elif self.figure == 'ellipse':
            text = 'Построить эллипс'
            column = 3

        create_button(self, text, FONT, 9, column_figure, 0, 0, 3, 'wen', lambda: self.root.create_figure(self.figure))
        self.grid(row=1, column=column, padx=PADX, pady=PADY, sticky=tk.N)


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
            create_label(self, 'Построение спектра окружностей', FONT_BOLD, 0, 0, PADX, PADY, tk.N, 'groove', 6)
        elif self.figure == 'ellipse':
            column_figure = 2
            create_label(self, 'Построение спектра эллипсов', FONT_BOLD, 0, 2, PADX, PADY, tk.N, 'groove', 6)

        create_label(self, 'X: ', FONT, 1, column_figure, 0, 0, tk.N)
        entry_spectrum_x = create_entry(self, FONT, 1, column_figure + 1, 1, 0, tk.N, WIDTH)

        create_label(self, 'Y: ', FONT, 1, column_figure + 2, 0, 0, tk.N)
        entry_spectrum_y = create_entry(self, FONT, 1, column_figure + 3, 1, 0, tk.N, WIDTH)

        create_label(self, 'n: ', FONT, 1, column_figure + 4, 0, 0, tk.N)
        entry_spectrum_n = create_entry(self, FONT, 1, column_figure + 5, 1, 0, tk.N, WIDTH)

        if self.figure == 'circle':
            create_label(self, 'R1: ', FONT, 2, column_figure, 0, 0, tk.N)
            entry_spectrum_r1 = create_entry(self, FONT, 2, column_figure + 1, 1, 0, tk.N, WIDTH + 3, 2)

            create_label(self, 'R2: ', FONT, 2, column_figure + 3, 0, 0, tk.N)
            entry_spectrum_r2 = create_entry(self, FONT, 2, column_figure + 4, 1, 0, tk.N, WIDTH + 3, 2)

            self.data = [entry_spectrum_x, entry_spectrum_y, entry_spectrum_n, entry_spectrum_r1, entry_spectrum_r2]

        elif self.figure == 'ellipse':
            create_radiobutton(self, self.choice_axis, 0, '', FONT, 4, 0, 1, 2, tk.W)

            create_label(self, 'a1: ', FONT, 4, column_figure, 0, 0, tk.N)
            entry_spectrum_a1 = create_entry(self, FONT, 4, column_figure + 1, 1, 0, tk.N, WIDTH)

            create_label(self, 'a2: ', FONT, 4, column_figure + 2, 0, 0, tk.N)
            entry_spectrum_a2 = create_entry(self, FONT, 4, column_figure + 3, 1, 0, tk.N, WIDTH)

            create_label(self, 'b: ', FONT, 4, column_figure + 4, 0, 0, tk.N)
            entry_spectrum_b = create_entry(self, FONT, 4, column_figure + 5, 1, 0, tk.N, WIDTH)

            create_radiobutton(self, self.choice_axis, 1, '', FONT, 5, 0, 1, 2, tk.W)

            create_label(self, 'b1: ', FONT, 5, column_figure, 0, 0, tk.N)
            entry_spectrum_b1 = create_entry(self, FONT, 5, column_figure + 1, 1, 0, tk.N, WIDTH)

            create_label(self, 'b2: ', FONT, 5, column_figure + 2, 0, 0, tk.N)
            entry_spectrum_b2 = create_entry(self, FONT, 5, column_figure + 3, 1, 0, tk.N, WIDTH)

            create_label(self, 'a: ', FONT, 5, column_figure + 4, 0, 0, tk.N)
            entry_spectrum_a = create_entry(self, FONT, 5, column_figure + 5, 1, 0, tk.N, WIDTH)

            create_button(self, 'Построить спектр', FONT, 6, column_figure, PADX, PADY, 6, 'wen',
                          lambda: self.root.create_spectrum(self.figure))

            self.data = [entry_spectrum_x, entry_spectrum_y, entry_spectrum_n]
            self.data.extend([entry_spectrum_a1, entry_spectrum_a2, entry_spectrum_b])
            self.data.extend([entry_spectrum_b1, entry_spectrum_b2, entry_spectrum_a])

        row_figure = 3 if self.figure == 'circle' else 6
        create_button(self, 'Построить спектр', FONT, row_figure, column_figure, PADX, PADY, 6, 'wen',
                      lambda: self.root.create_spectrum(self.figure))

        self.grid(row=3, column=column_figure + 1, padx=5, pady=5, sticky=tk.N)


class EfficiencyFrame(tk.Frame):
    def __init__(self, root, figure):
        super().__init__(root)

        self.root = root
        self.figure = figure

        self.add_efficiency()

    def add_efficiency(self):
        if self.figure == 'circle':
            column_figure = 0
            text = 'Эффективность построения\nокружностей по времени\n(поля ввода те же, что и для спектра)'
        else:
            column_figure = 2
            text = 'Эффективность построения\nэллипсов по времени\n(поля ввода те же, что и для спектра)'

        create_button(self, 'Вывести график', FONT, 1, column_figure, PADX, PADY, 1, 'wen',
                      lambda: self.root.efficiency(self.figure))
        create_label(self, text, FONT_BOLD, 0, column_figure, PADX, PADY, tk.N, 'groove')

        self.grid(row=5, column=column_figure + 1, padx=5, pady=5, sticky=tk.N)


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

        self.frame_efficiency_circle = EfficiencyFrame(self, 'circle')
        self.frame_efficiency_ellipse = EfficiencyFrame(self, 'ellipse')

        self.frame_general = tk.Frame(self)
        self.add_general()

    def add_separators(self):
        ttk.Separator(self, orient='vertical').grid(row=0, column=2, rowspan=6, padx=5, sticky='ns')
        ttk.Separator(self, orient='horizontal').grid(row=2, column=1, columnspan=3, pady=5, sticky='we')
        ttk.Separator(self, orient='horizontal').grid(row=4, column=1, columnspan=3, pady=5, sticky='we')
        ttk.Separator(self, orient='horizontal').grid(row=6, column=1, columnspan=3, pady=5, sticky='we')

    def add_canvas(self):
        self.canvas.grid(row=0, column=0, rowspan=8, padx=5, pady=5)

    def create_figure(self, figure):
        if figure == 'circle':
            data_figure = self.frame_input_circle.data
        else:
            data_figure = self.frame_input_ellipse.data

        x = data_figure[0].get()
        y = data_figure[1].get()
        if figure == 'circle':
            r = data_figure[2].get()
            self.canvas.draw_circle([x, y, r],
                                    self.frame_choice_circle.algorithm.get(),
                                    self.frame_choice_circle.color.get())
        elif figure == 'ellipse':
            a = data_figure[2].get()
            b = data_figure[3].get()
            self.canvas.draw_ellipse([x, y, a, b],
                                     self.frame_choice_ellipse.algorithm.get(),
                                     self.frame_choice_ellipse.color.get())

    def add_general(self):
        create_button(self.frame_general, 'Очистить холст', FONT, 0, 0, 0, 0, 1, 'we', self.canvas.delete_all)

        self.frame_general.grid(row=7, column=1, padx=5, columnspan=3, pady=5, sticky=tk.N)

    def create_spectrum(self, figure):
        if figure == 'circle':
            spectrum_data = self.frame_spectrum_circle.data
        else:
            spectrum_data = self.frame_spectrum_ellipse.data

        x = spectrum_data[0].get()
        y = spectrum_data[1].get()
        n = spectrum_data[2].get()

        if figure == 'circle':
            r1 = spectrum_data[3].get()
            r2 = spectrum_data[4].get()
            self.canvas.draw_spectrum_circle([x, y, r1, r2, n],
                                             self.frame_choice_circle.algorithm.get(),
                                             self.frame_choice_circle.color.get())
        elif figure == 'ellipse':
            if self.frame_spectrum_ellipse.choice_axis.get() == 0:
                a1 = spectrum_data[3].get()
                a2 = spectrum_data[4].get()
                b = spectrum_data[5].get()
                self.canvas.draw_spectrum_ellipse([x, y, a1, a2, n, b],
                                                  self.frame_spectrum_ellipse.choice_axis.get(),
                                                  self.frame_choice_ellipse.algorithm.get(),
                                                  self.frame_choice_ellipse.color.get())
            else:
                b1 = spectrum_data[6].get()
                b2 = spectrum_data[7].get()
                a = spectrum_data[8].get()
                self.canvas.draw_spectrum_ellipse([x, y, b1, b2, n, a],
                                                  self.frame_spectrum_ellipse.choice_axis.get(),
                                                  self.frame_choice_ellipse.algorithm.get(),
                                                  self.frame_choice_ellipse.color.get())

    def efficiency(self, figure):
        if figure == 'circle':
            efficiency_data = self.frame_spectrum_circle.data
        else:
            efficiency_data = self.frame_spectrum_ellipse.data

        x = efficiency_data[0].get()
        y = efficiency_data[1].get()
        n = efficiency_data[2].get()

        if figure == 'circle':
            r1 = efficiency_data[3].get()
            r2 = efficiency_data[4].get()
            func = [canonical_circle, parametric_circle, bresenham_circle, midpoint_circle, self.canvas.create_oval]
            compare_time_circle(self.canvas, func, [x, y, r1, r2, n])
        elif figure == 'ellipse':
            func = [canonical_ellipse, parametric_ellipse, bresenham_ellipse, midpoint_ellipse, self.canvas.create_oval]
            choice = self.frame_spectrum_ellipse.choice_axis.get()
            if self.frame_spectrum_ellipse.choice_axis.get() == 0:
                a1 = efficiency_data[3].get()
                a2 = efficiency_data[4].get()
                b = efficiency_data[5].get()
                compare_time_ellipse(self.canvas, func, [x, y, a1, a2, n, b], choice)
            else:
                b1 = efficiency_data[6].get()
                b2 = efficiency_data[7].get()
                a = efficiency_data[8].get()
                compare_time_ellipse(self.canvas, func, [x, y, b1, b2, n, a], choice)



