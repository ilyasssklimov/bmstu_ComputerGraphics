import tkinter as tk


FONT = 'Times 12'
FONT_BOLD = FONT + ' bold'
WIDTH = 5

PADX = 1
PADY = 1

CANVAS_WIDTH = 900
CANVAS_HEIGHT = 750


def create_label(root, text, font, row, column, padx, pady, sticky, relief=None, columnspan=1):
    label = tk.Label(root, text=text, font=font, relief=relief)
    label.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)


def create_entry(root, font, row, column, padx, pady, sticky, width=None, columnspan=1):
    entry_ellipse_x = tk.Entry(root, font=font, width=width)
    entry_ellipse_x.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)
    return entry_ellipse_x


def create_radiobutton(root, variable, value, text, font, row, column, padx, pady, sticky, columnspan=1):
    radiobutton = tk.Radiobutton(root, variable=variable, value=value, text=text, font=font)
    radiobutton.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)


def create_button(root, text, font, row, column, padx, pady, columnspan, sticky, command=None):
    button_create_spectrum = tk.Button(root, text=text, font=font, command=command)
    button_create_spectrum.grid(row=row, column=column, padx=padx, pady=pady, columnspan=columnspan, sticky=sticky)
