#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *

from functions_answer import *
from interface import *
from constants import *
from draw import *
from solution import *

greeting = "Чтобы нарисовать линию зажмите левую кнопку мыши и проведи в нужное место, затем отпустите.\n" + \
    "Для рисования многоугольника потребуется зажать shift и кликать по холсту, тем самым " + \
    "задаются углы многоугольника. Чтобы замкнуть многоугольник нужно нажать (не отпуская shift) пробел"


def main():
    root = Tk()

    cutter = [[]]  # отсекатель
    contour = [[]]
    temp_contour = []
    settings_interface(root, "1200x800", "Лабораторная работа №9")

    # print_info(greeting)

    canvas_class = paint_class(root)

    figure_selection = selection(2, CHOICE, [1000, 100])

    create_label(root, "Выберите, чем будет являться\n многоугольник,"
                       "вершины которого\n вы будете вводить", [1000, 35])

    create_label(root, "Красным цветом изображен отсекатель", [1000, 325])
    create_label(root, "Синим цветом - отсекаемый многоугольник ", [1000, 360])
    create_label(root, "Зеленым - получившееся отсечение ", [1000, 395])
    create_label(root, "Чтобы ввести отсекатель без\n"
                       "ввода координат просто кликните в\n"
                       "любое место поля. Чтобы ввести\n"
                       "отсекаемый многоугольник, зажмите\n"
                       "Shift после чего кликайте по полю,\n"
                       "не отпуская Shift. Чтобы замкнуть, \n"
                       "нажмите пробел", [1000, 500])

    # create_label(root, "Ввод:", [1000, 425])
    create_label(root, "Введите координаты вершины", [1000, 175])
    create_label(root, "х у через пробел", [1000, 200])
    entry_contour_start = create_entry(root, [1030, 225])
    # create_label(root, "До:", [900, 500])
    # entry_contour_stop = create_entry(root, [1000, 500])
    create_button("Добавить вершину", lambda arg1=temp_contour, arg2=entry_contour_start,
                  arg3=canvas_class, arg4=figure_selection: add_contour(arg1, arg2, arg3, arg4), [1000, 255])

    create_button("Замкнуть", lambda arg1=cutter,  arg2=contour, arg3=temp_contour,
                  arg4=canvas_class, arg5=figure_selection: close_contour(arg1, arg2, arg3, arg4, arg5), [1000, 285])

    create_button("Отсечь", lambda arg1=canvas_class, arg2=cutter, arg3=contour:
                  SolutionWrapper(arg1, arg2, arg3), [1000, 700])

    create_button("Очистить", lambda arg1=canvas_class, arg2=cutter, arg3=contour:
                  clear(arg1, arg2, arg3), [1000, 750])

    settings_bind(canvas_class, cutter, contour)
    root.bind(
        "<Shift-space>", lambda event, arg1=contour: canvas_class.keySpace_rectangle(event, arg1, "blue"))

    root.bind(
        "<space>", lambda event, arg1=cutter: canvas_class.keySpace_rectangle(event, arg1, "red"))

    root.mainloop()


if __name__ == "__main__":
    main()