import turtle # Create a screen
from turtle import color # Create a turtle object and call the functions
import random # Create random colors and speeds
t = turtle.Turtle() # Create a list of colors and speeds
t = turtle.Turtle()  #another turtle game on
color = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "black", "white", "brown", "grey", "cyan", "magenta"]  # Create a list of colors and speeds
speed = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Create a list of shapes 
def draw_square():  #another turtle game on
    t.forward(100) # forward 100 pixels
    t.right(90) # turn right 90 degrees
    for i in range(4): # repeat 4 times
        t.forward(360)        # forward 360 pixels
        t.right(90) # turn right 90 degrees                                     
        t.forward(360) # forward 360 pixels
        t.circle(radius=100, extent=90)
        t = turtle.Turtle() # turtle 
        t.color(random.choice(color))
for i in range(100):                # Draw 100 shapes
    t.pencolor(random.choice(color)) # Pick a random color
    t.pensize(random.randint(1, 10))
    t.speed(random.choice(speed))
    t.forward(100)
    t.right(30)           # Turn right 30 degrees
    t.forward(20)
    t.left(60)
    t.forward(100)       
    t.right(50)
    t.penup()
    t.setposition(10, -10)     # Move the pen to a new position
    t.pendown()                # Draw a line
def draw_circle():               # Draw other continuous objects 
    t.color(random.choice(color))
    t.speed(random.choice(speed))
    t.circle(100)
for i in range(36):
    t.right(10)

def draw_triangle():                 # Draw other continuous objects for the future
    t.color(random.choice(color))
    t.speed(random.choice(speed))
    for i in range(3):              
        t.forward(100)
        t.left(120)
turtle.done()                          # turtle