from turtle import Turtle

class BulletMaker:
    def __init__(self):
        self.bullets = []

    def create_bullet(self, player):
        new_bullet = Turtle(shape="circle")
        new_bullet.shapesize(stretch_wid=0.25, stretch_len=0.25)
        new_bullet.color("white")
        new_bullet.penup()
        self.bullets.append(new_bullet)
        new_bullet.goto(player.position())

    def move_bullets(self):
        for bullet in self.bullets:
            bullet.forward(20)

    def detect_collision(self, targets):
        for bullet in self.bullets:
            for target in targets:
                if bullet.distance(target) < 20:
                    return targets.index(target)
        return "False"
