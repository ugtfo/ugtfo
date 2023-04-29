from constants import *

from test import *


def multiplication_code(code1, code2):  # scalar_product
    result = 0
    for i in range(len(code1)):
        result += code1[i] * code2[i]
    return result


def sum_code(code):
    result_sum = 0
    for c in code:
        result_sum += c
    return result_sum


def create_code(point, rectangle):
    result_list = [0, 0, 0, 0]
    # print("point, rectangle = ", point, rectangle)

    result_list[0] = 1 if point[X] < rectangle[LEFT] else 0
    result_list[1] = 1 if point[X] > rectangle[RIGHT] else 0
    result_list[2] = 1 if point[Y] > rectangle[DOWN] else 0
    result_list[3] = 1 if point[Y] < rectangle[UP] else 0

    # print("result_list = ", result_list, "sum_code = ", sum_code(result_list))
    return result_list


def is_visible(code_1, code_2, rectangle):    
    # code_1 = create_code([start[X], start[Y]], rectangle)
    # code_2 = create_code([end[X], end[Y]], rectangle)

    if not sum_code(code_1) and not sum_code(code_2):
        return VISIBLE_LINE

    if multiplication_code(code_1, code_2) != 0:
        return INVISIBLE_LINE

    return PARTLY_VISIBLE_LINE


def cohen_sutherland(line, rectangle):
    flag, m = NORMAL_LINE, 1
    if line[X1] - line[X2] == 0:
        flag = VERTICAL_LINE
    else:
        m = (line[Y2] - line[Y1]) / (line[X2] - line[X1])
        if m == 0:
            flag = HORIZONTAL_LINE

    for i in range(4):
        code_1 = create_code([line[X1], line[Y1]], rectangle)
        code_2 = create_code([line[X2], line[Y2]], rectangle)
        vis = is_visible(code_1, code_2, rectangle)
        if vis == VISIBLE_LINE:
            return line
        elif vis == INVISIBLE_LINE:
            return INVISIBLE_LINE

        if code_1[i] == code_2[i]:
            continue

        if not code_1[i]:
            line[X1], line[Y1], line[X2], line[Y2] = line[X2], line[Y2], line[X1], line[Y1]

        if flag != VERTICAL_LINE:
            if i < 2:
                line[Y1] = m * (rectangle[i] - line[X1]) + line[Y1]
                line[X1] = rectangle[i]
                continue
            else:
                line[X1] = (1 / m) * (rectangle[i] - line[Y1]) + line[X1]
        line[Y1] = rectangle[i]

    return line


def find_solution(line_list, rectangle):
    result_list = list()

    for i in range(len(line_list)):
        res = cohen_sutherland(line_list[i], rectangle)
        if res != INVISIBLE_LINE:
            result_list.append(res)

    return result_list


def solution_wrapper(canvas_class, line_list, contour):
    result_list = find_solution(line_list, contour)
    for i in range(len(result_list)):
        canvas_class.draw_line(result_list[i])
