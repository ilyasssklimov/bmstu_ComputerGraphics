from algorithms import *
from config import *
import tkinter as tk


class CanvasLines(tk.Canvas):
    def __init__(self, frame):
        self.frame = frame
        self.width = 990
        self.height = 770
        super().__init__(frame, width=self.width, height=self.height, bg='white', highlightbackground='black')

    def clear_canvas(self):
        self.delete('all')

    def draw_pixel(self, x, y, color):
        self.create_rectangle((x, y) * 2, outline='', fill=color)
        # self.create_line(x, y, x + 1, y + 1, fill=color)

    def create_line_by_algo(self, coordinates, algorithm, color):
        # print(f'coordinates = {coordinates}')
        if algorithm == 0:
            self.create_line(*coordinates, fill=color)
        elif algorithm <= 3:
            for value in coordinates:
                self.draw_pixel(value[0], value[1], color)
        elif algorithm <= 5:
            # color_intensity = get_intensity(self, color, 1)
            for value in coordinates:
                # get_intensity(self, color, 255, value[2])
                self.draw_pixel(value[0], value[1], get_intensity(self, color, value[2]))

    def draw_line(self, coordinates, algorithm, color):
        coors = get_coordinates(coordinates)
        if not coors:
            return None
        fill = list(colors.values())[color]
        values = []

        if algorithm == 0:
            # print('You used library')
            values = coors
        elif algorithm == 1:
            # print('You used dda')
            values = dda(coors)
        elif algorithm == 2:
            # print('You used Bresenham (float)')
            values = bresenham_float(coors)
        elif algorithm == 3:
            # print('You used Bresenham (int)')
            values = bresenham_int(coors)
        elif algorithm == 4:
            # print('You used Bresenham (smooth)')
            values = bresenham_smooth(coors, 256)
        elif algorithm == 5:
            # print('You used Wu')
            values = wu(coors)

        self.create_line_by_algo(values, algorithm, fill)

    def create_spectrum(self, length, angle, algorithm, color):
        angle = float(angle)
        length = float(length)

        center_x = self.width // 2
        center_y = self.height // 2

        cur_angle = 0

        while cur_angle < 360:
            cur_angle += angle
            self.draw_line([center_x, center_y, center_x + cos_angle(cur_angle) * length,
                            center_y + sin_angle(cur_angle) * length], algorithm, color)
