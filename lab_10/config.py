import tkinter as tk


FONT = 'Times 14'
FONT_BOLD = FONT + ' bold'

PADX = 1
PADY = 1


FUNCS = ['sin(x) * cos(z)', 'sin(cos(x)) * sin(z)', 'cos(x) * z / 3']


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


def create_radiobutton(root, variable, value, text, font, row, column, padx, pady, sticky, columnspan=1):
    radiobutton = tk.Radiobutton(root, variable=variable, value=value, text=text, font=font)
    radiobutton.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)
