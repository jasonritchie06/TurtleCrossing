from turtle import Turtle
import time

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.hideturtle()
        self.reset()
        self.setheading(90)
        self.speed("fastest")

    def reset(self):
        self.clear()
        self.setposition(STARTING_POSITION)
        self.showturtle()
    
    def move_forward(self):
        self.setheading(90)
        new_y = self.ycor() + MOVE_DISTANCE
        self.setposition(self.xcor(), new_y)

    def move_backward(self):
        if not self.ycor() <= -280:
            self.setheading(-90)
            new_y = self.ycor() - MOVE_DISTANCE
            self.setposition(self.xcor(), new_y)

        else:
            self.setheading(90)

    def hit(self):
        self.reset()

