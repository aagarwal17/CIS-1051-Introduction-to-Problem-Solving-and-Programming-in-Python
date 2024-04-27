import turtle
wn = turtle.Screen()
wn.bgcolor("silver")
koopa = turtle.Turtle()
koopa.shape("turtle")
koopa.penup()

colors = ["red", "orange", "yellow", "gold", "lightgreen", "green", "cyan", "lightblue", "darkblue", "purple", "pink"]
for color in colors:
    print(color)
    koopa.color(color)
    koopa.forward(80)
    koopa.pendown()
    koopa.forward(15)
    koopa.penup()
    koopa.forward(15)
    koopa.stamp()
    koopa.forward(-110)
    koopa.right(30)
    
koopa.color("maroon")
koopa.forward(80)
koopa.pendown()
koopa.forward(15)
koopa.penup()
koopa.forward(15)
koopa.stamp()
    
wn.exitonclick()
