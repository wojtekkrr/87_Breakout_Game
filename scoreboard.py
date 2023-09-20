from turtle import Turtle
from colors import COLORS


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color(COLORS[0])
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    # Uaktualnienie wyniku
    def update_scoreboard(self):
        self.clear()
        self.goto(-400, -300)
        self.write(self.score, align="center", font=("Courier", 60, "normal"))

    # Dodanie punktu
    def point(self):
        self.score += 1
        self.update_scoreboard()

    # Komunikat koniec gry
    def game_over(self):
        self.clear()
        self.goto(0, - 60)
        self.write(f"Game Over", align="center", font=("Courier", 40, "normal"))
        self.goto(0, - 120)
        self.write(f"Your score is: {self.score}", align="center", font=("Courier", 40, "normal"))
