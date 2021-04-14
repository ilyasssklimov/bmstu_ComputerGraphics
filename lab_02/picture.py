import tkinter as tk
import tkinter.messagebox as mb
from transform import get_oval_point, body_params, head_params, eye_left_params, eye_right_params
from transform import transform, turn_x, turn_y


def error(message):
    mb.showerror('Ошибка', message)


class Cat:
    def __init__(self, canvas):
        self.canvas = canvas
        self.center_x = canvas.width // 2
        self.center_y = canvas.height // 2
        self.ovals_data = {
            'body': get_oval_point(*body_params(self.center_x, self.center_y)),
            'head': get_oval_point(*head_params(self.center_x, self.center_y)),
            'eye_1': get_oval_point(*eye_left_params(self.center_x, self.center_y)),
            'eye_2': get_oval_point(*eye_right_params(self.center_x, self.center_y)),
        }
        self.lines_data = {
            'mustache_1': [self.center_x - 140, self.center_y - 20, self.center_x - 40, self.center_y + 35],
            'mustache_2': [self.center_x - 140, self.center_y + 10, self.center_x - 40, self.center_y + 10],
            'mustache_3': [self.center_x - 140, self.center_y + 40, self.center_x - 40, self.center_y - 15],
            'ear_1': [self.center_x - 105, self.center_y - 30, self.center_x - 95, self.center_y - 55,
                      self.center_x - 85, self.center_y - 40],
            'ear_2': [self.center_x - 75, self.center_y - 40, self.center_x - 65, self.center_y - 55,
                      self.center_x - 55, self.center_y - 30],
            'leg_1': [self.center_x + 10, self.center_y + 60, self.center_x + 10, self.center_y + 110,
                      self.center_x - 15, self.center_y + 110],
            'leg_2': [self.center_x + 110, self.center_y + 60, self.center_x + 110, self.center_y + 110,
                      self.center_x + 135, self.center_y + 110]
        }
        self.initial_lines_data = self.lines_data.copy()
        self.initial_ovals_data = self.ovals_data.copy()
        self.cur_x = 0
        self.cur_y = 0
        self.kx = 1
        self.ky = 1
        self.beta = 0
        self.paint_cat(command=1)

    def create_polygon_line(self, data):
        try:
            for i in range(0, len(data) - 2, 2):
                self.canvas.create_line(data[i], data[i + 1], data[i + 2], data[i + 3], width=2, tag='cat')
        except IndexError:
            print('There are less than 4 points to create line')
        except KeyError:
            print('Incorrect key to create line')

    def create_line_transform(self, name, command):
        try:
            if command == 4:
                data = self.initial_lines_data[name]
                print(data)
                self.create_polygon_line(data)
            else:
                tmp_coordinates = []
                data = self.lines_data[name]
                for i in range(0, len(data), 2):
                    if command == 1:
                        tmp_coordinates.append(data[i] + self.cur_x)
                        tmp_coordinates.append(data[i + 1] + self.cur_y)
                    elif command == 2:
                        tmp_coordinates.append(transform(self.center_x, self.kx, data[i]))
                        tmp_coordinates.append(transform(self.center_y, self.ky, data[i + 1]))
                    elif command == 3:
                        tmp_coordinates.append(turn_x(self.center_x, data[i], self.center_y, data[i + 1], self.beta))
                        tmp_coordinates.append(turn_y(self.center_x, data[i], self.center_y, data[i + 1], self.beta))
                self.lines_data[name] = tmp_coordinates
                self.create_polygon_line(self.lines_data[name])
        except KeyError:
            print('Incorrect key to create line')

    def create_oval_transform(self, name, command):
        try:
            if command == 4:
                data = self.initial_ovals_data[name]
                self.canvas.create_polygon(data, fill='', outline='black', tag='cat', width=2)
            else:
                tmp_coordinates = []
                data = self.ovals_data[name]
                for i in range(0, len(data), 2):
                    if command == 1:
                        tmp_coordinates.append(data[i] + self.cur_x)
                        tmp_coordinates.append(data[i + 1] + self.cur_y)
                    elif command == 2:
                        tmp_coordinates.append(transform(self.center_x, self.kx, data[i]))
                        tmp_coordinates.append(transform(self.center_y, self.ky, data[i + 1]))
                    elif command == 3:
                        tmp_coordinates.append(turn_x(self.center_x, data[i], self.center_y, data[i + 1], self.beta))
                        tmp_coordinates.append(turn_y(self.center_x, data[i], self.center_y, data[i + 1], self.beta))
                self.ovals_data[name] = tmp_coordinates
                self.canvas.create_polygon(self.ovals_data[name], fill='', outline='black', tag='cat', width=2)
        except KeyError:
            print('Incorrect key to create oval')

    def paint_cat(self, command):
        self.canvas.delete('cat')

        self.create_oval_transform('body', command)
        self.create_oval_transform('head', command)
        self.create_oval_transform('eye_1', command)
        self.create_oval_transform('eye_2', command)

        self.create_line_transform('mustache_1', command)
        self.create_line_transform('mustache_2', command)
        self.create_line_transform('mustache_3', command)
        self.create_line_transform('ear_1', command)
        self.create_line_transform('ear_2', command)
        self.create_line_transform('leg_1', command)
        self.create_line_transform('leg_2', command)


