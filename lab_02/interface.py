import tkinter as tk
from picture import CanvasPicture


class InfoWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title = 'Информация о приложении'


class MainMenu(tk.Menu):
    def __init__(self, root):
        self.root = root
        super().__init__(root, tearoff=0)
        self.info_window = InfoWindow()
        self.add_paragraphs()

    def add_paragraphs(self):
        print(self.info_window)
        self.add_command(label='Информация о приложении', command=self.show_info)
        self.add_command(label='Выйти из приложения', command=self.root.destroy)

    def show_info(self):
        self.info_window.mainloop()


class MainFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.frame_carryover = tk.Frame(self)
        self.frame_scale_turn = tk.Frame(self)
        self.frame_general = tk.Frame(self)
        self.canvas = CanvasPicture(self)
        self.add_picture()
        self.add_carryover_widgets()
        self.add_scale_turn_widgets()
        self.add_general_widgets()

    def add_picture(self):
        self.canvas.grid(row=0, column=0, rowspan=3, padx=5, pady=5)

    def delete_fields(self):
        for widget in self.frame_carryover.winfo_children() + self.frame_scale_turn.winfo_children():
            if isinstance(widget, tk.Entry):
                widget.delete(0, 'end')

    def add_carryover_widgets(self):
        label_carryover = tk.Label(self.frame_carryover, text='Сделать перенос объекта в пикселях',
                                   font='Times 15 bold', relief='groove')
        label_carryover.grid(row=0, column=0, columnspan=4, pady=5, sticky=tk.N)

        label_x = tk.Label(self.frame_carryover, text='По оси абсцисс: ', font='Times 15')
        label_x.grid(row=1, column=0, sticky=tk.N)
        entry_x = tk.Entry(self.frame_carryover, font='Times 15')
        entry_x.grid(row=1, column=1, sticky=tk.N)
        label_y = tk.Label(self.frame_carryover, text='По оси ординат: ', font='Times 15')
        label_y.grid(row=2, column=0, sticky=tk.N)
        entry_y = tk.Entry(self.frame_carryover, font='Times 15')
        entry_y.grid(row=2, column=1, sticky=tk.N)

        button_carryover = tk.Button(self.frame_carryover, text='Перенести', font='Times 13',
                                     command=lambda: self.canvas.carryover_cat(entry_x.get(), entry_y.get(),
                                                                               self.label_center))
        button_carryover.grid(row=3, column=0, columnspan=4, pady=5, sticky='wen')

        self.frame_carryover.grid(row=0, column=1, padx=5, pady=5, sticky=tk.N)

    def add_scale_turn_widgets(self):
        label_scale = tk.Label(self.frame_scale_turn, text='Произвести масштабирование или\nповорот объекта',
                               font='Times 15 bold', relief='groove')
        label_scale.grid(row=0, column=0, columnspan=4, padx=3, pady=3, sticky=tk.N)

        label_center = tk.Label(self.frame_scale_turn, text='Координаты центра', font='Times 15')
        label_center.grid(row=1, column=0, columnspan=4, sticky=tk.N)

        label_center_x = tk.Label(self.frame_scale_turn, text='X:', font='Times 15')
        label_center_x.grid(row=2, column=0, sticky=tk.N)
        entry_center_x = tk.Entry(self.frame_scale_turn, font='Times 15', width=10)
        entry_center_x.grid(row=2, column=1, sticky=tk.N)

        label_center_y = tk.Label(self.frame_scale_turn, text='Y:', font='Times 15')
        label_center_y.grid(row=2, column=2, sticky=tk.N)
        entry_center_y = tk.Entry(self.frame_scale_turn, font='Times 15', width=10)
        entry_center_y.grid(row=2, column=3, sticky=tk.N)

        label_coefficient = tk.Label(self.frame_scale_turn, text='Коэффициенты масштабирования', font='Times 15')
        label_coefficient.grid(row=4, column=0, columnspan=4, pady=5, sticky=tk.N)

        label_coefficient_x = tk.Label(self.frame_scale_turn, text='KX:', font='Times 15')
        label_coefficient_x.grid(row=5, column=0, sticky=tk.N)
        entry_coefficient_x = tk.Entry(self.frame_scale_turn, font='Times 15', width=10)
        entry_coefficient_x.grid(row=5, column=1, sticky=tk.N)

        label_coefficient_y = tk.Label(self.frame_scale_turn, text='KY:', font='Times 15')
        label_coefficient_y.grid(row=5, column=2, sticky=tk.N)
        entry_coefficient_y = tk.Entry(self.frame_scale_turn, font='Times 15', width=10)
        entry_coefficient_y.grid(row=5, column=3, sticky=tk.N)

        button_scale = tk.Button(self.frame_scale_turn, text='Выполнить масштабирование', font='Times 13',
                                 command=lambda: self.canvas.scale_cat(entry_center_x.get(),
                                                                       entry_center_y.get(),
                                                                       entry_coefficient_x.get(),
                                                                       entry_coefficient_y.get(), self.label_center))
        button_scale.grid(row=6, column=0, columnspan=4, pady=5, sticky='wen')

        label_angle = tk.Label(self.frame_scale_turn, text='Угол:', font='Times 15')
        label_angle.grid(row=7, column=0, columnspan=2, pady=5, sticky=tk.N)
        entry_angle = tk.Entry(self.frame_scale_turn, font='Times 15')
        entry_angle.grid(row=7, column=2, columnspan=2, pady=5, sticky=tk.N)

        button_turn = tk.Button(self.frame_scale_turn, text='Выполнить поворот', font='Times 13',
                                command=lambda: self.canvas.turn_cat(entry_center_x.get(), entry_center_y.get(),
                                                                     entry_angle.get()))
        button_turn.grid(row=8, column=0, columnspan=4, pady=5, sticky='wen')

        button_delete = tk.Button(self.frame_scale_turn, text='Очистить все поля', font='Times 13',
                                  command=self.delete_fields)
        button_delete.grid(row=9, column=0, columnspan=4, pady=15, sticky='wen')

        self.frame_scale_turn.grid(row=1, column=1, padx=5, pady=5, sticky=tk.N)

    def add_general_widgets(self):
        button_revert = tk.Button(self.frame_general,
                                  text=' ' * 15 + 'Вернуться на один шаг назад' + ' ' * 15, font='Times 13',
                                  command=lambda: self.canvas.revert_command(self.label_center))
        button_revert.grid(row=1, column=0, columnspan=4, pady=2, sticky='wen')

        button_return_back = tk.Button(self.frame_general, text='Просмотреть исходное изображение', font='Times 13',
                                       command=lambda: self.canvas.cat.paint_cat(command=4))
        button_return_back.grid(row=2, column=0, columnspan=4, pady=2, sticky='wen')
        button_return_forward = tk.Button(self.frame_general, text='Просмотреть текущее изображение', font='Times 13',
                                          command=lambda: self.canvas.cat.paint_cat(command=1))
        button_return_forward.grid(row=3, column=0, columnspan=4, pady=2, sticky='wen')

        self.label_center = tk.Label(self.frame_general, text=f'Центральная точка объекта: '
                                                              f'({float(self.canvas.width // 2 - 140 + 150)};'
                                                              f' {float(self.canvas.height // 2 - 70 + 90)})',
                                font='Times 15 bold', relief='groove')
        self.label_center.grid(row=4, column=0, columnspan=4, pady=30, sticky='wens')

        self.frame_general.grid(row=2, column=1, padx=5, pady=5, sticky='wens')
