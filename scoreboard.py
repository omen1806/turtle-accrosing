from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-30, 250)
        self.level = 1
        self.write(f"LEVEL {self.level}", True, "center", FONT)

    def level_up(self):
        self.clear()
        self.level = +1
        self.write(f"LEVEL {self.level}", True, "center", FONT)

    def game_over(self):
        self.clear()
        self.write("GAME OVER", True, "center", FONT)