class CanvasPicture(tk.Canvas):
    def __init__(self, frame):
        self.frame = frame
        self.width = 700
        self.height = 700
        self.center_x = self.width // 2 - 140 + 150
        self.center_y = self.height // 2 - 70 + 90
        super().__init__(frame, width=self.width, height=self.height, bg='white', highlightbackground='black')
        self.cat = Cat(self)
        self.paint_system()
        self.commands = []

    def paint_system(self):
        self.create_line(10, 10, 10, self.height, arrow=tk.LAST, width=2)
        self.create_line(10, 10, self.width, 10, arrow=tk.LAST, width=2)
        for i in range(50 + 10, self.height - 1, 50):
            self.create_line(10 - 5, i, 10 + 5, i, width=2)
            self.create_line(i, 10 - 5, i, 10 + 5, width=2)

    def carryover_cat(self, x_str, y_str, label, revert=False):
        try:
            x = float(x_str)
        except ValueError:
            return error('Количество пикселей для переноса по оси абсцисс может быть только числом, '
                         'и не должны пристуствовать иные символы, кроме минуса, точки и цифр')
        try:
            y = float(y_str)
        except ValueError:
            return error('Количество пикселей для переноса по оси ординат может быть только числом, '
                         'и не должны присутствовать иные символы, кроме минуса, точки и цифр')

        if not revert:
            self.commands.append((1, x, y))
        self.center_x += x
        self.center_y += y
        label['text'] = f'Центральная точка объекта: ({self.center_x}; {self.center_y})'
        self.cat.cur_x = x
        self.cat.cur_y = y
        self.cat.kx = 1
        self.cat.ky = 1
        self.cat.beta = 0
        self.cat.paint_cat(command=1)
        self.cat.cur_x = 0
        self.cat.cur_y = 0

    def scale_cat(self, x_center_str, y_center_str, kx_xtr, ky_str, label, revert=False):
        try:
            x_center = float(x_center_str)
        except:
            return error('Кордината X точки центра масштабирования может быть только числом, '
                         'и не должны присутствовать иные символы, кроме минуса, точки и цифр')
        try:
            y_center = float(y_center_str)
        except:
            return error('Кордината Y точки центра масштабирования может быть только числом, '
                         'и не должны присутствовать иные символы, кроме минуса, точки и цифр')
        try:
            kx = float(kx_xtr)
        except:
            return error('Коэффициент масштабированияи KX может быть только числом, '
                         'и не должны присутствовать иные символы, кроме минуса, точки и цифр')
        try:
            ky = float(ky_str)
        except:
            return error('Коэффициент масштабированияи KY может быть только числом, '
                         'и не должны присутствовать иные символы, кроме минуса, точки и цифр')

        if not revert:
            self.commands.append((2, x_center, y_center, kx, ky))

        self.center_x = x_center
        self.center_y = y_center
        label['text'] = f'Центральная точка объекта: ({self.center_x}; {self.center_y})'
        self.cat.kx = kx
        self.cat.ky = ky
        self.cat.center_x = x_center
        self.cat.center_y = y_center
        self.cat.beta = 0
        self.cat.paint_cat(command=2)

    def turn_cat(self, x_center_str, y_center_str, beta_str, revert=False):
        try:
            x_center = float(x_center_str)
        except:
            return error('Кордината X точки центра переноса может быть только числом, '
                         'и не должны присутствовать иные символы, кроме минуса, точки и цифр')
        try:
            y_center = float(y_center_str)
        except:
            return error('Кордината Y точки центра переноса может быть только числом, '
                         'и не должны присутствовать иные символы, кроме минуса, точки и цифр')
        try:
            beta = float(beta_str)
        except:
            return error('Угол поворота может быть только числом, '
                         'и не должны присутствовать иные символы, кроме минуса, точки и цифр')
        if not revert:
            self.commands.append((3, x_center, y_center, beta))
        self.cat.center_x = x_center
        self.cat.center_y = y_center
        self.cat.beta = beta % 360
        self.cat.kx = 1
        self.cat.ky = 1
        self.cat.paint_cat(command=3)

    def revert_command(self, label):
        try:
            last_command = self.commands.pop()
        except IndexError:
            return error('Вы вернулись к изначальному изображению')

        if last_command[0] == 1:
            self.carryover_cat(-(last_command[1]), -(last_command[2]), label, revert=True)
        elif last_command[0] == 2:
            if last_command[3] and last_command[4]:
                kx = 1 / last_command[3]
                ky = 1 / last_command[4]
                self.scale_cat(last_command[1], last_command[2], kx, ky, label, revert=True)
            else:
                self.cat.ovals_data = self.cat.initial_ovals_data.copy()
                self.cat.lines_data = self.cat.initial_lines_data.copy()
                self.cat.cur_x = 0
                self.cat.cur_y = 0
                self.cat.kx = 1
                self.cat.ky = 1
                self.cat.beta = 0
                self.cat.paint_cat(command=1)
                for command in self.commands:
                    if command[0] == 1:
                        self.carryover_cat(command[1], command[2], label, revert=True)
                    elif command[0] == 2:
                        self.scale_cat(command[1], command[2], command[3], command[4], label, revert=True)
                    elif command[0] == 3:
                        self.turn_cat(command[1], command[2], command[3], revert=True)

        elif last_command[0] == 3:
            self.turn_cat(last_command[1], last_command[2], -(last_command[3]), revert=True)

