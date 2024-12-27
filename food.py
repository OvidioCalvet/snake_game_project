from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self) -> None:
        
        super().__init__()

        self.shape('circle')
        self.color('white')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed('fastest')
        self.refresh()

    def refresh(self):

        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)

        self.goto(rand_x, rand_y)