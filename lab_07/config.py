import tkinter as tk

CANVAS_WIDTH = 900
CANVAS_HEIGHT = 750

FONT = 'Times 12'
FONT_BOLD = FONT + ' bold'

PADX = 1
PADY = 1


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

    def clear(self):
        self.x = 0
        self.y = 0
        self.color = 'black'
        self.exist = False

    def set(self, x, y, color):
        self.__init__(x, y, color)

    @property
    def get(self):
        return self.x, self.y


def create_label(root, text, font, row, column, padx, pady, sticky, relief=None, columnspan=1):
    label = tk.Label(root, text=text, font=font, relief=relief)
    label.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)


def create_button(root, text, font, row, column, padx, pady, columnspan, sticky, command=None, bg=None):
    button = tk.Button(root, text=text, font=font, background=bg, activebackground=bg, command=command)
    button.grid(row=row, column=column, padx=padx, pady=pady, columnspan=columnspan, sticky=sticky)
    return button


def create_entry(root, font, row, column, padx, pady, sticky, width=None, columnspan=1):
    entry = tk.Entry(root, font=font, width=width)
    entry.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)
    return entry


Ctrl = [4, 12]
Shift = [1, 9]
