import tkinter as tk


CANVAS_WIDTH = 900
CANVAS_HEIGHT = 750

FONT = 'Times 12'
FONT_BOLD = FONT + ' bold'
WIDTH = 5

PADX = 1
PADY = 1


def sign(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1


def int_n(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num


class Point:
    def __init__(self, x=0, y=0, color='black', exist=True):
        self.x = x
        self.y = y
        self.color = color
        self.exist = exist

    def __bool__(self):
        return self.exist

    def __str__(self):
        return f"Point({self.x}, {self.y}, {self.color})"


def create_label(root, text, font, row, column, padx, pady, sticky, relief=None, columnspan=1):
    label = tk.Label(root, text=text, font=font, relief=relief)
    label.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)


def create_button(root, text, font, row, column, padx, pady, columnspan, sticky, command=None):
    button = tk.Button(root, text=text, font=font, command=command)
    button.grid(row=row, column=column, padx=padx, pady=pady, columnspan=columnspan, sticky=sticky)


def create_entry(root, font, row, column, padx, pady, sticky, width=None, columnspan=1):
    entry = tk.Entry(root, font=font, width=width)
    entry.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)
    return entry


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


Ctrl = 4
BLACK_COLOR = (0, 0, 0)
RED_COLOR = (255, 0, 0)
BLUE_COLOR = (0, 0, 255)
GREEN_COLOR = (0, 128, 0)
YELLOW_COLOR = (255, 255, 0)
WHITE_COLOR = (255, 255, 255)
