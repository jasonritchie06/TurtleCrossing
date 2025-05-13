import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from intro import Intro

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
intro = Intro()
intro.show()
screen.update()
time.sleep(5)
intro.un_show()
screen.update()
player  = Player()
score = Scoreboard()
cars = CarManager()

sleep_time = 0.1
game_is_on = True

screen.listen()

screen.onkey(player.move_forward, "Up")
screen.onkey(player.move_backward, "Down")
#screen.onkey(cars.level_up, "l")

def screen_hit():
    screen.bgcolor("yellow")
    player.color("red")
    player.shape("circle")
    screen.update()
    time.sleep(.25)
    screen.bgcolor("white")
    player.shape("turtle")
    player.color("green")
    screen.update()

def game_over():
    cars.clear_cars()
    score.game_over()
    screen.update()


while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    if player.ycor() >= 280:
        score.scored()
        cars.level_up()
        player.reset()
        new_sleep = sleep_time * .8
        if new_sleep != 0:
            sleep_time = new_sleep
    cars.move()

    for car in cars.cars:
        if player.distance(car) <= 20:
            if score.lives == 1:
                score.hit()
                screen_hit()
                game_is_on = False

            else:
                screen_hit()
                player.hit()
                score.hit()
                

game_over()


screen.exitonclick()