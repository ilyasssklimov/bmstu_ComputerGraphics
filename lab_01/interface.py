from my_math import find_result, delete_pair, change_pair, find_index
import math
import tkinter as tk
from tkinter import messagebox as mb
from tkinter import ttk

COORDINATES_X_1 = []
COORDINATES_Y_1 = []
COORDINATES_X_2 = []
COORDINATES_Y_2 = []


def error(message):
    mb.showerror('Ошибка', message)


def transform(center_t, kt, t):
    return int(kt * t + center_t * (1 - kt))


class EditWindow(tk.Tk):
    def __init__(self, table, width, height, num, canvas):
        super().__init__()
        self.title = 'Изменение координаты'
        self.num = num
        self.resizable(False, False)
        self.width = width
        self.height = height
        self.table = table
        self.canvas = canvas
        self.entry_edit_x, self.entry_edit_y = self.add_widgets(table.item(table.selection()[0])['values'])

    def add_widgets(self, values):
        label_num = tk.Label(self, text=f'№ {values[0]}', font='Times 20')
        label_num.grid(row=0, column=0, padx=3, pady=3)
        entry_edit_x = tk.Entry(self, font='Times 20', width=10)
        entry_edit_x.insert(0, values[1])
        entry_edit_x.grid(row=0, column=1, padx=3, pady=3)
        entry_edit_y = tk.Entry(self, font='Times 20', width=10)
        entry_edit_y.insert(0, values[2])
        entry_edit_y.grid(row=0, column=2, padx=3, pady=3)
        button_prompt = tk.Button(self, text='Подтвердить изменения', font='Times 15',
                                  command=lambda: self.confirm_edit(values, entry_edit_x.get(),
                                                                    entry_edit_y.get(), self.table, self.canvas))
        button_prompt.grid(row=1, column=0, columnspan=3, sticky='wens', pady=5, padx=5)
        return entry_edit_x, entry_edit_y

    def confirm_edit(self, value, x_str, y_str, table, canvas):
        try:
            x = float(x_str)
            y = float(y_str)
        except ValueError:
            self.destroy()
            return error('Координаты могут быть только числами')
        except:
            self.destroy()
            return error('Некорректные значения координат')

        table.item(table.selection()[0], text=value[0], values=(str(value[0]), x, y))
        value = list(map(float, value[1:]))
        if self.num == 1:
            change_pair(COORDINATES_X_1, COORDINATES_Y_1, value, list(map(float, [x, y])))
            canvas.delete(f'1,{value[0]},{value[1]}')
            canvas.delete('bisector')
            canvas.delete('text')
            canvas.paint_dot(x, y, self.width, self.height, 1, 'blue')
        elif self.num == 2:
            change_pair(COORDINATES_X_2, COORDINATES_Y_2, value, list(map(float, [x, y])))
            canvas.delete(f'2,{value[0]},{value[1]}')
            canvas.delete('bisector')
            canvas.delete('text')
            canvas.paint_dot(x, y, self.width, self.height, 2, 'red')

        self.destroy()


