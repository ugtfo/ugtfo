import copy
from copy import deepcopy

from interface import print_error
from convex import IsConvex
from constants import *


def GetNodes(polygon):
    nodes = list()
    for i in range(len(polygon)):
        nodes.append([polygon[i][0], polygon[i][1]])
    return nodes


def FindDirection(line):
    return [line[1][0] - line[0][0], line[1][1] - line[0][1]]


def Find_W(p1, p2):
    return [p1[0] - p2[0], p1[1] - p2[1]]


def ConvertParametric(line, t):
    return [round(line[0][0] + (line[1][0] - line[0][0]) * t), round(line[0][1] + (line[1][1] - line[0][1]) * t)]


def IsIntersection(ed1, ed2, peak):
    visiable1 = IsVisiable(ed1[0], ed2[0], ed2[1], peak)
    visiable2 = IsVisiable(ed1[1], ed2[0], ed2[1], peak)
    if not (visiable1 ^ visiable2):
        return False
    N = FindNormal(ed2[0], ed2[1], peak)
    D = FindDirection(ed1)
    W = Find_W(ed1[0], ed2[0])
    DScalar = Scalar(D, N)
    WScalar = Scalar(W, N)
    t = -WScalar/DScalar
    return ConvertParametric(ed1, t)


def Scalar(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]


def FindNormal(peak1, peak2, peak3):
    n = [peak2[1] - peak1[1], peak1[0] - peak2[0]]
    if Scalar([peak3[0] - peak2[0], peak3[1] - peak2[1]], n) < 0:
        n = [-n[0], -n[1]]
    return n


def IsVisiable(point, peak1, peak2, peak3):
    n = FindNormal(peak1, peak2, peak3)
    if Scalar(n, GetVector([peak2, point])) < 0:
        return False
    return True


def GetVector(line):
    return [line[1][0] - line[0][0], line[1][1] - line[0][1]]


def SutherlandHodgman(cutter, polygon):
    cutter.append(cutter[0])
    cutter.append(cutter[1])
    for i in range(len(cutter) - 2):
        new = []  # новый массив вершин
        if IsVisiable(f,  cutter[i], cutter[i + 1], cutter[i + 2]):
            new.append(f)
        s = polygon[0]
        for j in range(1, len(polygon)):
            t = IsIntersection([s, polygon[j]], [cutter[i],
                                                 cutter[i + 1]], cutter[i + 2])
            if t:
                new.append(t)
            s = polygon[j]
            if IsVisiable(s, cutter[i], cutter[i + 1], cutter[i + 2]):
                new.append(s)
        if not len(new):
            return False
        t = IsIntersection([s, f], [cutter[i], cutter[i + 1]], cutter[i + 2])
        if t:
            new.append(t)
        polygon = deepcopy(new)
    return polygon


def SolutionWrapper(canvas_class, cutter, polygon):
    if len(cutter) <= 1:
        print_error("Отсекатель не задан!")
        return

    if len(polygon[0]) <= 1:
        print_error("Многоугольник не задан!")
        return

    sign = IsConvex(cutter)
    if sign == False:
        print_error("Отсекатель не выпуклый!")
        return

    polygon = GetNodes(polygon[0])
    cutter = GetNodes(cutter[0])

    result = SutherlandHodgman(cutter, polygon)

    if not result:
        return

    result.append(result[0])
    for i in range(len(result) - 1):
        canvas_class.draw_line(
            [round(result[i][0]), round(result[i][1]),
             round(result[i+1][0]), round(result[i+1][1])], "green", 2)
