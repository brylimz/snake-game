from turtle import Turtle


class  Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.write(F"Score: {self.score}", align="center", font=("Arial", 24, "normal")
                   )