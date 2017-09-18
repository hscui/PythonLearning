# coding=utf-8
import math

S = 1
n = 1
while n < 100000000:
    S = S + (-1) ** n * (1 / (2 * n + 1))
    n = n + 1
print(S*4)
