from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.increase_score()

    def increase_score(self):
        self.write(
            arg=f"Score : {self.score}",
            move=False,
            align="center",
            font=("arial", 15, "normal"),
        )

    def update_score(self):
        self.score += 1
        self.clear()
        self.increase_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(
            arg="GAME OVER",
            move=False,
            align="center",
            font=("arial", 25, "normal"),
        )