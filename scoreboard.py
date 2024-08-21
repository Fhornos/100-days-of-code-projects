from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.score = 0
        self.goto((-40, 270))
        self.scored()

    def scored(self):
        self.clear()
        self.write(f"Current Score = {self.score}", font=("Arial", 9, "normal"))
        self.score += 1

    def game_over(self):
        self.goto(-40, 0)
        self.penup()
        self.pencolor("white")
        self.write("GAME OVER.", font=("Arial", 10, "normal"))
