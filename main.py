from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
# from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1200, height=800)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -360))
ball = Ball()

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
        time.sleep(3)




screen.exitonclick()