import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager:

    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

        

    def making_car(self):
        rand_num = random.randint(1, 6)
        if rand_num == 1 :
            self.car = Turtle()
            self.car.shape("square")
            self.car.color(COLORS[random.randint(0, 5)])
            self.car.shapesize(stretch_len=3)
            self.car.penup()
            self.car.goto(x=300, y=random.randint(-250, 270))
            self.car_list.append(self.car)

    def move(self):
        for i in self.car_list:
            i.setheading(180)
            i.forward(self.car_speed)

    def next_level(self):
        self.car_speed += MOVE_INCREMENT