import tkinter as tk
from interface import MainFrame, MainMenu


def config_root(root):
    root.title('Преобразование объекта')
    root.resizable(False, False)
    # main_menu = MainMenu(root)
    # root.config(menu=main_menu)


def main():
    root = tk.Tk()
    config_root(root)
    main_frame = MainFrame(root)
    main_frame.grid()
    root.mainloop()


if __name__ == '__main__':
    main()
