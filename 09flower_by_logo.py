# coding=utf-8
import turtle


def draw_flower(some_turtle):
    some_turtle.color('blue')
    some_turtle.speed(7)
    some_turtle.forward(70)
    some_turtle.left(55)
    some_turtle.forward(70)
    some_turtle.left(125)
    some_turtle.forward(70)
    some_turtle.left(55)
    some_turtle.forward(70)
    some_turtle.left(135)


brad = turtle.Turtle()
win = turtle.Screen()
for n in range(37):
    draw_flower(brad)
brad.setheading(270)
brad.forward(200)
win.exitonclick()
