from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600.0, height=600.0)
screen.bgcolor('#013220')

snake = Snake()

food = Food()

screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.left, 'a')
screen.onkey(snake.down, 's')
screen.onkey(snake.right, 'd')

game_is_on: bool = True
while game_is_on:
    screen.update()
    time.sleep(.01)
    snake.move()

    if snake.head.distance(food) < 15: 

        food.refresh()
        snake.new_segment()

        