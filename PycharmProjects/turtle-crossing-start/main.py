import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
level = Scoreboard()
all_cars = []

screen.listen()
screen.onkey(player.up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    loop = random.randint(0, 7)

    if loop == 6:
        new_car = CarManager()
        all_cars.append(new_car)
        loop = 0

    for car in all_cars:
        car.move_forward()  # Move each car forward

    for car in all_cars:
        if player.distance(car) < 20:
            level.game_over()
            game_is_on = False

    if player.ycor() == player.finish_line:
        player.goto(0, -280)
        level.inc_level()
        for car in all_cars:
            car.move_distance *= 2

screen.update()








screen.exitonclick()