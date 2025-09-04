from turtle import Turtle, Screen
from paddle import Paddle
from ball import BALL
from scoreboard import SCOREBOARD
import time
screen = Screen()
screen.tracer(0)
screen.title('PONG GAME')
screen.setup(800, 600)
screen.bgcolor("black")

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = BALL()
score=SCOREBOARD()

screen.listen()
screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')
screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')

def reset():
    ball.reset()
    r_paddle.reset((+350, 0))
    l_paddle.reset((-350, 0))


game_on = 1
while game_on:
    ball_speed = 0.09
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #detect if the ball hit the wall
    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.bounce_y()
    #detect if the ball hit paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect if the ball have passed the paddles
    if ball.xcor()>380:
        score.add_scroe('r')
        reset()
    if ball.xcor()<-380:
        score.add_scroe('l')
        reset()
screen.exitonclick()