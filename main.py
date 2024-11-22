from turtle import Turtle, Screen
from snake import Snake

screen = Screen()

screen.setup(width=600.0, height=600.0)

screen.bgcolor('black')

snake = Snake()
snake.create_snake()

screen.exitonclick()