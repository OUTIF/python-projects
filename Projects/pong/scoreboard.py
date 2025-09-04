from turtle import Turtle
FONT_SIZE=80
RSCORE_POSITION=(100,200)
LSCORE_POSITION=(-100,200)
class SCOREBOARD(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.r_score=0
        self.l_score=0
        self.goto(LSCORE_POSITION)
        self.write(self.l_score, align='center', font=('courier', FONT_SIZE, 'normal'))
        self.goto(RSCORE_POSITION)
        self.write(self.r_score, align='center', font=('courier', FONT_SIZE, 'normal'))

    def add_scroe(self, x):
        if x == "l":
            self.l_score +=1
        else:
            self.r_score +=1
        self.clear()
        self.goto(LSCORE_POSITION)
        self.write(self.l_score, align='center', font=('courier', FONT_SIZE, 'normal'))
        self.goto(RSCORE_POSITION)
        self.write(self.r_score, align='center', font=('courier', FONT_SIZE, 'normal'))


