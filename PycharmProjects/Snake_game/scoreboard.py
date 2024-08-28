from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.scoreshow()


    def scoreshow(self):
        self.clear()
        self.write(f"Score : {self.score} High score: {self.high_score}", False, align=ALIGNMENT, font=FONT)


    #track score
    def track_score(self):
        self.score += 1
        self.clear()
        self.scoreshow()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game over!!", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.scoreshow()


