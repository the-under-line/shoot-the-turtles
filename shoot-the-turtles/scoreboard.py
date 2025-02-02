from turtle import Turtle

FONT = ("Courier", 30)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=160)
        self.level = 1
        self.high_score = 0
        self.get_high_score()

    def display_level(self, turtles_killed):
        self.clear()
        self.update_high_score()
        self.write(f"Level: {self.level}, High Score: {self.high_score}, Turtles Killed: {turtles_killed}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_high_score()

    def game_over(self, turtles_killed):
        self.clear()
        self.display_level(turtles_killed)
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)

    def get_high_score(self):
        with open("high_score.txt") as data:
            self.high_score = int(data.read())

    def update_high_score(self):
            if self.level > self.high_score:
                self.high_score = self.level
                with open("high_score.txt", mode="w") as data:
                    data.write(str(self.high_score))
                self.get_high_score()


