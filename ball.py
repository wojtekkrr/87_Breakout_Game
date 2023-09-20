from turtle import Turtle
from colors import COLORS
from random import randint
import math


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color(COLORS[0])
        self.shape("circle")
        self.penup()
        self.goto(0, 200)
        # Nadanie początkowego kierunku piłce, jako losowy, z pewnego zakresu
        self.dir_degrees = randint(160, 200)
        # Przeliczenie na radiany
        self.dir_rad = self.dir_degrees * math.pi / 180
        self.speed = 10
        self.x_move = self.speed * math.sin(self.dir_rad)
        self.y_move = self.speed * math.cos(self.dir_rad)

    # Przesunięie piłki
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.dir_degrees = 180 - self.dir_degrees

    def bounce_x(self):
        self.dir_degrees *= -1

    # Aktualizacja parametrów ruchu
    def update_moves(self):
        self.dir_rad = self.dir_degrees * math.pi / 180
        self.x_move = self.speed * math.sin(self.dir_rad)
        self.y_move = self.speed * math.cos(self.dir_rad)

    # Nadanie nowego kierunku piłce
    def set_direction(self, new_dir_degrees):
        self.dir_degrees += new_dir_degrees
        self.update_moves()
