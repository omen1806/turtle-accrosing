import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

game_is_on = True

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.move, "Up")

cars_names = ["Car"]
cars = []

scoreboard = Scoreboard()
scoreboard.level

for car in cars_names:
   car = CarManager()
   cars.append(car)


while game_is_on:
   game_is_onn = True
   while game_is_onn:
      for car in cars_names:
         number = random.randint(0, 10)
         if number > 5:
            car = CarManager()
            cars.append(car)
         for car in cars:
            if car.distance(player) < 25:
               scoreboard.game_over()
               game_is_on = False
            elif player.ycor() > 280:
               scoreboard.level()
               game_is_onn = False
            car.car_move()
            screen.update()
            time.sleep(0.01)




screen.exitonclick()


