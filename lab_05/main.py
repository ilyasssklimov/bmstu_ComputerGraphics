import interface
import tkinter as tk


def create_main_frame(root):
    main_window = interface.MainWindowClass(root=root)
    root.title('Заполнение')
    root.resizable(False, False)
    main_window.grid()


def main():
    master = tk.Tk()
    create_main_frame(master)
    master.mainloop()


if __name__ == '__main__':
    main()
