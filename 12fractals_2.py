# coding=utf-8
import turtle


def fractals(t, order, length):
    # t.color('black', corlor_filled)
    if order == 0:
        t.forward(length)
    else:
        for angle in [120, -120, -120, 120, 0]:
            fractals(t, order - 1, length / 2)
            t.left(angle)


brad = turtle.Turtle()
win = turtle.Screen()
brad.fillcolor('green')
brad.begin_fill()
fractals(brad, 5, 360)
brad.left(120)
brad.forward(360)
brad.left(120)
brad.forward(360)
brad.end_fill()
win.exitonclick()
