from turtle import Turtle
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in STARTING_POS:
            self.add_segment(position)

    def add_segment(self, position):
            new_segment = Turtle("square")
            new_segment.color("green")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def reset(self):
        for segment in self.segments: #loop through the current segments of the snake and move to off the screen
            segment.goto(1000,1000)
        self.segments.clear() #clears all the segments from the list
        self.create_snake() #Initializes a new 3 segment snake
        self.head = self.segments[0] #Makes the first segment the head of snake

    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)
    
#Conditional statements to prevent the snake from going backwards on itself, just like the actual game

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

