from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from box import Box
# from scoreboard import Scoreboard
import time
from colors import COLORS
import math


screen = Screen()
screen.bgcolor("black")
screen.setup(width=1200, height=800)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -360))
ball = Ball()

rows = 5
columns = 11
for i in range(rows):
    for j in range(columns):
        exec(f"box_{j + 1 + i * columns} = Box(({-500 + j / columns * 1100}, {300 - i * 20}))")



screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.05)

    # Detect collision with right or left wall
    if ball.xcor() > 580 or ball.xcor() < -580:
        ball.bounce_x()

    # Detect collision with top wall
    if ball.ycor() > 380:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(paddle) <= 50 and ball.ycor() == -340:
        ball.bounce_y()

    # Detect collision with box
    for i in range(55):
        if ball.distance(locals()[f'box_{i + 1}']) <= 50 and abs(locals()[f'box_{i + 1}'].ycor() - ball.ycor()) == 20:
            ball.bounce_y()




screen.exitonclick()