class TableCoordinates(ttk.Treeview):
    def __init__(self, frame):
        super().__init__(frame, show='headings', columns=('#1', '#2', '#3'), height=15)
        self.heading('#1', text='№')
        self.column('#1', width=30)
        self.heading('#2', text='X')
        self.column('#2', width=80)
        self.heading('#3', text='Y')
        self.column('#3', width=80)

    def delete_coordinate(self, canvas, num, label):
        try:
            selected_coordinate = self.selection()[0]
        except IndexError:
            return error('Выберите точку, которую желаете удалить')
        except:
            return error('Некорректное действие')

        value = self.item(selected_coordinate)['values']
        self.delete(selected_coordinate)
        canvas.delete(f'{num},{value[1]},{value[2]}')
        canvas.delete('bisector')
        canvas.delete('text')
        label['text'] = 'Ожидание результата'
        value = list(map(float, value))
        if num == 1:
            global COORDINATES_X_1, COORDINATES_Y_1
            delete_pair(COORDINATES_X_1, COORDINATES_Y_1, value[1:])

        elif num == 2:
            global COORDINATES_X_2, COORDINATES_Y_2
            delete_pair(COORDINATES_X_2, COORDINATES_Y_2, value[1:])

        coordinates = self.get_children()
        for i, coordinate in enumerate(coordinates):
            value = self.item(coordinate)['values']
            self.item(coordinate, text=i, values=(str(i + 1), value[1], value[2]))

    def delete_all(self, canvas, num, label):
        coordinates = self.get_children()
        for coordinate in coordinates:
            self.delete(coordinate)

        canvas.delete(f'set_{num}')
        canvas.delete('bisector')
        label['text'] = 'Ожидание результата'

        global COORDINATES_X_1, COORDINATES_Y_1, COORDINATES_X_2, COORDINATES_Y_2
        if num == 1:
            COORDINATES_X_1 = []
            COORDINATES_Y_1 = []
        elif num == 2:
            COORDINATES_X_2 = []
            COORDINATES_Y_2 = []

    def edit_item(self, num, canvas, label):
        edit_window = EditWindow(self, canvas.width, canvas.height, num, canvas)
        label['text'] = 'Ожидание результата'
        edit_window.mainloop()


