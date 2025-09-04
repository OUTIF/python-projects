from turtle import Turtle

class BALL(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.X_MOVE = 10
        self.Y_MOVE = 10
        self.move_speed=0.1
    def move(self):
        newx = self.xcor() + self.X_MOVE
        newy = self.ycor() + self.Y_MOVE
        self.goto(newx, newy)


    def bounce_y(self):
        self.Y_MOVE *= -1
    def bounce_x(self):
        self.X_MOVE *= -1
        self.move_speed *= 0.9
    def reset(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1
