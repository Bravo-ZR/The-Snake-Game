from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 10, 'bold')
COLOR = 'CadetBlue1'

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.goto(0,280)
        self.color(COLOR)
        self.hideturtle()
        self.score = 0
        self.highscore = self.check_high_score()
        self.write(f"Score: {self.score} High Score:{self.highscore}", False, 'Center',('Arial', 10, 'bold'))
        
    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} High Score:{self.highscore}", False, ALIGNMENT ,FONT)
       
   # def game_over(self):
    #    self.goto(0,0)
    #    self.write("Game Over!", False, ALIGNMENT, FONT)    
            
    def reset(self):
        self.clear()
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.write(f"Score: {self.score} High Score:{self.highscore}", False, ALIGNMENT ,FONT)
        file = open("highscore.txt", mode='w+')
        file.write(str(self.highscore))
        file.close()
        
    def check_high_score(self):
        try:
            file = open("highscore.txt", mode="w+")
            contents = file.read()
            file.close()

            contents = int(contents)
            return contents
        except ValueError:
            value = 0
            return value