class CanvasSet(tk.Canvas):
    def __init__(self, frame):
        self.frame = frame
        self.width = 700
        self.height = 700
        self.k = 5
        self.center_x = self.width // 2
        self.center_y = self.height // 2
        super().__init__(frame, width=self.width, height=self.height, bg='white', highlightbackground='black')
        self.create_coordinate_system(self.width, self.height)

    def create_coordinate_system(self, width, height):
        self.delete_coordinate_system()
        self.create_line(width / 2, height, width / 2, 0, arrow=tk.LAST, tag='system')
        self.create_line(0, height / 2, width, height / 2, arrow=tk.LAST, tag='system')

    def delete_coordinate_system(self):
        self.delete('system')

    def paint_dot(self, x, y, width, height, num, color):
        self.create_oval(x * self.k + width / 2 - 3, -y * self.k + width / 2 - 3,
                         x * self.k + width / 2 + 3, -y * self.k + height / 2 + 3, fill=color,
                         tags=(f'set_{num}', f'{num},{x},{y}'))

    def paint_points(self, x1, y1, x2, y2, width, height):
        self.delete('set_1')
        self.delete('set_2')

        for x, y in zip(x1, y1):
            self.paint_dot(x, y, width, height, 1, 'blue')

        for x, y in zip(x2, y2):
            self.paint_dot(x, y, width, height, 2, 'red')

    def add_coordinates(self, entry_field, num, table):
        self.create_coordinate_system(self.width, self.height)
        self.paint_points(COORDINATES_X_1, COORDINATES_Y_1, COORDINATES_X_2, COORDINATES_Y_2, self.width, self.height)
        self.center_x = self.width // 2
        self.center_y = self.height // 2

        coordinates = entry_field.get().split()
        entry_field.delete(0, 'end')
        if len(coordinates) > 2:
            return error('Координат должно быть ровно две')
        try:
            x = float(coordinates[0])
            y = float(coordinates[1])
        except IndexError:
            return error('Должно быть введено две координаты через пробел')
        except ValueError:
            return error('Координаты должны быть числами')
        except:
            return error('Некорректные значения координат')

        self.delete('bisector')
        if num == 1:
            COORDINATES_X_1.append(x)
            COORDINATES_Y_1.append(y)
            table.insert("", tk.END, values=[len(COORDINATES_X_1), x, y])
            self.paint_dot(x, y, self.width, self.height, 1, 'blue')

        elif num == 2:
            COORDINATES_X_2.append(x)
            COORDINATES_Y_2.append(y)
            table.insert("", tk.END, values=[len(COORDINATES_X_2), x, y])
            self.paint_dot(x, y, self.width, self.height, 2, 'red')

    def create_line_carryover(self, x, y, i, j, color):
        self.create_line(x[i] * self.k + self.width / 2, -y[i] * self.k + self.height / 2,
                         x[j] * self.k + self.width / 2, -y[j] * self.k + self.height / 2, fill=color,
                         tag='bisector')

    def create_line_bisector(self, vertex, dot, color):
        self.create_line(vertex[0] * self.k + self.width / 2, -vertex[1] * self.k + self.height / 2,
                         dot[0] * self.k + self.width / 2, -dot[1] * self.k + self.height / 2, fill=color,
                         tag='bisector')

    def result(self, x1, y1, x2, y2, label):
        self.delete('bisector')
        self.delete('text')
        try:
            triangles, bisectors, minimum_angle = find_result(x1, y1, x2, y2)
            if not triangles or not bisectors:
                raise ValueError
        except ValueError:
            return error('Проверьте, что в каждом из множеств из указанных точек можно построить треугольник '
                         '(минимум три точки, не лежащие на одной прямой)')
        triangle_first_x = triangles[0][0]
        triangle_first_y = triangles[0][1]
        triangle_second_x = triangles[1][0]
        triangle_second_y = triangles[1][1]
        bisector_first = bisectors[0]
        bisector_second = bisectors[1]

        self.scale_result(triangle_first_x + triangle_second_x, triangle_first_y + triangle_second_y)

        self.create_line_carryover(triangle_first_x, triangle_first_y, 0, 1, 'blue')
        self.create_line_carryover(triangle_first_x, triangle_first_y, 1, 2, 'blue')
        self.create_line_carryover(triangle_first_x, triangle_first_y, 2, 0, 'blue')
        self.create_line_bisector((triangle_first_x[0], triangle_first_y[0]), bisector_first, 'green')
        self.create_line_bisector((triangle_first_x[1], triangle_first_y[1]), bisector_first, 'green')
        self.create_line_bisector((triangle_first_x[2], triangle_first_y[2]), bisector_first, 'green')
        self.create_oval(bisector_first[0] * self.k + self.width / 2 - 3,
                         -bisector_first[1] * self.k + self.height / 2 - 3,
                         bisector_first[0] * self.k + self.width / 2 + 3,
                         -bisector_first[1] * self.k + self.height / 2 + 3,
                         tag='bisector', fill='green')

        self.create_line_carryover(triangle_second_x, triangle_second_y, 0, 1, 'red')
        self.create_line_carryover(triangle_second_x, triangle_second_y, 1, 2, 'red')
        self.create_line_carryover(triangle_second_x, triangle_second_y, 2, 0, 'red')
        self.create_line_bisector((triangle_second_x[0], triangle_second_y[0]), bisector_second, 'orange')
        self.create_line_bisector((triangle_second_x[1], triangle_second_y[1]), bisector_second, 'orange')
        self.create_line_bisector((triangle_second_x[2], triangle_second_y[2]), bisector_second, 'orange')
        self.create_oval(bisector_second[0] * self.k + self.width / 2 - 3,
                         -bisector_second[1] * self.k + self.height / 2 - 3,
                         bisector_second[0] * self.k + self.width / 2 + 3,
                         -bisector_second[1] * self.k + self.height / 2 + 3,
                         tag='bisector', fill='orange')
        self.create_line_bisector(bisector_first, bisector_second, 'brown')

        self.create_text(triangle_first_x[0] * self.k + self.width / 2 + 10,
                         -triangle_first_y[0] * self.k + self.height / 2 - 10,
                         text=f'({triangle_first_x[0]}; {triangle_first_y[0]})', tags=('set_2', 'text'))
        self.create_text(triangle_first_x[1] * self.k + self.width / 2 + 10,
                         -triangle_first_y[1] * self.k + self.height / 2 - 10,
                         text=f'({triangle_first_x[1]}; {triangle_first_y[1]})', tags=('set_2', 'text'))
        self.create_text(triangle_first_x[2] * self.k + self.width / 2 + 10,
                         -triangle_first_y[2] * self.k + self.height / 2 - 10,
                         text=f'({triangle_first_x[2]}; {triangle_first_y[2]})', tags=('set_2', 'text'))

        self.create_text(triangle_second_x[0] * self.k + self.width / 2 + 10,
                         -triangle_second_y[0] * self.k + self.height / 2 - 10,
                         text=f'({triangle_second_x[0]}; {triangle_second_y[0]})', tags=('set_2', 'text'))
        self.create_text(triangle_second_x[1] * self.k + self.width / 2 + 10,
                         -triangle_second_y[1] * self.k + self.height / 2 - 10,
                         text=f'({triangle_second_x[1]}; {triangle_second_y[1]})', tags=('set_2', 'text'))
        self.create_text(triangle_second_x[2] * self.k + self.width / 2 + 10,
                         -triangle_second_y[2] * self.k + self.height / 2 - 10,
                         text=f'({triangle_second_x[2]}; {triangle_second_y[2]})', tags=('set_2', 'text'))

        text_1 = f'Два треугольника успешно найдены:\n\nКоординаты точек треугольника из первого\nмножества:\n'
        text_2 = f'\n№{find_index(COORDINATES_X_1, COORDINATES_Y_1, (triangle_first_x[0], triangle_first_y[0]))} -> ' \
                 f'({triangle_first_x[0]}; {triangle_first_y[0]})' \
                 f'\n№{find_index(COORDINATES_X_1, COORDINATES_Y_1, (triangle_first_x[1], triangle_first_y[1]))} -> ' \
                 f'({triangle_first_x[1]}; {triangle_first_y[1]})' \
                 f'\n№{find_index(COORDINATES_X_1, COORDINATES_Y_1, (triangle_first_x[2], triangle_first_y[2]))} -> ' \
                 f'({triangle_first_x[2]}; {triangle_first_y[2]})\n'
        text_3 = f'\nКоординаты точек тругольника из второго\nмножества:\n'
        text_4 = f'\n№{find_index(COORDINATES_X_2, COORDINATES_Y_2, (triangle_second_x[0], triangle_second_y[0]))} -> '\
                 f'({triangle_second_x[0]}; {triangle_second_y[0]})' \
                 f'\n№{find_index(COORDINATES_X_2, COORDINATES_Y_2, (triangle_second_x[1], triangle_second_y[1]))} -> '\
                 f'({triangle_second_x[1]}; {triangle_second_y[1]})' \
                 f'\n№{find_index(COORDINATES_X_2, COORDINATES_Y_2, (triangle_second_x[2], triangle_second_y[2]))} -> '\
                 f'({triangle_second_x[2]}; {triangle_second_y[2]})'
        text_5 = f'\n\nКоординаты точки пересчения биссектрис\nпервого треугольника:\n'
        text_6 = f'({round(bisector_first[0], 2)}; {round(bisector_first[1], 2)})'
        text_7 = f'\n\nКоординаты точки пересчения биссектрис\nвторого треугольника:\n'
        text_8 = f'({round(bisector_second[0], 2)}; {round(bisector_second[1], 2)})'
        text_9 = f'\n\nУгол наклона отрезка, соединяющего точки\nпересечения биссектрис к оси ординат:\n'
        text_10 = f'{round(90 - math.degrees(math.atan(1 / minimum_angle)), 2)}'
        text_11 = f'\n\n\nОбозначения:\nСиний цвет - первое множество\nКрасный цвет - второе множество\n' \
                  f'Зеленый цвет - биссектрисы треугольника\nв первом множестве\n' \
                  f'Оранжевый цвет - биссектрисы треугольника\nво втором множестве\n' \
                  f'Коричневый цвет - отрезок, соединяющий\nточки пересения биссектрис'
        text_result = text_1 + text_2 + text_3 + text_4 + text_5 + text_6 + text_7 + text_8 + text_9 + text_10 + text_11
        label['text'] = text_result

    def scale_result(self, x, y):
        x_abs = [abs(elem) for elem in x]
        y_abs = [abs(elem) for elem in y]
        max_x = max(x_abs)
        max_y = max(y_abs)
        dif_x = (self.width / 2 - 20) / abs(max_x)
        dif_y = (self.height / 2 - 20) / abs(max_y)
        self.k = min(dif_x, dif_y)
        self.create_coordinate_system(self.width, self.height)
        self.delete('set_1')
        self.delete('set_2')
        self.paint_points(COORDINATES_X_1, COORDINATES_Y_1, COORDINATES_X_2, COORDINATES_Y_2, self.width, self.height)

    def delete_all(self, table_first, table_second, label):
        table_first.delete_all(self, 1, label)
        table_second.delete_all(self, 2, label)


class MainFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.canvas = CanvasSet(self)
        self.table_first = TableCoordinates(self)
        self.table_second = TableCoordinates(self)
        self.add_input()
        self.add_canvas()
        self.add_table(1)
        self.add_table(2)
        self.add_result_widgets()

    def add_input(self):
        entry_to_set = tk.Entry(self, font='Times 15')
        entry_to_set.grid(row=0, column=0, columnspan=2, pady=5, sticky='wens')

        button_first = tk.Button(self, text='Добавить в первое множество',
                                 command=lambda: self.canvas.add_coordinates(entry_to_set, 1, self.table_first))
        button_first.grid(row=1, column=0, sticky='wens')

        button_second = tk.Button(self, text='Добавить во второе множество',
                                  command=lambda: self.canvas.add_coordinates(entry_to_set, 2, self.table_second))
        button_second.grid(row=1, column=1, sticky='wens')

    def add_canvas(self):
        self.canvas.grid(row=0, rowspan=8, column=5, padx=10, pady=10)

    def add_table(self, num):
        if num == 1:
            column = 0
            table = self.table_first
        else:
            column = 1
            table = self.table_second
        table.grid(row=2, column=column)
        button_delete = tk.Button(self, text='Удалить точку', command=lambda: table.delete_coordinate(self.canvas, num,
                                                                                                      self.label_result)
                                  )
        button_delete.grid(row=3, column=column, sticky='wens')

        button_edit = tk.Button(self, text='Изменить точку', command=lambda: table.edit_item(num, self.canvas,
                                                                                             self.label_result))
        button_edit.grid(row=4, column=column, sticky='wens')

        button_all_delete = tk.Button(self, text='Удалить все точки',
                                      command=lambda: table.delete_all(self.canvas, num, self.label_result))
        button_all_delete.grid(row=5, column=column, sticky='wens')

    def add_result_widgets(self):
        button_result = tk.Button(self, text='Вывести результат',
                                  command=lambda: self.canvas.result(COORDINATES_X_1, COORDINATES_Y_1,
                                                                     COORDINATES_X_2, COORDINATES_Y_2,
                                                                     self.label_result))
        button_result.grid(row=7, column=0, columnspan=2, pady=5, sticky='wens')

        button_clean_all = tk.Button(self, text='Удалить точки обоих множеств',
                                     command=lambda: self.canvas.delete_all(self.table_first, self.table_second,
                                                                            self.label_result))
        button_clean_all.grid(row=6, column=0, columnspan=2, sticky='wens')

        self.label_result = tk.Label(self, text='Ожидание результата', font='Times 13',
                                width=40, borderwidth=3, relief='sunken')
        self.label_result.grid(row=0, column=6, rowspan=8, padx=10, pady=10, sticky='wens')
