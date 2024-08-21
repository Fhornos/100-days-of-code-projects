from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.random_location()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)

    def random_location(self):
        random_location = (randint(0, 290), randint(0, 290))
        self.goto(random_location)
