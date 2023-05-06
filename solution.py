from math import *

from interface import print_error
from constants import *
from convex import IsConvex


def scalar(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]


def FindDirection(line):
    return [line[2] - line[0], line[3] - line[1]]


def Find_W(line1, p):
    return [line1[0] - p[0], line1[1] - p[1]]


def GetVector(line):
    return [line[2] - line[0], line[3] - line[1]]


def FindNormal(edge, inc_edge):
    n = [edge[3] - edge[1], edge[0] - edge[2]]
    if scalar(n, GetVector(inc_edge)) < 0:
        n = [-n[0], -n[1]]
    return n


def ConvertParametric(line, t):
    return [line[0] + (line[2] - line[0]) * t, line[1] + (line[3] - line[1]) * t]


def CyrusBeck(edges, line):
    t_b, t_e = 0, 1  # begin, end.
    D = FindDirection(line)
    for i in range(len(edges)):
        W = Find_W(line, edges[i])
        if i == len(edges) - 1:
            N = FindNormal(edges[i], edges[0])
        else:
            N = FindNormal(edges[i], edges[i + 1])
        Dscalar = scalar(D, N)
        Wscalar = scalar(W, N)
        if Dscalar == 0:
            if Wscalar < 0:
                return
        else:
            t = -Wscalar / Dscalar
            if Dscalar > 0:
                if t > 1:
                    return
                else:
                    t_b = max(t_b, t)
            elif Dscalar < 0:
                if t < 0:
                    return
                else:
                    t_e = min(t_e, t)
    if t_e < t_b:
        return
    return [ConvertParametric(line, t_b), ConvertParametric(line, t_e)]


def FindSolution(line_list, edges):
    result_list = list()

    for i in range(len(line_list)):
        temp = CyrusBeck(edges[0], line_list[i])
        if temp:
            result_list.append(temp)

    return result_list


def SolutionWrapper(canvas_class, line_list, polygon):
    sing = IsConvex(polygon)
    if not sing:
        print_error("Многоугольник невыпуклый!")
        return

    result_list = FindSolution(line_list, polygon)

    for i in range(len(result_list)):
        canvas_class.draw_line([result_list[i][0][0], result_list[i]
                                [0][1], result_list[i][1][0], result_list[i][1][1]], "green")
