from scoreboard import ScoreBoard
from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600.0, height=600.0)
screen.bgcolor('#013220')

scoreboard = ScoreBoard()
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

    #detect collision with food
    if snake.head.distance(food) < 15: 

        food.refresh()
        snake.new_segment()
        scoreboard.update()

    #detect collision with wall
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:

        scoreboard.collision()
        game_is_on = False

    #detect collision with tail
    if snake.head.distance(snake.segments[2]) < 15:

        scoreboard.collision()
        game_is_on = False

screen.exitonclick()