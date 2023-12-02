from turtle import Turtle, Screen
"""creeating our object from our Turtle class"""
tim = Turtle()
"""creeating our object from our Screen class"""
screen = Screen()
screen.listen()  # listen for user inputs

# def move_forward():
#     return tim.forward(10)
#
#
# screen.onkey(key="space", fun=move_forward) # the key keyword argument assigns a button to the function we have defined.
#
# screen.exitonclick()

""" Defining how our turtle object moves below """
def move_forward():
    return tim.forward(10)


def move_backward():
    return tim.backward(10)


def move_counter_clockwise():
    tim.penup()
    tim.right(90)
    tim.pendown()
    return tim.circle(100, 90)


def move_clockwise():
    tim.penup()
    tim.left(90)
    tim.pendown()
    return tim.circle(10, 180)


def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def turn_left():
    tim.heading()
    new_heading = tim.setheading(tim.heading() + 10)


def turn_right():
    tim.heading()
    new_heading = tim.setheading(tim.heading() - 45)

"""assigning butttons on our keyboard to the functions defined above"""
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="q", fun=turn_left)
screen.onkey(key="p", fun=turn_right)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()
