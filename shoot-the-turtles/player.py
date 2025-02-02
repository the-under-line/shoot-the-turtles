from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x=-320, y=0)

    def move_up(self):
        self.sety(self.ycor() + 10)
    def move_down(self):
        self.sety(self.ycor() - 10)




