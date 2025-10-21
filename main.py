from turtle import Turtle,Screen
from  paddle import  Paddle
from ball import Ball
from score_board import Scoreboard
import time

screen=Screen()
score=Scoreboard()
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

screen.listen()
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()





screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

is_game_on=True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #dedect the ball hit the wall bounce
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    #dedect the ball hit the paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    #dedect r side paddle miss
    if ball.xcor()>380:
        ball.reset_position()
        score.l_point()

    #dedect l side paddle miss
    if ball.xcor()<-380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()