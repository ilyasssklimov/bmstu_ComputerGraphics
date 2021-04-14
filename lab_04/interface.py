from lab_04.canvas import CanvasCirclesClass
from lab_04.data import algorithms, colors
import tkinter as tk
from tkinter import ttk


class MainWindowClass(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.frame_input = tk.Frame(self)

        self.frame_choice = tk.Frame(self)
        self.algorithm = tk.IntVar()
        self.algorithm.set(0)
        self.color = tk.IntVar()
        self.color.set(0)

        self.frame_spectrum = tk.Frame(self)
        self.spectrum_data = []
        self.choice_axis = tk.IntVar()
        self.choice_axis.set(0)

        self.frame_both = tk.Frame(self)

        self.canvas = CanvasCirclesClass(self)
        self.data_circle = []
        self.data_ellipse = []

        self.add_canvas()
        self.add_input()
        self.add_choice_circle()
        self.add_spectrum()
        self.add_both()

    def add_canvas(self):
        self.canvas.grid(row=0, column=0, rowspan=4, padx=5, pady=5)

    def add_input(self):
        label_center_circle = tk.Label(self.frame_input, text='Окружность: центр и радиус', font='Times 13 bold',
                                       relief='groove')
        label_center_circle.grid(row=0, column=0, columnspan=6, padx=3, pady=3, sticky=tk.N)

        label_circle_x = tk.Label(self.frame_input, text='X: ', font='Times 13')
        label_circle_x.grid(row=1, column=0, sticky=tk.N)
        entry_circle_x = tk.Entry(self.frame_input, font='Times 13', width=6)
        entry_circle_x.grid(row=1, column=1, sticky=tk.N)
        entry_circle_x.insert(0, '350')

        label_circle_y = tk.Label(self.frame_input, text='Y: ', font='Times 13')
        label_circle_y.grid(row=1, column=2, sticky=tk.N)
        entry_circle_y = tk.Entry(self.frame_input, font='Times 13', width=6)
        entry_circle_y.grid(row=1, column=3, sticky=tk.N)
        entry_circle_y.insert(0, '350')

        label_circle_r = tk.Label(self.frame_input, text='R: ', font='Times 13')
        label_circle_r.grid(row=1, column=4, sticky=tk.N)
        entry_circle_r = tk.Entry(self.frame_input, font='Times 13', width=6)
        entry_circle_r.grid(row=1, column=5, sticky=tk.N)
        entry_circle_r.insert(0, '150')

        self.data_circle.extend([entry_circle_x, entry_circle_y, entry_circle_r])

        separator = ttk.Separator(self.frame_input, orient='horizontal')
        separator.grid(row=2, column=0, columnspan=6, pady=10, sticky='we')

        label_center_circle = tk.Label(self.frame_input, text='Эллипс: центр и полуоси', font='Times 13 bold',
                                       relief='groove')
        label_center_circle.grid(row=3, column=0, columnspan=6, padx=3, pady=3, sticky=tk.N)

        label_ellipse_x = tk.Label(self.frame_input, text='X: ', font='Times 13')
        label_ellipse_x.grid(row=4, column=0, sticky=tk.N)
        entry_ellipse_x = tk.Entry(self.frame_input, font='Times 13', width=9)
        entry_ellipse_x.grid(row=4, column=1, columnspan=2, sticky=tk.N)
        entry_ellipse_x.insert(0, '350')

        label_ellipse_y = tk.Label(self.frame_input, text='Y: ', font='Times 13')
        label_ellipse_y.grid(row=4, column=3, sticky=tk.N)
        entry_ellipse_y = tk.Entry(self.frame_input, font='Times 13', width=9)
        entry_ellipse_y.grid(row=4, column=4, columnspan=2, sticky=tk.N)
        entry_ellipse_y.insert(0, '350')

        label_ellipse_a = tk.Label(self.frame_input, text='a: ', font='Times 13')
        label_ellipse_a.grid(row=5, column=0, sticky=tk.N)
        entry_ellipse_a = tk.Entry(self.frame_input, font='Times 13', width=9)
        entry_ellipse_a.grid(row=5, column=1, columnspan=2, sticky=tk.N)
        entry_ellipse_a.insert(0, '150')

        label_ellipse_b = tk.Label(self.frame_input, text='b: ', font='Times 13')
        label_ellipse_b.grid(row=5, column=3, sticky=tk.N)
        entry_ellipse_b = tk.Entry(self.frame_input, font='Times 13', width=9)
        entry_ellipse_b.grid(row=5, column=4, columnspan=2, sticky=tk.N)
        entry_ellipse_b.insert(0, '150')

        self.data_ellipse.extend([entry_ellipse_x, entry_ellipse_y, entry_ellipse_a, entry_ellipse_b])
        self.frame_input.grid(row=0, column=1, padx=5, pady=5, sticky=tk.N)

    def add_choice_circle(self):
        label_algorithm_circle = tk.Label(self.frame_choice, text='Выберите способ построения',
                                          font='Times 13 bold', relief='groove')
        label_algorithm_circle.grid(row=0, column=0, columnspan=3, padx=3, pady=3, sticky=tk.N)

        for index, algorithm in enumerate(algorithms):
            tk.Radiobutton(self.frame_choice, variable=self.algorithm, value=index, text=algorithm,
                           font='Times 13').grid(row=index + 1, column=0, columnspan=3,
                                                 padx=3, pady=1, sticky=(tk.W, tk.N))

        label_color_circle = tk.Label(self.frame_choice, text='Выберите цвет',
                                      font='Times 13 bold', relief='groove')
        label_color_circle.grid(row=6, column=0, columnspan=3, padx=3, pady=3, sticky=tk.N)

        row, column = 7, -1
        for index, color in enumerate(colors):
            if not index % 2:
                row = 7
                column += 1
            tk.Radiobutton(self.frame_choice, variable=self.color, value=index, text=color,
                           font='Times 13').grid(row=row, column=column, padx=7, pady=2, sticky='wn')
            row += 1

        button_create_circle = tk.Button(self.frame_choice, text='Построить окружность', font='Times 13',
                                         command=self.create_circle)
        button_create_circle.grid(row=9, column=0, columnspan=3, sticky='wen')

        button_create_ellipse = tk.Button(self.frame_choice, text='Построить эллипс', font='Times 13',
                                          command=self.create_ellipse)
        button_create_ellipse.grid(row=9, column=0, columnspan=3, sticky='wen')

        self.frame_choice.grid(row=1, column=1, padx=5, pady=5, sticky=tk.N)

    def create_circle(self):
        x = self.data_circle[0].get()
        y = self.data_circle[1].get()
        r = self.data_circle[2].get()
        self.canvas.draw_circle([x, y, r], self.algorithm.get(), self.color.get())

    def create_ellipse(self):
        x = self.data_ellipse[0].get()
        y = self.data_ellipse[1].get()
        a = self.data_ellipse[2].get()
        b = self.data_ellipse[3].get()
        self.canvas.draw_ellipse([x, y, a, b], self.algorithm.get(), self.color.get())

    def add_spectrum(self):
        label_center_circle = tk.Label(self.frame_spectrum, text='Построение спектра окружностой\n'
                                                                 '(указать радиусы) и\n'
                                                                 'эллипсов (указать полуоси)',
                                       font='Times 13 bold', relief='groove')
        label_center_circle.grid(row=0, column=0, columnspan=6, padx=3, pady=3, sticky=tk.N)

        label_spectrum_x = tk.Label(self.frame_spectrum, text='X:', font='Times 13')
        label_spectrum_x.grid(row=1, column=0, padx=1, pady=3, sticky=tk.N)
        entry_spectrum_x = tk.Entry(self.frame_spectrum, font='Times 13', width=6)
        entry_spectrum_x.grid(row=1, column=1, padx=1, pady=3, sticky=tk.N)

        label_spectrum_y = tk.Label(self.frame_spectrum, text='Y:', font='Times 13')
        label_spectrum_y.grid(row=1, column=2, padx=1, pady=3, sticky=tk.N)
        entry_spectrum_y = tk.Entry(self.frame_spectrum, font='Times 13', width=6)
        entry_spectrum_y.grid(row=1, column=3, padx=1, pady=3, sticky=tk.N)

        label_spectrum_n = tk.Label(self.frame_spectrum, text='n:', font='Times 13')
        label_spectrum_n.grid(row=1, column=4, padx=1, pady=3, sticky=tk.N)
        entry_spectrum_n = tk.Entry(self.frame_spectrum, font='Times 13', width=6)
        entry_spectrum_n.grid(row=1, column=5, padx=1, pady=3, sticky='wn')

        label_spectrum_r_start = tk.Label(self.frame_spectrum, text='R1: ', font='Times 13')
        label_spectrum_r_start.grid(row=2, column=0, padx=3, pady=3, sticky=tk.N)
        entry_spectrum_r_start = tk.Entry(self.frame_spectrum, font='Times 13', width=6)
        entry_spectrum_r_start.grid(row=2, column=1, padx=3, pady=3, sticky=tk.N)

        label_spectrum_r_finish = tk.Label(self.frame_spectrum, text='R2: ', font='Times 13')
        label_spectrum_r_finish.grid(row=2, column=2, padx=3, pady=3, sticky=tk.N)
        entry_spectrum_r_finish = tk.Entry(self.frame_spectrum, font='Times 13', width=6)
        entry_spectrum_r_finish.grid(row=2, column=3, padx=3, pady=3, sticky=tk.N)

        separator = ttk.Separator(self.frame_spectrum, orient='horizontal')
        separator.grid(row=3, column=0, columnspan=6, pady=10, sticky='we')

        tk.Radiobutton(self.frame_spectrum, variable=self.choice_axis, value=0, text='').grid(row=4,
                                                                                              column=0,
                                                                                              padx=1,
                                                                                              pady=2,
                                                                                              sticky=tk.W)
        label_spectrum_a1 = tk.Label(self.frame_spectrum, text='a1: ', font='Times 13')
        label_spectrum_a1.grid(row=4, column=1, padx=3, pady=3, sticky='en')
        entry_spectrum_a1 = tk.Entry(self.frame_spectrum, font='Times 13', width=7)
        entry_spectrum_a1.grid(row=4, column=2, padx=3, pady=3, sticky='en')

        label_spectrum_b1 = tk.Label(self.frame_spectrum, text='b1: ', font='Times 13')
        label_spectrum_b1.grid(row=4, column=3, padx=3, pady=3, sticky='en')
        entry_spectrum_b1 = tk.Entry(self.frame_spectrum, font='Times 13', width=7)
        entry_spectrum_b1.grid(row=4, column=4, padx=3, pady=3, sticky='en')

        tk.Radiobutton(self.frame_spectrum, variable=self.choice_axis, value=1, text='').grid(row=5,
                                                                                              column=0,
                                                                                              padx=1,
                                                                                              pady=2,
                                                                                              sticky=tk.W)
        label_spectrum_a2 = tk.Label(self.frame_spectrum, text='a2: ', font='Times 13')
        label_spectrum_a2.grid(row=5, column=1, padx=3, pady=3, sticky='en')
        entry_spectrum_a2 = tk.Entry(self.frame_spectrum, font='Times 13', width=7)
        entry_spectrum_a2.grid(row=5, column=2, padx=3, pady=3, sticky=tk.N)

        label_spectrum_b2 = tk.Label(self.frame_spectrum, text='b2: ', font='Times 13')
        label_spectrum_b2.grid(row=5, column=3, padx=3, pady=3, sticky='en')
        entry_spectrum_b2 = tk.Entry(self.frame_spectrum, font='Times 13', width=7)
        entry_spectrum_b2.grid(row=5, column=4, padx=3, pady=3, sticky=tk.N)

        button_create_spectrum = tk.Button(self.frame_spectrum, text='Построить спектр', font='Times 13',
                                           command=self.create_spectrum_circle)
        button_create_spectrum.grid(row=6, column=0, padx=3, pady=3, columnspan=6, sticky='wen')

        self.spectrum_data.extend([entry_spectrum_x, entry_spectrum_y,
                                   entry_spectrum_r_start, entry_spectrum_r_finish,
                                   entry_spectrum_n, entry_spectrum_a1, entry_spectrum_a2,
                                   entry_spectrum_b1, entry_spectrum_b2])
        self.frame_spectrum.grid(row=2, column=1, padx=5, pady=5, sticky=tk.N)

    def add_both(self):
        button_delete = tk.Button(self.frame_both, text='Очистить холст', font='Times 13',
                                  command=self.canvas.delete_all, width=33)
        button_delete.grid(row=0, column=0, sticky='we')

        self.frame_both.grid(row=3, column=1, padx=5, pady=5, sticky=tk.N)

    def create_spectrum_circle(self):
        x = self.spectrum_data[0].get()
        y = self.spectrum_data[1].get()
        r0 = self.spectrum_data[2].get()
        r1 = self.spectrum_data[3].get()
        n = self.spectrum_data[4].get()
        self.canvas.draw_spectrum_circle([x, y, r0], r1, n, self.algorithm.get(), self.color.get())

    def create_spectrum_ellipse(self):
        x = self.spectrum_data[0].get()
        y = self.spectrum_data[1].get()
        n = self.spectrum_data[4].get()
        if self.choice_axis == 0:
            t1 = self.spectrum_data[5].get()
            t2 = self.spectrum_data[6].get()
        else:
            t1 = self.spectrum_data[7].get()
            t2 = self.spectrum_data[8].get()

        self.canvas.draw_spectrum_ellipse()
