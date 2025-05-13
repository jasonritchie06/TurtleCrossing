from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.level = 1
        self.lives = 3
        self.update_score()

    def update_score(self):
        self.clear()
        self.setposition(-205,260)
        self.write(f"Level: {self.level}",False,align="center", font=FONT)
        self.setposition(0,260)
        self.write(f"Score: {self.score}",False,align="center", font=FONT)
        self.setposition(205,260)
        self.write(f"Lives: {self.lives}",False,align="center", font=FONT)
        #self.update()

    def scored(self):
        self.score += 10
        self.level += 1
        self.update_score()

    def hit(self):
          self.lives -= 1
          self.update_score()

    def game_over(self):
                self.setposition(0,0)
                self.color("red")
                self.write("G a m e  O v e r",False,align="center", font=("Courier", 24, "bold"))
