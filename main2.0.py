from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game 🐍")
screen.tracer(0)

snake = Snake()

screen.listen() #listen for keystrokes
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    #Getting the snake to move smoothly
    screen.update()
    time.sleep(0.1)

    snake.move()

        
























screen.exitonclick()