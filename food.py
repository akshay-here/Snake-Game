"""
Food class inheriting from the Turtle class
"""
from turtle import Turtle
import random


class Food(Turtle):
    """
    Turtle is the super class and Food is the subclass
    """
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()        #so that each time food spawned doesn't draw line from origin

        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        #making the turtle object(circle) smaller by half. So instead of 20X20, it's now 10X10 pixels wide

        self.color('Blue')
        self.speed(0)       #fastest speed
        self.refresh_food()

    def refresh_food(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        """
        coordinates have to be random for food to be spawned in random locations
        from (-280, 280) as now food object is 10X10 pixels wide so should be fully visible in the screen
        """
        self.goto(rand_x, rand_y)