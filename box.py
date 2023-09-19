from turtle import Turtle
from colors import COLORS
from random import choice


class Box(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color(choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)

    def destroy_box(self):
        self.goto(10000,10000)
