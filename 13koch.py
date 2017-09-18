# coding=utf-8
import turtle


def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order - 1, size / 3)
            t.left(angle)


brad = turtle.Turtle()
win = turtle.Screen()
koch(brad,5,1000)

win.exitonclick()
