from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score
import time

"""
Every turtle object is 20X20 pixels wide. Therefore square2 is -20 from origin and square3 
is -40 from origin so the 3 squares looking like a snake body
"""
screen = Screen()
screen.bgcolor('Black')
screen.setup(width=600, height=600)
screen.title('Snake Game')
screen.tracer(0)


#creating all the required objects:
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

should_continue = True
while should_continue:
    screen.update()
    time.sleep(0.1)
    snake.move()
    """
    To detect collision of snake head with food and then extend the snake body
    """
    if snake.head.distance(food) < 25:      #if food comes within 25 pixels of snake head then collision detected
        food.refresh_food()
        snake.extend()
        score.increase()
    """
    To detect collision with wall
    """
    if snake.head.xcor() > 295 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -295:
        """
        if the snake head goes closer than 10 pixels to the wall, then snake head has collided with wall
        so game should then end
        """
        should_continue = False
        score.game_over()

    """
    To detect collision with tail
    """
    """
    if the first if block not mentioned then game stops immediately as 
    snake head is the first element to be iterated through and distance 
    between itself is less than 10 pixels. So snake.segments[1:] will slice all the 
    segments in snake except the snake head
    """
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            should_continue = False
            score.game_over()


screen.exitonclick()