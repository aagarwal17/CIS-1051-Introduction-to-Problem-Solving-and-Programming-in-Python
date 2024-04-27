import turtle
import random

wn = turtle.Screen()
bob = turtle.Turtle()
wn.setworldcoordinates(-1,-1,-1,-1)


bob.penup()
bob.tracer(1000,25)
bob.color("blue")
          
for _ in range (10000):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    d = math.sqrt(x**2 + y**2)
    if d <= 1:
        bob.color("red")
    else:
        bob.color("blue")
    bob.goto(x, y)
    bob.stamp
    
