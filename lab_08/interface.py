import algorithm as alg
import canvas as cv
import config as cfg
from config import FONT, FONT_BOLD, PADX, PADY
import tkinter as tk
import tkinter.colorchooser as cch
import tkinter.messagebox as mb


class MainWindowClass(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.canvas = cv.Canvas(self)
        self.add_canvas()

        self.frame_cutter = tk.Frame(self)
        self.cutter_coors = None
        self.cutter = []
        self.add_cutter()

        self.frame_section = tk.Frame(self)
        self.section_coors = None
        self.section = []
        self.add_section()

        self.frame_color = tk.Frame(self)
        self.color_wins = dict()
        self.colors = {
            'cutter': 'black',
            'section': 'red',
            'result': 'blue'
        }
        self.add_color()

        self.frame_buttons = tk.Frame(self)
        self.add_buttons()

    def add_canvas(self):
        self.canvas.grid(row=0, column=0, rowspan=4, padx=5, pady=5)

    def add_cutter(self):
        cfg.create_label(self.frame_cutter, 'ВВОД ОТСЕКАТЕЛЯ', FONT_BOLD, 0, 0, PADX, PADY, tk.N, 'groove')
        cfg.create_label(self.frame_cutter, 'Очередная вершина\n(или ПКМ, \nверт./гориз. - +Ctrl)',
                         FONT_BOLD, 1, 0, PADX, 1, tk.N)
        self.cutter_coors = cfg.create_entry(self.frame_cutter, FONT, 2, 0, PADX, PADY, tk.N)
        cfg.create_button(self.frame_cutter, 'ДОБАВИТЬ', FONT, 3, 0, PADX, PADY, 1, 'WE', self.create_cutter)
        cfg.create_button(self.frame_cutter, 'ЗАМКНУТЬ', FONT, 4, 0, PADX, PADY, 1, 'WE', self.canvas.end_cutter)
        self.frame_cutter.grid(row=0, column=1, padx=5, pady=5, sticky=tk.N)

    def create_cutter(self):
        coors = self.cutter_coors.get().split()
        self.cutter_coors.delete(0, 'end')
        try:
            for i in range(0, len(coors) - 1, 2):
                x, y = float(coors[i]), float(coors[i + 1])
                self.canvas.draw_cutter(cfg.Point(x, y))

        except IndexError:
            mb.showerror('Ошибка', 'Должно быть введено больше двух координат, и их количество должно быть четным')
        except ValueError:
            mb.showerror('Ошибка', 'Каждая координата должна быть числом, введенным через пробел')

    def add_section(self):
        cfg.create_label(self.frame_section, 'ВВОД ОТРЕЗКОВ', FONT_BOLD, 0, 0, PADX, PADY, tk.N, 'groove')
        cfg.create_label(self.frame_section, 'Координаты отрезка\n(или ЛКМ,\nверт./гориз. - +Ctrl,\n'
                                             'параллельные - +Shift)',
                         FONT_BOLD, 1, 0, PADX, 1, tk.N)
        self.section_coors = cfg.create_entry(self.frame_section, FONT, 2, 0, PADX, PADY, tk.N)
        cfg.create_button(self.frame_section, 'ВВЕСТИ', FONT, 3, 0, PADX, PADY, 1, 'WE', self.create_section)
        self.frame_section.grid(row=1, column=1, padx=5, pady=5, sticky=tk.N)

    def create_section(self):
        coors = self.section_coors.get().split()
        self.section_coors.delete(0, 'end')
        try:
            x1, y1 = cfg.int_n(float(coors[0])), cfg.int_n(float(coors[1]))
            x2, y2 = cfg.int_n(float(coors[2])), cfg.int_n(float(coors[3]))
            self.canvas.draw_line(x1, y1, x2, y2, self.colors['section'])
            self.section.append([cfg.Point(x1, y1, self.colors['section']), cfg.Point(x2, y2, self.colors['section'])])
        except IndexError:
            mb.showerror('Ошибка', 'Должно быть введено 4 координаты')
        except ValueError:
            mb.showerror('Ошибка', 'Каждая координата должна быть числом, введенным через пробел')

    def add_color(self):
        cfg.create_label(self.frame_color, 'ЦВЕТ ОТСЕКАТЕЛЯ: ', FONT_BOLD, 0, 0, PADX, 4, tk.N, 'groove')
        self.color_wins['cutter'] = cfg.create_button(self.frame_color, '', FONT, 1, 0, PADX, 0, 4, 'WE',
                                                      lambda: self.choose_color('cutter'), self.colors['cutter'])

        cfg.create_label(self.frame_color, 'ЦВЕТ ОТРЕЗКОВ: ', FONT_BOLD, 2, 0, PADX, 4, tk.N, 'groove')
        self.color_wins['section'] = cfg.create_button(self.frame_color, '', FONT, 3, 0, PADX, 0, 4, 'WE',
                                                       lambda: self.choose_color('section'), self.colors['section'])

        cfg.create_label(self.frame_color, 'ЦВЕТ РЕЗУЛЬТАТА: ', FONT_BOLD, 4, 0, PADX, 4, tk.N, 'groove')
        self.color_wins['result'] = cfg.create_button(self.frame_color, '', FONT, 5, 0, PADX, 0, 4, 'WE',
                                                      lambda: self.choose_color('result'), self.colors['result'])

        self.frame_color.grid(row=2, column=1, padx=5, pady=5, sticky=tk.N)

    def choose_color(self, color):
        self.colors[color] = cch.askcolor()[1]
        self.color_wins[color].config(**{'background': self.colors[color], 'activebackground': self.colors[color]})

    def add_buttons(self):
        cfg.create_button(self.frame_buttons, 'ОТСЕЧЬ', FONT, 0, 0, PADX, PADY, 1, 'WE', lambda:
                          alg.cyrus_beck_cut(self.canvas, self.cutter, self.section))

        cfg.create_button(self.frame_buttons, 'ОЧИСТИТЬ ХОЛСТ', FONT, 1, 0, PADX, PADY, 1, 'WE', self.canvas.delete_all)
        cfg.create_button(self.frame_buttons, 'ИЗМЕРИТЬ ВРЕМЯ', FONT, 6, 0, PADX, PADY, 1, 'WE', self.count_time)

        self.frame_buttons.grid(row=3, column=1, padx=5, pady=5, sticky=tk.N)

    def count_time(self):
        time = alg.cut_simple(self.canvas, self.cutter, self.section)
        mb.showinfo('Время', f'Время для отсечения составило {time:.6f} секунды')
