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
    # Список для всех линий.
    line_list = list()
    contour = [[]]
    temp_contour = []
    settings_interface(root, "1200x800", "Лабораторная работа №8")

    print_info(greeting)

    canvas_class = paint_class(root)

    create_label(root, "Координаты линии:", [1010, 25])
    create_label(root, "Начальные координаты х у через пробел:", [1010, 75])
    entry_line_start = create_entry(root, [1000, 125])
    create_label(root, "Конечные координаты х у через пробел:", [1010, 175])
    entry_line_stop = create_entry(root, [1000, 225])
    create_button("Добавить линию", lambda arg1=line_list, arg2=entry_line_start,
                                           arg3=entry_line_stop, arg4=canvas_class: add_line(arg1, arg2, arg3, arg4),
                  [1000, 275])


    create_label(root, "Ввод контура:", [1010, 400])
    create_label(root, "Вершина контура:", [1010, 425])
    create_label(root, "Координаты х у через пробел:", [1010, 450])
    entry_contour_start = create_entry(root, [1000, 500])
    create_button("Добавить вершину", lambda arg1=temp_contour, arg2=entry_contour_start,
                  arg4=canvas_class: add_contour(arg1, arg2, arg4), [1000, 550])

    create_button("Замкнуть", lambda arg1=temp_contour, arg2=contour,
                  arg3=canvas_class: close_contour(arg1, arg2, arg3), [1000, 600])

    create_button("Отсечь", lambda arg1=canvas_class, arg2=line_list, arg3=contour:
                  SolutionWrapper(arg1, arg2, arg3), [1000, 700])

    create_button("Очистить", lambda arg1=canvas_class, arg2=line_list, arg3=contour:
                  clear(arg1, arg2, arg3), [1000, 750])

    settings_bind(canvas_class, line_list, contour)
    root.bind(
        "<Shift-space>", lambda event, arg1=contour: canvas_class.keySpace_rectangle(event, arg1))

    root.mainloop()


if __name__ == "__main__":
    main()