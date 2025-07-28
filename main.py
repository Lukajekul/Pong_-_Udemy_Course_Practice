from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))


game_is_on = True

def stop_game():
    global game_is_on
    game_is_on = False

ball = Ball()
score = Score(stop_callback=stop_game)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(score.game_ower, "h")




while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detecting coliton with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    #paddle baounce detection 
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.paddle_bounce()

    #detect when right misses
    if ball.xcor() > 380:
        score.l_point()
        ball.reset_position()

    #detect when left misses
    if ball.xcor() < -380:
        score.r_point()
        ball.reset_position()

    if score.l_score == 10:
        score.l_won()

    if score.r_score == 10:
        score.r_won()

screen.exitonclick()