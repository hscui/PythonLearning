# coding=utf-8
import math
import cmath


def quadratic(a, b, c):
    if not isinstance(a or b or c, (int, float)):
        raise TypeError('请输入数字')
    d = b ** 2 - 4 * a * c
    if d >= 0:
        return round((-b + math.sqrt(d)) / (2 * a), 2), round((-b - math.sqrt(d)) / (2 * a), 2)
    if d < 0:
        return (-b + cmath.sqrt(d)) / (2 * a), (-b - cmath.sqrt(d)) / (2 * a)
