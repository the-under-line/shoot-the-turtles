from turtle import Screen
from attack_manager import AttackManager
from player import Player
from bullet import BulletMaker
from scoreboard import Scoreboard
import time
# Create an attack manager class which spawns 5 turtles to move forward on the x-axis

# Create a player class that inherits from turtle that can move up and down and is facing sideways.

#
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 400)
screen.title("Shoot the Turtles!")

screen.textinput(title="How To Play", prompt="Rules:\n1) Shoot as many turtles as you can before they can go past you."
                                             "\n2) If a turtle goes past where you are, you die."
                                             "\n3) As the game goes on, the turtles gain speed and lives. "
                                             "\nIf you hit a turtle on a leg, you remove one life, "
                                             "if you hit it straight down the middle, you remove two lives!"
                                             "\nWhen you are ready, type 'okay' in the box below.")

screen.tracer(0)

attack_manager = AttackManager()
attack_manager.turtle_wave()

user = Player()

scoreboard = Scoreboard()

game_is_on = True
bullet_manager = BulletMaker()

def shoot():
    bullet_manager.create_bullet(player=user)

screen.listen()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.display_level(turtles_killed=attack_manager.attackers_died)
    screen.onkeypress(key="w", fun=user.move_up)
    screen.onkeypress(key="Up", fun=user.move_up)
    screen.onkeypress(key="s", fun=user.move_down)
    screen.onkeypress(key="Down", fun=user.move_down)
    screen.onkeypress(key="Right", fun=shoot)
    screen.onkeypress(key="d", fun=shoot)
    bullet_manager.move_bullets()
    turtle_shot = bullet_manager.detect_collision(targets=attack_manager.attackers)
    if turtle_shot != "False":
        attack_manager.attacker_death(turtle_shot)
        if attack_manager.check_level_complete():
            scoreboard.level_up()
            attack_manager.level_up(scoreboard.level)
    if attack_manager.game_over():
        scoreboard.game_over(attack_manager.attackers_died)
        game_is_on = False
    attack_manager.move_turtles()




screen.exitonclick()
