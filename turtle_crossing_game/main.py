import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
screen.onkey(player.moving_forward, "Up")

car_manager = CarManager()




game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.making_car()
    car_manager.move()
    for i in car_manager.car_list:
        if i.distance(player.asghar) < 20:
            game_is_on = False
            scoreboard.game_over()
            screen.exitonclick()
    if player.success():
        car_manager.next_level()
        scoreboard.increase_level()
    screen.update()


