from operator import truediv
from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# screen setup
screen = Screen()
screen.tracer(0)
screen.setup(width=600,height=600)
screen.title("Turtle Crossing Game")

tim = Player()
car_manager = CarManager()
level = Scoreboard()

screen.listen()
screen.onkey(tim.up,"Up")
screen.onkey(tim.down,"Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # create a new car, make it move
    car_manager.create_cars()
    car_manager.move_cars()

    # detect turtle collision with car
    for car in car_manager.all_cars:
        if car.distance(tim) < 20:
            game_is_on = False
            level.game_over()

    # detect turtle reaching finishing line
    if tim.is_at_goal():
        tim.reset_position()
        car_manager.level_up()

        
screen.exitonclick()