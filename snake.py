"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *
import random
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    #Low chance for food to move just one segment in a random direction.
    if randrange(20) == 0:
        food.x += randrange(-10, 11, 10)
        food.y += randrange(-10, 11, 10)

    #Ensures the food stays within the boundaries.
    food.x = min(max(food.x, -200), 190)
    food.y = min(max(food.y, -200), 190)

    clear()

    for body in snake:
        square(body.x, body.y, 9,snakeColor )

    square(food.x, food.y, 9, appleColor)
    
    update()
    ontimer(move, 100)


"""Choose a random color to the snake and the food"""
colors = ['blue','orange','green','black']
snakeColor = random.choice(colors)
colors.remove(snakeColor)
appleColor = random.choice(colors)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
