import interface as nrf
import tkinter as tk


def create_main_frame(root):
    main_window = nrf.MainWindowClass(root=root)
    root.title('Алгоритм плавающего горизонта')
    root.resizable(False, False)
    main_window.grid()


def main():
    master = tk.Tk()
    create_main_frame(master)
    master.mainloop()


if __name__ == '__main__':
    main()
