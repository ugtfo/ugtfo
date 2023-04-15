#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *

from functions_answer import *
from func_line import *
from interface import *
from constants import *
from draw import *
from fill import *


def main():
    root = Tk()
    points_list = [[]]
    settings_interface(root, "1200x800", "Затравочный алгоритм")

    canvas_class = paint_class(root)
    list_box = create_list_box(root, [800, 325])

    create_button("Выбрать цвет заполнения",
                  canvas_class.choose_color_line, [1000, 25])

    create_button("Выбрать цвет фона",
                  canvas_class.choose_color_line, [1000, 50])

    create_button("Выбрать цвет границы",
                  canvas_class.choose_color_line, [1000, 75])

    create_label(root, "Координаты точки:", [1000, 100])
    entry_point_coordinates = create_entry(root, [1000, 125])

    create_button("Добавить точку", lambda arg1=entry_point_coordinates, arg2=list_box, arg3=canvas_class,
                  arg4=points_list: add_point_entry(arg1, arg2, arg3, arg4), [1000, 165])

    create_button("Замкнуть фигуру", lambda arg1=points_list,
                  arg2=canvas_class, arg3=list_box: lock(arg1, arg2, arg3), [1000, 200])

    create_label(root, "Список точек:", [1000, 230])

    create_label(root, "Координаты \nзатравочной точки:", [1000, 560])
    entry_start_point = create_entry(root, [1000, 600])

    create_button(
        "Выполнить", lambda arg1=canvas_class, arg2=entry_start_point: fill_wrapper(arg1, arg2), [1000, 635])

    create_button(
        "Выполнить с задержкой", lambda arg1=canvas_class, arg2=entry_start_point: fill_wrapper(arg1, arg2, 1), [1000, 675])

    create_button("Очистить", lambda arg1=canvas_class, arg2=list_box, arg3=points_list:
                  clear(arg1, arg2, arg3), [1000, 715])
    canvas_class.canvas.bind("<Button-1>", lambda event,
                             arg1=canvas_class, arg2=list_box, arg3=points_list: add_point_click(event, arg1, arg2, arg3))

    canvas_class.canvas.bind(
        "<Motion>", lambda event: canvas_class.in_canvas(event))

    root.mainloop()


if __name__ == "__main__":
    main()