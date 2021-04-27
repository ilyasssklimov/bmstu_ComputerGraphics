import tkinter as tk


CANVAS_WIDTH = 900
CANVAS_HEIGHT = 750

FONT = 'Times 12'
FONT_BOLD = FONT + ' bold'
WIDTH = 5

PADX = 1
PADY = 1


class Point:
    def __init__(self, x=0, y=0, color='black', exist=True):
        self.x = x
        self.y = y
        self.color = color
        self.exist = exist

    def __bool__(self):
        return self.exist


def create_label(root, text, font, row, column, padx, pady, sticky, relief=None, columnspan=1):
    label = tk.Label(root, text=text, font=font, relief=relief)
    label.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)


def create_button(root, text, font, row, column, padx, pady, columnspan, sticky, command=None):
    button_create_spectrum = tk.Button(root, text=text, font=font, command=command)
    button_create_spectrum.grid(row=row, column=column, padx=padx, pady=pady, columnspan=columnspan, sticky=sticky)


def create_radiobutton(root, variable, value, text, font, row, column, padx, pady, sticky, columnspan=1):
    radiobutton = tk.Radiobutton(root, variable=variable, value=value, text=text, font=font)
    radiobutton.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)


colors = {
    'Черный': 'black',
    'Красный': 'red',
    'Синий': 'blue',
    'Зеленый': 'green',
    'Желтый': 'yellow',
    'Белый': 'white'
}
