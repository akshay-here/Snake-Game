"""
score is subclass
Turtle is super class
"""

from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        """
        Make turtle object white so text can be visible else it is black by default
        Turtle object is hidden so default arrow should not be seen
        then turtle object has to go to top of the screen (0, 270) but pen must also be lifted up
        """
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align='center', font=("Arial", 15, "normal"))

    def game_over(self):
        self.home()
        """
        turtle object goes to origin because of home()
        GAME OVER printed at origin before screen is cleared in increase() function 
        so can see the score once GAME OVER is printed
        """
        self.write("GAME OVER", align='center', font=("Arial", 20, "normal"))

    def increase(self):
        self.score += 1
        self.clear()        #so that score is cleared everytime and not overwritten on top every time
        self.update_score()