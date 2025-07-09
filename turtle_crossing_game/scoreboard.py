from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.scoreboard_update()

    def scoreboard_update(self):
        self.write(f"level: {self.level}", font=FONT, align="left")

    def increase_level(self):
        self.level += 1
        self.scoreboard_update()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", font=FONT, align="center")