from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player:

    def __init__(self):
        self.asghar = Turtle()
        self.asghar.shape("turtle")
        self.asghar.color("black")
        self.asghar.penup()
        self.asghar.goto(STARTING_POSITION)
        self.asghar.left(90)

    def moving_forward(self):
        self.asghar.forward(MOVE_DISTANCE)


    def success(self):
        if self.asghar.ycor() == 280 :
            self.asghar.goto(STARTING_POSITION)
            return True
        else:
            return False


