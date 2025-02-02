from turtle import Turtle

SPEED = 1.5
MOVE_INCREMENT = 1.5
START_LIVES = 1
LIVES_INCREMENT = 2

class AttackManager:
    def __init__(self):
        self.attackers = []
        self.start_y = 100
        self.attacker_lives = START_LIVES
        global SPEED
        self.speed = SPEED
        self.display_lives = 1
        self.attackers_died = 0

    def turtle_wave(self):
        for x in range(5):
            new_turtle = Turtle(shape="turtle")
            new_turtle.color("green")
            new_turtle.penup()
            new_turtle.goto(x=320, y=self.start_y)
            new_turtle.setheading(180)
            new_turtle.lives = self.attacker_lives
            self.attackers.append(new_turtle)
            self.start_y -= 50
    def move_turtles(self):
        for attacker in self.attackers:
            attacker.forward(self.speed)

    def check_level_complete(self):
        if len(self.attackers) == 0:
            return True
        else:
            return False

    def attacker_death(self, shot_index):
        if self.attackers[shot_index].lives == 1:
            self.attackers[shot_index].goto(1000,1000)
            del self.attackers[shot_index]
            self.attackers_died += 1
        else:
            self.attackers[shot_index].lives -= 1

    def level_up(self, new_level):
        self.start_y = 100
        if new_level % 2 == 0:
            global MOVE_INCREMENT
            self.speed += MOVE_INCREMENT
        else:
            self.attacker_lives += LIVES_INCREMENT
        self.turtle_wave()

    def game_over(self):
        for attacker in self.attackers:
            if attacker.xcor() < -320:
                return True

