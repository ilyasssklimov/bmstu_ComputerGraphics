import tkinter as tk
from interface import MainFrame


def config_root(root):
    root.title('Поиск')
    root.resizable(False, False)


def main():
    root = tk.Tk()
    config_root(root)
    entry_frame = MainFrame(root)
    entry_frame.grid(padx=5, pady=5)
    root.mainloop()


if __name__ == '__main__':
    main()
