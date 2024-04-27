import turtle
wn = turtle.Screen()
Olympia = turtle.Turtle()
Olympia.shape("turtle")
Olympia.width(10)

Olympia.color("blue")
Olympia.penup()
Olympia.goto(-225,-25)
Olympia.pendown()
Olympia.circle(100)

Olympia.color("black")
Olympia.penup()
Olympia.goto(0,-25)
Olympia.pendown()
Olympia.circle(100)

Olympia.color("red")
Olympia.penup()
Olympia.goto(225,-25)
Olympia.pendown()
Olympia.circle(100)

Olympia.color("yellow")
Olympia.penup()
Olympia.goto(-122,-125)
Olympia.pendown()
Olympia.circle(100)

Olympia.color("green")
Olympia.penup()
Olympia.goto(122,-125)
Olympia.pendown()
Olympia.circle(100)

wn.exitonclick()

