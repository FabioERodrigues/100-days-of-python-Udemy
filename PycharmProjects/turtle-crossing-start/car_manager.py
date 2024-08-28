from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.goto(270, random.randint(-220, 220))
        self.move_distance = STARTING_MOVE_DISTANCE
        self.setheading(180)  # Set the direction to left (west)


    def move_forward(self):
        self.forward(self.move_distance)  # Move the car forward