# TODO:  THE SNAKE GAME

"""
1. Create the snake body 
2. Moving the snake body
3. Makeing a food randomly
4. Handling the food and snake clash  
5. Creating the score board 
6. Detecting the Border
7. Showing the Game over 
8. Adding the segments 
9. Detecting head and body collusion
10. End the

"""

from turtle import Screen
from random import choice
from time import sleep
import turtle
from food import Food
from snake import Snake
from score import Score


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snack Game")


screen.tracer(0)  # to turn off the screen / not refresh the screen
is_game_on = True


snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


while is_game_on:
    screen.update()  # to turn on the screen / refresh the screen
    sleep(0.09)
    snake.move()
    if snake.head.distance(food) < 20:  # Detect collision with food
        food.refresh()
        snake.extend()
        score.update_score()
    if (
        snake.head.xcor() > 288
        or snake.head.xcor() < -299
        or snake.head.ycor() > 288
        or snake.head.ycor() < -295
    ):
        is_game_on = False
        score.game_over()

    for segment in snake.segment:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()


screen.exitonclick()