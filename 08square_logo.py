# coding=utf-8
import turtle


# brad = turtle.Turtle()
# a = 1
# b = 1
#
# while a < 1000:
#     if a % 5 == 0:
#         brad.left(10)
#         a += 1
#     else:
#         brad.forward(100)
#         brad.left(90)
#         a += 1

def draw_square(some_turtle):
    some_turtle.color('red')
    some_turtle.speed(4)
    for i in range(4):
        some_turtle.forward(100)
        some_turtle.left(90)
    # some_turtle.left(10)
    # win.exitonclick()

brad = turtle.Turtle()
win = turtle.Screen()
n = 1
while n < 37:
    draw_square(brad)
    brad.left(10)
    n += 1
brad.right(90)
brad.forward(200)
win.exitonclick()
