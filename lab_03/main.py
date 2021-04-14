import tkinter as tk
from interface import MainWindow


def config_root(root):
    root.title('Построение отрезков')
    # root.geometry('700x700')
    root.resizable(False, False)


def main():
    root = tk.Tk()
    config_root(root)
    main_window = MainWindow(root)
    main_window.grid()
    root.mainloop()


if __name__ == '__main__':
    main()
