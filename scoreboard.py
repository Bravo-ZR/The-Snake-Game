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
        self.write(f"Score: {self.score}", False, 'Center',('Arial', 10, 'bold'))
        
    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, ALIGNMENT ,FONT)
       
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", False, ALIGNMENT, FONT)    
          