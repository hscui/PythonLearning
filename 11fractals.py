# coding=utf-8
import turtle


def draw_triangle(some_turtle, vertice=120, edge=160, color_filled='green'):
    some_turtle.color('black', color_filled)
    if vertice == 120:
        some_turtle.begin_fill()
        some_turtle.forward(edge)
        some_turtle.left(120)
        some_turtle.forward(edge)
        some_turtle.left(120)
        some_turtle.forward(edge)
        some_turtle.end_fill()
    else:
        some_turtle.begin_fill()
        some_turtle.left(60)
        some_turtle.forward(edge)
        some_turtle.left(120)
        some_turtle.forward(edge)
        some_turtle.left(120)
        some_turtle.forward(edge)
        some_turtle.end_fill()
        # some_turtle.home()


# def draw_fractals(some_turtle):
#



brad = turtle.Turtle()
win = turtle.Screen()
draw_triangle(brad, 120, 240,'blue')
brad.left(120)
# for i in range(3):
#     brad.forward(30)
#     draw_triangle(brad, 60, 30, 'white')
#     brad.left(60)
#     brad.forward(30)
#     draw_triangle(brad, 60, 60, 'white')
#     brad.left(60)
#     brad.forward(30)
#     draw_triangle(brad, 60, 30, 'white')
#     brad.left(60)
#     brad.forward(30)
#     draw_triangle(brad, 60, 120, 'white')
#     brad.left(60)
#     brad.forward(30)
#     draw_triangle(brad, 60, 30, 'white')
#     brad.left(60)
#     brad.forward(30)
#     draw_triangle(brad, 60, 60, 'white')
#     brad.left(60)
#     brad.forward(30)
#     draw_triangle(brad, 60, 30, 'white')
#     brad.left(60)
#     brad.forward(30)
#     brad.left(120)

win.exitonclick()
