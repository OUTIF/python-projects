from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,ctuple):
        super().__init__()
        self.shape('square')
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(ctuple)

    def go_up(self):
        new_y = self.ycor()+30
        self.goto(self.xcor(),new_y)
    def go_down(self):
        new_y = self.ycor()-30
        self.goto(self.xcor(), new_y)

    def reset(self,ctuple):
        self.goto(ctuple)