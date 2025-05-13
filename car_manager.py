from turtle import Turtle
import random
from random import choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.move_dist = STARTING_MOVE_DISTANCE
        self.cars = []
        self.cars_to_create = 2
        self.create_cars(random.randint(1,self.cars_to_create))
        self.cycle = 0
        self.create_on_cycle = 15
        
    
    def move(self):
        for car in self.cars:
            new_x = car.xcor() - self.move_dist
            car.goto(new_x, car.ycor())
            
            if car.xcor() <= -280:
                car.hideturtle()
                self.cars.remove(car)
                car = None
        if self.cycle >= self.create_on_cycle:
            self.create_cars(random.randint(1,self.cars_to_create))
            self.cycle = 0
        self.cycle += 1 



    def create_cars(self, num_cars):
        for _ in range(num_cars):
            car = Turtle()    
            car.shape("square")
            
            car.shapesize(2,1,None)
            car.color(choice(COLORS))
            #car.hideturtle()
            car.penup()
            car.setheading(270)
            car.setposition(300, random.randint(-250, 250))
            self.cars.append(car)

    def level_up(self):
        self.cars_to_create += 1
        if self.create_on_cycle != 0:
            self.create_on_cycle -= 1

    def clear_cars(self):
        for car in self.cars:
            car.setpos(650,650)
            car.hideturtle()
            




        
