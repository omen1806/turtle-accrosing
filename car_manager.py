from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(1, 2)
        self.penup()
        self.goto(300, random.randint(-250, 260))

    def car_move(self):
        self.backward(MOVE_INCREMENT)

