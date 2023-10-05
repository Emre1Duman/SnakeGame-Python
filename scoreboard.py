from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        #open file with read permisions, and set the high score to the data provided
        with open("/Users/emre/Documents/Code/100DaysOfPython/Day11-20/Day20/data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score: #Adds the score to high score if it is greater
            self.high_score = self.score
            #saves the latest high score to the data file with write permisions
            with open("/Users/emre/Documents/Code/100DaysOfPython/Day11-20/Day20/data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0 #Reset score
        self.update_scoreboard()
    

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

        
