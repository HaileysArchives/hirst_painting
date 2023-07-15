import random
from turtle import Turtle, Screen

tim = Turtle()
tim.speed(1)

rows = 10
cols = 10

color_list = ["blue", "grenn", "red", "purple", "orange", "yellow", "navy"]

for c in range(rows):
    for _ in range(cols):
        tim.dot(20, random.choice(color_list))
        tim.forward(30)
    tim.setheading(90)
    tim.forward(30)
    tim.setheading(180)
    tim.forward(30)
    tim.setheading(0)



screen = Screen()
screen.exitonclick()