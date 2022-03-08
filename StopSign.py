import math
import turtle

#Named constants
WINDOW_WIDTH=400
WINDOW_HEIGHT=400
ANIMATION_SPEED=0
NUM_SIDES=8
LENGTH=100
ANGLE=45
TEXT_X=-5
TEXT_Y=-10

#Size the window
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
s=LENGTH

x=s/math.sqrt(2)
diameter=s+(2*x)
turtle.speed(ANIMATION_SPEED)
turtle.pendown

for x in range(0,8):
    turtle.forward(100)
    turtle.right(45)
turtle.penup()
turtle.right(90)
turtle.forward(120)
turtle.left(90)
turtle.forward(35)
turtle.write('Stop')
    
