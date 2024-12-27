from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):

        super().__init__()

        self.score = 0

        self.hideturtle()
        self.penup()
        self.goto(0.0, 250.0)
        self.color("White")
        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))

    def update(self): 
        
        self.score += 1
        self.hideturtle()
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))

    def collision(self):

        self.goto(0,0)
        self.write("Game over.", align="center", font=("Arial", 16, "normal"))