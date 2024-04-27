import turtle
wn = turtle.Screen()
wn.bgcolor("blue")
mikey = turtle.Turtle()
mikey.shape("turtle")
mikey.pensize(8)
mikey.speed(4)
mikey.color("white")

n = int(input("Type the number of sides you want:"))

for i in range(n):
    angle = 360//n
    mikey.forward(100)
    mikey.left(angle)
