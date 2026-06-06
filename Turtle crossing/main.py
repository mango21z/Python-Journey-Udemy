import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
all_car = []
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.listen()
    screen.onkeypress(player.up, "Up")
    car_manager.spawn_car()
    car_manager.move_car()

    #detect collidion with car
    for car in car_manager.all_car:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #successful crossing
    if player.is_at_finnish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_score()


screen.exitonclick()