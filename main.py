from turtle import Screen
from paddle import Paddle
from ball import Ball
from box import Box
from colors import COLORS
from scoreboard import Scoreboard
import time

# Parametry okna
screen = Screen()
screen.bgcolor(COLORS[5])
screen.setup(width=1200, height=800)
screen.title("Breakout")
screen.tracer(0)

# Generacja obiektów
paddle = Paddle((0, -360))
ball = Ball()
scoreboard = Scoreboard()

# Generacja obiektów box
rows = 4
columns = 11
boxes = []
for i in range(rows):
    for j in range(columns):
        boxes.append(Box((-500 + j / columns * 1100, 300 - i * 20)))

# Możliwość przesuwania odbijaka poprzez przytrzymanie strzałek
screen.listen()
screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.025)
    ball.move()

    # Detect collision with right or left wall
    if ball.xcor() > 590 or ball.xcor() < -590:
        ball.bounce_x()
        ball.update_moves()

    # Detect collision with top wall
    if ball.ycor() > 390:
        ball.bounce_y()
        ball.update_moves()

    # Detect collision with paddle
    if ball.distance(paddle) <= 55 and ball.ycor() <= -335:
        ball.bounce_y()
        # Zmiana kierunku ruchu piłki przy odbiciu
        ball.set_direction((ball.xcor() - paddle.xcor()) / 2)

    # Detect collision with box longer edge
    for box in boxes:
        if ball.distance(box) <= 55 and abs(box.ycor() - ball.ycor()) <= 20:
            ball.bounce_y()
            ball.update_moves()
            box.destroy_box()
            scoreboard.point()

    # Detect paddle misses
    if ball.ycor() < - 420:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
