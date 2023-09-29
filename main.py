from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

x_possitions = [(0, 0), (-20, 0), (-40, 0)]
screen.title("Snake Game 🐍")


for possition in x_possitions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(possition)























screen.exitonclick()