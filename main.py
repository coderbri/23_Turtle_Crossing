import time
from turtle import Screen

from background import draw_ocean, draw_waves, draw_road
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

def setup_screen():
    """Initial screen setup with background elements."""
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("AntiqueWhite")
    screen.title("Turtle Crossing")

    screen.tracer(0)    # ? Disable auto-refresh to optimize animation

    draw_ocean()
    draw_waves()
    draw_road()

    screen.update()     # ? Render all elements instantly
    return screen

screen = setup_screen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_forward, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
