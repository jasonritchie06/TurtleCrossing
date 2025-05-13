from turtle import Turtle
from random import choice

LG_FONT = ("Courier", 24, "bold")
MD_FONT = ("Courier", 18, "normal")
SM_FONT = ("Courier", 14, "normal")

class Intro(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()


    def show(self):
        colors = ["red", "green", "blue", "purple", "dark gray", "cyan", "magenta"]
        name = "T U R T L E  C R O S S I N G"
        by = "Jason Ritchie"
        controls = "Controls: Up/Down Arrow"
        
        x_pos = -268
        for char in name:
            self.setposition(x_pos, 200)
            self.color(choice(colors))
            self.write(char,False,align="Center", font=LG_FONT)
            x_pos += 20
        
            self.setposition(0, 30)
            self.color("blue")
            self.write("by",False,align="Center", font=MD_FONT)

            self.setposition(0, 0)
            self.color("blue")
            self.write(by,False,align="Center", font=MD_FONT)

            self.setposition(0, -230)
            self.color("blue")
            self.write(controls,False,align="Center", font=MD_FONT)


    def un_show(self):
        self.clear()