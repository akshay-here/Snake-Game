from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
"""
starting positions of each of the segments of snake body
each turtle object is 20X20 pixels
"""
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
"""
checking in up, down, left and right functions so that snake cannot back on itself
"""


class Snake:

    def __init__(self):
        self.segments = []      #list which will contain all the snake segments
        self.create_snake()
        self.head = self.segments[0]        #snake head object made

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.color('White')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    """
    create_snake and add_segment used to create the snake and make it 3 squares long
    extend used to extend body of snake by one square. It takes the position of the last most segment[-1]
    and then gets added at the end using add_segment function
    """

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        """
        Snake segments such that 3rd/last segment will follow (3-1) = 2nd segment and 2nd segment will
        follow (2-1) = 1st segment. So snake motion will be clearer if following segment becomes same coordinates
         as the previous segment
        """
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)